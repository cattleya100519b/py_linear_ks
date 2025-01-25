def disp_mat(name_mat: str, mat: any) -> None:
    """jupyter上に行列をLaTeX表示で出力する関数
    
    Args:
        name_mat (str): 行列の変数名
        mat: LaTeX 表示したい行列
    """
    from IPython.display import display, Math
    from sympy import latex, Matrix

    # numpy.ndarray(etc.) >> sympy.Matrixインスタンス >> LaTeX文字列 >> LaTeX数式
    display(Math(f'{name_mat}={latex(Matrix(mat))}'))