from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

def main():
    "главная"
    if rnd(0, 20) == 1: new_ball()
    motion()
    if notf:
        root.after(50, main)

def new_ball():
    "ясно из названия:)"
    global allBset
    x = rnd(100, 700)
    y = rnd(100, 400)
    r = rnd(30, 50)
    col = choice(colors)
    rx = rnd(-7, 7)
    ry = rnd(-7, 7)
    allBset.append([x, y, r, col, rx, ry])
    currentBset.add(len(allBset) - 1)

def bomb(x, y, r):
    "бомба"
    canv.create_oval(x - r, y - r, x + r, y + r, fill='black', width=0)
    canv.create_line(x, y, x + r, y - r, x + 2 * r, y - r, x + r, y - r // 7, x + 2 * r, y, smooth=1, width=3)
    canv.create_polygon(x + 2 * r // 3, y - r, x + r, y - 2 * r // 3, x + 2 * r // 3, y - r // 3, x + r // 3,
                        y - 2 * r //3, x + 2 * r // 3, y - r, fill='black', width=0)

def click(event):
    "счётчик очков; обнуляется при попадании по бомбам"
    global score, text, text1, canvb
    destrBset = set()
    for n in currentBset:
        x = allBset[n][0]
        y = allBset[n][1]
        r = allBset[n][2]
        col = allBset[n][3]
        if (x - event.x)**2 + (y - event.y)**2 <= r**2:
            if col == 'black':
                score = 0
                text = canv.create_text(420, 20, text='Вы набрали целых ' + str(score)+' очков!', font='Helvetica 20 bold', fill='#681847')
                canvb = Canvas(root, bg='#F0F8FF', width=800, height=600)
                canvb.place(x=0, y=0)
                label2 = Label(canvb, bg='#F0F8FF', fg='#8B0000', font='Helvetica 30 bold', width=30)
                label2['text'] = 'Аккуратнее, молодой человек!'
                label2.place(x=60, y=280)
                root.after(5000, canvb.destroy)
            else:
                score += 1
                text = canv.create_text(420, 20, text='Вы набрали целых ' + str(score) + ' очков!',
                                        font='Helvetica 20 bold', fill='#681847')
            destrBset.add(n)
    currentBset.difference_update(destrBset)

def motion():
    "анимация шариков"
    global allBset, text
    canv.delete(ALL)
    text = canv.create_text(420, 20, text='Вы набрали целых ' + str(score) + ' очков!', font='Helvetica 20 bold',
                            fill='#8B0000')
    for n in currentBset:
        rx = allBset[n][4]
        ry = allBset[n][5]
        allBset[n][0] = allBset[n][0] + rx
        allBset[n][1] = allBset[n][1] + ry
        x = allBset[n][0]
        y = allBset[n][1]
        r = allBset[n][2]
        if y - r <= 40 or y + r >= 450:
            allBset[n][5] = -ry
        if x - r <= 10 or x + r >= 790:
            allBset[n][4] = -rx
        col = allBset[n][3]
        if col == 'black':
            bomb(x, y, r)
        else:
            canv.create_oval(x-r, y-r, x+r, y+r, fill=col, width=0)


canv = Canvas(root, bg='#FFE4C4')
canv.pack(fill=BOTH, expand=1)
q = Button(root, text='Утомились?')
q.place(x=400, y=560)


text = canv.create_text(420, 20, text=0, font='Helvetica 30 bold', fill='#8B0000')
text1 = canv.create_text(20, 220, font='Helvetica 45 bold', fill='#8B0000')
canv.bind('<Button-1>', click)
q.bind('<Button-1>',quit)

allBset = []
currentBset = set()

notf = True

colors = ['#7FFFD4', '#191970', '#0000CD', '#4B0082', 'black']
score = 0

main()

mainloop()