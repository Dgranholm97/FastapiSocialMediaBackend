from sqlmodel import SQLModel, create_engine, Session, or_, select, col

from typing import Optional

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url, echo=True)   

def create_db_and_tables():   
    SQLModel.metadata.create_all(engine)  
    print("Database and tables created!")


from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlmodel import SQLModel

#@as_declarative()
class Base(SQLModel):
    id: Optional[int]


# From https://stackoverflow.com/questions/70138641/using-sqlalchemy-declarative-base-with-sql-model
# # Declarative base object
# Base = declarative_base()
# SQLModel.metadata = Base.metadata

# # Table declaration....

# SQLModel.metadata.create_all(engine)



if __name__ == "__main__":  
    create_db_and_tables()