FROM alpine:3.16.2

# installazione python e pip, copiata da internet :D
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt /requirements.txt

RUN python -m pip install -r requirements.txt

EXPOSE 8000

WORKDIR / 
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
