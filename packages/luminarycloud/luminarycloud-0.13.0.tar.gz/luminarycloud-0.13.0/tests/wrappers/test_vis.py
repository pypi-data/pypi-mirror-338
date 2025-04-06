# Copyright 2023-2024 Luminary Cloud, Inc. All Rights Reserved.
import pytest
from luminarycloud.types import Vector3
import luminarycloud.vis as vis
from luminarycloud._proto.api.v0.luminarycloud.vis import vis_pb2


def test_slice() -> None:
    slice = vis.Slice("my fancy slice")
    slice.plane.normal = [0, 1, 0]
    slice.plane.origin = [-0.01752500049769878, 0, 0.008750000037252903]
    slice.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    slice.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = slice._to_proto()
    assert isinstance(proto, vis_pb2.Filter)


def test_plane_clip() -> None:
    clip = vis.PlaneClip("my fancy clip")
    clip.plane.normal = [0, 1, 0]
    clip.plane.origin = [-0.01752500049769878, 0, 0.008750000037252903]
    clip.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    clip.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = clip._to_proto()
    assert isinstance(proto, vis_pb2.Filter)


def test_box_clip() -> None:
    clip = vis.BoxClip("my fancy clip")
    clip.box.center = [0, 1, 0]
    clip.box.lengths = [2, 2, 2]
    clip.box.angles = [90, 0, 0]
    clip.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    clip.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = clip._to_proto()
    assert isinstance(proto, vis_pb2.Filter)


def test_fixed_vector_glyph() -> None:
    glyph = vis.FixedSizeVectorGlyphs("my fancy glyph")
    glyph.field.quantity = vis.VisQuantity.VELOCITY
    glyph.size = 0.5
    glyph.sampling_rate = 10
    glyph.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    glyph.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = glyph._to_proto()
    assert isinstance(proto, vis_pb2.Filter)


def test_scaled_vector_glyph() -> None:
    glyph = vis.ScaledVectorGlyphs("my fancy glyph")
    glyph.field.quantity = vis.VisQuantity.VELOCITY
    glyph.scale = 0.5
    glyph.sampling_rate = 10
    glyph.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    glyph.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = glyph._to_proto()
    assert isinstance(proto, vis_pb2.Filter)


def test_threshold() -> None:
    threshold = vis.Threshold("my fancy threshold")
    threshold.field.quantity = vis.VisQuantity.VELOCITY
    threshold.min_value = 10
    threshold.max_value = 15.5
    threshold.display_attrs.field.quantity = vis.VisQuantity.PRESSURE
    threshold.display_attrs.representation = vis.Representation.SURFACE
    proto: vis_pb2.Filter = threshold._to_proto()
    assert isinstance(proto, vis_pb2.Filter)
    with pytest.raises(ValueError):
        threshold.min_value = 1000
        threshold.max_value = 0
        proto2: vis_pb2.Filter = threshold._to_proto()


def test_nested_dataclass() -> None:
    attrs0 = vis.DisplayAttributes()
    attrs0.field.component = vis.FieldComponent.MAGNITUDE
    attrs0.field.quantity = vis.VisQuantity.VELOCITY
    attrs0.representation = vis.Representation.WIREFRAME
    attrs0.visible = False
    attrs1 = vis.DisplayAttributes()
    assert attrs0.field.component != attrs1.field.component
    assert attrs0.field.quantity != attrs1.field.quantity
    assert attrs0.representation != attrs1.representation
    assert attrs0.visible != attrs1.visible
