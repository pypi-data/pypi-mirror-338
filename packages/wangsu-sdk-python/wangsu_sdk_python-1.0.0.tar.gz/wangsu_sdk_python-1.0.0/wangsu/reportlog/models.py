# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class CheckIsWhiteIpRequest(TeaModel):
    def __init__(
        self,
        white_name: str = None,
        type: str = None,
        white_hash: str = None,
        ip: str = None,
    ):
        # {"en":"entername", "zh_CN":"客户英文名"}
        self.white_name = white_name
        # {"en":"ip_white type:
        # comm_white
        # relay_white", "zh_CN":"白名单类型 
        # 普通白名单：comm_white
        # 中转白名单：relay_white"}
        self.type = type
        # {"en":"ip white hash verify value
        # format hash1:hash2", "zh_CN":"白名单hash值
        # hash1:hash2
        # 如果ipv6独立
        # 则：hash1:hash2:y"}
        self.white_hash = white_hash
        # {"en":"check ips,split by ,", "zh_CN":"检查的ip，多个,隔开"}
        self.ip = ip

    def validate(self):
        self.validate_required(self.white_name, 'white_name')
        self.validate_required(self.white_hash, 'white_hash')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_name is not None:
            result['white_name'] = self.white_name
        if self.type is not None:
            result['type'] = self.type
        if self.white_hash is not None:
            result['white_hash'] = self.white_hash
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('white_name') is not None:
            self.white_name = m.get('white_name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('white_hash') is not None:
            self.white_hash = m.get('white_hash')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class CheckIsWhiteIpResponse(TeaModel):
    def __init__(
        self,
        ret_code: str = None,
        data: List[str] = None,
    ):
        # {"en":"Return status code
        # success represents normal
        # fail  represents abnormality", "zh_CN":"返回状态码 
        # success 代表正常
        # fail 代表异常"}
        self.ret_code = ret_code
        # {"en":"return is every ip in use with yes or no", "zh_CN":"返回每个ip是否是在用白名单IP，格式为yes或者no"}
        self.data = data

    def validate(self):
        self.validate_required(self.ret_code, 'ret_code')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['ret_code'] = self.ret_code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ret_code') is not None:
            self.ret_code = m.get('ret_code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CheckIsWhiteIpPaths(TeaModel):
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


class CheckIsWhiteIpParameters(TeaModel):
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


class CheckIsWhiteIpRequestHeader(TeaModel):
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


class CheckIsWhiteIpResponseHeader(TeaModel):
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






class GetBotAttackIncidentLogDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
        attack_type: str = None,
        act: str = None,
        location: str = None,
        ip: str = None,
        url: str = None,
        referer: str = None,
        status_code: str = None,
        user_agent: str = None,
        uuid: str = None,
        page_size: int = None,
        current_page: int = None,
        client_id: str = None,
        browser_fp: str = None,
        rule_name: str = None,
        bot_rule_name: str = None,
        ip_condition: int = None,
        url_condition: int = None,
        referer_condition: int = None,
        status_code_conditon: int = None,
        user_agent_condition: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开。"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e.'GTM+8'.", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang
        # {"en":"Attack Type,separate by ';'.", "zh_CN":"攻击类型。多个以;隔开。"}
        self.attack_type = attack_type
        # {"en":"Action. 
        #  1:Interception 
        #  2:Log 
        #  7:Flag 
        #  8:Captcha", "zh_CN":"处理动作。 
        #  1：拦截 
        #  2：监控 
        #  7：攻击标记 
        #  8：验证码"}
        self.act = act
        # {"en":"IP location.", "zh_CN":"IP地理位置。"}
        self.location = location
        # {"en":"Client IP.", "zh_CN":"客户端IP。"}
        self.ip = ip
        # {"en":"URI.", "zh_CN":"URI。"}
        self.url = url
        # {"en":"Referer.", "zh_CN":"Referer。"}
        self.referer = referer
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.status_code = status_code
        # {"en":"User-Agent.", "zh_CN":"User-Agent。"}
        self.user_agent = user_agent
        # {"en":"Event ID.", "zh_CN":"事件ID。"}
        self.uuid = uuid
        # {"en":"The number of entries displayed per page.Maximum limit 10,000.", "zh_CN":"每页显示的条目数。最大限制10,000。"}
        self.page_size = page_size
        # {"en":"Current page number.", "zh_CN":"当前页码。"}
        self.current_page = current_page
        # {"en":"Client ID.", "zh_CN":"客户端ID。"}
        self.client_id = client_id
        # {"en":"Browser Fingerprint.", "zh_CN":"浏览器指纹。"}
        self.browser_fp = browser_fp
        # {"en":"Rule name.", "zh_CN":"规则名。"}
        self.rule_name = rule_name
        # {"en":"Bot rule name.", "zh_CN":"Bot规则名。"}
        self.bot_rule_name = bot_rule_name
        # {"en":"Query criteria matching method of 'Client IP'.Default value: 3. 
        #  1:equal 
        #  2:not equal 
        #  3:Include 
        #  4:Not Include.", "zh_CN":"'客户端IP'查询条件匹配方式。默认值：3。 
        #  1：相等 
        #  2：不相等 
        #  3：包含 
        #  4：不包含"}
        self.ip_condition = ip_condition
        # {"en":"Query criteria matching method of 'URI'. Default value: 3 
        #  1:equal 
        #  2:not equal 
        #  3:Include 
        #  4:Not Include.", "zh_CN":"'客户端URL'查询条件匹配方式。默认值：3。 
        #  1：相等 
        #  2：不相等 
        #  3：包含 
        #  4：不包含"}
        self.url_condition = url_condition
        # {"en":"Query criteria matching method of 'Referer'. Default value: 3 
        #  1:equal 
        #  2:not equal 
        #  3:Include 
        #  4:Not Include.", "zh_CN":"'客户端Rerfer'查询条件匹配方式。默认值：3。 
        #  1：相等 
        #  2：不相等 
        #  3：包含 
        #  4：不包含"}
        self.referer_condition = referer_condition
        # {"en":"Query criteria matching method of 'Response code'.Default value: 3 
        #  1:equal 
        #  2:not equal 
        #  3:Include 
        #  4:Not Include.", "zh_CN":"'客户端状态码'查询条件匹配方式。默认值：3。 
        #  1：相等 
        #  2：不相等 
        #  3：包含 
        #  4：不包含"}
        self.status_code_conditon = status_code_conditon
        # {"en":"Query criteria matching method of 'User-Agent'.Default value: 3 
        #  1:equal 
        #  2:not equal 
        #  3:Include 
        #  4:Not Include. ", "zh_CN":"'客户端UA'查询条件匹配方式。默认值：3。 
        #  1：相等 
        #  2：不相等 
        #  3：包含 
        #  4：不包含"}
        self.user_agent_condition = user_agent_condition

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.lang is not None:
            result['lang'] = self.lang
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.act is not None:
            result['act'] = self.act
        if self.location is not None:
            result['location'] = self.location
        if self.ip is not None:
            result['ip'] = self.ip
        if self.url is not None:
            result['url'] = self.url
        if self.referer is not None:
            result['referer'] = self.referer
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.browser_fp is not None:
            result['browserFp'] = self.browser_fp
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.bot_rule_name is not None:
            result['botRuleName'] = self.bot_rule_name
        if self.ip_condition is not None:
            result['ipCondition'] = self.ip_condition
        if self.url_condition is not None:
            result['urlCondition'] = self.url_condition
        if self.referer_condition is not None:
            result['refererCondition'] = self.referer_condition
        if self.status_code_conditon is not None:
            result['statusCodeConditon'] = self.status_code_conditon
        if self.user_agent_condition is not None:
            result['userAgentCondition'] = self.user_agent_condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('browserFp') is not None:
            self.browser_fp = m.get('browserFp')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('botRuleName') is not None:
            self.bot_rule_name = m.get('botRuleName')
        if m.get('ipCondition') is not None:
            self.ip_condition = m.get('ipCondition')
        if m.get('urlCondition') is not None:
            self.url_condition = m.get('urlCondition')
        if m.get('refererCondition') is not None:
            self.referer_condition = m.get('refererCondition')
        if m.get('statusCodeConditon') is not None:
            self.status_code_conditon = m.get('statusCodeConditon')
        if m.get('userAgentCondition') is not None:
            self.user_agent_condition = m.get('userAgentCondition')
        return self


class GetBotAttackIncidentLogDataResponseDataList(TeaModel):
    def __init__(
        self,
        referer: str = None,
        browser_fp: str = None,
        attack_type: str = None,
        rule_name: str = None,
        ip: str = None,
        uuid: str = None,
        version: str = None,
        client_id: str = None,
        url: str = None,
        block_id: str = None,
        content: str = None,
        mode: str = None,
        final_rule_id: int = None,
        event_type: str = None,
        act: str = None,
        zone: str = None,
        attack_time: str = None,
        strategy_desc: str = None,
        host: str = None,
        location: str = None,
        strategy_name: str = None,
        user_agent: str = None,
        detail_host: str = None,
        status_code: int = None,
    ):
        # {"en":"Referer.", "zh_CN":"Referer。"}
        self.referer = referer
        # {"en":"Browser Fingerprint.", "zh_CN":"浏览器指纹。"}
        self.browser_fp = browser_fp
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.attack_type = attack_type
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"IP.", "zh_CN":"IP。"}
        self.ip = ip
        # {"en":"Event id.", "zh_CN":"事件ID。"}
        self.uuid = uuid
        # {"en":"Version.", "zh_CN":"版本号。"}
        self.version = version
        # {"en":"Client id.", "zh_CN":"客户端ID。"}
        self.client_id = client_id
        # {"en":"URI.", "zh_CN":"URI。"}
        self.url = url
        # {"en":"Block id.", "zh_CN":"Block id。"}
        self.block_id = block_id
        # {"en":"Content.", "zh_CN":"内容。"}
        self.content = content
        # {"en":"Request method.", "zh_CN":"请求方法。"}
        self.mode = mode
        # {"en":"Rule id.", "zh_CN":"规则id。"}
        self.final_rule_id = final_rule_id
        # {"en":"Event type.", "zh_CN":"事件类型。"}
        self.event_type = event_type
        # {"en":"Processing action.", "zh_CN":"处理动作。"}
        self.act = act
        # {"en":"Zone.", "zh_CN":"时区。"}
        self.zone = zone
        # {"en":"Attack time.", "zh_CN":"攻击时间"}
        self.attack_time = attack_time
        # {"en":"Strategy description.", "zh_CN":"策略描述。。"}
        self.strategy_desc = strategy_desc
        # {"en":"Domain.", "zh_CN":"域名。"}
        self.host = host
        # {"en":"IP geographical location.", "zh_CN":"IP地理位置。"}
        self.location = location
        # {"en":"Strategy name.", "zh_CN":"策略名称。"}
        self.strategy_name = strategy_name
        # {"en":"User-Agent.", "zh_CN":"User-Agent"}
        self.user_agent = user_agent
        # {"en":"Domain detail.", "zh_CN":"域名详情。"}
        self.detail_host = detail_host
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.browser_fp, 'browser_fp')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.version, 'version')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.url, 'url')
        self.validate_required(self.block_id, 'block_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.final_rule_id, 'final_rule_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.act, 'act')
        self.validate_required(self.zone, 'zone')
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.strategy_desc, 'strategy_desc')
        self.validate_required(self.host, 'host')
        self.validate_required(self.location, 'location')
        self.validate_required(self.strategy_name, 'strategy_name')
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.detail_host, 'detail_host')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer is not None:
            result['referer'] = self.referer
        if self.browser_fp is not None:
            result['browser_fp'] = self.browser_fp
        if self.attack_type is not None:
            result['attack_type'] = self.attack_type
        if self.rule_name is not None:
            result['rule_name'] = self.rule_name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.version is not None:
            result['version'] = self.version
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.url is not None:
            result['url'] = self.url
        if self.block_id is not None:
            result['block_id'] = self.block_id
        if self.content is not None:
            result['content'] = self.content
        if self.mode is not None:
            result['mode'] = self.mode
        if self.final_rule_id is not None:
            result['final_rule_id'] = self.final_rule_id
        if self.event_type is not None:
            result['event_type'] = self.event_type
        if self.act is not None:
            result['act'] = self.act
        if self.zone is not None:
            result['zone'] = self.zone
        if self.attack_time is not None:
            result['attack_time'] = self.attack_time
        if self.strategy_desc is not None:
            result['strategy_desc'] = self.strategy_desc
        if self.host is not None:
            result['host'] = self.host
        if self.location is not None:
            result['location'] = self.location
        if self.strategy_name is not None:
            result['strategy_name'] = self.strategy_name
        if self.user_agent is not None:
            result['user_agent'] = self.user_agent
        if self.detail_host is not None:
            result['detail_host'] = self.detail_host
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('browser_fp') is not None:
            self.browser_fp = m.get('browser_fp')
        if m.get('attack_type') is not None:
            self.attack_type = m.get('attack_type')
        if m.get('rule_name') is not None:
            self.rule_name = m.get('rule_name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('block_id') is not None:
            self.block_id = m.get('block_id')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('final_rule_id') is not None:
            self.final_rule_id = m.get('final_rule_id')
        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('attack_time') is not None:
            self.attack_time = m.get('attack_time')
        if m.get('strategy_desc') is not None:
            self.strategy_desc = m.get('strategy_desc')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('strategy_name') is not None:
            self.strategy_name = m.get('strategy_name')
        if m.get('user_agent') is not None:
            self.user_agent = m.get('user_agent')
        if m.get('detail_host') is not None:
            self.detail_host = m.get('detail_host')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetBotAttackIncidentLogDataResponseData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        first_page: int = None,
        last_page: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page_count: int = None,
        list: List[GetBotAttackIncidentLogDataResponseDataList] = None,
    ):
        # {"en":"Rule name.", "zh_CN":"当前页码。"}
        self.current_page = current_page
        # {"en":"Current page number.", "zh_CN":"首页页码。"}
        self.first_page = first_page
        # {"en":"last page number.", "zh_CN":"末页页码。"}
        self.last_page = last_page
        # {"en":"The number of entries displayed per page.Maximum limit 10,000.", "zh_CN":"每页显示的条目数。最大限制10,000。"}
        self.page_size = page_size
        # {"en":"Total entries.Maximum limit 1,000,000.", "zh_CN":"总条目数。最大限制1,000,000。"}
        self.total_count = total_count
        # {"en":"Total page count.", "zh_CN":"总页数。"}
        self.total_page_count = total_page_count
        # {"en":"Data List", "zh_CN":"数据列表"}
        self.list = list

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.first_page, 'first_page')
        self.validate_required(self.last_page, 'last_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page_count, 'total_page_count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.first_page is not None:
            result['firstPage'] = self.first_page
        if self.last_page is not None:
            result['lastPage'] = self.last_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.total_page_count is not None:
            result['totalPageCount'] = self.total_page_count
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('firstPage') is not None:
            self.first_page = m.get('firstPage')
        if m.get('lastPage') is not None:
            self.last_page = m.get('lastPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('totalPageCount') is not None:
            self.total_page_count = m.get('totalPageCount')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = GetBotAttackIncidentLogDataResponseDataList()
                self.list.append(temp_model.from_map(k))
        return self


class GetBotAttackIncidentLogDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetBotAttackIncidentLogDataResponseData = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据"}
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
            temp_model = GetBotAttackIncidentLogDataResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetBotAttackIncidentLogDataPaths(TeaModel):
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


class GetBotAttackIncidentLogDataParameters(TeaModel):
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


class GetBotAttackIncidentLogDataRequestHeader(TeaModel):
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


class GetBotAttackIncidentLogDataResponseHeader(TeaModel):
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




