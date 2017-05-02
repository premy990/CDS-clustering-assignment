# Tagging Document Genres for Clusters

from AP1 import *
from AP3 import *

def cgrp(cluster):
	cgr=dict()
	for doc in cluster:
		val=cluster[doc]
		cgr[val]=[]
		if val not in cgr:
			cgr[val]=doc
		else:
			cgr[val].append(doc)
	print cgr
	return cgr

def cgrfreq():
	cfreq=dict()
	clsfreq=dict()
	for cl in cldoc:
		for word in MD.keys():
			cfreq[word]=0
			for doc in cldoc[cl]:
				cfreq[word]+=term_freq[doc][word]
				#print cl,word,doc,term_freq[doc][word]
		clsfreq[cl]=cfreq		
	return clsfreq
	
def freq_word(cl):
	tag=[]
	values=[]
	values=sorted(clsfreq[cl].values(),reverse=True)
	for v in values:
		for word in MD.keys():
			if clsfreq[cl][word]==v:
				tag.append(word)
	return tag

cldoc=cgrp(cluster)
print cldoc
clsfreq=cgrfreq()
#print clsfreq
tag=dict()
for cl in cldoc:
	tag[cluster]=freq_word(cl)
print tag
fout=open("C:\Users\prem\Desktop\cds dp assignment\tag.txt",'w')
fout.write(str(tag))
fout.close()
# once this code is tested, we can modify input reqmnts as per question	