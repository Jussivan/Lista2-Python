Num = []
for i in range (5):
    num = int(input(f"Digite o {i+1}° número: "))
    Num.append(num)
novo_num = int(input("adcione um outro número:"))
Num.append(novo_num)
print("Os números são : ", Num)