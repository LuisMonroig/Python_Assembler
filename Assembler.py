

if __name__ == "__main__":
    instruction = input("Please enter the assembly instruction: ")

    mnemonic = instruction.split(" ")[0]
    print("Mnemonic:",mnemonic)                     #tracer bullet to aid development

    computers_ISA = {"LOD":"00010000" , "STO":"00010001",  "ADD":"00100000",
                     "SUB":"00100001",  "JMP":"00110000",  "HLT": "11111111"}

    instructions_list = instruction.split(" ",1)
    print(instructions_list)

    registers = instructions_list[1].replace(" ","")
    print(registers)

    register_list = registers.split(",")

    num_reg1 = register_list[0][1:]  # i values of register Ri
    num_reg2 = register_list[1][1:]  # will be used in elifs below
    num_reg3 = register_list[2][1:]

    if mnemonic not in computers_ISA:
        print("There was a problem with the instruction mnemonic. Please consult the ISA documentation.\n\n")

    else:
        if len(register_list) != 3:
            print("Few or to many registers! Please, try again.\n\n")

        elif not (register_list[0][0] == register_list[1][0] == register_list[2][0] == "R"):
            print("Invalid register name! Please, provide a register with the form Ri where I is a natural number.\n\n")

        elif not (num_reg1.isnumeric() and num_reg2.isnumeric() and num_reg3.isnumeric()):
            print("Invalid register! Reister name is not accompanied only by an integer.\n\n")

        elif not(0 < int(num_reg1) < 256 and 0 < int(num_reg2) < 256 and 0 < int(num_reg3) < 256):
            print("Invalid register number! There most be integer from 0 to 255 besides the register name.\n\n")
        else:
            num_reg_binary  = [bin(int(num_reg1)).replace('0b',""), bin(int(num_reg2)).replace('0b',""), bin(int(num_reg3)).replace('0b',"")]
            zero_byte = "00000000"
            for index in range(3):
                num_reg_binary[index] = zero_byte[0:8-len(num_reg_binary[index])] + num_reg_binary[index]
                print(num_reg_binary[index])

            machine_code = computers_ISA[mnemonic] + num_reg_binary[0] + num_reg_binary[1] + num_reg_binary[2]
            print("The translation of the assembly instruction into machine code is:", machine_code,)
