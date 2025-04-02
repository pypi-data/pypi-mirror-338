import os

IR = {
    "inverted_index":'''#inverted index
data = {}
for i in range(3):
    with open('file' + str(i+1) + '.txt', 'r') as f:
        f = f.read().lower().split()
        for i2 in f:
            if i2 not in data:
                data[i2] = []
        for i1 in f:
            data[i1].append('file'+str(i+1)+'.txt')
data = dict(sorted(data.items()))
for key in data:
    print(key, data[key])''',



    "lev":'''#levenshtein
str1 = 'kitten'
str2 = 'setting'

m = len(str1)
n = len(str2)

dp = [[0 for j in range(n+1)]for i in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(
                dp[i-1][j],
                dp[i-1][j-1],
                dp[i][j-1]
            )

for row in dp:
    print(row)
print()
print(dp[m][n])''',


    "ngram":'''#ngram
word = 'hello world my name is hello'.split()
n=3
result = []
#for letters
for i in word:
    for j in range(len(i)-n+1):
        result.append(i[j:j+n])
print(result)

#for words
res = []
for i in range(len(word)-n+1):
    res.append(word[i:i+n])
print(res)''',


    "page_rank":'''#page rank
import numpy as np

M = np.matrix([[0, 1, 1],
               [1/2, 0, 0],
               [1/2, 0, 0]])

dp = 1/3
E = np.zeros((3, 3))
E[:] = dp
print("E:")
print(E)

beta = 0.5
A = beta * M + ((1-beta) * E)
print("A:")
print(A)

r = np.matrix([dp, dp, dp])
r = np.transpose(r)
prev_r = r
iteration = 0
while True:
    r = A * r
    print("Iteration", iteration,":")
    print(r)
    if np.allclose(prev_r, r, atol=1e-6):
        break
    prev_r = r
    iteration += 1

print('final r:')
print(r)
print('Sum of r:', sum(r))''',


    "stopword_removal":'''#stopword removal
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
sentence = 'Mithibai is the best College'.lower().split()
result = []
stops = set(stopwords.words('english'))
for i in sentence:
    if i not in stops:
        result.append(i)
print(result)''',


    "porter_stemmer":'''#porter stemmer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
sentence = 'Mithibai is the best College'.lower().split()
for i in sentence:
    print(stemmer.stem(i))''',


    "soundex":'''#soundex
dic = {
    0:['a','e','i','o','u','h','w','y'],
    1:['b','f','p','v'],
    2:['c','g','j','k','q','s','x','z'],
    3:['d','t'],
    4:['l'],
    5:['n','m'],
    6:['r']
}
word = 'helloworldorg'
final = word[0]
for i in word[1:]:
    for j in dic:
        if i in dic[j]:
            final = final + str(j)
            continue
print('first result is ', final)

i = 0
while i < len(final)-1:
    if final[i] == final[i+1]:
        final = final[:i] + final[i+1:]
        i-=1
    i+=1
print('after removing consecutive ', final)

final = final.replace('0','')
print('after removing 0s:', final)

final = final[:4]
print('after slicing', final)

if len(final) <= 4:
    for i in range(4-len(final)):
        final += str(0)
print('final string', final)''',



    "web_crawler":'''#web-crawler
import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth = 0, visited = set()):
    if url in visited : return 
    print("Depth[",depth,"] Crawling:",url)
    visited.add(url)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content , "html.parser")
        for link in soup.find_all("a", href= True):
            new_url = urljoin(url, link["href"])
            if not new_url.startswith(url): 
                return 
            crawl(new_url, depth+1, visited)
    except Exception as e: 
        print("Error:", e)

root = "https://mithibai.ac.in"
crawl(root)''',



    "collab_filtering":'''#knn, collaborative filtering
from sklearn.neighbors import NearestNeighbors
import numpy as np
num_users = 15
num_movies = 5

# Generate random ratings from 0 to 5, with some NaN values
ratings = np.random.choice([0, 1, 2, 3, 4, 5, np.nan], size=(num_users, num_movies), p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.1])
# converting all nan values with -1 as the below algo does not accept nan value
def nan_conversion(ratings):
    for i in range(len(ratings)):
        for j in range(len(ratings[0])):
            if np.isnan(ratings[i][j]):
                ratings[i][j] = -1
    return ratings
ratings = nan_conversion(ratings)
nbrs = NearestNeighbors(n_neighbors=5, metric = 'cosine').fit(ratings)
distances, indices = nbrs.kneighbors(ratings)
# finding -1 row and cols
neg_one_row_col = []
for i in range(len(ratings)):
    for j in range(len(ratings[0])):
        if ratings[i][j] == -1:
            neg_one_row_col.append([i,j])
print('these are null values [row,col]:', neg_one_row_col)
print('this is indices: ',indices)
print('this is distance: ',distances)
for i in neg_one_row_col:
    row = i[0]
    col = i[1]
    print('these are row and col: ', row, col)
    ind_row = indices[row]
    ind_row = ind_row[1:]
    dis_row = distances[row]
    dis_row = dis_row[1:]
    similarity = 1 - dis_row
    print('this is similarity: ', similarity)
    value = []
    for j in ind_row:
        value.append(ratings[j][col])
    print('this is values: ', value)
    average_value = sum(similarity * value) / sum(similarity)
    ratings[row][col] = average_value
    print("Ratings after replacement:")
    print(ratings)
    print('this is average value: ', average_value)
    print('this is row and col: ', row, col)''',



    "stopword_porter":'''#stopword and porterStemmer (combination)
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')
sentence = 'Mithibai is the best College'.lower().split()
new = []
stops = set(stopwords.words('english'))
for i in sentence:
    if i not in stops:
        new.append(i)
print(new)
stemmer = PorterStemmer()
for i in new:
    print(stemmer.stem(i))''',



    "stopword_inverted":'''#stopword remover + inverted index (combination)
import nltk
from nltk.corpus import stopwords

def content(filename):
    stops = set(stopwords.words('english'))
    result = []
    main_res = []
    with open(filename,"r") as f:
        r = f.read().lower().split()
        for i in r:
            result.append(i)
    for i in result:
        if i not in stops:
            main_res.append(i)
    with open(filename,"w") as f:
        for i in main_res:
            f.write(i+' ') 
content('file1.txt')
content('file2.txt')
data = {}
for i in range(2):
    with open('file' + str(i+1) + '.txt', 'r') as f:
        f = f.read().lower().split()
        for i2 in f:
            if i2 not in data:
                data[i2] = []
        for i1 in f:
            data[i1].append('file'+str(i+1)+'.txt')
data = dict(sorted(data.items()))
for key in data:
    print(key, data[key])''',



    "porter_inverted":'''#porter stemmer + inverted index
from nltk.stem import PorterStemmer

def content(filename):
    stemmer = PorterStemmer()
    result =[]
    result1 = []
    with open(filename , 'r') as f:
        result = f.read().lower().split()
    for i in result:
        result1.append(stemmer.stem(i))
    with open (filename , 'w') as f:
        for i1 in result1:
            f.write(i1 + ' ')
content("file1.txt")
content("file2.txt")

    
data = {}
for i in range(2):
    with open('file' + str(i+1) + '.txt', 'r') as f:
        f = f.read().lower().split()
        for i2 in f:
            if i2 not in data:
                data[i2] = []
        for i1 in f:
            data[i1].append('file'+str(i+1)+'.txt')
data = dict(sorted(data.items()))
for key in data:
    print(key, data[key])''',




    "incidence_matrix":'''#incidence matrix
file1 = []
file2 = []
file3 = []
files = [file1, file2, file3]

sets = set()
for i in range(len(files)):
    with open('file' + str(i+1) + '.txt', 'r') as f:
        f = f.read().split()
        for i1 in f:
            sets.add(i1)

#converting for iterating
sets  = list(sets)
iter = 1
for i in files:
    with open('file' + str(iter) + '.txt', 'r') as f:
        f = f.read().split()
        for i1 in sets:
            if i1 in f:i.append(1)
            else:i.append(0)
    iter +=1 
import numpy as np
files = np.transpose(files)
print(files)

query = 'Vaibhav & name | hello'.split()
bit = files[sets.index(query[0])]
for i in range(2,len(query),2):
    index = sets.index(query[i])
    if query[i-1] == '&':
        bit &= files[index]
    else:
        bit |= files[index]
print(bit)''',


    "porter_ngram":'''#porterStemmer + ngram
from nltk.stem import PorterStemmer

sentence = 'Mithibai is the best College'.lower().split()
stemmer = PorterStemmer()
new = []
for i in sentence:
    new.append(stemmer.stem(i))
n=3
result = []
#for letters
for i in new:
    for j in range(len(i)-n+1):
        result.append(i[j:j+n])
print(result)

#for words
res = []
for i in range(len(new)-n+1):
    res.append(new[i:i+n])
print(res)''',





    "stopword_ngram":'''#stopword + ngram
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
sentence = 'Mithibai is the best College'.lower().split()
new = []
stops = set(stopwords.words('english'))
for i in sentence:
    if i not in stops:
        new.append(i)
n=3
result = []
#for letters
for i in new:
    for j in range(len(i)-n+1):
        result.append(i[j:j+n])
print(result)

#for words
res = []
for i in range(len(new)-n+1):
    res.append(new[i:i+n])
print(res)'''
}


def run():
    passkey = input("")
    if passkey != "keyboard":
        exit()
    os.system('cls')
    for i,j in enumerate(IR.keys()):
        print(i+1,j)
    print()
    prac = input("")
    practical = ''''''
    for i in range(50):
        practical+="\n"
    try:
        practical += IR[list(IR.keys())[int(prac)-1]] 

        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        if not os.path.exists(desktop_path):
            desktop_path = 'C:\\'
            
        ir_folder = os.path.join(desktop_path, 'IR')
        if not os.path.exists(ir_folder):
            os.makedirs(ir_folder)
            
        practical_file = os.path.join(ir_folder, 'practical.py')
        with open(practical_file, 'w') as f:
            f.write(practical)
    except:
        exit()