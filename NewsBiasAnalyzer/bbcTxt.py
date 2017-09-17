#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 02:18:09 2017

@author: kyler
"""

import os

def getReal():
    for file in os.listdir("/bbc"):
        if file.endswith(".txt"):
            openF = open(file, "r")
            yield openF.read()