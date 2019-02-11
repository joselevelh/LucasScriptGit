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

def csvTruncate(uFile):

def transpose(OldList): #transpose the 2d list given
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
#print (transpose(csvList))
#Stuff=[[1,2],[4,5],[7,8]]
#newStuff=transpose(Stuff)
#print (newStuff)
