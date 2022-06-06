from ply import lex
from rules import *
from sys import argv
    
lexer = lex.lex()

for filename in argv[1:]:
    # Read input file
    with open(filename) as f:
        data = "".join(f.readlines())

    with open(filename + '.html', 'w') as f:
        # Open tags, copy CSS
        f.write("<html><head><style>")
        with open("style.css", "r") as style:
            f.write("".join(style.readlines()))
        f.write("</style></head><body>")
        # Write label colors
        for token in tokens[0:-2]:
            f.write(f"<span class='{token}'>{' '.join(token.lower().split('_'))}</span><br/>")
        f.write("<br/>CODE:<br/><div id='code'>")
        # Parse data, write to HTML
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
