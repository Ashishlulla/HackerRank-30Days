# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phonebook = {}
for i in range(n):
    key, value = input().split(" ")
    phonebook[key] = int(value)
    
while True:
    try:
        query = input()
        if query in phonebook.keys():
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except:
        break
