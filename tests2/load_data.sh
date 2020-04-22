#!/usr/bin/env bash
# $1 python3 ../odoo_import_thread.py --file=origin/res.partner_o2m.csv --model='res.partner' --size=1 --worker=1 --conf=conf/connection.conf --o2m
$1 python3 ../odoo_import_thread.py --file=hr.department.csv --model='hr.department' --size=1 --worker=1 --conf=conf/connection.conf --o2m
