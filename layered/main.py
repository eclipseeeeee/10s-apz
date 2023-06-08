from layers import DataLayer, BusinessLogicLayer, PresentationLayer

def main():
    # Create the layers
    data_layer = DataLayer()
    business_logic = BusinessLogicLayer(data_layer)
    presentation = PresentationLayer(business_logic)

    # Display the data
    presentation.display_data()

if __name__ == '__main__':
    main()
