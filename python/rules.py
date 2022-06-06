tokens = (
    "KEYWORD",
    "TYPE",
    "COMPARE_OPERATOR",
    "ASSIGNMENT_OPERATOR",
    "LOGICAL_OPERATOR",
    "MATHEMATICAL_OPERATOR",
    "SEMICOLON",
    "COMMENT",
    "BRACKET",
    "BOOLEAN",
    "DOUBLE_QUOTES",
    "SINGLE_QUOTES",
    "NUMBER",
    "LINE_BREAK",
    "NONE",
)

t_KEYWORD = r'if|while|do|for|break|continue|main|include|in\s|def|return|try|except|import|as|from|print|using|define|let|namespace|std|self'
t_TYPE = r'int|void|float|double|string|str|list|tuple|range|dict|set|bool|char|long|short|byte'
t_COMPARE_OPERATOR = r'>|>=|==|<=|<|!='
t_ASSIGNMENT_OPERATOR = r'='
t_LOGICAL_OPERATOR = r'&&|\|\||~|\sand\s|or|not'
t_MATHEMATICAL_OPERATOR = r'\+|-|\*|/\s|%|\^'
t_SEMICOLON = r';'
t_COMMENT = r'\#\s+.*|// .*'
t_BRACKET = r'\(|\)|\[|\]|\{|\}|<|>'
t_BOOLEAN = r'True|False|true|false'
t_DOUBLE_QUOTES = r'\"'
t_SINGLE_QUOTES = r'\''
t_NUMBER = r'[0-9]|[0-9]?\.[0-9]+'
t_LINE_BREAK = r'\n'
t_NONE = r'.'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)