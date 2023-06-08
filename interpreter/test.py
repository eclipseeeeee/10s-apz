import unittest
from main import Context, Constant, Variable, Add


class TestInterpreter(unittest.TestCase):
    def test_interpret_add_expression(self):
        # Create a context and set variables
        context = Context()
        context.set_variable('x', 5)
        context.set_variable('y', 10)

        # Create an expression: x + 7
        expression = Add(Variable('x'), Constant(7))

        # Evaluate the expression
        result = expression.interpret(context)

        # Assert the result
        self.assertEqual(result, 12)

    def test_interpret_variable_expression(self):
        # Create a context and set variables
        context = Context()
        context.set_variable('x', 5)

        # Create an expression: x
        expression = Variable('x')

        # Evaluate the expression
        result = expression.interpret(context)

        # Assert the result
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
