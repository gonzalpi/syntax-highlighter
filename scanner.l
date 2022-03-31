%{
    #include "scanner.h"
%}

%%

"if"|"while"|"do"|"for"|"break"|"continue"|"in"|"def"|"return"|"try"|"except"|"import"|"as"|"from"|"print"|"using"|"define"|"let"   return KEYWORD;
"int"|"void"|"float"|"double"|"string"|"str"|"list"|"tuple"|"range"|"dict"|"set"|"bool"|"char"|"long"|"short"|"byte"                return TYPE;
">"|">="|"=="|"<="|"<"|"!="     return COMPAREOP;
"="                             return ASSIGNMENTOP;
"&&"|"||"|"~"|"and"|"or"|"not"  return LOGICALOP;
"+"|"-"|"*"|"/"|"%"|"^"         return MATHOP;
";"                             return SEMICOLON;
"#.*"|"//.*"                    return COMMENT;
"("|")"|"["|"]"|"{"|"}"|"<"|">" return BRACKET;
"True"|"False"|"true"|"false"   return BOOLEAN;
"\""                            return DQUOTES;
"'"                             return SQUOTES;
[0-9]|[0-9]?\.[0-9]+            return NUMBER;
"\n"                            return LINEBREAK;
.                               return NONE;

%%

int yywrap(void)
{
    return 1;
}