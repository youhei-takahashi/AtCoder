s = input()
 
for i in range(len(s)):
    if s[i] == "A":
        s_index = i
        break
s = s[::-1]
for i in range(len(s)):
    if s[i] == "Z":
        end_index = i
        break
end_index = len(s) - end_index
print(end_index - s_index)