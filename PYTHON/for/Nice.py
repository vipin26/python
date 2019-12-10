S=raw_input("Enter a string: ")
for i in range(0,len(S),1):
    for j in range(0,i,1):
        print S[j],
    print
for i in range(len(S),0,-1):
    for j in range(0,i,1):
        print S[j],
    print
