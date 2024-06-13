from typing import Union, List
import sqlite3

class DatabaseRobota(object):
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseRobota, cls).__new__(cls, *args, **kwargs)
            cls._instance._connection = sqlite3.connect("mustage.db")
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
                        id INTEGER PRIMARY KEY,
                        vacancy_count INTEGER DEFAULT 0,
                        change INTEGER DEFAULT 0,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                
                cursor.execute(
                    """
                    INSERT INTO Robota (vacancy_count) VALUES (?)
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
                        WHERE id < ?
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
                            UPDATE Robota SET change = ?
                            WHERE id = ?
                            """, (change, current_id)
                        )

            self._connection.commit()
            
        except sqlite3.Error as e:
            return str(e)

        return None

            
    def retrieve_all(self) -> List[str]:
        try:
            with self._connection:
                cursor = self._connection.cursor()
                cursor.execute(
                    """
                    SELECT vacancy_count, change, 
                    strftime('%d.%m.%Y %H:%M:%S', timestamp) as formatted_timestamp 
                    FROM Robota
                    """
                )
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as e:
            return str(e)
        