arr=[10,20,20,10,20,30,40]
set_arr = set(arr)
socks= [int((arr.count(a))/2) for a in set_arr]
print(sum(socks))
