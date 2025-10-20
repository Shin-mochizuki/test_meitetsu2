from .data import *

def to_eng_name(d):
   ce=c_name_en()
   ce_map={}
   for i in range(len(ce)):
      ce_map[ce.loc[i]['COMPETENCY_NAME']]=ce.loc[i]['COMPETENCY_NAME_EN']
   d.rename(columns=ce_map,inplace=True)

   be=b_name_en()
   be_map={}
   for i in range(len(be)):
      be_map[be.loc[i]['TITLE']]=be.loc[i]['TITLE_EN']
   d.rename(columns=be_map,inplace=True)
   return d