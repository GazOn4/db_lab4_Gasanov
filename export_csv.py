import csv
import psycopg2

username = 'Vadym'
password = '123'
database = 'db_lab3'

OUTPUT_FILE_T = 'db_lab3_{}.csv'

TABLES = [
    'club',
    'contract',
    'match_player',
    'matches',
    'player',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])


