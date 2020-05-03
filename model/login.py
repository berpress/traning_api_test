import faker


class UserData:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    def random_user():
        fake = faker.Faker()
        return UserData(username=fake.email(), password=fake.password())
