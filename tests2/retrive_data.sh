#!/usr/bin/env bash

python3 ../odoo_export_thread.py -c conf/connection.conf --file=retrieved/sync_employee.doctor.csv --model='sync_employee.doctor' --worker=1 --size=200 --domain="[]" --field="id,department_id_m2m:id" --sep=";" --encoding=utf-8-sig