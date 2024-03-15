a=0; b=0; c=0; d=0; s=0; i=0; f=0

# a, b, c, d - standard registers
# s - stack size
# i - instruction pointer
# f - flags

opcodes = {
			int("10", 16):"MOV",
 			int("08", 16):"ADD", 
 			int("04", 16):"STM", 
 			int("20", 16):"LDM", 
 			int("80", 16):"CMP", 
 			int("40", 16):"SYSCALL", 
 			int("02", 16):"STK",
 			int("01", 16):"JMP"
 			# int("06", 16):"PUSH", 
 			# int("07", 16):"POP"
 		}

jumps = {
			int("02", 16):"EQL",
 			int("09", 16):"MORE", 
 			int("04", 16):"LESS", 
 		}

registers = {
			int("10", 16):"a",
 			int("08", 16):"b", 
 			int("04", 16):"c", 
 			int("20", 16):"d", 
 			int("80", 16):"s", 
 			int("40", 16):"i", 
 			int("02", 16):"f",

 		}

syscalls = {
			int("04", 16):"read",
 			int("10", 16):"write", 
 		}

f=open("vmcode.txt", "r")

vmcode=f.read().split()
f.close()


for i in range(len(vmcode)):
	vmcode[i]=int(vmcode[i], 16)

kolejnosc = [2, 1, 3]


vmcode2 = [0 for i in range(len(vmcode))]

for i in range(0, len(vmcode), 3):
	vmcode2[i] = vmcode[i + kolejnosc.index(1)]
	vmcode2[i+1] = vmcode[i + kolejnosc.index(2)]
	vmcode2[i+2] = vmcode[i + kolejnosc.index(3)]

print(vmcode)
print("\n\n")
print(vmcode2)
vmcode = vmcode2

klucze = opcodes.keys()
for i in range(0, len(vmcode), 3):
	if vmcode[i] not in klucze:
		print("UNKNOWN")
		continue
	# print(hex(vmcode[i]))
	print(opcodes[vmcode[i]])


