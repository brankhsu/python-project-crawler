import pandastable
import requests
import fake_useragent
import pandas
import tkinter
import time
import jieba
import jieba.analyse
import tkinter as tk
from tkinter import ttk
user_agent = fake_useragent.UserAgent()
text = ''
itemid = []
shopid = []
name = []
brand = []
shop_location = []
ctime = []
can_use_wholesale = []
show_free_shipping = []
shopee_verified = []
show_shopee_verified_label = []
is_official_shop = []
show_official_shop_label = []
show_official_shop_label_in_title = []
is_adult = []
historical_sold = []
stock = []
liked_count = []
view_count = []
currency = []
has_lowest_price_guarantee = []
discount = []
price = []
price_before_discount = []
price_min = []
price_max = []
price_min_before_discount = []
price_max_before_discount = []
cmt_count = []
item_rating = []
image = []
images = []
video_info_list = []
tier_variations = []
number_of_transactions = 100  #須為100的倍數
def add_shop_data(url):
    global text
    req = requests.get(url, headers={ 'user-agent': user_agent.random })
    # print(req.text)
    data = req.json()
    data2 = data["items"]
    # print(data2)
    for i in range(len(data2)):
        #itemid.append(data2[i]['itemid'])
        #shopid.append(data2[i]['shopid'])
        name.append(data2[i]['name'])
        text = str(text+data2[i]['name'])
        #brand.append(data2[i]['brand'])
        #shop_location.append(data2[i]['shop_location'])
        #ctime.append(data2[i]['ctime'])
        #can_use_wholesale.append(data2[i]['can_use_wholesale'])
        #show_free_shipping.append(data2[i]['show_free_shipping'])
        #shopee_verified.append(data2[i]['shopee_verified'])
        #is_official_shop.append(data2[i]['is_official_shop'])
        #show_official_shop_label.append(data2[i]['show_official_shop_label'])
        #show_official_shop_label_in_title.append(data2[i]['show_official_shop_label_in_title'])
        #is_adult.append(data2[i]['is_adult'])
        historical_sold.append(data2[i]['historical_sold'])
        stock.append(data2[i]['stock'])
        liked_count.append(data2[i]['liked_count'])
        view_count.append(data2[i]['view_count'])
        currency.append(data2[i]['currency'])
        #has_lowest_price_guarantee.append(data2[i]['has_lowest_price_guarantee'])
     #   discount.append(data2[i]['discount'])
        price.append(data2[i]['price']/10000)
        #price_before_discount.append(data2[i]['price_before_discount']/10000)
        #price_min.append(data2[i]['price_min']/10000)
        #price_max.append(data2[i]['price_max']/10000)
        #price_min_before_discount.append(data2[i]['price_min_before_discount']/10000)
        #price_max_before_discount.append(data2[i]['price_max_before_discount']/10000)
        #cmt_count.append(data2[i]['cmt_count'])
        #item_rating.append(data2[i]['item_rating'])
        #image.append(data2[i]['image'])
        #images.append(data2[i]['images'])
        #video_info_list.append(data2[i]['video_info_list'])
        #tier_variations.append(data2[i]['tier_variations'])


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


def create_shop_df(keyword):
    for i in range(0, number_of_transactions, 100):
        url = 'https://shopee.tw/api/v2/search_items/?by=relevancy&keyword='+keyword+'&limit='+str(100)+'&newest='+str(i)+'&order=desc&page_type=search&version=2'
        #print(url)
        add_shop_data(url)
        time.sleep(1)
    df = pandas.DataFrame({
        #'商品ID': itemid,
        #'賣場ID': shopid,
        '商品名稱': name,
        #'品牌':brand,
        #'賣場位置(出貨地):':shop_location,
        #'上架時間(時間戳)':ctime,
        #'是否有多件優惠':can_use_wholesale,
        #'是否顯示免運':show_free_shipping,
        #'是否為蝦皮優選':shopee_verified,
        # '是否顯示蝦皮優選標籤':show_shopee_verified_label,
        #'是否為官方商店':is_official_shop,
        #'是否在標題中顯示官方商店標籤':show_official_shop_label_in_title	,
        #'是否為成人商品':is_adult,
        '已售出數量':historical_sold,
        '庫存':stock,
        '喜歡數':liked_count,
        '瀏覽數':view_count,
        '貨幣':currency,
        #'最低價格保證':has_lowest_price_guarantee,
        #'折扣':discount,
        '價格(要再除100000)':price
        #'折扣前價格':price_before_discount,
        #'價格範圍(最低)':price_min,
        #'價格範圍(最高)':price_max,
        #'折扣前價格範圍(最低)':price_min_before_discount,
        #'折扣前價格範圍(最高)':price_max_before_discount
        #'評價數量':cmt_count,
        #'評價':item_rating,
        #'商品圖片(封面)':image,
        #'商品圖片':images,
        #'影片':video_info_list,
        #'規格':tier_variations

    })
    return df
def count():
    jieba.analyse.set_stop_words("stop.txt")
    tags = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
    for tag, weight in tags:
        print(tag + "," + str(int(weight * 10000)))
    return
def clustering():
    return
def graph():
    graph_dict = {
        '價格':price,
        'sold': historical_sold
    }
    garph_df = pandas.DataFrame(graph_dict)
    garph_df.plot(kind='scatter', title='散佈圖', alpha = .5, figsize=(6, 4), x='price', y='historical_sold',)
    #garph_df.show()
    return


def inputbox():
    window = tk.Tk()
    window.title('今天什麼最銷售')
    window.geometry('400x100')
    title = tk.Label(window, text='輸入想查詢的商品', bg='yellow', fg='#263238', font=('Arial', 12))
    title.grid(column=0, row=0, sticky=tk.W)
    key = tk.StringVar()
    keyword = tk.StringVar()
    entry = tk.Entry(window ,width = 20,textvariable =key)
    entry.grid(column = 1 , row = 0 , padx = 10)
    resultButton = tk.Button(window, text='Search',command=keyword.set(key.get()))
    resultButton.grid(column = 0 , row = 2 , sticky = tk.W)
    window.mainloop()
    return keyword.get()

def inputbox2():
    def button_event():
        print(var.get())

    root = tk.Tk()
    root.title('今天什麼最銷售')
    root.geometry('400x100')
    title = tk.Label(root, text='輸入想查詢的商品', bg='yellow', fg='#263238', font=('Arial', 12))
    title.grid(row=0, column=0)

    var = tk.StringVar()
    myentry = tk.Entry(root ,width = 20,textvariable =var)
    myentry.grid(row=0, column=1)

    mybutton = tk.Button(root, text='Search', command=button_event)
    mybutton.grid(row=1, column=1)

    root.mainloop()
    return var.get()