# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: To read in files and then process them
#
# Author:      David
#
# Created:     09/03/2014
# Copyright:   (c) David 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# This program will stem the files to make it easier to classify them.'

import re, random, math, collections, itertools, string,  os,  sys,  codecs
from stemming.porter2 import stem


#    import re,  itertools,  string,  nltk,  random

extension = ""
#Function that loads the text files containing the news stories both suitable and unsuitable , modifies the content and also loads the unsuitable word list.
def setUp(unsuitStories, suitStories, sentenceTrain, sentimentTest): #rename this shit right fucking here




    txt = codecs.open(extension + 'stop_words.txt',  'r',  'utf-8')
    stopWords = re.findall(r"[a-z\-]+", txt.read())
    totalStopWords = len(stopWords)

    txt =codecs.open(extension + 'unsuitable_words.txt', 'r',  'utf-8')
    unsuitableWordList = re.findall(r"[a-z\-]+", txt.read())

    txt = codecs.open(extension + 'unsuitableStory.txt', 'r',  'utf-8') 
    unsuitableStories = re.split(r'\n', txt.read()) 

    txt = codecs.open(extension + 'suitablestorys.txt', 'r',  'utf-8') 
    suitableStories = re.split(r'\n', txt.read()) 

    txt = codecs.open(extension + 'female_names.txt', 'r',  'utf-8') 
    female_names = re.split(r'\n', txt.read()) 

    stopWordRecompiling = re.compile('\\b(%s)\\W'%('|'.join(map(re.escape,stopWords))),re.I)
    namesRecompiling = re.compile('\\b(%s)\\W'%('|'.join(map(re.escape,female_names))),re.I)

    unsuitableStories = ([stopWordRecompiling.sub('',p) for p in unsuitableStories])
    unsuitableStories = [list.lower() for list in unsuitableStories]
    unsuitableStories = ([namesRecompiling.sub(' ',p) for p in unsuitableStories])

    suitableStories = ([stopWordRecompiling.sub('',p) for p in suitableStories])
    suitableStories = [list.lower() for list in suitableStories]
    suitableStories = ([namesRecompiling.sub(' ',p) for p in suitableStories])

    #Opens up list of all stories, unsuitable / suitable, the stop words, female names etc. 
    #Removes stop words from the stories.

    


    combinedList = ""
    fullWordSet= ""

    chars = [',', '!', '.', ';', '?', '\'',  '\"',  ':',  '-',  '?',  '\r',  '\)',  '\(',  '\[',  '\]', '\’' ,  '#', '”', '*']
    exclude = set(string.punctuation)

    i= 0
    while i < len(unsuitableStories):
        unsuitableStories[i] = re.sub('[%s]' % ' '.join(chars), ' ', unsuitableStories[i])
        unsuitableStories[i] = unsuitableStories[i].split(' ')     
        unsuitableStories[i] = ' '.join(ch for ch in unsuitableStories[i]  if ch not in exclude)
        unsuitableStories[i]= unsuitableStories[i].split(' ')   
        unsuitableStories[i] = [x for x in unsuitableStories[i] if not any(c.isdigit() for c in x)]
        decodingWords= ""
        decodingWords = ' '.join(unsuitableStories[i] )
        decodingWords = decodingWords.encode('utf-8')
        decodingWords =  re.sub(r'[^\x00-\x7f]',r'',decodingWords)
        decodingWords = decodingWords.replace("-", " ")
        unsuitableStories[i] = decodingWords.split()
       
        i = i + 1
        
    
    i = 0
    while i < len(suitableStories):
        suitableStories[i] = re.sub('[%s]' % ' '.join(chars), ' ', suitableStories[i])
        suitableStories[i] = suitableStories[i].split(' ')     
        suitableStories[i] = ' '.join(ch for ch in suitableStories[i]  if ch not in exclude)
        suitableStories[i]= suitableStories[i].split(' ')   
        suitableStories[i] = [x for x in suitableStories[i] if not any(c.isdigit() for c in x)]
        decodingWords= ""
        decodingWords = ' '.join(suitableStories[i] )
        decodingWords = decodingWords.encode('utf-8')
        decodingWords =  re.sub(r'[^\x00-\x7f]',r'',decodingWords)
        decodingWords = decodingWords.replace("-", " ")
        suitableStories[i] = decodingWords.split()
        i = i + 1
    
 
    #Runs through both sets of suitable/unsuitable stories and completely removes any punctuation , numbers, anything non alphabetical.
    #Maybe make this a function that repeats itself - also find a way to make this shorter and not overtly complex.
 
    
    #unsuitableStoriesCollapsed =  [item for sublist in unsuitableStories for item in sublist] - May use again 
    #suitableStoriesCollapsed =  [item for sublist in suitableStories for item in sublist] - May use again
    
    
    
    combinedList = unsuitableStories + suitableStories
    combinedList = [item for sublist in combinedList for item in sublist]
    for word in combinedList:
        if word not in fullWordSet:
            fullWordSet = fullWordSet + " " + word
            
    fullWordSet = fullWordSet.split()        
   

    #Gets all the stories , combines them and then removes all word duplicates.
    
    
    totalWords = len(fullWordSet)
    
    
    return test_Bayes_SetUP(totalWords,  fullWordSet,  suitableStories, unsuitableStories,  exclude,  combinedList,  unsuitableWordList)





    

