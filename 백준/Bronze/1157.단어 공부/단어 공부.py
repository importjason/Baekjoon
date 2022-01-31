word = input().upper()
w = list(set(word))

lst = []
for i in w :
    n = word.count(i)
    lst.append(n) 

if lst.count(max(lst)) == 1 :    
    print(w[lst.index(max(lst))]) 
else :
    print('?')