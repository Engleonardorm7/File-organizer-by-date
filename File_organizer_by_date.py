from importlib.resources import path
import pathlib 
import os
import shutil
import glob
import os.path, time
from datetime import datetime



    # ruta=pathlib.Path(".\OneDrive\Desktop\Platzi\Python\CursoPython_inter\python-programs")
    # for file in ruta.iterdir():
    #     print(file.name)
    #print("la Ubicacion es:", os.getcwd())
    
        
# def arrange():

#     ruta=pathlib.Path("/Users/leona.LAPTOP-20L2TPHV/Downloads/")
    
#     diccionario = { key : [v.name for v in ruta.glob(f'*{key}')] for key in {file.suffix for file in ruta.iterdir()}}
    
#     for extention, files in diccionario.items():
#         #  print(f"extension: {extention}")
#         #  print(f"files: {files}")
#         pass

#     for file in ruta.iterdir():
#         if os.path.exists("Documents")==True:
#             pass
#         else:
#             os.mkdir("Documents")
#         if os.path.exists("Pictures")==True:
#             pass
#         else:
#             os.mkdir("Pictures")
#         if os.path.exists("Programs")==True:
#             pass
#         else:
#             os.mkdir("Programs")
#         if os.path.exists("Others")==True:
#             pass
#         else:
#             os.mkdir("Others")
#         if os.path.exists("Folders")==False:
#             os.mkdir("Folders")

#     Folders= "Others","Programs","Pictures","Documents","Folders"    
#     foldExt=""
#     fol= [file for file in ruta.iterdir() if file.suffix in foldExt]
#     for file in fol:  
#         if file.name not in Folders:  
#             shutil.move(file,"Folders")

#     docsExt= ".py",".doc",".docx",".txt",".odt",".xlsx",".ppt",".pptx",".pdf",".html"       
#     docs= [file for file in ruta.iterdir() if file.suffix in docsExt]
#     for file in docs:    
#          shutil.move(file,"Documents")
        
#     picExt=   ".png",".jpg"
#     pics= [file for file in ruta.iterdir() if file.suffix in picExt]
#     for file in pics: 
#         shutil.move(file,"Pictures")  

#     progExt= ".exe",".msi"
#     prog= [file for file in ruta.iterdir() if file.suffix in progExt]
#     for file in prog: 
#         shutil.move(file,"Programs")  

#     others= [file for file in ruta.iterdir() if file.suffix not in (progExt,picExt,docsExt,foldExt)]
#     for file in others:           
#             shutil.move(file,"Others")

def arrange_year():
    ruta=pathlib.Path(".")
    for file in ruta.iterdir():

        #archivos=(time.ctime(os.path.getctime(file)))
        date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y") # Convert string to date format

        #archivos = glob.glob(ruta+os.path.sep+'*.png')
        #archivos.sort(key=os.path.getctime)
        #print(archivos)
        #print("Date created year: {} , month: {} , day: {}".format(str(date_of_created.year),str(date_of_created.month),str(date_of_created.day)))
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
    #print(Folders)
    for file in ruta.iterdir():

            date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y")
            year=str(date_of_created.year) 
            month=str(date_of_created.month) 
            if file not in fol:  

                shutil.move(file,f'{year}/{month}')

def arrange_month():

    
    ruta=pathlib.Path("/Users/leona.LAPTOP-20L2TPHV/Downloads/Pictures/")

    foldExt=""
    fol= [file for file in ruta.iterdir() if file.suffix in foldExt]           
    
    for file in fol:
        ruta=pathlib.Path(file)
        for file in ruta.iterdir():
            date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y")
            year=str(date_of_created.year)
            month=str(date_of_created.month) 
            print(month)
            if os.path.exists(month)==True:
                pass
            else:
                ubicacion=os.getcwd()+file+'/'
                print(ubicacion)
                print(file)
            Folders_month=[]
            Folders_month.append(month)
        # if file not in fol:  

        #     shutil.move(file,year)




#     for file in ruta.iterdir():
#             date_of_created = datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y")
#             year=str(date_of_created.year) 
#             month=str(date_of_created.month)
#     file_per_year=[file_per_year for file in ruta.iterdir() if year in Folders]
# #     print("your folder has been classified")
            
if __name__=="__main__":
    
    arrange_year()
    #arrange_month()