
import tkinter as tk
import math
root = tk.Tk()
root.geometry("600x1000")


def izracun(self):
    rezultat.delete(0,"end") #brise polje rezultata

#sprema unos u polja

    d_cil_odg = float(d_cil.get())

    h_cil_odg = float(h_cil.get())
 
    h_brtva_odg = float(h_brtva.get())

    d_brtva_odg = float(d_brtva.get())

    h_klip_odg = float(h_klip.get())

    gustoca_odg = float(gustoca.get())
 
    v_glava_odg = float(v_glava.get())

    v_blok_odg = float(v_blok.get())
   

    v_ulje_glava = v_glava_odg / gustoca_odg  #volumen u glavi u mL
 
    v_ulje_cil = v_blok_odg / gustoca_odg  #volumen u cil sa spust klipom

    v_ideal_valjak = d_cil_odg **2 * math.pi/4 *h_klip_odg /1000

    izvirivanje_klipa_iznad_baze_bloka =  v_ideal_valjak - v_ulje_cil

    v_u_blok = d_cil_odg**2 *math.pi/4 * h_cil_odg /1000

    v_u_brtvi = d_brtva_odg **2 *math.pi/4 * h_brtva_odg /1000

    v_u_glavi = v_ulje_glava - izvirivanje_klipa_iznad_baze_bloka

    v_gmt = v_u_glavi + v_u_brtvi

    v_dmt = v_u_brtvi + v_u_blok + v_u_glavi

    comp = v_dmt / v_gmt

    rezultat.insert(tk.END, str(comp))


d_cil = tk.Entry()
d_cil.place(x=400, y=80)
lb1 = tk.Label(root, text="Promjer cilindra: ")
lb1.place(x= 20, y= 80)

h_cil = tk.Entry()
h_cil.place(x=400, y=80*2)
lb2 = tk.Label(root, text="Hod klipa:  ")
lb2.place(x= 20, y= 80*2)

h_brtva = tk.Entry()
h_brtva.place(x=400, y=80*3)
lb3 = tk.Label(root, text="Visina brtve:  ")
lb3.place(x= 20, y= 80*3)

d_brtva = tk.Entry()
d_brtva.place(x=400, y=80*4)
lb4 = tk.Label(root, text="Promjer brtve: ")
lb4.place(x= 20, y= 80*4)

h_klip = tk.Entry()
h_klip.place(x=400, y=80*5)
lb5 = tk.Label(root, text="Klip spusten od GMT: ")
lb5.place(x= 20, y= 80*5)

gustoca = tk.Entry()
gustoca.place(x=400, y=80*6)
lb6 = tk.Label(root, text="Gustoća tekućine s kojom se mjeri: ")
lb6.place(x= 20, y= 80*6)

v_glava = tk.Entry()
v_glava.place(x=400, y=80*7)
lb8 = tk.Label(root, text="Masa ulja utisnut u komoru glave motora: ")
lb8.place(x= 20, y= 80*7)

v_blok = tk.Entry()
v_blok.place(x=400, y=80*8)
lb9 = tk.Label(root, text="Masa ulja utisnut u cilindar: ")
lb9.place(x= 20, y= 80*8)

rezultat = tk.Entry()
lb7 = tk.Label(root, text="Rezultirajuci kompresioni omjer =                   1 :  ")

lb7.place(x=20, y = 80*9) 

rezultat.place(x=300, y=80*9)


izr = tk.Button(root, text="Izracunaj!")
izr.bind("<Button-1>",izracun)
izr.place(x=400, y=80*10)


tk.mainloop()