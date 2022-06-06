# Syntax Highlighter

The program receives a text file containing code in C++, Python or JavaScript and outputs an HTML file containing the same code and highlighting elements from lexical categories that are shared between the three languages.

**Note: multi-threaded highlighting can be run in the [Python](python) implementation**

## How to highlight code

From the folder where all files are stored, run shell script with path to code file as an argument:

    ./run.sh path/to/file.py

In computers that cannot run shell scripts the code can be manually compiled and run:

    gcc scanner.c lex.yy.c -o scanner
    ./scanner < path/to/file.cpp

The highlighted code will be stored in ```output.html```, using the stylesheet ```style.css``` contained in this folder.

## Important notes

- An exception is yet to be implemented so that C++ and JavaScript comments be told apart from Python integer divisions ("//").

- Another exception is yet to be implemented so that Python comments be highlighted if there is no space between "#" and the text. C++ "#" statements should be taken into consideration.

## Sources consulted

[https://youtu.be/54bo1qaHAfk](https://youtu.be/54bo1qaHAfk)