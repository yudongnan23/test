from pymysql import *
import logging
from settings import *


def get_db():
    """

    :return:
    """
    db = connect(SERVER, USER, PASSWORD, DATABASE, charset=ENCODE)
    return db


def save_data(data: list):
    """

    :param data:
    :return:
    """
    db = get_db()
    cursor = db.cursor()

    for single_data in data:
        sql = '''
                insert into 
                movie(id,title,director,actor,year,country,class,grade,abstract,pic_url) values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''.format(
            single_data["id"],
            single_data["title"],
            single_data["director"],
            single_data["actor"],
            single_data["year"],
            single_data["country"],
            single_data["class"],
            single_data["grade"],
            single_data["abstract"],
            single_data["pic_url"]
        )

        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            logging.error(dict(
                messsage="Save the data to mysql is failed: {}".format(e),
                error_data=single_data
            ))
            db.rollback()
    db.close()


def query_movie_by_name(keywords: str, all=False) -> str:
    """

    :param keywords:
    :return:
    """
    db = get_db()

    cursor = db.cursor()
    sql1 = '''
            select title 
            from movie
            where title like "%{}%";  
    '''.format(keywords)
    sql2 = '''
            select * 
            from movie
            where title like "%{}%";
    '''.format(keywords)

    if all:
        cursor.execute(sql2)
        try:
            result = [list(value) for value in cursor.fetchall()]
            result_data = list(result)
        except:
            result_data = ""
    else:
        cursor.execute(sql1)
        try:
            result = cursor.fetchall()
            results = []
            for value in result:
                results.append(value[0])
            results = list(set(results))
            result_data = ",".join(results)

        except:
            result_data = ""
    return result_data
