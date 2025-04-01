# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class SecureLinkSdkAuthRequest(TeaModel):
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


class SecureLinkSdkAuthResponseContent(TeaModel):
    def __init__(
        self,
        sdk_token: str = None,
        issue_time: int = None,
    ):
        # {'en':'sdkToken', 'zh_CN':'sdk token'}
        self.sdk_token = sdk_token
        # {'en':'issueTime', 'zh_CN':'下发时间'}
        self.issue_time = issue_time

    def validate(self):
        self.validate_required(self.sdk_token, 'sdk_token')
        self.validate_required(self.issue_time, 'issue_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sdk_token is not None:
            result['sdkToken'] = self.sdk_token
        if self.issue_time is not None:
            result['issueTime'] = self.issue_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sdkToken') is not None:
            self.sdk_token = m.get('sdkToken')
        if m.get('issueTime') is not None:
            self.issue_time = m.get('issueTime')
        return self


class SecureLinkSdkAuthResponse(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_msg: str = None,
        content: SecureLinkSdkAuthResponseContent = None,
    ):
        # {'en':'Interface error code, 0-fail,1-success', 'zh_CN':'接口错误码，0-代表失败，1-代表成功'}
        self.return_code = return_code
        # {'en':'Error message', 'zh_CN':'错误信息'}
        self.return_msg = return_msg
        # {'en':'content', 'zh_CN':'数据，下面全是数据的内容'}
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
            temp_model = SecureLinkSdkAuthResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SecureLinkSdkAuthPaths(TeaModel):
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


class SecureLinkSdkAuthParameters(TeaModel):
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


class SecureLinkSdkAuthRequestHeader(TeaModel):
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


class SecureLinkSdkAuthResponseHeader(TeaModel):
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




