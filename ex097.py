def escreva(txt):
    tam = len(txt) + 4
    print("~"*tam)
    print(f"  {txt}")
    print("~"*tam)

msg = input("Digite uma mensagem: ")
escreva(msg)