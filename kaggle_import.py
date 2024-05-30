import csv
import psycopg2

username = 'Vadym'
password = '123'
database = 'db_lab3'

INPUT_CSV_FILE_1 = 'clubs.csv'
INPUT_CSV_FILE_2 = 'players.csv'
INPUT_CSV_FILE_3 = 'matches.csv'
INPUT_CSV_FILE_4 = 'contracts.csv'
INPUT_CSV_FILE_5 = 'match_stat.csv'

query_01 = '''
DELETE FROM club;
'''

query_02 = '''
DELETE FROM player;
'''

query_03 = '''
DELETE FROM matches;
'''

query_04 = '''
DELETE FROM contract;
'''

query_05 = '''
DELETE FROM match_player;
'''

query_1 = '''
INSERT INTO club (Club_id, Club_name) VALUES (%s, %s)
'''

query_2 = '''
INSERT INTO player (Player_id, Player_name) VALUES (%s, %s)
'''

query_3 = '''
INSERT INTO matches (match_id, match_date, club_id_one, clud_id_two) VALUES (%s, %s, %s, %s)
'''

query_4 = '''
INSERT INTO contract (player_id, club_id, join_date, leave_date, position_primary)
VALUES (%s, %s, %s, %s, %s)
'''

query_5 = '''
INSERT INTO match_player (match_id, player_id, goals, assits, saved, fouls, minutes_played)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_05)
    cur.execute(query_04)
    cur.execute(query_03)
    cur.execute(query_02)
    cur.execute(query_01)
    # перший файл csv
    with open(INPUT_CSV_FILE_1, 'r') as file_r:
        reader = csv.DictReader(file_r)
        for idx, row in enumerate(reader):
            print(idx)
            # кажний row це колонка з файлу csv
            values = (row['Serial'], row['Club'])
            cur.execute(query_1, values)

    # другий файл csv
    with open(INPUT_CSV_FILE_2, 'r') as file_r:
        reader = csv.DictReader(file_r)
        for idx, row in enumerate(reader):
            print(idx)
            # кажний row це колонка з файлу csv
            values = (row['Serial'], row['Player'])
            cur.execute(query_2, values)

    # третій файл csv
    with open(INPUT_CSV_FILE_3, 'r') as file_r:
        reader = csv.DictReader(file_r)
        for idx, row in enumerate(reader):
            print(idx)
            # кажний row це колонка з файлу csv
            values = (row['Serial'], row['Match_day'], row['Club_Home'], row['Club_Guest'])
            cur.execute(query_3, values)

    # четвертий файл csv
    with open(INPUT_CSV_FILE_4, 'r') as file_r:
        reader = csv.DictReader(file_r)
        for idx, row in enumerate(reader):
            print(idx)
            # кажний row це колонка з файлу csv
            values = (row['player_id'], row['club_id'], row['join_date'], row['leave_date'], row['position_primary'])
            cur.execute(query_4, values)

    # пятий файл csv
    with open(INPUT_CSV_FILE_5, 'r') as file_r:
        reader = csv.DictReader(file_r)
        for idx, row in enumerate(reader):
            print(idx)
            # кажний row це колонка з файлу csv
            values = (row['match_id'], row['player_id'], row['goals'], row['assits'],
                      row['saved'], row['fouls'], row['minutes_played'])
            cur.execute(query_5, values)

    conn.commit()
