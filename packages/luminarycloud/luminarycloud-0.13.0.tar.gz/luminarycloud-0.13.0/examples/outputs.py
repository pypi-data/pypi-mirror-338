import luminarycloud as lc
from sdk_util import get_client_for_env
import urllib3

urllib3.disable_warnings()

lc.set_default_client(get_client_for_env(env_name="stopcond"))

project = lc.create_project(name="Outputs Test")
geometry = project.create_geometry(
    cad_file_path="/sdk/testdata/cube.cgns",
    wait=True,
)

setup = project.list_simulation_templates()[
    0
]  # new project, so the only sim template is the default one

all_nodes = setup.list_output_definitions()
residuals = [n for n in all_nodes if isinstance(n, lc.outputs.ResidualOutputDefinition)]

for r in residuals:
    r.include[lc.enum.QuantityType.RESIDUAL_X_MOMENTUM] = False
    r.include[lc.enum.QuantityType.RESIDUAL_Y_MOMENTUM] = False
    r.include[lc.enum.QuantityType.RESIDUAL_Z_MOMENTUM] = False
    setup.update_output_definition(r.id, r)

pressure_drop = setup.create_output_definition(
    lc.outputs.SurfaceAverageOutputDefinition(
        name="Pressure drop",
        quantity=lc.enum.QuantityType.PRESSURE,
        surfaces=["lcTag/tagContainer/tag/bottom"],
        out_surfaces=["lcTag/tagContainer/tag/top"],
        calc_type=lc.enum.CalculationType.DIFFERENCE,
        include=lc.outputs.OutputDefinitionInclusions(
            base_value=True,
            trailing_average=lc.outputs.TrailingAverageConfig(
                averaging_iterations=10,
            ),
            convergence_monitoring=lc.outputs.ConvergenceMonitoringConfig(
                averaging_iterations=10,
                iterations_to_consider=5,
            ),
        ),
    )
)

force = setup.create_output_definition(
    lc.outputs.ForceOutputDefinition(
        name="Lift",
        quantity=lc.enum.QuantityType.LIFT,
        surfaces=["lcTag/tagContainer/tag/bottom"],
        calc_type=lc.enum.CalculationType.AGGREGATE,
        include=lc.outputs.OutputDefinitionInclusions(
            base_value=True,
            coefficient=True,
            trailing_average=lc.outputs.TrailingAverageConfig(
                averaging_iterations=10,
            ),
            convergence_monitoring=lc.outputs.ConvergenceMonitoringConfig(
                averaging_iterations=10,
                iterations_to_consider=5,
            ),
        ),
    )
)

force.include.coefficient = True
force.quantity = lc.enum.QuantityType.PRESSURE
setup.update_output_definition(force.id, force)  # fails: "PRESSURE is not a force quantity type"

setup.delete_output_definition(pressure_drop.id)

setup.get_general_stopping_conditions()
setup.update_general_stopping_conditions(stop_on_any=True)

stopping_conditions = setup.list_stopping_conditions()
for sc in stopping_conditions:
    setup.delete_stopping_condition(sc.id)

lift_sc = setup.create_or_update_stopping_condition(
    output_definition_id=force.id,
    threshold=0.01,
    averaging_iterations=10,
    iterations_to_consider=5,
)

setup.get_stopping_condition(lift_sc.id)

setup.delete_stopping_condition(lift_sc.id)
