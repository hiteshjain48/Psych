class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.expression()
            return expression
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            operand = self.expression()
            return [operator,operand]

    def term(self):
        left_node = self.factor()
        self.move()
        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operation, right_node]
        return left_node

    def expression(self):
        left_node = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, operation, right_node]
        return left_node

    def comp_expression(self):
        left_node = self.boolean_expression()
        while self.token.type == "COMP":
            operation = self.token
            self.move()
            right_node = self.boolean_expression()
            left_node = [left_node, operation, right_node]
        return left_node
    def boolean_expression(self):
        left_node = self.expression()
        while self.token.type == "BOOL":
            operation = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, operation, right_node]
        return left_node

    def statement(self):
        if self.token.type == "DECL":
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                right_node = self.comp_expression()
                return [left_node, operation, right_node]
        elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OP":
            return self.comp_expression()

    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token

    def parse(self):
        return self.statement()

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]