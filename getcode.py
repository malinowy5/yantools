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
			int("04", 16):"a",
 			int("40", 16):"b", 
 			int("08", 16):"c", 
 			int("02", 16):"d", 
 			int("20", 16):"s", 
 			int("10", 16):"i", 
 			int("90", 16):"f",
 			int("00", 16):"none",

 		}

syscalls = {
			int("08", 16):"read",
 			int("10", 16):"write", 
 			int("02", 16):"exit",
 			int("20", 16):"open",
 		}


def mov(arg1, arg2):
	print("MOV", end=' ')
	print(registers[arg1], end=' ')
	print("=", end=' ')
	print(hex(arg2))

def add(arg1, arg2):
	print("ADD", end=' ')
	print(registers[arg1], end=' ')
	print("+=", end=' ')
	print(registers[arg2])

def stm(arg1, arg2):
	print("STM *", end='')
	print(registers[arg1], end=' ')
	print("=", end=' ')
	print(registers[arg2])

def ldm(arg1, arg2):
	print("LDM", end=' ')
	print(registers[arg1], end=' ')
	print("= *", end='')
	print(registers[arg2])

def cmp(arg1, arg2):
	print("CMP", end=' ')
	print(registers[arg1], end=' ')
	print("?=", end=' ')
	print(registers[arg2])

def sys(arg1, arg2):
	print("SYSCALL", end=' ')
	print(syscalls[arg1], end='')
	print(",", end=' ')
	print(registers[arg2])

def stk(arg1, arg2):
	if (arg1!=0):
		print("POP", end=' ')
		print(registers[arg1])

	if (arg2!=0):
		print("PUSH", end=' ')
		print(registers[arg2])

def jmp(arg1, arg2):
	print("JMP", end=' ')
	print('flg', end='')
	print(",", end=' ')
	print(registers[arg2])

opcodes = {
			int("02", 16): mov,
 			int("04", 16): add, 
 			int("20", 16): stk,
 			int("08", 16): stm, 
 			int("40", 16): ldm, 
 			int("01", 16): cmp, 
 			int("10", 16): sys,
 			int("80", 16): jmp,
		}


f=open("vmcode.txt", "r")

vmcode=f.read().split()
f.close()


for i in range(len(vmcode)):
	vmcode[i]=int(vmcode[i], 16)

kolejnosc = [3, 1, 2]


vmcode2 = [0 for i in range(len(vmcode))]

for i in range(0, len(vmcode), 3):
	vmcode2[i] = vmcode[i + kolejnosc.index(1)]
	vmcode2[i+1] = vmcode[i + kolejnosc.index(2)]
	vmcode2[i+2] = vmcode[i + kolejnosc.index(3)]

# print(vmcode)
# print("\n\n")
# print(vmcode2)
vmcode = vmcode2

klucze = opcodes.keys()
for i in range(0, len(vmcode), 3):
	if vmcode[i] not in klucze:
		print("UNKNOWN " + hex(vmcode[i]))
		continue
	# print(hex(vmcode[i]))
	opcodes[vmcode[i]](vmcode[i+1], vmcode[i+2])



