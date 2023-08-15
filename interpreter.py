from tokens import Integer, Float


class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self,value):
        return float(value)

    def read_VAR(self,id):
        variable = self.data.read(id)
        variable_type = variable.type
        return getattr(self,f"read_{variable_type}")(variable.value)

    def compute(self,left,op,right):
        # left_type = "VAR" if str(left.type).startswith("VAR") else left.type
        left_type = "VAR" if left.type.startswith("VAR") else left.type
        right_type = "VAR" if right.type.startswith("VAR") else right.type

        if op.value == "=":
            left.type = f"VAR({right_type})"
            self.data.write(left,right)
            return self.data.read_all()

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

    def compute_unary(self, operator, operand):
        operand_type = "VAR" if operand.type.startswith("VAR") else operand.type
        operand = getattr(self, f"read_{operand_type}")(operand.value)
        if operator.value == "+":
            output = +operand
        elif operator.value == "-":
            output = -operand
        return Integer(output) if (operand_type == "INT") else Float(output)

    def interpret(self,tree=None):
        if tree is None:
            tree = self.tree
        if isinstance(tree, list) and len(tree) == 2:
            return self.compute_unary(tree[0], tree[1])
        elif not isinstance(tree, list):
            return tree
        else:
            left = tree[0]
            if isinstance(left,list):
                left = self.interpret(left)
            right = tree[2]
            if isinstance(right,list):
                right = self.interpret(right)
            operator = tree[1]
            return self.compute(left,operator,right)


