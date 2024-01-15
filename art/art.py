import tkinter as tk
import math
from PIL import Image,ImageTk,ImageDraw
from tkinter import filedialog

# a4 21,29.7
# a3 29.7,42

def grid():

	global image_,_image,size
	global wd,ht

	im=Image.open("data/image2.jpg")

	im.save("output/image2.jpg")
	x_,y_=im.size


	im1 = ImageDraw.Draw(im)   
	im1.line((int(x_/2),0, int(x_/2),int(y_)),fill="#ed2939", width = 0)
	im1.line((0,int(y_/2), int(x_),int(y_/2)),fill="#ed2939", width = 0) 

	cx=x_/2
	cy=y_/2


	if size=="a4":
		xx=x_/21
		yy=y_/29.7

	elif size=="a3":
		xx=x_/29.7
		yy=y_/42


	xx_=cx-xx
	while 1:
		im1.line((int(xx_),0,int(xx_),int(y_)),fill="#32fca7", width = 0)
		xx_-=xx
		if xx_<0:
			break


	xx_=cx+xx
	while 1:
		im1.line((int(xx_),0,int(xx_),int(y_)),fill="#32fca7", width = 0)
		xx_+=xx
		if xx_>x_:
			break




	yy_=cy-yy
	while 1:
		im1.line((0,int(yy_),int(x_),int(yy_)),fill="#32fca7", width = 0)
		yy_-=yy
		if yy_<0:
			break


	yy_=cy+yy
	while 1:
		im1.line((0,int(yy_),int(x_),int(yy_)),fill="#32fca7", width = 0)
		yy_+=yy
		if yy_>y_:
			break
	im.save("output/image1.jpg")


	canvas.delete(image_)

	im=Image.open("output/image1.jpg")
	im=im.resize((int(wd),int(ht)))

	im.save("data/grid_.jpg")


	_image=ImageTk.PhotoImage(file="data/grid_.jpg")
	image_=canvas.create_image(x,y,image=_image,anchor="nw")




def crop_image():
	global crop__
	global wd,ht
	global image_,_image

	x=(600-wd)/2
	y=40


	if crop__[0]<crop__[2]:
		x1=crop__[0]-x
		x2=crop__[2]-x
	elif crop__[2]<crop__[0]:
		x1=crop__[2]-x
		x2=crop__[0]-x

	if crop__[1]<crop__[-1]:
		y1=crop__[1]-y
		y2=crop__[-1]-y
	elif crop__[-1]<crop__[1]:
		y1=crop__[-1]-y
		y2=crop__[1]-y



	im=Image.open("data/image2.jpg")
	x_,y_=im.size


	x1=int(x1*x_/wd)
	x2=int(x2*x_/wd)

	y1=int(y1*y_/ht)
	y2=int(y2*y_/ht)



	im=im.crop((x1,y1,x2,y2))

	im.save("data/image3.jpg")






	im=Image.open("data/image3.jpg")

	x_,y_=im.size



	if y_/x_<1.414:
		xx=wd
		yy=xx*y_/x_
	elif y_/x_>1.414:
		yy=ht 
		xx=yy*x_/y_
	elif y_/x_==1.414:
		xx=wd
		yy=ht



	xx_=(wd-xx)/2
	yy_=(ht-yy)/2


	_cx=xx_*x_/xx
	_cy=yy_*y_/yy

	_cx=int(_cx)
	_cy=int(_cy)

	im2=im.crop((0-_cx,0-_cy,x_+_cx,y_+_cy))

	im2.save("data/image2.jpg")

	xx=int(xx)
	yy=int(yy)


	im=im.resize((xx,yy))


	xx_=(wd-xx)/2
	yy_=(ht-yy)/2


	

	

	im.save("data/image_.jpg")


	image=1
	canvas.delete(image_)


	im=Image.open("data/image2.jpg")
	im=im.resize((int(wd),int(ht)))

	im.save("data/image2_.jpg")


	_image=ImageTk.PhotoImage(file="data/image2_.jpg")
	image_=canvas.create_image(x,y,image=_image,anchor="nw")







def canvas_motion(e):
	global canvas,crop,crop__,_crop


	x=(600-wd)/2
	y=40

	if x<=e.x<=x+wd:
		if y<=e.y<=y+ht:
			if len(crop__)==2:

				canvas.delete(_crop)

				_crop=canvas.create_rectangle(crop__[0],crop__[1],e.x,e.y,outline="red")




