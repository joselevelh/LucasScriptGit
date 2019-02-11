from tkinter import filedialog
from tkinter import *
import csv

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.CSV"),("all files","*.*")))
print (root.filename)

csvList=[]
csvList=list(csv.reader(open(root.filename)))#This puts csv files into a 2d list
print(csvList)

print("Rows: =",len(csvList),"\ncollumns: ",len(csvList[0]))
print("last Row Size: ", len(csvList[len(csvList)-1]),"\n")


def truncateCsv(uList):   #Truncates the 2d array until all collumns have the same number of Rows
    tempList=uList
    while(len(tempList[0])!=len(tempList[len(tempList)-1])):
        del tempList[-1]
        print("deleted last Row")
    print("Rows: =",len(tempList),"\ncollumns: ",len(tempList[0]))
    print("last Row Size: ", len(tempList[len(tempList)-1]),"\n")
    return tempList


def transposeCsv(OldList): #transpose the 2d list given
    newlist = []
    i = 0
    while i < len(OldList[i]):
        j = 0
        vec = []
        while j < len(OldList):
            vec.append(OldList[j][i])
            j = j + 1
        newlist.append(vec)
        i = i + 1
    return newlist

truncatedList=truncateCsv(csvList)
print (transposeCsv(truncatedList))
