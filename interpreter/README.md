# Interpreter Pattern

The Interpreter pattern is a behavioral pattern that defines a language and its grammar, as well as an interpreter to evaluate expressions in that language. It allows you to interpret and evaluate complex expressions by breaking them down into simpler components.

## Components of the Interpreter Pattern

The Interpreter pattern typically involves the following components:

1. **Context**: It provides the context or environment in which the expressions are evaluated. It contains any necessary information or variables needed for the interpretation.

2. **Expression**: It is the base class/interface for all the expressions in the language. It defines an `interpret` method that takes a context as input and evaluates the expression.

3. **Concrete Expressions**: These are the concrete subclasses of the Expression class that represent different expressions in the language. Each concrete expression implements the `interpret` method according to its specific functionality.

## Example

In **`main.py`**, there is simple arithmetic language with the ability to evaluate addition expressions. It has the following components:

- **Context**: The Context class holds the variables used in the expressions. It provides methods to set and get variables.

- **Expression**: The Expression base class defines the `interpret` method, which is overridden by concrete expression classes.

- **Concrete Expressions**: We have three concrete expression classes:
  - `Constant`: It represents a constant value in the language.
  - `Variable`: It represents a variable in the language.
  - `Add`: It represents an addition expression. It takes two sub-expressions and evaluates their sum.

We create a context, set the variables, create an expression (`Add`) with sub-expressions (`Variable` and `Constant`), and call the `interpret` method on the expression. The interpretation evaluates the expression and returns the result.

## Usage

To `run the example`, execute the `main.py` file:

```zsh
python3 main.py
```

There is following `expression`:

```python
    # Usage example
    context = Context()
    context.set_variable('x', 5)
    context.set_variable('y', 10)

    expression = Add(Variable('x'), Constant(7))
    result = expression.interpret(context)

    expression = Add(Variable('x'), Constant(result))
    result = expression.interpret(context)

    print(f"Result: {result}")
```

*Output:*

```zsh
% python3 main.py
Result: 17
```

To `run the tests`, execute the `test.py` file:

```zsh
python3 test.py
```