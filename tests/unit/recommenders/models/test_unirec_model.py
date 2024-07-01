# Copyright (c) Recommenders contributors.
# Licensed under the MIT License.

import os
import copy
import pytest

try:
    from recommenders.models.unirec.utils.file_io import load_yaml
    from recommenders.models.unirec.model.sequential.sasrec import SASRec
except ImportError:
    pass  # skip this import if we are in cpu environment


@pytest.mark.gpu
@pytest.fixture(scope="module")
def base_config(unirec_config_path):
    base_file = os.path.join(unirec_config_path, "base.yaml")
    config = load_yaml(base_file)
    config["exp_name"] = "pytest"
    config["n_users"] = None

    return config


@pytest.mark.gpu
def test_sasrec_component_definition(base_config, unirec_config_path):
    config = copy.deepcopy(base_config)
    yaml_file = os.path.join(unirec_config_path, "model", "SASRec.yaml")
    config.update(load_yaml(yaml_file))

    model = SASRec(config)

    assert model.n_layers == 2
