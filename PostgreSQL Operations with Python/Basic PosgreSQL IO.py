import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
from psycopg2 import sql # Does not install with pandas, need separate pip install


csv_path = r"<path to file>"
fields = ["<list of fields in the database table you wish to write to>"]

host = "" 
database = ""
user = ""
password = ""

conn_string = f"postgresql://{user}:{password}@{host}/{database}" # Construct the database URL
engine = create_engine(conn_string) # Establish the connection to the db

insp = inspect(engine) # Allows US to retrieve details about the db and its structure
tables = insp.get_table_names() # returns all the table names in the db in list format

# Convert CSV to Python list
def get_csv_data(csv_path):
    df = pd.read_csv(csv_path)
    data = df.values.tolist()
    return data

# For QC Purposes, prints the CSV up to some limit
def print_list(qc_list, num_recs):
    i = 0
    while i <= num_recs:
        print(qc_list[i])
        if i >= len(qc_list):
            print("Reached the end of the list, terminating.")
            break
        i += 1

# Construct insert statement using using psycopg2
# Generally painful, but here for reference
def construct_insert_statement(table, fields, data_list, lim):
    # Added for testing purposes
    #TODO - Remove limit prior to production
    if lim > len(data_list)-1:
        lim = len(data_list)-1
        print("Limit was greater than the list length; using list length")
    data_subset = data_list[:lim]
    # Construct the initial part of the SQL statement
    query_header = sql.SQL("INSERT INTO" + " " + table + " (" + ", ".join(fields) + ")\n")
    # Loop through the list of values you wish to insert and construct an appropriate SQL statement for that row
    values_statements = []
    for row in data_subset:
        values = [sql.Literal(value) for value in row[:len(fields)]]
        values_statements.append(sql.SQL("({})".format(sql.SQL(',').join(values))))
    # Add all those rows together into a single body and concatenate with the header to form a complete SQL statement
    all_values = sql.SQL('\n').join(values_statements)
    insert_query = query_header + sql.SQL("VALUES\n{}").format(all_values)
    return insert_query

# Insert data using pandas, wayyyyy easier
def insert_data(table, fields, data_list):
    # Added for testing purposes
    #TODO - Remove limit prior to production
    if lim > len(data_list)-1:
        lim = len(data_list)-1
        print("Limit was greater than the list length; using list length")
    data_subset = data_list[:lim]
    df = pd.DataFrame(data=data_subset, columns=fields)
    df.to_sql(name=table, con=engine, if_exists='append', index=False)


# Querying the data using pandas is as easy as:
df = pd.read_sql(
    """
        -- Select the most populous city for every state in sample data
        WITH  ranked_pop AS (
            SELECT 
                id,
                state,
                pop_2010::int,
                DENSE_RANK() OVER (PARTITION BY state ORDER BY pop_2010) AS pop_rank
            FROM us_cities
                )

                SELECT
                    id,
                    state,
                    pop_2010,
                    pop_rank
                FROM ranked_pop
                WHERE pop_rank = 1
    """,
    engine
)