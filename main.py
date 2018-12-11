#imports
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as z # instead of wordnet everytime i just have to type z much easier 
#end of imports
#start of code
print("Welcome to the synonym finder made by Charlie Wilson :P")
print("Note, if you get an error saying permission denied then if you are running linux then just use sudo or if you are running windows then run as admin.")
print("The program could take a while to do the file but it works, just let it do its thing")
print("Patience is a virtue")
print("Have fun :) ")
print("The program starts here")
#multiple different prints cos i cant find the backslash on my keyboard nor can i be bothered keeping it in my clipboard otherwise i could reduce LOC with the backslash n but meh, first world problems
topara = input("where is the directory stored?? ") # looks for the file to read and paraphrase
file = open(topara, 'r') # reads it
print("File found") #assures the user that the program not in fact broken
print("Getting synonyms now......") # reassurance 
r = file.read() # reads the file
def tag(sentence): #function
    words = word_tokenize(sentence) # gets the type of word that the word is 
    words = pos_tag(words) # contextual thingies
    return words # return the type of word is 
def parapos(tag):
    return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ') # stack overflow thank you 
def pos(tag):
    if tag.startswith('NN'): # the tag of the type of word
        return z.NOUN # is a noun
    if tag.startswith('V'): # another type of word this time a verb
        return z.VERB  # is a verb 
def synonyms(word, tag):
    lemma_lists = [ss.lemmas() for ss in z.synsets(word, pos(tag))] # uses the functions pos and tag which have been created above
    lemmas = [lemma.name() for lemma in sum(lemma_lists, [])] # this loops through and outputs the synonyms
    return set(lemmas) # this shows the user the synonyms in the format [original word ["synonym"] ["next synonym"] yadayadayada 
def synonymIfExists(sentence): # this is the main bit of the program !!!!!!!!!!!!
 for (word, t) in tag(sentence): # this loops through every word in the thing given 
   if parapos(t): # basic if statement
    syns = synonyms(word, t) # this is the synonym var
    if syns:
     if len(syns) > 1: # if the value of syn is greater than one meaning that there is in fact a synonym it will yield a result (next line)
      yield [word, list(syns)] # some yield stuff 
      continue # NEXT !!
   yield [word, []] # some formatting stuff 

def paraphrase(sentence):
    print([x for x in synonymIfExists(sentence)])

paraphrase(r)
print("Thank you for using")
