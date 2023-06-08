import unittest
from unittest.mock import patch, call
from io import StringIO
from user import User
from user_view import UserView
from user_controller import UserController


class TestUserController(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe")
        self.view = UserView()
        self.controller = UserController(self.user, self.view)

    def test_handle_user_input(self):
        model = User("John Doe")
        view = UserView()
        controller = UserController(model, view)

        # Set up input and expected output
        input_values = ["display", "update", "Jane Smith", "display", "exit"]
        expected_output = ["Info: John Doe", "Info: Jane Smith"]

        # Mock the print function
        with patch("builtins.print") as mock_print:
            # Mock the input function
            with patch("builtins.input", side_effect=input_values):
                # Call the method to be tested
                controller.handle_user_input()

        # Verify the printed output matches the expected output
        mock_print.assert_has_calls([call(output) for output in expected_output])

    def test_handle_user_input_custom_input(self):
        model = User("John Doe")
        view = UserView()
        controller = UserController(model, view)

        # Set up input and expected output
        input_values = ["custom"]
        expected_output = ["Error: Invalid command."]

        # Mock the print function
        with patch("builtins.print") as mock_print:
            # Mock the input function
            with patch("builtins.input", side_effect=input_values):
                # Call the method to be tested
                controller.handle_user_input()

        # Verify the printed output matches the expected output
        mock_print.assert_has_calls([call(output) for output in expected_output])


if __name__ == "__main__":
    unittest.main()
