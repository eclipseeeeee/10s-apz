class PresentationLayer:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def display_data(self):
        data = self.business_logic.get_data()
        print("Data from the Business Logic Layer:")
        for item in data:
            print(item)