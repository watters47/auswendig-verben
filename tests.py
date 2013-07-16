#!/usr/bin/env python
#coding: utf-8

from nose.tools import ...
from auswendig_verben.api import get_verbs


def test_look_for_a_verb():
    result = get_verbs(infinitiv='sein')
    assert result is not None

