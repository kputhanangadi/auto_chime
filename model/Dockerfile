FROM python:3.10.9

RUN ["apt-get", "update"]

RUN ["apt-get", "install", "-y", "python3-opencv"]

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["bash"]