class Users():

	"""An empty list that holds all users"""
	user = []


	def __init__(self, name, email, password, roles):
		self.name = name
		self.email = email
		self.password = password
		self.roles = roles



	def _save(self, user):
		self.user.append(user)

		
		
class Admin(Users):
	def __init__(self, name, email, password, roles):
		super().__init__(name=name, email=email, password=password, roles=roles)
		self.roles = Admin

	def _delete(self, user):
		self.user.remove(user)



class Contributor(Users):
	def __init__(self, name, email, password, roles):
		super().__init__(name=name, email=email, password=password, roles=roles)
		self.roles = Contributor