def canvas_event_b1(e):

	global size
	global wd,ht
	global crop,crop1,crop2,crop3,crop__,_crop
	global image,image_,_image
	global _grid


	if 503.8755304101839<=e.x<=553.875530410184:
		if 535<=e.y<=560:
			if image==1:
				_grid=1
				grid()



	cx,cy=25,20

	r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2 )

	if r<=15:
		size="a4"
		draw_size()

		if _grid==1:
			grid()
		return


	cx,cy=65,20

	r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2 )

	if r<=15:
		size="a3"
		draw_size()

		if _grid==1:
			grid()

		return



	x=(600-wd)/2
	y=40
	
	if crop==1:
		if x<=e.x<=x+wd:
			if y<=e.y<=y+ht:
				crop__.append(e.x)
				crop__.append(e.y)

				if len(crop__)==4:
					crop=0

					canvas.delete(crop1)
					canvas.delete(crop2)
					canvas.delete(crop3)

					crop1=canvas.create_oval(x+wd+5,y+35, x+wd+5+30,y+30+35,fill="#000000",outline="#32fca7")
					crop2=canvas.create_line(x+wd+5+15-5,y+35+15-5-4, x+wd+5+15-5,y+35+15+5, x+wd+5+15+5+4,y+35+15+5, fill="#32fca7")
					crop3=canvas.create_line(x+wd+5+15-5-4,y+35+15-5, x+wd+5+15+5,y+35+15-5, x+wd+5+15+5,y+35+15+5+4, fill="#32fca7")

					canvas.delete(_crop)
					crop_image()

					crop__=[]

	cx,cy=x+wd+5+15,y+15

	r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2 )

	if r<=15:
		canvas.delete(image_)
		image=0
		_grid=0


		if crop==1:

			crop=0

			canvas.delete(crop1)
			canvas.delete(crop2)
			canvas.delete(crop3)

			crop1=canvas.create_oval(x+wd+5,y+35, x+wd+5+30,y+30+35,fill="#000000",outline="#32fca7")
			crop2=canvas.create_line(x+wd+5+15-5,y+35+15-5-4, x+wd+5+15-5,y+35+15+5, x+wd+5+15+5+4,y+35+15+5, fill="#32fca7")
			crop3=canvas.create_line(x+wd+5+15-5-4,y+35+15-5, x+wd+5+15+5,y+35+15-5, x+wd+5+15+5,y+35+15+5+4, fill="#32fca7")

		return



	cx,cy=x+wd+5+15,y+35+15

	r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2 )

	if r<=15:

		if image==1:
			if crop==0:
				crop=1
			elif crop==1:
				crop=0
			
			canvas.delete(crop1)
			canvas.delete(crop2)
			canvas.delete(crop3)


			if crop==0:
				canvas.delete(_crop)
				crop__=[]

				crop1=canvas.create_oval(x+wd+5,y+35, x+wd+5+30,y+30+35,fill="#000000",outline="#32fca7")
				crop2=canvas.create_line(x+wd+5+15-5,y+35+15-5-4, x+wd+5+15-5,y+35+15+5, x+wd+5+15+5+4,y+35+15+5, fill="#32fca7")
				crop3=canvas.create_line(x+wd+5+15-5-4,y+35+15-5, x+wd+5+15+5,y+35+15-5, x+wd+5+15+5,y+35+15+5+4, fill="#32fca7")
			elif crop==1:
				crop1=canvas.create_oval(x+wd+5,y+35, x+wd+5+30,y+30+35,fill="#32fca7",outline="#32fca7")
				crop2=canvas.create_line(x+wd+5+15-5,y+35+15-5-4, x+wd+5+15-5,y+35+15+5, x+wd+5+15+5+4,y+35+15+5, fill="#000000")
				crop3=canvas.create_line(x+wd+5+15-5-4,y+35+15-5, x+wd+5+15+5,y+35+15-5, x+wd+5+15+5,y+35+15+5+4, fill="#000000")
			return


	cx,cy=300,300

	r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2 )

	if r<=40:

		if image==0:

			im=filedialog.askopenfilename()

			try:
				im=Image.open(im)
				im = im.convert("RGB")
				im.save("data/image.jpg")

				im=Image.open("data/image.jpg")

				x_,y_=im.size



				if y_/x_<1.414:
					xx=wd
					yy=xx*y_/x_
				elif y_/x_>1.414:
					yy=ht 
					xx=yy*x_/y_
				elif y_/x_==1.414:
					xx=wd
					yy=ht



				xx_=(wd-xx)/2
				yy_=(ht-yy)/2


				_cx=xx_*x_/xx
				_cy=yy_*y_/yy

				_cx=int(_cx)
				_cy=int(_cy)

				im2=im.crop((0-_cx,0-_cy,x_+_cx,y_+_cy))

				im2.save("data/image2.jpg")

				xx=int(xx)
				yy=int(yy)


				im=im.resize((xx,yy))


				xx_=(wd-xx)/2
				yy_=(ht-yy)/2


				

				

				im.save("data/image_.jpg")


				image=1
				canvas.delete(image_)


				im=Image.open("data/image2.jpg")
				im=im.resize((int(wd),int(ht)))

				im.save("data/image2_.jpg")


				_image=ImageTk.PhotoImage(file="data/image2_.jpg")
				image_=canvas.create_image(x,y,image=_image,anchor="nw")



			
			except:
				pass





