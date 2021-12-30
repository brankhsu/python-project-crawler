from geopy.geocoders import Nominatim
import folium
import shopee_data
from folium.plugins import MarkerCluster

#給地名 求 經緯度
def gps_loaction(address):
    gps = Nominatim(user_agent="SkittBot")
    location = gps.geocode(address)
    return {'lon':location.longitude, 'lat':location.latitude}


def createMap():
    print("正在初始化地圖...")
    # 開啟一張初始地圖
    m0 = folium.Map([23.5, 121], zoom_start=7)
    # 座標群集化
    marker_cluster = MarkerCluster().add_to(m0)
    #dataFrame資料
    df = shopee_data.create_df('廚具')[0]
    # 將座標資料標註在地圖上
    print("這可能會需要一點時間...")
    for i in range(len(df)):
        print(f"第{i}筆位置以標註在地圖上")
        if (df['賣家地址'].equals('None')):  # 沒有地址資訊的不標記在地圖上
            continue
        # 做標點開後的說明(小框框)(HTML格式)
        information = '<b>商品名稱:</b><i>' + str(df['商品名稱'][i]) + '</i><br>' \
                      + '<b>已售出數量:</b><i>' + str(df['已售出數量'][i]) + '</i><br>' \
                      + '<b>價格:</b><i>' + str(df['價格'][i]) + '</i>'
        #print(information)
        lon = gps_loaction(df['賣家地址'][i])['lon']
        lat = gps_loaction(df['賣家地址'][i])['lat']
        #print('經度:{},緯度:{}'.format(lon, lat))
        folium.Marker(location=[lat, lon], popup=information).add_to(marker_cluster)
    print('map done')

    # 地圖會出html檔
    m0.save('map.html')


