def Merge_sort(A):
	if len(A)<=1:
		return A
	L=A[0:(len(A)//2)]
	R=A[len(A)//2:len(A)]
	L=Merge_sort(L)
	R=Merge_sort(R)
	return Merge(L,R)



def Merge(A,B):
	i,j,k=0,0,0

	C=[0]*(len(A)+len(B))
	while (k<len(C)):
		
		if (j==len(B) or (i<len(A) and A[i][0]<=B[j][0])):
			
			C[k]=A[i]
			i+=1
		else:
			C[k]=B[j]
			print(min(B[j][1],A[i][1]),max(B[j][1],A[i][1]),min(B[j][0],A[i][0]),max(B[j][0],A[i][0]))
			j+=1
		k+=1
		#print(A,B,C)
	return C

s=0
Start=[]
n=int(input())
M=[0]*n
Start=(list(map(int,input().split())))
for i in range(0,n):
	#print(i)
	M[i]=[Start[i],i+1]
	#print(M)
M=Merge_sort(M)
print('--',M)