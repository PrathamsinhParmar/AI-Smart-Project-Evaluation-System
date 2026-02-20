from app.database.connection import Base, engine
from app.models import evaluation, project, user  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
