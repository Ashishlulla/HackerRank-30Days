# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
even = ""
odd = ""
for i in range(n):
    word = input()
    words.append(word)

for word in words:
    for i in range(len(word)):
        if (i+1) % 2 == 0 :
            even +=word[i]
        else:
            odd +=word[i]
    print(odd+" "+even)
    even = ""
    odd = ""
        

