FROM python:3.13-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache 
ENV PATH="/app/venv/bin:$PATH"
ENV VALUE_API_SERVER="http://server"
ENV CONTEXT="default"
# TODO: INTEGRATE THIS
ENV PORT=80 
# TODO: INTEGRATE THIS
ENV HOST=0.0.0.0
# Run the application.
CMD uv run valueapifrontend --server $VALUE_API_SERVER --context $CONTEXT
