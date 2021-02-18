import io,sys
import os


#Get your PC's PATH
repositorypath=os.getcwd()
print(repositorypath)


sys.path.append(repositorypath)

from folder_finding import find_docx_in_folder
from docx_extract import docx_to_xlsx_multi
from docx_to_exist import docx_to_xlsx_exist

def main():

    #install essential package
    # os.system('pip install python-docx')
    # os.system('pip install xlsxwriter')
    # os.system('pip install pandas')
    # os.system('pip install workbook')
    # os.system('pip install openpyxl')
    
    #clear console
    os.system('cls')

    
if __name__=="__main__":
    main()