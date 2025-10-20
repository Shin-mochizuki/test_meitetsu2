import matplotlib.pyplot as pl
font={'family':'IPAPGothic'}
pl.rc('font', **font)
pl.style.use('ggplot')

def b_group_box(d,dn,file):
   fig=pl.figure(figsize=(12,4))
   pl.subplots_adjust(wspace=0.8,hspace=0.6)
   cn=d[0].columns
   for i in range(len(cn)):
      tmp=[]
      for dx in d:
         tmp+=[dx[cn[i]].dropna()]
      ax=fig.add_subplot(1,len(cn),i+1)
      b=ax.boxplot(tmp,widths=0.5)
      ax.set_title(cn[i],fontsize=8)
      ax.set_xticks([i+1 for i in range(len(dn))])
      ax.set_xticklabels(dn,rotation=90,fontsize=8)
      pl.ylim(-2,2)
      pl.xlim(0,len(dn)+1)
      for k in range(len(dn)):
         c1='#4682b4'   # steelblue
         c2='#ff6347'   # tomato
         pl.setp(b['boxes'][k],color=c1)
         pl.setp(b['medians'][k], color=c2, linewidth=1)
         pl.setp(b['fliers'][k],color=c1,marker='x',markersize=2,markerfacecolor=c1,linestyle='none')
         pl.setp(b['whiskers'][2*k],color=c1,linewidth=1,linestyle='--')
         pl.setp(b['whiskers'][2*k+1],color=c1,linewidth=1,linestyle='--')
         pl.setp(b['caps'][2*k],color=c1,linewidth=1)
         pl.setp(b['caps'][2*k+1],color=c1,linewidth=1)
   pl.savefig(file, bbox_inches='tight',pad_inches=0.2,dpi=400)
   pl.close()
