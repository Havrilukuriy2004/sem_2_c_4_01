import threading
import queue
import time
import os

input_file = 'input.txt'

T1 = 1  # Час для зчитування рядка
T2 = 2  # Час для обробки рядка у другому потоці
T3 = 3  # Час для обробки рядка у третьому потоці

line_queue = queue.Queue()

output_file1 = f'{os.path.splitext(input_file)[0]}_output1.txt'
output_file2 = f'{os.path.splitext(input_file)[0]}_output2.txt'


def read_file():
    with open(input_file, 'r') as f:
        for line in f:
            line_queue.put(line)
            time.sleep(T1)
    line_queue.put(None)
    line_queue.put(None)

def process_file1():
    with open(output_file1, 'w') as f:
        while True:
            line = line_queue.get()
            if line is None:
                break
            time.sleep(T2)
            f.write(line)
            line_queue.task_done()

def process_file2():
    with open(output_file2, 'w') as f:
        while True:
            line = line_queue.get()
            if line is None:
                break
            time.sleep(T3)
            f.write(line)
            line_queue.task_done()

thread_reader = threading.Thread(target=read_file)
thread_processor1 = threading.Thread(target=process_file1)
thread_processor2 = threading.Thread(target=process_file2)
thread_reader.start()
thread_processor1.start()
thread_processor2.start()
thread_reader.join()
thread_processor1.join()
thread_processor2.join()
