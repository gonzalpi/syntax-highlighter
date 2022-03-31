#include <stdio.h>
#include "scanner.h"

// From external module
extern int yylex();
extern int yylineno;
extern char *yytext;    // tokens

// Tokens
char *types[] =
{
    NULL,
    "keyword",
    "type",
    "compare_operator",
    "assignment_operator",
    "logical_operator",
    "mathematical_operator",
    "semicolon",
    "comment",
    "bracket",
    "boolean",
    "double_quotes",
    "single_quotes",
    "number",
    NULL,
    NULL
};

// Parser
int main()
{
    // Open file, reference stylesheet, open tags
    FILE *file = fopen("output.html", "w");
    fprintf(file, "<html><head><link rel='stylesheet' href='style.css'></head><body>");

    // Write label colors
    for (int i=1; i<14; i++)
    {
        fprintf
        (
            file,
            "<span class='%s'>%s</span><br/>",
            types[i], types[i]
        );
    }
    fprintf(file, "<br/>");

    // Lex
    int idx;
    idx = yylex();
    fprintf(file, "CODE:<br/><div id='code'>");
    while (idx)
    {
        if (idx==15) // NONE
        {
            fprintf(file, "%s", yytext);
            idx = yylex();
        }
        else if (idx==14)   // LINEBREAK
        {
            fprintf(file, "<br/>");
            idx = yylex();
        }
        else
        {
            fprintf
            (
                file,
                "<span class='%s'>%s</span>",
                types[idx], yytext
            );
            idx = yylex();
        }
        // fprintf(file, "%d %s\n\n", idx, yytext);
        // idx = yylex();
    }
    
    // Close tags and file
    fprintf(file, "</div></body></html>");
    fclose(file);

    // End
    return 0;
}