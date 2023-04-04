
# The Class To Create A User Object
class User:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def user_detail(self):
        print(
            f"""
Name: {self.name}
Age: {self.age}
Gender: {self.gender}
            """
        )

