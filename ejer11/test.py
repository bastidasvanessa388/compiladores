from antlr4 import *
from Expr1Lexer import Expr1Lexer
from Expr1Parser import Expr1Parser

# Entrada de prueba
input_stream = InputStream("1+2+3/n5+6+7+8")

lexer = Expr1Lexer(input_stream)

token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type]

        if token_name is None:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

parser = Expr1Parser(token_stream)

tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))