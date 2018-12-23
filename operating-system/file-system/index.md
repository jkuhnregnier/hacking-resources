# File System

## Tools to Use to Explore
* `hexdump`
* `file`
* `dd`
* `chardetect` - is part of the chardet python package

### Character Encoding
Related topics: BOM

#### What character encoding is a file made of?
It's impossible to know, except if the file itself contains this information. This is typically the case for XML, HTML, Excel and other files. But files such as .txt or .csv contain no such information, if they don't contain a byte order mark (BOM). The way programs know which encoding is used, is by analyzing the file and the characters within them. They then return a guess based on the specific characteristics made by different encoding systems. 

You can use `chardetect`, which is part of the chardet python package, to guess which character encoding a file contains.
https://github.com/chardet/chardet

Another alternative is the file command: `file <encoded-text-file>`, though, sometimes it is not as precise as chardet/chardetect.

https://www-archive.mozilla.org/projects/intl/UniversalCharsetDetection.html

#### Byte Order Mark
The byte order mark (BOM) is often essential in helping to decode whether a file has a UTF-n encoding or a different one. The lack of it, typically, means that it isn't encoded in UTF-n. 

https://stackoverflow.com/questions/13590749/reading-unicode-file-data-with-bom-chars-in-python 
https://stackoverflow.com/questions/5202648/adding-bom-unicode-signature-while-saving-file-in-python

