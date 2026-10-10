FROM python:3.11-slim

# Install OpenJDK 17 for Java sandbox code compilation & execution
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jdk-headless gcc && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app

# Copy dependencies first for fast layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Pre-compile problem catalog
RUN python curriculum_builder.py

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
