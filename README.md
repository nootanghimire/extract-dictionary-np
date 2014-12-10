Extract Meanings of english words from http://dictionary.com.np
===========

```bash
$ ./main.py <list_of_english_words_newline_seperated> <file_name_to_write_meanings> [--resume]
```

Smart save. Use Resume to continue from the last position.


Output File Format
=====
The output file will have the lines in the format as shown below:

`<english_text>      <meaning_comma_seperated>*`


\*null if meaning is not found. 
