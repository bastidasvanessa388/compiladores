from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser

# Entrada de prueba
input_stream = InputStream("3+4*5")

# Crear lexer
lexer = Expr3Lexer(input_stream)

# Crear stream de tokens
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type]

        if token_name is None:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Crear parser
parser = Expr3Parser(token_stream)

# Regla inicial
tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))