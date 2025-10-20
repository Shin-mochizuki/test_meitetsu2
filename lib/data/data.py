from lib.data.db import *

def competency_name():
    sql = """
    SELECT
        ID,
        COMPETENCY_NAME
    FROM growdb.COMPETENCIES
    """
    return(query(sql))

def adj_c_score(cid):
    sql = """
    SELECT
        USER_ID,
        COMPETENCY_ID,
        ADJUSTED_SCORE
    FROM growdb.COMPETENCY_SCORES
    WHERE USER_GIFT_COURSE_ID IN
        (SELECT
            ID
        FROM growdb.USER_GIFT_COURSES
        WHERE GIFT_COURSE_ID = {})
    """.format(cid)
    return(query(sql))

def status(cid):
    sql = """
    SELECT
        USER_ID,
        STATUS,
        COMPLETED_AT
    FROM growdb.USER_GIFT_COURSES
    WHERE GIFT_COURSE_ID = {}
    """.format(cid)
    return(query(sql))

def get_eval_count(cid):
    sql = """
        SELECT
            gr.STATUS,
            ugc.ID,
            ugc.USER_ID
        FROM
            growdb.GIFT_REQUESTS AS gr
                LEFT JOIN
            growdb.USER_GIFT_COURSES AS ugc ON ugc.ID = gr.USER_GIFT_COURSE_ID
        WHERE gr.USER_GIFT_COURSE_ID IN (
            SELECT
                ugc.ID
            FROM
                growdb.USER_GIFT_COURSES
            WHERE
                ugc.GIFT_COURSE_ID = {})
    """.format(cid)
    return (query(sql))

# def big5_score(cid):
#     sql = """
#     SELECT
#         UID,
#         ITEM,
#         SCORE
#     FROM
#         analysis.GIFT_COURSE_BIG5_SCORES
#     WHERE GIFT_COURSE_ID = {}
#     AND ITEM IN ("外向性-内向性","開放性-保守性","繊細性-平穏性","協調性-独立性","誠実性-快楽性")
#     """.format(cid)
#     return (query(sql))

def big5_score(uid):
    sql = """
    SELECT
        UID,
        ITEM,
        SCORE
    FROM
        analysis.GLOBAL_BIG5_SCORES
    WHERE UID IN ({})
    AND ITEM IN ("外向性-内向性","開放性-保守性","繊細性-平穏性","協調性-独立性","自律性-自由性")
    """.format(str(uid)[1:-1])
    return (query(sql))


def user_info(cid):
    sql = """
    SELECT
        u.UID,
        u.NAME2 AS NAME,
        u.GENDER,
        u.BIRTHDAY,
        u.MAIL1,
        u.MAIL2,
        u.MAIL3,
        ed.SCHOOL_NAME,
        ed.CONCENTRATION,
        ed.DATE_OF_ENTRY
    FROM analysis.USERS AS u
        LEFT JOIN
    growdb.EDUCATIONS AS ed ON ed.USER_ID = u.UID
    WHERE u.UID IN (SELECT ugc.USER_ID FROM growdb.USER_GIFT_COURSES AS ugc WHERE ugc.GIFT_COURSE_ID = {})
    """.format(cid)
    return(query(sql))

def c_user(c_id):
    sql='''
    SELECT
    u.UID,
    u.NAME1,
    u.NAME2,
    u.GENDER,
    u.COMMUNITY,
    u.MAIL1,
    u.MAIL2,
    u.MAIL3
    FROM analysis.USERS AS u
    LEFT JOIN growdb.USER_GIFT_COURSES AS ugc ON ugc.USER_ID = u.UID
    WHERE u.UID NOT IN (SELECT user_id FROM analytics.igs_parties)
    AND ugc.GIFT_COURSE_ID=\'{}\''''.format(c_id)
    return(query(sql))

def c_record(c_id):
    sql='''
    SELECT
    gr.EVALUATOR_ID AS EVALUATOR_ID,
    gr.EVALUATEE_ID AS EVALUATEE_ID,
    c.COMPETENCY_NAME AS COMPETENCY_NAME,
    gr.SCORE AS SCORE,
    gr.ANSWER_TIME AS ANSWER_TIME,
    gr.USER_GIFT_COURSE_ID AS USER_GIFT_COURSE_ID,
    gr.CREATED_AT AS CREATED_AT
    FROM growdb.GIFT_RECORDS AS gr
    LEFT JOIN growdb.EVAL_QUESTIONS AS eq
    ON gr.QUESTION_ID = eq.ID
    LEFT JOIN growdb.COMPETENCIES AS c
    ON eq.COMPETENCY_ID = c.ID
    WHERE gr.USER_GIFT_COURSE_ID IN (
    SELECT ID
    FROM USER_GIFT_COURSES
    WHERE GIFT_COURSE_ID = \'{}\')'''.format(c_id)
    return(query(sql))

def c_name():
    sql='SELECT ID,COMPETENCY_NAME FROM growdb.COMPETENCIES ORDER BY ID'
    return(query(sql))

def c_name_en():
    sql='SELECT ID,COMPETENCY_NAME,COMPETENCY_NAME_EN FROM growdb.COMPETENCIES ORDER BY ID'
    return(query(sql))

def c_name_order(d):
    n=pd.DataFrame(d.columns)
    n=n.join(c_name().set_index('COMPETENCY_NAME'),on='ITEM')
    n=n.sort_values(by='ID')['ITEM'].tolist()
    return d[n]

def c_name_order2(d):
    n=pd.DataFrame(d.columns)
    n=n.join(c_name().set_index('COMPETENCY_NAME'),on='COMPETENCY_NAME')
    n=n.sort_values(by='ID')['COMPETENCY_NAME'].tolist()
    return d[n]

def b_name():
    sql='SELECT ID,TITLE FROM growdb.BIG5S ORDER BY ID'
    return(query(sql))

def b_name_en():
    sql='SELECT ID,TITLE,TITLE_EN FROM growdb.BIG5S ORDER BY ID'
    return(query(sql))

def b_name_order(d):
    n=pd.DataFrame(d.columns)
    n=n.join(b_name().set_index('TITLE'),on='ITEM')
    n=n.sort_values(by='ID')['ITEM'].tolist()
    return d[n]
