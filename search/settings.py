# 爬虫基础url
BASE_URL_OF_SPIDER = "https://movie.douban.com/top250?start={}&filter="

# user-agent
REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "id=cpH5Z6wzYy0; douban-fav-remind=1; ll='118163'; _vwo_uuid_v2=D39AD5C50A2496F8C38E8FA0E8CAAAE54|a30d5275964046925d27ef0d9aedfaf4; __utmz=223695111.1578380415.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/240962/; ap_v=0,6.0; __utma=30149280.1636525139.1571933600.1586590142.1586694171.9; __utmc=30149280; __utmz=30149280.1586694171.9.9.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.5.6.1586694171; __utma=223695111.516478066.1576755124.1578380415.1586695731.4; __utmb=223695111.0.10.1586695731; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1586695732%2C%22https%3A%2F%2Fwww.douban.com%2Fdoulist%2F240962%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=7ccaf1c4af89339e.1576755124.4.1586696021.1578380416.",
    "Host": "movie.douban.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
}

# 爬虫控制频率时间
SLEEP_TIME = 2

# mysql配置
SERVER = "localhost"
USER = "root"
PASSWORD = "1234"
DATABASE = "search"
ENCODE = "utf8"

# 密匙
APP_SECRET = "lbj23"
