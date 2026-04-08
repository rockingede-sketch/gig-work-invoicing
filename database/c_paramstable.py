from os import name
import sqlalchemy
import params as params

engine = sqlalchemy.create_engine(f'mariadb+mariadbconnector://{params.Username}:{params.Password}@{params.Host}:{params.Port}/{params.Dbname}')
metadata = sqlalchemy.MetaData()
paramstable = sqlalchemy.Table('paramstable', metadata, autoload_with=engine)

class Paramstable:
    def __init__(self, name, description, valid_from, valid_to, year, value, created, updated):
        self.name = name
        self.description = description
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.year = year
        self.value = value
        self.created = created
        self.updated = updated

    def insert_to_db(self, p):
        #print(self.name, self.description, self.valid_from, self.valid_to, self.year, self.value, self.created, self.updated)
        stmt = sqlalchemy.insert(paramstable).values(
            name=self.name, 
            description=self.description, 
            valid_from=self.valid_from, 
            valid_to=self.valid_to, 
            year=self.year, 
            value=self.value, 
            created=self.created, 
            updated=self.updated)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            return True
    
    def update_to_db(self, p):
        #stmt = sqlalchemy.text("UPDATE params SET name=:name, description=:description, valid_from=:valid_from, valid_to=:valid_to, year=:year, value=:value, updated=:updated WHERE id=:id")
        stmt = sqlalchemy.update(paramstable).values(name=self.name, description=self.description, valid_from=self.valid_from, valid_to=self.valid_to, year=self.year, value=self.value, updated=self.updated).where(paramstable.id == self.id)
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            return True
        