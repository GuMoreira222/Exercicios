nums = [[], []]
for c in range(1,8):
    n = int(input(f"Digite o {c}º número: "))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print(f"Os números pares são {nums[0]}")
print(f"Os números ímpares são {nums[1]}")