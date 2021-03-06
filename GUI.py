import tkinter
from tkinter import *
import shopee_data as sd
import matplotlib.pyplot as plt
import map
from graphic_data import draw_scatter_figure, show_GUI_table
from tkhtmlview import HTMLLabel


# tkinter 套件
# 建立容器 tkinter.Tk()
# 設定視窗名子 .title
# 各類元件
# 建立框架 Frame()
# 標籤 label() (放圖或文字)
# 按鈕 button() (透過event觸發寫好的函式)
# 布局
# 設定布局 grid() (從左上 0,0開始)
# 控制視窗
# tk.mainloop() (一直顯示)
# destroy()  關掉該視窗
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


def mainframe(df,df1,keyword):
    def create_map():
        GUI_4() #地圖

    def action1():
        show_graph()  # 畫圓餅圖

    def action2():
        draw_scatter_figure(df1) #列出4大種類

    def action3():
        GUI_3(df) #同類商品價格
    t = tkinter.Tk()
    button_width = 34
    button_height = 4
    t.title('蝦皮產品分析')
    start_frame = Frame(width=1000, height=500)
    button_frame = Frame(width=1000, height=100, pady=10)
    start_frame.grid(row=0, column=0)
    button_frame.grid(row=2, column=0)

    fontStyle = tkinter.font.Font(family="Lucida Grande", size=30)
    fontStyle2 = tkinter.font.Font(family="Lucida Grande", size=20)
    button_fontStyle = tkinter.font.Font(family="Lucida Grande", size=10)

    button1 = Button(button_frame, text='目前最熱門', width=button_width, height=button_height, command=action1,font=button_fontStyle,fg='SlateGray')
    button1.grid(row=2, column=0)
    button2 = Button(button_frame, text='商品價格分布(以除去離群值)', width=button_width, height=button_height, command=action2, font=button_fontStyle,
                     fg='SlateGray')
    button2.grid(row=2, column=1)
    button3 = Button(button_frame, text='同類商品價格查詢', width=button_width, height=button_height,  command=action3,font=button_fontStyle,
                     fg='SlateGray')
    button3.grid(row=2, column=2)
    exit = Button(button_frame, text='產生地圖', width=button_width, height=button_height, command=create_map,
                  font=button_fontStyle, fg='SlateGray')
    exit.grid(row=2, column=3)
    label= Label(start_frame, text="現在搜尋的是蝦皮商場上"+keyword+"的資訊"+"\n\n\n\n\n本程式想要利用競品情報來提高自己銷售業績:\n 1.找出目前最熱門商品的特性\n 2.上架商品價格分析\n 3.商品訂價策略", justify=LEFT,
                  bd=180, font=fontStyle2, fg='SlateGray')
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
    plt.show()
    return


def GUI_3(df):
        def button_event():
            # 將取到的價格轉數字以利於比大小
            low = int(myentry1.get())
            high = int(myentry2.get())
            df2 = df[(df['價格'] > low) & (df['價格'] < high)]
            #補齊index
            df2 = df2.reset_index(drop=True)
            #關掉視窗
            root.destroy()
            show_GUI_table(df2)


        root = tkinter.Tk()
        root.title('同類商品價格查詢')
        root.geometry('400x100')
        title = tkinter.Label(root, text='同類商品價格查詢', bg='yellow', fg='#263238', font=('Arial', 12))
        title.grid(row=0, column=0)
        #tkinter entry 輸入的變數要是stringVar
        #設定 => stringVar.set()
        #書櫥 => stringVar.get()
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
def GUI_4():
    map.createMap()

    root = tkinter.Tk()
    root.title("showMap")
    root.geometry("200x200")
    #有能夠接受html格式參數的label
    mylabel = HTMLLabel(root , html =r"<h1><a href = '.\map.html'>Go to map!!!</a> <h1>")

    mylabel.grid(row = 0 , column = 0)
    root.mainloop()

