from .data.db import *

def query_course_info(cid):
    sql = """
    SELECT
        TITLE,
        CREATED_AT
    FROM
        GIFT_COURSES
    WHERE
        ID = {}
    """.format(cid)
    course_info = query(sql)
    return course_info
    
def query_relations(cid):
    sql = """
    SELECT
        REQ.ID,
        REQ.STATUS,
        REQ.USER_GIFT_COURSE_ID,
        REQ.USER_ID,
        ER.NAME AS RELATION
    FROM
        GIFT_REQUESTS AS REQ
            LEFT JOIN    
        GUEST_PROFILES AS GP ON GP.GIFT_REQUEST_ID = REQ.ID
            LEFT JOIN
        EVALUATOR_RELATIONS AS ER ON ER.ID = GP.EVALUATOR_RELATION_ID
    WHERE
        REQ.USER_GIFT_COURSE_ID IN (
            SELECT
                ID
            FROM
                USER_GIFT_COURSES
            WHERE
                GIFT_COURSE_ID = {})
    """.format(cid)
    req = query(sql)
    return req

def query_gift_records(cid):
    sql = """
    SELECT
        GR.*,
        C.COMPETENCY_NAME,
        U1.NAME AS EVALUATOR_NAME,
        U1.EMAIL AS EVALUATOR_EMAIL,
        U2.NAME AS EVALUATEE_NAME,
        U2.EMAIL AS EVALUATEE_EMAIL
    FROM
        GIFT_RECORDS AS GR
            LEFT JOIN
        EVAL_QUESTIONS AS EQ ON EQ.ID = GR.QUESTION_ID
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = EQ.COMPETENCY_ID
            LEFT JOIN
        USERS AS U1 ON U1.ID = GR.EVALUATOR_ID
            LEFT JOIN
        USERS AS U2 ON U2.ID = GR.EVALUATEE_ID
    WHERE
        GR.USER_GIFT_COURSE_ID IN (
            SELECT
                ID
            FROM
                USER_GIFT_COURSES
            WHERE
                GIFT_COURSE_ID = {})
    """.format(cid)
    gr = query(sql)
    return gr

def query_gift_record_from_uid(uids):
    ### all data
    sql = """
    SELECT
        GR.EVALUATOR_ID,
        GR.EVALUATEE_ID,
        GR.SCORE,
        GR.ANSWER_TIME,
        GR.USER_GIFT_COURSE_ID,
        GR.CREATED_AT,
        C.COMPETENCY_NAME
    FROM
        GIFT_RECORDS AS GR
            LEFT JOIN
        EVAL_QUESTIONS AS EQ ON EQ.ID = GR.QUESTION_ID
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = EQ.COMPETENCY_ID
    WHERE
        GR.EVALUATEE_ID IN ({})
    AND
        C.ID < 26
    AND
        GR.ANSWER_TIME != -1
     AND
         GR.USER_GIFT_COURSE_ID IS NOT NULL
    """.format(str(uids)[1:-1])
    return query(sql)

def query_relation_from_uid(uids):
    sql = """
    SELECT
        REQ.USER_GIFT_COURSE_ID,
        REQ.USER_ID,
        REQ.STATUS,
        REQ.COMPLETED_AT,
        ER.NAME AS RELATION
    FROM
        GIFT_REQUESTS AS REQ
            LEFT JOIN    
        GUEST_PROFILES AS GP ON GP.GIFT_REQUEST_ID = REQ.ID
            LEFT JOIN
        EVALUATOR_RELATIONS AS ER ON ER.ID = GP.EVALUATOR_RELATION_ID
    WHERE
        REQ.USER_ID IN ({})
    """.format(str(uids)[1:-1])
    return query(sql)

def query_emp_uids(uids):
    sql = """
    SELECT
        USER_ID
    FROM
        EMPLOYEES
    WHERE
        USER_ID NOT IN ({})
    """.format(str(uids)[1:-1])
    return query(sql)

def query_adjscore_from_cid(cid):
    # all scores
    sql = """
    SELECT
        CS.USER_ID,
        C.COMPETENCY_NAME,
        CS.ADJUSTED_SCORE AS SCORE
    FROM
        COMPETENCY_SCORES AS CS
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = CS.COMPETENCY_ID
    WHERE
        CS.USER_GIFT_COURSE_ID IN (
            SELECT
                ID
            FROM
                USER_GIFT_COURSES
            WHERE
                GIFT_COURSE_ID = {})
    AND
        CS.ADJUSTED_SCORE != 0.5
    """.format(cid)
    adj = query(sql).pivot_table(index="USER_ID",columns="COMPETENCY_NAME",values="SCORE")
    return adj

def query_adjscore_from_uid(uids):
    #adjusted_score等をデータベースから入手
    sql = """
        SELECT
            cs.USER_ID,
            c.COMPETENCY_NAME,
            u.NAME,
            cs.ADJUSTED_SCORE AS SCORE
        FROM
            COMPETENCY_SCORES as cs
                left join
            USERS AS u on u.ID = cs.USER_ID
                left join
            COMPETENCIES AS c ON c.ID = cs.COMPETENCY_ID
        WHERE
            cs.USER_ID IN ({})
        AND
            cs.ADJUSTED_SCORE != 0.5
        AND
            cs.USER_GIFT_COURSE_ID IS NULL;
        """.format(str(uids)[1:-1])
    adj = query(sql).pivot_table(index="USER_ID",columns="COMPETENCY_NAME",values="SCORE")
    return adj

def query_selfscore_from_cid(cid):
    sql = """
    SELECT
        SER.USER_ID,
        SER.SCORE,
        C.COMPETENCY_NAME
    FROM
        SELF_EVAL_RECORDS AS SER
            LEFT JOIN
        EVAL_QUESTIONS AS EQ ON EQ.ID = SER.QUESTION_ID
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = EQ.COMPETENCY_ID
    WHERE
        USER_GIFT_COURSE_ID IN (
            SELECT
                ID
            FROM
                USER_GIFT_COURSES
            WHERE
                GIFT_COURSE_ID IN ({}))
    """.format(cid)
    selfscore = query(sql).pivot_table(index="USER_ID",columns="COMPETENCY_NAME",values="SCORE",aggfunc="mean")
    return selfscore

def query_selfscore_from_uid(uids):
    sql = """
    SELECT
        SER.USER_ID,
        SER.SCORE,
        C.COMPETENCY_NAME
    FROM
        SELF_EVAL_RECORDS AS SER
            LEFT JOIN
        EVAL_QUESTIONS AS EQ ON EQ.ID = SER.QUESTION_ID
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = EQ.COMPETENCY_ID
    WHERE
        SER.USER_ID IN ({})
    AND
        C.ID < 26
    """.format(str(uids)[1:-1])
    selfscore = query(sql).pivot_table(index="USER_ID",columns="COMPETENCY_NAME",values="SCORE",aggfunc="mean")
    return selfscore


def query_new_score_from_cid(cid):
    # all scores
    sql = """
    SELECT
        CS.USER_ID,
        C.COMPETENCY_NAME,
        CS.OVERALL_SCORE AS SCORE
    FROM
        GROW_OVERALL_COMPETENCY_SCORES AS CS
            LEFT JOIN
        COMPETENCIES AS C ON C.ID = CS.COMPETENCY_ID
    WHERE
        CS.USER_GIFT_COURSE_ID IN (
            SELECT
                ID
            FROM
                USER_GIFT_COURSES
            WHERE
                GIFT_COURSE_ID = {})
    """.format(cid)
    new_score = query(sql).pivot_table(index="USER_ID",columns="COMPETENCY_NAME",values="SCORE")
    return new_score