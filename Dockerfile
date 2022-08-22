FROM python:3.8.1

WORKDIR /opt

ENV PYTHONUNBUFFERED 1

# this ensures that the system pip is current before setting up the user and using it.
RUN pip install --upgrade pip

RUN adduser --disabled-password --gecos '' newuser

# Install requirements, including from Gemfury
ADD . /opt/

# ADD requirements.txt .
RUN pip install --trusted-host pypi.python.org -r /opt/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:api"

RUN chmod +x /opt/run.sh
RUN chown -R newuser:newuser ./
USER newuser
# EXPOSE 8001

CMD ["bash", "./run.sh"]
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]


















# FROM python:3.8.1

# ENV PYTHONUNBUFFERED 1

# ADD requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# COPY . ./

# ENV PYTHONPATH "${PYTHONPATH}:app"
# CMD ["bash", "./run.sh"]

# # CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]