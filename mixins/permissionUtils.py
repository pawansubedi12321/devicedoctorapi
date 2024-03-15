from userpanel.models.rolesModel import Permission, Role, RolePermission
from mixins.urlMapper import PermissionManager


def update_permission():
    """
    Updates the permissions in the system.

    Deletes all existing permissions and role permissions, and creates new ones based on the current
    PermissionMap defined in the PermissionManager. Each role is created or retrieved from the database,
    and each permission in the PermissionMap is created or retrieved from the database and assigned to
    the role as a RolePermission.

    Returns:
        None
    """
    Permission.objects.all().delete()
    RolePermission.objects.all().delete()
    pm = PermissionManager()
    permisisons_map = pm.get_permission_map()
    for role, permission in permisisons_map.items():
        role_obj, _ = Role.objects.get_or_create(name=role)
        permission_routes = flatten_list(permission)
        for each_permission in permission_routes:
            permission_obj, _ = Permission.objects.get_or_create(
                route=each_permission[0],
                method=each_permission[1],
                name=f"can_{each_permission[1]}_{each_permission[0]}",
            )
            RolePermission.objects.get_or_create(
                role=role_obj, permission=permission_obj
            )


def flatten_list(nested_list):
    """
    Convert a nested list to a single list by flattening all sublists.

    Args:
        nested_list (list): The nested list to be flattened.

    Returns:
        list: A flattened version of the input list.
    """
    final_list = []
    for each in nested_list:
        if not isinstance(each, list):
            final_list.append(each)
            continue

        final_list.extend(flatten_list(each))
    return final_list
