fd = open('freq.txt', 'r')
for line in fd.readlines():
    line = line.strip('\n')
    (f, w) = line.split('\t')

for i in list:
	if token in (f, w):
		print(token)
	else:
		print("*" + token)