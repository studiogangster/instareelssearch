FROM python:3.9
RUN pip3 install flask
RUN pip3 install requests

CMD python3 main.py
