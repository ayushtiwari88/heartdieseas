from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#image work
img=Image.open('dill.jpg')
window=Tk()
render =ImageTk.PhotoImage(img)
i1=Label(window,image=render,width=1100,height=900)
i1.image=render
i1.place(x=400,y=5)


#ml
df = pd.read_csv('ge.csv')
def predict_train(args):
    dataframe = pd.DataFrame(args)
    try:
        x = df.iloc[:,:-1]
        y = df['target']
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=10)
        classifier = LogisticRegression(random_state=0)
        classifier.fit(x_train,y_train)
        y_pred = classifier.predict(dataframe)
        return y_pred
    except ValueError as er :
        print(f"wrong input by user{er}")

#heading
l0=Label(window,text='Heart disease prediction system',font=('Traditional serif',10,'bold'))
l0.grid(row=0,column=0,padx=10,pady=10)
#age box and entry
l1=Label(window,text='Age',font=('Traditional serif',10,'bold'))
l1.grid(row=1,column=0,padx=10,pady=10)

e1_value = StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1,padx=10,pady=10)

#sex box 
l2=Label(window,text='sex',font=('Traditional serif',10,'bold'))
l2.grid(row=2,column=0,padx=10,pady=10)

v1=StringVar()
choice1={"Male","Female"}
mf=OptionMenu(window,v1,*choice1)
v1.set("Male")
mf.grid(row=2,column=1,padx=10,pady=10)

#chest pain box 
l3=Label(window,text='Chest_Pain_Type',font=('Traditional serif',10,'bold'))
l3.grid(row=3,column=0,padx=10,pady=10)

v2=StringVar()
choice2={"Typical Angima","Asymptomatic","Atypical Angima","Non-Anginal Pain"}
cpt=OptionMenu(window,v2,*choice2)
v2.set("Asymptomatic")
cpt.grid(row=3,column=1,padx=10,pady=10)

#blood pressure box 
l4=Label(window,text='Resting_Blood_Pressure',font=('Traditional serif',10,'bold'))
l4.grid(row=4,column=0,padx=10,pady=10)

e2_value = StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=4,column=1,padx=10,pady=10)

#cholestrol box 
l5=Label(window,text='Cholestrol',font=('Traditional serif',10,'bold'))
l5.grid(row=5,column=0,padx=10,pady=10)

e3_value = StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=5,column=1,padx=10,pady=10)

#blood sugar box 
l6=Label(window,text='Fasting_Blood_Sugar',font=('Traditional serif',10,'bold'))
l6.grid(row=6,column=0,padx=10,pady=10)

v3=StringVar()
choice3={"Lower than 120mg/ml","Greater than 120mg/ml"}
fbs=OptionMenu(window,v3,*choice3)
v3.set("Lower than 120mg/ml")
fbs.grid(row=6,column=1,padx=10,pady=10)

#ecg box 
l7=Label(window,text='Rest_Ecg',font=('Traditional serif',10,'bold'))
l7.grid(row=7,column=0,padx=10,pady=10)

v4=StringVar()
choice4={"ST-T Wave Abnormality","Normal","Left Ventricular Hypertrophy"}
ecg=OptionMenu(window,v4,*choice4)
v4.set("ST-T Wave Abnormality")
ecg.grid(row=7,column=1,padx=10,pady=10)

#heart rate box 
l8=Label(window,text='Max_Heart_Rate_Achieved',font=('Traditional serif',10,'bold'))
l8.grid(row=8,column=0,padx=10,pady=10)

e4_value = StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=8,column=1,padx=10,pady=10)

#exercise indused engina box 
l9=Label(window,text='Exercise_Indused_Angina',font=('Traditional serif',10,'bold'))
l9.grid(row=9,column=0,padx=10,pady=10)

v5=StringVar()
choice5={"Yes","No"}
eia=OptionMenu(window,v5,*choice5)
v5.set("Yes")
eia.grid(row=9,column=1,padx=10,pady=10)

