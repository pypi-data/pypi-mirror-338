# Copyright (c) 2023-2024 Datalayer, Inc.
#
# Datalayer License

import json

from ..__version__ import __version__


async def test_config(jp_fetch):
    # When
    response = await jp_fetch("jupyter_kernels", "config")
    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "extension": "jupyter_kernels",
        "version": __version__
    }
