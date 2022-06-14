FROM python:3.9
RUN pip install pipenv
COPY . /carbon_footprint_web
RUN cd /carbon_footprint_web && pipenv lock --keep-outdated --requirements > requirements.txt
RUN cd /carbon_footprint_web && pip install -r requirements.txt
WORKDIR /carbon_footprint_web
