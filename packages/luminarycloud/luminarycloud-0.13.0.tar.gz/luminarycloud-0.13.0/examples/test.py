import luminarycloud as lc

# This points the client to main
lc.set_default_client(
    lc.Client(
        target="apis.main.int.luminarycloud.com",
        domain="luminarycloud-dev.us.auth0.com",
        client_id="mbM8OSEk5ShoU5iKfzUxSinKluPlxGQ9",
        audience="https://api-dev.luminarycloud.com",
    )
)


def tag(name):
    return f"lcTag/tagContainer/tag/{name}"


project = lc.create_project(name="Test")
geometry = project.create_geometry(
    cad_file_path="/sdk/testdata/cube.cgns",
    wait=True,
)
_, volumes = geometry.list_entities()

s = geometry.select_volumes([])
s.create_shape(
    lc.params.geometry.Sphere(radius=1.0, center=lc.types.Vector3(0, 0, 0)),
)
s.translate(lc.types.Vector3(1, 0, 0))
s.tag("sphere")
s.select(volumes)  # add cube
s.union()
s.clear()

_, volumes = geometry.list_entities()
s.import_cad("/sdk/testdata/cube.cgns")
s.translate(lc.types.Vector3(0, 1, 0))
