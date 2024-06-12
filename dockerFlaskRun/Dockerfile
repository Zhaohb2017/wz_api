FROM python:3.7

WORKDIR  /app

# 将当前目录中的文件复制到容器的工作目录中
COPY . /app
RUN echo "DefaultLimitNOFILE=65535" >> /etc/systemd/system.conf
RUN echo "DefaultLimitNPROC=65535" >> /etc/systemd/system.conf
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# 暴露容器的端口
EXPOSE 8863

CMD ["python", "flask_run.py"]
