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
	n=int(input())
	mas=list(map(int, (input().split())))
	for i in range(n-1):
	    for j in range(n-i-1):
	        if mas[j] > mas[j+1]:
	            mas[j], mas[j+1] = mas[j+1], mas[j]
	            print(" ".join(map(str, mas)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)