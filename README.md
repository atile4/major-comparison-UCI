# UCI Major Comparer

 ```
----------------------------------------
|         UCI Major Comparison         |
|                                      |
|           written by atile           |
----------------------------------------
```


Generates a list of overlapping courses between two majors from the University of California Irvine Catalogue

## Requirements
Python 3.7 interpreter

Modules in requirements.txt

## Installation
1. Download the .py files in majorcomparer folder
2. Run main.py

## Known Issues
- No distinction between B.S and B.A for majors

- Does not include any minors or Masters programs

- If multiple courses are listed in one column on the UCI course requirement catalogue, it will be counted as one course.

- If there are no overlapping courses under a major's subheader, that subheader will still be printed out with no distinction.

- If, on the UCI website, courses are listed in different tables, the program will only read the first table.
