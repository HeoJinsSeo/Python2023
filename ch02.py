#-*- coding:utf-8 -*-

def sum(a, b):
    """숫자의 합을 구하는 함수입니다.
    Args:
        a (int): 숫자
        b (int): 숫자

    Returns:
        int
    """
    c = a + b
    return c

if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    result = sum(a, b)
    print(result)
    
    docstring = sum.__doc__
    border = '#' * 20
    print('{}\n{}\n'.format(border, docstring, border))