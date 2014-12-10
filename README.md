Extract Meanings of english words from http://dictionary.com.np
===========

```bash
$ ./main.py <line_seperated_wordlist_en> <filename_to_write> [--resume]
```
Or 
```bash
$ ./main.py
```
to show uses. 

Smart save. Use Resume to continue from the last position.


Output File Format
=====
The output file will have the lines in the format as shown below:

`<english_text>      <meaning_comma_seperated>*`


\*null if meaning is not found. 
