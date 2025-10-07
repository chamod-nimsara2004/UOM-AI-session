sum_sq = 0
sum_num = 0

for i in range(1, 101):
    sum_sq += i * i
    sum_num += i

print(sum_num * sum_num - sum_sq)