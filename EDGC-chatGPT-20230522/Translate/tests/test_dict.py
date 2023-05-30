#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_dict
    ~~~~~~~~~

    Test Dict

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/Translate
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
from __future__ import unicode_literals
from dict import Dict


def test_e2c_words(capfd):
    Dict(['Test'])
    out, err = capfd.readouterr()
    assert '测试' in out


def test_e2c_sentences(capfd):
    Dict(['I', 'Love', 'You'])
    out, err = capfd.readouterr()
    assert '我爱你' in out


def test_c2e_words(capfd):
    Dict(['测试'])
    out, err = capfd.readouterr()
    assert 'Test' in out


def test_c2e_sentences(capfd):
    Dict(['我爱你'])
    out, err = capfd.readouterr()
    assert 'I love you' in out
