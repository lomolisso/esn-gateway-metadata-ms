from app.db import Base, engine, SessionLocal
from app.db.crud import read_edge_sensors

def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    print(read_edge_sensors(session=session))

    session.close()


if __name__ == "__main__":
    main()
