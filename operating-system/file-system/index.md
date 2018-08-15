# File System

## Tools to Use to Explore
* `hexdump`
* `file`
* `dd`
* `chardetect` - is part of the chardet python package

### Character Encoding
Related topics: BOM, 

*Find out what type of character encoding a file is made of:*
You can use `chardetect` - is part of the chardet python package
or the chardet Python project. https://github.com/chardet/chardet

The `file <encoded-text-file>` command is not as precise as chardet/chardetect.

https://www-archive.mozilla.org/projects/intl/UniversalCharsetDetection.html

#### Byte Order Mark
The byte order mark (BOM) is often essential in helping to decode whether a file has a UTF-n encoding or a different one. The lack of it, typically, means that it isn't encoded in UTF-n. 

https://stackoverflow.com/questions/13590749/reading-unicode-file-data-with-bom-chars-in-python 
https://stackoverflow.com/questions/5202648/adding-bom-unicode-signature-while-saving-file-in-python