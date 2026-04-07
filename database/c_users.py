import sqlalchemy
import params as params

engine = sqlalchemy.create_engine(f'mariadb+mariadbconnector://{params.Username}:{params.Password}@{params.Host}:{params.Port}/{params.Dbname}')

class user:
    def __init__(self, name, description, valid_from, valid_to, year, value, created, updated):
        self.name = name
        self.description = description
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.year = year
        self.value = value
        self.created = created
        self.updated = updated

    def insert_to_db(self):
        stmt = sqlalchemy.text("INSERT INTO params(name, description, valid_from, valid_to, year, value, created, updated) VALUES (:name, :description, :valid_from, :valid_to, :year, :value, :created, :updated)")
        with engine.connect() as conn:
            conn.execute(stmt, name=self.name, description=self.description, valid_from=self.valid_from, valid_to=self.valid_to, year=self.year, value=self.value, created=self.created, updated=self.updated)
            conn.commit()
            return True
    
    def update_to_db(self, id):
        stmt = sqlalchemy.text("UPDATE params SET name=:name, description=:description, valid_from=:valid_from, valid_to=:valid_to, year=:year, value=:value, updated=:updated WHERE id=:id")
        with engine.connect() as conn:
            conn.execute(stmt, name=self.name, description=self.description, valid_from=self.valid_from, valid_to=self.valid_to, year=self.year, value=self.value, updated=self.updated, id=id)
            conn.commit()
            return True
        