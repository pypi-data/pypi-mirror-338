# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class CreateAppRequestDebugFingerprintList(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        desc: str = None,
    ):
        # {"en":"Fingerprint, with a total length not exceeding 100, containing only colons, letters A to F in both uppercase and lowercase, and digits 0 to 9. After removing colons, the length should be between 32 and 64.","zh_CN":"指纹，总长度不超过100，仅包含冒号、A~F大小写字母和0~9的数字，去除冒号后长度介于32~64之间。"}
        self.fingerprint = fingerprint
        # {"en":"Description, no more than 60 characters.","zh_CN":"描述，长度不超过60。"}
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        debug_fingerprint_list: List[CreateAppRequestDebugFingerprintList] = None,
        name: str = None,
        fingerprint: str = None,
        package_name: str = None,
        type: int = None,
        platform: str = None,
    ):
        # {"en":"Debug fingerprint, only applicable to Android. If it matches the production fingerprint, it can be left blank.","zh_CN":"调试指纹，仅对Android生效，如果与正式指纹一致可不填写。"}
        self.debug_fingerprint_list = debug_fingerprint_list
        # {"en":"Application name should not exceed 60 characters and does not support characters ',\",<,>,&,/.","zh_CN":"应用名称，长度不超过60，不支持字符',\",<,>,&,/。"}
        self.name = name
        # {"en":"Official fingerprint, mandatory for Android applications. Please ensure this is the fingerprint for the officially launched application, otherwise authentication will fail and the service cannot be activated. You can check with technical support for the method to obtain the fingerprint. The total length should not exceed 100 characters and must include colons, uppercase and lowercase letters from A to F, and numbers from 0 to 9. After removing the colons, the length should be between 32 and 64.","zh_CN":"正式指纹，Android应用必填，请确保该指纹为正式上线应用的指纹，否则将鉴权失败无法启用服务。获取指纹方法可找技术支持确认。总长度不超过100，仅包含冒号、A~F大小写字母和0~9的数字，去除冒号后长度介于32~64之间。"}
        self.fingerprint = fingerprint
        # {"en":"Please fill in the carefully; otherwise, it will not be usable. The length must be between 3 and 100 characters, consisting of letters, numbers, underscores, and hyphens, with sections of the package name separated by periods. Format example: com.maa.test.","zh_CN":"包名，请认真填写包名，否则将无法使用。长度必须在 3 到 100 个字符之间，并且由字母、数字、下划线和连字符组成，包名的各部分之间用点号分隔。格式如：com.maa.test。"}
        self.package_name = package_name
        # {"dictionary":"belong=MAA-masp-portal-console|dict=AppType","en":"Application Type.","zh_CN":"应用类型。"}
        self.type = type
        # {"en":"Application Platform, Android or iOS.","zh_CN":"应用平台，Android、iOS。"}
        self.platform = platform

    def validate(self):
        if self.debug_fingerprint_list:
            for k in self.debug_fingerprint_list:
                if k:
                    k.validate()
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.platform, 'platform')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_fingerprint_list is not None:
            result['debugFingerprintList'] = []
            for k in self.debug_fingerprint_list:
                result['debugFingerprintList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.package_name is not None:
            result['packageName'] = self.package_name
        if self.type is not None:
            result['type'] = self.type
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debugFingerprintList') is not None:
            self.debug_fingerprint_list = []
            for k in m.get('debugFingerprintList'):
                temp_model = CreateAppRequestDebugFingerprintList()
                self.debug_fingerprint_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('packageName') is not None:
            self.package_name = m.get('packageName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class CreateAppRequestHeader(TeaModel):
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


class CreateAppPaths(TeaModel):
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


class CreateAppParameters(TeaModel):
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


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
    ):
        # {"dictionary":"belong=MAA-masp-portal-console|dict=wplus_code","en":"Response Code","zh_CN":"响应码"}
        self.code = code
        # {"en":"Return data, Application ID","zh_CN":"返回数据，应用ID"}
        self.data = data
        # {"en":"Response Description","zh_CN":"响应描述"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateAppResponseHeader(TeaModel):
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






class UpdateTunnelApplicationsContentItem(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        ip_or_domain: str = None,
        ports: str = None,
    ):
        # {"en":"protocol,support for tcp,udp,icmp,all", "zh_CN":"协议,支持tcp、udp、icmp、all.  all表示不限制协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口,支持IP地址(IP、IP/掩码、IPX-IPy)和域名(精确域名、泛域),多个以英文分号间隔,最大支持2万个"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.ports, 'ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.ports is not None:
            result['ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('ports') is not None:
            self.ports = m.get('ports')
        return self


class UpdateTunnelApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[UpdateTunnelApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 128)
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = UpdateTunnelApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class UpdateTunnelApplicationsResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[UpdateTunnelApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = UpdateTunnelApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class UpdateTunnelApplicationsPaths(TeaModel):
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


class UpdateTunnelApplicationsParameters(TeaModel):
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


class UpdateTunnelApplicationsRequestHeader(TeaModel):
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


class UpdateTunnelApplicationsResponseHeader(TeaModel):
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






class AddDebugFingerprintRequestDebugFingerprintList(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        desc: str = None,
    ):
        # {"en":"Fingerprint, with a total length not exceeding 100, containing only colons, letters A to F in both uppercase and lowercase, and digits 0 to 9. After removing colons, the length should be between 32 and 64.","zh_CN":"指纹，总长度不超过100，仅包含冒号、A~F大小写字母和0~9的数字，去除冒号后长度介于32~64之间。"}
        self.fingerprint = fingerprint
        # {"en":"Description, no more than 60 characters.","zh_CN":"描述，长度不超过60。"}
        self.desc = desc

    def validate(self):
        self.validate_required(self.fingerprint, 'fingerprint')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class AddDebugFingerprintRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        debug_fingerprint_list: List[AddDebugFingerprintRequestDebugFingerprintList] = None,
    ):
        # {"en":"Application ID","zh_CN":"应用ID"}
        self.app_id = app_id
        # {"en":"Debug fingerprint, only applicable to Android.","zh_CN":"调试指纹，仅对Android生效。"}
        self.debug_fingerprint_list = debug_fingerprint_list

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.debug_fingerprint_list, 'debug_fingerprint_list')
        if self.debug_fingerprint_list:
            for k in self.debug_fingerprint_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.debug_fingerprint_list is not None:
            result['debugFingerprintList'] = []
            for k in self.debug_fingerprint_list:
                result['debugFingerprintList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('debugFingerprintList') is not None:
            self.debug_fingerprint_list = []
            for k in m.get('debugFingerprintList'):
                temp_model = AddDebugFingerprintRequestDebugFingerprintList()
                self.debug_fingerprint_list.append(temp_model.from_map(k))
        return self


class AddDebugFingerprintRequestHeader(TeaModel):
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


class AddDebugFingerprintPaths(TeaModel):
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


class AddDebugFingerprintParameters(TeaModel):
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


class AddDebugFingerprintResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"dictionary":"belong=MAA-masp-portal-console|dict=wplus_code","en":"Response Code","zh_CN":"响应码"}
        self.code = code
        # {"en":"Response Description","zh_CN":"响应描述"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AddDebugFingerprintResponseHeader(TeaModel):
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






class AuthorizeUserApplicationRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_names: List[str] = None,
        action_type: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"Resource/Application type, default is tunnel. tunnel: tunnelApp, web: webApp, link: linkApp, saas: saasApp", "zh_CN":"资源/应用类型，默认是隧道应用. tunnel: 隧道应用, web: WEB应用, link: 快捷链接, saas: saas应用"}
        self.resource_type = resource_type
        # {"en":"List of resource/application names", "zh_CN":"资源/应用名称列表"}
        self.resource_names = resource_names
        # {"en":"Action Type, 0: Append, 1: Overwrite", "zh_CN":"操作类型，0：追加，1：覆盖"}
        self.action_type = action_type
        # {"en":"List of authorized users", "zh_CN":"授权的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"List of authorized user group IDs", "zh_CN":"授权的用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.resource_names, 'resource_names')
        self.validate_required(self.action_type, 'action_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_names is not None:
            result['resourceNames'] = self.resource_names
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceNames') is not None:
            self.resource_names = m.get('resourceNames')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AuthorizeUserApplicationResponse(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_names: List[str] = None,
        action_type: int = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
    ):
        # {"en":"Resource/Application type.tunnel: tunnelApp, web: webApp, link: linkApp, saas: saasApp", "zh_CN":"资源/应用类型 tunnel: 隧道应用, web: WEB应用, link: 快捷链接, saas: saas应用"}
        self.resource_type = resource_type
        # {"en":"List of resource/application names", "zh_CN":"资源/应用名称列表"}
        self.resource_names = resource_names
        # {"en":"Action Type, 0: Append, 1: Overwrite", "zh_CN":"操作类型，0：追加，1：覆盖"}
        self.action_type = action_type
        # {"en":"List of authorized users", "zh_CN":"授权的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"List of authorized user group IDs", "zh_CN":"授权的用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_names, 'resource_names')
        self.validate_required(self.action_type, 'action_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_names is not None:
            result['resourceNames'] = self.resource_names
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceNames') is not None:
            self.resource_names = m.get('resourceNames')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        return self


class AuthorizeUserApplicationPaths(TeaModel):
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


class AuthorizeUserApplicationParameters(TeaModel):
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


class AuthorizeUserApplicationRequestHeader(TeaModel):
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


class AuthorizeUserApplicationResponseHeader(TeaModel):
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






class AddWebApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        ip_or_domain: str = None,
        port: str = None,
        remark: str = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"protocol", "zh_CN":"协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口:0-65535"}
        self.port = port
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 128)
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.port, 'port')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.port is not None:
            result['port'] = self.port
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class AddWebApplicationsResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        ip_or_domain: str = None,
        port: str = None,
        remark: str = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"protocol", "zh_CN":"协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口:0-65535"}
        self.port = port
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.port, 'port')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.port is not None:
            result['port'] = self.port
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class AddWebApplicationsPaths(TeaModel):
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


