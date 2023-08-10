from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
while True:
    text = input("sudo: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    parser = Parser(tokens)
    tree = parser.expression()
    interpreter = Interpreter(tree)
    print(tree)
    output = interpreter.interpret()
    print(output)

