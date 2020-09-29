## Changes to the original project

Watch out for csv during import. The file may contain the BOM, which can be deleted by changing the encoding utf-8-sig
[UTF-8 codec with BOM signature](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig).

Csv files must not count the false field, except for Boolean fields.

The fields to extract (can be None or [] to extract all fields).

Per usare la connessione criptata impostare:`protocol = jsonrpcs`
Usare due file all'interno di conf, uno per scaricare e l'altro per caricare, se le macchine sono diverse.
Ad esempio:
`hostname = 172.16.0.189 
database = biolab_prod_05
login = admin
password = odoo
protocol = jsonrpc
port = 8065
uid = 2`
per caricare e la seguente per scaricare:
`[Connection]
hostname = biolab.dinamicheaziendali.it
database = biolab_8082
login = administration@biolab-srl.com
password = ElSa78791216
protocol = jsonrpcs
port = 443
uid = 16`
Nel caso di instanza locale usare: `hostname = localhost`

##Struttura CVS
Le chiavi esterne se sono assenti non devono essere ne false ne 0, ma ";;", 
ovvero lasciare il vuoto tra i due punto e virgola.

Se si hanno errori di ambiguità tipicamente si può eliminare il campo
del tipo `campo_in_questione` e lasciare `campo_in_questione/id`
