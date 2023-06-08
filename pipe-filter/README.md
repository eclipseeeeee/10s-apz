# Pipe-Filter Pattern Example
This example demonstrates the Pipe-Filter pattern in Python. The Pipe-Filter pattern involves breaking down a complex task into a series of smaller tasks called filters. Each filter performs a specific transformation or operation on the data and passes the processed data to the next filter through a pipe.

## Filters

- Uppercase Filter
The Uppercase Filter takes the input data and converts it to uppercase.

- Reverse Filter
The Reverse Filter takes the input data and reverses the order of characters.

## Implementation

The implementation consists of the following files:

- filters/uppercase.py: This file contains the implementation of the Uppercase Filter. It defines the filter_uppercase function, which performs the uppercase transformation on the input data.

- filters/reverse.py: This file contains the implementation of the Reverse Filter. It defines the filter_reverse function, which reverses the order of characters in the input data.

- main.py: This file coordinates the execution of the pipe-filter process. It imports the filters and calls them in the desired order, passing the output of one filter as the input to the next filter. The final result of the pipe-filter process is returned and printed.

## Usage

To `run the example` and see the results, you can execute the following command in the terminal:

```zsh
python3 main.py
```

The `main.py` script demonstrates the usage of the Pipe-Filter pattern with the Uppercase and Reverse filters. By default, it uses the input data 'Hello, World!'. The script will apply the uppercase transformation followed by the reverse operation on the input data and print the result.

*Output:*
```zsh
% python3 main.py
!DLROW ,OLLEH
```

To `run tests`, execute the following command:

```zsh
python3 test.py
```