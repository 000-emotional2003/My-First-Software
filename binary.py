print('===========================')
print('===========================')
print('     Decimal to Binary     ')
print('===========================')

#getting your number on a variable
#colocando o numero em uma variavel

num = int(input('Type the decimal value: '))

#just skipping lines so the script dont get dirty when runned
#apenas pulando linhas pro escript nao ficar sujo quando executado



print('\n')

#creating a list to receive the bytes
#and using *50 to add 50 empty spaces on the list
#so the python interpreter dont interpret the list as completely void or empty

#criando uma lista para receber os bytes 
#e usando *50 para adicionar 50 casas na lista
#e o python nao interpretar como uma lista vazia

bin = []*50

#running a loop to execute a code while num is not 0
#rodando um loop para executar um codigo enquanto num e diferente de 0

while num != 0:

#resto receive the  rest of the division of num for 2
#num receive the result of num divided by 2
#bin.append() puts the resto representing the binary bytes in the list

#resto recebe o resto da divisao de  num para 2
#num recebe o resultado de num dividido por 2
#bin.append() coloca o resto representando cada byte binario na lista 

   resto = num % 2
   num = num // 2
   bin.append(resto)

#reverse the result to not getting the rusult backwards
#revertendo o resultado para nao ter ele ao contrario 

bin.reverse()

#running a loop that print each byte of the list without brackets so it gets more readable
#rodando um loop que printa cada byte da lista sem os colchetes assim fica mais legivel

for byte in bin:
   print('  ', byte, end="")

print('\n')
