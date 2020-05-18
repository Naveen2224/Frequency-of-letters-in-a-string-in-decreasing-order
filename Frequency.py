def most_frequent(string):
    f={}
    for i in string:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    l = f.items()
    t = dict(sorted(l, key = lambda kv:(kv[1]),reverse = True))
    for j in t:
        print(j+" = 0"+str(f[j]))
string=input("enter a string: ")
most_frequent(string)
