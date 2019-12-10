age=0
e=0
try:
    age=input("enter a age : ")
    if(age<18):
        raise Exception()
except Exception as e:
    print e, "not valid age"
else:
    print"your welcome"
