# ---------------------- #
#  DROP TABLES           #
# ---------------------- #

drop_song_library = "DROP TABLE IF EXISTS song_library"
drop_user_library = "DROP TABLE IF EXISTS user_library"
drop_music_app_history = "DROP TABLE IF EXISTS music_app_history"

# ---------------------- #
#  CREATE TABLES         #
# ---------------------- #

create_song_library = """
    CREATE TABLE IF NOT EXISTS 
        song_library (
            session_id int,
            item_in_session int,
            artist text,
            song_title text,
            song_length float,
            PRIMARY KEY (session_id, item_in_session)
        )
"""

create_user_library = """
    CREATE TABLE IF NOT EXISTS 
        user_library (
            user_id int,
            session_id int,
            item_in_session int,
            artist text,
            song_title text,
            first_name text,
            last_name text,
            PRIMARY KEY (user_id, session_id, item_in_session)
        )
"""

create_music_app_history = """
    CREATE TABLE IF NOT EXISTS
        music_app_history (
            song_title text,
            user_id int,
            last_name text,
            first_name text,
            PRIMARY KEY (song_title, user_id)
        )
"""

# ---------------------- #
#  INSERT DATA           #
# ---------------------- #

insert_song_library = """
    INSERT INTO 
        song_library (
            session_id,
            item_in_session,
            artist,
            song_title,
            song_length
        )
        VALUES
        (%s, %s, %s, %s, %s)
"""

insert_user_library = """
    INSERT INTO
        user_library (
            user_id,
            session_id,
            item_in_session,
            artist,
            song_title,
            first_name,
            last_name
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s)
"""

insert_music_app_history = """
    INSERT INTO
        music_app_history (
            song_title,
            user_id,
            last_name,
            first_name
        )
        VALUES
        (%s, %s, %s, %s)
"""

# ---------------------- #
#  SELECT STATEMENTS     #
# ---------------------- #

select_song_library = """
    SELECT
        artist,
        song_title,
        song_length
    FROM
        song_library
    WHERE
        session_id = 338
    AND
        item_in_session = 4
"""

select_user_library = """
    SELECT
        artist,
        song_title,
        first_name,
        last_name
    FROM
        user_library
    WHERE
        user_id = 10
    AND
        session_id = 182
"""

select_music_app_history = """
    SELECT
        first_name, 
        last_name 
    FROM 
        music_app_history
    WHERE 
        song_title = 'All Hands Against His Own'
"""    

# ---------------------- #
#  QUERY LISTS           #
# ---------------------- #

create_table_queries = [create_song_library, create_user_library, create_music_app_history]
drop_table_queries = [drop_song_library, drop_user_library, drop_music_app_history]