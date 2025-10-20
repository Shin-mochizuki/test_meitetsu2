from .data import *

def c_self_score(cid):
   u=c_user(cid)
   uid=str(u['UID'].tolist())[1:-1]
   sql='''
   SELECT
   se.USER_ID,
   c.COMPETENCY_NAME,
   se.SCORE
   FROM growdb.SELF_EVAL_RECORDS as se
   LEFT JOIN growdb.EVAL_QUESTIONS AS q 
   ON se.QUESTION_ID=q.ID
   LEFT JOIN growdb.COMPETENCIES As c 
   ON q.COMPETENCY_ID=c.ID
   WHERE USER_ID IN ({})'''.format(uid)
   d=query(sql)
   d=d.groupby(['USER_ID','COMPETENCY_NAME']).mean().reset_index()
   d=d.pivot_table(index=['USER_ID'],columns=['COMPETENCY_NAME'],values='SCORE')
   return c_name_order2(d).reset_index()

# def c_self_score2(cid):
#    u=c_user(cid)
#    uid=str(u['UID'].tolist())[1:-1]
#    sql='''
#    SELECT
#    se.USER_ID,
#    c.COMPETENCY_NAME,
#    se.SCORE
#    FROM growdb.SELF_EVAL_RECORDS as se
#    LEFT JOIN growdb.EVAL_QUESTIONS AS q
#    ON se.QUESTION_ID=q.ID
#    LEFT JOIN growdb.COMPETENCIES As c
#    ON q.COMPETENCY_ID=c.ID
#    WHERE USER_ID IN ({})'''.format(uid)
#    d=query(sql)
#    return d
