import pytest

from mx_bluesky.hyperion.parameters.constants import CONST


@pytest.fixture
def test_rotation_start_outer_document(dummy_rotation_params):
    return {
        "uid": "d8bee3ee-f614-4e7a-a516-25d6b9e87ef3",
        "subplan_name": CONST.PLAN.ROTATION_OUTER,
        "mx_bluesky_parameters": dummy_rotation_params.model_dump_json(),
    }
