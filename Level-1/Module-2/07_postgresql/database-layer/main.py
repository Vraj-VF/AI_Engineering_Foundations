import os


def main():
    try:
        import psycopg
    except ImportError:
        print("Install psycopg before running the database demo")
        return
    url = os.environ.get(
        "DATABASE_URL", "postgresql://aiuser:local-password@localhost/aidb"
    )
    with psycopg.connect(url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "create table if not exists models (id serial primary key, name text not null)"
            )
            cursor.execute(
                "insert into models (name) values (%s)", (input("Model name: "),)
            )
            cursor.execute("select id, name from models")
            print(cursor.fetchall())


if __name__ == "__main__":
    main()
