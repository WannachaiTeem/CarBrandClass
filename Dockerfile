# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /CarBrand

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# COPY folder หรือ file งาน
COPY ./requirements.txt /CarBrand/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /CarBrand/requirements.txt

COPY ./app /CarBrand/app
COPY ./model /CarBrand/model

ENV PYTHONPATH "${PYTHONPATH}:/CarBrand"

# ต้องการใช้ poth 80 สำหรับให้ Containers สื่อสารกันเองใน Docker
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]




