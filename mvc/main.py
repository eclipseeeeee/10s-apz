from user import User
from user_view import UserView
from user_controller import UserController

if __name__ == "__main__":
    # Create instances of Model, View, and Controller
    user = User("Anna")
    view = UserView()
    controller = UserController(user, view)

    # Handle user input and update/display user information
    controller.handle_user_input()