#st depression box 
l10=Label(window,text='St_Depression',font=('Traditional serif',10,'bold'))
l10.grid(row=10,column=0,padx=10,pady=10)

e5_value = StringVar()
e5=Entry(window,textvariable=e5_value)
e5.grid(row=10,column=1,padx=10,pady=10)

#st slope 
l11=Label(window,text='St_Slope',font=('Traditional serif',10,'bold'))
l11.grid(row=11,column=0,padx=10,pady=10)

v6=StringVar()
choice6={"Downsloping","Flat","Upslopping"}
ss=OptionMenu(window,v6,*choice6)
v6.set("Downsloping")
ss.grid(row=11,column=1,padx=10,pady=10)

#vessels box 
l12=Label(window,text='Num_mMjor_Vessels',font=('Traditional serif',10,'bold'))
l12.grid(row=12,column=0,padx=10,pady=10)

e6_value = StringVar()
e6=Entry(window,textvariable=e6_value)
e6.grid(row=12,column=1,padx=10,pady=10)

#thalassemia box 
l13=Label(window,text='Thalassemia',font=('Traditional serif',10,'bold'))
l13.grid(row=13,column=0,padx=10,pady=10)

v7=StringVar()
choice7={"Reversable defect","Normal","Fixed defect"}
t=OptionMenu(window,v7,*choice7)
v7.set("Fixed defect")
t.grid(row=13,column=1,padx=10,pady=10)


def dictionary():
    a=e1.get(),v1.get(),v2.get(),e2.get(),e3.get(),v3.get(),v4.get(),e4.get(),v5.get(),e5.get(),v6.get(),e6.get(),v7.get()
    l=[]
    for i in a:
        l.append(i)
    print(l)
    
    if l[1].lower()=='female':
        l[1]=0
    else:
        l[1]=1
    
    cp=0
    #Typical Angima","Asymptomatic","Atypical Angima","Non-Anginal Pain
    if l[2]=='Atypical Angima':
        cp=1
    elif l[2]=='Non-Anginal Pain':
        cp=2
    elif l[2]=='Typical Angima':
        cp=0
    else:
        cp=3
    
    #Lower than 120mg/ml","Greater than 120mg/ml
    bs=0
    if l[5]=='Lower than 120mg/ml':
        bs=0
    else:
        bs=1
    
    #ST-T Wave Abnormality","Normal","Left Ventricular Hypertrophy
    re=0
    if l[6]=='ST-T Wave Abnormality':
        re=1
    elif l[6]=='Normal':
        re=0
    else:
        re=2
    
    if l[8].lower()=='no':
        l[8]=0
    else:
        l[8]=1
    
    s=0
    #"Downsloping","Flat","Upslopping"
    if l[10]=='Upslopping':
        s=0
    elif l[10]=='Flat':
        s=1
    else:
        s=2
    
    T=0
    "Reversable defect","Normal","Fixed defect"
    if l[12]=='Normal':
        T=1
    elif l[12]=='Fixed defect':
        T=2
    else:
        T=3
    
    data={df.columns[0]:[l[0]],df.columns[1]:[l[1]],df.columns[2]:[cp],df.columns[3]:[l[3]],df.columns[4]:[l[4]],df.columns[5]:[bs],df.columns[6]:[re],df.columns[7]:l[7],df.columns[8]:[l[8]],df.columns[9]:l[9],df.columns[10]:[s],df.columns[11]:l[11],df.columns[12]:[T]}
    print(data)
 
    D = predict_train(data)
    print(D)

    if D == 0:
        show_message(0)
    else:
        show_message(1)
    
#button box     
b=Button(window,text="Predict",font=('Traditional serif',15,'bold'),fg='white',command=dictionary,bg='red')
b.grid(row=14,column=1,padx=10,pady=10)

#message box
def  show_message(i):
    if i == 0:
        messagebox.showinfo("greetings", "You don't have any heart desease")
    else:
        messagebox.showinfo("greetings", "you have heart desease")


window.geometry('1900x1080')
window.mainloop()