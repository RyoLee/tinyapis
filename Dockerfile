FROM python:3.7.9-alpine
ADD ./TinyApis.cfg.sample /
ADD ./TinyApis.py /
ADD ./entrypoint.sh /
RUN pip install flask \
&& chmod +x /entrypoint.sh
WORKDIR /
ENTRYPOINT ["/entrypoint.sh"]