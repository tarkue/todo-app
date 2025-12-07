FROM python:3.9
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --locked

# Copy the rest of the application
COPY ./ /backend/

CMD ["uv", "run", "python", "main.py"]