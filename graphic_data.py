import tkinter
import pandastable
import matplotlib.pyplot as plt
import numpy as np


def draw_scatter_figure(df):
    historical_sold = df['已售出數量']
    price = df['價格']

    plt.style.use("ggplot")
    plt.scatter(historical_sold, price, c='green', s=20, label='revenue')
    plt.title('Scatter map for PChome product information', fontsize=20)
    plt.xlabel('Quntity')
    plt.ylabel('Price(NT$)')
    # tick_arr_x = np.arange(0,22,2)
    # plt.xticks(tick_arr_x)
    # tick_arr_y = np.arange(0, 500, 100)
    # plt.yticks(tick_arr_y)
    plt.legend(loc='best')

    plt.axline((np.median(historical_sold), 0),
               (np.median(historical_sold), 20)
               )  # 畫數量中位數直線
    plt.axline((0, np.median(price)),
               (20, np.median(price))
               )  # 畫價錢中位數橫線

    # print("數量中位數: "+str(np.median(historical_sold)))
    # print("價錢中位數: NT$"+str(np.median(price)))

    # plt.show()
    return [np.median(historical_sold), np.median(price)]


def draw_box_figure(df):
    plt.style.use("ggplot")
    # plt.figure(figsize=(2, 5))

    plt.subplot(1, 2, 1)
    plt.title('historical_sold')
    plt.boxplot(df['已售出數量'], showmeans=True)

    plt.subplot(1, 2, 2)
    plt.title('price')
    plt.boxplot(df['價格'], showmeans=True)

    plt.show()


def window_result(df):
    app = tkinter.Tk()
    app.geometry('600x400+200+100')
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)

    table = pt = pandastable.Table(f, dataframe=df,
                                   showtoolbar=True, showstatusbar=True)
    pt.show()
    app.mainloop()


def show_GUI_table(df):
    app = tkinter.Toplevel()
    # app.geometry('600x400+200+100')
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)
    f.grid(row=0, column=0)

    pt = pandastable.Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
    pt.show()
    app.mainloop()