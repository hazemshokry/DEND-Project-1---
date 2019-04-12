# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY, title VARCHAR, artist_id VARCHAR, year INT, duration numeric(10,5))
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, name VARCHAR, location VARCHAR, 
lattitude VARCHAR, longitude VARCHAR)
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL , start_time DECIMAL NOT NULL, user_id INT NOT NULL, level VARCHAR, song_id VARCHAR, 
artist_id VARCHAR, session_id INT, location VARCHAR, user_agent VARCHAR)
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, first_name VARCHAR, last_name VARCHAR,
gender VARCHAR, level VARCHAR)

""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS times (ts TIMESTAMP PRIMARY KEY, hour INT, day INT, week INT, month INT, 
year INT, weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id , artist_id, session_id,
location, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) ;

""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (
%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE SET title=EXCLUDED.title, artist_id=EXCLUDED.artist_id, year=EXCLUDED.year, duration=EXCLUDED.duration ;
""")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (
%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO UPDATE SET name=EXCLUDED.name, location=EXCLUDED.location, lattitude=EXCLUDED.lattitude, longitude=EXCLUDED.longitude  ;
""")


time_table_insert = ("""INSERT INTO times (ts, hour, day, week, month, year, weekday) VALUES (
%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (ts) DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT a.song_id,b.artist_id FROM songs a LEFT JOIN artists b ON a.artist_id = b.artist_id 
WHERE title = %s AND name = %s AND duration = %s
""")

# QUERY LISTS

create_table_queries = [song_table_create, artist_table_create, songplay_table_create, user_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]