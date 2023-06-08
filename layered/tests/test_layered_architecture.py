import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from layers import PresentationLayer, DataLayer, BusinessLogicLayer

class TestLayeredArchitecture(unittest.TestCase):
    def test_layered_architecture(self):
        data_layer = DataLayer()
        business_logic = BusinessLogicLayer(data_layer)
        presentation = PresentationLayer(business_logic)

        expected_output = [
            "Data from the Business Logic Layer:",
            "Item 1",
            "Item 2",
            "Item 3"
        ]

        # Redirecting the print output to a variable for assertion
        import sys
        from io import StringIO
        stdout = sys.stdout
        sys.stdout = StringIO()

        presentation.display_data()

        # Getting the printed output
        output = sys.stdout.getvalue().strip().split('\n')

        # Restoring the default print behavior
        sys.stdout = stdout

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
