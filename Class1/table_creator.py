import psycopg2

# 테이블 생성 함수
def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        timestamp timestamp,
        sepal_length float8, 
        sepal_width float8,
        petal_length float8,
        petal_width float8,
        target int
    );"""
    print(create_table_query)
    # 작성한 query 를 DB 에 전달
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()

# DB 연결
if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase",
    )
    create_table(db_connect)