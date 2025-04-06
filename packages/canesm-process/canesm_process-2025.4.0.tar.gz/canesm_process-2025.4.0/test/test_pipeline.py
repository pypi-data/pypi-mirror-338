from canproc.pipelines import canesm_pipeline
from canproc.pipelines import Pipeline
from canproc.pipelines.utils import parse_formula, AstParser
from canproc import register_module
from dask.dot import dot_graph
from canproc.runners import DaskRunner
from pathlib import Path
import pytest
import os


@pytest.mark.parametrize(
    "formula, vars, ops",
    [
        ("FSO", ["FSO"], []),
        ("FSO+FSR", ["FSO", "FSR"], ["+"]),
        ("FSO-FSR+OLR", ["FSO", "FSR", "OLR"], ["-", "+"]),
        ("FSO/FSR-OLR", ["FSO", "FSR", "OLR"], ["/", "-"]),
        ("FSO*FSR/OLR", ["FSO", "FSR", "OLR"], ["*", "/"]),
        (" FSO *FSR/ OLR+BALT - BEG", ["FSO", "FSR", "OLR", "BALT", "BEG"], ["*", "/", "+", "-"]),
        ("TCD > CDBC", ["TCD", "CDBC"], [">"]),
        ("TCD >= CDBC", ["TCD", "CDBC"], [">="]),
        ("TCD < CDBC", ["TCD", "CDBC"], ["<"]),
        ("TCD <= CDBC", ["TCD", "CDBC"], ["<="]),
    ],
    ids=[
        "single",
        "short",
        "add-sub",
        "div-sub",
        "mul-div",
        "whitespace",
        "greater than",
        "greater than equal",
        "less than",
        "less than equal",
    ],
)
def test_formula_parsing(formula: str, vars: list[str], ops: list[str]):
    test_vars, test_ops = parse_formula(formula)
    assert test_vars == vars
    assert test_ops == ops


@pytest.mark.parametrize(
    "filename, num_ops",
    [
        ("canesm_pipeline.yaml", 93),
        ("canesm_pipeline_v52.yaml", 8),
        ("test_duplicate_output.yaml", 8),
        ("test_masked_variable.yaml", 8),
        ("test_xarray_ops.yaml", 10),
        ("test_formula.yaml", 23),
        ("test_formula_compute_syntax.yaml", 22),
        ("test_multistage_computation.yaml", 9),
        ("test_compute_and_dag_in_stage.yaml", 10),
        ("docs_example_pipeline.yaml", 19),
        ("test_stage_resample.yaml", 18),
        ("test_default_resample_freqs.yaml", 16),
        ("test_stage_cycle.yaml", 12),
        ("test_stage_area_mean.yaml", 10),
        ("test_compute_from_branch.yaml", 10),
        ("test_encoding.yaml", 11),
    ],
    ids=[
        "canesm 6 pipeline",
        "canesm 5 pipeline",
        "duplicate outputs",
        "masked variable",
        "general xr dataset operations",
        "formula",
        "formula compute syntax",
        "multistage computation",
        "both compute and dag",
        "docs radiation example",
        "resample op in stage",
        "default resample stages",
        "cycle op in stage",
        "area_mean op in stage",
        "compute from branch",
        "encoding",
    ],
)
def test_canesm_pipeline(filename: str, num_ops: int):
    """
    Test that the expected number of nodes are created.
    Note that this doesn't guarantee correctness and we should be testing
    node connections, but that is harder to check.
    """
    pipeline = Path(__file__).parent / "data" / "pipelines" / filename
    dag = canesm_pipeline(pipeline, input_dir="test")
    assert len(dag.dag) == num_ops
    # assert dag.id[0 : len(dag_id)] == dag_id

    # runner = DaskRunner()
    # dsk, output = runner.create_dag(dag)
    # dot_graph(dsk, f"{filename.split('.')[0]}.png", rankdir="TB", collapse_outputs=True)


def test_metadata():
    pipeline = Path(__file__).parent / "data" / "pipelines" / "test_metadata.yaml"
    dag = canesm_pipeline(pipeline, input_dir="test")
    assert dag.dag[3].kwargs["metadata"] == {
        "long_name": "Daily mean ground temperature aggregated over all tiles",
        "units": "K",
    }
    assert dag.dag[6].kwargs["metadata"] == {
        "long_name": "Monthly mean ground temperature aggregated over all tiles",
        "units": "K",
        "max": True,
        "min": True,
    }


