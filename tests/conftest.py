import pytest
from pathlib import Path


@pytest.fixture
def test_crates():
    fixtures_dir = Path("tests") / "fixtures"
    return {
        "basic": fixtures_dir / "basic",
        "malformed": fixtures_dir / "malformed",
        "missing": fixtures_dir / "missing",
    }

