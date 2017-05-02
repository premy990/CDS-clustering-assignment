# Document clustering using K-means
from AP1 import *
import random
'''
def readf(f):
	s = open(f, 'r').read()
	a=dict()
	a=eval(s)
	return a
	
iddsum=readf("C:\Users\prem\Desktop\cds dp assignment\idsum.txt") 
print "done 1"
MD=readf("C:\Users\prem\Desktop\cds dp assignment\MD.txt")
print "done 2"
term_freq=readf("C:\Users\prem\Desktop\cds dp assignment\TF.txt")
print "done 3"
IDF=readf("C:\Users\prem\Desktop\cds dp assignment\IDF.txt")
print "done 4"
tfidf=readf("C:\Users\prem\Desktop\cds dp assignment\tfidf.txt")
print "done 5"
iddsum=dict()

for key in ['4592959', '21411112', '168602','14034821', '19793556', '10536562', '33370239','32995532', '30698901', '35320691', '20956043', '35033607', '36309911']:
	iddsum=idsum
'''

def kmeans(k):
	centroids=[]
	cdist=dict()
	cluster=dict()
	centroids=choose(k)										#initial centres chosen randomly
	print centroids
	#Cluster_centres=[]
		
	for centr in centroids:
		cdist[centr]=find_dist(centr,tfidf)
	for doc in iddsum:
		cluster[doc]=assign_cluster(doc,cdist,centroids)
	print set(cluster.values())
	Cluster_centres=new_centroid(cluster)					#new centroids' tfidf with same key as randomly chosen centres
	centroids=range(1,k)
	
	for i in range(10):
		print i												#as we are never changing the intials until last run
		for centr in centroids:
			cdist[centr]=find_dist(centr,Cluster_centres)	
		for doc in iddsum:
			cluster[doc]=assign_cluster(doc,cdist,centroids)
		Cluster_centres=new_centroid(cluster)
		centroids=range(1,k)
		print cluster
	return cluster,Cluster_centres
	
def choose(k):
	iddsumc=iddsum
	a=[]
	for i in range(0,k):
		id=iddsumc.keys()
		a.append(random.choice(id))
		#iddsumc.pop(a[i], None)							#Amusing!!!!!!!!!!!!
	return a

def find_dist(centr,tfidf2):
	dist=dict()
	delsq=dict()
	mean=[]
	RMSD=dict()
	for doc in iddsum:
		mean=0
		for word in MD.keys():
			delsq[word]=(tfidf[doc][word]-tfidf2[centr][word])**2
			#print tfidf[doc][word]-tfidf2[centr][word]
		mean=sum(delsq.values())/len(tfidf[doc])
		RMSD[doc]=mean**0.5
	return RMSD
		
def assign_cluster(doc,cdist,Cc):
	a=[]
	b=[]
	#minim=sorted(cdist[cluster].values())###################
	for c in Cc:
		a.append(cdist[c][doc])
	b=min(a)
	
	for c in Cc:
		if cdist[c][doc]==b:
			return c
		

def new_centroid(cluster):
	cgr=dict()
	for doc in cluster:
		val=cluster[doc]
		cgr[val]=[]
		if val not in cgr:
			cgr[val]=doc
		else:
			cgr[val].append(doc)
	
	new_cen_tfidf=dict()
	for cl in cgr:
		new_cen_tfidf[cl]=meann(cgr[cl])
	b=set(cgr.keys())
	i=1
	for s in b:
		new_cen_tfidf[i] = new_cen_tfidf.pop(s)
		i+=1
	print set(new_cen_tfidf.keys())
	return new_cen_tfidf
	
def meann(lst):
	summ=0
	nclustc=dict()
	for word in MD.keys():
		for doc in lst:
			summ+=tfidf[doc][word]
		nclustc[word]=summ/len(lst)
	return nclustc
		
cluster,Cluster_centres=kmeans(7)

fout=open("C:\Users\prem\Desktop\cds dp assignment\Cluster_centres.txt",'w')
fout.write(str(Cluster_centres))	
fout.close()

fout=open("C:\Users\prem\Desktop\cds dp assignment\cluster.txt",'w')
fout.write(str(cluster))	
fout.close()
