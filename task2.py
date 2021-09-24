import sys
if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = "task2_data.txt"
file = open(path)
content = file.read()
file.close()
#if len(sys.argv) > 1:
#	content = sys.argv[1]
#else:
#	content = "1 2 3 4 5 6 10"
data = [int(x) for x in content.split()]

maxOstZero = -1
maxOstOne = -1
R1 = 1
maxOstTwo1 = -1
maxOstTwo2 = -1
R2 = 1
#for i in range (0, len(data)-2):
#	for j in range (i, len(data)-2):
#		maybeR = data[i]+data[j]
#		if maybeR > trueR and maybeR%3==1:
#			trueR = maybeR
for num in data[:len(data)-1]:
	if num > maxOstZero and num % 3 == 0:
		maxOstZero = num
	if num > maxOstOne and num % 3 == 1:
		maxOstOne = num
	if num > maxOstTwo1 and num % 3 == 2:
		maxOstTwo1 = num
	elif num > maxOstTwo2 and num % 3 == 2:
		maxOstTwo2 = num
if maxOstZero != -1 and maxOstOne != -1:
	R1 = maxOstZero + maxOstOne
if maxOstTwo1 != -1 and maxOstTwo2 != -1:
	R2 = maxOstTwo1 + maxOstTwo2
print('Counted R:', max(R1,R2), ' Input R:', data[len(data)-1])
if max(R1,R2) != data[len(data)-1]:
	print('Контрольное значение неверно')
else:
	print('Контрольное значение верно')
