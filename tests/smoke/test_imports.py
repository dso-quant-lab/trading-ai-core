"""
Smoke test: validate top-level modules under src can be imported safely.

Does NOT run live data fetches, model training, trades, or pipeline runs.
"""

import pytest


def test_import_src_package():
    """src package is importable."""
    import src  # noqa: F401


@pytest.mark.parametrize(
    "module",
    [
        "src.data",
        "src.execution",
        "src.features",
        "src.models",
        "src.pipelines",
        "src.portfolio",
        "src.risk",
        "src.sentiment",
        "src.utils",
    ],
)
def test_import_src_submodules(module):
    """Each src subpackage imports without side effects."""
    __import__(module)
