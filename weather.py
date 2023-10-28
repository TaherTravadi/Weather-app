from tkinter import *
from tkinter import ttk
import  requests


def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1172ed9e1db265ac388f7ad24aac6670").json()
    l1_one.config(text=data["weather"][0]["main"])
    l2_two.config(text=data["weather"][0]["description"])
    l3_three.config(text=str(int(data["main"]["temp"]-273.15)))
    l4_four.config(text=data["main"]["pressure"])



win=Tk()

win.title("Weather")
win.config(bg="blue")
win.geometry("600x600")
label1=Label(win,text="Excel Weather App",font=("Time New Roman",30,"bold"))
label1.place(x=25,y=50,height=50,width=450)
city_name=StringVar()
list=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

combo=ttk.Combobox(win,values=list,font=("Time New Roman",10,"bold"),textvariable=city_name)
combo.place(x=25,y=120,height=50,width=450)
l1=Label(win,text="Weather Climate",font=("Time New Roman",20))
l1.place(x=25,y=260,height=50,width=210)
l1_one=Label(win,text="",font=("Time New Roman",20))
l1_one.place(x=250,y=260,height=50,width=210)
l2=Label(win,text="Weather Description",font=("Time New Roman",17))
l2.place(x=25,y=330,height=50,width=210)
l2_two=Label(win,text="",font=("Time New Roman",17))
l2_two.place(x=250,y=330,height=50,width=210)
l3=Label(win,text="Temperature",font=("Time New Roman",20))
l3.place(x=25,y=400,height=50,width=210)
l3_three=Label(win,text="",font=("Time New Roman",20))
l3_three.place(x=250,y=400,height=50,width=210)
l4=Label(win,text="Pressure",font=("Time New Roman",20))
l4.place(x=25,y=470,height=50,width=210)
l4_four=Label(win,text="",font=("Time New Roman",20))
l4_four.place(x=250,y=470,height=50,width=210)
b1=Button(win,text="Submit",font=("Time New Roman",20,"bold"),command=data_get)
b1.place(y=190,height=50,width=100,x=200)

win.mainloop()



