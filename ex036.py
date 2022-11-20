from time import sleep

valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Digite o tempo do financiamento: "))
parcela = valor/(anos*12)
print("\033[33mProcessando...\033[m")
sleep(2)
if parcela > salario*30/100:
    print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos, a parcela fica de R${parcela:.2f}.")
    print("Empréstimo \033[31mNEGADO!\033[m")
else:
    print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos, a parcela fica de R${parcela:.2f}.")
    print("Empréstimo \033[32mCONCEDIDO!\033[m")
