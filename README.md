# RandomNinja: Random Number File Generator

## Description & Usage
A fast random number file generator (500,000+ lines per second), that takes the following as input:

- A custom range of integers to generate within
- The maximum number of lines to be generated
- Method (either allow duplicating values or disallow)
- Output location for the generated .txt file

...and then generates a text document of randomized integers within the specified constraints; also supports zero-redundancy (non-repeating values). Ideal to aid in benchmarking sorting algorithms or any general usage scenario where large sets of random integers may be reqired (such as statistics).

<div align="center">
<img src="https://github.com/SHUR1K-N/RandomNinja-Random-Number-File-Generator/blob/master/Images/Example.png" >
<p>Example Execution</p>
</div>

This project was created in Python, primarily for the purpose of testing my own [**Double-Edged Sorting algorithm's**](https://github.com/SHUR1K-N/Double-Edged-Sort) performance.

## Dependencies to PIP-Install
- **tqdm** (for progress bars)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
