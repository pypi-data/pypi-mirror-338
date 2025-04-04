from epidemmo.stage import Stage
from epidemmo.flow import Flow, FlowError
from epidemmo.factor import Factor, FactorError

import pytest


@pytest.fixture()
def get_simple_flow():
    s = Stage('S', 10, index=0)
    i = Stage('I', 0, index=1)
    beta = Factor('beta', 0.4)
    fl = Flow(s, {i: 1}, beta, {}, index=0)
    return s, i, beta, fl


def test_start(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert fl._start == s


def test_simple_end_dict(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert isinstance(fl._end_dict, dict)


def test_simple_end_value(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert fl._end_dict[i].value == 1


def test_simple_ind_dict(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert isinstance(fl._ind_dict, dict)


def test_simple_ind_value(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert fl._ind_dict == {}


def test_simple_fl_factor(get_simple_flow):
    s, i, beta, fl = get_simple_flow
    assert fl._flow_factor == beta

