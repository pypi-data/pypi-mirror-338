from .._client import get_default_client
from ..enum.vis_enums import EntityType
from typing import TYPE_CHECKING

import luminarycloud._proto.api.v0.luminarycloud.vis.vis_pb2 as vispb

if TYPE_CHECKING:
    from .visualization import Scene, LookAtCamera
    import requests

try:
    # we need requests for downloading render data
    import requests
    import luminarycloud_jupyter as lcj
except ImportError:
    lcj = None


class InteractiveScene:
    """
    The InteractiveScene acts as the bridge between the the Scene and
    the Jupyter widget, handling checking if we have the widget package
    before passing calls to the widget to handle it being an optional
    dependency
    """

    # Using the type causes a circular import error, not sure on best way to resolve.
    # I do want to keep this in a separate file
    def __init__(self, scene: "Scene") -> None:
        if not lcj or not requests:
            raise ImportError("InteractiveScene requires luminarycloud[jupyter] to be installed")
        # TODO (will): not sure on how to suppress the unbound var warnings from pyright
        # but we won't have this be unbound b/c of the decorator check
        self.widget = lcj.LCVisWidget()

        # Display the initial scene we've been given
        # Submit request for the render data URLs we need
        req = vispb.GetRenderDataUrlsRequest()
        req.project_id = scene._project_id
        if scene._entity_type == EntityType.SIMULATION:
            req.entity.simulation.id = scene._solution.simulation_id
            req.entity.simulation.solution_id = scene._solution.id
        elif scene._entity_type == EntityType.MESH:
            req.entity.mesh.id = scene._mesh.id
        elif scene._entity_type == EntityType.GEOMETRY:
            req.entity.geometry.id = scene._geometry.id
        else:
            # Should never hit b/c the Scene would have complained already
            raise TypeError(
                f"Expected Solution, Mesh or Geometry in Scene, got {scene._entity_type}"
            )

        # TODO later make this a separate method to load the scene URLs
        # TODO: would be nice to report filter execution progress
        resp = get_default_client().GetRenderDataUrls(req)

        # TODO: would be nice to print/report some download progress info
        render_data = requests.get(resp.urls.data_files[0].signed_url)
        self.widget.data = render_data.content

    def _ipython_display_(self) -> None:
        """
        When the InteractiveScene is shown in Jupyter we show the underlying widget
        to run the widget's frontend code
        """
        self.widget._ipython_display_()

    def set_surface_visibility(self, surface_id: str, visible: bool) -> None:
        self.widget.set_surface_visibility(surface_id, visible)

    def set_surface_color(self, surface_id: str, color: list[float]) -> None:
        self.widget.set_surface_color(surface_id, color)

    def reset_camera(self) -> None:
        self.widget.reset_camera()

    def get_camera(self) -> "LookAtCamera":
        # Import here to avoid circular import issue
        from .visualization import LookAtCamera

        camera = LookAtCamera()
        camera.position = self.widget.camera_position
        camera.look_at = self.widget.camera_look_at
        camera.up = self.widget.camera_up
        return camera
