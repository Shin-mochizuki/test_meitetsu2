from lib.data.data import *
import datetime

def course_data(cid):
    # Competency name
    competencies = competency_name()
    competency_dict = {k:v for k,v in zip(competencies.ID,competencies.COMPETENCY_NAME)}
    # Adjusted_score
    adj = adj_c_score(cid).pivot_table(index="USER_ID",columns="COMPETENCY_ID",values="ADJUSTED_SCORE")\
            .rename(columns=competency_dict)
    cn = adj.columns.tolist()
    # Status
    st = status(cid).drop_duplicates(subset=["USER_ID"],keep="last").set_index("USER_ID")
    #User info
    user = user_info(cid).sort_values(by=["UID","DATE_OF_ENTRY"])\
            .drop_duplicates(subset=["UID"],keep="last").set_index("UID")\
            .drop("DATE_OF_ENTRY",axis=1)
    uid = user.index.tolist()
    #Big5 SCORE
    big5 = big5_score(uid).pivot_table(index="UID",columns="ITEM",values="SCORE")\
            .loc[:,["外向性-内向性","開放性-保守性","繊細性-平穏性","協調性-独立性","自律性-自由性"]]
    bn = big5.columns.tolist()
    #EVAL count
    gr = get_eval_count(cid).pivot_table(index="USER_ID",columns="STATUS",values="ID",aggfunc="count")\
        .rename(columns=({1:"未回答",2:"回答"}))
    # gr = get_eval_count(cid)
    # data frame
    data = pd.concat([user,adj,big5,st,gr],axis=1)\
        .reset_index().rename(columns={"index":"UID","USER_ID":"UID"})\
        .pipe(lambda df: df.assign(COMPLETED_AT=df["COMPLETED_AT"]+datetime.timedelta(hours=9)))
    return data,cn,bn
