a=0; b=0; c=0; d=0; s=0; i=0; f=0

# a, b, c, d - standard registers
# s - stack size
# i - instruction pointer
# f - flags


jumps = {
			int("02", 16):"EQL",
 			int("09", 16):"MORE", 
 			int("04", 16):"LESS", 
 		}

registers = {
			"a": int("02", 16),
 			"b": int("04", 16), 
 			"c": int("01", 16),
 			"d": int("08", 16), 
 			"s": int("10", 16), 
 			"i": int("40", 16), 
 			"f": int("20", 16),
		}

syscalls = {
			"read": int("01", 16),
 			"open": int("10", 16), 
 			"write": int("04", 16),
 			"exit": int("20", 16), 
		}



opcodes = {
			"MOV": int("02", 16),
 			"ADD": int("10", 16), 
 			"STK": int("40", 16),
 			"STM": int("04", 16), 
 			"LDM": int("80", 16), 
 			"CMP": int("01", 16), 
 			"SYS": int("08", 16),
 			"JMP": int("20", 16),
		}


f=open("code.txt", "r")

code=f.read().split()
f.close()

res=[]

def mov(i):
	res.append(opcodes['MOV'])
	res.append(registers[code[i+1]])
	res.append(int(code[i+2], 16))

def add(i):
	res.append(opcodes['ADD'])
	res.append(registers[code[i+1]])
	res.append(registers[code[i+2]])

def stk(i):
	res.append(opcodes['STK'])

	if code[i+1] == '0':
		res.append(0)
	else:
		res.append(registers[code[i+1]])

	if code[i+2] == '0':
		res.append(0)
	else:
		res.append(registers[code[i+2]])

def stm(i):
	res.append(opcodes['STM'])
	res.append(registers[code[i+1]])
	res.append(registers[code[i+2]])

def ldm(i):
	res.append(opcodes['LDM'])
	res.append(registers[code[i+1]])
	res.append(registers[code[i+2]])

def sys(i):
	res.append(opcodes['SYS'])
	res.append(syscalls[code[i+1]])
	if code[i+2] == '0':
		res.append(0)
	else:
		res.append(registers[code[i+2]])


for i in range(0, len(code), 3):
	if code[i] == 'MOV': mov(i)
	elif code[i] == 'ADD': add(i)
	elif code[i] == 'STK': stk(i)
	elif code[i] == 'STM': stm(i)
	elif code[i] == 'LDM': ldm(i)
	elif code[i] == 'SYS': sys(i)
	# elif code[i] == 'CMP': cmp(i)
	# elif code[i] == 'JMP': jmp(i)





# print(res)

code=res

kolejnosc = [2, 1, 3]
code2 = [0 for i in range(len(code))]
for i in range(0, len(code), 3):
	code2[i+kolejnosc.index(1)] = code[i]
	code2[i+kolejnosc.index(2)] = code[i+1]
	code2[i+kolejnosc.index(3)] = code[i+2]

print(code2)
