import base64
import copy
import json
import logging
import typing

import googleapiclient
import googleapiclient.errors
import googleapiclient.discovery

import cfg_mgmt
import cfg_mgmt.model as cmm
import ci.log
import ci.util
import model
import model.base
import model.container_registry
import model.gcp


ci.log.configure_default_logging()
logger = logging.getLogger(__name__)

GcpServiceAccount = model.container_registry.ContainerRegistryConfig | model.gcp.GcpServiceAccount


def qualified_service_account_name(
    service_account_name: str,
    project_id: str = '-',
) -> str:
    return f'projects/{project_id}/serviceAccounts/{service_account_name}'


def qualified_service_account_key_name(
    service_account_name: str,
    key_name: str,
    project_id: str = '-',
) -> str:
    base_name = qualified_service_account_name(
        service_account_name=service_account_name,
        project_id=project_id,
    )
    return f'{base_name}/keys/{key_name}'


def create_iam_client(
    cfg_element: model.container_registry.ContainerRegistryConfig | model.gcp.GcpServiceAccount,
) -> googleapiclient.discovery.Resource:
    if isinstance(cfg_element, model.container_registry.ContainerRegistryConfig):
        credentials = cfg_element.credentials().service_account_credentials()
    elif isinstance(cfg_element, model.gcp.GcpServiceAccount):
        credentials = cfg_element.service_account_credentials()
    else:
        raise NotImplementedError

    return googleapiclient.discovery.build(
        serviceName='iam',
        version='v1',
        credentials=credentials,
    )


def _create_service_account_key(
    iam_client: googleapiclient.discovery.Resource,
    service_account_name: str,
) -> dict:
    '''
    Creates a key for a service account.
    '''

    key_request = iam_client.projects().serviceAccounts().keys().create(
        name=service_account_name,
        body={},
    )
    try:
        key = key_request.execute()
    except googleapiclient.errors.HttpError as e:
        logger.error('unable to create key')
        raise e

    logger.info('Created key: ' + key['name'])
    return json.loads(base64.b64decode(key['privateKeyData']))


def delete_service_account_key(
    iam_client: googleapiclient.discovery.Resource,
    service_account_key_name: str,
):
    try:
        iam_client.projects().serviceAccounts().keys().delete(
            name=service_account_key_name,
        ).execute()
        logger.info('Deleted key: ' + service_account_key_name)

    except googleapiclient.errors.HttpError as e:
        if not e.status_code == 404:
            raise

        logger.warning(f'{service_account_key_name=} not found, will remove entry from config queue')


def rotation_cfg_or_none(
    gcp_cfg: GcpServiceAccount,
    cfg_factory: model.ConfigFactory,
):
    if (rotation_cfg_reference := gcp_cfg.rotation_cfg()):
        return cfg_factory.resolve_cfg_element_reference(
            cfg_element_reference=rotation_cfg_reference,
        )

    return None


def rotate_cfg_element(
    cfg_element: GcpServiceAccount,
    cfg_factory: model.ConfigFactory,
) ->  typing.Tuple[cfg_mgmt.revert_function, dict, model.NamedModelElement]:
    rotation_cfg = rotation_cfg_or_none(
        gcp_cfg=cfg_element,
        cfg_factory=cfg_factory,
    ) or cfg_element

    logger.info(f'using {rotation_cfg.name()=} for rotation')

    client_email = cfg_element.client_email()

    iam_client = create_iam_client(
        cfg_element=rotation_cfg,
    )

    service_account_name = qualified_service_account_name(
        client_email,
    )

    old_key_id = cfg_element.private_key_id()
    old_key_id = qualified_service_account_key_name(
        service_account_name=client_email,
        key_name=old_key_id,
    )

    new_key = _create_service_account_key(
        iam_client=iam_client,
        service_account_name=service_account_name,
    )

    raw_cfg = copy.deepcopy(cfg_element.raw)

    if isinstance(cfg_element, model.container_registry.ContainerRegistryConfig):
        raw_cfg['password'] = json.dumps(new_key)
    elif isinstance(cfg_element, model.gcp.GcpServiceAccount):
        raw_cfg['service_account_key'] = new_key
    else:
        raise ValueError(cfg_element)

    updated_elem = type(cfg_element)(
        # checked for correct type already
        name=cfg_element.name(),
        raw_dict=raw_cfg,
        type_name=cfg_element._type_name,
    )

    secret_id = {'gcp_secret_key': old_key_id}

    def revert():
        delete_service_account_key(
            iam_client=iam_client,
            service_account_key_name=qualified_service_account_key_name(
                service_account_name=client_email,
                key_name=new_key['private_key_id'],
            )
        )

    return revert, secret_id, updated_elem


def delete_config_secret(
    cfg_element: GcpServiceAccount,
    cfg_queue_entry: cmm.CfgQueueEntry,
    cfg_factory: model.ConfigFactory,
) -> GcpServiceAccount | None:
    rotation_cfg = rotation_cfg_or_none(
        gcp_cfg=cfg_element,
        cfg_factory=cfg_factory,
    ) or cfg_element

    logger.info(f'using {rotation_cfg.name()=} for deletion')

    logger.info('deleting old gcr secret')
    iam_client = create_iam_client(
        cfg_element=rotation_cfg,
    )
    delete_service_account_key(
        iam_client=iam_client,
        service_account_key_name=cfg_queue_entry.secretId['gcp_secret_key'],
    )
    return None
