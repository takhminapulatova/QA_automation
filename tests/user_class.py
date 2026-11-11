class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
    def introduce(self):
        print("Hello my username is", self.username)
    def __str__(self) -> str:
        return f"{self.username}, age {self.age}"

class Admin(User):
    def introduce(self):
        print("Hello, I am an admin:", self.username)

user1 = User("tomsmith", 30)
user2 = User("admin", 33)
print(user1.username, user1.age)
print(user2.username, user2.age)

user1.introduce()
user2.introduce()

admin = Admin("superadmin", 35)
admin.introduce()

print(user1)
print(user2)

# class User:
#     pass
# user1 = User()
# user1.username = "tomsmith"
# print(user1.username)
#
# user2 = User()
# user2.username = "admin"
# print(user2.username)
