FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

EXPOSE 8000

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt && chmod +x start.sh

CMD [ "./start.sh" ]
