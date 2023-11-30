FROM python:3-slim


WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000


CMD [\
"sh", "-c", \
"npx", "tailwindcss", "-i", "./base/static/src/input.css", "-o", "./base/static/src/output.css", "--watch" & "python3", "manage.py", "runserver", "0.0.0.0:8000" \
]
