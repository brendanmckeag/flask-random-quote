FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handler.py /

ENV PORT=5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "handler:app"]
