FROM python:3.12-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_server /app/mcp_server

EXPOSE 5000

CMD ["uvicorn", "mcp_server.main:app", "--host", "0.0.0.0", "--port", "5000"]