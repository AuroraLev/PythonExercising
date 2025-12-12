n = int(input())

for i in range(n):
    pr = i
    cur = i+1
    sum = cur + pr
    print(f"Current Number, {cur} Previous Number {pr}, Sum: {sum}")
    
#Solution:
#previous_num = 0
    
#    for i in range(1,11):
#       x_sum = previous_num + i
#       print(i, previous_num, x_sum)
#       previous_num = i