#TRAIN BAYES DOES NOT WORK BECAUSE IT DOESN NOT RECIEVE THE CORRECT VARIABLES SO FAR.


def test_Bayes_SetUP(totalWords,  fullWordSet,  suitableStories, unsuitableStories,  exclude,  combinedList,  unsuitableWordList):



    storiesTotal = len(unsuitableStories) + len(suitableStories) #Calculates total stories
    testSet = ["null"] * storiesTotal # sets up a list to contain the test set - There must be a better way of doing this.
    testSetClassification = ["null"] * storiesTotal#sets up a list to contain test set story classification


    storiesCounter = 0 #Used for referencing the story to copy to the test set
    testSetCounter = 0 # Used for referencing the story that was copied to the test set and it's suitability.

    for list in unsuitableStories:

        if random.randint(1,10)<= 2:
            testSet[testSetCounter] = unsuitableStories[storiesCounter]
            unsuitableStories.pop(storiesCounter)    
                      
            testSetClassification[testSetCounter] = "Unsuitable"
            testSetCounter = testSetCounter + 1    
        else:
            storiesCounter = storiesCounter + 1

    #Above loop runs through all the stories that are unsuitable. It uses the random function to determine whether or not the story should be copied to the test set.
    #If they are copied then it removes that story from the original set , determines it's corresponding classification and increases the counter to reference the test set.
    # If it's not copied then the counter to reference the list is increased (Not increased otherwise because stories are Popped and thus the list becomes list - 1

    storiesCounter = 0  
    for list in suitableStories:
        if random.randint(1,10)<=2:
            testSet[testSetCounter] = suitableStories[storiesCounter]
            
            suitableStories.pop(storiesCounter)  
            testSetClassification[testSetCounter] = "Suitable"
            testSetCounter = testSetCounter + 1  
        else:
            storiesCounter = storiesCounter + 1

    #The counter used to reference the stories is reset and this loop works the same as the previous but for stories in the suitable test set.

    # Roughly 20% of stories should become part of the test set.



    totalSuitableStories = len(suitableStories)
    totalUnsuitableStories = len(unsuitableStories)
    totalStories = totalSuitableStories + totalUnsuitableStories
    #Calcs total stories left in the training data.

    testSet = [ x for x in testSet if "null" not in x ]
   
    #Any blank instances in the test set are removed.


    return training_Setup(totalWords,  fullWordSet,  suitableStories, unsuitableStories,  testSet, testSetClassification, exclude,  unsuitableWordList, totalSuitableStories, totalUnsuitableStories,  totalStories)


def training_Setup(totalWords,  fullWordSet,  suitableStories, unsuitableStories,  testSet, testSetClassification, exclude,  unsuitableWordList, totalSuitableStories, totalUnsuitableStories,  totalStories):

    wordoccurenceUnsuitableStories = [0] * (totalWords)
    wordoccurenceSuitableStories = [0] * (totalWords)
    totalWordOccurences = [0] * (totalWords)
    #Above variables will store the number of stories (not the total number of occurences) words appear in.


    counter = 0 #Sets up a counter for keeping track of list posistions.

    for word in fullWordSet: #Runs through every word in the full list of words (nb unique list - no duplicates)

        # Resets to 0 the list index
        
        listIndex = 0 # Resets to 0 the list index
        for list in unsuitableStories: 
            if word in unsuitableStories[listIndex]:
                wordoccurenceUnsuitableStories[counter] = wordoccurenceUnsuitableStories[counter] + 1
            listIndex = listIndex + 1
       
       #Runs through all the unsuitable Stories. If a word is found in one of the lists then the corresponding list posistion counting word occurences in unsuitable stories is updated.
       #The loop will only check for the word in each story once, and not count the number of appearances
       #The list index will update at the end of each cycle to increase by 1 the number of the list being checked.
       
       
        listIndex = 0 # Resets to 0 the list index
        for list in suitableStories:
            if word in suitableStories[listIndex]:
                wordoccurenceSuitableStories[counter] = wordoccurenceSuitableStories[counter] + 1
            listIndex = listIndex + 1    


        totalWordOccurences [counter] = wordoccurenceSuitableStories[counter] + wordoccurenceUnsuitableStories[counter]
        
        counter = counter + 1
        #Tallys the total occurences of each word in a corresponding list posistion (  x['5'] = y['5'] + z['5'] )   

    
    
    
    
    
    return Classifier(totalWords,  fullWordSet,  totalWordOccurences,  wordoccurenceSuitableStories, wordoccurenceUnsuitableStories,  testSet, testSetClassification, exclude,  unsuitableWordList, totalSuitableStories, totalUnsuitableStories,  totalStories)





