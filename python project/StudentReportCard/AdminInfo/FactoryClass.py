from AdminInfo.AdminUser import AdminUser
from AdminInfo.StudentUser import StudentUser
class factory_object_creator(AdminUser,StudentUser):
	def getType(self,object_type):
			if(object_type == 'admin'):
				print('hello admin')
				return AdminUser()
			else:
				print('hello student')
				return StudentUser()