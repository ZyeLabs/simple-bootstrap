#!/usr/bin/env python
# encoding: utf-8
"""
bootstrap.py

A Simple bootstrap script
- Creates a virtualenv
- Installs packages from requirements.txt
- Update - re-install packages/update
- Remove - Remove the virual env
- setup - create the virtual env
"""

import os
import sys
import subprocess
import shutil

pwd = os.path.dirname(__file__)
virtualdir = os.path.join(pwd,"main")

if len(sys.argv) != 2:
    print "bootstrap takes exactly one argument"
    print "Try update, setup, remove"
    sys.exit(2)

for arg in sys.argv: 
    if arg == 'update' or arg == "setup":
        subprocess.call(["python",os.path.join(pwd,"pip.py"),"install",
                         "-E",os.path.join(pwd,"main"),
                         "--enable-site-packages",
                         "--requirement",os.path.join(pwd,"requirements.txt")])
        break
    if arg == "remove":
        if os.path.exists(virtualdir):
            shutil.rmtree(virtualdir)
        break