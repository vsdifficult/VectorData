FROM python:3.12

RUN apt-get update && apt-get install -y build-essential

RUN pip install sentence-transformers chromadb fastapi sentence_transformers pydantic uvicorn 

COPY . /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["python", "./src/main.py"]
