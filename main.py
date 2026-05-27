import os
import shutil

while True:
    with os.scandir("C:/Users/Aayush/Downloads") as it:
        bool = os.path.exists('C:/Users/Aayush/Downloads')

        if bool:
            for entry in it:
                if entry.name.endswith(".exe") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsexe')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsexe')
            for entry in it:
                if entry.name.endswith(".exe") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsexe')
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadspdf')
        if bool1:
            for entry in it:
                if entry.name.endswith(".pdf") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadspdf')
        else:
            os.mkdir('C:/Users/Aayush/Downloadspdf')
            for entry in it:
                if entry.name.endswith(".pdf") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadspdf')            
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadsmsi')

        if bool1:
            for entry in it:
                if entry.name.endswith(".msi") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsmsi')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsmsi')
            for entry in it:
                if entry.name.endswith(".msi") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsmsi') 
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadsppt')

        if bool1:
            for entry in it:
                if entry.name.endswith(".ppt") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsppt')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsppt')
            for entry in it:
                if entry.name.endswith(".ppt") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsppt') 
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadszip')

        if bool1:
            for entry in it:
                if entry.name.endswith(".zip") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadszip')
        else:
            os.mkdir('C:/Users/Aayush/Downloadszip')
            for entry in it:
                if entry.name.endswith(".zip") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadszip') 
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadsrar')

        if bool1:
            for entry in it:
                if entry.name.endswith(".rar") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsrar')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsrar')
            for entry in it:
                if entry.name.endswith(".rar") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsrar')
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadsxlsx')
        if bool1:
            for entry in it:
                if entry.name.endswith(".xlsx") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsxlsx')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsxlsx')
            for entry in it:
                if entry.name.endswith(".xlsx") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsxlsx')
    ######################################################################################################################################################################
    with os.scandir("G:\Downloads") as it:
        bool1 = os.path.exists('C:/Users/Aayush/Downloadsiso')
        if bool1:
            for entry in it:
                if entry.name.endswith(".iso") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}','C:/Users/Aayush/Downloadsiso')
        else:
            os.mkdir('C:/Users/Aayush/Downloadsiso')
            for entry in it:
                if entry.name.endswith(".iso") and entry.is_file():
                    name = entry.name
                    shutil.move(f'C:/Users/Aayush/Downloads{name}',f'C:/Users/Aayush/Downloadsiso')