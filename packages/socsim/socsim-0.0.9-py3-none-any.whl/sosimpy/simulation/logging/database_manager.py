import os
import sqlite3
import json
from typing import Tuple, List, Union


class SimLogger:
    def __init__(self, log_directory: str, buffer_size: int = 50):
        """
        :param log_directory: Directory path where the logs.db is stored or created.
        :param buffer_size: The number of records to accumulate in-memory before flushing to DB.
        """
        os.makedirs(log_directory, exist_ok=True)
        self.db_path = os.path.join(log_directory, "logs.db")
        self.buffer_size = buffer_size
        self._initialize_db()

        # Buffers for different types of logs
        self._agent_log_buffer = []
        self._conversation_log_buffer = []
        self._metric_log_buffer = []
        self._agent_properties_buffer = []

    def _initialize_db(self):
        """Creates necessary tables if they do not exist."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AgentLog (
            agent_id INT,
            iter_idx INT,
            location_x INT,
            location_y INT,
            latent_attributes TEXT,
            questionnaire_r TEXT,
            agent_history TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AgentProperties (
            agent_id INT PRIMARY KEY,
            age INT,
            gender TEXT,
            location TEXT,
            urbanicity TEXT,
            ethnicity TEXT,
            education TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ConversationLog (
            id TEXT PRIMARY KEY,
            conv_member_1 INT,
            conv_member_2 INT,
            iteration_idx INT,
            question TEXT,
            reply TEXT,
            final_response TEXT,
            agreement_score INT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS MetricLog (
            iter_idx INT,
            metric_name TEXT,
            metric TEXT
        );
        """)

        connection.commit()
        connection.close()

    def insert_agent_log(self,
                         agent_id: int,
                         iter_idx: int,
                         location: Tuple[float, float],
                         questionnaire_responses: List[str],
                         latent_attributes: List[Union[int, float]],
                         agent_history: str):
        """
        Buffer an AgentLog record in memory, and flush if the buffer is full.
        """
        self._agent_log_buffer.append((
            agent_id,
            iter_idx,
            location[0],
            location[1],
            json.dumps(questionnaire_responses),
            json.dumps(latent_attributes),
            agent_history
        ))

        # Flush if buffer is full
        if len(self._agent_log_buffer) >= self.buffer_size:
            self._flush_agent_log()

    def insert_conversation_log(self,
                                id: str,
                                conv_pair: Tuple[int, int],
                                iteration_idx: int,
                                question: str,
                                reply: str,
                                final_response: str,
                                agreement_score: int):
        """
        Buffer a ConversationLog record in memory, and flush if the buffer is full.
        """
        self._conversation_log_buffer.append((
            id,
            conv_pair[0],
            conv_pair[1],
            iteration_idx,
            question,
            reply,
            final_response,
            agreement_score
        ))

        # Flush if buffer is full
        if len(self._conversation_log_buffer) >= self.buffer_size:
            self._flush_conversation_log()

    def insert_metric_log(self,
                          iter_idx: int,
                          metric_name: List[str],
                          metric: List[float]):
        """
        Buffer a MetricLog record in memory, and flush if the buffer is full.
        """
        self._metric_log_buffer.append((
            iter_idx,
            json.dumps(metric_name),
            json.dumps(metric)
        ))

        # Flush if buffer is full
        if len(self._metric_log_buffer) >= self.buffer_size:
            self._flush_metric_log()

    def insert_agent_properties(self,
                                agent_id: int,
                                age: int,
                                gender: str,
                                location: str,
                                urbanicity: str,
                                ethnicity: str,
                                education: str):
        """
        Buffer an AgentProperties record in memory, and flush if the buffer is full.
        """
        self._agent_properties_buffer.append((
            agent_id,
            age,
            gender,
            location,
            urbanicity,
            ethnicity,
            education
        ))

        # Flush if buffer is full
        if len(self._agent_properties_buffer) >= self.buffer_size:
            self._flush_agent_properties()

    def _flush_agent_log(self):
        """Flush all buffered AgentLog records to the database."""
        if not self._agent_log_buffer:
            return

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        sql = """
            INSERT INTO AgentLog
            (agent_id, iter_idx, location_x, location_y, questionnaire_r, latent_attributes, agent_history)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.executemany(sql, self._agent_log_buffer)

        connection.commit()
        connection.close()

        # Clear the buffer after flushing
        self._agent_log_buffer.clear()

    def _flush_conversation_log(self):
        """Flush all buffered ConversationLog records to the database."""
        if not self._conversation_log_buffer:
            return

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        sql = """
            INSERT INTO ConversationLog
            (id, conv_member_1, conv_member_2, iteration_idx, question, reply, final_response, agreement_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.executemany(sql, self._conversation_log_buffer)

        connection.commit()
        connection.close()

        # Clear the buffer after flushing
        self._conversation_log_buffer.clear()

    def _flush_metric_log(self):
        """Flush all buffered MetricLog records to the database."""
        if not self._metric_log_buffer:
            return

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        sql = """
            INSERT INTO MetricLog
            (iter_idx, metric_name, metric) 
            VALUES (?, ?, ?)
        """
        cursor.executemany(sql, self._metric_log_buffer)

        connection.commit()
        connection.close()

        # Clear the buffer after flushing
        self._metric_log_buffer.clear()

    def _flush_agent_properties(self):
        """Flush all buffered AgentProperties records to the database."""
        if not self._agent_properties_buffer:
            return

        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        sql = """
            INSERT INTO AgentProperties
            (agent_id, age, gender, location, urbanicity, ethnicity, education)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.executemany(sql, self._agent_properties_buffer)

        connection.commit()
        connection.close()

        # Clear the buffer after flushing
        self._agent_properties_buffer.clear()

    def flush_all(self):
        """
        Manually flush all buffers at once.
        Call this if you want to ensure everything is written right away.
        """
        self._flush_agent_log()
        self._flush_conversation_log()
        self._flush_metric_log()
        self._flush_agent_properties()

    def __del__(self):
        """
        Attempt to flush any remaining data when the object is about to be destroyed.
        In practice, it's better to call .flush_all() or have a context manager
        to ensure flushing is always done reliably.
        """
        try:
            self.flush_all()
        except Exception as e:
            # If there's an error on shutdown, we can log/ignore it here.
            pass