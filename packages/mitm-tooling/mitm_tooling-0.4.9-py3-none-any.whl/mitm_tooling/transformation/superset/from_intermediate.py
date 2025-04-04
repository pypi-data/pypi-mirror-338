from uuid import UUID

from mitm_tooling.representation import Header
from .asset_bundles.asset_bundles import SupersetDatasourceBundle, \
    SupersetMitMDatasetBundle
from .common import DBConnectionInfo
from .definitions import DatasourceIdentifierMap
from .definitions.mitm_dataset import MitMDatasetIdentifier


def header_into_superset_datasource_bundle(header: Header,
                                           db_conn_info: DBConnectionInfo,
                                           database_uuid: UUID | None = None,
                                           ds_id_map: DatasourceIdentifierMap | None = None) -> SupersetDatasourceBundle:
    from ..sql.from_intermediate import header_into_db_meta
    from .from_sql import db_meta_into_superset_datasource_bundle
    db_meta = header_into_db_meta(header)
    return db_meta_into_superset_datasource_bundle(db_meta,
                                                   db_conn_info,
                                                   database_uuid=database_uuid,
                                                   ds_id_map=ds_id_map)


def header_into_mitm_dataset_bundle(header: Header,
                                    db_conn_info: DBConnectionInfo,
                                    dataset_identifier: MitMDatasetIdentifier,
                                    database_uuid: UUID | None = None,
                                    ds_id_map: DatasourceIdentifierMap | None = None) -> SupersetMitMDatasetBundle:
    from ..sql.from_intermediate import header_into_db_meta
    from .from_sql import db_meta_into_mitm_dataset_bundle
    db_meta = header_into_db_meta(header)
    return db_meta_into_mitm_dataset_bundle(db_meta,
                                            db_conn_info,
                                            dataset_identifier,
                                            header.mitm,
                                            database_uuid=database_uuid,
                                            ds_id_map=ds_id_map)
