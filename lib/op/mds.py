from scipy.spatial import distance
from sklearn import manifold

def mds(d):
   mds=manifold.MDS(n_components=2, dissimilarity='precomputed')
   #mds=manifold.MDS(n_init=400,n_components=2, dissimilarity='precomputed')
   re=mds.fit_transform(distance.cdist(d,d))
   return re
