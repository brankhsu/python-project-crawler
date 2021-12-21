import GUI
import shopee_data


keyword = GUI.inputbox()
list= shopee_data.create_df(keyword)
prev_df = list[0]
after_df = list[1]
GUI.mainframe(prev_df,after_df,keyword)



