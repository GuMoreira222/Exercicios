e = input("Digite uma expressão: ")
pilha = list()
for s in e:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")




