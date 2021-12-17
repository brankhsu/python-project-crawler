import GUI
import shopee_data


#keyword = GUI.inputbox()
df = shopee_data.create_df("廚具")
GUI.mainframe(df)



