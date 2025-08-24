FROM python:3.12-bookworm

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire mcp_server directory including generated_client
COPY mcp_server/ /app/mcp_server/

# Verify that the generated_client directory exists
RUN ls -la /app/mcp_server/generated_client/ || echo "Warning: generated_client directory not found"

EXPOSE 5000

CMD ["uvicorn", "mcp_server.main:app", "--host", "0.0.0.0", "--port", "5000"]
