import matplotlib.pyplot as pl
font={'family':'IPAPGothic'}
pl.rc('font', **font)
pl.style.use('ggplot')

def pl_bar(x_col,y,file):
   pl.figure(figsize=(6,1.8))
   pl.bar(range(len(x_col)),y,tick_label=x_col,color="steelblue")
   pl.xticks(rotation=90,fontsize=10)
   #pl.xlabel('x')
   #pl.ylabel('y')
   pl.tight_layout()
   pl.savefig(file,bbox_inches='tight',pad_inches=0.2,dpi=400)
   pl.clf()

def pl_line(x,y,file):
   pl.plot(x,y,linewidth=2.0,color="steelblue")
   pl.xticks(rotation=90)
   pl.xlabel('x')
   pl.ylabel('y')
   pl.tight_layout()
   pl.savefig(file,bbox_inches='tight',pad_inches=0.2,dpi=400)
   pl.clf()

def pl_scatter(x,y,file):
   pl.scatter(x,y,marker='o',alpha=0.9,s=30,c="steelblue")
   pl.xlabel('x')
   pl.ylabel('y')
   pl.tight_layout()
   pl.savefig(file,bbox_inches='tight',pad_inches=0.2,dpi=400)
   pl.clf()

def pl_hist(x,file):
   pl.hist(x,color='steelblue')
   pl.xlabel('x')
   pl.ylabel('y')
   pl.tight_layout()
   pl.savefig(file,bbox_inches='tight',pad_inches=0.2,dpi=400)
   pl.clf()
