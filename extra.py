def can_unlock(x):
    while x > 0:

        x_str = str(x)
        if '33' in x_str:
            x_str = x_str.replace('33', '')
            x = int(x_str) if x_str else 0
        else:

            if x >= 33:
                x -= 33
            else:
                break  


    return x == 0


t = int(input())  
results = []

for _ in range(t):
    x = int(input())
    if can_unlock(x):
        results.append("YES")
    else:
        results.append("NO")


print("\n".join(results))
