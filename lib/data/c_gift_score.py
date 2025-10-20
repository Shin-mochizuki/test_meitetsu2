from .data import *

def c_gift_score(cid):
   sql='''
   SELECT 
   gr.EVALUATOR_ID,
   gr.EVALUATEE_ID,
   c.COMPETENCY_NAME,
   gr.SCORE
   FROM growdb.GIFT_RECORDS AS gr 
   LEFT JOIN growdb.USER_GIFT_COURSES AS ugc 
   ON gr.USER_GIFT_COURSE_ID=ugc.ID
   LEFT JOIN growdb.EVAL_QUESTIONS AS q 
   ON gr.QUESTION_ID=q.ID
   LEFT JOIN growdb.COMPETENCIES As c 
   ON q.COMPETENCY_ID=c.ID
   WHERE ugc.GIFT_COURSE_ID={}'''.format(cid)
   d=query(sql)
   d=d.groupby(['EVALUATEE_ID','COMPETENCY_NAME']).mean().reset_index()
   d=d.pivot_table(index=['EVALUATEE_ID'],columns=['COMPETENCY_NAME'],values='SCORE')
   # competency order
   return c_name_order2(d).reset_index()
