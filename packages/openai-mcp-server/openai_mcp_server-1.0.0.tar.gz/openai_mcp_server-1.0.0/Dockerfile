# Use Python 3.13 slim as base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install uv && uv venv && uv pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=""

# Command to run the MCP server
CMD ["uvicorn", "openai_mcp_server.main:app", "--host", "0.0.0.0", "--port", "8000"]