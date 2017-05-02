'''
def readf(f):
	s = open(f, 'r').read()
	a=dict()
	a=eval(s)
	return a
	
idsum=readf("C:\Users\prem\Desktop\cds dp assignment\idsum.txt") 
print "done 1"
MD=readf("C:\Users\prem\Desktop\cds dp assignment\MD.txt")
print "done 2"
term_freq=readf("C:\Users\prem\Desktop\cds dp assignment\TF.txt")
print "done 3"
IDF=readf("C:\Users\prem\Desktop\cds dp assignment\IDF.txt")
print "done 3"

#######################Pt2
'''

from AP1 import *

def conv2distance(new_doc,k1):
	d1vec=dict()
	distance=dict()
	for doc in iddsum:
		distance[doc]=0
		for word in MD.keys():
			d1vec[word]=tfidf[doc][word]*tfidf[new_doc][word]
			distance[doc]+=d1vec[word]									# distance of any vector (can find distance of new_doc similarly)
	knearest(distance,k1)

	
def knearest(distance,k):
	a=[]
	a=sorted(distance.values(),reverse=True)
	for i in range(1,k):
		for key in distance:
			if distance[key]==a[i]:
				print key
		
conv2distance('33370239',7)