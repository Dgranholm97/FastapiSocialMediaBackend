from sqlmodel import SQLModel, create_engine, Session, or_, select, col

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url, echo=True)   

def create_db_and_tables():   
    SQLModel.metadata.create_all(engine)  
    print("Database and tables created!")

if __name__ == "__main__":  
    create_db_and_tables()