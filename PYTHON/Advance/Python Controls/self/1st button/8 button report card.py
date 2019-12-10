from Tkinter import*

def marksheet():
    print"clicked"
    a=float(T4.get("1.0",END))
    b=float(T5.get("1.0",END))
    c=float(T6.get("1.0",END))
    T7.insert(END,str(a+b+c))
    if(a>=40 and b>=40 and c>=40):
        # print"pass",a,b,c
        T8.insert(END,"PASS")
    else:
        # print"fail",a,b,c
        T8.insert(END,"FAIL")
    Avg=(a+b+c)/3
    if(Avg>85 and Avg<=100):
        # print"A ",AVG
        T9.insert(END,"A")
    elif(Avg>70 and Avg<=85):
       # print"B",Avg
        T9.insert(END,"B")
    elif(Avg>55 and Avg<=70):
        # print"C",Avg
        T9.insert(END,"C")
    elif(Avg>40 and Avg<=55):
        #print"D",Avg
        T9.insert(END,"D")
    else:
        #print"F",Avg
        T9.insert(END,"F")
    
    
    
    

L1=Label(text="STUDENT NAME")
L1.pack()
T1=Text(height=3,width=30)
T1.pack()

L2=Label(text="ROLL NO.")
L2.pack()
T2=Text(height=3,width=30)
T2.pack()

L3=Label(text="SUBJECT & MARKS")
L3.pack()

L4=Label(text="PHYSICS")
L4.pack()
T4=Text(height=3,width=30)
T4.pack()

L5=Label(text="CHEMISTRY")
L5.pack()
T5=Text(height=3,width=30)
T5.pack()

L6=Label(text="MATHMATICS")
L6.pack()
T6=Text(height=3,width=30)
T6.pack()

b=Button(text="CLICK HERE",command=marksheet)
b.pack()

L7=Label(text="TOTAL")
L7.pack()
T7=Text(height=3,width=30)
T7.pack()

L8=Label(text="RESULT")
L8.pack()
T8=Text(height=3,width=30)
T8.pack()

L9=Label(text="GRADE")
L9.pack()
T9=Text(height=3,width=30)
T9.pack()

mainloop()
