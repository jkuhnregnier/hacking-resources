# Filetypes

## Excel

*.xlsx*
Is simply a zip file containing multiple XML files. 

```
$ file excel-file.xlsx
excel-file.xlsx: Zip archive data, at least v2.0 to extract
```

```
$ unzip excel-file.xlsx
Archive:  excel-file.xlsx
 inflating: [Content_Types].xml
 inflating: _rels/.rels
 inflating: xl/_rels/workbook.xml.rels
 inflating: xl/workbook.xml
 inflating: xl/sharedStrings.xml
 inflating: xl/theme/theme1.xml
 inflating: xl/styles.xml
 inflating: xl/worksheets/sheet1.xml
 inflating: docProps/core.xml
 inflating: docProps/app.xml
```

More information:
- http://officeopenxml.com/anatomyofOOXML-xlsx.php
- https://stackoverflow.com/questions/4886027/looking-for-a-clear-description-of-excels-xlsx-xml-format
- https://www.data2type.de/xml-xslt-xslfo/spreadsheetml/xlsx-format/

Potentially dangerous file extensions as all of them allow the execution of macros:
.xlsm
.xlsb (bin)
.xls (bin)
.xltm

*.csv*

https://github.com/wireservice/csvkit
https://donatstudios.com/CSV-An-Encoding-Nightmare
https://stackoverflow.com/questions/37177069/how-to-check-encoding-of-a-csv-file