from tkinter import filedialog
from tkinter import *
import csv
from statistics import mean
from statistics import stdev
from statistics import variance

def newMean(list0):   #gets the mean of the list not including zeros.
    new=[]
    empty=True
    i=0
    while i<len(list0):
        if not list0[i]==0:
            new.append(list0[i])
            if not list0[i] == 0 :
                    empty=False
        i+=1
    if empty:   #the mean function must be non-zero so we are making sure that we return 0 as the mean if the list is all zeroes.
        return 0
    else:
        return mean(new)

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

def printData(niceData,tHold):    # parse the truncated 2d list for relevant data and print it nicely onto a text file.
    #Prompt user for threshold
    thresholdVar= tHold
    tempRaw,tempBsln,tempDela=[],[],[] #initialize temp raw and baseline variables

    with open("Output.txt", "w") as text_file:
        print("Hey ${PERSON_NAME}, \n This email should contain the data you are looking for -Jose Level \n ", file=text_file)
        print("File Opened: {}\n".format(root.filename), file=text_file)
        numCols=len(niceData)   #Amount of columns in niceData
        i=1    #We want to skip the first Column because it is the time Column and therefore does not contain integer data.
        while (i<numCols):   #go through every Column.
            cTitle=niceData[i][0]   #The first element of each Column is the title of that Column.
            if "Diff" in cTitle:   #We only want the Diff_Key... data.
                cData=niceData[i][1:]   #The rest of the elements in each Column are data strings.
                cData=list(map(int,cData))
                cMean= newMean(cData)   #We had to write a new mean function so that it did not include the zeros in the list.
                cStdev= stdev(cData)
                cVar= variance(cData)
                cMin=min(cData)
                cMax=max(cData)
                print("Title: {}".format(cTitle), file=text_file)   #Print all statistics onto the Output.txt file
                #print("Data: {}".format(cData), file=text_file)
                print("Mean: {}".format(cMean), file=text_file)
                print("Standard Deviation: {}".format(cStdev), file=text_file)
                print("Variance: {}".format(cVar), file=text_file)
                print("Min: {}".format(cMin), file=text_file)
                print("Max: {} \n".format(cMax), file=text_file)
                #print("\n", file=text_file)
            elif "Raw" in cTitle:
                tempRaw= niceData[i][1:]
                tempRaw=list(map(int,tempRaw))
                rawTitle= cTitle
            elif "Bsln" in cTitle:
                tempBsln= niceData[i][1:]
                tempBsln=list(map(int,tempBsln))
                bslnTitle= cTitle
                tempDelta= getDelta(tempRaw,tempBsln,thresholdVar)   #Use getDelta() to create a list of deltas given the raw, bsln and threshold
                cTitle = "Deltas"   #change the title to correctly label the delta list we are printing
                print("Title: {}".format(cTitle), file=text_file)
                #print("Delta: {}".format(tempDelta[0]), file=text_file)
                #print("Status: {}".format(tempDelta[1]), file=text_file)
                print("Max: {}".format(max(tempDelta[2])), file=text_file)
                print("Mean: {}".format(newMean(tempDelta[2])), file=text_file)
                print("------------------------------------------------------------------------------------------------------------------------------------", file=text_file)
                #print("\n", file=text_file)

            i+=1

def removeBlanks(bList): #bList is a 2d list with elements that may be empty strings, we want to remove these empty strings.
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

def getDelta(raw,bsln,threshold): # the difference between list raw and list 2 and returns a 2d list delta[][] where delta[0]-> value difference and delta[1]-> boolean check for threshold pass.
    if not (len(raw)==len(bsln)):
        raise Exception('The two Lists should be the same dimensions')
        return []
    delta=[1]   #placeholders for the delta values
    delta.append([1])
    delta.append([1])
    tempList1,tempList2,tempList3=[],[],[]
    i=0
    while i<len(raw)-1:
        tempList1.append(abs(raw[i]-bsln[i]))   #write the absolute value of the difference between raw and bsln to delta[0]
        tempList2.append(int(tempList1[i]>= threshold))  #write boolean check for delta and threshold to delta[1]
        if (abs(raw[i]-bsln[i])-threshold >=0):
            tempList3.append(abs(raw[i]-bsln[i]))
        i+=1
    delta[0],delta[1],delta[2]=tempList1,tempList2,tempList3
    return delta


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.CSV"),("all files","*.*")))
def main():

    
    #print (root.filename)
    csvList=[]
    csvList=list(csv.reader(open(root.filename)))#This puts csv files into a 2d list

    tHold=2   #this will be specified by the user.
        #print(csvList)
        #print(removeBlanks(csvList))
        #print("Now without extra rows:\n ")
        #print(truncateCsv(removeBlanks(csvList)))
        #print("Now with a transpose:\n ")
        #print(transposeCsv(truncateCsv(removeBlanks(csvList))))
        #print("Now with data:\n ")
    print(printData(transposeCsv(truncateCsv(removeBlanks(csvList))),(tHold)))

main()