class AddWebApplicationsParameters(TeaModel):
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


class AddWebApplicationsRequestHeader(TeaModel):
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


class AddWebApplicationsResponseHeader(TeaModel):
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






class QueryAppListRequest(TeaModel):
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


class QueryAppListAppInfo(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_package: str = None,
        app_version: str = None,
        app_size: str = None,
        app_update_time: str = None,
    ):
        # {"en":"app name", "zh_CN":"应用名称"}
        self.app_name = app_name
        # {"en":"app ", "zh_CN":"应用包名"}
        self.app_package = app_package
        # {"en":"app version", "zh_CN":"应用版本"}
        self.app_version = app_version
        # {"en":"app size", "zh_CN":"应用大小"}
        self.app_size = app_size
        # {"en":"app update/install time", "zh_CN":"应用更新/安装时间"}
        self.app_update_time = app_update_time

    def validate(self):
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.app_package, 'app_package')
        self.validate_required(self.app_version, 'app_version')
        self.validate_required(self.app_size, 'app_size')
        self.validate_required(self.app_update_time, 'app_update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_package is not None:
            result['appPackage'] = self.app_package
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.app_size is not None:
            result['appSize'] = self.app_size
        if self.app_update_time is not None:
            result['appUpdateTime'] = self.app_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appPackage') is not None:
            self.app_package = m.get('appPackage')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('appSize') is not None:
            self.app_size = m.get('appSize')
        if m.get('appUpdateTime') is not None:
            self.app_update_time = m.get('appUpdateTime')
        return self


class QueryAppListResponse(TeaModel):
    def __init__(
        self,
        apps: List[QueryAppListAppInfo] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"app list", "zh_CN":"应用列表"}
        self.apps = apps
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.apps, 'apps')
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['apps'] = []
            for k in self.apps:
                result['apps'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apps') is not None:
            self.apps = []
            for k in m.get('apps'):
                temp_model = QueryAppListAppInfo()
                self.apps.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryAppListPaths(TeaModel):
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


class QueryAppListParameters(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"no", "zh_CN":"云手机id"}
        self.id = id

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class QueryAppListRequestHeader(TeaModel):
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


class QueryAppListResponseHeader(TeaModel):
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






class DescribeAuthorizedApplicationsOfUserRequest(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        # {"en":"User Name", "zh_CN":"用户名"}
        self.username = username

    def validate(self):
        self.validate_required(self.username, 'username')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class DescribeAuthorizedApplicationsOfUserResponse(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_name: str = None,
    ):
        # {"en":"Resource/Application type, default is tunnel. tunnel: tunnelApp, web: webApp, link: linkApp, saas: saasApp", "zh_CN":"资源/应用类型，默认是隧道应用. tunnel: 隧道应用, web: WEB应用, link: 快捷链接, saas: saas应用"}
        self.resource_type = resource_type
        # {"en":"Resource/Application name", "zh_CN":"资源/应用名称"}
        self.resource_name = resource_name

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_name, 'resource_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        return self


class DescribeAuthorizedApplicationsOfUserPaths(TeaModel):
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


class DescribeAuthorizedApplicationsOfUserParameters(TeaModel):
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


class DescribeAuthorizedApplicationsOfUserRequestHeader(TeaModel):
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


class DescribeAuthorizedApplicationsOfUserResponseHeader(TeaModel):
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






class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
    ):
        # {"en":"Application ID","zh_CN":"应用ID"}
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self


class DeleteAppRequestHeader(TeaModel):
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


class DeleteAppPaths(TeaModel):
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


class DeleteAppParameters(TeaModel):
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


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"dictionary":"belong=MAA-masp-portal-console|dict=wplus_code","en":"Response Code","zh_CN":"响应码"}
        self.code = code
        # {"en":"Response Description","zh_CN":"响应描述"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteAppResponseHeader(TeaModel):
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