def draw_size():
	global canvas
	global size
	global a4_1,a4_2,a3_1,a3_2,quit

	quit=ImageTk.PhotoImage(file="icons/quitb.png")
	
	canvas.delete(a4_1)
	canvas.delete(a4_2)
	canvas.delete(a3_1)
	canvas.delete(a3_2)

	if size=="a4":

		a4_1=canvas.create_oval(10,5,40,35,fill="#32fca7",outline="#32fca7")
		a3_1=canvas.create_oval(10+40,5,40+40,35,fill="#000000",outline="#32fca7")

		a4_2=canvas.create_text(25,20,text="a4",font=("FreeMono",13),fill="#000000")
		a3_2=canvas.create_text(25+40,20,text="a3",font=("FreeMono",13),fill="#32fca7")

	elif size=="a3":

		a4_1=canvas.create_oval(10,5,40,35,fill="#000000",outline="#32fca7")
		a3_1=canvas.create_oval(10+40,5,40+40,35,fill="#32fca7",outline="#32fca7")

		a4_2=canvas.create_text(25,20,text="a4",font=("FreeMono",13),fill="#32fca7")
		a3_2=canvas.create_text(25+40,20,text="a3",font=("FreeMono",13),fill="#000000")



size="a4"

a4_1=()
a4_2=()

a3_1=()
a3_2=()

image=0
crop=0
crop__=[]
_crop=()

image_=()
_image=()

_grid=0

root=tk.Tk()
root.geometry("600x600+0+0")
root.title("grid")


canvas=tk.Canvas(width=600,height=600,bg="#000000",relief="flat",highlightthickness=0,border=0)
canvas.place(in_=root,x=0,y=0)

canvas.bind("<Button-1>",canvas_event_b1)
canvas.bind("<Motion>",canvas_motion)



wd=520/1.414
ht=520

x=(600-wd)/2
y=40
canvas.create_rectangle(x-1,y-1,x+wd,y+ht,fill="#000000",outline="#999999")
canvas.create_oval(300-40,300-40, 300+40,300+40,fill="#000000",outline="#999999")
canvas.create_line(300,300-20,300,300+20,fill="#999999")
canvas.create_line(300-20,300,300+20,300,fill="#999999")



canvas.create_oval(x+wd+5,y, x+wd+5+30,y+30,fill="#fe3939")
canvas.create_line(x+wd+5+15-6,y+15-6, x+wd+5+15+6,y+15+6,fill="#ffffff",width=2)
canvas.create_line(x+wd+5+15-6,y+15+6, x+wd+5+15+6,y+15-6,fill="#ffffff",width=2)

crop1=canvas.create_oval(x+wd+5,y+35, x+wd+5+30,y+30+35,fill="#000000",outline="#32fca7")
crop2=canvas.create_line(x+wd+5+15-5,y+35+15-5-4, x+wd+5+15-5,y+35+15+5, x+wd+5+15+5+4,y+35+15+5, fill="#32fca7")
crop3=canvas.create_line(x+wd+5+15-5-4,y+35+15-5, x+wd+5+15+5,y+35+15-5, x+wd+5+15+5,y+35+15+5+4, fill="#32fca7")



#canvas.create_rectangle(x+wd+20,600-70+5, x+wd+20+50,600-70+30,outline="#32fca7")

canvas.create_arc(x+wd+20,600-70+5, x+wd+20+25,600-70+30,start=90,extent=180,outline="#32fca7",style="arc")
canvas.create_arc(x+wd+20+25,600-70+5, x+wd+20+25+25,600-70+30,start=270,extent=180,outline="#32fca7",style="arc")
canvas.create_line(x+wd+20+12.5,600-70+5,x+wd+20+25+25-12.5+1,600-70+5,fill="#32fca7")
canvas.create_line(x+wd+20+12.5,600-70+30,x+wd+20+25+25-12.5+1,600-70+30,fill="#32fca7")

canvas.create_text(x+wd+20+25,600-70+5+12.5,text="grid",fill="#32fca7",font=("FreeMono",13))


draw_size()
root.mainloop()