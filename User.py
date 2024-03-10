from Exceptions import Max_Role_Assignment_Count_Reached_Exception
from Roles import Role, AwsS3Role, DefaultPermissionLessUserRole

class User:
    Max_Role_Assignment_Count = 0
    def __init__(self, name: str) -> None:
        self.name = name
        self.roles : set = {DefaultPermissionLessUserRole()}

    
    def add_role(self, role: Role):
        if len(self.roles)>= User.Max_Role_Assignment_Count:
            raise Max_Role_Assignment_Count_Reached_Exception(max_role_assg_count=User.Max_Role_Assignment_Count)
        self.roles.add(role)