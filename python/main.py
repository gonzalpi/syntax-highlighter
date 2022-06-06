from ply import lex
from rules import *
from sys import argv
    
lexer = lex.lex()

# Read input file
with open(argv[1]) as f:
    data = "".join(f.readlines())

with open('output.html', 'w') as f:
    # Reference stylesheet, open tags
    f.write("<html><head><link rel='stylesheet' href='style.css'></head><body>")
    # Write label colors
    for token in tokens[0:-2]:
        f.write(f"<span class='{token}'>{' '.join(token.lower().split('_'))}</span><br/>")
    f.write("<br/>CODE:<br/><div id='code'>")
    # Parse data, write to html
    lexer.input(data)
    while(True):
        tok = lexer.token()
        if not tok:
            break
        if tok.value=="\n":
            f.write("<br/>")
            continue
        if tok.value=="\s":
            f.write(" ")
        f.write(f"<span class='{tok.type}'>{tok.value}</span>")
    # Close tags
    f.write("</div></body></html>")
