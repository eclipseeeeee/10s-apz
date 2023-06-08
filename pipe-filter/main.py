from filters import reverse, uppercase

def run_pipe_filter(input_data):
    # Run the pipe-filter sequence
    result = uppercase(input_data)
    result = reverse(result)

    # Return the final result
    return result

if __name__ == '__main__':
    input_data = 'Hello, World!'
    result = run_pipe_filter(input_data)
    print(result)