class QueryApplicationDetailContentItem(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        ip_or_domain: str = None,
        ports: str = None,
    ):
        # {"en":"application name", "zh_CN":"协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口,支持IP地址(IP、IP/掩码、IPX-IPy)和域名(精确域名、泛域),多个以英文分号间隔,最大支持2万个"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.ports, 'ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.ports is not None:
            result['ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('ports') is not None:
            self.ports = m.get('ports')
        return self


class QueryApplicationDetailRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[QueryApplicationDetailContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = QueryApplicationDetailContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class QueryApplicationDetailResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[QueryApplicationDetailContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = QueryApplicationDetailContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class QueryApplicationDetailPaths(TeaModel):
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


class QueryApplicationDetailParameters(TeaModel):
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


class QueryApplicationDetailRequestHeader(TeaModel):
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


class QueryApplicationDetailResponseHeader(TeaModel):
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






class AuthorizeApplicationForUserRequest(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        action_type: int = None,
        resource_type: str = None,
        authorized_users: List[str] = None,
        authorized_user_group_ids: List[int] = None,
        exclude_users: List[str] = None,
        exclude_user_group_ids: List[int] = None,
    ):
        # {"en":"Resource/Application Name", "zh_CN":"资源/应用名称"}
        self.resource_name = resource_name
        # {"en":"Action Type, 0: Append, 1: Overwrite", "zh_CN":"操作类型，0：追加，1：覆盖"}
        self.action_type = action_type
        # {"en":"Resource Type, e.g., tunnel, web, link, saas", "zh_CN":"资源类型，比如：隧道应用、WEB应用、快捷链接、saas应用"}
        self.resource_type = resource_type
        # {"en":"List of authorized users", "zh_CN":"授权的用户列表"}
        self.authorized_users = authorized_users
        # {"en":"List of authorized user group IDs", "zh_CN":"授权的用户组ID列表"}
        self.authorized_user_group_ids = authorized_user_group_ids
        # {"en":"List of excluded users", "zh_CN":"例外用户列表"}
        self.exclude_users = exclude_users
        # {"en":"List of excluded user group IDs", "zh_CN":"例外用户组ID列表"}
        self.exclude_user_group_ids = exclude_user_group_ids

    def validate(self):
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.action_type, 'action_type')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.authorized_users is not None:
            result['authorizedUsers'] = self.authorized_users
        if self.authorized_user_group_ids is not None:
            result['authorizedUserGroupIds'] = self.authorized_user_group_ids
        if self.exclude_users is not None:
            result['excludeUsers'] = self.exclude_users
        if self.exclude_user_group_ids is not None:
            result['excludeUserGroupIds'] = self.exclude_user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('authorizedUsers') is not None:
            self.authorized_users = m.get('authorizedUsers')
        if m.get('authorizedUserGroupIds') is not None:
            self.authorized_user_group_ids = m.get('authorizedUserGroupIds')
        if m.get('excludeUsers') is not None:
            self.exclude_users = m.get('excludeUsers')
        if m.get('excludeUserGroupIds') is not None:
            self.exclude_user_group_ids = m.get('excludeUserGroupIds')
        return self


class AuthorizeApplicationForUserResponse(TeaModel):
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


class AuthorizeApplicationForUserPaths(TeaModel):
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


class AuthorizeApplicationForUserParameters(TeaModel):
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


class AuthorizeApplicationForUserRequestHeader(TeaModel):
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


class AuthorizeApplicationForUserResponseHeader(TeaModel):
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






class DeleteWebApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteWebApplicationsResponse(TeaModel):
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


class DeleteWebApplicationsPaths(TeaModel):
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


class DeleteWebApplicationsParameters(TeaModel):
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


class DeleteWebApplicationsRequestHeader(TeaModel):
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


class DeleteWebApplicationsResponseHeader(TeaModel):
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






class AddTunnelApplicationsContentItem(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        ip_or_domain: str = None,
        ports: str = None,
    ):
        # {"en":"protocol,support for tcp,udp,imcp,all.", "zh_CN":"协议,支持tcp,udp,icmp,all. all表示不限制协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口,支持IP地址(IP、IP/掩码、IPX-IPy)和域名(精确域名、泛域),多个以英文分号间隔,最大支持2万个"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.ports, 'ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.ports is not None:
            result['ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('ports') is not None:
            self.ports = m.get('ports')
        return self


class AddTunnelApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[AddTunnelApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.name is not None:
            self.validate_max_length(self.name, 'name', 128)
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        self.validate_required(self.content_list, 'content_list')
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = AddTunnelApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class AddTunnelApplicationsResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[AddTunnelApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        self.validate_required(self.content_list, 'content_list')
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = AddTunnelApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class AddTunnelApplicationsPaths(TeaModel):
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


class AddTunnelApplicationsParameters(TeaModel):
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


class AddTunnelApplicationsRequestHeader(TeaModel):
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


class AddTunnelApplicationsResponseHeader(TeaModel):
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






class UpdateWebApplicationsContentItem(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        ip_or_domain: str = None,
        ports: str = None,
    ):
        # {"en":"protocol", "zh_CN":"协议"}
        self.protocol = protocol
        # {"en":"ip or domain", "zh_CN":"ip或者域名"}
        self.ip_or_domain = ip_or_domain
        # {"en":"application ports", "zh_CN":"端口,支持IP地址(IP、IP/掩码、IPX-IPy)和域名(精确域名、泛域),多个以英文分号间隔,最大支持2万个"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ip_or_domain, 'ip_or_domain')
        self.validate_required(self.ports, 'ports')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_or_domain is not None:
            result['ipOrDomain'] = self.ip_or_domain
        if self.ports is not None:
            result['ports'] = self.ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipOrDomain') is not None:
            self.ip_or_domain = m.get('ipOrDomain')
        if m.get('ports') is not None:
            self.ports = m.get('ports')
        return self


class UpdateWebApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        new_name: str = None,
        remark: str = None,
        content_list: List[UpdateWebApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"new  application name", "zh_CN":"新的应用名称"}
        self.new_name = new_name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.new_name, 'new_name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.new_name is not None:
            result['newName'] = self.new_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('newName') is not None:
            self.new_name = m.get('newName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = UpdateWebApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class UpdateWebApplicationsResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        content_list: List[UpdateWebApplicationsContentItem] = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name
        # {"en":"Remark,Maximum length is 255 characters.", "zh_CN":"备注最大长度255个字符"}
        self.remark = remark
        # {"en":"application contents ", "zh_CN":"应用内容"}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.remark is not None:
            self.validate_max_length(self.remark, 'remark', 255)
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.content_list is not None:
            result['contentList'] = []
            for k in self.content_list:
                result['contentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('contentList') is not None:
            self.content_list = []
            for k in m.get('contentList'):
                temp_model = UpdateWebApplicationsContentItem()
                self.content_list.append(temp_model.from_map(k))
        return self


class UpdateWebApplicationsPaths(TeaModel):
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


class UpdateWebApplicationsParameters(TeaModel):
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


class UpdateWebApplicationsRequestHeader(TeaModel):
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


class UpdateWebApplicationsResponseHeader(TeaModel):
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






class ManageEphoneAppAppParamsObject(TeaModel):
    def __init__(
        self,
        url: str = None,
        pkg_name: str = None,
    ):
        # {"en":"apk url", "zh_CN":"apk文件下载地址"}
        self.url = url
        # {"en":"papckage name", "zh_CN":"app包名"}
        self.pkg_name = pkg_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.pkg_name is not None:
            result['pkgName'] = self.pkg_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('pkgName') is not None:
            self.pkg_name = m.get('pkgName')
        return self


class ManageEphoneAppOperateObject(TeaModel):
    def __init__(
        self,
        id: str = None,
        op: str = None,
        params: ManageEphoneAppAppParamsObject = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.id = id
        # {"en":"operate type", "zh_CN":"操作类型，可选值：install, uninstall, start, stop, clean"}
        self.op = op
        # {"en":"app operaate params", "zh_CN":"app 操作的参数"}
        self.params = params

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.op, 'op')
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.op is not None:
            result['op'] = self.op
        if self.params is not None:
            result['params'] = self.params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('params') is not None:
            temp_model = ManageEphoneAppAppParamsObject()
            self.params = temp_model.from_map(m['params'])
        return self


class ManageEphoneAppRequest(TeaModel):
    def __init__(
        self,
        apps: List[ManageEphoneAppOperateObject] = None,
    ):
        # {"en":"list of apps to operate on", "zh_CN":"操作的云手机应用数组"}
        self.apps = apps

    def validate(self):
        self.validate_required(self.apps, 'apps')
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['apps'] = []
            for k in self.apps:
                result['apps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apps') is not None:
            self.apps = []
            for k in m.get('apps'):
                temp_model = ManageEphoneAppOperateObject()
                self.apps.append(temp_model.from_map(k))
        return self


class ManageEphoneAppTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        message: str = None,
    ):
        # {"en":"task id", "zh_CN":"任务单id"}
        self.id = id
        # {"en":"message", "zh_CN":"任务单消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ManageEphoneAppResponse(TeaModel):
    def __init__(
        self,
        tasks: List[ManageEphoneAppTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['tasks'] = []
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = []
            for k in m.get('tasks'):
                temp_model = ManageEphoneAppTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ManageEphoneAppPaths(TeaModel):
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


class ManageEphoneAppParameters(TeaModel):
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


class ManageEphoneAppRequestHeader(TeaModel):
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


class ManageEphoneAppResponseHeader(TeaModel):
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






class DeleteTunnelApplicationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"application name", "zh_CN":"应用名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteTunnelApplicationsResponse(TeaModel):
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


class DeleteTunnelApplicationsPaths(TeaModel):
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


class DeleteTunnelApplicationsParameters(TeaModel):
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


class DeleteTunnelApplicationsRequestHeader(TeaModel):
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


class DeleteTunnelApplicationsResponseHeader(TeaModel):
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




