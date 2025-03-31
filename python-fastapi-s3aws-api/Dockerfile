FROM python:3.11-alpine

WORKDIR /usr/src/app

# Copying only the requirements.txt
COPY ./requirements.txt ./

# Invalidating cache &
# installing the dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

# Copying the rest of the files
COPY . .

EXPOSE 8000

CMD ["uvicorn", "--app-dir", "./app", "main:app", "--host", "0.0.0.0", "--port", "8000"]