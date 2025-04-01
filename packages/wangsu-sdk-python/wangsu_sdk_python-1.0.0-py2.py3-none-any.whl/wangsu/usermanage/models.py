# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AddAccountIdentRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"login name", "zh_CN":"登录名"}
        self.login_name = login_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class AddAccountIdentResponse(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        secret_key: str = None,
    ):
        # {"en":"accessKey", "zh_CN":"accessKey"}
        self.access_key = access_key
        # {"en":"secretKey", "zh_CN":"secretKey"}
        self.secret_key = secret_key

    def validate(self):
        self.validate_required(self.access_key, 'access_key')
        self.validate_required(self.secret_key, 'secret_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        return self


class AddAccountIdentPaths(TeaModel):
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


class AddAccountIdentParameters(TeaModel):
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


class AddAccountIdentRequestHeader(TeaModel):
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


class AddAccountIdentResponseHeader(TeaModel):
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






class DeleteSubAccountRequest(TeaModel):
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


class DeleteSubAccountResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"请求结果信息"}
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


class DeleteSubAccountPaths(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"Sub account login name", "zh_CN":"子用户登录名"}
        self.login_name = login_name

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class DeleteSubAccountParameters(TeaModel):
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


class DeleteSubAccountRequestHeader(TeaModel):
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


class DeleteSubAccountResponseHeader(TeaModel):
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






class CheckLoginNameLegalRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"login name", "zh_CN":"登录名"}
        self.login_name = login_name

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class CheckLoginNameLegalResponse(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
    ):
        # {"en":"Message", "zh_CN":"消息提示"}
        self.message = message
        # {"en":"Status Code", "zh_CN":"错误具体状态码"}
        self.code = code

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CheckLoginNameLegalPaths(TeaModel):
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


class CheckLoginNameLegalParameters(TeaModel):
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


class CheckLoginNameLegalRequestHeader(TeaModel):
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


class CheckLoginNameLegalResponseHeader(TeaModel):
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






class QuerySubAccountInfoRequest(TeaModel):
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


class QuerySubAccountInfoSubAccount(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        display_name: str = None,
        email: str = None,
        mobile: str = None,
        create_time: str = None,
        console_enable: int = None,
        status: int = None,
    ):
        # {"en":"login name", "zh_CN":"登录名"}
        self.login_name = login_name
        # {"en":"display name", "zh_CN":"称呼"}
        self.display_name = display_name
        # {"en":"email", "zh_CN":"邮箱"}
        self.email = email
        # {"en":"mobile", "zh_CN":"手机"}
        self.mobile = mobile
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"consoleEnable", "zh_CN":"是否允许登录控制台：1是 0 否"}
        self.console_enable = console_enable
        # {"en":"status", "zh_CN":"状态： 1 启用 0 停用"}
        self.status = status

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.email, 'email')
        self.validate_required(self.mobile, 'mobile')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.console_enable, 'console_enable')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.console_enable is not None:
            result['consoleEnable'] = self.console_enable
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('consoleEnable') is not None:
            self.console_enable = m.get('consoleEnable')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QuerySubAccountInfoResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QuerySubAccountInfoSubAccount = None,
    ):
        # {"en":"Status Code", "zh_CN":"错误具体状态码"}
        self.code = code
        # {"en":"Message", "zh_CN":"消息提示"}
        self.message = message
        # {"en":"data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QuerySubAccountInfoSubAccount()
            self.data = temp_model.from_map(m['data'])
        return self


class QuerySubAccountInfoPaths(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"Login Name", "zh_CN":"子账号登录名"}
        self.login_name = login_name

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class QuerySubAccountInfoParameters(TeaModel):
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


class QuerySubAccountInfoRequestHeader(TeaModel):
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


class QuerySubAccountInfoResponseHeader(TeaModel):
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






