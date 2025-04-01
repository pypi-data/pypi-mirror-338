# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ApiMncSendsmsRequest(TeaModel):
    def __init__(
        self,
        mobiles: str = None,
        signature: str = None,
        content: str = None,
    ):
        # {"en":"mobiles", "zh_CN":"手机号列表，多个用半角逗号分隔"}
        self.mobiles = mobiles
        # {"en":"signature", "zh_CN":"短信签名"}
        self.signature = signature
        # {"en":"content", "zh_CN":"短信内容，最大字符数500"}
        self.content = content

    def validate(self):
        self.validate_required(self.mobiles, 'mobiles')
        self.validate_required(self.signature, 'signature')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['mobiles'] = self.mobiles
        if self.signature is not None:
            result['signature'] = self.signature
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mobiles') is not None:
            self.mobiles = m.get('mobiles')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ApiMncSendsmsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # {"en":"code", "zh_CN":"返回代码，0为成功，非0失败"}
        self.code = code
        # {"en":"message", "zh_CN":"异常信息，发送成功该字段为空，失败该字段非空"}
        self.message = message
        # {"en":"requestId", "zh_CN":"请求id,全局唯一"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ApiMncSendsmsPaths(TeaModel):
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


class ApiMncSendsmsParameters(TeaModel):
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


class ApiMncSendsmsRequestHeader(TeaModel):
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


class ApiMncSendsmsResponseHeader(TeaModel):
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




