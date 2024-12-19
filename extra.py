def remove_consecutive_3s(x):
    x_str = str(x)
    new_x_str = ""
    skip_next = False
    
    for i in range(len(x_str) - 1):
        if skip_next:
            skip_next = False
            continue
        if x_str[i] == '3' and x_str[i + 1] == '3':
            skip_next = True 
        else:
            new_x_str += x_str[i]
    
    
    if not skip_next:
        new_x_str += x_str[-1]
    
    
    return int(new_x_str) if new_x_str else 0


t = int(input())  
results = []

for _ in range(t):
    x = int(input())
    
    while x > 0:
        
        new_x = remove_consecutive_3s(x)
        
        if new_x == x:  
            if x >= 33:
                x -= 33
            else:
                break  
        else:
            x = new_x
    
    if x == 0:
        results.append("YES")
    else:
        results.append("NO")


print("\n".join(results))
