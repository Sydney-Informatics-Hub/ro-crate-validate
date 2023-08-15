import json
from pathlib import Path

import pytest

from ro_crate_validate.ro_crate_validate import load_crate

from ro_crate_validate.exceptions import ROCrateException, ROCrateException


def test_missing(test_crates):
    with pytest.raises(ROCrateException):
        load_crate(test_crates["missing"])

