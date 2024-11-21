import sys
def sext_decimal_to_binary(decimal_value, num_bits):
    decimal_value=int(decimal_value)
    sign_bit = decimal_value < 0
    binary_value = bin(abs(decimal_value))[2:].zfill(32)  # Assuming 32-bit representation
    if sign_bit:
        extended_binary_value = '1' * (num_bits - len(binary_value)) + binary_value
    else:
        extended_binary_value = '0' * (num_bits - len(binary_value)) + binary_value
    return extended_binary_value

def sext_binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number



r_type=["'0110011',"'0110011',"'0110011',"'0110011',
        "'0110011',"'0110011','0110011',
        "'0110011',"'0110011']

i_type=['0000011','0010011','0010011','1100111']

b_type=['1100011','1100011','1100011','1100011',
        '1100011','1100011']

s_type=['0100011']

u_type=['0110111','0010111']

j_type=['1101111']

bonus_type={"mul":'0000011',"rst":'0010011',"halt":'0010011',"rvrs":'1100111'}

r_func3=['000','000','001','010','011','100','101','110','111']
i_funt3=["010","000","011","000"]
s_funt3=["010"]
b_funt3=["000","001","100","101","110","111"]
bonus_funt3=["010","000","011","000"]


register_value={
        "00000":'00000000000000000000000000000000',
        '00001':'00000000000000000000000000000000',
        '00010':'00000000000000000000000000000000',
        '00011':'00000000000000000000000000000000',
        '00100':'00000000000000000000000000000000',
        '00101':'00000000000000000000000000000000',
        '00110':'00000000000000000000000000000000',
        '00111':'00000000000000000000000000000000',
        '01000':'00000000000000000000000000000000',
        '01001':'00000000000000000000000000000000',
        '01010':'00000000000000000000000000000000',
        '01011':'00000000000000000000000000000000',
        '01100':'00000000000000000000000000000000',
        '01101':'00000000000000000000000000000000',
        '01110':'00000000000000000000000000000000',
        '01111':'00000000000000000000000000000000',
        '10000':'00000000000000000000000000000000',
        '10001':'00000000000000000000000000000000',
        '10010':'00000000000000000000000000000000',
        '10011':'00000000000000000000000000000000',
        '10100':'00000000000000000000000000000000',
        '10101':'00000000000000000000000000000000',
        '10110':'00000000000000000000000000000000',
        '10111':'00000000000000000000000000000000',
        '11000':'00000000000000000000000000000000',
        '11001':'00000000000000000000000000000000',
        '11010':'00000000000000000000000000000000',
        '11011':'00000000000000000000000000000000',
        '11100':'00000000000000000000000000000000',
        '11101':'00000000000000000000000000000000',
        '11110':'00000000000000000000000000000000',
        '11111':'00000000000000000000000000000000'}
