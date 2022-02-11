import dataclasses
import psycopg2


@dataclasses.dataclass
class ConnectionData:
    host: str
    port: int
    dbname: str
    user: str
    password: str


class PostgreSQL:
    def __init__(self, connection_data: ConnectionData):
        self.connection_data = connection_data
        self.conn = psycopg2.connect(**connection_data.__dict__)

    def __del__(self):
        del self.conn
