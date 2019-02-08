# Python Script for data analysis Rev.2
# by Sebastian Betancur, under the supervision of Lucas Mallory
#Worked on by Jose Level as of 2/7/2019

# Keep in mind, this program HAS HARDCODED components for the data results provided by the Probes
# This program supports undefinite number of KeyFunctions, sensors, and readings.


#For convenivece and labeling:
import os
import datetime

now = datetime.datetime.now()                           #Used to display time.
#input()

Foldername="/LucasScript"
                    #C:\Users\240027853\Documents\LucasScript                                    #NOTE:use backslash '/' or double forward '\\' when typing paths
Dir = "C:/Users/240027853/Documents/"+ str(Foldername)  #Always specify where your TestFiles are by HARDCODING its path to the Dir variable
DirFiles = os.listdir(Dir)                              #Dir is your directory path, lists all elements (files) in the folder
NumFiles = len(DirFiles)                                #Determines number of files in the folder
DirNames = list(DirFiles)

for i in range(0,NumFiles):

    Split = DirNames[i].split(".")
    DirNames[i]= Split[0]

for Filenum in range(0,NumFiles):                       #For each file in the folder...

    DataPath = Dir + "/" + DirFiles[Filenum]            #Check file number(0,1,2...)
    Thumbnail= "Summary"
                                                        #Open Data
    #try:
    DataFile = open(DataPath)                           #Open the selected file
    #except:
    #    print("File number " + Filenum + "could not be read!\n")
    #    continue

    DataText = DataFile.read()                          #Read all its content
    lines= DataText.splitlines()                        #split text into single lines
    len_lines=len(lines)                                #stablish number of lines to check

    print("Num of keys in file: ", (len_lines-1)/5)

    if(DirFiles[Filenum][(len(DirFiles[Filenum])-3):(len(DirFiles[Filenum]))]!="csv"):                      #This section determines if a file is a csv or not.
        if(DirNames[Filenum][(len(DirNames[Filenum])-(len(Thumbnail))):len(DirNames[Filenum])]!=Thumbnail):
            print("WARN: Non-csv file: ( "+str(DirFiles[Filenum])+ " ) was skipped.")
        continue
    else:

        #Begin report:
        DateTime=now.strftime("%Y-%m-%d %H:%M")                                                             #Store date & time of file creation
        ProcessedData=open(Dir +"/"+ str(DirNames[Filenum])+"_"+str(Thumbnail)+".txt","w")                  #Creates destination file
        ProcessedData.write("File " + str(Filenum) +"\n")                                                   #Title
        ProcessedData.write("Date & Time:  " + DateTime)                                                    #Date & time


        #Begin Checking:
        Collumns= lines[0].split(",")                                                                   #Takes every Collumn name for Key Titles
        for offset in range(0,len(Collumns)-len(Collumns)%5,5):
                                                                                                        #For each set of Collumns aka number of different keys used
                                                                                                        #THIS REQUIRES FORMATING OF THE DATA:
                                                                                                        #the program will check every first and fourth collumn to determine
                                                                                                        #if there is data available. After each key (set of 4 collumns)
                                                                                                        #is tested, the read values go onto the next key (next set
                                                                                                        #of collums)
            ProcessedData.write("\n\nResults from  " +str(Collumns[offset+1])+ ":\n\n")
            ProcessedData.write("\tTest #\tAverage\tStdDiv\tVariance\tMin\tMax\tSamples\n")

            Testnum=0 #Keeps track of the number of tests per Key
            state=0   #Keeps track of operations to determine next protocol
            datacheck=0 #Dectects if there was no usable data in the test


            for c in range(1,len_lines):                                                                #test every line
                KeyRead=[int(s) for s in lines[c].split(",") if s.isdigit()]                            #take numbers in the text-line and splits it by "," as in CSV files
                try:
                    if ((KeyRead[offset]==1) and (state==1)):                                           #If it is still sampling data... sample
                        Readings[Testnum]+=(KeyRead[offset+3],)
                        #print(KeyRead)
                except:
                    print("I think your file is too long.")
                    exit()

                if ((KeyRead[offset]==1) and (state==0)):                                               #If data is detected... initialize sampling
                                                                                                        #New entry operations
                                                                                                        #Reset measurements,
                    Readings={}
                    SenseMax={}
                    SenseMin={}
                    Average={}
                    StdDiv={}
                    Variance={}
                    state=1
                    datacheck=1

                    #Iterate & start new set:
                    Testnum+=1
                    Readings[Testnum]= (KeyRead[offset+3],)
                    SenseMax[Testnum]= 0
                    SenseMin[Testnum]= 0
                    Average[Testnum]= 0
                    StdDiv[Testnum]= 0
                    Variance[Testnum]=0

                if ((KeyRead[offset]==0)and(state==1)):                                             #If there are no more 1s... Save your data in a file.
                    state=0
                    SenseMax[Testnum]=max(Readings[Testnum])
                    SenseMin[Testnum]=min(Readings[Testnum])
                    Average[Testnum]=sum(Readings[Testnum])/float(len(Readings[Testnum]))
                    Sum=0
                    for s in range(0,len(Readings[Testnum])):
                        Sum+=((Readings[Testnum][s]) - Average[Testnum])**2
                    if((len(Readings[Testnum])-1 )==0):
                        print("WARN: File: " + str(Filenum) +" Key: "+ str(Collumns[offset])+" Test: " + str(Testnum) + " there is only 1 sample\n")
                        Variance[Testnum]=0
                        StdDiv[Testnum]=0
                    else:
                         Variance[Testnum] =Sum/float((len(Readings[Testnum])-1))
                         StdDiv[Testnum]=Variance[Testnum]**(1/2.0)
                    #Save Data:
                    ProcessedData.write("\n\t" + str(Testnum)+ "\t" + str(round(Average[Testnum],1)) + "\t" + str(round(StdDiv[Testnum],2))+ "\t" + str(round(Variance[Testnum],2))+ "\t\t"+ str(SenseMin[Testnum]) + "\t" + str(SenseMax[Testnum]) +"\t" +str(Readings[Testnum]))

                if (datacheck==0 and c==(len_lines-1)):
                    ProcessedData.write("\n\tNo data recorded")

        ProcessedData.write("\n\n\tEnd of all gathered results.\n\n")
        ProcessedData.close()
