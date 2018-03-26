from AdminInfo.UserType import UserType
from interface import implements,Interface
class StudentUser(implements(UserType)):
	def _factory_method(self):
		print('inside Student')