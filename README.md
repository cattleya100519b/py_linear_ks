## jupyter内 LaTeX (markdown)
1. 行列
$$
    \boldsymbol{A} =
        \begin{pmatrix}
        1 & 4 & -3 \\
        -2 & 1 & 2 \\
        \end{pmatrix} \quad
    \boldsymbol{B} =
        \begin{pmatrix}
        2 & -3 & 5 \\
        -1 & 4 & 1 \\
        \end{pmatrix}
$$

## jupyter内 LaTeX (display)
1. 行列
```python
from sympy import latex, Matrix
from IPython.display import display, Math

# numpy.ndarray >> sympy.Matrix >> LaTeX文字列 >> LaTeX数式
display(Math(f'C={latex(Matrix(C))}'))
```