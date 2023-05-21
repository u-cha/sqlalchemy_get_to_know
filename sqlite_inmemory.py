from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# using core.Engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as connection:
    result = connection.execute(text("SELECT 'HELLO WORLD'"))
    connection.execute(text("CREATE TABLE my_table (x int, y int)"))
    connection.execute(text("INSERT INTO my_table (x, y) VALUES (:x, :y)"), [{"x": 0, "y": 1}, {"x": 1, "y": 2}])
    connection.commit()
    print(result.all())
    result2 = connection.execute(text("SELECT x, y FROM my_table"))
    for x, y in result2:
        print(f"x: {x}, y: {y}")
    result3 = connection.execute(text("SELECT * FROM my_table WHERE y >= :y"), [{'y': 1}])
    for row in result3:
        print(f"x: {row.x}, y: {row.y}")

#using orm.Session
statement = text("SELECT x, y FROM my_table WHERE y >= :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(statement, {"y": 1})
    for row in result:
        print(f"From Session x: {row.x}  y: {row.y}")

# using .begin(), which autocommits implicitely

# with engine.begin() as committing_connection:
#     committing_connection.execute(text("INSERT INTO my_table (x, y) VALUES (:x, :y)"), [{"x": 4, "y": 5}, {"x": 5, "y": 6}])
#     result2 = committing_connection.execute(text("SELECT * FROM my_table"))
#     print(result2.all())
