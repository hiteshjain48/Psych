from lexer import Lexer

while True:
    text = input("sudo: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)

