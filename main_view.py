__author__ = 'Lesmed'


import view as v
from Tkinter import*

v0=Tk(className="Lesmed")
v1=Toplevel(v0)
lista=[]
mivalor1=StringVar()
mivalor2=StringVar()
mivalor3=StringVar()
mivalor4=StringVar()
mivalor5=StringVar()
mivalor6=StringVar()
label1=Label(v1,text="digite la fila").pack()
entry1=Entry(v1,textvar=mivalor1).pack()
label2=Label(v1,text="digite la columna").pack()
entry2=Entry(v1,textvar=mivalor2).pack()
label3=Label(v1,text="orientacion").pack()
entry3=Entry(v1,textvar=mivalor3).pack()
label4=Label(v1,text="Pista").pack()
entry4=Entry(v1,textvar=mivalor4).pack()
label5=Label(v1,text="palabra").pack()
entry5=Entry(v1,textvar=mivalor5).pack()
label6=Label(v1,text="Para salir digite si").pack()
entry6=Entry(v1,textvar=mivalor6).pack()
def listas_del_crucigrama(): #esta funcion crea las sublistas de la lista que contienen los datos
    nlista=[]
    cont=0
    while True:
        pri=mivalor1.get()
        nlista.append(pri)
        seg=mivalor2.get()
        nlista.append(seg)
        cuar=mivalor3.get()
        nlista.append(cuar)
        qint=mivalor4.get()
        nlista.append(qint)
        sex=mivalor5.get()
        nlista.append(sex)
        ter=len(sex)
        nlista.insert(2,ter)
        lista.append(nlista)
        cont=cont+1
        fin=raw_input("salir")
        if fin!="salir":
            pass
        if fin=="salir":
            break
        nlista=[]
    print lista, cont

matriz=[0,0,0,0,0]
def crear_matriz():
    for x in range(len(lista[0][5])):
            obj=Entry(v0, width=2, bg="green")
            lista[0][5]=obj
            lista[0][5].grid(column=x,row=1)

palabra=0
def unir():
    ind=0
    while ind<len(lista):
        a=lista[0][5].get()
        lista.append(a)
        ind+=1
        palabra="".join(lista)
    print lista, palabra
    if palabra==listag[0]:
        for x in range(len(matriz)):
            lista[0][5].configure(state="disabled")
            del lista[:len(lista[0][5])]
    else:
        print False
        del lista[:len(lista[0][5])]


b1=Button(v1,text="unir",command=lambda:listas_del_crucigrama()).pack()
b2=Button(v0,text="Crear",command=lambda:crear_matriz()).pack()
b3=Button(v0,text="Verificar",command=lambda:unir()).pack()
v0.geometry("200x300")
v0.mainloop()
v0.mainloop()