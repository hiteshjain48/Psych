from lexer import Lexer
from parse import Parser
while True:
    text = input("sudo: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    tree = parser.expression()
    print(tree)

