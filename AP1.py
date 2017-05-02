import string
import re

nameid=dict()
f = open("C:\Users\prem\Desktop\cds dp assignment\meta_data_1200.csv")
a=f.read().replace(',','\r')
asp=a.split('\r')

for i, c in enumerate(asp):
	#print i, c
	if i%2==0 and i>1:
		nameid[c]=''
	elif i%2==1 and i>1:
		nameid[asp[i-1]]=c
	#print nameid

#####																			nameid coverted to dictionary format
	
idsum=dict()
f=open("C:\Users\prem\Desktop\cds dp assignment\plot_summaries_1200.txt")
a=f.read().replace('[[',' ')
asp=re.split(r'[\n\t]', a)

for i, c in enumerate(asp):
	#print i, c
	if i%2==0:
		idsum[c]=''
	elif i%2==1:
		idsum[asp[i-1]]=c
#print idsum['10004664']
'''
fout=open("C:\Users\prem\Desktop\cds dp assignment\idsum.txt",'w')
fout.write(str(idsum))
fout.close()
'''
#print idsum.keys()

################################################################SAMPLING###########################################################
iddsum=dict()

for key in ['4592959', '21411112', '168602','14034821', '19793556', '10536562', '33370239','32995532', '30698901', '35320691', '20956043', '35033607', '36309911']:
	iddsum[key]=idsum[key]
	
#####																			iddsum coverted to dictionary format

def convert2tf(doc):
	#doc = ''.join([c for c in doc if c not in ('!', '?','.',',','\n','\t','//','{{','[[','/')])
	hist1=dict()
	#vec1=clean(doc)
	vec1=doc.replace('[[',' ').replace('{{',' ').replace('"\"',' ').replace('"\d+"',' ').replace('}}',' ').replace('\n',' ').replace('\t',' ').replace(':',' ').replace('_',' ')#.split(' ')
	vec1=re.findall(r'\w+',vec1)
	
	#print vec1

	for word in vec1:
		word=word.strip(string.punctuation+string.whitespace)
		word=word.lower()
		hist1[word]=hist1.get(word,0)+1
		hist1.pop('', None)
	return hist1																#unsorted  vector for one doc

TF=dict()

iddsum.pop('', None)
for id in iddsum:					#iterating for each document
	TF[id]=convert2tf(iddsum[id])

fout=open("C:\Users\prem\Desktop\cds dp assignment\TF1.txt",'w')
fout.write(str(TF))
fout.close	
#print TF['33370239']		
#print TF['33370239'].keys()													#unsorted vector ready for all documents							

#																				Finding Master dictionary for the documents
MD=dict()	#master dictionary
def convert2md():
	doc=open("C:\Users\prem\Desktop\cds dp assignment\plot_summaries_1200.txt")
	doc=doc.read()
	
	#doc = ''.join([c for c in doc if c not in ('!', '-','?','.',',','\n','\t','//','{{','[[','/')])
	hist1=dict()
	#vec1=clean(doc)
	
	vec1=doc.replace('[[',' ').replace('{{',' ').replace('"\"',' ').replace('"\d+"',' ').replace('}}',' ').replace('\n',' ').replace('\t',' ').replace(':',' ').replace('_',' ')#.split(' ')
	vec1=re.findall(r'\w+',vec1)
	#print vec1

	for word in vec1:
		word=word.strip(string.punctuation+string.whitespace)
		word=word.lower()
		if word not in iddsum.keys():								#done to remove numbers from MD
			hist1[word]=hist1.get(word,0)+1
		
	return hist1
	
MD=convert2md()
MD.pop('', None)

#print MD.keys()
#print TF['29126410'].keys()

fout=open("C:\Users\prem\Desktop\cds dp assignment\MD.txt",'w')
fout.write(str(MD))
fout.close()
#print MD

term_freq=dict()
def termfr(doc):
	term_freqi=dict()
	for word in MD:
		#print word
		if word in TF[doc]:
			#print TF[doc][word]
			term_freqi[word]=TF[doc][word]
		else:
			term_freqi[word]=0
		#	
	return term_freqi

for doc1 in iddsum:
	term_freq[doc1]=termfr(doc1)
	#print term_freq

doc1='33370239'
#print TF[doc1].keys()
#print TF[doc1]['and']

term_freq[doc1]=termfr(doc1)	
																											#term_freq done!!!!!!!!!!!!!!!!!
fout=open("C:\Users\prem\Desktop\cds dp assignment\TF.txt",'w')
fout.write(str(term_freq))
fout.close()
'''
WR=dict()
#calculating Word repetition
for word in MD.keys():
	WR[word]=0
	for id in iddsum:
		if word in TF[id].keys():
			WR[word]+=1
		else:
			WR[word]=WR[word]	
																				#Word repetition in all docs done !
fout=open("C:\Users\prem\Desktop\cds dp assignment\WR.txt",'w')
fout.write(str(WR))
fout.close()
'''
def readf(f):
	s = open(f, 'r').read()
	a=dict()
	a=eval(s)
	return a
	
WR=readf("C:\Users\prem\Desktop\cds dp assignment\WR.txt") 
print "done 1"
################################################temporary
total_docs=len(iddsum)

# Calculating IDF
from math import log10

IDF=dict()

def conv2IDF(doc):
	idfvec=dict()
	for word in MD:
		#print word
		if word in TF[doc]:
			idfvec[word]=log10(total_docs/1+WR[word])
		else:
			idfvec[word]=0
	return idfvec	
	
for id in iddsum:
	IDF[id]=conv2IDF(id)
																				#IDF vector done
fout=open("C:\Users\prem\Desktop\cds dp assignment\IDF.txt",'w')
fout.write(str(IDF))	
fout.close()

tfidf=dict()
def conv2tfidf(doc):
	tfidfvec=dict()
	for word in MD.keys():
		tfidfvec[word]=term_freq[doc][word]*IDF[doc][word]
	return tfidfvec

for doc in iddsum:
	tfidf[doc]=conv2tfidf(doc)											

fout=open("C:\Users\prem\Desktop\cds dp assignment\TF_IDF.txt",'w')
fout.write(str(tfidf))	
fout.close()
