#!/bin/bash

mkdir -p "/tmp/output"
pytest --driver Remote --capability browserName chrome -v --html="/tmp/output/report.html"

#pytest  -n 4 --driver Remote --selenium-host 4444 --capability browserName chrome  -v --html="/tmp/output/report.html"