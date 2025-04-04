# ParallelRunner

## Overview
`ParallelRunner` is a Python utility for executing functions in parallel using the `multiprocessing` module. It allows you to distribute workloads across multiple CPU cores, making it ideal for computationally intensive tasks.

### Features:
- Run functions in parallel with controlled concurrency.
- Supports both normal and array-based arguments.
- Optionally track progress using `tqdm`.
- Handles errors gracefully without stopping execution.
- Supports indexed execution if needed.

## Installation
```sh
pip install parallel-runner
```

## Usage
### Basic Example
```python
from parallel_runner import ParallelRunner

def sample_task(ix, x, y):
    return x + y + ix  # Example function that takes indexed arguments

runner = ParallelRunner(
    procedure=sample_task,
    concurrency=4,
    ix_needed=True,
    use_tqdm=True,
    array_args={"x": [1, 2, 3, 4], "y": [10, 20, 30, 40]},
)

results = runner.run()
print(results)  # Outputs: {0: 11, 1: 23, 2: 35, 3: 47}
```

### Example: Processing Large Data Sets
```python
import time
from parallel_runner import ParallelRunner

def process_data(data_chunk):
    time.sleep(1)  # Simulate a long computation
    return sum(data_chunk)

data = [[i for i in range(100)] for _ in range(10)]
runner = ParallelRunner(
    procedure=process_data,
    concurrency=5,
    array_args={"data_chunk": data},
)

results = runner.run()
print(results)  # Outputs sum of each chunk
```

### Example: Web Scraping in Parallel
```python
import requests
from parallel_runner import ParallelRunner

def fetch_page(ix, url):
    response = requests.get(url)
    return len(response.content)

urls = ["https://example.com" for _ in range(10)]
runner = ParallelRunner(
    procedure=fetch_page,
    concurrency=5,
    ix_needed=True,
    array_args={"url": urls},
)

results = runner.run()
print(results)  # Outputs content length for each page
```

## Parameters
| Parameter       | Type      | Description |
|----------------|----------|-------------|
| `procedure`    | function | The function to run in parallel. |
| `debug`        | bool     | If True, runs sequentially for debugging. |
| `concurrency`  | int      | Number of parallel processes. |
| `ix_needed`    | bool     | If True, passes an index (`ix`) to the function. |
| `use_tqdm`     | bool     | If True, displays a progress bar. |
| `no_iteration` | int      | Number of iterations (if `array_args` is empty). |
| `normal_args`  | dict     | Arguments passed unchanged to all function calls. |
| `array_args`   | dict     | Arguments that vary per process (lists must have the same length). |

## License
This project is licensed under the MIT License.

