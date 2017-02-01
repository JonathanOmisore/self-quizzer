import random
from nltk import tokenize

def main():
    notes = input("Enter notes file \n ") #User enters file containing notes
    wordsidontwant = ["the", "or", "a", "and", "in", "this", "on", "of","is","to","will","by"] #Don't want any common prepositions or articles
    with open(notes, "r") as file: #While the file is open
        notes = file.read() #Read file
        words = tokenize.sent_tokenize(notes) #Convert paragraphs into an array containing sentences


 
    question = random.choice(words) #Pick a random sentence
    missingword = random.choice(question.split()) #Pick a random word that the user must remember
    if any(x.lower() in missingword.lower() for x in wordsidontwant): #If the missing word happens to be any of the words I don't want
        tryagain = True 
        while tryagain: #While the missingword is a word I don't want
            missingword = random.choice(question.split()) #Pick a different word that isn't in the wordsidontwant list
            if not any(x.lower() in missingword.lower() for x in wordsidontwant): #If the different word isn't in the wordsidontwant list
                tryagain = False #end the loop
            
    
    answer = input("Fill in the blank: \n" + question.replace(missingword,"_") + "\n") 
    if answer not in missingword:
        print("Wrong. Correct answer is " + missingword)
    else:
        print("Correct")
while True:
    main()
            
