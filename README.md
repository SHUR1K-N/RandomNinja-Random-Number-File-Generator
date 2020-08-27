# RandomNinja: The Random Number File Generator

A fast random number file generator (500,000+ lines per second) I created, that takes the following as input:

- A custom range of integers to generate within
- The maximum number of lines to be generated
- Method (either allow duplicating values or disallow)
- Output location for the generated .txt file

...and then generates a text document of randomized integers within the specified constraints; also supports zero-redundancy (non-repeating values). Ideal to aid in benchmarking sorting algorithms or any general usage scenario where large sets of random integers may be reqired (such as statistics). This project was created in Python, primarily for the purpose of testing my own [Double-Edged Sorting algorithm's](https://github.com/SHUR1K-N/Double-Edged-Sort) performance.

**Dependencies you may have to "pip install" before being able to run the Python file(s):**

**tqdm** (for progress bars)

**colorama** (for colors)

**termcolor** (for colors)

My website: http://bit.do/SHUR1KN
