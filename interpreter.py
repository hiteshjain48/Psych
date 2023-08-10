from tokens import Integer, Float


class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def read_INT(self, value):
        return int(value)

    def read_FLT(self,value):
        return float(value)

    def compute(self,left,op, right):
        left_type = left.type
        right_type = right.type
        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self,f"read_{right_type}")(right.value)
        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right
        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)

    def interpret(self,tree=None):
        if tree is None:
            tree = self.tree
        left = tree[0]
        if isinstance(left,list):
            left = self.interpret(left)
        right = tree[2]
        if isinstance(right,list):
            right = self.interpret(right)
        operator = tree[1]
        return self.compute(left,operator,right)


