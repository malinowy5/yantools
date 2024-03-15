a=0; b=0; c=0; d=0; s=0; i=0; f=0

f=open("vmcode.txt", "r")

vmcode=f.read().split()


for i in range(len(vmcode)):
	vmcode[i]=int(vmcode[i], 16)

kolejnosc = [2, 1, 3]


if kolejnosc[0]!=1:
	for i in range(0, len(vmcode), 3):
		vmcode[i], vmcode[i+kolejnosc[0]-1] = vmcode[i+kolejnosc[0]-1], vmcode[i]

print(vmcode)
kolejnosc[0], kolejnosc[kolejnosc[0]-1] = kolejnosc[kolejnosc[0]-1], kolejnosc[0]
print(kolejnosc)


# opcodes = {int("10", 16):"MOV", int("01", 16):"ADD", int("04", 16):"STM", int("03", 16):"LDM", int("02", 16):"CMP", int("05", 16):"SYSCALL", int("06", 16):"PUSH", int("07", 16):"POP"}
# klucze = opcodes.keys()
# for i in range(0, len(vmcode), 3):
# 	if vmcode[i] not in klucze:
# 		continue
# 	print(opcodes[vmcode[i]])


