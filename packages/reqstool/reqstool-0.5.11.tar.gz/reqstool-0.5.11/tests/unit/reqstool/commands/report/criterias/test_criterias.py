# Copyright © LFV

from reqstool_python_decorators.decorators.decorators import SVCs

from reqstool.commands.report.criterias.group_by import GroupbyOptions, GroupByOrganizor
from reqstool.commands.report.criterias.sort_by import SortByOptions
from reqstool.common.validator_error_holder import ValidationErrorHolder
from reqstool.common.validators.semantic_validator import SemanticValidator
from reqstool.locations.local_location import LocalLocation
from reqstool.model_generators.combined_indexed_dataset_generator import CombinedIndexedDatasetGenerator
from reqstool.model_generators.combined_raw_datasets_generator import CombinedRawDatasetsGenerator
from reqstool.models.raw_datasets import CombinedRawDataset


@SVCs("SVC_034")
def test_basic_baseline(resource_funcname_rootdir, local_testdata_resources_rootdir_w_path):
    semantic_validator = SemanticValidator(validation_error_holder=ValidationErrorHolder())
    crd: CombinedRawDataset = CombinedRawDatasetsGenerator(
        initial_location=LocalLocation(path=local_testdata_resources_rootdir_w_path("test_basic/baseline/ms-101")),
        semantic_validator=semantic_validator,
    ).combined_raw_datasets

    cid = CombinedIndexedDatasetGenerator(_crd=crd).combined_indexed_dataset

    gbc = GroupByOrganizor(
        cid=cid,
        group_by=GroupbyOptions.INITIAL_IMPORTS,
        sort_by=[SortByOptions.ID, SortByOptions.REVISION, SortByOptions.SIGNIFICANCE],
    )

    for key, value in gbc:
        print(f"{key}: {[cid.requirements[urn_id]for urn_id in value]}")

    assert gbc is not None
