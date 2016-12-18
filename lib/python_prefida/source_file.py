#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os


def source_file(name=None):
    #+ Returns the source file of the routine `name`
    #+ If name is not given then it returns the source file of caller routine

    if name is None:
        return os.path.abspath(__file__)
    else:
        Exception('Feature not created yet')
