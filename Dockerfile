FROM python:3.8

WORKDIR /home/ilya/Universe/PythonISP/ISP-LP1
# main.py /
ADD . .

RUN pip3 install numpy

CMD [ "python3", "main.py" ]
