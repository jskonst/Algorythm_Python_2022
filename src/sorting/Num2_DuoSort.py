def Answ():
	num=int(input())
	mas=[]
	for i in range(num):
		mas.append(list(map(int,input().split())))
		mas.sort(key = lambda x: x[1], reverse=True)
	for j in range(num-1):
		for i in range(0,num-j-1):
			if mas[i][1]==mas[i+1][1] and mas[i][0]>=mas[i+1][0]:
				mas[i][0],mas[i+1][0]=mas[i+1][0],mas[i][0]
	for i in range(num):
		print(mas[i][0],mas[i][1])
Answ()