class ApiIamBatchattachorreclaimpolicy2subaccountDnaRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        policy_id: List[int] = None,
        type: int = None,
    ):
        # {"en":"Sub account login name", "zh_CN":"子用户登录名"}
        self.login_name = login_name
        # {"en":"Specify policy ID", "zh_CN":"指定权限策略id"}
        self.policy_id = policy_id
        # {"en":"Select you want to add or revoke policy for sub account.
        # 
        # 0:add policy
        # 
        # 1:revoke policy", "zh_CN":"选择需要为子用户添加或撤销权限策略
        # 
        # 0：添加权限
        # 
        # 1：撤销权限"}
        self.type = type

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ApiIamBatchattachorreclaimpolicy2subaccountDnaResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
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


class ApiIamBatchattachorreclaimpolicy2subaccountDnaPaths(TeaModel):
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


class ApiIamBatchattachorreclaimpolicy2subaccountDnaParameters(TeaModel):
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


class ApiIamBatchattachorreclaimpolicy2subaccountDnaRequestHeader(TeaModel):
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


class ApiIamBatchattachorreclaimpolicy2subaccountDnaResponseHeader(TeaModel):
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






class UpdateAccountIdentRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        status: str = None,
    ):
        # {"en":"accessKey", "zh_CN":"accessKey"}
        self.access_key = access_key
        # {"en":"status", "zh_CN":"状态 disabled表示禁用，activated表示启用"}
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateAccountIdentResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"请求结果信息"}
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


class UpdateAccountIdentPaths(TeaModel):
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


class UpdateAccountIdentParameters(TeaModel):
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


class UpdateAccountIdentRequestHeader(TeaModel):
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


class UpdateAccountIdentResponseHeader(TeaModel):
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






class QueryAgentAssociatedMainAccountServiceRequest(TeaModel):
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


class QueryAgentAssociatedMainAccountServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        main_account: str = None,
        display_name: str = None,
        parent_main_account: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Message", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Primary account login name", "zh_CN":"主账号登录名"}
        self.main_account = main_account
        # {"en":"Primary account display name", "zh_CN":"主账号显示名"}
        self.display_name = display_name
        # {"en":"The parent account of the primary account", "zh_CN":"主账号对应的父主账号登录名"}
        self.parent_main_account = parent_main_account

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.main_account, 'main_account')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.parent_main_account, 'parent_main_account')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.main_account is not None:
            result['mainAccount'] = self.main_account
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.parent_main_account is not None:
            result['parentMainAccount'] = self.parent_main_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('mainAccount') is not None:
            self.main_account = m.get('mainAccount')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('parentMainAccount') is not None:
            self.parent_main_account = m.get('parentMainAccount')
        return self


class QueryAgentAssociatedMainAccountServicePaths(TeaModel):
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


class QueryAgentAssociatedMainAccountServiceParameters(TeaModel):
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


class QueryAgentAssociatedMainAccountServiceRequestHeader(TeaModel):
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


class QueryAgentAssociatedMainAccountServiceResponseHeader(TeaModel):
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






class DeleteAccountIdentRequest(TeaModel):
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


class DeleteAccountIdentResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"请求结果信息"}
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


