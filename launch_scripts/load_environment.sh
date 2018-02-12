#!/bin/bash

python3.6 -m venv $HOME/ddf_env
source $HOME/ddf_env/bin/activate
pip install -r requirements.txt
