from collections.abc import Iterable
from uuid import UUID

from mitm_tooling.representation import Header
from .asset_bundles.asset_bundles import SupersetDatasourceBundle, \
    SupersetVisualizationBundle, SupersetMitMDatasetBundle
from .common import DBConnectionInfo
from .definitions import DatasourceIdentifierMap
from .definitions.mitm_dataset import MitMDatasetIdentifier
from .from_intermediate import header_into_superset_datasource_bundle, header_into_mitm_dataset_bundle
from .visualizations.registry import VisualizationType, mk_visualization


def mk_superset_datasource_bundle(header: Header, db_conn_info: DBConnectionInfo, database_uuid: UUID | None = None,
                                  ds_id_map: DatasourceIdentifierMap | None = None) -> SupersetDatasourceBundle:
    return header_into_superset_datasource_bundle(header,
                                                  db_conn_info,
                                                  database_uuid=database_uuid,
                                                  ds_id_map=ds_id_map)


def mk_superset_visualization_bundle(header: Header,
                                     mitm_dataset_identifier: MitMDatasetIdentifier,
                                     ds_id_map: DatasourceIdentifierMap,
                                     visualization_types: Iterable[
                                         VisualizationType]) -> SupersetVisualizationBundle:
    return SupersetVisualizationBundle.combine(*(
        mk_visualization(vzt, header, mitm_dataset_identifier, ds_id_map) for vzt
        in set(visualization_types)
    ))


def mk_superset_mitm_dataset_bundle(header: Header,
                                    db_conn_info: DBConnectionInfo,
                                    mitm_dataset_identifier: MitMDatasetIdentifier,
                                    database_uuid: UUID | None = None,
                                    ds_id_map: DatasourceIdentifierMap | None = None,
                                    visualization_types: Iterable[
                                                             VisualizationType] | None = None) -> SupersetMitMDatasetBundle:
    mitm_dataset_bundle = header_into_mitm_dataset_bundle(header,
                                                          db_conn_info,
                                                          mitm_dataset_identifier,
                                                          database_uuid=database_uuid,
                                                          ds_id_map=ds_id_map)
    if visualization_types is not None:
        mdi = mitm_dataset_bundle.mitm_dataset.identifier
        ds_id_map = mitm_dataset_bundle.datasource_bundle.placeholder_dataset_identifiers
        mitm_dataset_bundle = mitm_dataset_bundle.with_visualization_bundle(
            mk_superset_visualization_bundle(header, mdi, ds_id_map, visualization_types))

    return mitm_dataset_bundle
