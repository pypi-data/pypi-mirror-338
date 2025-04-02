from unittest.mock import patch

from mx_bluesky.beamlines.i24.serial.write_nexus import call_nexgen


@patch("mx_bluesky.beamlines.i24.serial.write_nexus.bps.sleep")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.SSX_LOGGER")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.caget")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.cagetstring")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.pathlib.Path.read_text")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.pathlib.Path.exists")
def test_call_nexgen_for_extruder(
    fake_path,
    fake_read_text,
    fake_caget_str,
    fake_caget,
    fake_log,
    sleep,
    dummy_params_ex,
    RE,
):
    fake_caget_str.return_value = f"{dummy_params_ex.filename}_5001"
    fake_caget.return_value = 32
    fake_path.return_value = True
    fake_read_text.return_value = ""
    with patch("mx_bluesky.beamlines.i24.serial.write_nexus.requests") as patch_request:
        RE(call_nexgen(None, dummy_params_ex, 0.6, (1000, 1200)))
        patch_request.post.assert_called_once()

    assert patch_request.post.call_args.kwargs["json"]["expt_type"] == "extruder"


@patch("mx_bluesky.beamlines.i24.serial.write_nexus.bps.sleep")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.SSX_LOGGER")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.caget")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.cagetstring")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.pathlib.Path.read_text")
@patch("mx_bluesky.beamlines.i24.serial.write_nexus.pathlib.Path.exists")
def test_call_nexgen_for_fixed_target(
    fake_path,
    fake_read_text,
    fake_caget_str,
    fake_caget,
    fake_log,
    sleep,
    dummy_params_without_pp,
    RE,
):
    expected_filename = f"{dummy_params_without_pp.filename}_5002"
    fake_caget_str.return_value = expected_filename
    fake_caget.return_value = 32
    fake_path.return_value = True
    fake_read_text.return_value = ""
    with patch("mx_bluesky.beamlines.i24.serial.write_nexus.requests") as patch_request:
        RE(call_nexgen(None, dummy_params_without_pp, 0.6, (1000, 1200)))
        patch_request.post.assert_called_once()

    assert patch_request.post.call_args.kwargs["json"]["expt_type"] == "fixed-target"
    assert patch_request.post.call_args.kwargs["json"]["filename"] == expected_filename
