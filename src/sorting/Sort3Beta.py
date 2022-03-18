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
			j+=1
			if j==1:
				print(min(B[-1][1],A[-1][1]),max(B[0][1],A[0][1]),min(B[0][0],A[0][0]),max(B[-1][0],A[-1][0]))
		k+=1
	return C




s=0
String=''
Start=[]
n=int(input())
M=[0]*n
Start=(list(map(int,input().split())))
for i in range(0,n):
	M[i]=[Start[i],i+1]
M=Merge_sort(M)
for i in range(n):
	String=str(M[i][0])+" "+String
print(String)