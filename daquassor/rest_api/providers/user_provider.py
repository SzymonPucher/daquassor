from typing import List

import sqlalchemy.exc
from sqlmodel import create_engine, Session, select

from daquassor.rest_api.models.user import User


class UserProvider:
    def __init__(self, db_connection_url: str):
        self.engine = create_engine(db_connection_url)

    def get_users(self) -> List[User]:
        with Session(self.engine) as session:
            return session.exec(select(User)).all()

    def get_user(self, email: str) -> User:
        with Session(self.engine) as session:
            return session.exec(select(User).where(User.email == email)).one()

    def add_user(self, user: User) -> None:
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

    def update_user(self, user: User) -> None:
        with Session(self.engine) as session:
            db_user = self.get_user(user.email)
            db_user.update_from_obj(user)
            session.add(db_user)
            try:
                session.commit()
            except sqlalchemy.exc.IntegrityError as e:
                raise ValueError(str(e))

    def delete_user(self, user_id: str) -> None:
        with Session(self.engine) as session:
            db_user = self.get_user(user_id)
            session.delete(db_user)
            session.commit()
