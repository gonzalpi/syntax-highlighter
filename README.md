# Syntax Highlighter

The program receives a text file containing code in C++, Python or JavaScript and outputs an HTML file containing the same code and highlighting elements from lexical categories that are shared between the three languages.

Note that:
- An exception is yet to be implemented so that C++ and JavaScript comments be told apart from Python integer divisions ("//").
- Another exception is yet to be implemented so that Python comments be highlighted if there is no space between "#" and the text. C++ "#" statements should be taken into consideration.

Sources consulted: [https://youtu.be/54bo1qaHAfk](https://youtu.be/54bo1qaHAfk)