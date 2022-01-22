
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

def line_array(file):
    word_array = []
    for n, line in enumerate(csv.readlines(),1):
        words = re.findall(r"\b\w+\b",line)
        word_array.append([w.lower() for w in words if w.isalpha() == True]) #Words must not have any other characters or numbers - pure lowercase strings
    return word_array

#Generate the lines, then filter based on words only

with open(r'C:\Users\retro\Documents\1Hack reservoir\sustainability texts.txt', 'r') as csv:
    line_array  = line_array(csv)
    
    
    #Training with permutations of the sentences themselves? considering proximity, could we increase the length of the sentences
    
#Later - develop something to separate by full stops
    #for n,line in enumerate(csv.readlines(),1):
     #   if n > 15:
      #      break
       # print(n, line)

    


#Checking the sample of data
for text in common_texts:
    print(text)


model = Word2Vec(sentences= line_array, vector_size=100, window=5, min_count=1, workers=4) #Tweak workers for the number of processors dedicated to the training
model.save("sustainability.model") #Save to be able to load it up for re-training later

model = Word2Vec.load("sustainability.model")


############### We put in a logical sentence which makes logical sense, and can be used to alter the weights of the words
sentence = 'Sustainability is very important to save the environment'

model.train([["hello", "world", "computer", "desktop"]], total_examples=1, epochs=1)
#(0, 2)
vector = model.wv['secondary']  # get numpy vector of a word

sims = model.wv.most_similar(positive = 'human', negative = 'trees', topn=10)  # get other similar words - positive is for closer matches, negative is for words farther away 

print("\n Similarity tuples:")

for i in sims: #Note sims stores the words and the vector weighting as a tuple
    print(i)

from gensim.models import KeyedVectors

# Store just the words + their trained embeddings.
word_vectors = model.wv
word_vectors.save("sustainability.wordvectors")

# Load back with memory-mapping = read-only, shared across processes.
wv = KeyedVectors.load("sustainability.wordvectors", mmap='r')



vector = wv['computer']  # Get numpy vector of a word - vector related to all other words

'''Tasks to complete now:
Write the program to reaf file objects - then generate similar results

Should not require training - rather, will be trained with a pre-loaded array of values for vector corpus

Generate a greaphical representation in 2D of the proximity of the words
'''



