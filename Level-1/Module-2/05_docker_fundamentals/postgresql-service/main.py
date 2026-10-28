from pathlib import Path


def main():
    compose = """services:
  api:
    build: .
    depends_on:
      database:
        condition: service_healthy
  database:
    image: postgres:16
    environment:
      POSTGRES_DB: aidb
      POSTGRES_USER: aiuser
      POSTGRES_PASSWORD: local-password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U aiuser -d aidb"]
      interval: 5s
      timeout: 5s
      retries: 5
volumes:
  postgres-data:
"""
    Path("docker-compose.yml").write_text(compose, encoding="utf-8")
    print("PostgreSQL service, named volume, and health check created")


if __name__ == "__main__":
    main()
