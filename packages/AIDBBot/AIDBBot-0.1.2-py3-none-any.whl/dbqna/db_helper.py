# db_helper.py
import psycopg2

class DBHelper:
    def __init__(self, host, port, database, user, password):
        """Initialize database connection settings"""
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect_to_db(self):
        """Establish connection to the PostgreSQL database"""
        try:
            
            conn = psycopg2.connect(
                host=self.host[0],
                port=self.port[0],
                database=self.database[0],
                user=self.user[0],
                password=self.password
            )
            return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def execute_query(self, query):
        """Execute an SQL query and return results"""
        query = query.replace("\\n", " ").strip()
        conn = self.connect_to_db()
        if conn is None:
            return "Database connection failed."

        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    conn.commit()
                    return "Query executed successfully."
        except Exception as e:
            return f"Error executing query: {e}"
        finally:
            if conn:
                conn.close()


# Functions to be imported
def get_database_schema(host, port, database, user, password):
    """Fetches the schema of all tables in the database."""
    db_helper = DBHelper(host, port, database, user, password)
    conn = db_helper.connect_to_db()
    if conn is None:
        return "Database connection failed."
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT table_name, column_name, data_type 
                FROM information_schema.columns 
                WHERE table_schema = 'public'
                ORDER BY table_name, ordinal_position;
            """)
            schema_data = cursor.fetchall()

            schema_dict = {}
            for table_name, column_name, data_type in schema_data:
                if table_name not in schema_dict:
                    schema_dict[table_name] = []
                schema_dict[table_name].append(f"{column_name} ({data_type})")

            schema_description = "\n".join(
                [f"Table: {table}\nColumns: {', '.join(columns)}" for table, columns in schema_dict.items()]
            )
            return schema_description
    except Exception as e:
        return f"Error fetching schema: {e}"
    finally:
        if conn:
            conn.close()


def execute_query(query, host, port, database, user, password):
    """Execute an SQL query using DBHelper"""
    db_helper = DBHelper(host, port, database, user, password)
    return db_helper.execute_query(query)