class DeleteAccountIdentPaths(TeaModel):
    def __init__(
        self,
        access_key: str = None,
    ):
        # {"en":"accessKey", "zh_CN":"accessKey"}
        self.access_key = access_key

    def validate(self):
        self.validate_required(self.access_key, 'access_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        return self


class DeleteAccountIdentParameters(TeaModel):
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


class DeleteAccountIdentRequestHeader(TeaModel):
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


class DeleteAccountIdentResponseHeader(TeaModel):
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






class AddSubAccountRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        display_name: str = None,
        password: str = None,
        status: int = None,
        parent_login_name: str = None,
        email: str = None,
        phone: str = None,
        mobile: str = None,
        api_key: str = None,
        console_enable: int = None,
        programmatic_enable: int = None,
        login_reset_password: int = None,
    ):
        # {"en":"login name", "zh_CN":"登录名"}
        self.login_name = login_name
        # {"en":"display name", "zh_CN":"称呼"}
        self.display_name = display_name
        # {"en":"password", "zh_CN":"密码"}
        self.password = password
        # {"en":"status", "zh_CN":"状态： 1 启用 0 停用"}
        self.status = status
        # {"en":"parentLoginName", "zh_CN":"父账号登录名"}
        self.parent_login_name = parent_login_name
        # {"en":"email", "zh_CN":"邮箱"}
        self.email = email
        # {"en":"phone", "zh_CN":"电话"}
        self.phone = phone
        # {"en":"mobile", "zh_CN":"手机"}
        self.mobile = mobile
        # {"en":"apiKey", "zh_CN":"apiKey"}
        self.api_key = api_key
        # {"en":"consoleEnable", "zh_CN":"是否允许登录控制台：1是 0 否"}
        self.console_enable = console_enable
        # {"en":"programmaticEnable", "zh_CN":"是否允许编程访问：1是 0 否"}
        self.programmatic_enable = programmatic_enable
        # {"en":"loginResetPassword", "zh_CN":"登录是否需重置密码：1是 0 否"}
        self.login_reset_password = login_reset_password

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.password, 'password')
        self.validate_required(self.status, 'status')
        self.validate_required(self.parent_login_name, 'parent_login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.password is not None:
            result['password'] = self.password
        if self.status is not None:
            result['status'] = self.status
        if self.parent_login_name is not None:
            result['parentLoginName'] = self.parent_login_name
        if self.email is not None:
            result['email'] = self.email
        if self.phone is not None:
            result['phone'] = self.phone
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.console_enable is not None:
            result['consoleEnable'] = self.console_enable
        if self.programmatic_enable is not None:
            result['programmaticEnable'] = self.programmatic_enable
        if self.login_reset_password is not None:
            result['loginResetPassword'] = self.login_reset_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('parentLoginName') is not None:
            self.parent_login_name = m.get('parentLoginName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('consoleEnable') is not None:
            self.console_enable = m.get('consoleEnable')
        if m.get('programmaticEnable') is not None:
            self.programmatic_enable = m.get('programmaticEnable')
        if m.get('loginResetPassword') is not None:
            self.login_reset_password = m.get('loginResetPassword')
        return self


class AddSubAccountResponse(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
    ):
        # {"en":"Message", "zh_CN":"消息提示"}
        self.message = message
        # {"en":"Status Code", "zh_CN":"错误具体状态码"}
        self.code = code

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class AddSubAccountPaths(TeaModel):
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


class AddSubAccountParameters(TeaModel):
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


class AddSubAccountRequestHeader(TeaModel):
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


class AddSubAccountResponseHeader(TeaModel):
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






class GetSubAccountListRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Get a list of sub accounts under the main account", "zh_CN":"主用户登录名"}
        self.login_name = login_name
        # {"en":"Sub account loginName or displayName fuzzy query", "zh_CN":"子账号loginName或displayName模糊查询"}
        self.name = name
        # {"en":"Page Number of Current Page.If it was empty, it would be treated as not being divided into pages. The contents filled in the pageSize field would not be effective", "zh_CN":"指定分页查询时,当前页的页码。为空则不分页处理全部返回,pageSize字段填写内容不生效"}
        self.page_index = page_index
        # {"en":"The maximum number of data displayed on each page.
        # The maximum value of the PageSize is 100. The number of data bar displayed on each page was 20 by default. When the PageSize value is empty, and pageIndex is not empty,20 data would be returned by default.", "zh_CN":"指定分页查询时,每页显示的数据最大条数。
        # PageSize参数最大取值为100。每页默认显示的数据条数为20条,PageSize参数值为空时,将默认返回20条数据。"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.name is not None:
            result['name'] = self.name
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetSubAccountListSubAccount(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        display_name: str = None,
        email: str = None,
        mobile: str = None,
        create_time: str = None,
        status: int = None,
    ):
        # {"en":"Sub account login name", "zh_CN":"子用户登录名"}
        self.login_name = login_name
        # {"en":"Sub account display name", "zh_CN":"子用户显示名"}
        self.display_name = display_name
        # {"en":"Sub accout's E-mail", "zh_CN":"绑定的邮箱"}
        self.email = email
        # {"en":"Sub accout's mobile phone", "zh_CN":"绑定的手机"}
        self.mobile = mobile
        # {"en":"CreateTime", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"The status of accout1:Activate0:Disable", "zh_CN":"账号启用/禁用状态,1代表启用,0代表禁用"}
        self.status = status

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.email, 'email')
        self.validate_required(self.mobile, 'mobile')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetSubAccountListPageInfo(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
        rows: List[GetSubAccountListSubAccount] = None,
    ):
        # {"en":"page Index", "zh_CN":"页码"}
        self.page_index = page_index
        # {"en":"page Size", "zh_CN":"每页个数"}
        self.page_size = page_size
        # {"en":"total", "zh_CN":"总条数"}
        self.total = total
        # {"en":"rows", "zh_CN":"每页数据"}
        self.rows = rows

    def validate(self):
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        if self.rows is not None:
            result['rows'] = []
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = GetSubAccountListSubAccount()
                self.rows.append(temp_model.from_map(k))
        return self


class GetSubAccountListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetSubAccountListPageInfo = None,
    ):
        # {"en":"code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"data", "zh_CN":"返回值"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = GetSubAccountListPageInfo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetSubAccountListPaths(TeaModel):
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


