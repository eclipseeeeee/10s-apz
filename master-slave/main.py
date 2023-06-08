import multiprocessing


def square_worker(input_queue, output_queue):
    while True:
        number = input_queue.get()
        if number is None:
            break
        square = number ** 2
        output_queue.put(square)


def run_master_slave(numbers):
    # Create input and output queues for communication
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    # Create a list of slave processes
    num_processes = multiprocessing.cpu_count()  # Number of available CPU cores
    processes = []

    # Start slave processes
    for _ in range(num_processes):
        process = multiprocessing.Process(target=square_worker, args=(input_queue, output_queue))
        process.start()
        processes.append(process)

    # Assign tasks to the slave processes
    for number in numbers:
        input_queue.put(number)

    # Send termination signal to slave processes
    for _ in range(num_processes):
        input_queue.put(None)

    # Collect results from the output queue
    results = []
    for _ in range(len(numbers)):
        square = output_queue.get()
        results.append(square)

    # Wait for slave processes to complete
    for process in processes:
        process.join()

    return results


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = run_master_slave(numbers)
    print(results)
