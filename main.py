import GUI
import shopee_data


keyword = GUI.inputbox()
df = shopee_data.create_df(keyword)
print(df)
GUI.mainframe(df,keyword)



