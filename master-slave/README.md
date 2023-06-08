# Master-Slave Pattern Example

This example demonstrates the Master-Slave pattern in Python. The pattern involves a master component that controls and coordinates one or more slave components. The master component distributes tasks or workloads to the slave components, and they perform the assigned tasks.

In this example, the master component generates a list of numbers, and the slave components calculate the square of each number in parallel.

## Implementation

**`main.py`** contains the main logic for the Master-Slave pattern implementation. It defines the square_worker function, which represents the worker task performed by each slave process. 

The `run_master_slave` function is responsible for coordinating the master-slave communication and task distribution. The script generates a list of numbers and calculates their squares using the Master-Slave pattern.

## Usage

To `run the example` and see the results, you can execute the following command in the terminal:

```zsh
python3 main.py
```

The script will generate a list of numbers and calculate their squares using the Master-Slave pattern. The calculated squares will be printed as the output.

*Output*:
```zsh
% python3 main.py 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

To `run the tests`, execute the following command:

```zsh
python3 test.py
```


## Dependencies

The implementation uses the following dependencies:

- **multiprocessing:** This built-in Python module is used for process-based parallelism and communication between processes.