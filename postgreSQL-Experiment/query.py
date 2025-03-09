import psycopg2
import os, time
from datetime import datetime
from config import load_config

def get_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Measure start time
                start_time = time.time()
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                # Measure end time
                end_time = time.time()

                # Calculate execution time
                execution_time = end_time - start_time

                # Print the results
                print("Execution time for query:", execution_time, "seconds")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_vendors()
