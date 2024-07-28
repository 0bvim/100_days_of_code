class User:

	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		print(f"At position {self.id}: User {self.username} created.")


user_1 = User("001", "Stete")
user_2 = User("002", "Lila")
