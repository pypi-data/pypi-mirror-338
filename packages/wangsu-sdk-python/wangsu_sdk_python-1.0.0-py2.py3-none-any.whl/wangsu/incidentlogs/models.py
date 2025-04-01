# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DownloadAttackLogRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        language: str = None,
        domain: str = None,
        client_ip: str = None,
        attack_type: str = None,
        process_action: str = None,
        uri: str = None,
        accurate_uri: int = None,
        user_agent: str = None,
        accurate_user_agent: int = None,
        state_code: str = None,
        referer: str = None,
        request_mode: str = None,
    ):
        # {"en":"Start time 2020-01-01 00:00:00  interval between start time and end time < = 1 day", "zh_CN":"开始时间 2020-01-01 00:00:00 开始时间与结束时间间隔<=1天"}
        self.start_time = start_time
        # {"en":"End time 2020-01-02 00:00:00  interval between start time and end time < = 1 day", "zh_CN":"结束时间 2020-01-02 00:00:00 开始时间与结束时间间隔<=1天"}
        self.end_time = end_time
        # {"en":"language default:cn
        #     cn Chinese
        #     en English", "zh_CN":"语言 默认为中文
        #     cn 中文
        #     en 英文"}
        self.language = language
        # {"en":"Domain name. Multiple values are separated by English commas.If blank, query all.", "zh_CN":"域名，多个值使用英文逗号分隔，域名为空查询全部"}
        self.domain = domain
        # {"en":"Client IP, multiple are separated by English commas", "zh_CN":"客户端IP，多个使用英文逗号分隔"}
        self.client_ip = client_ip
        # {"en":"Protection strategy, multiple are separated by English commas
        # 001 built in protection
        # 002 HTTP watermark protection
        # 003 access control
        # 004 frequency limit
        # 005 four layer DDoS protection
        # ", "zh_CN":"防护策略，多个使用英文逗号分隔
        # 001  内置防护
        # 002  HTTP水印防护
        # 003  访问控制
        # 004  频率限制
        # 005  四层DDoS防护
        # "}
        self.attack_type = attack_type
        # {"en":"Processing actions, multiple are separated by English commas, and the input parameter is empty to query all
        # Intercept: 1
        # Man machine verification: 2
        # IntelligentBlocking: 3
        # Alarm: 4
        # Custom block page: 5
        # Disconnect: 6
        # ", "zh_CN":"处理动作，多个使用英文逗号分隔,入参为空查询全部
        # 拦截：1
        # 人机校验：2
        # 智能封禁：3
        # 告警：4
        # 跳转友好界面：5
        # 断开连接：6
        # "}
        self.process_action = process_action
        # {"en":"uri", "zh_CN":"uri"}
        self.uri = uri
        # {"en":"Whether the URIs match exactly, 1 yes", "zh_CN":"uri是否精确匹配，1是"}
        self.accurate_uri = accurate_uri
        # {"en":"userAgent", "zh_CN":"userAgent"}
        self.user_agent = user_agent
        # {"en":"Whether useragent exactly matches, 1 yes", "zh_CN":"useragent 是否精确匹配, 1 yes"}
        self.accurate_user_agent = accurate_user_agent
        # {"en":"Status codes, multiple separated by commas", "zh_CN":"状态码，多个使用逗号分隔"}
        self.state_code = state_code
        # {"en":"referer", "zh_CN":"referer"}
        self.referer = referer
        # {"en":"Request mode: multiple are separated by commas (get, post, head, options, put, delete, trace, connect)", "zh_CN":"请求方式，多个使用逗号分隔（GET,POST,HEAD,OPTIONS,PUT,DELETE,TRACE,CONNECT）"}
        self.request_mode = request_mode

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.process_action, 'process_action')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.language is not None:
            result['language'] = self.language
        if self.domain is not None:
            result['domain'] = self.domain
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.process_action is not None:
            result['processAction'] = self.process_action
        if self.uri is not None:
            result['uri'] = self.uri
        if self.accurate_uri is not None:
            result['accurateUri'] = self.accurate_uri
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.accurate_user_agent is not None:
            result['accurateUserAgent'] = self.accurate_user_agent
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.referer is not None:
            result['referer'] = self.referer
        if self.request_mode is not None:
            result['requestMode'] = self.request_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('processAction') is not None:
            self.process_action = m.get('processAction')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('accurateUri') is not None:
            self.accurate_uri = m.get('accurateUri')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('accurateUserAgent') is not None:
            self.accurate_user_agent = m.get('accurateUserAgent')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('requestMode') is not None:
            self.request_mode = m.get('requestMode')
        return self


