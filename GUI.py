import tkinter
from tkinter import *
import pandastable
import shopee_data as sd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from graphic_data import draw_scatter_figure


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

    def button1():
        show_graph()  # 畫圓餅圖
        return

    def button2(df):
        # GUI_2(df) #列出4大種類
        return

    def button3(df):
        # GUI_3(df) #同類商品價格
        return

    t = tkinter.Tk()
    t.title('蝦皮產品分析')
    t['bg'] = 'RoyalBlue'
    start_frame = Frame(width=1000, height=500)
    button_frame = Frame(width=1000, height=100, pady=10)
    start_frame.grid(row=0, column=0, padx=1, pady=3)
    button_frame.grid(row=2, column=0)

    fontStyle = tkinter.font.Font(family="Lucida Grande", size=30)
    button_fontStyle = tkinter.font.Font(family="Lucida Grande", size=10)
    button_width = 34
    button_height = 4
    button1 = Button(button_frame, text='目前最熱門', width=button_width, height=button_height, font=button_fontStyle,
                     fg='SlateGray')
    button1.grid(row=2, column=0)
    button2 = Button(button_frame, text='商品分析', width=button_width, height=button_height, font=button_fontStyle,
                     fg='SlateGray')
    button2.grid(row=2, column=1)
    button3 = Button(button_frame, text='', width=button_width, height=button_height, font=button_fontStyle,
                     fg='SlateGray')
    button3.grid(row=2, column=2)
    exit = Button(button_frame, text='退出', width=button_width, height=button_height, command=exit_frame,
                  font=button_fontStyle, fg='SlateGray')
    exit.grid(row=2, column=3)
    label = Label(start_frame, text="本程式想要利用競品情報來提高自己銷售業績:\n 1.找出目前最熱門商品的特性\n 2.上架商品價格分析\n 3.商品訂價策略", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    label.pack(side=LEFT)
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
    df['出現次數'].plot(kind='pie', title='圓餅圖', figsize=(4, 4))
    return


def GUI_2(df):
    median = draw_scatter_figure(df)
    median_sold = median[0]
    median_price = median[1]

    df1 = df[df['已售出數量'] > median_sold and df['價格'] < median_price]  # 低價高需求
    df2 = df[df['已售出數量'] < median_sold and df['價格'] < median_price]  # 低價低需求
    dfˇ = df[df['已售出數量'] < median_sold and df['價格'] > median_price]  # 高價低需求

    t = tkinter.Tk()
    t.title('蝦皮產品分析')
    t['bg'] = 'RoyalBlue'
    fontStyle = tkinter.font.Font(family="Lucida Grande", size=30)
    frame1 = Frame(width=1000, height=350)
    frame2 = Frame(width=1000, height=350)
    frame3 = Frame(width=1000, height=350)
    frame1.grid(row=0, column=0, sticky=t.E + t.W)
    frame2.grid(row=1, column=0, sticky=t.E + t.W)
    frame3.grid(row=2, column=0, sticky=t.E + t.W)

    label = Label(frame1, text="引流款 (低價，高需求 ) \n 衝評價或是利用免運門檻來提高客單價進行收單。", justify=LEFT,
                  bd=180, font=fontStyle, fg='SlateGray')
    label.grid(row = 0 , column = 0)
    pt1 = pandastable.Table(frame1, dataframe=df1, showtoolbar=True, showstatusbar=True)
    pt1.grid(row = 1 ,column = 0)
    pt1.show()



    t.mainloop()


def GUI_3(df):
    return
