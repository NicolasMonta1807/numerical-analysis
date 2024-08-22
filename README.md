
# PLU Solver

Python implementation to solve a linear equation system using PLU factorization.

## Installation

- Clone this repo

```shell
git clone https://github.com/NicolasMonta1807/plu-solver.git
```

- Dependencies
```shell
pip install numpy 
```

## Usage

Input the problem's matrix using a csv format

```shell
0,0.125,0.25,0.5
0.5,0,0,0
0,0.25,0,0
0,0,0.125,0
```

*Note: Use decimal notation instead of fractions*

Run the program
```shell
python3 main.py <filename>
```

The program will ask for the solution vector 'b':
```python
Input solution vector 'b':
175,100,50,25
```


*Note: Input values using comma as separator*

This will give you the solution for Ax = b:

```python
Solution:
[200. 200. 200. 200.]
```

In case you want to get all the PLU factorization matrices, use the `verbose` flag
```shell
python3 main.py <filename> verbose
```
```python
P-Transposed:
[[0. 0. 1. 0.]
 [1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 0. 1.]]
L:
[[1.  0.  0.  0. ]
 [0.  1.  0.  0. ]
 [0.  0.5 1.  0. ]
 [0.  0.  0.5 1. ]]
U:
[[ 0.5   0.    0.    0.  ]
 [ 0.    0.25  0.    0.  ]
 [ 0.    0.    0.25  0.5 ]
 [ 0.    0.    0.   -0.25]]
 ```