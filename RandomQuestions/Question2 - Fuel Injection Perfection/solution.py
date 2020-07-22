def solution(n:int)-> int:
    table = {1: 0, 2: 1}
    def fuel(n):
        if n in table:
            return table[n]
        if n % 2 != 0:
            #agar odd hai to +1 ya -1 karo aur minimum nikalo lekin steps 2 hi add honge so this way
            table[n] = min(fuel((n + 1) / 2) + 2,
                           fuel((n - 1) / 2) + 2)
        else:
            table[n] = fuel(n / 2) + 1
        return table[n]
    return fuel(n)
print(solution(int(input())))
