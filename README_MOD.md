## Changes to the original project

Watch out for csv during import. The file may contain the BOM, which can be deleted by changing the encoding utf-8-sig
[UTF-8 codec with BOM signature](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig).

Csv files must not count the false field, except for Boolean fields.