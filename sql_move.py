import psycopg2



try:
    old = psycopg2.connect(user = "",
                            password = "",
                            host = "",
                            port = "",
                            database = "")

    cursor = old.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


try:
    new = psycopg2.connect(user = "",
                            password = "",
                            host = "",
                            port = "",
                            database = "")

    cursor = new.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)



try:
    cursor = old.cursor()
    postgreSQL_select_Query = f"""
    SELECT * FROM PUBLIC.BAN
    """

    cursor.execute(postgreSQL_select_Query)
    db = cursor.fetchall()
    for row in db:
        print(f"'{row[0]}',{row[1]},{row[2]}")
        try:
            cursor = new.cursor()
            postgreSQL_select_Query = f"""
            INSERT INTO ban () VALUES ('{row[0]}',{row[1]},{row[2]})
            """
            cursor.execute(postgreSQL_select_Query)
            new.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
except (Exception, psycopg2.Error) as error:
    print(error)

print("---------------")


try:
    cursor = new.cursor()
    postgreSQL_select_Query = f"""
    SELECT * FROM PUBLIC.BAN
    """

    cursor.execute(postgreSQL_select_Query)
    db = cursor.fetchall()
    for row in db:
        print(f"'{row[0]}',{row[1]},{row[2]}")
except (Exception, psycopg2.Error) as error:
    print(error)