class DownloadAttackLogResponse(TeaModel):
    def __init__(
        self,
        access_time: str = None,
        client_ip: str = None,
        domain: str = None,
        request_method: str = None,
        uri: str = None,
        referer: str = None,
        user_agent: str = None,
        state_code: str = None,
        dst_port: str = None,
        agreement: str = None,
        rule_name: str = None,
        process_action: str = None,
        ip_location: str = None,
        http_version: str = None,
    ):
        # {"en":"accessTime", "zh_CN":"访问时间"}
        self.access_time = access_time
        # {"en":"clientIp", "zh_CN":"客户端ip"}
        self.client_ip = client_ip
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"requestMethod", "zh_CN":"请求方式"}
        self.request_method = request_method
        # {"en":"uri", "zh_CN":"uri"}
        self.uri = uri
        # {"en":"referer", "zh_CN":"referer"}
        self.referer = referer
        # {"en":"userAgent", "zh_CN":"userAgent"}
        self.user_agent = user_agent
        # {"en":"stateCode", "zh_CN":"状态码"}
        self.state_code = state_code
        # {"en":"dstPort", "zh_CN":"端口"}
        self.dst_port = dst_port
        # {"en":"agreement", "zh_CN":"协议"}
        self.agreement = agreement
        # {"en":"ruleName", "zh_CN":"规则名称"}
        self.rule_name = rule_name
        # {'en':'processAction','zh_CN':'处理动作'}
        self.process_action = process_action
        # {"en":"ip location", "zh_CN":"ip地理位置"}
        self.ip_location = ip_location
        # {"en":"httpVersion", "zh_CN":"http版本"}
        self.http_version = http_version

    def validate(self):
        self.validate_required(self.access_time, 'access_time')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.uri, 'uri')
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.state_code, 'state_code')
        self.validate_required(self.dst_port, 'dst_port')
        self.validate_required(self.agreement, 'agreement')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.process_action, 'process_action')
        self.validate_required(self.ip_location, 'ip_location')
        self.validate_required(self.http_version, 'http_version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_time is not None:
            result['accessTime'] = self.access_time
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.uri is not None:
            result['uri'] = self.uri
        if self.referer is not None:
            result['referer'] = self.referer
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.dst_port is not None:
            result['dstPort'] = self.dst_port
        if self.agreement is not None:
            result['agreement'] = self.agreement
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.process_action is not None:
            result['processAction'] = self.process_action
        if self.ip_location is not None:
            result['ipLocation'] = self.ip_location
        if self.http_version is not None:
            result['httpVersion'] = self.http_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTime') is not None:
            self.access_time = m.get('accessTime')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('dstPort') is not None:
            self.dst_port = m.get('dstPort')
        if m.get('agreement') is not None:
            self.agreement = m.get('agreement')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('processAction') is not None:
            self.process_action = m.get('processAction')
        if m.get('ipLocation') is not None:
            self.ip_location = m.get('ipLocation')
        if m.get('httpVersion') is not None:
            self.http_version = m.get('httpVersion')
        return self


class DownloadAttackLogPaths(TeaModel):
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


class DownloadAttackLogParameters(TeaModel):
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


class DownloadAttackLogRequestHeader(TeaModel):
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


class DownloadAttackLogResponseHeader(TeaModel):
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






class QueryAttackLogDetailsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        language: str = None,
        domain: str = None,
        client_ip: str = None,
        attack_type: str = None,
        process_action: str = None,
        uri: str = None,
        accurate_uri: int = None,
        user_agent: str = None,
        accurate_user_agent: int = None,
        state_code: str = None,
        referer: str = None,
        request_mode: str = None,
    ):
        # {"en":"Start time 2020-01-01 00:00:00    interval between start time and end time < = one day", "zh_CN":"开始时间  2020-01-01 00:00:00  开始时间与结束时间间隔<=1天"}
        self.start_time = start_time
        # {"en":"End time 2020-01-02 00:00:00   interval between start time and end time < = one day", "zh_CN":"结束时间  2020-01-02 00:00:00  开始时间与结束时间间隔<=1天"}
        self.end_time = end_time
        # {"en":"language default:cn
        #     cn Chinese
        #     en English", "zh_CN":"语言 默认为中文
        #     cn 中文
        #     en 英文"}
        self.language = language
        # {"en":"Domain name. Multiple values are separated by English commas.If blank, query all.", "zh_CN":"域名，多个值使用英文逗号分隔，域名为空查询全部"}
        self.domain = domain
        # {"en":"Client IP, multiple are separated by English commas", "zh_CN":"客户端IP，多个使用英文逗号分隔"}
        self.client_ip = client_ip
        # {"en":"Protection strategy, multiple are separated by English commas
        # 001 built in protection
        # 002 HTTP watermark protection
        # 003 access control
        # 004 frequency limit
        # 005 four layer DDoS protection
        # ", "zh_CN":"防护策略，多个使用英文逗号分隔
        # 001  内置防护
        # 002  HTTP水印防护
        # 003  访问控制
        # 004  频率限制
        # 005  四层DDoS防护
        # "}
        self.attack_type = attack_type
        # {"en":"Processing actions, multiple are separated by English commas, and the input parameter is empty to query all
        # Intercept: 1
        # Man machine verification: 2
        # IntelligentBlocking: 3
        # Alarm: 4
        # Custom block page: 5
        # Disconnect: 6
        # ", "zh_CN":"处理动作，多个使用英文逗号分隔,入参为空查询全部
        # 拦截：1
        # 人机校验：2
        # 智能封禁：3
        # 告警：4
        # 跳转友好界面：5
        # 断开连接：6
        # 注：防护策略和处理动作必填"}
        self.process_action = process_action
        # {"en":"uri", "zh_CN":"uri"}
        self.uri = uri
        # {"en":"Whether the URIs match exactly, 1 yes", "zh_CN":"uri是否精确匹配，1是"}
        self.accurate_uri = accurate_uri
        # {"en":"userAgent", "zh_CN":"userAgent"}
        self.user_agent = user_agent
        # {"en":"Whether useragent exactly matches, 1 yes", "zh_CN":"Whether useragent exactly matches, 1 yes"}
        self.accurate_user_agent = accurate_user_agent
        # {"en":"Status codes, multiple separated by commas", "zh_CN":"状态码，多个使用逗号分隔"}
        self.state_code = state_code
        # {"en":"referer", "zh_CN":"referer"}
        self.referer = referer
        # {"en":"Request mode: multiple are separated by commas (get, post, head, options, put, delete, trace, connect)", "zh_CN":"请求方式，多个使用逗号分隔（GET,POST,HEAD,OPTIONS,PUT,DELETE,TRACE,CONNECT）"}
        self.request_mode = request_mode

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.process_action, 'process_action')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.language is not None:
            result['language'] = self.language
        if self.domain is not None:
            result['domain'] = self.domain
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.process_action is not None:
            result['processAction'] = self.process_action
        if self.uri is not None:
            result['uri'] = self.uri
        if self.accurate_uri is not None:
            result['accurateUri'] = self.accurate_uri
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.accurate_user_agent is not None:
            result['accurateUserAgent'] = self.accurate_user_agent
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.referer is not None:
            result['referer'] = self.referer
        if self.request_mode is not None:
            result['requestMode'] = self.request_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('processAction') is not None:
            self.process_action = m.get('processAction')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('accurateUri') is not None:
            self.accurate_uri = m.get('accurateUri')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('accurateUserAgent') is not None:
            self.accurate_user_agent = m.get('accurateUserAgent')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('requestMode') is not None:
            self.request_mode = m.get('requestMode')
        return self


