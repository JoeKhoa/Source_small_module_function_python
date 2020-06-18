import pandas as pd 

movies_excel_file = 'movies.xls'
movies_data = pd.read_excel(movies_excel_file)
# print(movies_data.head(10))
movies_sheet1= pd.read_excel(movies_excel_file,sheet_name=2,index_col=1)
# print(movies_sheet1.head(10))
excel_file_info = pd.ExcelFile(movies_excel_file)
"""get all excel file information"""
#sheet_name
file_sheet_names = excel_file_info.sheet_names
print(type(file_sheet_names))


for name in file_sheet_names:
    print(name)