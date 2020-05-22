import psycopg2
from config import aws_postgres_server_name, aws_postgres_database, aws_postgres_username, aws_postgres_port, aws_postgres_password

def add_passenger(title, fname, lname, ticket_class, sex, siblings_spouse, parents_children, fare, age, port, cabin):
    try:
        connection = psycopg2.connect(user=aws_postgres_username,
                                        password=aws_postgres_password,
                                        host=aws_postgres_server_name,
                                        port=aws_postgres_port,
                                        database=aws_postgres_database)
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO public.titanicpassengers (title, fname, lname, ticket_class, sex, siblings_spouse, parents_children, fare, age, port, cabin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (title, fname, lname, ticket_class, sex, siblings_spouse, parents_children, fare, age, port, cabin)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()


def get_passengers():
    try:
        connection = psycopg2.connect(user=aws_postgres_username,
                                        password=aws_postgres_password,
                                        host=aws_postgres_server_name,
                                        port=aws_postgres_port,
                                        database=aws_postgres_database)
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from public.titanicpassengers"

        cursor.execute(postgreSQL_select_Query)

        mobile_records = cursor.fetchall() 
        
        print("Print each row and it's columns values")
        all_rows = {}
        for row in mobile_records:
            all_rows[row[0]] = row

        print(all_rows)

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to retrive record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

    return all_rows

add_passenger('Mr', 'John', 'Smith', '3', 'm', '1', '1', '8', '20', 'C', 'Z')
get_passengers()
