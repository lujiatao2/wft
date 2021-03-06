FROM python:3.7.9-alpine
COPY . /wft
WORKDIR /wft
RUN rm -rf .idea venv \
    && pip config set global.trusted-host mirrors.aliyun.com \
    && pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/ \
    && pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","0:8000"]