#!/usr/bin/env bash
pip install --user -r requirements.txt
airflow db init
airflow users create -r Admin -u admin -e admin@example.com -f admin -l user -p admin1234
airflow webserver