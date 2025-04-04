import os

import pytest

from .data import RESOURCE_ROOT


@pytest.fixture
def xanes_filename():
    return os.path.join(RESOURCE_ROOT, "xanes.h5")
