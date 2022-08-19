FROM python:3.8.1-slim-buster

ENV PYTHONUNBUFFERED 1


ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . ./

# CMD ["uvicorn", "api.main:app", "--reload", "--port", "8001"]


ENTRYPOINT uvicorn api.main:app --reload


# CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]



# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
# CMD ["uvicorn", "api.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"]
# CMD ["uvicorn", "api.main:app", "--reload", "--port", "80"]
# uvicorn api.main:app --reload

# Delete all none files
# docker rmi $(docker images -f "dangling=true" -q)
# wsl --shutdown (to stop deamon)
# wsl --start (to start up deamon)
# cd "C:\Program Files\Docker\Docker"./DockerCli.exe -SwitchDaemon
# docker system prune