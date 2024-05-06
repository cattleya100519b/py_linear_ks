import numpy as np


def print_matrix(name_matrix: str, np_matrix) -> None:
    """numpy.ndarrayな行列をjupyter上にLaTeX形式で出力する
    
    Args:
        name_matrix (str): 行列の変数名
        np_matrix (numpy.ndarray): LaTeX 表示したい行列
    """
    from sympy import latex, Matrix
    from IPython.display import display, Math

    # numpy.ndarray >> sympy.Matrix >> LaTeX文字列 >> LaTeX数式
    display(Math(f'{name_matrix}={latex(Matrix(np_matrix))}'))