def test_encoding_propagation():
    pipeline = Path(__file__).parent / "data" / "pipelines" / "test_encoding.yaml"
    dag = canesm_pipeline(pipeline, input_dir="test")

    # test setup default (daily ST)
    assert dag.dag[3].kwargs["encoding"] == {"dtype": "float32", "_FillValue": 1.0e20}

    # test stage default (monthly ST)
    assert dag.dag[6].kwargs["encoding"] == {"dtype": "float64", "_FillValue": -999}

    # test variable encoding (monthly GT)
    assert dag.dag[10].kwargs["encoding"] == {"dtype": "float64", "_FillValue": 1.0e20}


def test_pipeline_with_custom_function():

    # defined in conftest.py
    import mymodule

    register_module(mymodule, "mymodule")

    pipeline = Path(__file__).parent / "data" / "pipelines" / "test_user_function.yaml"
    dag = canesm_pipeline(pipeline, input_dir="test")
    assert len(dag.dag) == 16


@pytest.mark.skip(reason="requires access to science")
def test_run_pipeline(
    client=None, report=True, filename: str | None = None, scheduler: str = "threads"
):

    import time
    from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler, visualize
    from dask.distributed import performance_report

    # qsub -I -lselect=1:ncpus=80:mem=175gb -lplace=scatter -Wumask=022 -S/bin/bash -qdevelopment -lwalltime=02:00:00
    config = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rlr001/software/pipelines/canesm-processor/test/tables/core_cmip6.yaml"
    # config = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rlr001/software/pipelines/canesm-processor/test/tables/"
    input_dir = (
        r"/space/hall5/sitestore/eccc/crd/ccrn/users/rvs001/data/jcl-diag-test-002/1.0x1.0_annual"
    )
    output_dir = r"/space/hall5/sitestore/eccc/crd/ccrn/users/rlr001/canproc/jcl-diag-test-002"

    print("creating pipeline...")
    pipeline = Pipeline(config, input_dir, output_dir)
    dag = pipeline.render()

    runner = DaskRunner()
    dsk, output = runner.create_dag(dag)
    dot_graph(dsk, f"{Path(config).name.split('.')[0]}.png", rankdir="TB", collapse_outputs=True)

    print("creating output directories...")
    for directory in pipeline.directories.values():
        os.makedirs(directory, exist_ok=True)

    start = time.time()
    print("running dag...")
    runner = DaskRunner(scheduler=scheduler)
    if client is not None:
        runner.scheduler = client.get
        # runner.run(dag)
        if report:
            with performance_report(filename=filename):
                output = runner.run(dag, optimize=True)
        else:
            output = runner.run(dag, optimize=True)
        end = time.time()
        print(f"processing took {end - start:3.4f} seconds")
        # client.profile(filename='profile_client.html')  # save to html file
    else:
        output = runner.run(
            dag,
            optimize=True,
            ray_init_kwargs={
                "num_cpus": 35,
                "object_store_memory": 16 * 1e9,
                "dashboard_host": "0.0.0.0",
            },
        )

        # with Profiler() as prof, ResourceProfiler(dt=0.0001) as rprof, CacheProfiler() as cprof:
        # output = runner.run(dag, optimize=False)
        end = time.time()
        print(f"processing took {end - start:3.4f} seconds")
        # visualize([prof, rprof, cprof], filename=filename)

    print("SUCCESS!")


if __name__ == "__main__":

    local = True
    if local:
        client = None
        cluster = None
    else:
        from dask.distributed import LocalCluster, SubprocessCluster

        tpc = 1
        workers = 1
        cluster = LocalCluster(
            processes=True, n_workers=workers, threads_per_worker=tpc
        )  # Fully-featured local Dask cluster
        # cluster = SubprocessCluster()
        client = cluster.get_client()

    scheduler = "threads"
    if cluster:
        filename = f"client_{'processes'}_dask_c12-96_{workers}cpu_{tpc}tpc.html"
    else:
        filename = f"profile_{scheduler}_dask.html"
    test_run_pipeline(client, filename=filename, scheduler=scheduler, report=True)
