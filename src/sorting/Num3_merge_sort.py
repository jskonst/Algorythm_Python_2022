"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'1',\
'1'\
]))
>>> task_merge_sort()
1
>>> sys.stdin = io.StringIO(chr(10).join([\
'2',\
'3 1',\
]))
>>> task_merge_sort()
1 2 1 3
1 3 
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'5 4 3 2 1',\
]))
>>> task_merge_sort()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5 
>>> print(merge([2,3,4],[1,2,3]))
[1, 2, 2, 3, 3, 4]
"""

n = int(input())
res = []
for i in range(n):
    number, value = map(int, input().split())
    res.append([number, value])
for i in range(n-1):
    for j in range(n-i-1):
        if res[j][1] < res[j+1][1]:
            res[j], res[j+1] = res[j+1], res[j]
        if res[j][1] == res[j+1][1]:
            if res[j][0] > res[j+1][0]:
                res[j], res[j+1] = res[j+1], res[j]
print()
[print(i[0], i[1]) for i in res]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)