class GetSubAccountListParameters(TeaModel):
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


class GetSubAccountListRequestHeader(TeaModel):
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


class GetSubAccountListResponseHeader(TeaModel):
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






class QueryPolicyAttachedMainAccountOrSubAccountRequest(TeaModel):
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


class QueryPolicyAttachedMainAccountOrSubAccountPolicyDescribe(TeaModel):
    def __init__(
        self,
        language_code: str = None,
        language_value: str = None,
    ):
        # {"en":"Language type", "zh_CN":"语言类型"}
        self.language_code = language_code
        # {"en":"Policy description", "zh_CN":"策略描述内容"}
        self.language_value = language_value

    def validate(self):
        self.validate_required(self.language_code, 'language_code')
        self.validate_required(self.language_value, 'language_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language_code is not None:
            result['languageCode'] = self.language_code
        if self.language_value is not None:
            result['languageValue'] = self.language_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('languageCode') is not None:
            self.language_code = m.get('languageCode')
        if m.get('languageValue') is not None:
            self.language_value = m.get('languageValue')
        return self


class QueryPolicyAttachedMainAccountOrSubAccountResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_describe: List[QueryPolicyAttachedMainAccountOrSubAccountPolicyDescribe] = None,
        policy_type: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Message", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"policyId", "zh_CN":"策略id"}
        self.policy_id = policy_id
        # {"en":"policy name", "zh_CN":"策略名称"}
        self.policy_name = policy_name
        # {"en":"Plocy description with multi language", "zh_CN":"国际化策略描述"}
        self.policy_describe = policy_describe
        # {"en":"policy type", "zh_CN":"策略类型：system：系统策略、custom自定义策略"}
        self.policy_type = policy_type

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.policy_describe, 'policy_describe')
        if self.policy_describe:
            for k in self.policy_describe:
                if k:
                    k.validate()
        self.validate_required(self.policy_type, 'policy_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.policy_describe is not None:
            result['policyDescribe'] = []
            for k in self.policy_describe:
                result['policyDescribe'].append(k.to_map() if k else None)
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('policyDescribe') is not None:
            self.policy_describe = []
            for k in m.get('policyDescribe'):
                temp_model = QueryPolicyAttachedMainAccountOrSubAccountPolicyDescribe()
                self.policy_describe.append(temp_model.from_map(k))
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self


class QueryPolicyAttachedMainAccountOrSubAccountPaths(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"loginName(Main or ordinary subAccount are available)", "zh_CN":"用户登录名（可传主子用户）"}
        self.login_name = login_name

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class QueryPolicyAttachedMainAccountOrSubAccountParameters(TeaModel):
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


class QueryPolicyAttachedMainAccountOrSubAccountRequestHeader(TeaModel):
    def __init__(
        self,
        acceptlanguage: str = None,
    ):
        # {"en":"Select the specified language and return the policy description of the corresponding language. Optional values:zh_CN，en，ko_KR，ja_JP；Default language is en
        # ", "zh_CN":"选择指定语言返回对应语言的策略描述，可选值：zh_CN，en，ko_KR，ja_JP；未选择默认en	"}
        self.acceptlanguage = acceptlanguage

    def validate(self):
        self.validate_required(self.acceptlanguage, 'acceptlanguage')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceptlanguage is not None:
            result['Accept-Language'] = self.acceptlanguage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accept-Language') is not None:
            self.acceptlanguage = m.get('Accept-Language')
        return self


class QueryPolicyAttachedMainAccountOrSubAccountResponseHeader(TeaModel):
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






class ListAccountIdentRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
    ):
        # {"en":"loginName", "zh_CN":"登录名"}
        self.login_name = login_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        return self


