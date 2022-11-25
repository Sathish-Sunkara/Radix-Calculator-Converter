from tkinter import *

root=Tk()

root.title("RADIX CONVERTER")
root.geometry("1000x1000")





def others_to_dec(string,sys1):
    dec=0
    le=len(string)-1
    for l in string:
        if l>='0' and l<='9':
            val=int(l)
        elif ((l>='a') and (l<='z')):
            val=int(ord(l))-87
        elif ((l>='A') and (l<='Z')):
            val=int(ord(l))-55
        else:
            pass
        dec=dec+val*pow(sys1,le)
        le=le-1
    return dec
   


def dec_to_others(decimal,sys2):
    li=[]
    dec=int(decimal)
    while(dec>0):
        rem=dec%sys2
        if rem>=0 and rem<=9:
            li.append(str(rem))
        elif rem>=10 and rem<=35:
            li.append(str(chr(rem+55)))
        else:
            pass
        dec=dec//sys2
    st="".join(li)
    st=st[::-1]
    return st



def function():
    dis.delete(0,END)
    if((int(sys1.get())<=1) or (int(sys1.get())>36) or (int(sys2.get())<=1) or (int(sys2.get())>36)):
        s="this converter is only used for 2 to 36 radix only"
        dis.insert(0,s)
    elif(string.get()==''):
         s="please enter some number to convert"
         dis.insert(0,s)
    elif(string.get()!=''):
        string1=string.get()
        flag=0
        if((int(sys1.get())>=2) and (int(sys1.get())<=10)):
            for i in range(len(string1)):
                if(not((string1[i]>='0') and (string1[i]<='9'))):
                    s="Alphabets Are Not present In The Number System "+sys1.get()+" !!!"
                    flag=1
                    dis.insert(0,s)
                    break
        else:
            for i in range(len(string1)):
                if((not((string1[i]>='0') and (string1[i]<='9'))) and (not((string1[i]>='a') and (string1[i]<='z'))) and (not((string1[i]>='A') and (string1[i]<='Z')))):
                    s="enter a valid number without symbols"
                    flag=1
                    dis.insert(0,s)
                    break
    else:
        pass
    if flag==0:
        result=others_to_dec(string.get(),int(sys1.get()))
        result=dec_to_others(result,int(sys2.get()))
        dis.insert(0,str(result))
    else:
        pass









label1=Label(root,text="--------------MENU-------------",padx=30,pady=30,font=('Arial',35),fg="red")
label1.pack()

label2=Label(root,text="enter the number for conversion:",padx=10,pady=3,font=('Arial',22),fg="blue")
label2.pack()

string=Entry(root,width=40,font=('Arial',25))
string.pack(pady=5)

label3=Label(root,text="enter the system:",padx=10,pady=3,font=('Arial',22),fg="green")
label3.pack()

sys1=Entry(root,width=10,font=('Arial',25))
sys1.pack(pady=5)

label4=Label(root,text="which system u want to convert:",padx=10,pady=3,font=('Arial',22),fg="green")
label4.pack()

sys2=Entry(root,width=10,font=('Arial',25))
sys2.pack(pady=5)

btn=Button(root,text="submit" ,command=function,padx=3,pady=3,font=('Arial',18),fg="#f4a444")
btn.pack(padx=5,pady=8)

#answer

label_x=Label(root,text="ANSWER:",padx=10,font=('Arial',25),fg="brown")
label_x.pack()

dis=Entry(root,width=40,font=('Arial',25))
dis.pack()







root.mainloop()



