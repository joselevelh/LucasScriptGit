from tkinter import filedialog
from tkinter import *
import csv

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.CSV"),("all files","*.*")))
print (root.filename)

#with open(root.filename, newline='') as csvfile:
    #LucasCSV = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #for row in LucasCSV:
        #print(', '.join(row))
def getCols(rList,numElements):
    for rows in rList:
        for cols in rList[rows]:
            NewList[cols][rows]=rList[rows][cols]
    return NewList
testList=[[1,2,3],[4,5,6],[7,8,9]]
#getCols(testList,9)
print(getCols(testList,9))
