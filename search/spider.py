import requests
from settings import BASE_URL_OF_SPIDER, REQUEST_HEADERS, SLEEP_TIME
from time import sleep
from lxml.etree import HTML
from multiprocessing import Process, Queue
from db_manager import save_data


def get_page(page: int) -> str:
    """

    :return: page data from douban
    """
    response = requests.get(BASE_URL_OF_SPIDER.format(page), headers=REQUEST_HEADERS)
    response.encoding = "utf-8"

    return response.text


def clean_data(text: str) -> list:
    """

    :param text:
    :return:
    """
    results = []

    html = HTML(text)
    items = html.xpath("//ol/li")

    for item in items:
        id = item.xpath(".//div[1]/div[1]/a/@href")[0].split("/")[-2]
        # 电影图片url
        pic_url = item.xpath(".//div[1]/div[1]/a/img/@src")[0]
        # 电影片名
        title = item.xpath(".//div/div[2]/div[1]/a/span[1]/text()")[0]
        director_and_actor = item.xpath(".//div/div[2]/div[2]/p/text()[1]")[0].split("主演:")
        # 获取导演信息，取第一个
        director = director_and_actor[0].strip().split("导演:")[1].split("/")[0].strip()
        # 获取主演信息，取第一个
        try:
            actor = director_and_actor[1].strip().split("/")[0].strip()
        except:
            actor = ""
        if actor == "...":
            actor = ""
        year_country_class = item.xpath(".//div/div[2]/div[2]/p/text()[2]")[0].strip().split("/")
        # 电影发布年份
        year = year_country_class[0].strip()
        # 电影发布国家
        country = year_country_class[1].strip()
        # 电影类别
        _class = year_country_class[2].strip()
        # 电影评分
        grade = item.xpath(".//div/div[2]/div[2]/div[1]/span[2]/text()")[0]
        try:
            # 电影摘要
            abstract = item.xpath(".//div/div[2]/div[2]/p[2]/span/text()")[0]
        except:
            abstract = ""

        result = {
            "id": id,
            "pic_url": pic_url,
            "title": title,
            "director": director,
            "actor": actor,
            "year": year,
            "country": country,
            "class": _class,
            "grade": grade,
            "abstract": abstract
        }
        results.append(result)

    return results


def consume_data(queue):
    """ 清洗网页数据并调用函数存储数据

    :param queue：
    :return:
    """

    while True:
        text = queue.get()
        if not text:
            break

        data = clean_data(text)
        save_data(data)

    return


def start_spider():
    """

    :return:
    """
    # 创通信队列
    queue = Queue()
    # 创建一个子进程，用于并发清洗抓取的页面
    process = Process(target=consume_data, args=(queue,))
    process.start()

    # 循环获取所有页面内容
    for page in range(0, 256, 25):
        # 获取指定页面的数据
        response = get_page(page)
        # 将页面内容丢进队列
        queue.put(response)
        sleep(SLEEP_TIME)
    queue.put(None)
    process.join()
