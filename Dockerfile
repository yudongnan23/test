FROM ubuntu:18.04

# 更换软件源
COPY sources.list .
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN mv sources.list /etc/apt/sources.list

RUN apt-get upgrade && apt-get update

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# 更换时区
RUN apt-get install tzdata
#set timezone
ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y build-essential wget

RUN apt-get install -y python3.6 python3.6-dev python3-distutils

RUN wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN apt-get update

COPY requirements.txt .
RUN pip3.6 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# TODO： 安装mysql并定义数据表

WORKDIR /var/www/work
COPY search search
WORKDIR /search

ENTRYPOINT["python3.6"]

CMD ["app.py"]
