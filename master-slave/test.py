import unittest
from multiprocessing import Process, Queue
import queue

from main import square_worker, run_master_slave


class TestMasterSlave(unittest.TestCase):
    def test_square_worker(self):
        input_queue = Queue()
        output_queue = Queue()

        # Put numbers into the input queue
        input_queue.put(2)
        input_queue.put(4)
        input_queue.put(6)
        input_queue.put(None)  # Termination signal

        # Create and start the worker process
        process = Process(target=square_worker, args=(input_queue, output_queue))
        process.start()

        # Retrieve results from the output queue
        results = []
        while True:
            try:
                square = output_queue.get(timeout=1)  # Set a timeout to avoid getting stuck
                if square is None:
                    break
                results.append(square)
            except queue.Empty:  # Use queue.Empty instead of Queue.Empty
                break

        process.join()

        self.assertEqual(results, [4, 16, 36])

    def test_run_master_slave(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        results = run_master_slave(numbers)

        self.assertEqual(sorted(results), sorted([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))


if __name__ == '__main__':
    unittest.main()
