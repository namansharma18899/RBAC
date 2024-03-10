class Max_Role_Assignment_Count_Reached_Exception(Exception):
    def __init__(self, max_role_assg_count: int, *args) -> None:
        self.message = f'Max Role Assignment Count Reached {max_role_assg_count}' 
        super(Max_Role_Assignment_Count_Reached_Exception, self).__init__(self.message,*args)