FROM python:3.11.3-bullseye
# ��������� ������� �����
WORKDIR /var/kpopbot
#EXPOSE 8080
RUN pip install telebot
CMD cd /var/kpopbot && python3 main.py