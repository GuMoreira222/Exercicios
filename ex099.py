from time import sleep

def maior(*nums):
    m = 0
    print("-="*30)
    print("Analisando os valores passados.")
    for c, n in enumerate(nums):
        if c == 0:
            m = n
        else:
            if n > m:
                m = n
        print(n, end=' ')
        sleep(0.5)
    print(f"Foram informados {len(nums)} valores ao todo.")
    print(f"O maior valor informado foi {m}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()