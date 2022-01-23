
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
#session = WolframLanguageSession()


#session.evaluate(wlexpr('')) #Can put wolfram expressions into the program to use functionality

#session.evaluate(w1.MinMax()) #Can be used to evaluate any built in functions from wolfram language

#session.terminate()

#Error is generally taken as the magnitude of the distance.
#Word vec model using gensim library in python


from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import re
import io

def line_array(file):
    word_array = []
    for n, line in enumerate(csv.readlines(),1):
        words = re.findall(r"\b\w+\b",line)
        word_array.append([w.lower() for w in words if w.isalpha() == True]) #Words must not have any other characters or numbers - pure lowercase strings
    return word_array

#Generate the lines, then filter based on words only

with open(r'C:\Users\retro\Documents\1Hack reservoir\sustainability texts.txt', 'r') as csv:
    line_array  = line_array(csv)
    

model = Word2Vec(sentences= line_array, vector_size=100, window=5, min_count=1, workers=4) #Tweak workers for the number of processors dedicated to the training
model.save("sustainability.model") #Save to be able to load it up for re-training later

model = Word2Vec.load("sustainability.model")

############### We put in a logical sentence which makes logical sense, and can be used to alter the weights of the words
sentence = 'Sustainability is very important to save the environment'
sent_list = [w.lower() for w in sentence.split(' ') if w.isalpha() == True]  #Can add sentence divided into list of words to add to training data
print(sent_list)

model.train(sent_list, total_examples=1, epochs=1)

#1. Function that generates associated words  form preference words for each category



vector = model.wv['secondary']  # get numpy vector of a word

sims = model.wv.most_similar(positive = 'life', topn=15)  # get other similar words - positive is for closer matches, negative is for words farther away 

print("\n Similarity tuples:")

#Checking the list of similar words
for i in sims: #Note sims stores the words and the vector weighting as a tuple
    print(i)

from gensim.models import KeyedVectors

# Store just the words + their trained embeddings.
word_vectors = model.wv
word_vectors.save("sustainability.wordvectors")

# Load back with memory-mapping = read-only, shared across processes.
wv = KeyedVectors.load("sustainability.wordvectors", mmap='r')


#Example: to print the vector positions of a limuted set of words:
def sample_vectors(line_array):
    for l_num, line in enumerate(line_array, 0): 
        if l_num > 10:
            break
        for word in line: 
            print('\n {}'.format(word))
            print(wv[word])

sample_vectors(line_array)
import itertools

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    return data

fpath = r'C:\Users\retro\Documents\1Hack reservoir\samplevc.vec'

#with open(r'C:\Users\retro\Documents\1Hack reservoir\samplevc.vec', 'r') as sample_vec:
load_vectors = load_vectors(fpath)


model = Word2Vec(sentences= line_array, vector_size=100, window=5, min_count=1, workers=4) #Tweak workers for the number of processors dedicated to the training
model.save("sustainability.model") #Save to be able to load it up for re-training later

sims = model.wv.most_similar(positive = 'life', topn=15)  # get other similar words - positive is for closer matches, negative is for words farther away 
print(sims)


##########################################################################################
class Categories:
    def __init__(self, industries, goal, regions, interests):
        self.industries = industries[0]; self.industries_reject = industries[1] #List of 2, for industries of interest, industries of lower interest
        self.goal = goal #Company ethos/ goals 
        self.regions = regions 
        self.technologies = interests #More general, associated with specific areas of industry (i.e. in vehicles, specifically in EV charging, EV battery coolant etc...)  
        
    @property
    def industry_sims(self):
        pos = [interest for interest in self.industries]
        neg = [n_interest for n_interest in self.industries_reject]
        sims  = model.wv.most_similar(positive = pos, negative = neg,topn = 15) #Check if positive and negative can take in a list rather than just a string 
        return sims[:, 0] #First row extracted - of all similar words        
   
    @property
    def goals_sim(self):
        pos = [goal for goal in self.goals]
        sims  = model.wv.most_similar(positive = pos,topn = 15) #Check if positive and negative can take in a list rather than just a string 
        return sims[:, 0] #First row extracted - of all similar words        
     
    #Need to do for 2 more categories


site = io.open(sitename, 'r', encoding='utf-8', newline='\n', errors='ignore') 


dir = "C:\Users\retro\Documents\1Hack reservoir\Sitewords"
for filename in os.listdir(r"{}".format(dir)):
    if filename.endswith(".txt"):
        with open(r"{}/{}".format(dir,filename), 'r') as sitefile:



        #similarity matchup , generates reservour of vectors for industry



#numpy.unique() Will count the number of occurences of each word


#Generate a set of similar words associated with sustainability - based on preferences (set P)
#Checks the maximum number of matches within the scraped vector of a website to give match 1.
#OR
#Alternatively: performs a similarity test with the vector from set P - by itertools (Set A)
#Complexity order 2?

