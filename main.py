import psycopg2

username = 'Vadym'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
select
	club.club_name,
	count(club_id_one) as count_game 
from
	club
	join matches on club.club_id = matches.club_id_one
group by
	club.club_name;
'''
query_2 = '''
select 
    player.player_name,
    matches.match_date,
    match_player.goals as max_score
from 
    player
    join match_player using(player_id)
	join matches using(match_id)
where 
    match_player.goals = (select max(goals) from match_player);
'''

query_3 = '''
select 
    club.club_name,
    player.player_name,
    sum(contract.leave_date-contract.join_date) as days_left
from 
    club 
    join contract using (club_id)
	join player using(player_id)
group by 
    club.club_name, 
    player.player_name
order by 
    days_left;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")

    cur = conn.cursor()
    print('\nЗапит 1:')
    cur.execute(query_1)
    for row in cur:
        print(row)

    cur = conn.cursor()
    print('\nЗапит 2:')
    cur.execute(query_2)
    for row in cur:
        print(row)

    cur = conn.cursor()
    print('\nЗапит 3:')
    cur.execute(query_3)
    for row in cur:
        print(row)
