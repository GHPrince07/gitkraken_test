n, b = input().split()
b = int(b)
n = list(n)
alphabet_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num_list = range(10, 36)

alphabet_dic = {}
for alphabet, num in zip(alphabet_list, num_list):
    alphabet_dic[alphabet] = num

sum = 0
for id, n_alphabet in enumerate(n):
    if n_alphabet in alphabet_list:
        sum += alphabet_dic[n_alphabet]*b**(len(n)-1-id)
    else:
        sum += int(n_alphabet)*b**(len(n)-1-id)
print(sum)