class QueryAttackLogDetailsResponseDataHttpRequestInfo(TeaModel):
    def __init__(
        self,
        location_ip: str = None,
        http_version: str = None,
        request_method: str = None,
        uri: str = None,
        referer: str = None,
        user_agent: str = None,
    ):
        # {'en':'locationIp','zh_CN':'ip地址'}
        self.location_ip = location_ip
        # {'en':'httpVersion','zh_CN':'HTTP版本'}
        self.http_version = http_version
        # {'en':'requestMethod','zh_CN':'请求方法'}
        self.request_method = request_method
        # {'en':'uri','zh_CN':'uri'}
        self.uri = uri
        # {'en':'referer','zh_CN':'referer'}
        self.referer = referer
        # {'en':'userAgent','zh_CN':'userAgent'}
        self.user_agent = user_agent

    def validate(self):
        self.validate_required(self.location_ip, 'location_ip')
        self.validate_required(self.http_version, 'http_version')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.uri, 'uri')
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.user_agent, 'user_agent')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_ip is not None:
            result['locationIp'] = self.location_ip
        if self.http_version is not None:
            result['httpVersion'] = self.http_version
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.uri is not None:
            result['uri'] = self.uri
        if self.referer is not None:
            result['referer'] = self.referer
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('locationIp') is not None:
            self.location_ip = m.get('locationIp')
        if m.get('httpVersion') is not None:
            self.http_version = m.get('httpVersion')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        return self


