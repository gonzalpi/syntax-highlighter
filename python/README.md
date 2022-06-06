# Syntax Highlighter

The program receives a text file containing code in C/C++, Python or JavaScript and outputs an HTML file containing the same code and highlighting elements from lexical categories that are shared between the three languages.

## How to highlight code

Install libraries in ```requirements.txt``` in a Python 3 environment.

From the ```python``` folder run:

```bash
# Single-threaded
python single.py path/to/file/1.py path/to/file/2.cpp ...
# Multi-threaded
python multi.py path/to/file/1.java path/to/file/2.py ...
```

The highlighted code will be stored in ```path/to/file/1.java_single.html``` for the single-threaded code and in ```path/to/file/2.cpp_multi.html```, using the style in ```style.css```.

## Important notes

- The grammar rules are the same as those in the C implementation, therefore all exceptions that are yet to be accounted for, do too in this one.