FROM python

WORKDIR /root/Hyper_Speed0

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install pymine

CMD ["python3","-m","main.py"]