class QueryAttackLogDetailsResponseDataTcpRequestInfo(TeaModel):
    def __init__(
        self,
        location_ip: str = None,
        location_ip_en: str = None,
        ds_port: str = None,
        agreement: str = None,
    ):
        # {'en':'locationIp','zh_CN':'IP地理位置'}
        self.location_ip = location_ip
        # {'en':'locationIpEn','zh_CN':'IP地理位置英文名称'}
        self.location_ip_en = location_ip_en
        # {'en':'dsPort','zh_CN':'端口'}
        self.ds_port = ds_port
        # {'en':'agreement','zh_CN':'协议'}
        self.agreement = agreement

    def validate(self):
        self.validate_required(self.location_ip, 'location_ip')
        self.validate_required(self.location_ip_en, 'location_ip_en')
        self.validate_required(self.ds_port, 'ds_port')
        self.validate_required(self.agreement, 'agreement')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_ip is not None:
            result['locationIp'] = self.location_ip
        if self.location_ip_en is not None:
            result['locationIpEn'] = self.location_ip_en
        if self.ds_port is not None:
            result['dsPort'] = self.ds_port
        if self.agreement is not None:
            result['agreement'] = self.agreement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('locationIp') is not None:
            self.location_ip = m.get('locationIp')
        if m.get('locationIpEn') is not None:
            self.location_ip_en = m.get('locationIpEn')
        if m.get('dsPort') is not None:
            self.ds_port = m.get('dsPort')
        if m.get('agreement') is not None:
            self.agreement = m.get('agreement')
        return self


class QueryAttackLogDetailsResponseData(TeaModel):
    def __init__(
        self,
        access_time: str = None,
        client_ip: str = None,
        domain: str = None,
        attack_type: str = None,
        process_action: str = None,
        pro_strategy: str = None,
        state_code: str = None,
        http_request_info: QueryAttackLogDetailsResponseDataHttpRequestInfo = None,
        tcp_request_info: QueryAttackLogDetailsResponseDataTcpRequestInfo = None,
    ):
        # {'en':'accessTime','zh_CN':'访问时间'}
        self.access_time = access_time
        # {'en':'clientIp','zh_CN':'客户端IP'}
        self.client_ip = client_ip
        # {'en':'domain','zh_CN':'域名'}
        self.domain = domain
        # {'en':'attackType','zh_CN':'攻击类型'}
        self.attack_type = attack_type
        # {'en':'processAction','zh_CN':'处理动作'}
        self.process_action = process_action
        # {'en':'proStrategy','zh_CN':'防护策略'}
        self.pro_strategy = pro_strategy
        # {'en':'stateCode','zh_CN':'状态码'}
        self.state_code = state_code
        self.http_request_info = http_request_info
        self.tcp_request_info = tcp_request_info

    def validate(self):
        self.validate_required(self.access_time, 'access_time')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.process_action, 'process_action')
        self.validate_required(self.pro_strategy, 'pro_strategy')
        self.validate_required(self.state_code, 'state_code')
        self.validate_required(self.http_request_info, 'http_request_info')
        if self.http_request_info:
            self.http_request_info.validate()
        self.validate_required(self.tcp_request_info, 'tcp_request_info')
        if self.tcp_request_info:
            self.tcp_request_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_time is not None:
            result['accessTime'] = self.access_time
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.process_action is not None:
            result['processAction'] = self.process_action
        if self.pro_strategy is not None:
            result['proStrategy'] = self.pro_strategy
        if self.state_code is not None:
            result['stateCode'] = self.state_code
        if self.http_request_info is not None:
            result['httpRequestInfo'] = self.http_request_info.to_map()
        if self.tcp_request_info is not None:
            result['tcpRequestInfo'] = self.tcp_request_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTime') is not None:
            self.access_time = m.get('accessTime')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('processAction') is not None:
            self.process_action = m.get('processAction')
        if m.get('proStrategy') is not None:
            self.pro_strategy = m.get('proStrategy')
        if m.get('stateCode') is not None:
            self.state_code = m.get('stateCode')
        if m.get('httpRequestInfo') is not None:
            temp_model = QueryAttackLogDetailsResponseDataHttpRequestInfo()
            self.http_request_info = temp_model.from_map(m['httpRequestInfo'])
        if m.get('tcpRequestInfo') is not None:
            temp_model = QueryAttackLogDetailsResponseDataTcpRequestInfo()
            self.tcp_request_info = temp_model.from_map(m['tcpRequestInfo'])
        return self


class QueryAttackLogDetailsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: QueryAttackLogDetailsResponseData = None,
    ):
        # {"en":"response code", "zh_CN":"响应码，响应成功为200，响应失败见状态码"}
        self.code = code
        # {"en":"response message", "zh_CN":"响应信息，响应成功为success"}
        self.msg = msg
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            temp_model = QueryAttackLogDetailsResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryAttackLogDetailsPaths(TeaModel):
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


class QueryAttackLogDetailsParameters(TeaModel):
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


class QueryAttackLogDetailsRequestHeader(TeaModel):
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


class QueryAttackLogDetailsResponseHeader(TeaModel):
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






class GetWAFAttackLogRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        acts: List[str] = None,
        attack_types: List[str] = None,
        ips: List[str] = None,
        ip_condition: int = None,
        ip_location: str = None,
        urls: List[str] = None,
        url_condition: int = None,
        referer: str = None,
        referer_condition: int = None,
        user_agent: str = None,
        user_agent_condition: int = None,
        http_verisions: List[str] = None,
        status_codes: List[str] = None,
        status_code_condition: int = None,
        event_id: str = None,
        rule_ids: List[str] = None,
        rule_id_condition: int = None,
        rule_name: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {"en":"Action,default value: 1 and 2.
        #     1: Block
        #     2: GetWAFAttackLogLog", "zh_CN":"处理动作，默认值：1和2。
        #     1：拦截
        #     2：监控"}
        self.acts = acts
        # {"en":"Attack type, array. [SQL Injection: WAF_SQLI,
        # X-Site Scripting: WAF_XSS,
        # File Inclusion: WAF_RFI,
        # File Uploading: WAF_FILE_UPLOAD,
        # Command Injection: WAF_CMDI,
        # Directory Traversal: WAF_DIR_TRAVERSAL,
        # 3rd Party Component Exploit: WAF_THIRDCOMP,
        # XPATH/LDAP/SSI Injection: WAF_XPATH_LDAP_SSI,
        # Malicious Scanning: WAF_SCANNER,
        # Webshell Uploading: WAF_SHELL_BACKDOOR,
        # Unauthorized Download: WAF_FILE_DOWNLOAD,
        # Illegal Access(RFC): WAF_ILLEGAL,
        # Illegal HTTP Method(RFC): WAF_INVALID_METHOD,
        # Illegal HTTP Version(RFC): WAF_INVALID_PROTOCOL,
        # HTTP Buffer Overflow(RFC): WAF_BUF_OVERFLOW,
        # Server Sensitive Info Leakage[remarks:combination]: WAF_SERVER_ERROR_LEAKAGE,WAF_SENS_DATA_LEAKAGE,
        # XML Injection: WAF_XXE,
        # Custom Rules: WAF_CUSTOM_RULE,
        # Cookie Protection: WAF_COOKIE_PROTECT,
        # CSRF: WAF_CSRF,
        # Adware Insertion Prevention: WAF_UAD,
        # Webshell Access Detection: WAF_WEBSHELL,
        # Threat Intelligence: WAF_THREAT_INTELLIGENCE,
        # Credential Stuffing: WAF_HIT_LIB,
        # Server-side Request Forge: WAF_SSRF,
        # Malicious Dig: WAF_COIN,
        # Access Control[remarks:combination]: WAF_BLACK_IP,WAF_BLACK_URL,WAF_BLACK_UA,WAF_BLACK_HEADER,WAF_ACCESS_CONTROL,
        # Rate Limiting: WAF_FORCE_CRACKING,
        # Response Code Rate Limiting: WAF_BLACK_STATUS,
        # IP Repeated Violations: WAF_DYNAMIC_BLACK_IP]", "zh_CN":"攻击类型，数组。[SQL注入：WAF_SQLI,
        # XSS跨站：WAF_XSS,
        # 文件包含：WAF_RFI,
        # 文件上传：WAF_FILE_UPLOAD,
        # 命令注入：WAF_CMDI,
        # 目录遍历：WAF_DIR_TRAVERSAL,
        # 第三方组件漏洞：WAF_THIRDCOMP,
        # XPATH/LDAP/SSI注入：WAF_XPATH_LDAP_SSI,
        # 扫描器：WAF_SCANNER,
        # 木马后门：WAF_SHELL_BACKDOOR,
        # 非法下载：WAF_FILE_DOWNLOAD,
        # 非法请求(合规)：WAF_ILLEGAL,
        # 非法请求方法(合规)：WAF_INVALID_METHOD,
        # 非法请求协议(合规)：WAF_INVALID_PROTOCOL,
        # 缓冲区溢出(合规)：WAF_BUF_OVERFLOW,
        # 服务器信息泄露[备:多个组合]：WAF_SERVER_ERROR_LEAKAGE,WAF_SENS_DATA_LEAKAGE,
        # XML注入：WAF_XXE,
        # 自定义规则：WAF_CUSTOM_RULE,
        # Cookie防护：WAF_COOKIE_PROTECT,
        # CSRF：WAF_CSRF,
        # 恶意广告检测：WAF_UAD,
        # 后门识别：WAF_WEBSHELL,
        # 威胁情报：WAF_THREAT_INTELLIGENCE,
        # 撞库：WAF_HIT_LIB,
        # 服务端请求伪造：WAF_SSRF,
        # 恶意挖矿：WAF_COIN,
        # 访问控制[备:多个组合]：WAF_BLACK_IP,WAF_BLACK_URL,WAF_BLACK_UA,WAF_BLACK_HEADER,WAF_ACCESS_CONTROL,
        # 频率限制：WAF_FORCE_CRACKING,
        # 状态码限速：WAF_BLACK_STATUS,
        # 攻击IP惩罚：WAF_DYNAMIC_BLACK_IP]"}
        self.attack_types = attack_types
        # {"en":"Client IP.", "zh_CN":"客户端IP。"}
        self.ips = ips
        # {"en":"The logic of ip match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"IP条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.ip_condition = ip_condition
        # {"en":"The geographical location of IP.", "zh_CN":"IP地理位置。"}
        self.ip_location = ip_location
        # {"en":"Request Path.", "zh_CN":"请求路径。"}
        self.urls = urls
        # {"en":"The logic of path match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"路径条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.url_condition = url_condition
        # {"en":"HTTP request header: Referer.", "zh_CN":"请求Referer。"}
        self.referer = referer
        # {"en":"The logic of referer match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"Referer条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.referer_condition = referer_condition
        # {"en":"HTTP request header: User-Agent.", "zh_CN":"请求User-Agent。"}
        self.user_agent = user_agent
        # {"en":"The logic of user-agent match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"User-Agent条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.user_agent_condition = user_agent_condition
        # {"en":"HTTP version, such as:[HTTP/1.1].", "zh_CN":"HTTP版本，比如:[HTTP/1.1]。"}
        self.http_verisions = http_verisions
        # {"en":"HTTP response status code.", "zh_CN":"HTTP响应状态码。"}
        self.status_codes = status_codes
        # {"en":"The logic of status code match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"HTTP状态码条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.status_code_condition = status_code_condition
        # {"en":"Event ID.", "zh_CN":"事件ID。"}
        self.event_id = event_id
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.rule_ids = rule_ids
        # {"en":"The logic of rule id match conditions, default value 3.
        #     1: Equal
        #     2: Not Equal
        #     3: Included
        #     4: Excluded", "zh_CN":"规则ID条件匹配逻辑，默认值3。
        #     1：等于
        #     2：不等于
        #     3：包含
        #     4：不包含"}
        self.rule_id_condition = rule_id_condition
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"The language of response data, default value: cn.
        #     cn: Chinese
        #     en: English", "zh_CN":"返回内容的语言版本，默认值：cn。
        #     cn：中文
        #     en：英文"}
        self.lang = lang
        # {"en":"Current page.", "zh_CN":"当前页码。"}
        self.page_num = page_num
        # {"en":"Records per page, max 1000 records.", "zh_CN":"每页日志条数, 最大1000。"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.acts is not None:
            result['acts'] = self.acts
        if self.attack_types is not None:
            result['attackTypes'] = self.attack_types
        if self.ips is not None:
            result['ips'] = self.ips
        if self.ip_condition is not None:
            result['ipCondition'] = self.ip_condition
        if self.ip_location is not None:
            result['ipLocation'] = self.ip_location
        if self.urls is not None:
            result['urls'] = self.urls
        if self.url_condition is not None:
            result['urlCondition'] = self.url_condition
        if self.referer is not None:
            result['referer'] = self.referer
        if self.referer_condition is not None:
            result['refererCondition'] = self.referer_condition
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.user_agent_condition is not None:
            result['userAgentCondition'] = self.user_agent_condition
        if self.http_verisions is not None:
            result['httpVerisions'] = self.http_verisions
        if self.status_codes is not None:
            result['statusCodes'] = self.status_codes
        if self.status_code_condition is not None:
            result['statusCodeCondition'] = self.status_code_condition
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.rule_ids is not None:
            result['ruleIds'] = self.rule_ids
        if self.rule_id_condition is not None:
            result['ruleIdCondition'] = self.rule_id_condition
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.lang is not None:
            result['lang'] = self.lang
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('acts') is not None:
            self.acts = m.get('acts')
        if m.get('attackTypes') is not None:
            self.attack_types = m.get('attackTypes')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('ipCondition') is not None:
            self.ip_condition = m.get('ipCondition')
        if m.get('ipLocation') is not None:
            self.ip_location = m.get('ipLocation')
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('urlCondition') is not None:
            self.url_condition = m.get('urlCondition')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('refererCondition') is not None:
            self.referer_condition = m.get('refererCondition')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('userAgentCondition') is not None:
            self.user_agent_condition = m.get('userAgentCondition')
        if m.get('httpVerisions') is not None:
            self.http_verisions = m.get('httpVerisions')
        if m.get('statusCodes') is not None:
            self.status_codes = m.get('statusCodes')
        if m.get('statusCodeCondition') is not None:
            self.status_code_condition = m.get('statusCodeCondition')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('ruleIds') is not None:
            self.rule_ids = m.get('ruleIds')
        if m.get('ruleIdCondition') is not None:
            self.rule_id_condition = m.get('ruleIdCondition')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetWAFAttackLogLog(TeaModel):
    def __init__(
        self,
        referer: str = None,
        method: str = None,
        response_code: str = None,
        attack_type: str = None,
        rule_name: str = None,
        ip: str = None,
        uuid: str = None,
        url: str = None,
        client_id: str = None,
        content: str = None,
        rule_id: str = None,
        event_id: str = None,
        http_version: str = None,
        zone: str = None,
        domain: str = None,
        action: str = None,
        location: str = None,
        time: str = None,
        user_agent: str = None,
        detail_domain: str = None,
    ):
        # {'en':'Request referer.', 'zh_CN':'请求Referer。'}
        self.referer = referer
        # {'en':'HTTP request method.', 'zh_CN':'HTTP请求方式。'}
        self.method = method
        # {'en':'HTTP response status code.', 'zh_CN':'HTTP响应状态码。'}
        self.response_code = response_code
        # {'en':'Attack type.', 'zh_CN':'攻击类型。'}
        self.attack_type = attack_type
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Client IP.', 'zh_CN':'客户端IP。'}
        self.ip = ip
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.uuid = uuid
        # {'en':'Request Path.', 'zh_CN':'请求路径。'}
        self.url = url
        # {'en':'Client ID.', 'zh_CN':'客户端ID。'}
        self.client_id = client_id
        # {'en':'Detail information.', 'zh_CN':'详细信息。'}
        self.content = content
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.event_id = event_id
        # {'en':'HTTP version.', 'zh_CN':'HTTP版本。'}
        self.http_version = http_version
        # {'en':'Match area.', 'zh_CN':'匹配区域。'}
        self.zone = zone
        # {'en':'Domain.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'Action.
        #         1: Block
        #         2: GetWAFAttackLogLog', 'zh_CN':'处理动作。
        #         1：拦截
        #         2：监控'}
        self.action = action
        # {'en':'The geographical location of IP.', 'zh_CN':'IP地理位置。'}
        self.location = location
        # {'en':'Time.', 'zh_CN':'时间。'}
        self.time = time
        # {'en':'Request User-Agent.', 'zh_CN':'请求User-Agent。'}
        self.user_agent = user_agent
        # {'en':'Domain.', 'zh_CN':'域名。'}
        self.detail_domain = detail_domain

    def validate(self):
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.method, 'method')
        self.validate_required(self.response_code, 'response_code')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.url, 'url')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.http_version, 'http_version')
        self.validate_required(self.zone, 'zone')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.action, 'action')
        self.validate_required(self.location, 'location')
        self.validate_required(self.time, 'time')
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.detail_domain, 'detail_domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer is not None:
            result['referer'] = self.referer
        if self.method is not None:
            result['method'] = self.method
        if self.response_code is not None:
            result['responseCode'] = self.response_code
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.url is not None:
            result['url'] = self.url
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.content is not None:
            result['content'] = self.content
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.http_version is not None:
            result['httpVersion'] = self.http_version
        if self.zone is not None:
            result['zone'] = self.zone
        if self.domain is not None:
            result['domain'] = self.domain
        if self.action is not None:
            result['action'] = self.action
        if self.location is not None:
            result['location'] = self.location
        if self.time is not None:
            result['time'] = self.time
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.detail_domain is not None:
            result['detailDomain'] = self.detail_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('responseCode') is not None:
            self.response_code = m.get('responseCode')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('httpVersion') is not None:
            self.http_version = m.get('httpVersion')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('detailDomain') is not None:
            self.detail_domain = m.get('detailDomain')
        return self


