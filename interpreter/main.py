class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name)


class Expression:
    def interpret(self, context):
        pass


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get_variable(self.name)


class Add(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        left_value = self.left_expression.interpret(context)
        right_value = self.right_expression.interpret(context)
        return left_value + right_value


if __name__ == "__main__":
    # Usage example
    context = Context()
    context.set_variable('x', 5)
    context.set_variable('y', 10)

    expression = Add(Variable('x'), Constant(7))
    result = expression.interpret(context)

    expression = Add(Variable('x'), Constant(result))
    result = expression.interpret(context)

    print(f"Result: {result}")
