from .Logging import Debug
from .SnowflakeIntegration import SnowflakeIntegration

class SnowflakeLogging:
    """Handles task logging to snowflake."""

    def __init__():
        pass

    @staticmethod
    def write_log(task_id: str, task_name: str, task_status: str, task_message: str, verbose: bool = False):
        """Writes a log entry to Snowflake.

        Args:
            task_id (str): The task ID to associate with the log entry.
            task_name (str): The name of the task.
            task_status (str): The status of the task.
            task_message (str): The message to log.
            verbose (bool, optional): set True to enable DEBUG output. Defaults to False.
        """
        conn = SnowflakeIntegration.connect(profile="snowforge", verbose=verbose)
        cur = conn.cursor()

        try:
            cur.execute(f"INSERT INTO TASK_LOGS (TASK_ID, TASK_NAME, TASK_STATUS, TASK_MESSAGE) VALUES ('{task_id}', '{task_name}', '{task_status}', '{task_message}')")
            conn.commit()
            Debug.log(f"Successfully wrote log entry for task '{task_name}' with status '{task_status}' to Snowflake.", 'INFO', verbose)
        except Exception as e:
            conn.rollback()
            Debug.log(f"Error writing log entry for task '{task_name}' with status '{task_status}' to Snowflake.\n{e}", 'ERROR')
        finally:
            cur.close()
            conn.close()
            Debug.log("Connection to Snowflake closed.", 'DEBUG', verbose)