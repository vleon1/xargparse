#!/bin/bash


set -ex


#virtualenv ./build/env2
#python3 -m venv ./build/env3

#./build/env2/bin/pip install pylint
#./build/env3/bin/pip install pylint mypy

#./build/env2/bin/pylint ./src/xargparse.py
./build/env3/bin/pylint ./src/xargparse.py
./build/env3/bin/mypy ./src/xargparse.py
