"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['4','4 3 2 1']))  # input
>>> bubble_sort()
3 4 2 1
3 2 4 1
3 2 1 4
2 3 1 4
2 1 3 4
1 2 3 4
"""

def bubble_sort():
    n = input()
    inp_string = input()
    str_lst = inp_string.split(" ")
    print(str_lst)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)