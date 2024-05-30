import psycopg2
import matplotlib.pyplot as plt

username = 'Vadym'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
-- Це для завдання №3 (VIEW)
create view ClubsGames as
-- Сам запит
select
	club.club_name,
	count(club_id_one) as count_game 
from
	club
	join matches on club.club_id = matches.club_id_one
group by
	club.club_name;
'''

# Додатковий для запиту №2
# Вивести гравця і матч, у якому забив більше за всіх голів.
query_4 = '''
-- Це для завдання №3 (VIEW)
create view PlayersScores as
-- Сам запит
select 
    player.player_name,
    sum(match_player.goals) as max_score
from 
    player
    join match_player using(player_id)
	join matches using(match_id)
where
	not match_player.goals = 0
group by
	player.player_name;
'''

# Додатковий для запиту №3
# Вивести гравців, у яких підраховано кількість днів до закінчення контракту.
query_5 = '''
-- Це для завдання №3 (VIEW)
create view PlayersDays as
-- Сам запит
select 
    player.player_name,
    sum(contract.leave_date-contract.join_date) as days_left
from 
    club 
    join contract using (club_id)
	join player using(player_id)
group by 
    player.player_name
having
    sum(contract.leave_date-contract.join_date) >= 1750
order by 
    days_left;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    # Графік №1
    # Це завдання під номером №3 (VIEW)
    cur.execute('DROP VIEW IF EXISTS ClubsGames')

    cur.execute(query_1)

    # Це завдання під номером №3 (VIEW)
    cur.execute('SELECT * FROM ClubsGames')

    Club_id_one = []
    count_game = []

    for row in cur:
        Club_id_one.append(row[0])
        count_game.append(row[1])

    # типи графіків
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    # змінні що входят в графік №1
    bar = bar_ax.bar(Club_id_one, count_game, label='Total')
    bar_ax.set_title('Кількість зіграних матчів у клубів')
    bar_ax.set_xlabel('Клуби')
    bar_ax.set_ylabel('Кількість матчів')

    # Графік №2
    # Це завдання під номером №3 (VIEW)
    cur.execute('DROP VIEW IF EXISTS PlayersScores')

    cur.execute(query_4)

    # Це завдання під номером №3 (VIEW)
    cur.execute('SELECT * FROM PlayersScores')

    Player_name = []
    max_score = []

    for row in cur:
        Player_name.append(row[0])
        max_score.append(row[1])

    # змінні що входят в графік №2
    pie_ax.pie(max_score, labels=Player_name, autopct='%1.1f%%')
    pie_ax.set_title('Гравці з максимальним забитими голами')

    # Графік №3
    # Це завдання під номером №3 (VIEW)
    cur.execute('DROP VIEW IF EXISTS PlayersDays')

    cur.execute(query_5)

    # Це завдання під номером №3 (VIEW)
    cur.execute('SELECT * FROM PlayersDays')

    Player_name = []
    days_left = []

    for row in cur:
        Player_name.append(row[0])
        days_left.append(row[1])

    # змінні що входят в графік №3
    graph_ax.plot(Player_name, days_left, marker='o')
    graph_ax.set_title('Кількість днів до закінчення контракту у гравців')
    graph_ax.set_xlabel('Гравці')
    graph_ax.set_ylabel('Кількість днів')

# розміри вікна з графіками
mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
