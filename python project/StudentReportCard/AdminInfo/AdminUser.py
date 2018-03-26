from interface import implements,Interface
from AdminInfo.UserType import UserType
class AdminUser(implements(UserType)):
	def _factory_method(self):
		print('inside Admin')