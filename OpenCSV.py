from tkinter import filedialog
from tkinter import *
import csv
from statistics import mean


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.CSV"),("all files","*.*")))
#print (root.filename)

csvList=[]
csvList=list(csv.reader(open(root.filename)))#This puts csv files into a 2d list
#print(csvList)

print("Rows: =",len(csvList),"\nColumns: ",len(csvList[0]))
print("last Row Size: ", len(csvList[len(csvList)-1]),"\n")


def truncateCsv(uList):   #Truncates the 2d array until all Columns have the same number of Rows
    tempList=uList
    while(len(tempList[0])!=len(tempList[len(tempList)-1])):
        del tempList[-1]
        print("deleted last Row")
    print("Rows: =",len(tempList),"\nColumns: ",len(tempList[0]))
    print("last Row Size: ", len(tempList[len(tempList)-1]),"\n")
    return tempList


def transposeCsv(OldList): #transpose the 2d list given
    newlist = []
    i = 0
    while i < len(OldList[i]):
        j = 0
        vec = []
        while j < len(OldList)-1:
            vec.append(OldList[j][i])
            j = j + 1
        newlist.append(vec)
        i = i + 1
    return newlist

def printData(niceData):    # parse the truncated 2d list for relevant data and print it nicely.
    numCols=len(niceData)   #Amount of columns in niceData
    #numRows=len(niceData[0])    #Amount of rows in the first Column Column
    colCounter=1    #We want to skip the first Column because it is the time Column and therefore does not contain integer data.
    while (colCounter<numCols):   #go through every Column.
        ColumnTitle=niceData[colCounter][0]   #The first element of each Column is the title of that Column.
        ColumnData=niceData[colCounter][1:]   #The rest of the elements in each Column are data strings.
        n=0
        while(n<len(ColumnData)-1):
            ColumnData[n]=list(filter(None,ColumnData[n]))   #Filter the list for empty strings.
            n+=1
        ColumnData=list(map(int,ColumnData[0]))   #Make the list of strings into integers.
        ColumnMean= mean(ColumnData[0])
        #ColumnStdev= statistics.stdev(ColumnData)
        #ColumnVar= statistics.variance(ColumnData)
        #ColumnMin=min(ColumnData)
        #ColumnMax=max(ColumnData)
        colCounter+=1
    with open("Output.txt", "w") as text_file:
        print("Column: {}".format(ColumnData), file=text_file)
        print("Mean: {}".format(ColumnMean), file=text_file)

def printData2(niceData):
    thisList=niceData
    thisList=filter(None,thisList[5])
    return thisList


truncatedList=truncateCsv(csvList)
print (transposeCsv(truncatedList))
#printData(transposeCsv(truncatedList))
print
