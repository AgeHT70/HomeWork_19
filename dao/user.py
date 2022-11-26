from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username ==
                                               username).first()

    def create(self, user_d):
        new_user = User(**user_d)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        user.name = user_d.get("name")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
