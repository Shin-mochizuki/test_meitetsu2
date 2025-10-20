import numpy as np
import matplotlib.pyplot as pl
font={'family':'IPAPGothic'}
pl.rc('font', **font)
pl.style.use('ggplot')

def corr(d,file):
   d=d.dropna()
   cor_m=np.corrcoef(d.transpose())
   ax=pl.figure(figsize=(8,8),dpi=100).add_subplot(1,1,1)
   ax.set_xticks([i + 0.5  for i in range(cor_m.shape[0])])
   ax.set_xticklabels(d.columns, minor=False,rotation=90,fontsize=11)
   ax.set_yticks([i + 0.5  for i in range(cor_m.shape[0])])
   ax.set_yticklabels(d.columns, minor=False,fontsize=8)
   hm=ax.pcolor(cor_m, cmap=pl.cm.Blues)
   pl.colorbar(hm)
   pl.xlim(0,cor_m.shape[0])
   pl.ylim(0,cor_m.shape[0])
   pl.tight_layout()
   pl.savefig(file, bbox_inches='tight',pad_inches=0.2,dpi=500)
   pl.close()
