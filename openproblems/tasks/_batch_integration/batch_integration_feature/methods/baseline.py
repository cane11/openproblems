from .....tools.decorators import method
from .....tools.utils import check_version
from ...batch_integration_graph.methods.baseline import _randomize_features


@method(
    method_name="No Integration",
    paper_name="No Integration (baseline)",
    paper_reference="openproblems",
    paper_year=2022,
    code_url="https://github.com/openproblems-bio/openproblems",
    is_baseline=True,
)
def no_integration(adata, test=False):
    adata.uns["method_code_version"] = check_version("openproblems")
    return adata


@method(
    method_name="Random Integration",
    paper_name="Random Integration (baseline)",
    paper_reference="openproblems",
    paper_year=2022,
    code_url="https://github.com/openproblems-bio/openproblems",
    is_baseline=True,
)
def random_integration(adata, test=False):
    adata.X = _randomize_features(adata.X)
    adata.uns["method_code_version"] = check_version("openproblems")
    return adata


@method(
    method_name="Random Integration by Celltype",
    paper_name="Random Integration by Celltype (baseline)",
    paper_reference="openproblems",
    paper_year=2022,
    code_url="https://github.com/openproblems-bio/openproblems",
    is_baseline=True,
)
def celltype_random_integration(adata, test=False):
    adata.X = _randomize_features(adata.X, partition=adata.obs["labels"])
    adata.uns["method_code_version"] = check_version("openproblems")
    return adata


@method(
    method_name="Random Integration by Batch",
    paper_name="Random Integration by Batch (baseline)",
    paper_reference="openproblems",
    paper_year=2022,
    code_url="https://github.com/openproblems-bio/openproblems",
    is_baseline=True,
)
def batch_random_integration(adata, test=False):
    adata.X = _randomize_features(adata.X, partition=adata.obs["batch"])
    adata.uns["method_code_version"] = check_version("openproblems")
    return adata
