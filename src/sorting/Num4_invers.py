def Merge_sort(A):
	if len(A)<=1:
		return A,0
	L=A[0:len(A)//2]
	R=A[len(A)//2:len(A)]
	L,invl=Merge_sort(L)
	R,invr=Merge_sort(R)
	merged,inv=Merge(L,R)
	inv+=invl+invr
	return merged, inv



def Merge(A,B):
	i,j,k,Count=0,0,0,0
	C=[0]*(len(A)+len(B))
	while (k<len(C)):
		if (j==len(B) or (i<len(A) and A[i]<=B[j])):
			C[k]=A[i]
			i+=1
		else:
			C[k]=B[j]
			Count += (len(A) - i)
			j+=1
		k+=1
	return C,Count

inv=0
M=[]
def task():
    n = int(input())
    print(Merge_sort(list(map(int, input().split())))[1])
task()