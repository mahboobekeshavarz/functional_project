class BaseException(Exception):
	pass

class UsernameException(BaseException):
	def __init__(self, message='you cant choose admin as username'):
		self.message = message
		super().__init__(self.message)

class PasswordException(BaseException):
	def __init__(self, message='the length of password must be at least 3!'):
		self.message = message
		super().__init__(self.message)

