# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteTerminalAuthRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_name: List[int] = None,
    ):
        # {"en":"terminal auth name ", "zh_CN":"要删除的基础权限名称"}
        self.terminal_auth_name = terminal_auth_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        return self


class DeleteTerminalAuthContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_name: List[int] = None,
    ):
        # {"en":"terminal auth name ", "zh_CN":"要删除的基础权限名称"}
        self.terminal_auth_name = terminal_auth_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        return self


class DeleteTerminalAuthResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: DeleteTerminalAuthContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = DeleteTerminalAuthContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class DeleteTerminalAuthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteTerminalAuthParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteTerminalAuthRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class DeleteTerminalAuthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateRightsGroupsToUserOrUserGroupRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_names: List[str] = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
        action_type: int = None,
    ):
        # {"en":"List of base permission names", "zh_CN":"基础权限名称列表"}
        self.terminal_auth_names = terminal_auth_names
        # {"en":"List of authorized users", "zh_CN":"授权的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"List of authorized user group IDs", "zh_CN":"授权的用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids
        # {"en":"Action Type, 0: Append, 1: Overwrite", "zh_CN":"操作类型，0：追加，1：覆盖"}
        self.action_type = action_type

    def validate(self):
        self.validate_required(self.terminal_auth_names, 'terminal_auth_names')
        self.validate_required(self.action_type, 'action_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_names is not None:
            result['terminalAuthNames'] = self.terminal_auth_names
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        if self.action_type is not None:
            result['actionType'] = self.action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthNames') is not None:
            self.terminal_auth_names = m.get('terminalAuthNames')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        return self


class AssociateRightsGroupsToUserOrUserGroupResponse(TeaModel):
    def __init__(
        self,
        terminal_auth_names: List[str] = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
        action_type: int = None,
    ):
        # {"en":"List of base permission names", "zh_CN":"基础权限名称列表"}
        self.terminal_auth_names = terminal_auth_names
        # {"en":"List of authorized users", "zh_CN":"授权的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"List of authorized user group IDs", "zh_CN":"授权的用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids
        # {"en":"Action Type, 0: Append, 1: Overwrite", "zh_CN":"操作类型，0：追加，1：覆盖"}
        self.action_type = action_type

    def validate(self):
        self.validate_required(self.terminal_auth_names, 'terminal_auth_names')
        self.validate_required(self.action_type, 'action_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_names is not None:
            result['terminalAuthNames'] = self.terminal_auth_names
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        if self.action_type is not None:
            result['actionType'] = self.action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthNames') is not None:
            self.terminal_auth_names = m.get('terminalAuthNames')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        return self


class AssociateRightsGroupsToUserOrUserGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateRightsGroupsToUserOrUserGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateRightsGroupsToUserOrUserGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateRightsGroupsToUserOrUserGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateTerminalAuthRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        terminal_auth_name: str = None,
        enable_status: int = None,
        remark: str = None,
        authorized_resources: List[int] = None,
        authorized_users: List[int] = None,
        authorized_user_group_ids: List[int] = None,
        new_terminal_auth_name: str = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Terminal auth name of the specific auth.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Whether to enable the auth,1: enable 0: disable", "zh_CN":"是否启用该权限，1:启用0:禁用"}
        self.enable_status = enable_status
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"Associated application list", "zh_CN":"关联的应用列表"}
        self.authorized_resources = authorized_resources
        # {"en":"Associated user list", "zh_CN":"关联的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"关联的用户组列表ID"}
        self.authorized_user_group_ids = authorized_user_group_ids
        # {"en":"New terminal auth name of the specific auth.", "zh_CN":"新权限名称"}
        self.new_terminal_auth_name = new_terminal_auth_name

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.remark is not None:
            result['remark'] = self.remark
        if self.authorized_resources is not None:
            result['authorizedResources'] = self.authorized_resources
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        if self.new_terminal_auth_name is not None:
            result['newTerminalAuthName'] = self.new_terminal_auth_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('authorizedResources') is not None:
            self.authorized_resources = m.get('authorizedResources')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        if m.get('newTerminalAuthName') is not None:
            self.new_terminal_auth_name = m.get('newTerminalAuthName')
        return self


class UpdateTerminalAuthContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_name: str = None,
        enable_status: int = None,
        remark: str = None,
        authorized_resources: List[int] = None,
        authorized_users: List[int] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Whether to enable the user,1: enable 0: disable", "zh_CN":"是否启用用户，1:启用0:禁用"}
        self.enable_status = enable_status
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"Associated application list ", "zh_CN":"关联的应用列表"}
        self.authorized_resources = authorized_resources
        # {"en":"Associated user list", "zh_CN":"关联的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"关联的用户组列表ID"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')
        self.validate_required(self.enable_status, 'enable_status')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.remark is not None:
            result['remark'] = self.remark
        if self.authorized_resources is not None:
            result['authorizedResources'] = self.authorized_resources
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('authorizedResources') is not None:
            self.authorized_resources = m.get('authorizedResources')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class UpdateTerminalAuthResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: UpdateTerminalAuthContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = UpdateTerminalAuthContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class UpdateTerminalAuthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateTerminalAuthParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateTerminalAuthRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class UpdateTerminalAuthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTerminalAuthInfoRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthInfoResourceEntity(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        resource_id: List[int] = None,
    ):
        # {"en":"resource name", "zh_CN":"应用名称/资源名称"}
        self.resource_name = resource_name
        # {"en":"the resource id, "zh_CN":"应用ID"}
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class QueryTerminalAuthInfoUserEntity(TeaModel):
    def __init__(
        self,
        terminal_user_name: str = None,
        terminal_user_id: List[int] = None,
    ):
        # {"en":"terminal username", "zh_CN":"用户名称"}
        self.terminal_user_name = terminal_user_name
        # {"en":"the terminal user id, "zh_CN":"终端用户id"}
        self.terminal_user_id = terminal_user_id

    def validate(self):
        self.validate_required(self.terminal_user_name, 'terminal_user_name')
        self.validate_required(self.terminal_user_id, 'terminal_user_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_user_name is not None:
            result['terminalUserName'] = self.terminal_user_name
        if self.terminal_user_id is not None:
            result['terminalUserId'] = self.terminal_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalUserName') is not None:
            self.terminal_user_name = m.get('terminalUserName')
        if m.get('terminalUserId') is not None:
            self.terminal_user_id = m.get('terminalUserId')
        return self


class QueryTerminalAuthInfoGroupEntity(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        resourgroup_idce_id: List[int] = None,
    ):
        # {"en":"group name", "zh_CN":"用户组名称"}
        self.group_name = group_name
        # {"en":"the group id, "zh_CN":"用户组id"}
        self.resourgroup_idce_id = resourgroup_idce_id

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.resourgroup_idce_id, 'resourgroup_idce_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.resourgroup_idce_id is not None:
            result['resourgroupIdceId'] = self.resourgroup_idce_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('resourgroupIdceId') is not None:
            self.resourgroup_idce_id = m.get('resourgroupIdceId')
        return self


class QueryTerminalAuthInfoContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_name: str = None,
        relevant_resources: List[QueryTerminalAuthInfoResourceEntity] = None,
        remark: str = None,
        status: int = None,
        terminal_auth_id: int = None,
        authorized_users: List[QueryTerminalAuthInfoUserEntity] = None,
        authorized_user_groups: List[QueryTerminalAuthInfoGroupEntity] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Associated application list ", "zh_CN":"关联的应用列表"}
        self.relevant_resources = relevant_resources
        # {'en':'remark', 'zh_CN':'备注'}
        self.remark = remark
        # {"en":"The status of basic permissions", "zh_CN":"基础权限的状态 0 关闭 1 开启"}
        self.status = status
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated user list ", "zh_CN":"终端用户列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ", "zh_CN":"终端用户组列表"}
        self.authorized_user_groups = authorized_user_groups

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')
        self.validate_required(self.relevant_resources, 'relevant_resources')
        if self.relevant_resources:
            for k in self.relevant_resources:
                if k:
                    k.validate()
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.status, 'status')
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')
        if self.authorized_users:
            for k in self.authorized_users:
                if k:
                    k.validate()
        if self.authorized_user_groups:
            for k in self.authorized_user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.relevant_resources is not None:
            result['relevantResources'] = []
            for k in self.relevant_resources:
                result['relevantResources'].append(k.to_map() if k else None)
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.authorized_users is not None:
            result['authorizedUsers'] = []
            for k in self.authorized_users:
                result['authorizedUsers'].append(k.to_map() if k else None)
        if self.authorized_user_groups is not None:
            result['authorizedUserGroups'] = []
            for k in self.authorized_user_groups:
                result['authorizedUserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('relevantResources') is not None:
            self.relevant_resources = []
            for k in m.get('relevantResources'):
                temp_model = QueryTerminalAuthInfoResourceEntity()
                self.relevant_resources.append(temp_model.from_map(k))
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = []
            for k in m.get('authorizedUsers'):
                temp_model = QueryTerminalAuthInfoUserEntity()
                self.authorized_users.append(temp_model.from_map(k))
        if m.get('authorizedUserGroups') is not None:
            self.authorized_user_groups = []
            for k in m.get('authorizedUserGroups'):
                temp_model = QueryTerminalAuthInfoGroupEntity()
                self.authorized_user_groups.append(temp_model.from_map(k))
        return self


class QueryTerminalAuthInfoResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: QueryTerminalAuthInfoContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = QueryTerminalAuthInfoContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class QueryTerminalAuthInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthInfoParameters(TeaModel):
    def __init__(
        self,
        terminal_auth_name: int = None,
    ):
        # {"en":"terminal auth name.", "zh_CN":"基础权限的名称"}
        self.terminal_auth_name = terminal_auth_name

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        return self


class QueryTerminalAuthInfoRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class QueryTerminalAuthInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RemoveTerminalAuthUserOrGroupRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated user list ", "zh_CN":"终端用户名称列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"终端用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class RemoveTerminalAuthUserOrGroupContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated user list ", "zh_CN":"终端用户名称列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"终端用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class RemoveTerminalAuthUserOrGroupResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: RemoveTerminalAuthUserOrGroupContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = RemoveTerminalAuthUserOrGroupContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class RemoveTerminalAuthUserOrGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RemoveTerminalAuthUserOrGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RemoveTerminalAuthUserOrGroupRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class RemoveTerminalAuthUserOrGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTerminalAuthListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthListResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthListRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"UAC account name", "zh_CN":"UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class QueryTerminalAuthListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddTerminalAuthUserOrGroupRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated user list ", "zh_CN":"终端用户名称列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"终端用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AddTerminalAuthUserOrGroupContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated user list ", "zh_CN":"终端用户名称列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"终端用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AddTerminalAuthUserOrGroupResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: AddTerminalAuthUserOrGroupContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = AddTerminalAuthUserOrGroupContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class AddTerminalAuthUserOrGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTerminalAuthUserOrGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTerminalAuthUserOrGroupRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class AddTerminalAuthUserOrGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RemoveTerminalAuthResourceRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        relevant_resources: List[str] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated application list ID", "zh_CN":"关联的应用名称列表"}
        self.relevant_resources = relevant_resources

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.relevant_resources is not None:
            result['relevantResources'] = self.relevant_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('relevantResources') is not None:
            self.relevant_resources = m.get('relevantResources')
        return self


class RemoveTerminalAuthResourceContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        relevant_resources: List[str] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated application list ID", "zh_CN":"关联的应用名称列表}
        self.relevant_resources = relevant_resources

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.relevant_resources is not None:
            result['relevantResources'] = self.relevant_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('relevantResources') is not None:
            self.relevant_resources = m.get('relevantResources')
        return self


class RemoveTerminalAuthResourceResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: RemoveTerminalAuthResourceContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = RemoveTerminalAuthResourceContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class RemoveTerminalAuthResourcePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RemoveTerminalAuthResourceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RemoveTerminalAuthResourceRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class RemoveTerminalAuthResourceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTerminalUserGroupByAuthConfigRequest(TeaModel):
    def __init__(
        self,
        auth_config_name: str = None,
        group_name: str = None,
    ):
        # {"en":"the auth config name", "zh_CN":"身份源名称"}
        self.auth_config_name = auth_config_name
        # {"en":"terminal group name.", "zh_CN":"用户组名称"}
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config_name is not None:
            result['authConfigName'] = self.auth_config_name
        if self.group_name is not None:
            result['groupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfigName') is not None:
            self.auth_config_name = m.get('authConfigName')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        return self


class QueryTerminalUserGroupByAuthConfigContentEntityGroupList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        group_id: int = None,
        parent_group_name: str = None,
        parent_group_id: str = None,
        remark: str = None,
        create_time: int = None,
    ):
        # {'en':'groupName', 'zh_CN':'用户组名称'}
        self.group_name = group_name
        # {'en':'groupId', 'zh_CN':'用户组ID'}
        self.group_id = group_id
        # {'en':'parentGroupName', 'zh_CN':'父组名称'}
        self.parent_group_name = parent_group_name
        # {'en':'parentGroupID', 'zh_CN':'父组ID'}
        self.parent_group_id = parent_group_id
        # {'en':'remark', 'zh_CN':'备注'}
        self.remark = remark
        # {'en':'createTime', 'zh_CN':'创建时间'}
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.parent_group_name, 'parent_group_name')
        self.validate_required(self.parent_group_id, 'parent_group_id')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.parent_group_name is not None:
            result['parentGroupName'] = self.parent_group_name
        if self.parent_group_id is not None:
            result['parentGroupID'] = self.parent_group_id
        if self.remark is not None:
            result['remark'] = self.remark
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('parentGroupName') is not None:
            self.parent_group_name = m.get('parentGroupName')
        if m.get('parentGroupID') is not None:
            self.parent_group_id = m.get('parentGroupID')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class QueryTerminalUserGroupByAuthConfigContentEntity(TeaModel):
    def __init__(
        self,
        group_list: List[QueryTerminalUserGroupByAuthConfigContentEntityGroupList] = None,
    ):
        # {'en':'groupList', 'zh_CN':'group集合，下面为字段'}
        self.group_list = group_list

    def validate(self):
        self.validate_required(self.group_list, 'group_list')
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_list is not None:
            result['groupList'] = []
            for k in self.group_list:
                result['groupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupList') is not None:
            self.group_list = []
            for k in m.get('groupList'):
                temp_model = QueryTerminalUserGroupByAuthConfigContentEntityGroupList()
                self.group_list.append(temp_model.from_map(k))
        return self


class QueryTerminalUserGroupByAuthConfigResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: QueryTerminalUserGroupByAuthConfigContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = QueryTerminalUserGroupByAuthConfigContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class QueryTerminalUserGroupByAuthConfigPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalUserGroupByAuthConfigParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalUserGroupByAuthConfigRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class QueryTerminalUserGroupByAuthConfigResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateTerminalAuthRelatedResourcesRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_id: int = None,
        relevant_resources: List[str] = None,
    ):
        # {"en":"the identify of terminal auth.", "zh_CN":"基础权限的ID"}
        self.terminal_auth_id = terminal_auth_id
        # {"en":"Associated application list ID", "zh_CN":"关联的应用列表ID"}
        self.relevant_resources = relevant_resources

    def validate(self):
        self.validate_required(self.terminal_auth_id, 'terminal_auth_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_id is not None:
            result['terminalAuthId'] = self.terminal_auth_id
        if self.relevant_resources is not None:
            result['relevantResources'] = self.relevant_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthId') is not None:
            self.terminal_auth_id = m.get('terminalAuthId')
        if m.get('relevantResources') is not None:
            self.relevant_resources = m.get('relevantResources')
        return self


class UpdateTerminalAuthRelatedResourcesContentEntity(TeaModel):
    def __init__(
        self,
        terminal_auth_name: str = None,
        relevant_resources: List[str] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Associated application list ID", "zh_CN":"关联的应用列表ID"}
        self.relevant_resources = relevant_resources

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')
        self.validate_required(self.relevant_resources, 'relevant_resources')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.relevant_resources is not None:
            result['relevantResources'] = self.relevant_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('relevantResources') is not None:
            self.relevant_resources = m.get('relevantResources')
        return self


class UpdateTerminalAuthRelatedResourcesResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: UpdateTerminalAuthRelatedResourcesContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = UpdateTerminalAuthRelatedResourcesContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class UpdateTerminalAuthRelatedResourcesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateTerminalAuthRelatedResourcesParameters(TeaModel):
    def __init__(
        self,
        terminal_auth_name: str = None,
        relevant_resources: List[str] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Associated application list ID", "zh_CN":"关联的应用列表ID"}
        self.relevant_resources = relevant_resources

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')
        self.validate_required(self.relevant_resources, 'relevant_resources')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.relevant_resources is not None:
            result['relevantResources'] = self.relevant_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('relevantResources') is not None:
            self.relevant_resources = m.get('relevantResources')
        return self


class UpdateTerminalAuthRelatedResourcesRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"uac account name", "zh_CN":"当前企业的UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class UpdateTerminalAuthRelatedResourcesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTerminalAuthResourceListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthResourceListContentEntity(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        remark: List[str] = None,
        resource_id: List[int] = None,
    ):
        # {"en":"resource name", "zh_CN":"应用名称/资源名称"}
        self.resource_name = resource_name
        # {"en":"Description of the resource", "zh_CN":"备注"}
        self.remark = remark
        # {"en":"the resource id, "zh_CN":"应用ID"}
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class QueryTerminalAuthResourceListResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: QueryTerminalAuthResourceListContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = QueryTerminalAuthResourceListContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class QueryTerminalAuthResourceListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthResourceListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTerminalAuthResourceListRequestHeader(TeaModel):
    def __init__(
        self,
        auth_user: str = None,
    ):
        # {"en":"UAC account name", "zh_CN":"UAC主账号名"}
        self.auth_user = auth_user

    def validate(self):
        self.validate_required(self.auth_user, 'auth_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_user is not None:
            result['authUser'] = self.auth_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authUser') is not None:
            self.auth_user = m.get('authUser')
        return self


class QueryTerminalAuthResourceListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddTerminalAuthRequest(TeaModel):
    def __init__(
        self,
        terminal_auth_name: str = None,
        enable_status: int = None,
        remark: str = None,
        auth_resources: List[int] = None,
        authorized_users: List[int] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.terminal_auth_name = terminal_auth_name
        # {"en":"Whether to enable the user,1: enable 0: disable", "zh_CN":"是否启用该权限，1:启用0:禁用"}
        self.enable_status = enable_status
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"Associated application list ", "zh_CN":"关联的应用列表"}
        self.auth_resources = auth_resources
        # {"en":"Associated user list", "zh_CN":"关联的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"关联的用户组列表ID"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.terminal_auth_name, 'terminal_auth_name')
        self.validate_required(self.enable_status, 'enable_status')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.terminal_auth_name is not None:
            result['terminalAuthName'] = self.terminal_auth_name
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.remark is not None:
            result['remark'] = self.remark
        if self.auth_resources is not None:
            result['authResources'] = self.auth_resources
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('terminalAuthName') is not None:
            self.terminal_auth_name = m.get('terminalAuthName')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('authResources') is not None:
            self.auth_resources = m.get('authResources')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AddTerminalAuthContentEntity(TeaModel):
    def __init__(
        self,
        name: str = None,
        enable_status: int = None,
        remark: str = None,
        authorized_resources: List[int] = None,
        authorized_users: List[int] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"Username of the specific user.", "zh_CN":"权限名称"}
        self.name = name
        # {"en":"Whether to enable the user,1: enable 0: disable", "zh_CN":"是否启用用户，1:启用0:禁用"}
        self.enable_status = enable_status
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"Associated application list", "zh_CN":"关联的应用列表"}
        self.authorized_resources = authorized_resources
        # {"en":"Associated user list ", "zh_CN":"关联的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"Associated user group list ID", "zh_CN":"关联的用户组列表ID"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.enable_status, 'enable_status')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.remark is not None:
            result['remark'] = self.remark
        if self.authorized_resources is not None:
            result['authorizedResources'] = self.authorized_resources
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('authorizedResources') is not None:
            self.authorized_resources = m.get('authorizedResources')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AddTerminalAuthResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: AddTerminalAuthContentEntity = None,
    ):
        # {"en":"Interface error code, 0-fail,1-success", "zh_CN":"接口错误码，0-代表失败，1-代表成功"}
        self.return_code = return_code
        # {"en":"Error message", "zh_CN":"错误信息"}
        self.return_msg = return_msg
        # {"en":"content", "zh_CN":"数据，下面全是数据的内容"}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = AddTerminalAuthContentEntity()
            self.content = temp_model.from_map(m['content'])
        return self


class AddTerminalAuthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTerminalAuthParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTerminalAuthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTerminalAuthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




