#
# Copyright (c) 2020 Kian Cross
#

from packaging import version
from pixy import metadata

def test_version():
    version.parse(metadata.version)
