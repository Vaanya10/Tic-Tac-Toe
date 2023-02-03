from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title('Tic Tac Toe')
Label(root, text="Player 1:X",font="times 15",fg='black',bg='yellow').grid(row=0, column=1) 
Label(root, text="Player 2:O",font="times 15",fg='black',bg='yellow').grid(row=0, column=2)

Button1 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(1))
Button1.grid(row=1, column=1)
Button2 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(2))
Button2.grid(row=1, column=2)
Button3 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(3))
Button3.grid(row=1, column=3)
Button4 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(4))
Button4.grid(row=2, column=1)
Button5 = Button(root, width=15, height=7, font=('times 16 bold'),  bg='beige', command=lambda:checker(5))
Button5.grid(row=2, column=2)
Button6 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(6))
Button6.grid(row=2, column=3)
Button7 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(7))
Button7.grid(row=3, column=1)
Button8 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(8))
Button8.grid(row=3, column=2)
Button9 = Button(root, width=15, height=7, font=('times 16 bold'), bg='beige', command=lambda:checker(9))
Button9.grid(row=3, column=3)

digits = [1,2,3,4,5,6,7,8,9]
mark = ''
count = 0
panels = ['panel']*10

def win(panels,sign):
    return ((panels[1]==panels[2]==panels[3]==sign)
            or(panels[1]==panels[4]==panels[7]==sign)
            or(panels[1]==panels[5]==panels[9]==sign)
            or(panels[2]==panels[5]==panels[8]==sign)
            or(panels[3]==panels[6]==panels[9]==sign)
            or(panels[3]==panels[5]==panels[7]==sign)
            or(panels[4]==panels[5]==panels[6]==sign)
            or(panels[7]==panels[8]==panels[9]==sign))

def checker(digit):
    global count,mark,digits
    if digit ==1:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button1.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')



    if digit ==2:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button2.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==3:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button3.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==4:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button4.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==5:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button5.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==6:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button6.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==7:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button7.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==8:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button8.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')

    if digit ==9:
        if digit in digits:
            digits.remove(digit)
            if count%2 == 0:
                mark='x'
                panels[digit] = mark
            if count%2 != 0:
                mark='o'
                panels[digit] = mark
            Button9.config(text=mark)
            count=count+1
            sign = mark
            if win(panels,sign) and sign =='x':
                msg.showinfo('Result','Player 1 wins')
                root.destroy()
            if win(panels,sign) and sign =='o':
                msg.showinfo('Result','Player 2 wins')
                root.destroy()
        else:
            msg.showinfo('Error','Value already exists')



root.mainloop()