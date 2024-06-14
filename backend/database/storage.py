from typing import Union, List
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

"""
Note!!! SQLITE3 database getting locked Celery
database that has better support for multiple connections such as postgres or mysql, 
sqlite really isn't built up to do it and is more used for development where its very rare 
you'd have multiple concurrent connections
"""


class DatabaseRobota(object):
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseRobota, cls).__new__(cls, *args, **kwargs)
            cls._instance._connection = psycopg2.connect(
                dbname=DB_NAME, 
                user=DB_USER, 
                password=DB_PASSWORD,
                host=DB_HOST
            )
        return cls._instance
    
    def execute_task(self, price: int) -> Union[None, str]:
        
        if not isinstance(price, int):
            raise ValueError(f"Incorrect date type {price}")
            
        try:
            with self._connection:
                cursor = self._connection.cursor()
                
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Robota (
                        id SERIAL PRIMARY KEY,
                        vacancy_count INTEGER,
                        change INTEGER,
                        timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                
                cursor.execute(
                    """
                    INSERT INTO Robota (vacancy_count) VALUES (%s)
                    """, (price,)
                )
                
                cursor.execute(
                    """
                    SELECT id, vacancy_count FROM Robota WHERE id = (SELECT MAX(id) FROM Robota)
                    """
                )
                current_record = cursor.fetchone()

                if current_record:
                    current_id = current_record[0]
                    current_vacancy_count = current_record[1]
                    
                    cursor.execute(
                        """
                        SELECT vacancy_count FROM Robota
                        WHERE id < %s
                        ORDER BY id DESC
                        LIMIT 1
                        """, (current_id,)
                    )
                    previous_record = cursor.fetchone()
                    
                    if previous_record:
                        previous_vacancy_count = previous_record[0]
                        change = current_vacancy_count - previous_vacancy_count

                        cursor.execute(
                            """
                            UPDATE Robota SET change = %s
                            WHERE id = %s
                            """, (change, current_id)
                        )

            self._connection.commit()
            
        except psycopg2.Error as e:
            raise str(e)

        return None

            
    def retrieve_all(self) -> List[str]:
        try:
            with self._connection:
                cursor = self._connection.cursor()
                cursor.execute(
                    """
                    SELECT vacancy_count, change, 
                    to_char(timestamp, 'DD.MM.YYYY HH24:MI:SS') as formatted_timestamp 
                    FROM Robota
                    """
                )
                rows = cursor.fetchall()
                return rows
        except psycopg2.Error as e:
            return str(e)