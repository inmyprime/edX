s = 'zyxwvu'
max_sub_length = 0
i = 0
s_length = len(s)
longest_sub = s[0]
while i < s_length - max_sub_length:
    j = i
    while j < len(s)-1 and s[j] <= s[j+1]:
        j += 1
    cur_sub_length = j - i + 1
    if cur_sub_length > max_sub_length:
        max_sub_length = cur_sub_length
        longest_sub = s[i:j+1]
    i = j + 1
print('Longest substring in alphabetical order is:',longest_sub)
        

