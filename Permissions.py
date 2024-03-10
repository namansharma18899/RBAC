import random


class Permission:
    def __init__(self, name) -> None:
        self.id : str= f"{random.randrange(10000,20900)}"
        self.name = name
        self.disable = False
    
    def disable_permission(self):
        self.enable = True

list_user_info_perm = Permission('AWSListUserInfo')
put_perm = Permission('AWSPutObject')
list_perm = Permission('AWSListObject')
get_perm = Permission('AWSGetObject')