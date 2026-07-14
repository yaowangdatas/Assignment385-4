import mysql.connector as mydbconnection
from mysql.connector import Error

'''
3. generate_user_table() Method:
➢ Establish a connection to the RegistrationDB.
➢ Create a user table with the following fields/columns:
▶ email varchar(100)
▶ name varchar(50)
▶ password varchar(30)
➢ Insert the following values into the table:
▶ 'ywbaek@perscholas.org', 'young', 'letsgomets'
▶ 'mcordon@perscholas.org', 'marcial', 'perscholas'
▶ 'mhaseeb@perscholas.org', 'haseeb', 'platform'
'''

def generate_user_table():
    try:
        # Establish connection to RegistrationDB
        conn = mydbconnection.connect(database='registrationdb', user='root', password='root')

        if conn.is_connected():
            cursor = conn.cursor()

            # Create user table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS user (
                email VARCHAR(100) NOT NULL,
                name VARCHAR(50) NOT NULL,
                password VARCHAR(30) NOT NULL
            );
            """
            cursor.execute(create_table_query)
            print("'user' table is created")

            # Insert records
            insert_query = """INSERT INTO user (email, name, password) VALUES (%s, %s, %s);"""

            users = [('ywbaek@perscholas.org', 'young', 'letsgomets'),
                ('mcordon@perscholas.org', 'marcial', 'perscholas'),
                ('mhaseeb@perscholas.org', 'haseeb', 'platform')]

            cursor.executemany(insert_query, users)

            # Save changes
            conn.commit()

            print(cursor.rowcount, " records inserted into user table successfully.")

    except Error as error:
        print("Failed to insert record into user table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")


'''
4. get_all_users() Method:
➢ Establish a connection to the RegistrationDB.
➢ Print out the email, name, and password of all users.
'''

def get_all_users():
    try:
        # Establish connection to RegistrationDB
        conn = mydbconnection.connect(database='registrationdb', user='root', password='root')

        if conn.is_connected():
            cursor = conn.cursor()

            # Retrieve all users
            query = "SELECT email, name, password FROM user;"
            cursor.execute(query)

            users = cursor.fetchall()

            # Print all users
            print("Total rows in 'user' table: ", cursor.rowcount)
            print("\nPrinting each row")
            for row in users:
                print("Email: ", row[0])
                print("Name: ", row[1])
                print("Password: ", row[2], "\n" )

    except Error as e:
        print("Fail to get data from 'user' table {}.").format(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

'''
5. get_user_by_name(name) Method:
➢ Establish a connection to the RegistrationDB.
➢ Print out the email and password of the user with the given name.
'''

def get_user_by_name(name):
    try:
        # Establish connection to RegistrationDB
        conn = mydbconnection.connect(database='registrationdb', user='root', password='root')

        if conn.is_connected():
            cursor = conn.cursor()

            # Query user by name
            query = "SELECT email, password FROM user WHERE name = %s;"
            cursor.execute(query, (name,))

            user = cursor.fetchall()

            if user:
                print("Email: ", user[0][0])
                print("Password: ", user[0][1], "\n")
            else:
                print(f"User {name} not found.")

    except Error as e:
        print("Error to get data from 'user' table. {}").format(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")


'''
6. validate_user(email, password) Method:
Establish a connection to the RegistrationDB.
Return True if a user exists with the given email and password. Return False otherwise.
'''

def validate_user(email, password):
    try:
        # Establish connection to RegistrationDB
        conn = mydbconnection.connect(database='registrationdb', user='root', password='root')

        if conn.is_connected():
            cursor = conn.cursor()

            # Check if the user exists
            query = """
            SELECT * FROM user
            WHERE email = %s AND password = %s;
            """
            cursor.execute(query, (email, password))

            user = cursor.fetchone()

            if user:
                return True
            else:
                return False

    except Error as e:
        print("Error to validate the email and password.").format(e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")


'''
7. update_user(email, name, password) method:
➢ Establish a connection to the RegistrationDB.
➢ For the user with the given email, set the values of name and password to the given name and password.
➢ Return True if successful, False otherwise.
➢ Test the functions by running them in the program.
➢ Check the database manually to see if the changes are applied correctly.
'''
def update_user(email, name, password):
    try:
        # Establish connection to RegistrationDB
        conn = mydbconnection.connect(database='registrationdb', user='root', password='root')

        if conn.is_connected():
            cursor = conn.cursor()

            # Update the user's name and password
            query = """
            UPDATE user
            SET name = %s,
                password = %s
            WHERE email = %s;
            """

            cursor.execute(query, (name, password, email))
            conn.commit()
            
            # Check if any row was updated
            if cursor.rowcount > 0:
                return True
            else:
                return False

    except Error as e:
        print("Error while updating data: ").format(e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")




# Call the functions
# generate_user_table()

# get_all_users()

# get_user_by_name("young")
# get_user_by_name('young1')

# valid_user = validate_user("ywbaek@perscholas.org", "letsgomets")
# print("Valid user: ", valid_user)
# invalid_user = validate_user("ywbaek@perscholas.org", "wrongpass")
# print("Invalid user: ", invalid_user)    # False


# Update an existing user
updated = update_user(
    "ywbaek@perscholas.org",
    "Young",
    "newpassword"
)

if updated:
    print("User updated successfully.")
else:
    print("User update failed.")


