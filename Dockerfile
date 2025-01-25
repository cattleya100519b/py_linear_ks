FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Dockerコンテナ内で新しいKernelを登録
RUN python -m ipykernel install --user --name=my_docker_kernel --display-name "Python (Docker)"