# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryAccountTrailLogRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2023-12-20T10:00 + 08:00 (10:0:00 Beijing time on December 20, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest one year data can be obtained at most.", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2023-12-20T10:00:00+08:00（为北京时间2023年12月20日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近1年 的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4.  Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days. ", "zh_CN":"	结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        return self


class QueryAccountTrailLogReferencedResourceView(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_names: List[str] = None,
    ):
        # {"en":"Resource Type.", "zh_CN":"资源类型"}
        self.resource_type = resource_type
        # {"en":"Resource Name.", "zh_CN":"资源名称"}
        self.resource_names = resource_names

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_names, 'resource_names')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_names is not None:
            result['resourceNames'] = self.resource_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceNames') is not None:
            self.resource_names = m.get('resourceNames')
        return self


class QueryAccountTrailLogUserIdentityView(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        idp_login_name: List[str] = None,
        client_name: List[str] = None,
    ):
        # {"en":"Account login name.", "zh_CN":"账号登录名"}
        self.login_name = login_name
        # {"en":"IDP internal account.", "zh_CN":"idp内部切换账号"}
        self.idp_login_name = idp_login_name
        # {"en":"IDP name.", "zh_CN":"	idp名称"}
        self.client_name = client_name

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.idp_login_name, 'idp_login_name')
        self.validate_required(self.client_name, 'client_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['loginName'] = self.login_name
        if self.idp_login_name is not None:
            result['idpLoginName'] = self.idp_login_name
        if self.client_name is not None:
            result['clientName'] = self.client_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')
        if m.get('idpLoginName') is not None:
            self.idp_login_name = m.get('idpLoginName')
        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')
        return self


class QueryAccountTrailLogResultView(TeaModel):
    def __init__(
        self,
        event_code: str = None,
        event_cn_name: str = None,
        event_en_name: str = None,
        event_source: str = None,
        event_time: str = None,
        request_id: str = None,
        referenced_resources: List[QueryAccountTrailLogReferencedResourceView] = None,
        product_code: str = None,
        source_ip_address: str = None,
        user_agent: str = None,
        user_identity: QueryAccountTrailLogUserIdentityView = None,
    ):
        # {"en":"Event code.", "zh_CN":"事件code"}
        self.event_code = event_code
        # {"en":"Event Chinese Name.", "zh_CN":"事件中文名称"}
        self.event_cn_name = event_cn_name
        # {"en":"Event English Name.", "zh_CN":"事件英文名称"}
        self.event_en_name = event_en_name
        # {"en":"Event Source.", "zh_CN":"事件来源"}
        self.event_source = event_source
        # {"en":"Event time.", "zh_CN":"事件发生时间点"}
        self.event_time = event_time
        # {"en":"Request ID.", "zh_CN":"请求ID"}
        self.request_id = request_id
        # {"en":"The list of resources impacted by the event.", "zh_CN":"事件影响的资源列表。"}
        self.referenced_resources = referenced_resources
        # {"en":"The product code related to the event.", "zh_CN":"事件相关的产品code。"}
        self.product_code = product_code
        # {"en":"The source IP address of the initiating event.", "zh_CN":"事件发起的源IP。"}
        self.source_ip_address = source_ip_address
        # {"en":"The client proxy identity for sending API requests.", "zh_CN":"发送API请求的客户端代理标识。"}
        self.user_agent = user_agent
        # {"en":"The identity information of the requester.", "zh_CN":"请求者的身份信息。"}
        self.user_identity = user_identity

    def validate(self):
        self.validate_required(self.event_code, 'event_code')
        self.validate_required(self.event_cn_name, 'event_cn_name')
        self.validate_required(self.event_en_name, 'event_en_name')
        self.validate_required(self.event_source, 'event_source')
        self.validate_required(self.event_time, 'event_time')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.referenced_resources, 'referenced_resources')
        if self.referenced_resources:
            for k in self.referenced_resources:
                if k:
                    k.validate()
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.source_ip_address, 'source_ip_address')
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.user_identity, 'user_identity')
        if self.user_identity:
            self.user_identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_code is not None:
            result['eventCode'] = self.event_code
        if self.event_cn_name is not None:
            result['eventCnName'] = self.event_cn_name
        if self.event_en_name is not None:
            result['eventEnName'] = self.event_en_name
        if self.event_source is not None:
            result['eventSource'] = self.event_source
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.referenced_resources is not None:
            result['referencedResources'] = []
            for k in self.referenced_resources:
                result['referencedResources'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.source_ip_address is not None:
            result['sourceIpAddress'] = self.source_ip_address
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.user_identity is not None:
            result['userIdentity'] = self.user_identity.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')
        if m.get('eventCnName') is not None:
            self.event_cn_name = m.get('eventCnName')
        if m.get('eventEnName') is not None:
            self.event_en_name = m.get('eventEnName')
        if m.get('eventSource') is not None:
            self.event_source = m.get('eventSource')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('referencedResources') is not None:
            self.referenced_resources = []
            for k in m.get('referencedResources'):
                temp_model = QueryAccountTrailLogReferencedResourceView()
                self.referenced_resources.append(temp_model.from_map(k))
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('sourceIpAddress') is not None:
            self.source_ip_address = m.get('sourceIpAddress')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('userIdentity') is not None:
            temp_model = QueryAccountTrailLogUserIdentityView()
            self.user_identity = temp_model.from_map(m['userIdentity'])
        return self


class QueryAccountTrailLogResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryAccountTrailLogResultView] = None,
    ):
        # {"en":"API response code", "zh_CN":"API响应码"}
        self.code = code
        # {"en":"API response message", "zh_CN":"API响应消息"}
        self.message = message
        # {"en":"Audit log query results", "zh_CN":"审计日志查询结果"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

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
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = QueryAccountTrailLogResultView()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAccountTrailLogPaths(TeaModel):
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


class QueryAccountTrailLogParameters(TeaModel):
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


class QueryAccountTrailLogRequestHeader(TeaModel):
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


class QueryAccountTrailLogResponseHeader(TeaModel):
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




