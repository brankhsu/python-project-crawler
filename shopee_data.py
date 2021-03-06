import jieba
import requests
import fake_useragent
import pandas
import jieba.analyse
import organize_data

user_agent = fake_useragent.UserAgent()
name = []
historical_sold = []
price = []
shop_location = []
number_of_transactions = 100  #須為100的倍數

#把資料爬下來，放入正確的陣列內
def add_data(url):
    req = requests.get(url, headers={ 'user-agent': user_agent.random })
    data = req.json()
    data2 = data["items"]

    for i in range(len(data2)):
        name.append(data2[i]['item_basic']['name'])
        historical_sold.append(data2[i]['item_basic']['historical_sold'])
        price.append(data2[i]['item_basic']['price'] / 100000)
        shop_location.append(data2[i]['item_basic']['shop_location'] )



def create_df(word):
    keyword = word
    for i in range(0, number_of_transactions, 100):
        url = 'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword='+keyword+'&limit='+str(100)+'&newest='+str(i)+'&order=desc&page_type=search&version=2'
        add_data(url)

    df = pandas.DataFrame({
        '商品名稱': name,
        '已售出數量': historical_sold,
        '價格': price,
        '賣家地址':shop_location
    })
    df1 = df.copy(deep=True) #它返回 DataFrame 的副本，並且設定副本更動不影響原值
    for i in range(5):
        df1 = organize_data.remove_zero(df1)
        df1 = organize_data.remove_outliers(df1)
    df1 = df1.reset_index(drop=True)
    return [df,df1]


def count():
    jieba.analyse.set_stop_words("stop.txt")
    text = ''
    #統計商品名子
    for i in name:
        text += i
    #找除前十項出現次數的詞
    tags = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
    name2 = []
    times = []
    #分別將商品名稱和出現次數家到list
    for tag, weight in tags:
        name2.append(tag)
        times.append(int(weight * 10000))
    count_df = pandas.DataFrame({
        '商品名稱': name2,
        '出現次數': times,
    })
    #為了畫圓餅圖設定index
    count_df.set_index('商品名稱' , inplace=True)
    return count_df