import re

from dodal.devices.oav.snapshots.snapshot_image_processing import (
    compute_beam_centre_pixel_xy_for_mm_position,
    draw_crosshair,
)
from event_model import Event, EventDescriptor, RunStart
from PIL import Image

from mx_bluesky.common.external_interaction.callbacks.common.plan_reactive_callback import (
    PlanReactiveCallback,
)
from mx_bluesky.common.parameters.constants import DocDescriptorNames
from mx_bluesky.common.utils.log import ISPYB_ZOCALO_CALLBACK_LOGGER as CALLBACK_LOGGER


class BeamDrawingCallback(PlanReactiveCallback):
    """
    Callback that monitors for OAV_ROTATION_SNAPSHOT_TRIGGERED events and
    draws a crosshair at the beam centre, saving the snapshot to a file.
    The callback assumes an OAV device "oav"
    Examples:
        Take a snapshot at the current location
    >>> from bluesky.run_engine import RunEngine
    >>> import bluesky.preprocessors as bpp
    >>> import bluesky.plan_stubs as bps
    >>> from dodal.devices.oav.oav_detector import OAV
    >>> from mx_bluesky.common.parameters.components import WithSnapshot
    >>> def take_snapshot(params: WithSnapshot, oav: OAV, run_engine: RunEngine):
    ...     run_engine.subscribe(BeamDrawingCallback())
    ...     @bpp.run_decorator(md={
    ...     "activate_callbacks": ["BeamDrawingCallback"],
    ...         "with_snapshot": params.model_dump_json(),
    ...     })
    ...     def inner_plan():
    ...         yield from bps.abs_set(oav.snapshot.directory, "/path/to/snapshot_folder", wait=True)
    ...         yield from bps.abs_set(oav.snapshot.filename, "my_snapshot_prefix", wait=True)
    ...         yield from bps.trigger(oav.snapshot, wait=True)
    ...         yield from bps.create(DocDescriptorNames.OAV_ROTATION_SNAPSHOT_TRIGGERED)
    ...         yield from bps.read(oav)
    ...         yield from bps.save()
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, log=CALLBACK_LOGGER, **kwargs)
        self._snapshot_files: list[str] = []
        self._microns_per_pixel: tuple[float, float]
        self._beam_centre: tuple[int, int]
        self._rotation_snapshot_descriptor: str = ""

    def activity_gated_start(self, doc: RunStart):
        if self.activity_uid == doc.get("uid"):
            with_snapshot_json = doc.get("with_snapshot")  # type: ignore
            assert with_snapshot_json, (
                "run start event did not have expected snapshot json"
            )
        return doc

    def activity_gated_descriptor(self, doc: EventDescriptor) -> EventDescriptor | None:
        if doc.get("name") == DocDescriptorNames.OAV_ROTATION_SNAPSHOT_TRIGGERED:
            self._rotation_snapshot_descriptor = doc["uid"]
        return doc

    def activity_gated_event(self, doc: Event) -> Event:
        if doc["descriptor"] == self._rotation_snapshot_descriptor:
            self._handle_rotation_snapshot(doc)
        return doc

    def _extract_base_snapshot_params(self, doc: Event):
        data = doc["data"]
        self._snapshot_files.append(data["oav-snapshot-last_saved_path"])
        self._microns_per_pixel = (
            data["oav-microns_per_pixel_x"],
            data["oav-microns_per_pixel_y"],
        )
        self._beam_centre = (data["oav-beam_centre_i"], data["oav-beam_centre_j"])

    def _handle_rotation_snapshot(self, doc: Event):
        self._extract_base_snapshot_params(doc)
        data = doc["data"]
        snapshot_path = data["oav-snapshot-last_saved_path"]
        match = re.match("(.*)\\.png", snapshot_path)
        assert match, f"Snapshot {snapshot_path} was not a .png file"
        snapshot_base = match.groups()[0]
        output_snapshot_path = f"{snapshot_base}_with_beam_centre.png"
        self._generate_snapshot_at(snapshot_path, output_snapshot_path, 0, 0)
        data["oav-snapshot-last_saved_path"] = output_snapshot_path
        return doc

    def _generate_snapshot_at(
        self, input_snapshot_path: str, output_snapshot_path: str, x_mm: int, y_mm: int
    ):
        """
        Save a snapshot to the specified path, with an annotated crosshair at the specified
        position
        Args:
            input_snapshot_path: The non-annotated image path.
            output_snapshot_path:  The path to the image that will be annotated.
            x_mm: Relative x location of the sample to the original image (mm)
            y_mm: Relative y location of the sample to the original image (mm)
        """
        image = Image.open(input_snapshot_path)
        x_px, y_px = compute_beam_centre_pixel_xy_for_mm_position(
            (x_mm, y_mm), self._beam_centre, self._microns_per_pixel
        )
        draw_crosshair(image, x_px, y_px)
        image.save(output_snapshot_path, format="png")
