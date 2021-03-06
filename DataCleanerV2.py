'''
Created on Feb 23, 2021

@author: prasanna
'''

import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog


#1.Creating a dialog box enabling the user to select the desired excel
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

#2.function that allows  the user to select the data
def getExcel ():
    global df
    import_file_path = filedialog.askopenfilename()
    u=import_file_path
    return u

#end of the function

#3.code that links the function and the gui
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

var=getExcel ()
#print(var)

#data maipulation

df=pd.read_excel(r'D:/Data_analysis_with_python/counterparties.xlsx')

df=df.set_index('Sno.')

#apply map used here to make all the items to uppercase
df=df.applymap(lambda x: x.upper() if type(x)== str else x)

df=df.applymap(lambda x: x.replace('[.:@"]',''))
df=df.applymap(lambda x: x.replace("'",""))
df['CounterpartyName']=df['CounterpartyName'].str.replace('LTD','')
df['CounterpartyName']=df['CounterpartyName'].str.replace('LIMITED','')
df['CounterpartyName']=df['CounterpartyName'].str.replace(' ','')
df=df.duplicated(keep='first')
l=(df[df])
y='The duplicates are:'

top = tk.Toplevel()
msg2=tk.Label(top,text=y,anchor='w')
msg2.pack()
msg = tk.Label(top, text=l,anchor='w')
msg.pack()
frame = tk.Frame(top, width=500, height=500)
frame.pack()
root.mainloop()

