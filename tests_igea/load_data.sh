#!/usr/bin/env bash

#python3 ../odoo_import_thread.py --file=tosend/1_hr.department.csv --model='hr.department' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#python3 ../odoo_import_thread.py --file=tosend/2_sync_structure.organisational_unit.csv --model='sync_structure.organisational_unit' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/3_sync.work_location.csv --model='sync.work_location' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok provare a mettere anche le UO in sync.work_location
#python3 ../odoo_import_thread.py --file=tosend/4_sync_places.location.csv --model='sync_places.location' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/5_sync_places.department.csv --model='sync_places.department' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/6_sync_places.room.csv --model='sync_places.room' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/7_sync_places.bed.csv --model='sync_places.bed' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/8_account.analytic.group.csv --model='account.analytic.group' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#ok
#python3 ../odoo_import_thread.py --file=tosend/9_account.analytic.account.csv --model='account.analytic.account' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#Contabilità->Configurazione->Conti Analitici -> OK
#python3 ../odoo_import_thread.py --file=tosend/10_account.analytic.tag.csv --model='account.analytic.tag' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#Etichette analitiche -> OK
#python3 ../odoo_import_thread.py --file=tosend/10a_account.analytic.distribution.csv --model='account.analytic.distribution' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#Distribuzione analitica -> Ok
#python3 ../odoo_import_thread.py --file=tosend/11_account.account.csv --model='account.account' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#[OK]Contabilità->Configurazione->Piano dei conti
#python3 ../odoo_import_thread.py --file=tosend/12_sync_employee.doctor.csv --model='sync_employee.doctor' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#[OK]Togliere department_id/id
#python3 ../odoo_import_thread.py --file=tosend/13_sync_employee.nurse.csv --model='sync_employee.nurse' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/14_sync_employee.other_employee.csv --model='sync_employee.other_employee' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/15_product.category.csv --model='product.category' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/16_product.template.csv --model='product.template' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/16a_sync_product.service_type.csv --model='sync_product.service_type' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/17_product.template.csv --model='product.template' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/18_product.pricelist.csv --model='product.pricelist' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/18a_product.pricelist.item.csv --model='product.pricelist.item' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
#OK
#python3 ../odoo_import_thread.py --file=tosend/19_sync_service_pack.hs_pack.csv --model='sync_service_pack.hs_pack' --size=1 --worker=1 --conf=conf/connection_upload.conf --sep=";"
