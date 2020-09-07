FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY setup_db.py ./

RUN python setup_db.py

COPY . .

ENV FLASK_ENV=production

EXPOSE 3000

CMD [ "python", "app.py" ]