memory_value={
    "0x00010000":"00000000000000000000000000001011",
    "0x00010004":"00000000000000000000000000000011",
    "0x00010008":"00000000000000000000000000000000",
    "0x0001000c":"00000000000000000000000000000000",
    "0x00010010":"00000000000000000000000000000000",
    "0x00010014":"00000000000000000000000000000000",
    "0x00010018":"00000000000000000000000000000000",
    "0x0001001c":"00000000000000000000000000000000",
    "0x00010020":"00000000000000000000000000000000",
    "0x00010024":"00000000000000000000000000000000",
    "0x00010028":"00000000000000000000000000000000",
    "0x0001002c":"00000000000000000000000000000000",
    "0x00010030":"00000000000000000000000000000000",
    "0x00010034":"00000000000000000000000000000000",
    "0x00010038":"00000000000000000000000000000000",
    "0x0001003c":"00000000000000000000000000000000",
    "0x00010040":"00000000000000000000000000000000",
    "0x00010044":"00000000000000000000000000000000",
    "0x00010048":"00000000000000000000000000000000",
    "0x0001004c":"00000000000000000000000000000000",
    "0x00010050":"00000000000000000000000000000000",
    "0x00010054":"00000000000000000000000000000000",
    "0x00010058":"00000000000000000000000000000000",
    "0x0001005c":"00000000000000000000000000000000",
    "0x00010060":"00000000000000000000000000000000",
    "0x00010064":"00000000000000000000000000000000",
    "0x00010068":"00000000000000000000000000000000",
    "0x0001006c":"00000000000000000000000000000000",
    "0x00010070":"00000000000000000000000000000000",
    "0x00010074":"00000000000000000000000000000000",
    "0x00010078":"00000000000000000000000000000000",
    "0x0001007c":"00000000000000000000000000000000"
}
pc=0
input=sys.argvs[-2]
output=sys.argvs[-1]
input_file=open(input)
machine_code=input_file.readlines()
output=open(output,'a')
while sext_binary_to_decimal(pc)<len(machine_code):
    code=machine_code[sext_binary_to_decimal(pc//4)]
    opcode=code[-7:]
    func3=code[-15:-12]
    func7=code[-32:-25]
    if(opcode=="1101111"):
            r=code[-12:-7]
            imm=code[-32]+code[-20:-12]+code[-21]+code[-31:-21]+"0"
            register_value[r]=sext_decimal_to_binary(sext_binary_to_decimal(pc)+4,32)
            pc=sext_decimal_to_binary(sext_binary_to_decimal(pc)+int(imm),32)
    if(opcode=="0110011"):
        rd=code[-7:-12]
        rs1=code[-15:-20]
        rs2=code[-20:-25]
        if(func3=='000'):
            if(func7=="0000000"):
                register_value[rd]=sext_decimal_to_binary(sext_binary_to_decimal(register_value[rs1])+sext_binary_to_decimal(register_value[rs2]))
            if(func7=="0100000"):
                register_value[rd]=sext_decimal_to_binary(sext_binary_to_decimal(register_value[rs1])-sext_binary_to_decimal(register_value[rs2]))
        elif(func3=="001"):
            shift=int(register_value[-5:],2)
            register_value[rd]=(register_value[rs1]+"0"*shift)[-32:]
        elif(func3=="010"):
            if(sext_binary_to_decimal(register_value[rs1]) < sext_binary_to_decimal(register_value[rs2])):
                register_value[rd] = sext_decimal_to_binary("1")
        
        elif(func3 == "011"): #sltu operation
            if(int(register_value[rs1], 2) < int(register_value[rs2],2)):
                register_value[rd] = sext_decimal_to_binary("1")
            
        elif(func3 == "100"): #xor operation
            register_value[rd] = register_value[rs1] ^ register_value[rs2]
            
        elif(func3 == "101"): #srl operation
            shift = int(register_value[rs2][-5:],2)
            register_value[rd]=("0"*shift+register_value[rs1])[:32]
            
        elif(func3 == "110"): #or operation
            register_value[rd] = register_value[rs1] or register_value[rs2]
            
        elif(func3 == "111"): #and operation
            register_value[rd] = register_value[rs1] and register_value[rs2]
        pc+=4
    if(opcode in i_type):
        temp=pc
        line = line[::-1]
        opcode = line[0:7][::-1]
        rd = line[7:12][::-1]
        func3 = line[12:15][::-1]
        rs1 = line[15:20][::-1]
        imm = line[20:32][::-1]
        
        if(func3 == "010"): #lw operation
            rs1_val = sext_binary_to_decimal(register_value[rs1]) 
            imm_val = sext_binary_to_decimal(imm)
            
            print(rs1_val)
            print(imm_val)
            temp = rs1_val + imm_val #integer value
            print(temp)
            register_value[rd] = memory_value["0x000" + str(hex(temp))[2:]]
        
        elif(func3 == "000" and opcode == "0010011"):  #addi operation
            rs1_val = sext_binary_to_decimal(register_value[rs1]) 
            imm_val = sext_binary_to_decimal(imm)
            temp = rs1_val + imm_val #integer value
            
            register_value[rd] = sext_decimal_to_binary(str(temp))
            
        elif(func3 == "011"):    #sltiu operation
            if(int(rs1,2)<int(imm,2)):
                register_value[rd] = sext_decimal_to_binary("1")
                
        elif(func3 == "000" and opcode == "1100111"):
            val = pc
            val +=4
            register_value[rd] = sext_decimal_to_binary(str(val))
            
            pc = sext_binary_to_decimal(register_value[rs1]) + sext_binary_to_decimal(imm)
        if(temp == pc):
            pc+=4
    if(opcode in b_type):
        imm = line[0]+line[-8]+line[1:7]+line[-12:-8]+'0'
        rs1 = line[-20:-15]
        rs2 = line[-25:-20]
        rs1_sig_val = sext_binary_to_decimal(register_value[rs1])
        rs2_sig_val = sext_binary_to_decimal(register_value[rs2])
        rs1_unsig_val = int(register_value[rs1], 2)
        rs2_unsig_val = int(register_value[rs2], 2)
    
        imm_val = sext_binary_to_decimal(imm)
    
        if (func3 == "000"):
            if (rs1_sig_val == rs2_sig_val):
                pc += imm_val
        elif (func3 == "001"):
            if (rs1_sig_val != rs2_sig_val):
                pc += imm_val
        elif (func3 == "100"):
            if (rs1_sig_val < rs2_sig_val):
                pc += imm_val
        elif (func3 == "101"):
            if (rs1_sig_val >= rs2_sig_val):
                pc += imm_val
        elif (func3 == "110"):
            if (rs1_unsig_val < rs2_unsig_val):
                pc += imm_val
        elif (func3 == "111"):
            if (rs1_unsig_val >= rs2_unsig_val):
                pc += imm_val
        if(pc==temp):
            pc+=4
    if(opcode in s_type):
        rs2 = line[-25:-20]
        rs1 = line[-20:-15]

        imm = line[-32:-25] + line[-12:-7]

        imm_dec = sext_binary_to_decimal(imm)
        rs1_dec = sext_binary_to_decimal(register_value[rs1])

        add = imm_dec+rs1_dec

        memory_value["0x000"+hex(add)[2:]] = register_value[rs2]
    if(opcode in u_type):
        rd = line[-12:-7]
        imm = line[-32:-12]

        imm = imm + 12*'0'

        if opcode=="0110111":
            #lui
            register_value[rd]=imm
        else:
            #auipe
            register_value[rd]= sext_decimal_to_binary(str(pc + sext_binary_to_decimal(imm)))








    if(opcode in bonus_type and func3 in bonus_funt3):
        if(opcode=="0000011"):#mul
            rd,rs1,rs2=code.split()[1].split(',')
            register_value[rd]=sext_decimal_to_binary(sext_binary_to_decimal(rs1)*sext_binary_to_decimal(rs2),32)

        elif(opcode=="0010011" and func3=="000"):#rst
            for i in register_value:
                register_value[i]=0

        elif(opcode=="0010011" and func3=="011"):#halt
            break

        elif(opcode=="1100111"):#rvrs
            rd=code[7:12]
            rs1=code[15:20]
            rs2=code[20:25]
            register_value[rd]=register_value[rs1][::-1]

    outputcode=""
    for i in register_value.keys():
        outputcode+=register_value[i]+" "
    output.write(outputcode)
outputcode=[]
for i in memory_value.keys():
    outputcode.append(i,':',"0b"+memory_value[i])
output.writelines(outputcode)
