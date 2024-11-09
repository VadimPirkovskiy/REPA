n = str(input())
k = len(n)
c = 0
for i in range(0, k ):
    if n[i]=="а" or n[i]=='А' or n[i]=="a" or n[i]=='A' :
        c+=1
n = n.replace('а' , 'о')#кирилица
n = n.replace('a' , 'o')#латиница
n = n.replace('А' , 'О')#кирилица
n = n.replace('A' , 'O')#латиница
print('Замен:' , c)
print("Символов:" , k)
print("Строка с заменой:", n )