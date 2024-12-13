FROM python:latest
RUN apt-get update && apt-get install libgl1 -y
RUN pip install pyqt5
