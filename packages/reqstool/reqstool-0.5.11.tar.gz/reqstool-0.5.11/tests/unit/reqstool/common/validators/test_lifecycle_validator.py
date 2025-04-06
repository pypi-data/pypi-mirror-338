# Copyright © LFV

import pytest
from reqstool.common.validator_error_holder import ValidationErrorHolder
from reqstool.common.validators.lifecycle_validator import LifecycleValidator
from reqstool.common.validators.semantic_validator import SemanticValidator
from reqstool.locations.local_location import LocalLocation
from reqstool.model_generators.combined_indexed_dataset_generator import CombinedIndexedDatasetGenerator
from reqstool.model_generators.combined_raw_datasets_generator import CombinedRawDatasetsGenerator
from reqstool.models.raw_datasets import CombinedRawDataset
from reqstool_python_decorators.decorators.decorators import SVCs


@pytest.fixture
def combined_indexed_dataset(local_testdata_resources_rootdir_w_path):
    semantic_validator = SemanticValidator(validation_error_holder=ValidationErrorHolder())
    crd: CombinedRawDataset = CombinedRawDatasetsGenerator(
        initial_location=LocalLocation(path=local_testdata_resources_rootdir_w_path("test_basic/lifecycle/ms-101")),
        semantic_validator=semantic_validator,
    ).combined_raw_datasets

    return CombinedIndexedDatasetGenerator(_crd=crd).combined_indexed_dataset


@SVCs("SVC_038")
def test_defunct_states(combined_indexed_dataset, caplog):

    LifecycleValidator(combined_indexed_dataset)

    assert "Urn ms-101:SVC_102 is used in an annotation despite being obsolete." in caplog.text
    assert (
        "The requirement ms-101:REQ_203 is marked as obsolete but the SVCs ms-101:SVC_202, ms-101:SVC_203 references it."
        in caplog.text
    )
    assert "Urn ms-101:REQ_101 is used in an annotation despite being deprecated." in caplog.text
    assert "Urn ms-101:SVC_101 is used in an annotation despite being deprecated." in caplog.text


@SVCs("SVC_038")
def test_active_states(combined_indexed_dataset, caplog):

    LifecycleValidator(combined_indexed_dataset)

    assert "The SVC ms-101:SVC_202 is marked as effective but the MVR ms-101:MVR_202 references it." not in caplog.text
    assert "Urn ms-101:REQ_201 is used in an annotation despite being draft." not in caplog.text
    assert "The SVC ms-101:SVC_201 is marked as draft but the MVR ms-101:MVR_201 references it." not in caplog.text


@SVCs("SVC_038")
def test_invalid_schema(local_testdata_resources_rootdir_w_path, caplog):
    with pytest.raises(SystemExit) as excinfo:
        semantic_validator = SemanticValidator(validation_error_holder=ValidationErrorHolder())
        CombinedRawDatasetsGenerator(
            initial_location=LocalLocation(
                path=local_testdata_resources_rootdir_w_path("test_basic/lifecycle/validation_error")
            ),
            semantic_validator=semantic_validator,
        ).combined_raw_datasets

    assert excinfo.type == SystemExit
    # 128 schema validation error
    assert str(excinfo.value) == "128"
    assert "'reason' is a required property" in caplog.text
