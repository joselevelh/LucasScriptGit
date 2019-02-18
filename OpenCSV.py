from tkinter import filedialog
from tkinter import *
import csv
from statistics import mean
from statistics import stdev
from statistics import variance


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
    while i < len(OldList[0]):
        j = 0
        vec = []
        while j < len(OldList):
            vec.append(OldList[j][i])
            j = j + 1
        newlist.append(vec)
        i = i + 1
    return newlist

def printData(niceData):    # parse the truncated 2d list for relevant data and print it nicely onto a text file.
    with open("Output.txt", "w") as text_file:
        numCols=len(niceData)   #Amount of columns in niceData
        i=1    #We want to skip the first Column because it is the time Column and therefore does not contain integer data.
        while (i<numCols):   #go through every Column.
            cTitle=niceData[i][0]   #The first element of each Column is the title of that Column.
            cData=niceData[i][1:]   #The rest of the elements in each Column are data strings.
            #print ("This is the title: ",cTitle)
            #print (" This is the Data as strings: ",cData)
            cData=list(map(int,cData))
        #    print (" This is the Data as integers: ",cData)
            #cData=list(map(int,cData[i]))   #Make the list of strings into integers.
            cMean= mean(cData)
            cStdev= stdev(cData)
            cVar= variance(cData)
            cMin=min(cData)
            cMax=max(cData)
        #    print (" This is the mean: ",cMean)
        #    print (" This is the Standard Deviation: ",cStdev)
        #    print (" This is the Variance: ",cVar)
        #    print (" This is the min: ",cMin)
        #    print (" This is the max: ",cMax,"\n")
            i+=1
            print("Title: {}".format(cTitle), file=text_file)
            print("Data: {}".format(cData), file=text_file)
            print("Mean: {}".format(cMean), file=text_file)
            print("Standard Deviation: {}".format(cStdev), file=text_file)
            print("Variance: {}".format(cVar), file=text_file)
            print("Min: {}".format(cMin), file=text_file)
            print("Max: {}".format(cMax), file=text_file)
            print("\n", file=text_file)

def removeBlanks(bList): #bList is a list of lists with elements that may be empty strings, we want to remove these empty strings.
    wBlanks=bList
    i=0
    while(i<len(wBlanks)):
        j=0
        while(j<len(wBlanks[i])):
            if not (wBlanks[i][j]):
                del wBlanks[i][j]
            else:   #We must check the same position again if we remove a blank because all the elements in the list have now shifted.
                j+=1
        if not (wBlanks[i]):#check if the list is empty.
            del wBlanks[i]
        else:
            i+=1
    return wBlanks

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.CSV"),("all files","*.*")))
#print (root.filename)

csvList=[]
csvList=list(csv.reader(open(root.filename)))#This puts csv files into a 2d list
print(csvList)

print("Now without blanks:\n ")
print(removeBlanks(csvList))

print("Now without extra rows:\n ")
print(truncateCsv(removeBlanks(csvList)))

print("Now with a transpose:\n ")
print(transposeCsv(truncateCsv(removeBlanks(csvList))))

print("Now with data:\n ")
print(printData(transposeCsv(truncateCsv(removeBlanks(csvList)))))

#print("Rows: =",len(csvList),"\nColumns: ",len(csvList[0]))
#print("last Row Size: ", len(csvList[len(csvList)-1]),"\n")

#truncatedList=truncateCsv(csvList)
#print (transposeCsv(truncatedList))
