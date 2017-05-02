# Document clustering using K-means++
import random
from AP1 import *
from AP3 import choose
from AP3 import find_dist
from AP3 import assign_cluster
from AP3 import new_centroid
from AP3 import meann

def kmeanspp(k,tfidf):
	centroidspp=[]
	cdist=dict()
	cluster=dict()
	centroidspp=pp(k)
		
	for centr in centroidspp:
		cdist[centr]=find_dist(centr,tfidf)
	for doc in iddsum:
		cluster[doc]=assign_cluster(doc,cdist,centroidspp)
		print cluster
	Cluster_centres=new_centroid(cluster)					#new centroids' tfidf with same key as randomly chosen centres
	
	for i in range(10):
												#as we are never changing the intials until last run
		for centr in centroidspp:
			cdist[centr]=find_dist(centr,Cluster_centres)	
		for doc in iddsum:
			cluster[doc]=assign_cluster(doc,cdist,centroidspp)
		Cluster_centres=new_centroid(cluster)
	print cluster
	return cluster,Cluster_centres

###		
def pp(k):
	iddsumc=iddsum
	points=[]
	dist=dict()
	points=choose(1)
	#print points[0]
	probab=[]
	for i in range(k):
		#print i
		dist=find_dist(points[i],tfidf)			#distance of each doc from the point
		probab.append(find_probab(dist))						#probability for 1st wtd. centre
		#print probab
		points.append(wchoose(dist.keys(),probab[i].values()))
	#print points
	return points
	
def find_probab(dist): 
	probabi=dict()
	a=dist.values()
	for doc in iddsum:
		probabi[doc]=dist[doc]**2/sum(a)**2
	return probabi
	###
	
def wchoose(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
		cumulative_probability +=item_probability
		if x < cumulative_probability: break
    return item


		
cluster,Cluster_centres=kmeanspp(7,tfidf)

fout=open("C:\Users\prem\Desktop\cds dp assignment\Cluster_centrespp.txt",'w')
fout.write(str(Cluster_centres))	
fout.close()

fout=open("C:\Users\prem\Desktop\cds dp assignment\clusterpp.txt",'w')
fout.write(str(cluster))	
fout.close()
