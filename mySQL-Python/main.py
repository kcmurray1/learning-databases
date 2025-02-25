from app import create_app
import mysql.connector


def main():
    # connect to db
    mydb = mysql.connector.connect(
        host="localhost",
        user="local",
        password="password"
    )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")

    for item in cursor:
        print(item)
    
    
    cursor.close()
    mydb.close()
    app = create_app()

    # app.run()

if __name__ == "__main__":
    main()