class GetWAFAttackLogLogList(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_records: int = None,
        total_pages: int = None,
        log: List[GetWAFAttackLogLog] = None,
    ):
        # {'en':'Current page.', 'zh_CN':'当前页码。'}
        self.current_page = current_page
        # {'en':'Records per page.', 'zh_CN':'每页日志条数。'}
        self.page_size = page_size
        # {'en':'Total number of records.', 'zh_CN':'总记录数量。'}
        self.total_records = total_records
        # {'en':'Total pages.', 'zh_CN':'合计页数。'}
        self.total_pages = total_pages
        # {'en':'GetWAFAttackLogLog list.', 'zh_CN':'日志列表。'}
        self.log = log

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_records, 'total_records')
        self.validate_required(self.total_pages, 'total_pages')
        self.validate_required(self.log, 'log')
        if self.log:
            for k in self.log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_records is not None:
            result['totalRecords'] = self.total_records
        if self.total_pages is not None:
            result['totalPages'] = self.total_pages
        if self.log is not None:
            result['log'] = []
            for k in self.log:
                result['log'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')
        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')
        if m.get('log') is not None:
            self.log = []
            for k in m.get('log'):
                temp_model = GetWAFAttackLogLog()
                self.log.append(temp_model.from_map(k))
        return self


class GetWAFAttackLogResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFAttackLogLogList = None,
    ):
        # {"en":"Return 0 means success, please see <Error code> to check other status code.", "zh_CN":"0状态码表示请求成功，其他状态码说明请参见《错误码》。"}
        self.code = code
        # {"en":"Error message or Success.", "zh_CN":"错误信息或Success。"}
        self.message = message
        # {"en":"Return data.", "zh_CN":"返回值。"}
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
            temp_model = GetWAFAttackLogLogList()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFAttackLogPaths(TeaModel):
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


class GetWAFAttackLogParameters(TeaModel):
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


class GetWAFAttackLogRequestHeader(TeaModel):
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


class GetWAFAttackLogResponseHeader(TeaModel):
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




