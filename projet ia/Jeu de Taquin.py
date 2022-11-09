from tkinter import * 
from Solver import Solver
from Solver import Taquin
global puzzl , t ,j

j=0
fenetre = Tk()

board = [[1,2,3],[4,5,6],[7,8,0]]
photos=[]
for i in range(0,9):
	photos.append(PhotoImage(file="./images/"+str(i)+".png"))

global Lph , LAff
Lph = photos[0:9]

can=Canvas( width=540,height=540,bg='white')
can.pack( side =TOP, padx =20, pady =20)
fenetre['bg']='white'
fenetre.title (' Jeu de Taquin')

puzzl = Taquin(board,can,Lph)
s = Solver(puzzl,fenetre)


def solv():
	global s
	s =Solver(puzzl,fenetre)
	s.largeur()

def solv_prof():
	global s
	s =Solver(puzzl,fenetre)
	s.profondeur()

def solv_prof_lim():
	global s
	s =Solver(puzzl,fenetre)
	s.solve_prof_limite()

def mel():
	global puzzl
	puzzl = puzzl.shuffle()

def melanger():
	print(puzzl.board)

LAff = list([0,1,2,3,4,5,6,7,8])
LAff=[]
for row in board:
    LAff.extend(row)

Button(text='Set',command=mel).pack(side=LEFT)
Button(text='Recherche en largeur',command=solv).pack(side=LEFT)
Button(text='Recherche en profondeur',command=solv_prof).pack(side=LEFT)
Button(text='Recherche en profondeur limité (L=3)',command=solv_prof_lim).pack(side=LEFT)
Button(text='A *',command=solv).pack(side=LEFT)
Button(text='Quitter',command=fenetre.quit).pack(side=LEFT)
for k in range(0,8) :
    eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
    aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[LAff[k]])

can.pack()

fenetre.mainloop()
