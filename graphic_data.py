import tkinter
import pandastable
import matplotlib.pyplot as plt
import numpy as np


def draw_scatter_figure(df):
    historical_sold = df['已售出數量']
    price = df['價格']

    plt.style.use("ggplot")
    plt.scatter(historical_sold, price, c='green', s=20, label='revenue')
    plt.title('Scatter map for shopee product information', fontsize=20)
    plt.xlabel('Quntity')
    plt.ylabel('Price(NT$)')
    plt.legend(loc='best')

    plt.axline((np.median(historical_sold), 0),
               (np.median(historical_sold), 20)
               )  # 畫數量中位數直線
    plt.axline((0, np.median(price)),
               (20, np.median(price))
               )  # 畫價錢中位數橫線

<<<<<<< HEAD
    plt.show()
    return [np.median(historical_sold), np.median(price)]


=======
    # plt.show()
    return [np.median(historical_sold) , np.median(price)]
>>>>>>> 40159c6b4ea7b4eb4bd279ea8f3f4c2c4b1be703
def draw_box_figure(df):
    plt.style.use("ggplot")

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
<<<<<<< HEAD
    app = tkinter.Toplevel()
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)
    f.grid(row=0, column=0)

    pt = pandastable.Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
=======

    app = tkinter.Toplevel()
    # app.geometry('600x400+200+100')
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)
    f.grid(row = 0 , column = 0)

    pt = pandastable.Table(f, dataframe=df,showtoolbar=True, showstatusbar=True)
>>>>>>> 40159c6b4ea7b4eb4bd279ea8f3f4c2c4b1be703
    pt.show()
    app.mainloop()