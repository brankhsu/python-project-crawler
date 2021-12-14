import jieba
import pandastable
import requests
import fake_useragent
import pandas
import tkinter
import time
import jieba.analyse
import graphic_data
import organize_data



user_agent = fake_useragent.UserAgent()
name = []
historical_sold = []
price = []
number_of_transactions = 500  #須為100的倍數

def add_data(url):
    req = requests.get(url, headers={ 'user-agent': user_agent.random })
    data = req.json()
    data2 = data["items"]

    for i in range(len(data2)):
        name.append(data2[i]['item_basic']['name'])
        historical_sold.append(data2[i]['item_basic']['historical_sold'])
        price.append(data2[i]['item_basic']['price'] / 100000)

def show_GUI_table(df):
    app = tkinter.Tk()
    app.geometry('600x400+200+100')
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)

    table = pt = pandastable.Table(f, dataframe=df,
                                   showtoolbar=True, showstatusbar=True)
    pt.show()
    app.mainloop()


def create_df(word):
    keyword = word
    for i in range(0, number_of_transactions, 100):
        url = 'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword='+keyword+'&limit='+str(100)+'&newest='+str(i)+'&order=desc&page_type=search&version=2'
        add_data(url)

    df = pandas.DataFrame({
        '商品名稱': name,
        '已售出數量': historical_sold,
        '價格': price,
    })
    for i in range(5):
        df = organize_data.remove_zero(df)
        df = organize_data.remove_outliers(df)
    return df

def count():
    jieba.analyse.set_stop_words("stop.txt")
    text = ''
    for i in name:
        text += i
    tags = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
    name2 = []
    times = []
    for tag, weight in tags:
        name2.append(tag)
        times.append(int(weight * 10000))
    count_df = pandas.DataFrame({
        '商品名稱': name2,
        '出現次數': times,
    })
    count_df.set_index('商品名稱' , inplace=True)
    return count_df
