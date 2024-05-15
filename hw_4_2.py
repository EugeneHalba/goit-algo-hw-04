from pathlib import Path
path = Path ()
try:
    def get_cats_info(path):
        with open (path , "r", encoding="utf-8") as file:
            cats_list = []
            cats_info = []
            cats_dict = {}      
            for line in file:
                cats_info.append(line.split(','))
            for string in cats_info:
                cats_id = string[0] 
                cats_name = string [1]
                cats_age = string [2]      
                cats_dict ={'id':cats_id, 'name':cats_name, 'age':cats_age}   
                cats_list.append(cats_dict)
                cats_info = cats_list 
        return cats_info
except Exception as e:
    print(f'{e} ')
                         
cats_info = get_cats_info('/Users/macbookkiev/Documents/PYTON/my_repo/HW_4/HW_4_1/cats_file.txt')
print (*cats_info, sep='\n')
