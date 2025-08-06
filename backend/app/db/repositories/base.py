from databases import Database


class BaseRepository(Database):
    def __init__(self, db: Database) -> None:
        self.db = db
