from importlib.resources import path
import pathlib 
import os
import shutil
import glob
import os.path, time
from datetime import datetime

def arrange_year():
    ruta=pathlib.Path(".")
    for file in ruta.iterdir():       
        date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y") # Convert string to date format
        year=str(date_of_created.year)
        month=str(date_of_created.month)
        print(year)
        if os.path.exists(year)==True and os.path.exists(f'{year}/{month}')==True:
            pass
        else:
            os.makedirs(f'{year}/{month}')
        Folders=[]
        Folders.append(year)

        foldExt=""
        fol= [file for file in ruta.iterdir() if file.suffix in foldExt]           
    for file in ruta.iterdir():

            date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y")
            year=str(date_of_created.year) 
            month=str(date_of_created.month) 
            if file not in fol:  

                shutil.move(file,f'{year}/{month}')
            
if __name__=="__main__":
    
    arrange_year()
