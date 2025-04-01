# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class LiveFetchTaskRequest(TeaModel):
    def __init__(
        self,
        urls: List[str] = None,
        view: str = None,
        carrier: str = None,
        action: int = None,
    ):
        # {'en':'url,Multiple values are separated by ","', 'zh_CN':'指要直播预拉取的频道集合，即url集合，URL必须是标准的http(s)://开头，且为具体的URL，不支持正则与目录，每次调用允许多个url，单次最多提交400条url。多个url时用引号和逗号隔开。'}
        self.urls = urls
        # {"en":"view", "zh_CN":"要预热的地区；多个值用'，'分隔，单次调用最多同时传入10个view；允许为空，当view不传值时，表示预热所有区域；输入格式为：&bull; 假设要预热福建省，只需输入'福建'，如果想同时预热浙江省和福建省，只需输入'浙江，福建'；&bull; 如果要预热海外区域，则不需要传入运营商，只需要传入国家名，例如'奥地利''美国'等。注：由于数据的特殊性，如果想预热广东全省，需将广州和深圳同时传入，即需输入'广东，广州，深圳'。"}
        self.view = view
        # {'en':'Operators,Such as China Telecom, China Unicom, etc.Multiple values are separated by ",",Allow to be empty.The default value is all operators', 'zh_CN':'预热的运营商，如电信、联通等；多个值用"，"分隔，允许为空，当carrier不传值时，表示预热所有运营商。'}
        self.carrier = carrier
        # {'en':'0 start preftch 1 stop prefetch', 'zh_CN':'表示本次任务的操作类型，即传递给内容服务器一个操作的命令，可设置的数值有：0：开始预热，创建新的预热任务1：停止预热，停止已经在预热的任务'}
        self.action = action

    def validate(self):
        self.validate_required(self.urls, 'urls')
        self.validate_required(self.action, 'action')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urls is not None:
            result['urls'] = self.urls
        if self.view is not None:
            result['view'] = self.view
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('view') is not None:
            self.view = m.get('view')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class LiveFetchTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {'en':'result code', 'zh_CN':'表示任务创建的状态码，200表示成功，非200表示失败'}
        self.code = code
        # {'en':'message', 'zh_CN':'表示任务提交后，系统的响应消息'}
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


class LiveFetchTaskPaths(TeaModel):
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


class LiveFetchTaskParameters(TeaModel):
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


class LiveFetchTaskRequestHeader(TeaModel):
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


class LiveFetchTaskResponseHeader(TeaModel):
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




