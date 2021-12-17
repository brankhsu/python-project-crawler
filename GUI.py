import tkinter
from tkinter import *
import pandastable
import pandas
import shopee_data as sd
import matplotlib.pyplot as plt
import numpy as np

from graphic_data import draw_scatter_figure, show_GUI_table


def inputbox():
    def button_event():
        root.destroy()

    root = tkinter.Tk()
    root.title('今天什麼最銷售')
    root.geometry('400x100')
    title = tkinter.Label(root, text='輸入想查詢的商品', bg='yellow', fg='#263238', font=('Arial', 12))
    title.grid(row=0, column=0)
    var = tkinter.StringVar()
    myentry = tkinter.Entry(root, width=20, textvariable=var)
    myentry.grid(row=0, column=1)
    mybutton = tkinter.Button(root, text='Search', command=button_event)
    mybutton.grid(row=1, column=1)
    root.mainloop()
    return var.get()


def mainframe(df):
    def exit_frame():
        t.destroy()

    def action1():
        show_graph()  # 畫圓餅圖

    def action2():
        GUI_2(df) #列出4大種類

    def action3():
        GUI_3(df) #同類商品價格

    t = tkinter.Tk()
    t.title('蝦皮產品分析')
    start_frame = Frame(width=1000, height=500)
    button_frame = Frame(width=1000, height=100, pady=10)
    start_frame.grid(row=0, column=0, padx=1, pady=3)
    button_frame.grid(row=2, column=0)

    fontStyle = tkinter.font.Font(family="Lucida Grande", size=30)
    button_fontStyle = tkinter.font.Font(family="Lucida Grande", size=10)
    button_width = 34
    button_height = 4
    button1 = Button(button_frame, text='目前最熱門', width=button_width, height=button_height, command=action1,font=button_fontStyle,
                     fg='SlateGray')
    button1.grid(row=2, column=0)
    button2 = Button(button_frame, text='同類商品價格查詢', width=button_width, height=button_height, command=action2, font=button_fontStyle,
                     fg='SlateGray')
    button2.grid(row=2, column=1)
    button3 = Button(button_frame, text='', width=button_width, height=button_height,  command=action3,font=button_fontStyle,
                     fg='SlateGray')
    button3.grid(row=2, column=2)
    exit = Button(button_frame, text='退出', width=button_width, height=button_height, command=exit_frame,
                  font=button_fontStyle, fg='SlateGray')
    exit.grid(row=2, column=3)
    label = Label(start_frame, text="本程式想要利用競品情報來提高自己銷售業績:\n 1.找出目前最熱門商品的特性\n 2.上架商品價格分析\n 3.商品訂價策略", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    #label.pack(side=LEFT)
    label.grid(row=0, column=0)
    exit.grid(row=2, column=3)
    start_frame.grid_propagate(0)
    button_frame.grid_propagate(0)
    t.mainloop()
    return


def show_graph():
    plt.style.use('ggplot')
    plt.rcParams['font.family'] = 'DFKai-SB'
    df = sd.count()
    print(df)
    df['出現次數'].plot(kind='pie', title='圓餅圖', figsize=(4, 4))
    plt.show()
    return


def GUI_2(df):
    root = Tk()
    root.title('蝦皮產品分析')
    median = draw_scatter_figure(df)
    median_sold = median[0]
    median_price = median[1]

    df1 = df[(df['已售出數量'] > median_sold) & (df['價格'] < median_price)]  # 低價高需求
    df2 = df[(df['已售出數量'] < median_sold) & (df['價格'] < median_price)]  # 低價低需求
    df3 = df[(df['已售出數量'] < median_sold) & (df['價格'] > median_price)]  # 高價低需求

    fontStyle = tkinter.font.Font(family="Lucida Grande", size=10)
    frame1 = Frame(master = root ,width=1000, height=350)
    frame2 = Frame(width=1000, height=350)
    frame3 = Frame(width=1000, height=350)
    frame1.grid(row=0, column=0)
    frame2.grid(row=1, column=0)
    frame3.grid(row=2, column=0)

    label = Label(frame1, text="引流款 (低價，高需求 ) \n衝評價或是利用免運門檻來提高客單價進行收單。", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    label.grid(row = 0 , column = 0)
    pt1 = pandastable.Table(frame1, dataframe=df1, showtoolbar=True, showstatusbar=True)

    label2 = Label(frame2, text="地雷款 (低價，低需求)\n地雷款基本上此區商品不是主要營收來源，上架商品順序的話，會建議盡量先避開此區商品。", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    pt2 = pandastable.Table(frame2, dataframe=df2, showtoolbar=True, showstatusbar=True)
    label2.grid(row=0, column=0)
    label3 = Label(frame3, text="引流款 (低價，高需求 ) \n衝評價或是利用免運門檻來提高客單價進行收單。", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    label3.grid(row=0, column=0)
    pt3 = pandastable.Table(frame3, dataframe=df3, showtoolbar=True, showstatusbar=True)

    pt1.show()
    pt2.show()
    pt3.show()

    root.mainloop()


def GUI_3(df):
        def button_event():
            low = int(myentry1.get())
            high = int(myentry2.get())
            df2 = df[(df['價格'] > low) & (df['價格'] < high)]
            df2 = df2.reset_index(drop=True)
            show_GUI_table(df2)
            root.destroy()
        root = tkinter.Tk()
        root.title('同類商品價格查詢')
        root.geometry('400x100')
        title = tkinter.Label(root, text='同類商品價格查詢', bg='yellow', fg='#263238', font=('Arial', 12))
        title.grid(row=0, column=0)
        var1 = tkinter.StringVar()
        var2 = tkinter.StringVar()
        myentry1 = tkinter.Entry(root, width=20, textvariable=var1)
        myentry1.grid(row=1, column=0)
        text1 = tkinter.Label(root, text='到', bg='yellow', fg='#263238', font=('Arial', 12))
        text1.grid(row=1, column=1)
        myentry2 = tkinter.Entry(root, width=20, textvariable=var2)
        myentry2.grid(row=1, column=2)
        mybutton = tkinter.Button(root, text='Search', command=button_event)
        mybutton.grid(row=2, column=2)
        root.mainloop()
        return