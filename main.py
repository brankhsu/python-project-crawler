import GUI
import shopee_data

#輸入
keyword = GUI.inputbox()
#爬取資料
list= shopee_data.create_df(keyword)
#正規化前的dataset
prev_df = list[0]
#正規化後的dataset
after_df = list[1]
#顯示mainFrame
GUI.mainframe(prev_df,after_df,keyword)



