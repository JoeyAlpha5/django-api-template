FROM python:3.11


#########################
# Upload required files #
#########################

WORKDIR /app/
COPY . .

RUN pip install -r requirements/base.txt
RUN python manage.py collectstatic --no-input

EXPOSE 8000
