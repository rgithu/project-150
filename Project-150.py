from tkinter import *
import random
root=Tk()
root.title("Country Capitals")
root.geometry("500x500")
root.configure(background="red")
enter_name=Entry(root)
enter_name.place(relx=0.5,rely=0.1,anchor=CENTER)
enter_name2=Entry(root)
enter_name2.place(relx=0.5,rely=0.2,anchor=CENTER)
label_country_list=Label(root)
label_capital_list=Label(root)
label_random_country=Label(root)
label_lucky_capital=Label(root)

list1=[]
list2=[]

def addcountry():
    countryname=enter_name.get()
    list1.append(countryname)
    label_country_list["text"]="Country names  are : "+str(list1)

def addcapital():    
    capitalname=enter_name2.get()
    list2.append(capitalname)
    label_capital_list["text"]="Capital names  are : "+str(list2)
    
def ran_no():
    length1=len(list1)
    ran1=random.randint(0,lenght1-1)
    genrate_random=list1[ran1]
    label_random_country["text"]="Random country is :"+str(ran1)
    length2=len(list2)
    ran2=random.randint(0,lenght2-1)
    genrate_random2=list2[ran2]
    label_random_capital["text"]="Random capital is :"+str(ran2)
    
   
btn = Button(root,text="Add Country name",command=addcountry,bg="yellow")
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
btn2 = Button(root,text="Add Capital name",command=addcapital,bg="yellow")
btn2.place(relx=0.5,rely=0.4,anchor=CENTER)
label_country_list.place(relx=0.5,rely=0.5,anchor=CENTER)
label_capital_list.place(relx=0.5,rely=0.6,anchor=CENTER)
btn3 = Button(root,text="Random country and city is ",command=ran_no,bg="yellow")
btn3.place(relx=0.5,rely=0.7,anchor=CENTER)
label_random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
label_lucky_capital.place(relx=0.5,rely=0.9,anchor=CENTER)


root.mainloop()