class ListAccountIdentResponse(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        secret_key: str = None,
        status: str = None,
    ):
        # {"en":"accessKey", "zh_CN":"accessKey"}
        self.access_key = access_key
        # {"en":"secretKey", "zh_CN":"secretKey"}
        self.secret_key = secret_key
        # {"en":"status", "zh_CN":"状态 disabled表示禁用，activated表示启用"}
        self.status = status

    def validate(self):
        self.validate_required(self.access_key, 'access_key')
        self.validate_required(self.secret_key, 'secret_key')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAccountIdentPaths(TeaModel):
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


class ListAccountIdentParameters(TeaModel):
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


class ListAccountIdentRequestHeader(TeaModel):
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


class ListAccountIdentResponseHeader(TeaModel):
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






class UpdateSubAccountRequest(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        display_name: str = None,
        email: str = None,
        mobile: str = None,
        console_enable: int = None,
        open_api_status: int = None,
        area_code: str = None,
        login_reset_password: int = None,
        password: str = None,
    ):
        # {"en":"Sub account login name", "zh_CN":"子用户登录名"}
        self.login_name = login_name
        # {"en":"display name", "zh_CN":"子用户显示名称"}
        self.display_name = display_name
        # {"en":"email", "zh_CN":"邮箱"}
        self.email = email
        # {"en":"mobile", "zh_CN":"手机"}
        self.mobile = mobile
        # {"en":"Programmatic Access or not 1:Yes0:No", "zh_CN":"子用户是否允许登录控制台：1是 0 否"}
        self.console_enable = console_enable
        # {"en":"openApiStatus", "zh_CN":"是否开启OpenAPI 0否，1是"}
        self.open_api_status = open_api_status
        # {"en":"area code", "zh_CN":"手机号区号"}
        self.area_code = area_code
        # {"en":"loginResetPassword", "zh_CN":"登录是否重置密码 1 是 0  否"}
        self.login_reset_password = login_reset_password
        # {"en":"password", "zh_CN":"密码"}
        self.password = password

    def validate(self):
        self.validate_required(self.login_name, 'login_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.console_enable is not None:
            result['consoleEnable'] = self.console_enable
        if self.open_api_status is not None:
            result['openApiStatus'] = self.open_api_status
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        if self.login_reset_password is not None:
            result['loginResetPassword'] = self.login_reset_password
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('consoleEnable') is not None:
            self.console_enable = m.get('consoleEnable')
        if m.get('openApiStatus') is not None:
            self.open_api_status = m.get('openApiStatus')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('loginResetPassword') is not None:
            self.login_reset_password = m.get('loginResetPassword')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class UpdateSubAccountResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"请求结果信息"}
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


class UpdateSubAccountPaths(TeaModel):
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


class UpdateSubAccountParameters(TeaModel):
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


class UpdateSubAccountRequestHeader(TeaModel):
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


class UpdateSubAccountResponseHeader(TeaModel):
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




