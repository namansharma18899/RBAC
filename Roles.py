from Permissions import Permission, put_perm, get_perm, list_perm, list_user_info_perm


class Role:
    def __init__(self, name: str) -> None:
        self.name = name
        self.permissions: dict = {}

    def add_permission(self, permisison: Permission):
        self.permissions[permisison.name] = True

    def remove_permission(self, permisison: Permission):
        self.permissions.pop(permisison.name)


class DefaultPermissionLessUserRole(Role):
    def __init__(self) -> None:
        super().__init__(name="DefaultUser")
        super().add_permission(permisison=list_user_info_perm)

    def add_permission(self, permisison: Permission):
        # No Concrete Implementation
        pass

class AwsS3Role(Role):
    def __init__(self) -> None:
        super().__init__(name="AwsS3User")
        super().add_permission(permisison=list_user_info_perm)
        super().add_permission(list_perm)
        super().add_permission(get_perm)
        super().add_permission(put_perm)

    def add_permission(self, permisison: Permission):
        pass # No Concrete Implementation

    def remove_permission(self, permisison: Permission):
        pass # return super().remove_permission(permisison)