from time import sleep

def foo(lst):
	lst[2] = str(int(lst[2]) - 1)

def countdown(ListInp, count):
	for i in range(count):
		if ListInp[2] == ListInp[1] == ListInp[0] == '00' :
			ListInp[0] = '23'
			ListInp[1] = '59'
			ListInp[2] = '59'
		elif ListInp[2] == ListInp[1] == '00':
			ListInp[1] = '59'
			ListInp[2] = '59'
		elif ListInp[2] == '00':
			ListInp[2] = '59'
		else:
			foo(ListInp)
		print(":".join(ListInp))
		sleep(1)

inp = input("Insert time to countdown style. (00:00:00)\n>>> ").strip()
count = input("Insert score of countdown\n>>> ").strip()

inp = inp.split(':')
if (len(inp) == 3 and 0 <= int(inp[0]) <= 23 and 0 <= int(inp[1]) <= 59 and 
	0 <= int(inp[2]) <= 59 and count.isdigit()):
	countdown(inp, int(count))
else:
	print("invalid input")