def Classifier(totalWords,  fullWordSet,  totalWordOccurences,  wordoccurenceSuitableStories, wordoccurenceUnsuitableStories,  testSet, testSetClassification, exclude,  unsuitableWordList, totalSuitableStories, totalUnsuitableStories,  totalStories):


    correctlyClassified = 0
    incorrectlyClassified = 0
    classUnSuit = 0
    x = 0 
    lenTestSet = len(testSet)
    print (lenTestSet)
    
   # p(B|A) = p(B|A) * p(A)
      #                  /p(B)
    
    
    try:
            pA = float(totalUnsuitableStories) / float(totalStories)
    except ZeroDivisionError:
            pA = 0

    try:
            pAsuit = float(totalSuitableStories)/float(totalStories)
    except ZeroDivisionError:
            pAsuit = 0
            

    while x < lenTestSet:

        originalClassification = testSetClassification[x]
        
        storyClassify = testSet[x]
        
        pBA = float(0)
        pBA = pA
        i = 0
        pB=float(0)    
        for word in fullWordSet:
            if word in  storyClassify:
                
                if wordoccurenceUnsuitableStories [i] == 0:
                    pBA = pBA
                    
                else:   
                    pBA = pBA * (float(wordoccurenceUnsuitableStories[i]) / float(totalUnsuitableStories))
                    if pB == 0: 
                        pB = (float(totalWordOccurences[i]) / float(totalStories))
                    else:
                        pB = pB * (float(totalWordOccurences[i]) / float(totalStories))
            i = i + 1
        #Basically checks each word, if it's there it calculates probability of that word * probability of other words that are in the story that needs classifying.
        #Also updates pB as neccessary.

        
        finalprobunsuit = float(pBA)/float(pB)
        
        
        pB=(0)    
        pBA = pAsuit
        i = 0
        for word in fullWordSet:
            if word in  storyClassify:
                if wordoccurenceSuitableStories[i] == 0:
                    pBA = pBA
                else:
                    pBA = pBA * (float(wordoccurenceSuitableStories[i]) / float(totalUnsuitableStories))
                    if pB == 0: 
                        pB = (float(totalWordOccurences[i]) / float(totalStories))
                    else:
                        pB = pB * (float(totalWordOccurences[i]) / float(totalStories))
            i = i + 1

              #Basically checks each word, if it's there it calculates probability of that word * probability of other words that are in the story that needs classifying.
        #Also updates pB as neccessary.
        
        finalprobsuit = float(pBA) / float(pB)
        
        
        

        if finalprobsuit > finalprobunsuit:
            suitability = "True"
        else:
            suitability = "False"
        #####
       
        print ('It was classified as:')
        print (suitability)
        print ('It should have been:')
        print originalClassification
        
        if suitability == "False":

            if testSetClassification[x] == "Unsuitable":
                correctlyClassified = correctlyClassified + 1
                x = x + 1         
            else:
                incorrectlyClassified = incorrectlyClassified + 1
                x = x + 1
        elif suitability == "True":
            if testSetClassification[x] == "Suitable":
                correctlyClassified = correctlyClassified + 1
                x = x + 1
            else:
                incorrectlyClassified = incorrectlyClassified + 1
                x = x + 1
        else:
            x = x + 1


    #Above seems a bit pointless try and uncongest it ,also remove incorrectly classified.




    correctClassificationPercentage = float(correctlyClassified) / float(lenTestSet)
    print ('stories correctly classified percentage')
    print (correctClassificationPercentage)     


    print 'The End'



print "Start of the program"

sentencesTrain=[]
sentencesTest=[]


setUp(extension + 'unsuitableStory.txt', extension + 'suitablestorys.txt', sentencesTrain, sentencesTest)



