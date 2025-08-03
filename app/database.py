from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.meta = MetaData()
        self.meta.reflect(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def insert_batch(self, records, batch_size=10):
        conn = self.engine.connect()
        trademarks = self.meta.tables['trademarks']
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            try:
                conn.execute(trademarks.insert(), batch)
            except Exception as e:
                print(f"DB Insert Error: {e}")
        conn.close()
