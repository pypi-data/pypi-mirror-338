# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class L7DdosTrendRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time
        # {"en":"Hostname list.", "zh_CN":"域名数组。"}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.domains, 'domains')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class L7DdosTrendAttackedUrl(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        attack_count: int = None,
        def_count: int = None,
        ai_count: int = None,
        ip_count: int = None,
        area_count: int = None,
        rule_count: int = None,
        limit_count: int = None,
        time: str = None,
    ):
        # {"en":"All Requests(QPS)", "zh_CN":"所有请求（QPS）"}
        self.all_count = all_count
        # {"en":"L7 DDoS Attack(QPS)", "zh_CN":"CC攻击（QPS）"}
        self.attack_count = attack_count
        # {"en":"Managed Ruleset Protection(QPS)", "zh_CN":"内置规则防护（QPS）"}
        self.def_count = def_count
        # {"en":"Adaptive DDoS Protection(QPS)", "zh_CN":"AI智能防护（QPS）"}
        self.ai_count = ai_count
        # {"en":"IP Block(QPS)", "zh_CN":"IP封禁（QPS）"}
        self.ip_count = ip_count
        # {"en":"Geo Block(QPS)", "zh_CN":"区域封禁（QPS）"}
        self.area_count = area_count
        # {"en":"Custom Rules(QPS)", "zh_CN":"自定义规则（QPS）"}
        self.rule_count = rule_count
        # {"en":"Rate Limit(QPS)", "zh_CN":"频率限制（QPS）"}
        self.limit_count = limit_count
        # {"en":"Time.", "zh_CN":"时间。"}
        self.time = time

    def validate(self):
        self.validate_required(self.all_count, 'all_count')
        self.validate_required(self.attack_count, 'attack_count')
        self.validate_required(self.def_count, 'def_count')
        self.validate_required(self.ai_count, 'ai_count')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.area_count, 'area_count')
        self.validate_required(self.rule_count, 'rule_count')
        self.validate_required(self.limit_count, 'limit_count')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_count is not None:
            result['all_count'] = self.all_count
        if self.attack_count is not None:
            result['attack_count'] = self.attack_count
        if self.def_count is not None:
            result['def_count'] = self.def_count
        if self.ai_count is not None:
            result['ai_count'] = self.ai_count
        if self.ip_count is not None:
            result['ip_count'] = self.ip_count
        if self.area_count is not None:
            result['area_count'] = self.area_count
        if self.rule_count is not None:
            result['rule_count'] = self.rule_count
        if self.limit_count is not None:
            result['limit_count'] = self.limit_count
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_count') is not None:
            self.all_count = m.get('all_count')
        if m.get('attack_count') is not None:
            self.attack_count = m.get('attack_count')
        if m.get('def_count') is not None:
            self.def_count = m.get('def_count')
        if m.get('ai_count') is not None:
            self.ai_count = m.get('ai_count')
        if m.get('ip_count') is not None:
            self.ip_count = m.get('ip_count')
        if m.get('area_count') is not None:
            self.area_count = m.get('area_count')
        if m.get('rule_count') is not None:
            self.rule_count = m.get('rule_count')
        if m.get('limit_count') is not None:
            self.limit_count = m.get('limit_count')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class L7DdosTrendPeak(TeaModel):
    def __init__(
        self,
        peak_value: int = None,
        peak_time: str = None,
    ):
        # {"en":"L7DdosTrendPeak Attack Value", "zh_CN":"峰值（QPS）"}
        self.peak_value = peak_value
        # {"en":"L7DdosTrendPeak Attack Time", "zh_CN":"峰值时间"}
        self.peak_time = peak_time

    def validate(self):
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_value is not None:
            result['peak_value'] = self.peak_value
        if self.peak_time is not None:
            result['peak_time'] = self.peak_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('peak_value') is not None:
            self.peak_value = m.get('peak_value')
        if m.get('peak_time') is not None:
            self.peak_time = m.get('peak_time')
        return self


class L7DdosTrendResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[L7DdosTrendAttackedUrl] = None,
        peak_qps: List[L7DdosTrendPeak] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data
        # {"en":"L7DdosTrendPeak Attack QPS", "zh_CN":"CC攻击QPS峰值"}
        self.peak_qps = peak_qps

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.peak_qps, 'peak_qps')
        if self.peak_qps:
            for k in self.peak_qps:
                if k:
                    k.validate()

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
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.peak_qps is not None:
            result['peak_qps'] = []
            for k in self.peak_qps:
                result['peak_qps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = L7DdosTrendAttackedUrl()
                self.data.append(temp_model.from_map(k))
        if m.get('peak_qps') is not None:
            self.peak_qps = []
            for k in m.get('peak_qps'):
                temp_model = L7DdosTrendPeak()
                self.peak_qps.append(temp_model.from_map(k))
        return self


class L7DdosTrendPaths(TeaModel):
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


class L7DdosTrendParameters(TeaModel):
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


class L7DdosTrendRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class L7DdosTrendResponseHeader(TeaModel):
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






class GetbotrequestuseragentTopdataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        top_num: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetbotrequestuseragentTopdataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Bot request count.", "zh_CN":"bot请求数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetbotrequestuseragentTopdataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetbotrequestuseragentTopdataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetbotrequestuseragentTopdataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetbotrequestuseragentTopdataPaths(TeaModel):
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


class GetbotrequestuseragentTopdataParameters(TeaModel):
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


class GetbotrequestuseragentTopdataRequestHeader(TeaModel):
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


class GetbotrequestuseragentTopdataResponseHeader(TeaModel):
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






class GetTriggeredCustomRulesRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTriggeredCustomRulesRuleHitDTO(TeaModel):
    def __init__(
        self,
        act: str = None,
        value: int = None,
    ):
        # {'en':'Action.', 'zh_CN':'采取动作。'}
        self.act = act
        # {'en':'Hit times.', 'zh_CN':'命中数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTriggeredCustomRulesRuleTopDTO(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        scene: str = None,
        hits: List[GetTriggeredCustomRulesRuleHitDTO] = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Protected target.', 'zh_CN':'业务场景。'}
        self.scene = scene
        # {'en':'Trigger times, sort by times.', 'zh_CN':'触发次数，按次数排序。'}
        self.hits = hits

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.scene, 'scene')
        self.validate_required(self.hits, 'hits')
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.scene is not None:
            result['scene'] = self.scene
        if self.hits is not None:
            result['hits'] = []
            for k in self.hits:
                result['hits'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('hits') is not None:
            self.hits = []
            for k in m.get('hits'):
                temp_model = GetTriggeredCustomRulesRuleHitDTO()
                self.hits.append(temp_model.from_map(k))
        return self


class GetTriggeredCustomRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTriggeredCustomRulesRuleTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTriggeredCustomRulesRuleTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTriggeredCustomRulesPaths(TeaModel):
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


class GetTriggeredCustomRulesParameters(TeaModel):
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


class GetTriggeredCustomRulesRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTriggeredCustomRulesResponseHeader(TeaModel):
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






class L4DdosEventRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class L4DdosEventAttackedUrl(TeaModel):
    def __init__(
        self,
        duration: str = None,
        start_time: str = None,
        attack_type: List[str] = None,
        end_time: str = None,
        max_time: str = None,
        status: str = None,
        max_value: str = None,
    ):
        # {"en":"Duration.", "zh_CN":"持续时间。"}
        self.duration = duration
        # {"en":"Start time.", "zh_CN":"开始时间。"}
        self.start_time = start_time
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.attack_type = attack_type
        # {"en":"End time.", "zh_CN":"结束时间。"}
        self.end_time = end_time
        # {"en":"Max time.", "zh_CN":"峰值时间。"}
        self.max_time = max_time
        # {"en":"Status.", "zh_CN":"状态 1.清洗结束 0.清洗中。"}
        self.status = status
        # {"en":"Peak bandwidth.", "zh_CN":"峰值（Mbps）。"}
        self.max_value = max_value

    def validate(self):
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.max_time, 'max_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.max_value, 'max_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.attack_type is not None:
            result['attack_type'] = self.attack_type
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.max_time is not None:
            result['max_time'] = self.max_time
        if self.status is not None:
            result['status'] = self.status
        if self.max_value is not None:
            result['max_value'] = self.max_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('attack_type') is not None:
            self.attack_type = m.get('attack_type')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('max_time') is not None:
            self.max_time = m.get('max_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('max_value') is not None:
            self.max_value = m.get('max_value')
        return self


class L4DdosEventResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[L4DdosEventAttackedUrl] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = L4DdosEventAttackedUrl()
                self.data.append(temp_model.from_map(k))
        return self


class L4DdosEventPaths(TeaModel):
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


class L4DdosEventParameters(TeaModel):
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


class L4DdosEventRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class L4DdosEventResponseHeader(TeaModel):
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






class GetDistributionOfWAFAttackSourceRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        policys: List[str] = None,
        lang: str = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {'en':'Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]', 'zh_CN':'触发策略类型，数组。
        # [protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]'}
        self.policys = policys
        # {"en":"The language of response data, default value: cn.
        #     cn: Chinese
        #     en: English", "zh_CN":"返回内容的语言版本，默认值：cn。
        #     cn：中文
        #     en：英文"}
        self.lang = lang

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.policys is not None:
            result['policys'] = self.policys
        if self.lang is not None:
            result['lang'] = self.lang
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
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class GetDistributionOfWAFAttackSourceAttackArea(TeaModel):
    def __init__(
        self,
        country: str = None,
        province: str = None,
        total_count: int = None,
    ):
        # {"en":"Country.", "zh_CN":"国家。"}
        self.country = country
        # {"en":"Province.", "zh_CN":"省份。"}
        self.province = province
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.country, 'country')
        self.validate_required(self.province, 'province')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['country'] = self.country
        if self.province is not None:
            result['province'] = self.province
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetDistributionOfWAFAttackSourceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetDistributionOfWAFAttackSourceAttackArea] = None,
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
                temp_model = GetDistributionOfWAFAttackSourceAttackArea()
                self.data.append(temp_model.from_map(k))
        return self


class GetDistributionOfWAFAttackSourcePaths(TeaModel):
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


class GetDistributionOfWAFAttackSourceParameters(TeaModel):
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


class GetDistributionOfWAFAttackSourceRequestHeader(TeaModel):
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


class GetDistributionOfWAFAttackSourceResponseHeader(TeaModel):
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






class GetRuleStatusStatisticsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        lang: str = None,
    ):
        # {'en':'Domain name.', 'zh_CN':'域名。'}
        self.domain = domain
        # {"en":"The language of response data, default value: cn.
        #     cn: Chinese
        #     en: English", "zh_CN":"返回内容的语言版本，默认值：cn。
        #     cn：中文
        #     en：英文"}
        self.lang = lang

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class GetRuleStatusStatisticsStatisticalRuleStatus(TeaModel):
    def __init__(
        self,
        attack_type_name: str = None,
        type: str = None,
        log: int = None,
        block: int = None,
        off: int = None,
    ):
        # {'en':'Attack type name.', 'zh_CN':'攻击类型名称。'}
        self.attack_type_name = attack_type_name
        # {'en':'Attack type.', 'zh_CN':'攻击类型。'}
        self.type = type
        # {'en':'The number of rules that enable monitoring for this domain name.', 'zh_CN':'该域名开启监控的规则数。'}
        self.log = log
        # {'en':'The number of blocked rules for this domain name.', 'zh_CN':'该域名开启拦截的规则数。'}
        self.block = block
        # {'en':'The number of rules closed for this domain name.', 'zh_CN':'该域名关闭的规则数。'}
        self.off = off

    def validate(self):
        self.validate_required(self.attack_type_name, 'attack_type_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.log, 'log')
        self.validate_required(self.block, 'block')
        self.validate_required(self.off, 'off')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type_name is not None:
            result['attackTypeName'] = self.attack_type_name
        if self.type is not None:
            result['type'] = self.type
        if self.log is not None:
            result['log'] = self.log
        if self.block is not None:
            result['block'] = self.block
        if self.off is not None:
            result['off'] = self.off
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackTypeName') is not None:
            self.attack_type_name = m.get('attackTypeName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('log') is not None:
            self.log = m.get('log')
        if m.get('block') is not None:
            self.block = m.get('block')
        if m.get('off') is not None:
            self.off = m.get('off')
        return self


class GetRuleStatusStatisticsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetRuleStatusStatisticsStatisticalRuleStatus = None,
    ):
        # {"en":"Return 0 means success, please see <Error code> to check other status code.", "zh_CN":"0状态码表示请求成功，其他状态码说明请参见《错误码》。"}
        self.code = code
        # {"en":"error message or Success.", "zh_CN":"错误信息或Success。"}
        self.message = message
        # {'en':'return data.','zh_CN':'返回值。'}
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
            temp_model = GetRuleStatusStatisticsStatisticalRuleStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class GetRuleStatusStatisticsPaths(TeaModel):
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


class GetRuleStatusStatisticsParameters(TeaModel):
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


class GetRuleStatusStatisticsRequestHeader(TeaModel):
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


class GetRuleStatusStatisticsResponseHeader(TeaModel):
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






class L7DdosEventsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        hostnames: List[str] = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time
        # {"en":"Hostname list.", "zh_CN":"域名数组。"}
        self.hostnames = hostnames

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        return self


class L7DdosEventsAttackedUrl(TeaModel):
    def __init__(
        self,
        duration: str = None,
        start_time: str = None,
        total_count: str = None,
        end_time: str = None,
        channel: str = None,
        max_time: str = None,
        status: str = None,
    ):
        # {"en":"Duration(minutes)", "zh_CN":"持续时间。"}
        self.duration = duration
        # {"en":"Start Time", "zh_CN":"开始时间。"}
        self.start_time = start_time
        # {"en":"Attacked Requests", "zh_CN":"攻击次数。"}
        self.total_count = total_count
        # {"en":"End time", "zh_CN":"结束时间。"}
        self.end_time = end_time
        # {"en":"Attacked Hostnames", "zh_CN":"被攻击域名。"}
        self.channel = channel
        # {"en":"Peak Time", "zh_CN":"峰值时间。"}
        self.max_time = max_time
        # {"en":"Status.(1. Mitigated 0. Mitigating)", "zh_CN":"状态。（ 1.清洗结束 0.清洗中）"}
        self.status = status

    def validate(self):
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.max_time, 'max_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.total_count is not None:
            result['total_count'] = self.total_count
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.channel is not None:
            result['channel'] = self.channel
        if self.max_time is not None:
            result['max_time'] = self.max_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('max_time') is not None:
            self.max_time = m.get('max_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class L7DdosEventsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[L7DdosEventsAttackedUrl] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = L7DdosEventsAttackedUrl()
                self.data.append(temp_model.from_map(k))
        return self


class L7DdosEventsPaths(TeaModel):
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


class L7DdosEventsParameters(TeaModel):
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


class L7DdosEventsRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class L7DdosEventsResponseHeader(TeaModel):
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






class GetApiNumberRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetApiNumberVo(TeaModel):
    def __init__(
        self,
        active: int = None,
        inactive: int = None,
        stop: int = None,
    ):
        # {"en":"Activate.", "zh_CN":"激活。"}
        self.active = active
        # {"en":"To be activated.", "zh_CN":"待激活。"}
        self.inactive = inactive
        # {"en":"Deactivate.", "zh_CN":"停用。"}
        self.stop = stop

    def validate(self):
        self.validate_required(self.active, 'active')
        self.validate_required(self.inactive, 'inactive')
        self.validate_required(self.stop, 'stop')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.inactive is not None:
            result['inactive'] = self.inactive
        if self.stop is not None:
            result['stop'] = self.stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('inactive') is not None:
            self.inactive = m.get('inactive')
        if m.get('stop') is not None:
            self.stop = m.get('stop')
        return self


class GetApiNumberResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetApiNumberVo = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
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
            temp_model = GetApiNumberVo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetApiNumberPaths(TeaModel):
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


class GetApiNumberParameters(TeaModel):
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


class GetApiNumberRequestHeader(TeaModel):
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


class GetApiNumberResponseHeader(TeaModel):
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






class GetTotalRequestNumberRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetTotalRequestNumberVo(TeaModel):
    def __init__(
        self,
        total: int = None,
        attack: int = None,
    ):
        # {"en":"The total number of requests.", "zh_CN":"总请求数。"}
        self.total = total
        # {"en":"The number of API requests detected and blocked by API Shield.", "zh_CN":"缓解次数。"}
        self.attack = attack

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.attack, 'attack')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.attack is not None:
            result['attack'] = self.attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        return self


class GetTotalRequestNumberResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetTotalRequestNumberVo = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
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
            temp_model = GetTotalRequestNumberVo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetTotalRequestNumberPaths(TeaModel):
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


class GetTotalRequestNumberParameters(TeaModel):
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


class GetTotalRequestNumberRequestHeader(TeaModel):
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


class GetTotalRequestNumberResponseHeader(TeaModel):
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






class GetWAFAttackIPRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        policys: List[str] = None,
        top_num: int = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {'en':'Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]', 'zh_CN':'触发策略类型，数组。
        # [protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]'}
        self.policys = policys
        # {"en":"Attacker IP Top value, default Top 100, only support Top 1000.", "zh_CN":"攻击IP Top值，默认返回Top 100，最大只能查询 Top 1000。"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.policys is not None:
            result['policys'] = self.policys
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetWAFAttackIPAttackIp(TeaModel):
    def __init__(
        self,
        ip: str = None,
        block_count: int = None,
        total_count: int = None,
        monitor_count: int = None,
        country_en: str = None,
        country_cn: str = None,
        province_en: str = None,
        province_cn: str = None,
        city_en: str = None,
        city_cn: str = None,
    ):
        # {"en":"Attacker IP.", "zh_CN":"攻击IP。"}
        self.ip = ip
        # {"en":"Block requests.", "zh_CN":"拦截请求数。"}
        self.block_count = block_count
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.total_count = total_count
        # {"en":"Log requests.", "zh_CN":"监控请求数。"}
        self.monitor_count = monitor_count
        # {"en":"Country(English)", "zh_CN":"国家英文。"}
        self.country_en = country_en
        # {"en":"Country(Chinese)", "zh_CN":"国家中文。"}
        self.country_cn = country_cn
        # {"en":"Province(English)", "zh_CN":"省份英文。"}
        self.province_en = province_en
        # {"en":"Province(Chinese)", "zh_CN":"省份中文。"}
        self.province_cn = province_cn
        # {"en":"City(English)", "zh_CN":"城市英文。"}
        self.city_en = city_en
        # {"en":"City(Chinese)", "zh_CN":"城市中文。"}
        self.city_cn = city_cn

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.block_count, 'block_count')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.monitor_count, 'monitor_count')
        self.validate_required(self.country_en, 'country_en')
        self.validate_required(self.country_cn, 'country_cn')
        self.validate_required(self.province_en, 'province_en')
        self.validate_required(self.province_cn, 'province_cn')
        self.validate_required(self.city_en, 'city_en')
        self.validate_required(self.city_cn, 'city_cn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.block_count is not None:
            result['blockCount'] = self.block_count
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.monitor_count is not None:
            result['monitorCount'] = self.monitor_count
        if self.country_en is not None:
            result['countryEn'] = self.country_en
        if self.country_cn is not None:
            result['countryCn'] = self.country_cn
        if self.province_en is not None:
            result['provinceEn'] = self.province_en
        if self.province_cn is not None:
            result['provinceCn'] = self.province_cn
        if self.city_en is not None:
            result['cityEn'] = self.city_en
        if self.city_cn is not None:
            result['cityCn'] = self.city_cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('blockCount') is not None:
            self.block_count = m.get('blockCount')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('monitorCount') is not None:
            self.monitor_count = m.get('monitorCount')
        if m.get('countryEn') is not None:
            self.country_en = m.get('countryEn')
        if m.get('countryCn') is not None:
            self.country_cn = m.get('countryCn')
        if m.get('provinceEn') is not None:
            self.province_en = m.get('provinceEn')
        if m.get('provinceCn') is not None:
            self.province_cn = m.get('provinceCn')
        if m.get('cityEn') is not None:
            self.city_en = m.get('cityEn')
        if m.get('cityCn') is not None:
            self.city_cn = m.get('cityCn')
        return self


class GetWAFAttackIPResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetWAFAttackIPAttackIp] = None,
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
                temp_model = GetWAFAttackIPAttackIp()
                self.data.append(temp_model.from_map(k))
        return self


class GetWAFAttackIPPaths(TeaModel):
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


class GetWAFAttackIPParameters(TeaModel):
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


class GetWAFAttackIPRequestHeader(TeaModel):
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


class GetWAFAttackIPResponseHeader(TeaModel):
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






class GetTopAttackSourcesForGlobalRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTopAttackSourcesForGlobalAreaTopDTO(TeaModel):
    def __init__(
        self,
        area: str = None,
        value: int = None,
    ):
        # {'en':'Source country or area.', 'zh_CN':'来源国家或地区。'}
        self.area = area
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.area, 'area')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['area'] = self.area
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTopAttackSourcesForGlobalResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopAttackSourcesForGlobalAreaTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopAttackSourcesForGlobalAreaTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopAttackSourcesForGlobalPaths(TeaModel):
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


class GetTopAttackSourcesForGlobalParameters(TeaModel):
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


class GetTopAttackSourcesForGlobalRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopAttackSourcesForGlobalResponseHeader(TeaModel):
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






class GetApiEventLogsRequest(TeaModel):
    def __init__(
        self,
        acts: List[str] = None,
        api_name: str = None,
        api_name_condition: str = None,
        attack_types: List[str] = None,
        client_ip: str = None,
        client_ip_condition: str = None,
        domains: List[str] = None,
        end_time: str = None,
        front_path: str = None,
        front_path_condition: str = None,
        ip_location: str = None,
        log_remark: str = None,
        page_num: int = None,
        page_size: int = None,
        referer: str = None,
        referer_condition: str = None,
        rule_name: str = None,
        start_time: str = None,
        status_code: str = None,
        status_code_condition: str = None,
        tactics_type: str = None,
        ua: str = None,
        ua_conditon: str = None,
        uuid: str = None,
    ):
        # {"en":"The action to execute when a rule is matched, array,default value:[\"1\",\"2\",\"3\"].
        #  1:Block
        #  2:Log
        #  3:Sign", "zh_CN":"触发规则时的处理动作，数组。默认值：[\"1\",\"2\",\"3\"]。
        # 1：拦截
        # 2：监控
        # 3：标记"}
        self.acts = acts
        # {"en":"API name.", "zh_CN":"API名称。"}
        self.api_name = api_name
        # {"en":"The logic of API name match conditions,default value: INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL: Not equal
        #  INCLUDE: Included
        #  EXCLUDE: Not included.", "zh_CN":"API名称参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.api_name_condition = api_name_condition
        # {"en":"List of event type, array.
        # [API_ACB: Access control blacklist,
        # API_AUTH_FAILED: Authentication failed,
        # API_BODY_LIMIT: Noncompliance request body,
        # API_DEACTIVATE_CALL: Deactivate API call,
        # API_METHOD_LIMIT: Noncompliance request method,
        # API_PARAM_LIMIT: Noncompliance parameter,
        # API_QUOTA_LIMIT: Quota limit,
        # API_REQUEST_LIMIT: High concurrency Limit,
        # API_UNAUTH_OBJECT: Unauthorized object]", "zh_CN":"事件类型，数组。
        # [API_ACB：访问控制限制,
        # API_AUTH_FAILED：鉴权失败,
        # API_BODY_LIMIT：请求BODY违规,
        # API_DEACTIVATE_CALL：停用API调用,
        # API_METHOD_LIMIT：请求方法违规,
        # API_PARAM_LIMIT：请求参数违规,
        # API_QUOTA_LIMIT：配额封顶,
        # API_REQUEST_LIMIT：限流封顶,
        # API_UNAUTH_OBJECT：非授权调用]"}
        self.attack_types = attack_types
        # {"en":"Client IP.", "zh_CN":"客户端IP。"}
        self.client_ip = client_ip
        # {"en":"The logic of ip match conditions, default value:INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL:Not equal
        #  INCLUDE:Included
        #  EXCLUDE: Not included.", "zh_CN":"客户端IP参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.client_ip_condition = client_ip_condition
        # {"en":"List of domain name.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path
        # {"en":"The logic of front path match conditions, default value:INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL: Not equal
        #  INCLUDE: Included
        #  EXCLUDE: Not included.", "zh_CN":"前端路径参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.front_path_condition = front_path_condition
        # {"en":"IP location.", "zh_CN":"IP地理位置。"}
        self.ip_location = ip_location
        # {"en":"Abnormal info.", "zh_CN":"异常说明。"}
        self.log_remark = log_remark
        # {"en":"The current page number.", "zh_CN":"当前页码。"}
        self.page_num = page_num
        # {"en":"The number of records per page.", "zh_CN":"每页日志条数。"}
        self.page_size = page_size
        # {"en":"HTTP request header: Referer.", "zh_CN":"来源网址。"}
        self.referer = referer
        # {"en":"The logic of referer match conditions, default value:INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL: Not equal
        #  INCLUDE: Included
        #  EXCLUDE: Not included.", "zh_CN":"Referer参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.referer_condition = referer_condition
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.status_code = status_code
        # {"en":"The logic of status code match conditions, default value:INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL: Not equal
        #  INCLUDE: Included
        #  EXCLUDE: Not included.", "zh_CN":"状态码参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.status_code_condition = status_code_condition
        # {"en":"Rule type.", "zh_CN":"规则类型。"}
        self.tactics_type = tactics_type
        # {"en":"HTTP request header: User-Agent.", "zh_CN":"User-Agent头。"}
        self.ua = ua
        # {"en":"The logic of User-Agent match conditions, default value:INCLUDE.
        #  EQUAL: Equal
        #  UNEQUAL: Not equal
        #  INCLUDE: Included
        #  EXCLUDE: Not included.", "zh_CN":"UA参数条件。默认值：INCLUDE。
        # EQUAL：等于
        # UNEQUAL：不等于
        # INCLUDE：包含
        # EXCLUDE：不包含
        # "}
        self.ua_conditon = ua_conditon
        # {"en":"Event ID.", "zh_CN":"事件ID。"}
        self.uuid = uuid

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acts is not None:
            result['acts'] = self.acts
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_name_condition is not None:
            result['apiNameCondition'] = self.api_name_condition
        if self.attack_types is not None:
            result['attackTypes'] = self.attack_types
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.client_ip_condition is not None:
            result['clientIpCondition'] = self.client_ip_condition
        if self.domains is not None:
            result['domains'] = self.domains
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        if self.front_path_condition is not None:
            result['frontPathCondition'] = self.front_path_condition
        if self.ip_location is not None:
            result['ipLocation'] = self.ip_location
        if self.log_remark is not None:
            result['logRemark'] = self.log_remark
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.referer is not None:
            result['referer'] = self.referer
        if self.referer_condition is not None:
            result['refererCondition'] = self.referer_condition
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_code_condition is not None:
            result['statusCodeCondition'] = self.status_code_condition
        if self.tactics_type is not None:
            result['tacticsType'] = self.tactics_type
        if self.ua is not None:
            result['ua'] = self.ua
        if self.ua_conditon is not None:
            result['uaConditon'] = self.ua_conditon
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acts') is not None:
            self.acts = m.get('acts')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiNameCondition') is not None:
            self.api_name_condition = m.get('apiNameCondition')
        if m.get('attackTypes') is not None:
            self.attack_types = m.get('attackTypes')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('clientIpCondition') is not None:
            self.client_ip_condition = m.get('clientIpCondition')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        if m.get('frontPathCondition') is not None:
            self.front_path_condition = m.get('frontPathCondition')
        if m.get('ipLocation') is not None:
            self.ip_location = m.get('ipLocation')
        if m.get('logRemark') is not None:
            self.log_remark = m.get('logRemark')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('refererCondition') is not None:
            self.referer_condition = m.get('refererCondition')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusCodeCondition') is not None:
            self.status_code_condition = m.get('statusCodeCondition')
        if m.get('tacticsType') is not None:
            self.tactics_type = m.get('tacticsType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        if m.get('uaConditon') is not None:
            self.ua_conditon = m.get('uaConditon')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetApiEventLogsVo(TeaModel):
    def __init__(
        self,
        act: str = None,
        act_desc: str = None,
        api_name: str = None,
        attack_desc: str = None,
        attack_type: str = None,
        client_ip: str = None,
        domain: str = None,
        exception_desc: str = None,
        front_path: str = None,
        http_version: str = None,
        ip_location: str = None,
        referer: str = None,
        request_head: str = None,
        request_method: str = None,
        request_url: str = None,
        response: str = None,
        rule_name: str = None,
        status_code: str = None,
        tactics_type: str = None,
        time: str = None,
        ua: str = None,
        uuid: str = None,
    ):
        # {"en":"The action to execute when a rule is matched.
        #  1:Block
        #  2:Log
        #  3:Sign", "zh_CN":"触发规则时的处理动作。
        # 1：拦截
        # 2：监控
        # 3：标记"}
        self.act = act
        # {"en":"The action description to execute when a rule is matched.", "zh_CN":"处理动作描述。"}
        self.act_desc = act_desc
        # {"en":"API name.", "zh_CN":"api名称。"}
        self.api_name = api_name
        # {"en":"Event description.", "zh_CN":"事件描述。"}
        self.attack_desc = attack_desc
        # {"en":"Event type.", "zh_CN":"事件类型。"}
        self.attack_type = attack_type
        # {"en":"Client IP.", "zh_CN":"客户端IP。"}
        self.client_ip = client_ip
        # {"en":"Domain.", "zh_CN":"域名。"}
        self.domain = domain
        # {"en":"Abnormal info.", "zh_CN":"异常说明。"}
        self.exception_desc = exception_desc
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path
        # {"en":"HTTP version.", "zh_CN":"http版本。"}
        self.http_version = http_version
        # {"en":"IP location.", "zh_CN":"IP 地理位置。"}
        self.ip_location = ip_location
        # {"en":"HTTP request header: Referer.", "zh_CN":"来源网址。"}
        self.referer = referer
        # {"en":"HTTP request header.", "zh_CN":"请求头信息。"}
        self.request_head = request_head
        # {"en":"HTTP request method.", "zh_CN":"请求方法。"}
        self.request_method = request_method
        # {"en":"HTTP request URL.", "zh_CN":"请求URL。"}
        self.request_url = request_url
        # {"en":"HTTP response header.", "zh_CN":"响应头信息。"}
        self.response = response
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.status_code = status_code
        # {"en":"Rule type.", "zh_CN":"规则类型。"}
        self.tactics_type = tactics_type
        # {"en":"Time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"HTTP request header: User-Agent.", "zh_CN":"User-Agent头。"}
        self.ua = ua
        # {"en":"Event ID.", "zh_CN":"事件ID。"}
        self.uuid = uuid

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.act_desc, 'act_desc')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.attack_desc, 'attack_desc')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.exception_desc, 'exception_desc')
        self.validate_required(self.front_path, 'front_path')
        self.validate_required(self.http_version, 'http_version')
        self.validate_required(self.ip_location, 'ip_location')
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.request_head, 'request_head')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.request_url, 'request_url')
        self.validate_required(self.response, 'response')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.tactics_type, 'tactics_type')
        self.validate_required(self.time, 'time')
        self.validate_required(self.ua, 'ua')
        self.validate_required(self.uuid, 'uuid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.act_desc is not None:
            result['actDesc'] = self.act_desc
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.attack_desc is not None:
            result['attackDesc'] = self.attack_desc
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.exception_desc is not None:
            result['exceptionDesc'] = self.exception_desc
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        if self.http_version is not None:
            result['httpVersion'] = self.http_version
        if self.ip_location is not None:
            result['ipLocation'] = self.ip_location
        if self.referer is not None:
            result['referer'] = self.referer
        if self.request_head is not None:
            result['requestHead'] = self.request_head
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.request_url is not None:
            result['requestUrl'] = self.request_url
        if self.response is not None:
            result['response'] = self.response
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.tactics_type is not None:
            result['tacticsType'] = self.tactics_type
        if self.time is not None:
            result['time'] = self.time
        if self.ua is not None:
            result['ua'] = self.ua
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('actDesc') is not None:
            self.act_desc = m.get('actDesc')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('attackDesc') is not None:
            self.attack_desc = m.get('attackDesc')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('exceptionDesc') is not None:
            self.exception_desc = m.get('exceptionDesc')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        if m.get('httpVersion') is not None:
            self.http_version = m.get('httpVersion')
        if m.get('ipLocation') is not None:
            self.ip_location = m.get('ipLocation')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('requestHead') is not None:
            self.request_head = m.get('requestHead')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('requestUrl') is not None:
            self.request_url = m.get('requestUrl')
        if m.get('response') is not None:
            self.response = m.get('response')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('tacticsType') is not None:
            self.tactics_type = m.get('tacticsType')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetApiEventLogsPage(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
        records: GetApiEventLogsVo = None,
    ):
        # {"en":"The current page number.", "zh_CN":"当前页码。"}
        self.page_num = page_num
        # {"en":"The number of records per page.", "zh_CN":"每页日志条数。"}
        self.page_size = page_size
        # {"en":"The total number of records.", "zh_CN":"总条数。"}
        self.total = total
        # {"en":"List of event log.", "zh_CN":"事件日志列表。"}
        self.records = records

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')
        self.validate_required(self.records, 'records')
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        if self.records is not None:
            result['records'] = self.records.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('records') is not None:
            temp_model = GetApiEventLogsVo()
            self.records = temp_model.from_map(m['records'])
        return self


class GetApiEventLogsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetApiEventLogsPage = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
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
            temp_model = GetApiEventLogsPage()
            self.data = temp_model.from_map(m['data'])
        return self


class GetApiEventLogsPaths(TeaModel):
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


class GetApiEventLogsParameters(TeaModel):
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


class GetApiEventLogsRequestHeader(TeaModel):
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


class GetApiEventLogsResponseHeader(TeaModel):
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






class GetWAFPolicyDetailsRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        rule_id: str = None,
        policys: List[str] = None,
        time_zone: str = None,
        acts: List[str] = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.rule_id = rule_id
        # {"en":"Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]", "zh_CN":"触发策略类型，数组。[protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]"}
        self.policys = policys
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {"en":"Action, default 1 and 2.
        #     1: Block
        #     2: Log", "zh_CN":"处理动作，默认1和2。
        #     1：拦截
        #     2：监控"}
        self.acts = acts

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.rule_id, 'rule_id')

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
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.policys is not None:
            result['policys'] = self.policys
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.acts is not None:
            result['acts'] = self.acts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('acts') is not None:
            self.acts = m.get('acts')
        return self


class GetWAFPolicyDetailsAttackItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        attack_time: str = None,
        total_count: int = None,
    ):
        # {"en":"Attacker IP", "zh_CN":"攻击IP。"}
        self.name = name
        # {"en":"Last attack time.", "zh_CN":"最近攻击时间。"}
        self.attack_time = attack_time
        # {"en":"Attack requests.", "zh_CN":"攻击次数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetWAFPolicyDetailsAttackItemArray(TeaModel):
    def __init__(
        self,
        count: int = None,
        list: List[GetWAFPolicyDetailsAttackItem] = None,
    ):
        # {"en":"Attacker IP count", "zh_CN":"攻击IP记录数。"}
        self.count = count
        # {"en":"Attacker IP array", "zh_CN":"攻击IP数组。"}
        self.list = list

    def validate(self):
        self.validate_required(self.count, 'count')
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
        if self.count is not None:
            result['count'] = self.count
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = GetWAFPolicyDetailsAttackItem()
                self.list.append(temp_model.from_map(k))
        return self


class GetWAFPolicyDetailsAttackUrlItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        attack_time: str = None,
        total_count: int = None,
    ):
        # {"en":"URL", "zh_CN":"URL"}
        self.name = name
        # {"en":"Last attack time.", "zh_CN":"最近防护时间。"}
        self.attack_time = attack_time
        # {"en":"Attack requests.", "zh_CN":"攻击次数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetWAFPolicyDetailsAttackUrlItemArray(TeaModel):
    def __init__(
        self,
        count: int = None,
        list: List[GetWAFPolicyDetailsAttackUrlItem] = None,
    ):
        # {"en":"Attack requests count", "zh_CN":"受攻击URL记录数。"}
        self.count = count
        # {"en":"Attack requests array", "zh_CN":"受攻击URL数组。"}
        self.list = list

    def validate(self):
        self.validate_required(self.count, 'count')
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
        if self.count is not None:
            result['count'] = self.count
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = GetWAFPolicyDetailsAttackUrlItem()
                self.list.append(temp_model.from_map(k))
        return self


class GetWAFPolicyDetailsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
        attack_time: str = None,
        attack_type: str = None,
        attack_type_name: str = None,
        attack_type_name_en: str = None,
        total_count: int = None,
        rule_id: str = None,
        rule_name: str = None,
        ips: List[GetWAFPolicyDetailsAttackItemArray] = None,
        urls: List[GetWAFPolicyDetailsAttackUrlItemArray] = None,
    ):
        # {"en":"Return 0 means success, please see <Error code> to check other status code.", "zh_CN":"0状态码表示请求成功，其他状态码说明请参见《错误码》。"}
        self.code = code
        # {"en":"Error message or Success.", "zh_CN":"错误信息或Success。"}
        self.message = message
        # {"en":"Return data.", "zh_CN":"返回值。"}
        self.data = data
        # {"en":"Last attack time.", "zh_CN":"最近攻击时间。"}
        self.attack_time = attack_time
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.attack_type = attack_type
        # {"en":"Chinese name of attack type.", "zh_CN":"攻击类型中文名称。"}
        self.attack_type_name = attack_type_name
        # {"en":"English name of attack type.", "zh_CN":"攻击类型英文名称。"}
        self.attack_type_name_en = attack_type_name_en
        # {"en":"Attack requests.", "zh_CN":"攻击次数。"}
        self.total_count = total_count
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.rule_id = rule_id
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Attacker IP.", "zh_CN":"攻击IP。"}
        self.ips = ips
        # {"en":"Attacked url.", "zh_CN":"受攻击URL。"}
        self.urls = urls

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.attack_type_name, 'attack_type_name')
        self.validate_required(self.attack_type_name_en, 'attack_type_name_en')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.ips, 'ips')
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()
        self.validate_required(self.urls, 'urls')
        if self.urls:
            for k in self.urls:
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
            result['data'] = self.data
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.attack_type_name is not None:
            result['attackTypeName'] = self.attack_type_name
        if self.attack_type_name_en is not None:
            result['attackTypeNameEn'] = self.attack_type_name_en
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.ips is not None:
            result['ips'] = []
            for k in self.ips:
                result['ips'].append(k.to_map() if k else None)
        if self.urls is not None:
            result['urls'] = []
            for k in self.urls:
                result['urls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('attackTypeName') is not None:
            self.attack_type_name = m.get('attackTypeName')
        if m.get('attackTypeNameEn') is not None:
            self.attack_type_name_en = m.get('attackTypeNameEn')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ips') is not None:
            self.ips = []
            for k in m.get('ips'):
                temp_model = GetWAFPolicyDetailsAttackItemArray()
                self.ips.append(temp_model.from_map(k))
        if m.get('urls') is not None:
            self.urls = []
            for k in m.get('urls'):
                temp_model = GetWAFPolicyDetailsAttackUrlItemArray()
                self.urls.append(temp_model.from_map(k))
        return self


class GetWAFPolicyDetailsPaths(TeaModel):
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


class GetWAFPolicyDetailsParameters(TeaModel):
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


class GetWAFPolicyDetailsRequestHeader(TeaModel):
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


class GetWAFPolicyDetailsResponseHeader(TeaModel):
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






class GetTrendsByrpsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        act_type: List[str] = None,
        domains: List[str] = None,
    ):
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTrendsByrpsEventTypeDTO(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: int = None,
    ):
        # {'en':'Attack type.
        #  BLOCK: IP/Geo Block
        #  DMS_DEFEND: DDoS Protection
        #  WAF_DEFEND: WAF
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  INTELLIGENCE: Threat Intelligence
        #  RATE_LIMIT: Rate Limiting
        #  CUSTOMIZE_RULE: Custom Rules', 'zh_CN':'攻击类型。
        #  BLOCK：IP/区域封禁
        #  DMS_DEFEND：DDoS防护
        #  WAF_DEFEND：WAF
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  INTELLIGENCE：威胁情报
        #  RATE_LIMIT：频率限制
        #  CUSTOMIZE_RULE：自定义规则'}
        self.code = code
        # {'en':'Number of attack requests of this type(per second).', 'zh_CN':'该类型攻击请求数（每秒均值）。'}
        self.value = value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTrendsByrpsEventTrendDTO(TeaModel):
    def __init__(
        self,
        time_point: str = None,
        total: int = None,
        attack: int = None,
        mitigated: int = None,
        monitored: int = None,
        whitelist: int = None,
        distribution: List[GetTrendsByrpsEventTypeDTO] = None,
    ):
        # {'en':'Time point(yyyy-MM-dd HH-mm-ss).', 'zh_CN':'时间点（yyyy-MM-dd HH-mm-ss）。'}
        self.time_point = time_point
        # {'en':'Total requests(per second).', 'zh_CN':'总请求数（每秒均值）。'}
        self.total = total
        # {'en':'Attack requests(per second).', 'zh_CN':'攻击请求数（每秒均值）。'}
        self.attack = attack
        # {'en':'Mitigated requests.', 'zh_CN':'已抵御请求数。'}
        self.mitigated = mitigated
        # {'en':'Monitored requests.', 'zh_CN':'观察请求数。'}
        self.monitored = monitored
        # {'en':'Whitelist requests(per second).', 'zh_CN':'白名单请求数（每秒均值）。'}
        self.whitelist = whitelist
        # {'en':'Attack type classification requests(per second).', 'zh_CN':'攻击类型分类请求数（每秒均值）。'}
        self.distribution = distribution

    def validate(self):
        self.validate_required(self.time_point, 'time_point')
        self.validate_required(self.total, 'total')
        self.validate_required(self.attack, 'attack')
        self.validate_required(self.mitigated, 'mitigated')
        self.validate_required(self.monitored, 'monitored')
        self.validate_required(self.whitelist, 'whitelist')
        self.validate_required(self.distribution, 'distribution')
        if self.distribution:
            for k in self.distribution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        if self.total is not None:
            result['total'] = self.total
        if self.attack is not None:
            result['attack'] = self.attack
        if self.mitigated is not None:
            result['mitigated'] = self.mitigated
        if self.monitored is not None:
            result['monitored'] = self.monitored
        if self.whitelist is not None:
            result['whitelist'] = self.whitelist
        if self.distribution is not None:
            result['distribution'] = []
            for k in self.distribution:
                result['distribution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        if m.get('mitigated') is not None:
            self.mitigated = m.get('mitigated')
        if m.get('monitored') is not None:
            self.monitored = m.get('monitored')
        if m.get('whitelist') is not None:
            self.whitelist = m.get('whitelist')
        if m.get('distribution') is not None:
            self.distribution = []
            for k in m.get('distribution'):
                temp_model = GetTrendsByrpsEventTypeDTO()
                self.distribution.append(temp_model.from_map(k))
        return self


class GetTrendsByrpsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTrendsByrpsEventTrendDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTrendsByrpsEventTrendDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTrendsByrpsPaths(TeaModel):
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


class GetTrendsByrpsParameters(TeaModel):
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


class GetTrendsByrpsRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTrendsByrpsResponseHeader(TeaModel):
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






class GetRequestTrendRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetRequestTrendVo(TeaModel):
    def __init__(
        self,
        flow_celling: int = None,
        illegal_request_body: int = None,
        auth_failed: int = None,
        api_deactivate_call: int = None,
        access_control_black: int = None,
        back_origin: int = None,
        total_request: int = None,
        request_method_limit: int = None,
        quota_celling: int = None,
        remission: int = None,
        without_auth: int = None,
        time: int = None,
    ):
        # {"en":"The total number of high concurrency limit.", "zh_CN":"限流封顶总数。"}
        self.flow_celling = flow_celling
        # {"en":"The total number of noncompliance request body.", "zh_CN":"请求Body违规总数。"}
        self.illegal_request_body = illegal_request_body
        # {"en":"The total number of authentication failed.", "zh_CN":"鉴权失败总数。"}
        self.auth_failed = auth_failed
        # {"en":"The total number of deactivate API call.", "zh_CN":"停用API调用总数。"}
        self.api_deactivate_call = api_deactivate_call
        # {"en":"The total number of access control blacklist.", "zh_CN":"访问控制限制总数。"}
        self.access_control_black = access_control_black
        # {"en":"The total number of back-to-source.", "zh_CN":"回源数。"}
        self.back_origin = back_origin
        # {"en":"The total number of requests.", "zh_CN":"总请求数。"}
        self.total_request = total_request
        # {"en":"The total number of noncompliance request method.", "zh_CN":"请求方法违规总数。"}
        self.request_method_limit = request_method_limit
        # {"en":"The total number of quota limit.", "zh_CN":"配额封顶总数。"}
        self.quota_celling = quota_celling
        # {"en":"The total number of remission.", "zh_CN":"缓解数。"}
        self.remission = remission
        # {"en":"The total number of unauthorized calls.", "zh_CN":"非授权调用总数。"}
        self.without_auth = without_auth
        # {"en":"The time point of request trend.", "zh_CN":"请求趋势时间点。"}
        self.time = time

    def validate(self):
        self.validate_required(self.flow_celling, 'flow_celling')
        self.validate_required(self.illegal_request_body, 'illegal_request_body')
        self.validate_required(self.auth_failed, 'auth_failed')
        self.validate_required(self.api_deactivate_call, 'api_deactivate_call')
        self.validate_required(self.access_control_black, 'access_control_black')
        self.validate_required(self.back_origin, 'back_origin')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.request_method_limit, 'request_method_limit')
        self.validate_required(self.quota_celling, 'quota_celling')
        self.validate_required(self.remission, 'remission')
        self.validate_required(self.without_auth, 'without_auth')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_celling is not None:
            result['flowCelling'] = self.flow_celling
        if self.illegal_request_body is not None:
            result['illegalRequestBody'] = self.illegal_request_body
        if self.auth_failed is not None:
            result['authFailed'] = self.auth_failed
        if self.api_deactivate_call is not None:
            result['apiDeactivateCall'] = self.api_deactivate_call
        if self.access_control_black is not None:
            result['accessControlBlack'] = self.access_control_black
        if self.back_origin is not None:
            result['backOrigin'] = self.back_origin
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.request_method_limit is not None:
            result['requestMethodLimit'] = self.request_method_limit
        if self.quota_celling is not None:
            result['quotaCelling'] = self.quota_celling
        if self.remission is not None:
            result['remission'] = self.remission
        if self.without_auth is not None:
            result['withoutAuth'] = self.without_auth
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowCelling') is not None:
            self.flow_celling = m.get('flowCelling')
        if m.get('illegalRequestBody') is not None:
            self.illegal_request_body = m.get('illegalRequestBody')
        if m.get('authFailed') is not None:
            self.auth_failed = m.get('authFailed')
        if m.get('apiDeactivateCall') is not None:
            self.api_deactivate_call = m.get('apiDeactivateCall')
        if m.get('accessControlBlack') is not None:
            self.access_control_black = m.get('accessControlBlack')
        if m.get('backOrigin') is not None:
            self.back_origin = m.get('backOrigin')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('requestMethodLimit') is not None:
            self.request_method_limit = m.get('requestMethodLimit')
        if m.get('quotaCelling') is not None:
            self.quota_celling = m.get('quotaCelling')
        if m.get('remission') is not None:
            self.remission = m.get('remission')
        if m.get('withoutAuth') is not None:
            self.without_auth = m.get('withoutAuth')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class GetRequestTrendResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: List[GetRequestTrendVo] = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"List of data.", "zh_CN":"数据列表。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetRequestTrendVo()
                self.data.append(temp_model.from_map(k))
        return self


class GetRequestTrendPaths(TeaModel):
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


class GetRequestTrendParameters(TeaModel):
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


class GetRequestTrendRequestHeader(TeaModel):
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


class GetRequestTrendResponseHeader(TeaModel):
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






class GetL7DdosAnalysisAttackIpListV2Request(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
        top_num: int = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time
        # {"en":"domains list.", "zh_CN":"域名数组。"}
        self.domains = domains
        # {"en":"Top num.", "zh_CN":"默认10条。"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.domains, 'domains')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        if self.top_num is not None:
            result['topNum'] = self.top_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetL7DdosAnalysisAttackIpListV2AttackIp(TeaModel):
    def __init__(
        self,
        ip: str = None,
        all_count: int = None,
        alarm_count: int = None,
        alarm_ratio: float = None,
        count: int = None,
        ratio: float = None,
        ip_country_cn: str = None,
        ip_province_cn: str = None,
        ip_city_en: str = None,
        ip_country_en: str = None,
        ip_province_en: str = None,
    ):
        # {"en":"ip.", "zh_CN":"攻击ip。"}
        self.ip = ip
        # {"en":"All count.", "zh_CN":"总请求数。"}
        self.all_count = all_count
        # {"en":"Observed Requests.", "zh_CN":"观察请求数。"}
        self.alarm_count = alarm_count
        # {"en":"Observed Ratio.", "zh_CN":"观察请求占比。"}
        self.alarm_ratio = alarm_ratio
        # {"en":"Resisted Requests.", "zh_CN":"已抵御请求数。"}
        self.count = count
        # {"en":"Resisted Ratio.", "zh_CN":"已抵御请求占比。"}
        self.ratio = ratio
        # {"en":"Country - Chinese.", "zh_CN":"国家——中文。"}
        self.ip_country_cn = ip_country_cn
        # {"en":"Province -  Chinese.", "zh_CN":"省份——中文。"}
        self.ip_province_cn = ip_province_cn
        # {"en":"city - English.", "zh_CN":"城市——英文。"}
        self.ip_city_en = ip_city_en
        # {"en":"Country - English.", "zh_CN":"国家——英文。"}
        self.ip_country_en = ip_country_en
        # {"en":"Province - English.", "zh_CN":"省份——英文。"}
        self.ip_province_en = ip_province_en

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.all_count, 'all_count')
        self.validate_required(self.alarm_count, 'alarm_count')
        self.validate_required(self.alarm_ratio, 'alarm_ratio')
        self.validate_required(self.count, 'count')
        self.validate_required(self.ratio, 'ratio')
        self.validate_required(self.ip_country_cn, 'ip_country_cn')
        self.validate_required(self.ip_province_cn, 'ip_province_cn')
        self.validate_required(self.ip_city_en, 'ip_city_en')
        self.validate_required(self.ip_country_en, 'ip_country_en')
        self.validate_required(self.ip_province_en, 'ip_province_en')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.all_count is not None:
            result['all_count'] = self.all_count
        if self.alarm_count is not None:
            result['alarmCount'] = self.alarm_count
        if self.alarm_ratio is not None:
            result['alarmRatio'] = self.alarm_ratio
        if self.count is not None:
            result['count'] = self.count
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.ip_country_cn is not None:
            result['ip_country_cn'] = self.ip_country_cn
        if self.ip_province_cn is not None:
            result['ip_province_cn'] = self.ip_province_cn
        if self.ip_city_en is not None:
            result['ip_city_en'] = self.ip_city_en
        if self.ip_country_en is not None:
            result['ip_country_en'] = self.ip_country_en
        if self.ip_province_en is not None:
            result['ip_province_en'] = self.ip_province_en
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('all_count') is not None:
            self.all_count = m.get('all_count')
        if m.get('alarmCount') is not None:
            self.alarm_count = m.get('alarmCount')
        if m.get('alarmRatio') is not None:
            self.alarm_ratio = m.get('alarmRatio')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('ip_country_cn') is not None:
            self.ip_country_cn = m.get('ip_country_cn')
        if m.get('ip_province_cn') is not None:
            self.ip_province_cn = m.get('ip_province_cn')
        if m.get('ip_city_en') is not None:
            self.ip_city_en = m.get('ip_city_en')
        if m.get('ip_country_en') is not None:
            self.ip_country_en = m.get('ip_country_en')
        if m.get('ip_province_en') is not None:
            self.ip_province_en = m.get('ip_province_en')
        return self


class GetL7DdosAnalysisAttackIpListV2Response(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetL7DdosAnalysisAttackIpListV2AttackIp] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetL7DdosAnalysisAttackIpListV2AttackIp()
                self.data.append(temp_model.from_map(k))
        return self


class GetL7DdosAnalysisAttackIpListV2Paths(TeaModel):
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


class GetL7DdosAnalysisAttackIpListV2Parameters(TeaModel):
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


class GetL7DdosAnalysisAttackIpListV2RequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetL7DdosAnalysisAttackIpListV2ResponseHeader(TeaModel):
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






class QueryCCAttackDetailsRequest(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        time_zone: str = None,
    ):
        # {"en":"Start date format yyyy MM DD HH: mm: SS", "zh_CN":"起始日期 格式 yyyy-MM-dd HH:mm:ss"}
        self.startdate = startdate
        # {"en":"End date format yyyy MM DD HH: mm: SS", "zh_CN":"结束日期 格式 yyyy-MM-dd HH:mm:ss"}
        self.enddate = enddate
        # {"en":"Domain names, multiple separated by semicolons", "zh_CN":"域名,多个用分号分隔"}
        self.channel = channel
        # {"en":"Time zone offset,default:28800000", "zh_CN":"时区，默认为28800000"}
        self.time_zone = time_zone

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class QueryCCAttackDetailsResponse(TeaModel):
    def __init__(
        self,
        ip_country_cn: str = None,
        ip_country_en: str = None,
        attackdomain: str = None,
        cn_country_code: str = None,
        en_country_code: str = None,
        count: int = None,
        en_city: str = None,
        cn_city: str = None,
        attackip: str = None,
        ip_province_cn: str = None,
        ip_province_en: str = None,
        ip_city_en: str = None,
        ip_city_cn: str = None,
        time: str = None,
    ):
        # {"en":"IP home, Chinese", "zh_CN":"ip归属地，中文"}
        self.ip_country_cn = ip_country_cn
        # {"en":"IP home, English", "zh_CN":"ip归属地，英文"}
        self.ip_country_en = ip_country_en
        # {"en":"Attacked domain name", "zh_CN":"被攻击域名"}
        self.attackdomain = attackdomain
        # {"en":"country code", "zh_CN":"国家编码"}
        self.cn_country_code = cn_country_code
        # {"en":"Country code, English", "zh_CN":"国家编码，英文"}
        self.en_country_code = en_country_code
        # {"en":"count", "zh_CN":"攻击数量"}
        self.count = count
        # {"en":"City, English", "zh_CN":"城市，英文"}
        self.en_city = en_city
        # {"en":"City, Chinese", "zh_CN":"城市，中文"}
        self.cn_city = cn_city
        # {"en":"attackip", "zh_CN":"攻击ip"}
        self.attackip = attackip
        # {"en":"IP Province, Chinese", "zh_CN":"ip所在省，中文"}
        self.ip_province_cn = ip_province_cn
        # {"en":"IP Province, English", "zh_CN":"ip所在省，英文"}
        self.ip_province_en = ip_province_en
        # {"en":"IP City, English", "zh_CN":"ip所在城市，英文"}
        self.ip_city_en = ip_city_en
        # {"en":"IP City, Chinese", "zh_CN":"ip所在城市，中文"}
        self.ip_city_cn = ip_city_cn
        # {"en":"time", "zh_CN":"时间"}
        self.time = time

    def validate(self):
        self.validate_required(self.ip_country_cn, 'ip_country_cn')
        self.validate_required(self.ip_country_en, 'ip_country_en')
        self.validate_required(self.attackdomain, 'attackdomain')
        self.validate_required(self.cn_country_code, 'cn_country_code')
        self.validate_required(self.en_country_code, 'en_country_code')
        self.validate_required(self.count, 'count')
        self.validate_required(self.en_city, 'en_city')
        self.validate_required(self.cn_city, 'cn_city')
        self.validate_required(self.attackip, 'attackip')
        self.validate_required(self.ip_province_cn, 'ip_province_cn')
        self.validate_required(self.ip_province_en, 'ip_province_en')
        self.validate_required(self.ip_city_en, 'ip_city_en')
        self.validate_required(self.ip_city_cn, 'ip_city_cn')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_country_cn is not None:
            result['ip_country_cn'] = self.ip_country_cn
        if self.ip_country_en is not None:
            result['ip_country_en'] = self.ip_country_en
        if self.attackdomain is not None:
            result['attackdomain'] = self.attackdomain
        if self.cn_country_code is not None:
            result['cn_country_code'] = self.cn_country_code
        if self.en_country_code is not None:
            result['en_country_code'] = self.en_country_code
        if self.count is not None:
            result['count'] = self.count
        if self.en_city is not None:
            result['en_city'] = self.en_city
        if self.cn_city is not None:
            result['cn_city'] = self.cn_city
        if self.attackip is not None:
            result['attackip'] = self.attackip
        if self.ip_province_cn is not None:
            result['ip_province_cn'] = self.ip_province_cn
        if self.ip_province_en is not None:
            result['ip_province_en'] = self.ip_province_en
        if self.ip_city_en is not None:
            result['ip_city_en'] = self.ip_city_en
        if self.ip_city_cn is not None:
            result['ip_city_cn'] = self.ip_city_cn
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip_country_cn') is not None:
            self.ip_country_cn = m.get('ip_country_cn')
        if m.get('ip_country_en') is not None:
            self.ip_country_en = m.get('ip_country_en')
        if m.get('attackdomain') is not None:
            self.attackdomain = m.get('attackdomain')
        if m.get('cn_country_code') is not None:
            self.cn_country_code = m.get('cn_country_code')
        if m.get('en_country_code') is not None:
            self.en_country_code = m.get('en_country_code')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('en_city') is not None:
            self.en_city = m.get('en_city')
        if m.get('cn_city') is not None:
            self.cn_city = m.get('cn_city')
        if m.get('attackip') is not None:
            self.attackip = m.get('attackip')
        if m.get('ip_province_cn') is not None:
            self.ip_province_cn = m.get('ip_province_cn')
        if m.get('ip_province_en') is not None:
            self.ip_province_en = m.get('ip_province_en')
        if m.get('ip_city_en') is not None:
            self.ip_city_en = m.get('ip_city_en')
        if m.get('ip_city_cn') is not None:
            self.ip_city_cn = m.get('ip_city_cn')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class QueryCCAttackDetailsPaths(TeaModel):
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


class QueryCCAttackDetailsParameters(TeaModel):
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


class QueryCCAttackDetailsRequestHeader(TeaModel):
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


class QueryCCAttackDetailsResponseHeader(TeaModel):
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






class GetBotRequestRefererTopDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        top_num: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetBotRequestRefererTopDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Bot request count", "zh_CN":"Bot请求数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetBotRequestRefererTopDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRequestRefererTopDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data rturned", "zh_CN":"返回数据"}
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
                temp_model = GetBotRequestRefererTopDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRequestRefererTopDataPaths(TeaModel):
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


class GetBotRequestRefererTopDataParameters(TeaModel):
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


class GetBotRequestRefererTopDataRequestHeader(TeaModel):
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


class GetBotRequestRefererTopDataResponseHeader(TeaModel):
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






class GetRiskEventTop5Request(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API groups.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API names.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domains.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetRiskEventTop5Vo(TeaModel):
    def __init__(
        self,
        attack_type: str = None,
        count: int = None,
    ):
        # {"en":"Attack type.
        # accessControlBlack:Access Control Blacklist
        # authFailed:Authentication Failed
        # illegalRequestBody:Noncompliance Request Body
        # apiDeactivateCall:Deactivate API call
        # requestMethodLimit:Noncompliance Request Method
        # illegalRequestParam:Noncompliance Parameter
        # quotaCelling:Quota Limit
        # flowCelling:High Concurrency Limit
        # withoutAuth:Unauthorized Object.
        # ", "zh_CN":"攻击类型。
        # accessControlBlack:访问控制限制
        # authFailed:鉴权失败
        # illegalRequestBody:请求Body违规
        # apiDeactivateCall:停用API调用
        # requestMethodLimit:请求方法违规
        # illegalRequestParam:请求参数违规
        # quotaCelling:配额封顶
        # flowCelling:限流封顶
        # withoutAuth:非授权调用。"}
        self.attack_type = attack_type
        # {"en":"The number of certain risk records.", "zh_CN":"某种风险记录数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetRiskEventTop5Response(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: List[GetRiskEventTop5Vo] = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetRiskEventTop5Vo()
                self.data.append(temp_model.from_map(k))
        return self


class GetRiskEventTop5Paths(TeaModel):
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


class GetRiskEventTop5Parameters(TeaModel):
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


class GetRiskEventTop5RequestHeader(TeaModel):
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


class GetRiskEventTop5ResponseHeader(TeaModel):
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






class GetTriggeredDDoSManagedRulesRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTriggeredDDoSManagedRulesRuleHitDTO(TeaModel):
    def __init__(
        self,
        act: str = None,
        value: int = None,
    ):
        # {'en':'Action.', 'zh_CN':'采取动作。'}
        self.act = act
        # {'en':'Hit times.', 'zh_CN':'命中数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTriggeredDDoSManagedRulesRuleTopDTO(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        action: str = None,
        hits: List[GetTriggeredDDoSManagedRulesRuleHitDTO] = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Rule type.', 'zh_CN':'规则类型。'}
        self.rule_type = rule_type
        # {'en':'System recommended action.', 'zh_CN':'系统推荐动作。'}
        self.action = action
        # {'en':'Trigger times, sort by times.', 'zh_CN':'触发次数，按次数排序。'}
        self.hits = hits

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.action, 'action')
        self.validate_required(self.hits, 'hits')
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.action is not None:
            result['action'] = self.action
        if self.hits is not None:
            result['hits'] = []
            for k in self.hits:
                result['hits'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('hits') is not None:
            self.hits = []
            for k in m.get('hits'):
                temp_model = GetTriggeredDDoSManagedRulesRuleHitDTO()
                self.hits.append(temp_model.from_map(k))
        return self


class GetTriggeredDDoSManagedRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTriggeredDDoSManagedRulesRuleTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTriggeredDDoSManagedRulesRuleTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTriggeredDDoSManagedRulesPaths(TeaModel):
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


class GetTriggeredDDoSManagedRulesParameters(TeaModel):
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


class GetTriggeredDDoSManagedRulesRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTriggeredDDoSManagedRulesResponseHeader(TeaModel):
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






class GetTopAttackSourcesForChinaMainlandRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTopAttackSourcesForChinaMainlandAreaTopDTO(TeaModel):
    def __init__(
        self,
        area: str = None,
        city: str = None,
        value: int = None,
    ):
        # {'en':'Source area(domestic province).', 'zh_CN':'来源地区（国内省份）。'}
        self.area = area
        # {'en':'Source city.', 'zh_CN':'来源城市。'}
        self.city = city
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.area, 'area')
        self.validate_required(self.city, 'city')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['area'] = self.area
        if self.city is not None:
            result['city'] = self.city
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTopAttackSourcesForChinaMainlandResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopAttackSourcesForChinaMainlandAreaTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopAttackSourcesForChinaMainlandAreaTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopAttackSourcesForChinaMainlandPaths(TeaModel):
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


class GetTopAttackSourcesForChinaMainlandParameters(TeaModel):
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


class GetTopAttackSourcesForChinaMainlandRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopAttackSourcesForChinaMainlandResponseHeader(TeaModel):
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






class GetWAFAttackEventRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
    ):
        # {'en':'Domain, array.', 'zh_CN':'域名，数组。'}
        self.domains = domains
        # {'en':'Start time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'开始时间，yyyy-MM-dd HH:mm:ss。'}
        self.start_time = start_time
        # {'en':'End time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'结束时间，yyyy-MM-dd HH:mm:ss。'}
        self.end_time = end_time
        # {'en':'Time zone, GMT+8 by default.', 'zh_CN':'时区，默认GMT+8，即“GMT+8”。'}
        self.time_zone = time_zone

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        return self


class GetWAFAttackEventAttackEvent(TeaModel):
    def __init__(
        self,
        attack_count: int = None,
        start_time: str = None,
        end_time: str = None,
        attack_type: str = None,
        ip: str = None,
        attack_event_type: str = None,
        attack_type_name_en: str = None,
        attack_type_name: str = None,
        event_name_en: str = None,
        event_name: str = None,
    ):
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.attack_count = attack_count
        # {"en":"Start time of attack.", "zh_CN":"攻击事件起始时间。"}
        self.start_time = start_time
        # {"en":"End time of attack.", "zh_CN":"攻击事件截止时间。"}
        self.end_time = end_time
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.attack_type = attack_type
        # {"en":"Attacker Ip.", "zh_CN":"攻击IP。"}
        self.ip = ip
        # {"en":"Attack event type.", "zh_CN":"攻击事件类型。"}
        self.attack_event_type = attack_event_type
        # {"en":"English name of attack type.", "zh_CN":"攻击类别英文名称。"}
        self.attack_type_name_en = attack_type_name_en
        # {"en":"Chinese name of attack type.", "zh_CN":"攻击类别中文名称。"}
        self.attack_type_name = attack_type_name
        # {"en":"English name of attack event.", "zh_CN":"攻击事件英文名称。"}
        self.event_name_en = event_name_en
        # {"en":"Chinese name of attack event.", "zh_CN":"攻击事件中文名称。"}
        self.event_name = event_name

    def validate(self):
        self.validate_required(self.attack_count, 'attack_count')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.attack_event_type, 'attack_event_type')
        self.validate_required(self.attack_type_name_en, 'attack_type_name_en')
        self.validate_required(self.attack_type_name, 'attack_type_name')
        self.validate_required(self.event_name_en, 'event_name_en')
        self.validate_required(self.event_name, 'event_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_count is not None:
            result['attackCount'] = self.attack_count
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.ip is not None:
            result['ip'] = self.ip
        if self.attack_event_type is not None:
            result['attackEventType'] = self.attack_event_type
        if self.attack_type_name_en is not None:
            result['attackTypeNameEn'] = self.attack_type_name_en
        if self.attack_type_name is not None:
            result['attackTypeName'] = self.attack_type_name
        if self.event_name_en is not None:
            result['eventNameEn'] = self.event_name_en
        if self.event_name is not None:
            result['eventName'] = self.event_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackCount') is not None:
            self.attack_count = m.get('attackCount')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('attackEventType') is not None:
            self.attack_event_type = m.get('attackEventType')
        if m.get('attackTypeNameEn') is not None:
            self.attack_type_name_en = m.get('attackTypeNameEn')
        if m.get('attackTypeName') is not None:
            self.attack_type_name = m.get('attackTypeName')
        if m.get('eventNameEn') is not None:
            self.event_name_en = m.get('eventNameEn')
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        return self


class GetWAFAttackEventAttackEventList(TeaModel):
    def __init__(
        self,
        attack_event_list: List[GetWAFAttackEventAttackEvent] = None,
        total_count: int = None,
    ):
        # {"en":"Attack events.", "zh_CN":"攻击事件。"}
        self.attack_event_list = attack_event_list
        # {"en":"Number of attack events.", "zh_CN":"攻击事件数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.attack_event_list, 'attack_event_list')
        if self.attack_event_list:
            for k in self.attack_event_list:
                if k:
                    k.validate()
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_event_list is not None:
            result['attackEventList'] = []
            for k in self.attack_event_list:
                result['attackEventList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackEventList') is not None:
            self.attack_event_list = []
            for k in m.get('attackEventList'):
                temp_model = GetWAFAttackEventAttackEvent()
                self.attack_event_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetWAFAttackEventResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFAttackEventAttackEventList = None,
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
            temp_model = GetWAFAttackEventAttackEventList()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFAttackEventPaths(TeaModel):
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


class GetWAFAttackEventParameters(TeaModel):
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


class GetWAFAttackEventRequestHeader(TeaModel):
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


class GetWAFAttackEventResponseHeader(TeaModel):
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






class GetRiskEventNumberRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetRiskEventNumberVoData(TeaModel):
    def __init__(
        self,
        time: str = None,
        count: int = None,
    ):
        # {"en":"The time point of risk event, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"风险事件时间点，格式：yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"The number of risks at a certain point in time.", "zh_CN":"某时间点的风险数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetRiskEventNumberVo(TeaModel):
    def __init__(
        self,
        total: int = None,
        data: List[GetRiskEventNumberVoData] = None,
    ):
        # {"en":"The total number of risk events.", "zh_CN":"风险事件总数。"}
        self.total = total
        # {"en":"List of risk event.", "zh_CN":"风险事件列表。"}
        self.data = data

    def validate(self):
        self.validate_required(self.total, 'total')
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
        if self.total is not None:
            result['total'] = self.total
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetRiskEventNumberVoData()
                self.data.append(temp_model.from_map(k))
        return self


class GetRiskEventNumberResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetRiskEventNumberVo = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
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
            temp_model = GetRiskEventNumberVo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetRiskEventNumberPaths(TeaModel):
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


class GetRiskEventNumberParameters(TeaModel):
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


class GetRiskEventNumberRequestHeader(TeaModel):
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


class GetRiskEventNumberResponseHeader(TeaModel):
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






class GetWAFAttackedDomainRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        policys: List[str] = None,
    ):
        # {'en':'Domain, array.', 'zh_CN':'域名，数组'}
        self.domains = domains
        # {'en':'Start time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'开始时间，yyyy-MM-dd HH:mm:ss。'}
        self.start_time = start_time
        # {'en':'End time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'结束时间，yyyy-MM-dd HH:mm:ss。'}
        self.end_time = end_time
        # {'en':'Time zone, GMT+8 by default.', 'zh_CN':'时区，默认GMT+8，即“GMT+8”。'}
        self.time_zone = time_zone
        # {'en':'Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]', 'zh_CN':'触发策略类型，数组 
        # [protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]'}
        self.policys = policys

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.policys is not None:
            result['policys'] = self.policys
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
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        return self


class GetWAFAttackedDomainAttackedDomain(TeaModel):
    def __init__(
        self,
        domain: str = None,
        attack_type_top_1: str = None,
        total_hit_count: int = None,
        total_count: int = None,
        block_count: int = None,
        alert_count: int = None,
    ):
        # {"en":"Attacked domains.", "zh_CN":"受攻击域名。"}
        self.domain = domain
        # {"en":"Attack type top 1.", "zh_CN":"Top1攻击类型。"}
        self.attack_type_top_1 = attack_type_top_1
        # {"en":"Total requests.", "zh_CN":"检测请求数。"}
        self.total_hit_count = total_hit_count
        # {"en":"Attack requests", "zh_CN":"攻击请求数。"}
        self.total_count = total_count
        # {"en":"Block requests.", "zh_CN":"拦截请求数。"}
        self.block_count = block_count
        # {"en":"Log requests.", "zh_CN":"监控请求数。"}
        self.alert_count = alert_count

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.attack_type_top_1, 'attack_type_top_1')
        self.validate_required(self.total_hit_count, 'total_hit_count')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.block_count, 'block_count')
        self.validate_required(self.alert_count, 'alert_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.attack_type_top_1 is not None:
            result['attackTypeTop1'] = self.attack_type_top_1
        if self.total_hit_count is not None:
            result['totalHitCount'] = self.total_hit_count
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.block_count is not None:
            result['blockCount'] = self.block_count
        if self.alert_count is not None:
            result['alertCount'] = self.alert_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('attackTypeTop1') is not None:
            self.attack_type_top_1 = m.get('attackTypeTop1')
        if m.get('totalHitCount') is not None:
            self.total_hit_count = m.get('totalHitCount')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('blockCount') is not None:
            self.block_count = m.get('blockCount')
        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')
        return self


class GetWAFAttackedDomainAttackedDomainList(TeaModel):
    def __init__(
        self,
        all_total_count: int = None,
        all_block_count: int = None,
        count: int = None,
        list: List[GetWAFAttackedDomainAttackedDomain] = None,
    ):
        # {"en":"Total requests.", "zh_CN":"检测请求数。"}
        self.all_total_count = all_total_count
        # {"en":"Block requests.", "zh_CN":"拦截请求数。"}
        self.all_block_count = all_block_count
        # {"en":"Amount of list field.", "zh_CN":"List字段数据量。"}
        self.count = count
        # {"en":"Attacked domains.", "zh_CN":"受攻击域名。"}
        self.list = list

    def validate(self):
        self.validate_required(self.all_total_count, 'all_total_count')
        self.validate_required(self.all_block_count, 'all_block_count')
        self.validate_required(self.count, 'count')
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
        if self.all_total_count is not None:
            result['allTotalCount'] = self.all_total_count
        if self.all_block_count is not None:
            result['allBlockCount'] = self.all_block_count
        if self.count is not None:
            result['count'] = self.count
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allTotalCount') is not None:
            self.all_total_count = m.get('allTotalCount')
        if m.get('allBlockCount') is not None:
            self.all_block_count = m.get('allBlockCount')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = GetWAFAttackedDomainAttackedDomain()
                self.list.append(temp_model.from_map(k))
        return self


class GetWAFAttackedDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFAttackedDomainAttackedDomainList = None,
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
            temp_model = GetWAFAttackedDomainAttackedDomainList()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFAttackedDomainPaths(TeaModel):
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


class GetWAFAttackedDomainParameters(TeaModel):
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


class GetWAFAttackedDomainRequestHeader(TeaModel):
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


class GetWAFAttackedDomainResponseHeader(TeaModel):
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






class DmsThreatenAnalysisAttackedUrlsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        hostname: str = None,
        top_num: int = None,
    ):
        # {"en":"start time", "zh_CN":"开始时间"}
        self.start_time = start_time
        # {"en":"end time", "zh_CN":"结束时间"}
        self.end_time = end_time
        # {"en":"hostname", "zh_CN":"域名，多个用;分隔"}
        self.hostname = hostname
        # {"en":"top num", "zh_CN":"默认10条"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.hostname, 'hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.top_num is not None:
            result['topNum'] = self.top_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class DmsThreatenAnalysisAttackedUrlsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: dict = None,
        url: str = None,
        alarm_count: int = None,
        count: int = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data
        # {"en":"url", "zh_CN":"url"}
        self.url = url
        # {"en":"alarm count", "zh_CN":"告警数"}
        self.alarm_count = alarm_count
        # {"en":"all count", "zh_CN":"总数"}
        self.count = count

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')
        self.validate_required(self.url, 'url')
        self.validate_required(self.alarm_count, 'alarm_count')
        self.validate_required(self.count, 'count')

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
            result['data'] = self.data
        if self.url is not None:
            result['url'] = self.url
        if self.alarm_count is not None:
            result['alarmCount'] = self.alarm_count
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('alarmCount') is not None:
            self.alarm_count = m.get('alarmCount')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class DmsThreatenAnalysisAttackedUrlsPaths(TeaModel):
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


class DmsThreatenAnalysisAttackedUrlsParameters(TeaModel):
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


class DmsThreatenAnalysisAttackedUrlsRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class DmsThreatenAnalysisAttackedUrlsResponseHeader(TeaModel):
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






class GetBotRequestOverviewDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        return self


class GetBotRequestOverviewDataResponseData(TeaModel):
    def __init__(
        self,
        good_bot_request: int = None,
        relief_request: int = None,
        total_request: int = None,
        unknow_bot_request: int = None,
    ):
        # {"en":"Known bot type request count.", "zh_CN":"已知Bot类型请求数。"}
        self.good_bot_request = good_bot_request
        # {"en":"Relief bot attack count.", "zh_CN":"缓解Bot攻击数。"}
        self.relief_request = relief_request
        # {"en":"Total request count.", "zh_CN":"总请求数。"}
        self.total_request = total_request
        # {"en":"Unknown bot type request count.", "zh_CN":"未知Bot类型请求数。"}
        self.unknow_bot_request = unknow_bot_request

    def validate(self):
        self.validate_required(self.good_bot_request, 'good_bot_request')
        self.validate_required(self.relief_request, 'relief_request')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.unknow_bot_request, 'unknow_bot_request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.good_bot_request is not None:
            result['goodBotRequest'] = self.good_bot_request
        if self.relief_request is not None:
            result['reliefRequest'] = self.relief_request
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.unknow_bot_request is not None:
            result['unknowBotRequest'] = self.unknow_bot_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('goodBotRequest') is not None:
            self.good_bot_request = m.get('goodBotRequest')
        if m.get('reliefRequest') is not None:
            self.relief_request = m.get('reliefRequest')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('unknowBotRequest') is not None:
            self.unknow_bot_request = m.get('unknowBotRequest')
        return self


class GetBotRequestOverviewDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetBotRequestOverviewDataResponseData = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
            temp_model = GetBotRequestOverviewDataResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetBotRequestOverviewDataPaths(TeaModel):
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


class GetBotRequestOverviewDataParameters(TeaModel):
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


class GetBotRequestOverviewDataRequestHeader(TeaModel):
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


class GetBotRequestOverviewDataResponseHeader(TeaModel):
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






class GetTopAttackTargetsByPathRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default: 100, max: 1000.', 'zh_CN':'取前几排名，默认100，上限1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTopAttackTargetsByPathUrlTopDTO(TeaModel):
    def __init__(
        self,
        url: str = None,
        attack: int = None,
    ):
        # {'en':'URL.', 'zh_CN':'URL。'}
        self.url = url
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.attack = attack

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.attack, 'attack')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.attack is not None:
            result['attack'] = self.attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        return self


class GetTopAttackTargetsByPathResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopAttackTargetsByPathUrlTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopAttackTargetsByPathUrlTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopAttackTargetsByPathPaths(TeaModel):
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


class GetTopAttackTargetsByPathParameters(TeaModel):
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


class GetTopAttackTargetsByPathRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopAttackTargetsByPathResponseHeader(TeaModel):
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






class GetActiveApiTop5Request(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetActiveApiTop5Vo(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        count: int = None,
        url: str = None,
    ):
        # {"en":"API name.", "zh_CN":"API名称。"}
        self.api_name = api_name
        # {"en":"The total number of requests.", "zh_CN":"调用总次数。"}
        self.count = count
        # {"en":"HTTP request URL.", "zh_CN":"URL地址。"}
        self.url = url

    def validate(self):
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.count, 'count')
        self.validate_required(self.url, 'url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.count is not None:
            result['count'] = self.count
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetActiveApiTop5Response(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: List[GetActiveApiTop5Vo] = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetActiveApiTop5Vo()
                self.data.append(temp_model.from_map(k))
        return self


class GetActiveApiTop5Paths(TeaModel):
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


class GetActiveApiTop5Parameters(TeaModel):
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


class GetActiveApiTop5RequestHeader(TeaModel):
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


class GetActiveApiTop5ResponseHeader(TeaModel):
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






class GetBotRequestSourceIPTopDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
        top_num: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e. 'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetBotRequestSourceIPTopDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        province: str = None,
        count: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Area.", "zh_CN":"地区。"}
        self.province = province
        # {"en":"Bot request count.", "zh_CN":"Bot请求数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.province, 'province')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.province is not None:
            result['province'] = self.province
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetBotRequestSourceIPTopDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRequestSourceIPTopDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetBotRequestSourceIPTopDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRequestSourceIPTopDataPaths(TeaModel):
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


class GetBotRequestSourceIPTopDataParameters(TeaModel):
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


class GetBotRequestSourceIPTopDataRequestHeader(TeaModel):
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


class GetBotRequestSourceIPTopDataResponseHeader(TeaModel):
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






class CcAttackQpsForQueryRequest(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        package_id: str = None,
        need_detail: str = None,
        enddate: str = None,
        domains: str = None,
        custom_code: str = None,
        acctype: str = None,
    ):
        # {"en":"start time format: "yyyy-MM-dd HH:mm:ss"", "zh_CN":"开始时间("yyyy-MM-dd HH:mm:ss")"}
        self.startdate = startdate
        # {"en":"packageId or acctype should be selected at least one.", "zh_CN":"套餐ID: packageId和acctype至少传一个,但不能同时传"}
        self.package_id = package_id
        # {"en":"need Detail : 1
        # no need Detail: 0 default : 1", "zh_CN":"是否需要查看域名或是转发规则带宽的详细信息：0：不需要；1：需要，默认需要"}
        self.need_detail = need_detail
        # {"en":"end time format: "yyyy-MM-dd HH:mm:ss"", "zh_CN":"结束时间("yyyy-MM-dd HH:mm:ss")"}
        self.enddate = enddate
        # {"en":"domain, split by semicolon(";").", "zh_CN":"域名，支持多个用英文半角分号分隔；不传默认查询全部域名"}
        self.domains = domains
        # {"en":"custom code", "zh_CN":"客户英文名"}
        self.custom_code = custom_code
        # {"en":"packageId or acctype should be selected at least one. acctype( Only One can be selected): gess，fsa，app-s，dms-https，wss, dms， wss-https，s-appa， wsa，esa，wsa-https", "zh_CN":"packageId和acctype不能同时传且至少传一个；产品外部服务类型,只支持传1个:gess，fsa，app-s，dms-https，wss, dms， wss-https，s-appa， wsa，esa，wsa-https"}
        self.acctype = acctype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.package_id is not None:
            result['packageId'] = self.package_id
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.domains is not None:
            result['domains'] = self.domains
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.acctype is not None:
            result['acctype'] = self.acctype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('packageId') is not None:
            self.package_id = m.get('packageId')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('acctype') is not None:
            self.acctype = m.get('acctype')
        return self


class CcAttackQpsForQueryResponse(TeaModel):
    def __init__(
        self,
        msg: str = None,
        time: str = None,
        hit: int = None,
        hitdeny: int = None,
        code: str = None,
    ):
        # {"en":"response message", "zh_CN":"响应信息，成功时为success"}
        self.msg = msg
        # {"en":"Time of CC attack", "zh_CN":"统计CC攻击的时间"}
        self.time = time
        # {"en":"Number of total requests", "zh_CN":"总请求数"}
        self.hit = hit
        # {"en":"Number of CC attack", "zh_CN":"CC攻击次数"}
        self.hitdeny = hitdeny
        # {"en":"status code 200: success", "zh_CN":"状态码，成功为200；失败见“错误码”信息"}
        self.code = code

    def validate(self):
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.time, 'time')
        self.validate_required(self.hit, 'hit')
        self.validate_required(self.hitdeny, 'hitdeny')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.time is not None:
            result['time'] = self.time
        if self.hit is not None:
            result['hit'] = self.hit
        if self.hitdeny is not None:
            result['hitdeny'] = self.hitdeny
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        if m.get('hitdeny') is not None:
            self.hitdeny = m.get('hitdeny')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CcAttackQpsForQueryPaths(TeaModel):
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


class CcAttackQpsForQueryParameters(TeaModel):
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


class CcAttackQpsForQueryRequestHeader(TeaModel):
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


class CcAttackQpsForQueryResponseHeader(TeaModel):
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






class ListAttackLogsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        domain_list: List[str] = None,
        policy_type_list: List[str] = None,
        page_size: int = None,
        current_page: int = None,
    ):
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days. ', 'zh_CN':'开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days. ', 'zh_CN':'结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if  not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domain_list = domain_list
        # {'en':'Policy type list. 
        #  DMS_DEFEND: DDoS Protection
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  WAF_DEFEND: WAF
        #  BLOCK: IP/Geo Block
        #  CUSTOMIZE_RULE: Custom Rules
        #  RATE_LIMIT: Rate Limiting
        #  INTELLIGENCE: Threat Intelligence', 'zh_CN':'策略类型列表。
        # DMS_DEFEND：DDoS防护
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  WAF_DEFEND：WAF
        #  BLOCK：IP/区域封禁
        #  CUSTOMIZE_RULE：自定义规则
        #  RATE_LIMIT：频率限制
        #  INTELLIGENCE：威胁情报'}
        self.policy_type_list = policy_type_list
        # {'en':'The number of records per page, default value:10, maximum value 2000.', 'zh_CN':'每页显示的条目数，默认：10，最大：2000。'}
        self.page_size = page_size
        # {'en':'The current page, default value: 1.', 'zh_CN':'当前第几页，默认：1。'}
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.policy_type_list is not None:
            result['policyTypeList'] = self.policy_type_list
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('policyTypeList') is not None:
            self.policy_type_list = m.get('policyTypeList')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        return self


class ListAttackLogsAttackLogSimpleDto(TeaModel):
    def __init__(
        self,
        attack_time: str = None,
        client_ip: str = None,
        domain: str = None,
        uuid: str = None,
        request_id: str = None,
        policy_type: str = None,
        path: str = None,
        status_code: str = None,
        action: str = None,
    ):
        # {'en':'Attack time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'攻击时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.attack_time = attack_time
        # {'en':'Client IP location.', 'zh_CN':'客户端IP。'}
        self.client_ip = client_ip
        # {'en':'Hostname.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.uuid = uuid
        # {'en':'Requeset ID.', 'zh_CN':'请求ID。'}
        self.request_id = request_id
        # {'en':'Policy type. 
        #  DMS_DEFEND: DDoS Protection
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  WAF_DEFEND: WAF
        #  BLOCK: IP/Geo Block
        #  CUSTOMIZE_RULE: Custom Rules
        #  RATE_LIMIT: Rate Limiting
        #  INTELLIGENCE: Threat Intelligence', 'zh_CN':'策略类型。
        #  DMS_DEFEND：DDoS防护
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  WAF_DEFEND：WAF
        #  BLOCK：IP/区域封禁
        #  CUSTOMIZE_RULE：自定义规则
        #  RATE_LIMIT：频率限制
        #  INTELLIGENCE：威胁情报'}
        self.policy_type = policy_type
        # {'en':'Path.', 'zh_CN':'路径。'}
        self.path = path
        # {'en':'Status code.', 'zh_CN':'状态码。'}
        self.status_code = status_code
        # {'en':'Action.', 'zh_CN':'处理动作。'}
        self.action = action

    def validate(self):
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.path, 'path')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.action, 'action')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.domain is not None:
            result['domain'] = self.domain
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.path is not None:
            result['path'] = self.path
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class ListAttackLogsPageBean(TeaModel):
    def __init__(
        self,
        list: ListAttackLogsAttackLogSimpleDto = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page_count: int = None,
    ):
        # {'en':'Return content.', 'zh_CN':'返回内容。'}
        self.list = list
        # {'en':'The current page number.', 'zh_CN':'当前页码。'}
        self.page_num = page_num
        # {'en':'The number of records per page.', 'zh_CN':'每页显示的条目数。'}
        self.page_size = page_size
        # {'en':'The total number of records.', 'zh_CN':'总记录数。'}
        self.total_count = total_count
        # {'en':'The total number of pages.', 'zh_CN':'总页数。'}
        self.total_page_count = total_page_count

    def validate(self):
        self.validate_required(self.list, 'list')
        if self.list:
            self.list.validate()
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page_count, 'total_page_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['list'] = self.list.to_map()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.total_page_count is not None:
            result['totalPageCount'] = self.total_page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('list') is not None:
            temp_model = ListAttackLogsAttackLogSimpleDto()
            self.list = temp_model.from_map(m['list'])
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('totalPageCount') is not None:
            self.total_page_count = m.get('totalPageCount')
        return self


class ListAttackLogsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: ListAttackLogsPageBean = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
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
            temp_model = ListAttackLogsPageBean()
            self.data = temp_model.from_map(m['data'])
        return self


class ListAttackLogsPaths(TeaModel):
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


class ListAttackLogsParameters(TeaModel):
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


class ListAttackLogsRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class ListAttackLogsResponseHeader(TeaModel):
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






class GetTopAttackSourcesForClientIPsRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTopAttackSourcesForClientIPsAreaTopDTO(TeaModel):
    def __init__(
        self,
        area: str = None,
        value: int = None,
        ip: str = None,
    ):
        # {'en':'Source area(country or area, province).', 'zh_CN':'来源地区（国家或地区、省份）。'}
        self.area = area
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.value = value
        # {'en':'Source IP.', 'zh_CN':'来源IP。'}
        self.ip = ip

    def validate(self):
        self.validate_required(self.area, 'area')
        self.validate_required(self.value, 'value')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['area'] = self.area
        if self.value is not None:
            result['value'] = self.value
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class GetTopAttackSourcesForClientIPsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopAttackSourcesForClientIPsAreaTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopAttackSourcesForClientIPsAreaTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopAttackSourcesForClientIPsPaths(TeaModel):
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


class GetTopAttackSourcesForClientIPsParameters(TeaModel):
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


class GetTopAttackSourcesForClientIPsRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopAttackSourcesForClientIPsResponseHeader(TeaModel):
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






class GetSummaryRequestsRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetSummaryRequestsEventDTO(TeaModel):
    def __init__(
        self,
        total: int = None,
        attack: int = None,
        whitelist: int = None,
        resisted: int = None,
        observed: int = None,
    ):
        # {'en':'Total requests.', 'zh_CN':'总请求数。'}
        self.total = total
        # {'en':'Attack requests,sum of resisted requests and observed requests.', 'zh_CN':'攻击请求数，已抵御请求数与观察请求数之和。'}
        self.attack = attack
        # {'en':'Whitelist requests.', 'zh_CN':'白名单请求数。'}
        self.whitelist = whitelist
        # {'en':'Resisted requests.', 'zh_CN':'已抵御请求数。'}
        self.resisted = resisted
        # {'en':'Observed requests.', 'zh_CN':'观察请求数。'}
        self.observed = observed

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.attack, 'attack')
        self.validate_required(self.whitelist, 'whitelist')
        self.validate_required(self.resisted, 'resisted')
        self.validate_required(self.observed, 'observed')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.attack is not None:
            result['attack'] = self.attack
        if self.whitelist is not None:
            result['whitelist'] = self.whitelist
        if self.resisted is not None:
            result['resisted'] = self.resisted
        if self.observed is not None:
            result['observed'] = self.observed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        if m.get('whitelist') is not None:
            self.whitelist = m.get('whitelist')
        if m.get('resisted') is not None:
            self.resisted = m.get('resisted')
        if m.get('observed') is not None:
            self.observed = m.get('observed')
        return self


class GetSummaryRequestsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: GetSummaryRequestsEventDTO = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
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
            temp_model = GetSummaryRequestsEventDTO()
            self.data = temp_model.from_map(m['data'])
        return self


class GetSummaryRequestsPaths(TeaModel):
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


class GetSummaryRequestsParameters(TeaModel):
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


class GetSummaryRequestsRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetSummaryRequestsResponseHeader(TeaModel):
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






class GetActTypeDistributionDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime.Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        return self


class GetActTypeDistributionDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # {"en":"Action status.", "zh_CN":"处置状态。"}
        self.name = name
        # {"en":"Action times.", "zh_CN":"处置次数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetActTypeDistributionDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetActTypeDistributionDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned", "zh_CN":"返回数据"}
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
                temp_model = GetActTypeDistributionDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetActTypeDistributionDataPaths(TeaModel):
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


class GetActTypeDistributionDataParameters(TeaModel):
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


class GetActTypeDistributionDataRequestHeader(TeaModel):
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


class GetActTypeDistributionDataResponseHeader(TeaModel):
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






class GetBotRuleTypeTopDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime.Format:yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
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

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        return self


class GetBotRuleTypeTopDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # {"en":"Rule name.", "zh_CN":"规则名。"}
        self.name = name
        # {"en":"Trigger Times.", "zh_CN":"触发次数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetBotRuleTypeTopDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRuleTypeTopDataResponseData] = None,
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
                temp_model = GetBotRuleTypeTopDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRuleTypeTopDataPaths(TeaModel):
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


class GetBotRuleTypeTopDataParameters(TeaModel):
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


class GetBotRuleTypeTopDataRequestHeader(TeaModel):
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


class GetBotRuleTypeTopDataResponseHeader(TeaModel):
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






class GetWAFAttackTrendRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        interval_expression: str = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {"en":"Attack trend granularity, default value: 5m.
        # 5m: 5 minutes
        # 1h: hour
        # 1d: day", "zh_CN":"攻击趋势粒度，默认值：5m。
        # 5m：5分钟
        # 1h：小时
        # 1d：天"}
        self.interval_expression = interval_expression

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.interval_expression is not None:
            result['intervalExpression'] = self.interval_expression
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
        if m.get('intervalExpression') is not None:
            self.interval_expression = m.get('intervalExpression')
        return self


class GetWAFAttackTrendHitTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Total requests.", "zh_CN":"检测请求数。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendAttackTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendRuleTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Web rules.", "zh_CN":"Web规则防护。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendProtocolTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Protocol validation.", "zh_CN":"协议合规检测。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendWebShellTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Webshell access detection.", "zh_CN":"后门识别。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendAccessTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Access control/Rate limiting.", "zh_CN":"访问控制/限速。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendOtherTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"Time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"时间，yyyy-MM-dd HH:mm:ss。"}
        self.time = time
        # {"en":"Other rules.", "zh_CN":"其他防护规则。"}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetWAFAttackTrendAttackRequestTrend(TeaModel):
    def __init__(
        self,
        hit: List[GetWAFAttackTrendHitTrend] = None,
        attack: List[GetWAFAttackTrendAttackTrend] = None,
        rule: List[GetWAFAttackTrendRuleTrend] = None,
        protocol: List[GetWAFAttackTrendProtocolTrend] = None,
        web_shell: List[GetWAFAttackTrendWebShellTrend] = None,
        access: List[GetWAFAttackTrendAccessTrend] = None,
        other: List[GetWAFAttackTrendOtherTrend] = None,
    ):
        # {"en":"Total requests", "zh_CN":"检测请求数。"}
        self.hit = hit
        # {"en":"Attack requests", "zh_CN":"攻击请求数。"}
        self.attack = attack
        # {"en":"Web rules", "zh_CN":"Web规则防护。"}
        self.rule = rule
        # {"en":"Protocol validation", "zh_CN":"协议合规检测。"}
        self.protocol = protocol
        # {"en":"Webshell access detection", "zh_CN":"后门识别。"}
        self.web_shell = web_shell
        # {"en":"Access control/Rate limiting", "zh_CN":"访问控制/限速。"}
        self.access = access
        # {"en":"Other rules。", "zh_CN":"其他防护规则。"}
        self.other = other

    def validate(self):
        self.validate_required(self.hit, 'hit')
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()
        self.validate_required(self.attack, 'attack')
        if self.attack:
            for k in self.attack:
                if k:
                    k.validate()
        self.validate_required(self.rule, 'rule')
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()
        self.validate_required(self.protocol, 'protocol')
        if self.protocol:
            for k in self.protocol:
                if k:
                    k.validate()
        self.validate_required(self.web_shell, 'web_shell')
        if self.web_shell:
            for k in self.web_shell:
                if k:
                    k.validate()
        self.validate_required(self.access, 'access')
        if self.access:
            for k in self.access:
                if k:
                    k.validate()
        self.validate_required(self.other, 'other')
        if self.other:
            for k in self.other:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit is not None:
            result['hit'] = []
            for k in self.hit:
                result['hit'].append(k.to_map() if k else None)
        if self.attack is not None:
            result['attack'] = []
            for k in self.attack:
                result['attack'].append(k.to_map() if k else None)
        if self.rule is not None:
            result['rule'] = []
            for k in self.rule:
                result['rule'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['protocol'] = []
            for k in self.protocol:
                result['protocol'].append(k.to_map() if k else None)
        if self.web_shell is not None:
            result['webShell'] = []
            for k in self.web_shell:
                result['webShell'].append(k.to_map() if k else None)
        if self.access is not None:
            result['access'] = []
            for k in self.access:
                result['access'].append(k.to_map() if k else None)
        if self.other is not None:
            result['other'] = []
            for k in self.other:
                result['other'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hit') is not None:
            self.hit = []
            for k in m.get('hit'):
                temp_model = GetWAFAttackTrendHitTrend()
                self.hit.append(temp_model.from_map(k))
        if m.get('attack') is not None:
            self.attack = []
            for k in m.get('attack'):
                temp_model = GetWAFAttackTrendAttackTrend()
                self.attack.append(temp_model.from_map(k))
        if m.get('rule') is not None:
            self.rule = []
            for k in m.get('rule'):
                temp_model = GetWAFAttackTrendRuleTrend()
                self.rule.append(temp_model.from_map(k))
        if m.get('protocol') is not None:
            self.protocol = []
            for k in m.get('protocol'):
                temp_model = GetWAFAttackTrendProtocolTrend()
                self.protocol.append(temp_model.from_map(k))
        if m.get('webShell') is not None:
            self.web_shell = []
            for k in m.get('webShell'):
                temp_model = GetWAFAttackTrendWebShellTrend()
                self.web_shell.append(temp_model.from_map(k))
        if m.get('access') is not None:
            self.access = []
            for k in m.get('access'):
                temp_model = GetWAFAttackTrendAccessTrend()
                self.access.append(temp_model.from_map(k))
        if m.get('other') is not None:
            self.other = []
            for k in m.get('other'):
                temp_model = GetWAFAttackTrendOtherTrend()
                self.other.append(temp_model.from_map(k))
        return self


class GetWAFAttackTrendResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFAttackTrendAttackRequestTrend = None,
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
            temp_model = GetWAFAttackTrendAttackRequestTrend()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFAttackTrendPaths(TeaModel):
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


class GetWAFAttackTrendParameters(TeaModel):
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


class GetWAFAttackTrendRequestHeader(TeaModel):
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


class GetWAFAttackTrendResponseHeader(TeaModel):
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






class QueryDDoSAttackDetailsRequest(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        msec: str = None,
        acce_type: str = None,
    ):
        # {"en":"Start date format yyyy-MM-dd HH:mm:ss", "zh_CN":"起始日期 格式 yyyy-MM-dd HH:mm:ss"}
        self.startdate = startdate
        # {"en":"End date format yyyy-MM-dd HH:mm:ss", "zh_CN":"结束日期 格式 yyyy-MM-dd HH:mm:ss"}
        self.enddate = enddate
        # {"en":"Time zone, such as 28800000. The default is 28800000", "zh_CN":"时区，如：28800000 默认为：28800000"}
        self.msec = msec
        # {"en":"Business type: dms by default", "zh_CN":"业务类型,默认为dms"}
        self.acce_type = acce_type

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.msec is not None:
            result['msec'] = self.msec
        if self.acce_type is not None:
            result['acceType'] = self.acce_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('msec') is not None:
            self.msec = m.get('msec')
        if m.get('acceType') is not None:
            self.acce_type = m.get('acceType')
        return self


class QueryDDoSAttackDetailsResponseData(TeaModel):
    def __init__(
        self,
        total_flow: str = None,
        ip: str = None,
        time: str = None,
        type: str = None,
    ):
        # {'en':'attack peak value', 'zh_CN':'攻击峰值'}
        self.total_flow = total_flow
        # {'en':'IP', 'zh_CN':'IP'}
        self.ip = ip
        # {'en':'attack time', 'zh_CN':'攻击时间'}
        self.time = time
        # {'en':'attack type', 'zh_CN':'攻击类型'}
        self.type = type

    def validate(self):
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.time, 'time')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.ip is not None:
            result['ip'] = self.ip
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryDDoSAttackDetailsResponse(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        data: List[QueryDDoSAttackDetailsResponseData] = None,
        error_code: str = None,
        code: str = None,
    ):
        # {"en":"error response message", "zh_CN":"错误响应信息"}
        self.error_message = error_message
        # {'en':'result', 'zh_CN':'结果'}
        self.data = data
        # {"en":"error response code", "zh_CN":"错误响应码"}
        self.error_code = error_code
        # {"en":"response code", "zh_CN":"响应码"}
        self.code = code

    def validate(self):
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = QueryDDoSAttackDetailsResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class QueryDDoSAttackDetailsPaths(TeaModel):
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


class QueryDDoSAttackDetailsParameters(TeaModel):
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


class QueryDDoSAttackDetailsRequestHeader(TeaModel):
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


class QueryDDoSAttackDetailsResponseHeader(TeaModel):
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






class GetWAFRequestAndAttackEventRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GTM+8，即“GTM+8”。"}
        self.time_zone = time_zone

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        return self


class TotalRequest(TeaModel):
    def __init__(
        self,
        test_request: int = None,
        attack_request: int = None,
        block_request: int = None,
        high_risk_attack: int = None,
        continue_permeate: int = None,
        high_frequency_attack: int = None,
    ):
        # {"en":"Total requests.", "zh_CN":"检测请求数。"}
        self.test_request = test_request
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.attack_request = attack_request
        # {"en":"Block requests.", "zh_CN":"拦截请求数。"}
        self.block_request = block_request
        # {"en":"High risk threat requests.", "zh_CN":"高风险攻击请求数。"}
        self.high_risk_attack = high_risk_attack
        # {"en":"Persistent threat requests.", "zh_CN":"持续性渗透请求数。"}
        self.continue_permeate = continue_permeate
        # {"en":"High frequency threat requests.", "zh_CN":"高频率攻击请求数。"}
        self.high_frequency_attack = high_frequency_attack

    def validate(self):
        self.validate_required(self.test_request, 'test_request')
        self.validate_required(self.attack_request, 'attack_request')
        self.validate_required(self.block_request, 'block_request')
        self.validate_required(self.high_risk_attack, 'high_risk_attack')
        self.validate_required(self.continue_permeate, 'continue_permeate')
        self.validate_required(self.high_frequency_attack, 'high_frequency_attack')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.test_request is not None:
            result['testRequest'] = self.test_request
        if self.attack_request is not None:
            result['attackRequest'] = self.attack_request
        if self.block_request is not None:
            result['blockRequest'] = self.block_request
        if self.high_risk_attack is not None:
            result['highRiskAttack'] = self.high_risk_attack
        if self.continue_permeate is not None:
            result['continuePermeate'] = self.continue_permeate
        if self.high_frequency_attack is not None:
            result['highFrequencyAttack'] = self.high_frequency_attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('testRequest') is not None:
            self.test_request = m.get('testRequest')
        if m.get('attackRequest') is not None:
            self.attack_request = m.get('attackRequest')
        if m.get('blockRequest') is not None:
            self.block_request = m.get('blockRequest')
        if m.get('highRiskAttack') is not None:
            self.high_risk_attack = m.get('highRiskAttack')
        if m.get('continuePermeate') is not None:
            self.continue_permeate = m.get('continuePermeate')
        if m.get('highFrequencyAttack') is not None:
            self.high_frequency_attack = m.get('highFrequencyAttack')
        return self


class GetWAFRequestAndAttackEventResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: TotalRequest = None,
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
            temp_model = TotalRequest()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFRequestAndAttackEventPaths(TeaModel):
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


class GetWAFRequestAndAttackEventParameters(TeaModel):
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


class GetWAFRequestAndAttackEventRequestHeader(TeaModel):
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


class GetWAFRequestAndAttackEventResponseHeader(TeaModel):
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






class GetOriginalRequestInformationRequest(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        domain: str = None,
        attack_time: str = None,
    ):
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.uuid = uuid
        # {'en':'Hostname.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'Attack time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'攻击时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.attack_time = attack_time

    def validate(self):
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.attack_time, 'attack_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.domain is not None:
            result['domain'] = self.domain
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        return self


class GetOriginalRequestInformationAttackLogSeniorInfoDto(TeaModel):
    def __init__(
        self,
        request_head: str = None,
    ):
        # {'en':'Request header information.', 'zh_CN':'请求头信息。'}
        self.request_head = request_head

    def validate(self):
        self.validate_required(self.request_head, 'request_head')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_head is not None:
            result['requestHead'] = self.request_head
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestHead') is not None:
            self.request_head = m.get('requestHead')
        return self


class GetOriginalRequestInformationResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: GetOriginalRequestInformationAttackLogSeniorInfoDto = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
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
            temp_model = GetOriginalRequestInformationAttackLogSeniorInfoDto()
            self.data = temp_model.from_map(m['data'])
        return self


class GetOriginalRequestInformationPaths(TeaModel):
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


class GetOriginalRequestInformationParameters(TeaModel):
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


class GetOriginalRequestInformationRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetOriginalRequestInformationResponseHeader(TeaModel):
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






class GetDomainBotVisitDetailsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
    ):
        # {"en":"Domain.Separate by';'.", "zh_CN":"域名串，分号拼接"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        return self


class GetDomainBotVisitDetailsResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        total_request: int = None,
        bot_request: int = None,
        relief_attack: int = None,
        type_total: int = None,
        type: str = None,
    ):
        # {"en":"Domain.", "zh_CN":"域名。"}
        self.domain = domain
        # {"en":"Total request count.", "zh_CN":"总请求数。"}
        self.total_request = total_request
        # {"en":"Bot request count.", "zh_CN":"Bot请求数。"}
        self.bot_request = bot_request
        # {"en":"Relief attack count.", "zh_CN":"缓解攻击数。"}
        self.relief_attack = relief_attack
        # {"en":"Total attack type count.", "zh_CN":"攻击类型总数。"}
        self.type_total = type_total
        # {"en":"Top5 bot types.", "zh_CN":"Bot类型TOP5。"}
        self.type = type

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.bot_request, 'bot_request')
        self.validate_required(self.relief_attack, 'relief_attack')
        self.validate_required(self.type_total, 'type_total')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.bot_request is not None:
            result['botRequest'] = self.bot_request
        if self.relief_attack is not None:
            result['reliefAttack'] = self.relief_attack
        if self.type_total is not None:
            result['typeTotal'] = self.type_total
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('botRequest') is not None:
            self.bot_request = m.get('botRequest')
        if m.get('reliefAttack') is not None:
            self.relief_attack = m.get('reliefAttack')
        if m.get('typeTotal') is not None:
            self.type_total = m.get('typeTotal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDomainBotVisitDetailsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetDomainBotVisitDetailsResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetDomainBotVisitDetailsResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDomainBotVisitDetailsPaths(TeaModel):
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


class GetDomainBotVisitDetailsParameters(TeaModel):
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


class GetDomainBotVisitDetailsRequestHeader(TeaModel):
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


class GetDomainBotVisitDetailsResponseHeader(TeaModel):
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






class L4DdosTrendRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class L4DdosTrendAttackedUrl(TeaModel):
    def __init__(
        self,
        normal_bps: str = None,
        attack_bps: str = None,
        normal_pps: str = None,
        attack_pps: str = None,
        syn_bps: str = None,
        syn_pps: str = None,
        ack_bps: str = None,
        ack_pps: str = None,
        udp_bps: str = None,
        udp_pps: str = None,
        icmp_bps: str = None,
        icmp_pps: str = None,
        other_pps: str = None,
        other_bps: str = None,
        time: str = None,
    ):
        # {"en":"Normal bandwidth.(bps)", "zh_CN":"正常带宽。（bps）"}
        self.normal_bps = normal_bps
        # {"en":"Total cleaning bandwidth.", "zh_CN":"总清洗带宽。"}
        self.attack_bps = attack_bps
        # {"en":"Normal packages.(pps)", "zh_CN":"正常包数。（pps）"}
        self.normal_pps = normal_pps
        # {"en":"Total  packages.", "zh_CN":"总清洗包数。"}
        self.attack_pps = attack_pps
        # {"en":"SYN Flood.(bps)", "zh_CN":"SYN Flood。（bps）"}
        self.syn_bps = syn_bps
        # {"en":"SYN Flood.(pps)", "zh_CN":"SYN Flood。（pps）"}
        self.syn_pps = syn_pps
        # {"en":"ACK Flood.(bps)", "zh_CN":"ACK Flood。（bps）"}
        self.ack_bps = ack_bps
        # {"en":"ACK Flood.(pps)", "zh_CN":"ACK Flood。（pps）"}
        self.ack_pps = ack_pps
        # {"en":"UDP Flood. (bps)", "zh_CN":"UDP Flood。 (bps)"}
        self.udp_bps = udp_bps
        # {"en":"UDP Flood. (pps)", "zh_CN":"UDP Flood。 (pps)"}
        self.udp_pps = udp_pps
        # {"en":"ICMP Flood. (bps)", "zh_CN":"ICMP Flood。 (bps)"}
        self.icmp_bps = icmp_bps
        # {"en":"ICMP Flood. (pps)", "zh_CN":"ICMP Flood。 (pps)"}
        self.icmp_pps = icmp_pps
        # {"en":"Other Flood. (pps)", "zh_CN":"Other Flood。 (pps)"}
        self.other_pps = other_pps
        # {"en":"Other Flood.(bps)", "zh_CN":"Other Flood。(bps)"}
        self.other_bps = other_bps
        # {"en":"Time.", "zh_CN":"时间。"}
        self.time = time

    def validate(self):
        self.validate_required(self.normal_bps, 'normal_bps')
        self.validate_required(self.attack_bps, 'attack_bps')
        self.validate_required(self.normal_pps, 'normal_pps')
        self.validate_required(self.attack_pps, 'attack_pps')
        self.validate_required(self.syn_bps, 'syn_bps')
        self.validate_required(self.syn_pps, 'syn_pps')
        self.validate_required(self.ack_bps, 'ack_bps')
        self.validate_required(self.ack_pps, 'ack_pps')
        self.validate_required(self.udp_bps, 'udp_bps')
        self.validate_required(self.udp_pps, 'udp_pps')
        self.validate_required(self.icmp_bps, 'icmp_bps')
        self.validate_required(self.icmp_pps, 'icmp_pps')
        self.validate_required(self.other_pps, 'other_pps')
        self.validate_required(self.other_bps, 'other_bps')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.normal_bps is not None:
            result['normal_bps'] = self.normal_bps
        if self.attack_bps is not None:
            result['attack_bps'] = self.attack_bps
        if self.normal_pps is not None:
            result['normal_pps'] = self.normal_pps
        if self.attack_pps is not None:
            result['attack_pps'] = self.attack_pps
        if self.syn_bps is not None:
            result['syn_bps'] = self.syn_bps
        if self.syn_pps is not None:
            result['syn_pps'] = self.syn_pps
        if self.ack_bps is not None:
            result['ack_bps'] = self.ack_bps
        if self.ack_pps is not None:
            result['ack_pps'] = self.ack_pps
        if self.udp_bps is not None:
            result['udp_bps'] = self.udp_bps
        if self.udp_pps is not None:
            result['udp_pps'] = self.udp_pps
        if self.icmp_bps is not None:
            result['icmp_bps'] = self.icmp_bps
        if self.icmp_pps is not None:
            result['icmp_pps'] = self.icmp_pps
        if self.other_pps is not None:
            result['other_pps'] = self.other_pps
        if self.other_bps is not None:
            result['other_bps'] = self.other_bps
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('normal_bps') is not None:
            self.normal_bps = m.get('normal_bps')
        if m.get('attack_bps') is not None:
            self.attack_bps = m.get('attack_bps')
        if m.get('normal_pps') is not None:
            self.normal_pps = m.get('normal_pps')
        if m.get('attack_pps') is not None:
            self.attack_pps = m.get('attack_pps')
        if m.get('syn_bps') is not None:
            self.syn_bps = m.get('syn_bps')
        if m.get('syn_pps') is not None:
            self.syn_pps = m.get('syn_pps')
        if m.get('ack_bps') is not None:
            self.ack_bps = m.get('ack_bps')
        if m.get('ack_pps') is not None:
            self.ack_pps = m.get('ack_pps')
        if m.get('udp_bps') is not None:
            self.udp_bps = m.get('udp_bps')
        if m.get('udp_pps') is not None:
            self.udp_pps = m.get('udp_pps')
        if m.get('icmp_bps') is not None:
            self.icmp_bps = m.get('icmp_bps')
        if m.get('icmp_pps') is not None:
            self.icmp_pps = m.get('icmp_pps')
        if m.get('other_pps') is not None:
            self.other_pps = m.get('other_pps')
        if m.get('other_bps') is not None:
            self.other_bps = m.get('other_bps')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class L4DdosTrendPeak(TeaModel):
    def __init__(
        self,
        peak_time: str = None,
        peak_value: int = None,
    ):
        # {"en":"Maximum attack time.", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"Maximum attack value.", "zh_CN":"峰值"}
        self.peak_value = peak_value

    def validate(self):
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_time is not None:
            result['peak_time'] = self.peak_time
        if self.peak_value is not None:
            result['peak_value'] = self.peak_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('peak_time') is not None:
            self.peak_time = m.get('peak_time')
        if m.get('peak_value') is not None:
            self.peak_value = m.get('peak_value')
        return self


class L4DdosTrendResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[L4DdosTrendAttackedUrl] = None,
        peak_bps: List[L4DdosTrendPeak] = None,
        peak_pps: List[L4DdosTrendPeak] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data
        # {"en":"Maximum attack bps.", "zh_CN":"DDoS攻击带宽峰值"}
        self.peak_bps = peak_bps
        # {"en":"Maximum attack qps.", "zh_CN":"DDoS攻击包速峰值"}
        self.peak_pps = peak_pps

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.peak_bps, 'peak_bps')
        if self.peak_bps:
            for k in self.peak_bps:
                if k:
                    k.validate()
        self.validate_required(self.peak_pps, 'peak_pps')
        if self.peak_pps:
            for k in self.peak_pps:
                if k:
                    k.validate()

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
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.peak_bps is not None:
            result['peak_bps'] = []
            for k in self.peak_bps:
                result['peak_bps'].append(k.to_map() if k else None)
        if self.peak_pps is not None:
            result['peak_pps'] = []
            for k in self.peak_pps:
                result['peak_pps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = L4DdosTrendAttackedUrl()
                self.data.append(temp_model.from_map(k))
        if m.get('peak_bps') is not None:
            self.peak_bps = []
            for k in m.get('peak_bps'):
                temp_model = L4DdosTrendPeak()
                self.peak_bps.append(temp_model.from_map(k))
        if m.get('peak_pps') is not None:
            self.peak_pps = []
            for k in m.get('peak_pps'):
                temp_model = L4DdosTrendPeak()
                self.peak_pps.append(temp_model.from_map(k))
        return self


class L4DdosTrendPaths(TeaModel):
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


class L4DdosTrendParameters(TeaModel):
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


class L4DdosTrendRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class L4DdosTrendResponseHeader(TeaModel):
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






class GetWAFDomainHistoryRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
    ):
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class GetWAFDomainHistoryResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[str] = None,
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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetWAFDomainHistoryPaths(TeaModel):
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


class GetWAFDomainHistoryParameters(TeaModel):
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


class GetWAFDomainHistoryRequestHeader(TeaModel):
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


class GetWAFDomainHistoryResponseHeader(TeaModel):
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






class GetBotAccessURLTopDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        top_num: int = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e. 'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetBotAccessURLTopDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        # {"en":"URL.", "zh_CN":"统计类型"}
        self.name = name
        # {"en":"Bot request count.", "zh_CN":"Bot请求数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetBotAccessURLTopDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotAccessURLTopDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetBotAccessURLTopDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotAccessURLTopDataPaths(TeaModel):
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


class GetBotAccessURLTopDataParameters(TeaModel):
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


class GetBotAccessURLTopDataRequestHeader(TeaModel):
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


class GetBotAccessURLTopDataResponseHeader(TeaModel):
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






class GetBotRequestTypeDistributeDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
        top_num: int = None,
        type: str = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e. 'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num
        # {"en":"Bot type.
        #  0:All 
        #  1:known type bot 
        #  2:unknown type bot", "zh_CN":"Bot类型。 
        #  0：全部 
        #  1：已知bot 
        #  2：未知bot"}
        self.type = type

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
        if self.type is not None:
            result['type'] = self.type
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetBotRequestTypeDistributeDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: int = None,
    ):
        # {"en":"Policies Triggered.", "zh_CN":"触发规则。"}
        self.name = name
        # {"en":"Bot Type. 
        #   1:known type bot 
        #  2:unknown type bot", "zh_CN":"Bot类型。 
        #  1：已知bot 
        #  2：未知bot"}
        self.type = type
        # {"en":"Bot request count.", "zh_CN":"Bot请求数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetBotRequestTypeDistributeDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRequestTypeDistributeDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetBotRequestTypeDistributeDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRequestTypeDistributeDataPaths(TeaModel):
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


class GetBotRequestTypeDistributeDataParameters(TeaModel):
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


class GetBotRequestTypeDistributeDataRequestHeader(TeaModel):
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


class GetBotRequestTypeDistributeDataResponseHeader(TeaModel):
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






class GetTopAttackTargetsByHostnameRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 100, max: 1000.', 'zh_CN':'取前几排名，默认：100，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTopAttackTargetsByHostnameDomainTopDTO(TeaModel):
    def __init__(
        self,
        domain: str = None,
        attack: int = None,
    ):
        # {'en':'Hostname.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.attack = attack

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.attack, 'attack')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.attack is not None:
            result['attack'] = self.attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        return self


class GetTopAttackTargetsByHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopAttackTargetsByHostnameDomainTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopAttackTargetsByHostnameDomainTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopAttackTargetsByHostnamePaths(TeaModel):
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


class GetTopAttackTargetsByHostnameParameters(TeaModel):
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


class GetTopAttackTargetsByHostnameRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopAttackTargetsByHostnameResponseHeader(TeaModel):
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






class GetTopPoliciesTriggeredRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
        act_type: List[str] = None,
    ):
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        if self.act_type is not None:
            result['actType'] = self.act_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        return self


class GetTopPoliciesTriggeredEventTypeDTO(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: int = None,
    ):
        # {'en':'Attack type.
        #  BLOCK: IP/Geo Block
        #  DMS_DEFEND: DDoS Protection
        #  WAF_DEFEND: WAF
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  INTELLIGENCE: Threat Intelligence
        #  RATE_LIMIT: Rate Limiting
        #  CUSTOMIZE_RULE: Custom Rules', 'zh_CN':'攻击类型。
        #  BLOCK：IP/区域封禁
        #  DMS_DEFEND：DDoS防护
        #  WAF_DEFEND：WAF
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  INTELLIGENCE：威胁情报
        #  RATE_LIMIT：频率限制
        #  CUSTOMIZE_RULE：自定义规则'}
        self.code = code
        # {'en':'Number of requests that triggered the policy type.', 'zh_CN':'触发该策略类型的请求数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTopPoliciesTriggeredResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTopPoliciesTriggeredEventTypeDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTopPoliciesTriggeredEventTypeDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTopPoliciesTriggeredPaths(TeaModel):
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


class GetTopPoliciesTriggeredParameters(TeaModel):
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


class GetTopPoliciesTriggeredRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTopPoliciesTriggeredResponseHeader(TeaModel):
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






class GetDistributionOfWAFAttackTypeRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        attack_types: List[str] = None,
        acts: List[str] = None,
        top_num: int = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
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
        # {"en":"Action, defaule 1 and 2.
        # 1: Block
        # 2: Log", "zh_CN":"处理动作，默认1和2。
        # 1：拦截
        # 2：监控"}
        self.acts = acts
        # {"en":"Attack type top value, default 100.", "zh_CN":"攻击类型top值，默认100。"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.attack_types is not None:
            result['attackTypes'] = self.attack_types
        if self.acts is not None:
            result['acts'] = self.acts
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('attackTypes') is not None:
            self.attack_types = m.get('attackTypes')
        if m.get('acts') is not None:
            self.acts = m.get('acts')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetDistributionOfWAFAttackTypeAttackTypeTop(TeaModel):
    def __init__(
        self,
        attack_type_name_en: str = None,
        attack_type_name: str = None,
        total_count: int = None,
    ):
        # {"en":"English name of attack type.", "zh_CN":"攻击类型英文。"}
        self.attack_type_name_en = attack_type_name_en
        # {"en":"Chinese name of attack type.", "zh_CN":"攻击类型中文。"}
        self.attack_type_name = attack_type_name
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.attack_type_name_en, 'attack_type_name_en')
        self.validate_required(self.attack_type_name, 'attack_type_name')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type_name_en is not None:
            result['attackTypeNameEn'] = self.attack_type_name_en
        if self.attack_type_name is not None:
            result['attackTypeName'] = self.attack_type_name
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackTypeNameEn') is not None:
            self.attack_type_name_en = m.get('attackTypeNameEn')
        if m.get('attackTypeName') is not None:
            self.attack_type_name = m.get('attackTypeName')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetDistributionOfWAFAttackTypeAttackTypePage(TeaModel):
    def __init__(
        self,
        all_total_count: int = None,
        top: List[GetDistributionOfWAFAttackTypeAttackTypeTop] = None,
    ):
        # {"en":"Attack requests.", "zh_CN":"攻击请求数。"}
        self.all_total_count = all_total_count
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.top = top

    def validate(self):
        self.validate_required(self.all_total_count, 'all_total_count')
        self.validate_required(self.top, 'top')
        if self.top:
            for k in self.top:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_total_count is not None:
            result['allTotalCount'] = self.all_total_count
        if self.top is not None:
            result['top'] = []
            for k in self.top:
                result['top'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allTotalCount') is not None:
            self.all_total_count = m.get('allTotalCount')
        if m.get('top') is not None:
            self.top = []
            for k in m.get('top'):
                temp_model = GetDistributionOfWAFAttackTypeAttackTypeTop()
                self.top.append(temp_model.from_map(k))
        return self


class GetDistributionOfWAFAttackTypeResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetDistributionOfWAFAttackTypeAttackTypePage = None,
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
            temp_model = GetDistributionOfWAFAttackTypeAttackTypePage()
            self.data = temp_model.from_map(m['data'])
        return self


class GetDistributionOfWAFAttackTypePaths(TeaModel):
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


class GetDistributionOfWAFAttackTypeParameters(TeaModel):
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


class GetDistributionOfWAFAttackTypeRequestHeader(TeaModel):
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


class GetDistributionOfWAFAttackTypeResponseHeader(TeaModel):
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






class GetWAFTriggerRuleListRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        acts: List[str] = None,
        policys: List[str] = None,
    ):
        # {"en":"Domain, array.", "zh_CN":"域名，数组。"}
        self.domains = domains
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Time zone, GMT+8 by default.", "zh_CN":"时区，默认GMT+8，即“GMT+8”。"}
        self.time_zone = time_zone
        # {"en":"Action, default 1 and 2.
        #     1: Block
        #     2: Log", "zh_CN":"处理动作，默认1和2。
        #     1：拦截
        #     2：监控"}
        self.acts = acts
        # {"en":"Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]", "zh_CN":"触发策略类型，数组。[protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]"}
        self.policys = policys

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.policys is not None:
            result['policys'] = self.policys
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
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        return self


class GetWAFTriggerRuleListTriggerRule(TeaModel):
    def __init__(
        self,
        act: str = None,
        rule_name: str = None,
        attack_type: str = None,
        attack_type_name: str = None,
        attack_type_name_en: str = None,
        rule_id: str = None,
        total_count: str = None,
    ):
        # {"en":"Action.
        #     1: Block
        #     2: Log", "zh_CN":"处理动作。
        #     1：拦截
        #     2：监控"}
        self.act = act
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Attack type.", "zh_CN":"攻击类型。"}
        self.attack_type = attack_type
        # {"en":"Chinese name of attack type.", "zh_CN":"攻击类型中文名称。"}
        self.attack_type_name = attack_type_name
        # {"en":"English name of attack type.", "zh_CN":"攻击类型英文名称。"}
        self.attack_type_name_en = attack_type_name_en
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.rule_id = rule_id
        # {"en":"Trigger requests.", "zh_CN":"触发次数。"}
        self.total_count = total_count

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.attack_type, 'attack_type')
        self.validate_required(self.attack_type_name, 'attack_type_name')
        self.validate_required(self.attack_type_name_en, 'attack_type_name_en')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.attack_type_name is not None:
            result['attackTypeName'] = self.attack_type_name
        if self.attack_type_name_en is not None:
            result['attackTypeNameEn'] = self.attack_type_name_en
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('attackTypeName') is not None:
            self.attack_type_name = m.get('attackTypeName')
        if m.get('attackTypeNameEn') is not None:
            self.attack_type_name_en = m.get('attackTypeNameEn')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetWAFTriggerRuleListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFTriggerRuleListTriggerRule = None,
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
            temp_model = GetWAFTriggerRuleListTriggerRule()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFTriggerRuleListPaths(TeaModel):
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


class GetWAFTriggerRuleListParameters(TeaModel):
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


class GetWAFTriggerRuleListRequestHeader(TeaModel):
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


class GetWAFTriggerRuleListResponseHeader(TeaModel):
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






class GetWAFAttackedURLRequest(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: str = None,
        policys: List[str] = None,
    ):
        # {'en':'Domain, array.', 'zh_CN':'域名，数组。'}
        self.domains = domains
        # {'en':'Start time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'开始时间，yyyy-MM-dd HH:mm:ss。'}
        self.start_time = start_time
        # {'en':'End time, yyyy-MM-dd HH:mm:ss.', 'zh_CN':'结束时间，yyyy-MM-dd HH:mm:ss。'}
        self.end_time = end_time
        # {'en':'Time zone, GMT+8 by default.', 'zh_CN':'时区，默认GMT+8，即“GMT+8”。'}
        self.time_zone = time_zone
        # {'en':'Policy type, array. [protocol: Protocol Validation,
        # webShell: Webshell Access Detection,
        # other: Others Rules,
        # access: Access Control/Rate Limiting,
        # rule: WAF Rules]', 'zh_CN':'触发策略类型，数组 
        # [protocol：协议合规检测，
        # webShell：后门识别，
        # other：其他防护规则，
        # access：访问控制/限速，
        # rule：Web规则防护]'}
        self.policys = policys

    def validate(self):
        self.validate_required(self.domains, 'domains')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.policys is not None:
            result['policys'] = self.policys
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
        if m.get('policys') is not None:
            self.policys = m.get('policys')
        return self


class GetWAFAttackedURLAttackedUrl(TeaModel):
    def __init__(
        self,
        url: str = None,
        attack_type_top_1: str = None,
        total_count: int = None,
        block_count: int = None,
        alert_count: int = None,
    ):
        # {"en":"Attacked url", "zh_CN":"受攻击url。"}
        self.url = url
        # {"en":"Attack type top 1.", "zh_CN":"Top1攻击类型。"}
        self.attack_type_top_1 = attack_type_top_1
        # {"en":"Total requests of attacked url.", "zh_CN":"受攻击URL检测请求数。"}
        self.total_count = total_count
        # {"en":"Block requests of attacked url.", "zh_CN":"受攻击URL拦截请求数。"}
        self.block_count = block_count
        # {"en":"Log requests of attacked url.", "zh_CN":"受攻击URL监控请求数。"}
        self.alert_count = alert_count

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.attack_type_top_1, 'attack_type_top_1')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.block_count, 'block_count')
        self.validate_required(self.alert_count, 'alert_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.attack_type_top_1 is not None:
            result['attackTypeTop1'] = self.attack_type_top_1
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.block_count is not None:
            result['blockCount'] = self.block_count
        if self.alert_count is not None:
            result['alertCount'] = self.alert_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('attackTypeTop1') is not None:
            self.attack_type_top_1 = m.get('attackTypeTop1')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('blockCount') is not None:
            self.block_count = m.get('blockCount')
        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')
        return self


class GetWAFAttackedURLAttackedUrlList(TeaModel):
    def __init__(
        self,
        all_total_count: int = None,
        all_block_count: int = None,
        list: List[GetWAFAttackedURLAttackedUrl] = None,
    ):
        # {"en":"Total requests.", "zh_CN":"检测请求数。"}
        self.all_total_count = all_total_count
        # {"en":"Block requests.", "zh_CN":"拦截请求数。"}
        self.all_block_count = all_block_count
        # {"en":"Attacked url.", "zh_CN":"受攻击url。"}
        self.list = list

    def validate(self):
        self.validate_required(self.all_total_count, 'all_total_count')
        self.validate_required(self.all_block_count, 'all_block_count')
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
        if self.all_total_count is not None:
            result['allTotalCount'] = self.all_total_count
        if self.all_block_count is not None:
            result['allBlockCount'] = self.all_block_count
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allTotalCount') is not None:
            self.all_total_count = m.get('allTotalCount')
        if m.get('allBlockCount') is not None:
            self.all_block_count = m.get('allBlockCount')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = GetWAFAttackedURLAttackedUrl()
                self.list.append(temp_model.from_map(k))
        return self


class GetWAFAttackedURLResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetWAFAttackedURLAttackedUrlList = None,
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
            temp_model = GetWAFAttackedURLAttackedUrlList()
            self.data = temp_model.from_map(m['data'])
        return self


class GetWAFAttackedURLPaths(TeaModel):
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


class GetWAFAttackedURLParameters(TeaModel):
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


class GetWAFAttackedURLRequestHeader(TeaModel):
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


class GetWAFAttackedURLResponseHeader(TeaModel):
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






class GetL7DdosAnalysisAttackedUrlListV2Request(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        hostnames: List[str] = None,
        top_num: int = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time
        # {"en":"Hostname list.", "zh_CN":"域名数组。"}
        self.hostnames = hostnames
        # {"en":"Top num.", "zh_CN":"默认10条。"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.top_num is not None:
            result['topNum'] = self.top_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetL7DdosAnalysisAttackedUrlListV2AttackedUrl(TeaModel):
    def __init__(
        self,
        alarm_count: int = None,
        count: int = None,
        url: str = None,
    ):
        # {"en":"Observed Requests.", "zh_CN":"观察请求数。"}
        self.alarm_count = alarm_count
        # {"en":"Resisted Requests.", "zh_CN":"已抵御请求数。"}
        self.count = count
        # {"en":"URL.", "zh_CN":"URL。"}
        self.url = url

    def validate(self):
        self.validate_required(self.alarm_count, 'alarm_count')
        self.validate_required(self.count, 'count')
        self.validate_required(self.url, 'url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_count is not None:
            result['alarmCount'] = self.alarm_count
        if self.count is not None:
            result['count'] = self.count
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmCount') is not None:
            self.alarm_count = m.get('alarmCount')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetL7DdosAnalysisAttackedUrlListV2Response(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetL7DdosAnalysisAttackedUrlListV2AttackedUrl] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetL7DdosAnalysisAttackedUrlListV2AttackedUrl()
                self.data.append(temp_model.from_map(k))
        return self


class GetL7DdosAnalysisAttackedUrlListV2Paths(TeaModel):
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


class GetL7DdosAnalysisAttackedUrlListV2Parameters(TeaModel):
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


class GetL7DdosAnalysisAttackedUrlListV2RequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetL7DdosAnalysisAttackedUrlListV2ResponseHeader(TeaModel):
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






class GetTriggeredRateLimitingRulesRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTriggeredRateLimitingRulesRuleHitDTO(TeaModel):
    def __init__(
        self,
        act: str = None,
        value: int = None,
    ):
        # {'en':'Action.', 'zh_CN':'采取动作。'}
        self.act = act
        # {'en':'Hit times.', 'zh_CN':'命中数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTriggeredRateLimitingRulesRuleTopDTO(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        scene: str = None,
        hits: List[GetTriggeredRateLimitingRulesRuleHitDTO] = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Protected target.', 'zh_CN':'业务场景。'}
        self.scene = scene
        # {'en':'Trigger times, sort by times.', 'zh_CN':'触发次数，按次数排序。'}
        self.hits = hits

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.scene, 'scene')
        self.validate_required(self.hits, 'hits')
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.scene is not None:
            result['scene'] = self.scene
        if self.hits is not None:
            result['hits'] = []
            for k in self.hits:
                result['hits'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('hits') is not None:
            self.hits = []
            for k in m.get('hits'):
                temp_model = GetTriggeredRateLimitingRulesRuleHitDTO()
                self.hits.append(temp_model.from_map(k))
        return self


class GetTriggeredRateLimitingRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTriggeredRateLimitingRulesRuleTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTriggeredRateLimitingRulesRuleTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTriggeredRateLimitingRulesPaths(TeaModel):
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


class GetTriggeredRateLimitingRulesParameters(TeaModel):
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


class GetTriggeredRateLimitingRulesRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTriggeredRateLimitingRulesResponseHeader(TeaModel):
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






class GetConsumerNumberRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetConsumerNumberVo(TeaModel):
    def __init__(
        self,
        total: int = None,
        auth: int = None,
    ):
        # {"en":"The total number of consumers.", "zh_CN":"消费方总数。"}
        self.total = total
        # {"en":"The total number of authorized consumers.", "zh_CN":"已授权消费方总数。"}
        self.auth = auth

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.auth, 'auth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.auth is not None:
            result['auth'] = self.auth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('auth') is not None:
            self.auth = m.get('auth')
        return self


class GetConsumerNumberResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetConsumerNumberVo = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"数据。"}
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
            temp_model = GetConsumerNumberVo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetConsumerNumberPaths(TeaModel):
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


class GetConsumerNumberParameters(TeaModel):
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


class GetConsumerNumberRequestHeader(TeaModel):
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


class GetConsumerNumberResponseHeader(TeaModel):
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






class GetTriggeredWAFManagedRulesRequest(TeaModel):
    def __init__(
        self,
        top: int = None,
        act_type: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        domains: List[str] = None,
    ):
        # {'en':'Top rankings, default value: 10, max: 1000.', 'zh_CN':'取前几排名，默认：10，上限：1000。'}
        self.top = top
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'起始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'截止时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class GetTriggeredWAFManagedRulesRuleHitDTO(TeaModel):
    def __init__(
        self,
        act: str = None,
        value: int = None,
    ):
        # {'en':'Action.', 'zh_CN':'采取动作。'}
        self.act = act
        # {'en':'Hit times.', 'zh_CN':'命中数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.act, 'act')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['act'] = self.act
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetTriggeredWAFManagedRulesRuleTopDTO(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        action: str = None,
        hits: List[GetTriggeredWAFManagedRulesRuleHitDTO] = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Rule type.', 'zh_CN':'规则类型。'}
        self.rule_type = rule_type
        # {'en':'System recommended action.', 'zh_CN':'系统推荐动作。'}
        self.action = action
        # {'en':'Trigger times, sort by times.', 'zh_CN':'触发次数，按次数排序。'}
        self.hits = hits

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.action, 'action')
        self.validate_required(self.hits, 'hits')
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.action is not None:
            result['action'] = self.action
        if self.hits is not None:
            result['hits'] = []
            for k in self.hits:
                result['hits'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('hits') is not None:
            self.hits = []
            for k in m.get('hits'):
                temp_model = GetTriggeredWAFManagedRulesRuleHitDTO()
                self.hits.append(temp_model.from_map(k))
        return self


class GetTriggeredWAFManagedRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetTriggeredWAFManagedRulesRuleTopDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetTriggeredWAFManagedRulesRuleTopDTO()
                self.data.append(temp_model.from_map(k))
        return self


class GetTriggeredWAFManagedRulesPaths(TeaModel):
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


class GetTriggeredWAFManagedRulesParameters(TeaModel):
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


class GetTriggeredWAFManagedRulesRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetTriggeredWAFManagedRulesResponseHeader(TeaModel):
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






class GetBotRequestStatisticPerDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        top_num: int = None,
    ):
        # {"en":"Domain.Separate by';'.", "zh_CN":"域名串，分号拼接"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone, default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        if self.top_num is not None:
            result['topNum'] = self.top_num
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetBotRequestStatisticPerDomainResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Bot request count.", "zh_CN":"Bot请求数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetBotRequestStatisticPerDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRequestStatisticPerDomainResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetBotRequestStatisticPerDomainResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRequestStatisticPerDomainPaths(TeaModel):
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


class GetBotRequestStatisticPerDomainParameters(TeaModel):
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


class GetBotRequestStatisticPerDomainRequestHeader(TeaModel):
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


class GetBotRequestStatisticPerDomainResponseHeader(TeaModel):
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






class GetBotRequestTrendsAndTriggerRulesDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
    ):
        # {"en":"Domain.Separate by';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime.Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e. 'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang

    def validate(self):
        self.validate_required(self.domain, 'domain')
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
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrendDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Request times.", "zh_CN":"请求数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrend(TeaModel):
    def __init__(
        self,
        time: str = None,
        detail: List[GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrendDetail] = None,
    ):
        # {"en":"Request time.", "zh_CN":"请求时间。"}
        self.time = time
        # {"en":"Trend detail.", "zh_CN":"趋势详情。"}
        self.detail = detail

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.detail is not None:
            result['detail'] = []
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('detail') is not None:
            self.detail = []
            for k in m.get('detail'):
                temp_model = GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrendDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRuleDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Request times.", "zh_CN":"请求数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRule(TeaModel):
    def __init__(
        self,
        time: str = None,
        detail: List[GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRuleDetail] = None,
    ):
        # {"en":"Request time", "zh_CN":"请求时间。"}
        self.time = time
        # {"en":"Trigger rules detail.", "zh_CN":"触发规则详情。"}
        self.detail = detail

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.detail is not None:
            result['detail'] = []
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('detail') is not None:
            self.detail = []
            for k in m.get('detail'):
                temp_model = GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRuleDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponseData(TeaModel):
    def __init__(
        self,
        request_trend: List[GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrend] = None,
        trigger_rule: List[GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRule] = None,
    ):
        # {"en":"Request Trend.", "zh_CN":"请求趋势。"}
        self.request_trend = request_trend
        # {"en":"Trigger Rule.", "zh_CN":"触发规则。"}
        self.trigger_rule = trigger_rule

    def validate(self):
        self.validate_required(self.request_trend, 'request_trend')
        if self.request_trend:
            for k in self.request_trend:
                if k:
                    k.validate()
        self.validate_required(self.trigger_rule, 'trigger_rule')
        if self.trigger_rule:
            for k in self.trigger_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_trend is not None:
            result['requestTrend'] = []
            for k in self.request_trend:
                result['requestTrend'].append(k.to_map() if k else None)
        if self.trigger_rule is not None:
            result['triggerRule'] = []
            for k in self.trigger_rule:
                result['triggerRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestTrend') is not None:
            self.request_trend = []
            for k in m.get('requestTrend'):
                temp_model = GetBotRequestTrendsAndTriggerRulesDataResponseDataRequestTrend()
                self.request_trend.append(temp_model.from_map(k))
        if m.get('triggerRule') is not None:
            self.trigger_rule = []
            for k in m.get('triggerRule'):
                temp_model = GetBotRequestTrendsAndTriggerRulesDataResponseDataTriggerRule()
                self.trigger_rule.append(temp_model.from_map(k))
        return self


class GetBotRequestTrendsAndTriggerRulesDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetBotRequestTrendsAndTriggerRulesDataResponseData = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
            temp_model = GetBotRequestTrendsAndTriggerRulesDataResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetBotRequestTrendsAndTriggerRulesDataPaths(TeaModel):
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


class GetBotRequestTrendsAndTriggerRulesDataParameters(TeaModel):
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


class GetBotRequestTrendsAndTriggerRulesDataRequestHeader(TeaModel):
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


class GetBotRequestTrendsAndTriggerRulesDataResponseHeader(TeaModel):
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






class QueryEventTrendRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        act_type: List[str] = None,
        domains: List[str] = None,
    ):
        # {'en':'Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.start_time = start_time
        # {'en':'End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 31 days.', 'zh_CN':'结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过31天。'}
        self.end_time = end_time
        # {'en':'Multiple choice. Disposal result, default value: all results.
        #  mitigated: Mitegaed requests.
        #  monitored: monitored requests.', 'zh_CN':'多选。处置结果，默认：展示所有结果。
        #  mitigated：已抵御请求数。
        #  monitored：观察请求数。'}
        self.act_type = act_type
        # {'en':'Hostname list, if not specified, it means all the hostnames of the account.', 'zh_CN':'域名列表，未指定时查询账号下的所有域名。'}
        self.domains = domains

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.act_type is not None:
            result['actType'] = self.act_type
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('actType') is not None:
            self.act_type = m.get('actType')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class QueryEventTrendEventTypeDTO(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: int = None,
    ):
        # {'en':'Policy type.
        #  BLOCK: IP/Geo Block
        #  DMS_DEFEND: DDoS Protection
        #  WAF_DEFEND: WAF
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  INTELLIGENCE: Threat Intelligence
        #  RATE_LIMIT: Rate Limiting
        #  CUSTOMIZE_RULE: Custom Rules', 'zh_CN':'策略类型。
        #  BLOCK：IP/区域封禁
        #  DMS_DEFEND：DDoS防护
        #  WAF_DEFEND：WAF
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  INTELLIGENCE：威胁情报
        #  RATE_LIMIT：频率限制
        #  CUSTOMIZE_RULE：自定义规则'}
        self.code = code
        # {'en':'Number of policy requests of this type.', 'zh_CN':'该策略类型请求数。'}
        self.value = value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryEventTrendEventTrendDTO(TeaModel):
    def __init__(
        self,
        time_point: str = None,
        total: int = None,
        attack: int = None,
        mitigated: int = None,
        monitored: int = None,
        whitelist: int = None,
        distribution: List[QueryEventTrendEventTypeDTO] = None,
    ):
        # {'en':'Time point, format: yyyy-MM-dd HH-mm-ss.', 'zh_CN':'时间点，格式：yyyy-MM-dd HH-mm-ss。'}
        self.time_point = time_point
        # {'en':'Total requests.', 'zh_CN':'总请求数。'}
        self.total = total
        # {'en':'Attack requests.', 'zh_CN':'攻击请求数。'}
        self.attack = attack
        # {'en':'Mitigated requests.', 'zh_CN':'已抵御请求数。'}
        self.mitigated = mitigated
        # {'en':'Monitored requests.', 'zh_CN':'观察请求数。'}
        self.monitored = monitored
        # {'en':'Whitelist requests.', 'zh_CN':'白名单请求数。'}
        self.whitelist = whitelist
        # {'en':'Policy type classification requests.', 'zh_CN':'策略类型分类请求数。'}
        self.distribution = distribution

    def validate(self):
        self.validate_required(self.time_point, 'time_point')
        self.validate_required(self.total, 'total')
        self.validate_required(self.attack, 'attack')
        self.validate_required(self.mitigated, 'mitigated')
        self.validate_required(self.monitored, 'monitored')
        self.validate_required(self.whitelist, 'whitelist')
        self.validate_required(self.distribution, 'distribution')
        if self.distribution:
            for k in self.distribution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        if self.total is not None:
            result['total'] = self.total
        if self.attack is not None:
            result['attack'] = self.attack
        if self.mitigated is not None:
            result['mitigated'] = self.mitigated
        if self.monitored is not None:
            result['monitored'] = self.monitored
        if self.whitelist is not None:
            result['whitelist'] = self.whitelist
        if self.distribution is not None:
            result['distribution'] = []
            for k in self.distribution:
                result['distribution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('attack') is not None:
            self.attack = m.get('attack')
        if m.get('mitigated') is not None:
            self.mitigated = m.get('mitigated')
        if m.get('monitored') is not None:
            self.monitored = m.get('monitored')
        if m.get('whitelist') is not None:
            self.whitelist = m.get('whitelist')
        if m.get('distribution') is not None:
            self.distribution = []
            for k in m.get('distribution'):
                temp_model = QueryEventTrendEventTypeDTO()
                self.distribution.append(temp_model.from_map(k))
        return self


class QueryEventTrendResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[QueryEventTrendEventTrendDTO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = QueryEventTrendEventTrendDTO()
                self.data.append(temp_model.from_map(k))
        return self


class QueryEventTrendPaths(TeaModel):
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


class QueryEventTrendParameters(TeaModel):
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


class QueryEventTrendRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class QueryEventTrendResponseHeader(TeaModel):
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






class GetL7DdosAnalysisAttackedHostnameListV2Request(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        hostnames: List[str] = None,
        top_num: int = None,
    ):
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.
        # The time range does not exceed 30 days)", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 时间范围不超过30天。"}
        self.end_time = end_time
        # {"en":"Hostname list.", "zh_CN":"域名数组"}
        self.hostnames = hostnames
        # {"en":"Top num.", "zh_CN":"默认10条"}
        self.top_num = top_num

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.top_num is not None:
            result['topNum'] = self.top_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        return self


class GetL7DdosAnalysisAttackedHostnameListV2AttackedDomain(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        alarm_count: int = None,
        alarm_ratio: float = None,
        count: int = None,
        ratio: float = None,
        hostname: str = None,
    ):
        # {"en":"All count.", "zh_CN":"总请求。"}
        self.all_count = all_count
        # {"en":"Observed Requests..", "zh_CN":"观察请求数。"}
        self.alarm_count = alarm_count
        # {"en":"Observed Ratio.", "zh_CN":"观察请求占比。"}
        self.alarm_ratio = alarm_ratio
        # {"en":"Resisted Requests..", "zh_CN":"已抵御请求数。"}
        self.count = count
        # {"en":"Resisted Ratio.", "zh_CN":"已抵御请求占比。"}
        self.ratio = ratio
        # {"en":"Hostname.", "zh_CN":"域名。"}
        self.hostname = hostname

    def validate(self):
        self.validate_required(self.all_count, 'all_count')
        self.validate_required(self.alarm_count, 'alarm_count')
        self.validate_required(self.alarm_ratio, 'alarm_ratio')
        self.validate_required(self.count, 'count')
        self.validate_required(self.ratio, 'ratio')
        self.validate_required(self.hostname, 'hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_count is not None:
            result['all_count'] = self.all_count
        if self.alarm_count is not None:
            result['alarmCount'] = self.alarm_count
        if self.alarm_ratio is not None:
            result['alarmRatio'] = self.alarm_ratio
        if self.count is not None:
            result['count'] = self.count
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_count') is not None:
            self.all_count = m.get('all_count')
        if m.get('alarmCount') is not None:
            self.alarm_count = m.get('alarmCount')
        if m.get('alarmRatio') is not None:
            self.alarm_ratio = m.get('alarmRatio')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        return self


class GetL7DdosAnalysisAttackedHostnameListV2Response(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[GetL7DdosAnalysisAttackedHostnameListV2AttackedDomain] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetL7DdosAnalysisAttackedHostnameListV2AttackedDomain()
                self.data.append(temp_model.from_map(k))
        return self


class GetL7DdosAnalysisAttackedHostnameListV2Paths(TeaModel):
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


class GetL7DdosAnalysisAttackedHostnameListV2Parameters(TeaModel):
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


class GetL7DdosAnalysisAttackedHostnameListV2RequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetL7DdosAnalysisAttackedHostnameListV2ResponseHeader(TeaModel):
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






class GetInfrastructureLogListRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        client_ips: List[str] = None,
        target_ips: List[str] = None,
        rule_name: str = None,
        policy_names: List[str] = None,
        actions: List[str] = None,
        page_size: int = None,
        current_page: int = None,
    ):
        # {'en':'Start time, format:yyyy-MM-dd HH:mm:ss. 
        # Only supports querying logs of the past month, the query time range cannot exceed 24 hours.', 'zh_CN':'开始时间，格式：yyyy-MM-dd HH:mm:ss。
        # 仅支持查询近一个月的日志，查询时间范围不能超过24小时。'}
        self.start_time = start_time
        # {'en':'End time, format:yyyy-MM-dd HH:mm:ss. 
        # Only supports querying logs of the past month, the query time range cannot exceed 24 hours.', 'zh_CN':'结束时间，格式：yyyy-MM-dd HH:mm:ss。
        # 仅支持查询近一个月的日志，查询时间范围不能超过24小时，格式：yyyy-MM-dd HH:mm:ss。'}
        self.end_time = end_time
        # {'en':'Client IP.', 'zh_CN':'客户端IP。'}
        self.client_ips = client_ips
        # {'en':'Node IP.', 'zh_CN':'节点IP。'}
        self.target_ips = target_ips
        # {'en':'Rule Name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Policy Name.
        # rule_protection:Managed Ruleset Protection', 'zh_CN':'策略名称。
        # rule_protection：内置防护规则'}
        self.policy_names = policy_names
        # {'en':'Action.
        # connection_denied:Connection Refused', 'zh_CN':'处理动作。
        # connection_denied：拒绝连接'}
        self.actions = actions
        # {'en':'The number of records per page, default value:10', 'zh_CN':'每页显示的条目数。默认值：10'}
        self.page_size = page_size
        # {'en':'Current page, default:1', 'zh_CN':'当前第几页。默认值：1'}
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.policy_names, 'policy_names')
        self.validate_required(self.actions, 'actions')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.client_ips is not None:
            result['clientIps'] = self.client_ips
        if self.target_ips is not None:
            result['targetIps'] = self.target_ips
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.policy_names is not None:
            result['policyNames'] = self.policy_names
        if self.actions is not None:
            result['actions'] = self.actions
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('clientIps') is not None:
            self.client_ips = m.get('clientIps')
        if m.get('targetIps') is not None:
            self.target_ips = m.get('targetIps')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('policyNames') is not None:
            self.policy_names = m.get('policyNames')
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        return self


class GetInfrastructureLogListCsecInfrastructureLogVO(TeaModel):
    def __init__(
        self,
        attack_time: str = None,
        client_ip: str = None,
        target_ip: str = None,
        policy_name: str = None,
        rule_name: str = None,
        action: str = None,
        ip_site: str = None,
        content: str = None,
        target_port: str = None,
    ):
        # {'en':'Time.', 'zh_CN':'时间。'}
        self.attack_time = attack_time
        # {'en':'Client IP.', 'zh_CN':'客户端IP。'}
        self.client_ip = client_ip
        # {'en':'Node IP.', 'zh_CN':'节点IP。'}
        self.target_ip = target_ip
        # {'en':'Policy Name.', 'zh_CN':'策略名称。'}
        self.policy_name = policy_name
        # {'en':'Rule Name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Action.', 'zh_CN':'处理动作。'}
        self.action = action
        # {'en':'IP site.', 'zh_CN':'IP地理位置。'}
        self.ip_site = ip_site
        # {'en':'Explanation.', 'zh_CN':'异常说明。'}
        self.content = content
        # {'en':'Target port.', 'zh_CN':'目标端口。'}
        self.target_port = target_port

    def validate(self):
        self.validate_required(self.attack_time, 'attack_time')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.target_ip, 'target_ip')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.action, 'action')
        self.validate_required(self.ip_site, 'ip_site')
        self.validate_required(self.content, 'content')
        self.validate_required(self.target_port, 'target_port')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.target_ip is not None:
            result['targetIp'] = self.target_ip
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.action is not None:
            result['action'] = self.action
        if self.ip_site is not None:
            result['ipSite'] = self.ip_site
        if self.content is not None:
            result['content'] = self.content
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('targetIp') is not None:
            self.target_ip = m.get('targetIp')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('ipSite') is not None:
            self.ip_site = m.get('ipSite')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        return self


class GetInfrastructureLogListPageVO(TeaModel):
    def __init__(
        self,
        current: int = None,
        size: int = None,
        pages: int = None,
        total: int = None,
        records: GetInfrastructureLogListCsecInfrastructureLogVO = None,
    ):
        # {'en':'The current page number.', 'zh_CN':'当前页码。'}
        self.current = current
        # {'en':'The number of records per page.', 'zh_CN':'每页显示的条目数。'}
        self.size = size
        # {'en':'Pages.', 'zh_CN':'页数。'}
        self.pages = pages
        # {'en':'The total number of records.', 'zh_CN':'总记录数。'}
        self.total = total
        # {'en':'Records.', 'zh_CN':'记录。'}
        self.records = records

    def validate(self):
        self.validate_required(self.current, 'current')
        self.validate_required(self.size, 'size')
        self.validate_required(self.pages, 'pages')
        self.validate_required(self.total, 'total')
        self.validate_required(self.records, 'records')
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.size is not None:
            result['size'] = self.size
        if self.pages is not None:
            result['pages'] = self.pages
        if self.total is not None:
            result['total'] = self.total
        if self.records is not None:
            result['records'] = self.records.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('records') is not None:
            temp_model = GetInfrastructureLogListCsecInfrastructureLogVO()
            self.records = temp_model.from_map(m['records'])
        return self


class GetInfrastructureLogListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: GetInfrastructureLogListPageVO = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
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
            temp_model = GetInfrastructureLogListPageVO()
            self.data = temp_model.from_map(m['data'])
        return self


class GetInfrastructureLogListPaths(TeaModel):
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


class GetInfrastructureLogListParameters(TeaModel):
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


class GetInfrastructureLogListRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class GetInfrastructureLogListResponseHeader(TeaModel):
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






class GetBotRequestSourceDistributionDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        time_zone: int = None,
        lang: str = None,
        top_num: int = None,
        type: str = None,
    ):
        # {"en":"Domain.Separate by ';'.", "zh_CN":"域名。多个以;隔开"}
        self.domain = domain
        # {"en":"StartTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"开始时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.start_time = start_time
        # {"en":"EndTime. Format: yyyy-MM-dd HH:mm:ss", "zh_CN":"结束时间。格式： yyyy-MM-dd HH:mm:ss"}
        self.end_time = end_time
        # {"en":"Time zone. Default 8, i.e.'GTM+8'", "zh_CN":"时区，默认8，即“GTM+8”"}
        self.time_zone = time_zone
        # {"en":"Language type. Default cn. 
        #  en:English 
        #  cn:Chinese ", "zh_CN":"语言类型。 默认cn 
        #  en：英文 
        #  cn：中文"}
        self.lang = lang
        # {"en":"Number of top values.Default value 10", "zh_CN":"排名最前值数目。默认10"}
        self.top_num = top_num
        # {"en":"Area search type. 
        #  0:Global 
        #  1:China ", "zh_CN":"地区查询类型。 
        #  0：全球 
        #  1：中国"}
        self.type = type

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.type, 'type')

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
        if self.top_num is not None:
            result['topNum'] = self.top_num
        if self.type is not None:
            result['type'] = self.type
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
        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetBotRequestSourceDistributionDataResponseData(TeaModel):
    def __init__(
        self,
        name: str = None,
        count: int = None,
    ):
        # {"en":"Statistical type.", "zh_CN":"统计类型。"}
        self.name = name
        # {"en":"Bot request count", "zh_CN":"Bot请求数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetBotRequestSourceDistributionDataResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[GetBotRequestSourceDistributionDataResponseData] = None,
    ):
        # {"en":"Status code, success is '200'.", "zh_CN":"状态码，成功为“200”。"}
        self.code = code
        # {"en":"Return message, success is 'Success'.", "zh_CN":"返回信息，成功为“Success”。"}
        self.message = message
        # {"en":"Data returned.", "zh_CN":"返回数据。"}
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
                temp_model = GetBotRequestSourceDistributionDataResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetBotRequestSourceDistributionDataPaths(TeaModel):
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


class GetBotRequestSourceDistributionDataParameters(TeaModel):
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


class GetBotRequestSourceDistributionDataRequestHeader(TeaModel):
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


class GetBotRequestSourceDistributionDataResponseHeader(TeaModel):
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






class QueryAttackLogDetailInfoRequest(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        request_id: str = None,
        domain: str = None,
        policy_type: str = None,
        attack_time: str = None,
    ):
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.uuid = uuid
        # {'en':'Request ID.', 'zh_CN':'请求ID。'}
        self.request_id = request_id
        # {'en':'Hostname.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'Policy type. 
        #  DMS_DEFEND: DDoS Protection
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  WAF_DEFEND: WAF
        #  BLOCK: IP/Geo Block
        #  CUSTOMIZE_RULE: Custom Rules
        #  RATE_LIMIT: Rate Limiting
        #  INTELLIGENCE: Threat Intelligence', 'zh_CN':'策略类型。
        #  DMS_DEFEND：DDoS防护
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  WAF_DEFEND：WAF
        #  BLOCK：IP/区域封禁
        #  CUSTOMIZE_RULE：自定义规则
        #  RATE_LIMIT：频率限制
        #  INTELLIGENCE：威胁情报'}
        self.policy_type = policy_type
        # {'en':'Attack time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'攻击时间，时间格式：yyyy-MM-dd HH:mm:ss。'}
        self.attack_time = attack_time

    def validate(self):
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.attack_time, 'attack_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.domain is not None:
            result['domain'] = self.domain
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.attack_time is not None:
            result['attackTime'] = self.attack_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('attackTime') is not None:
            self.attack_time = m.get('attackTime')
        return self


class QueryAttackLogDetailInfoAttackLogBasicInfoDto(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uuid: str = None,
        request_method: str = None,
        http_version: str = None,
        path: str = None,
        uri: str = None,
        user_agent: str = None,
        referer: str = None,
        status_code: str = None,
        client_ip: str = None,
        ip_location: str = None,
        user_finger: str = None,
        browser_finger: str = None,
        device_finger: str = None,
        app_name: str = None,
        app_version: str = None,
        app_id: str = None,
        app_package_name: str = None,
        sdk_version: str = None,
    ):
        # {'en':'Request ID.', 'zh_CN':'请求ID。'}
        self.request_id = request_id
        # {'en':'Event ID.', 'zh_CN':'事件ID。'}
        self.uuid = uuid
        # {'en':'Request Method.', 'zh_CN':'请求方法。'}
        self.request_method = request_method
        # {'en':'Http Version.', 'zh_CN':'HTTP版本。'}
        self.http_version = http_version
        # {'en':'Path.', 'zh_CN':'路径。'}
        self.path = path
        # {'en':'URI.', 'zh_CN':'URI。'}
        self.uri = uri
        # {'en':'User-Agent.', 'zh_CN':'User-Agent。'}
        self.user_agent = user_agent
        # {'en':'Referer.', 'zh_CN':'Referer。'}
        self.referer = referer
        # {'en':'Status Code.', 'zh_CN':'状态码。'}
        self.status_code = status_code
        # {'en':'Client IP.', 'zh_CN':'客户端IP。'}
        self.client_ip = client_ip
        # {'en':'IP geolocation.', 'zh_CN':'IP地理位置。'}
        self.ip_location = ip_location
        # {'en':'Client ID.', 'zh_CN':'客户端ID。'}
        self.user_finger = user_finger
        # {'en':'Browser fingerprint.', 'zh_CN':'浏览器指纹。'}
        self.browser_finger = browser_finger
        # {'en':'Device fingerprint.', 'zh_CN':'设备指纹。'}
        self.device_finger = device_finger
        # {'en':'APP name.', 'zh_CN':'APP名称。'}
        self.app_name = app_name
        # {'en':'APP version.', 'zh_CN':'APP版本。'}
        self.app_version = app_version
        # {'en':'APP ID.', 'zh_CN':'APP ID。'}
        self.app_id = app_id
        # {'en':'APP .', 'zh_CN':'APP包名。'}
        self.app_package_name = app_package_name
        # {'en':'SDK version.', 'zh_CN':'SDK版本。'}
        self.sdk_version = sdk_version

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.http_version, 'http_version')
        self.validate_required(self.path, 'path')
        self.validate_required(self.uri, 'uri')
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.ip_location, 'ip_location')
        self.validate_required(self.user_finger, 'user_finger')
        self.validate_required(self.browser_finger, 'browser_finger')
        self.validate_required(self.device_finger, 'device_finger')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.app_version, 'app_version')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_package_name, 'app_package_name')
        self.validate_required(self.sdk_version, 'sdk_version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.http_version is not None:
            result['httpVersion'] = self.http_version
        if self.path is not None:
            result['path'] = self.path
        if self.uri is not None:
            result['uri'] = self.uri
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.referer is not None:
            result['referer'] = self.referer
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.ip_location is not None:
            result['ipLocation'] = self.ip_location
        if self.user_finger is not None:
            result['userFinger'] = self.user_finger
        if self.browser_finger is not None:
            result['browserFinger'] = self.browser_finger
        if self.device_finger is not None:
            result['deviceFinger'] = self.device_finger
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_package_name is not None:
            result['appPackageName'] = self.app_package_name
        if self.sdk_version is not None:
            result['sdkVersion'] = self.sdk_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('httpVersion') is not None:
            self.http_version = m.get('httpVersion')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('ipLocation') is not None:
            self.ip_location = m.get('ipLocation')
        if m.get('userFinger') is not None:
            self.user_finger = m.get('userFinger')
        if m.get('browserFinger') is not None:
            self.browser_finger = m.get('browserFinger')
        if m.get('deviceFinger') is not None:
            self.device_finger = m.get('deviceFinger')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appPackageName') is not None:
            self.app_package_name = m.get('appPackageName')
        if m.get('sdkVersion') is not None:
            self.sdk_version = m.get('sdkVersion')
        return self


class QueryAttackLogDetailInfoAttackLogIpBlockDto(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        rule_action: str = None,
        explain: str = None,
    ):
        # {'en':'Policy name.', 'zh_CN':'策略名称。'}
        self.policy_name = policy_name
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Description.', 'zh_CN':'说明。'}
        self.explain = explain

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.explain, 'explain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.explain is not None:
            result['explain'] = self.explain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('explain') is not None:
            self.explain = m.get('explain')
        return self


class QueryAttackLogDetailInfoAttackLogWafRuleDto(TeaModel):
    def __init__(
        self,
        rule_type: str = None,
        rule_action: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_desc: str = None,
        match_area: str = None,
        match_content: str = None,
    ):
        # {'en':'Rule type.', 'zh_CN':'规则类型。'}
        self.rule_type = rule_type
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Rule description.', 'zh_CN':'规则描述。'}
        self.rule_desc = rule_desc
        # {'en':'Hit request area.', 'zh_CN':'命中请求区域。'}
        self.match_area = match_area
        # {'en':'Hit request content.', 'zh_CN':'命中请求内容。'}
        self.match_content = match_content

    def validate(self):
        self.validate_required(self.rule_type, 'rule_type')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_desc, 'rule_desc')
        self.validate_required(self.match_area, 'match_area')
        self.validate_required(self.match_content, 'match_content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['ruleType'] = self.rule_type
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc
        if self.match_area is not None:
            result['matchArea'] = self.match_area
        if self.match_content is not None:
            result['matchContent'] = self.match_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')
        if m.get('matchArea') is not None:
            self.match_area = m.get('matchArea')
        if m.get('matchContent') is not None:
            self.match_content = m.get('matchContent')
        return self


class QueryAttackLogDetailInfoAttackLogDdosRuleDto(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        rule_action: str = None,
        rule_id: str = None,
        rule_name: str = None,
        explain: str = None,
    ):
        # {'en':'Policy name.', 'zh_CN':'策略名称。'}
        self.policy_name = policy_name
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Description.', 'zh_CN':'说明。'}
        self.explain = explain

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.explain, 'explain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.explain is not None:
            result['explain'] = self.explain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('explain') is not None:
            self.explain = m.get('explain')
        return self


class QueryAttackLogDetailInfoAttackLogBotRuleDto(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        rule_action: str = None,
        rule_name: str = None,
        bot_category: str = None,
        bot_label: str = None,
        event_desc: str = None,
    ):
        # {'en':'Policy name.', 'zh_CN':'策略名称。'}
        self.policy_name = policy_name
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Bot Category.', 'zh_CN':'Bot分类。'}
        self.bot_category = bot_category
        # {'en':'Bot tag.', 'zh_CN':'Bot标签。'}
        self.bot_label = bot_label
        # {'en':'Event description.', 'zh_CN':'事件描述。'}
        self.event_desc = event_desc

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.bot_category, 'bot_category')
        self.validate_required(self.bot_label, 'bot_label')
        self.validate_required(self.event_desc, 'event_desc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.bot_category is not None:
            result['botCategory'] = self.bot_category
        if self.bot_label is not None:
            result['botLabel'] = self.bot_label
        if self.event_desc is not None:
            result['eventDesc'] = self.event_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('botCategory') is not None:
            self.bot_category = m.get('botCategory')
        if m.get('botLabel') is not None:
            self.bot_label = m.get('botLabel')
        if m.get('eventDesc') is not None:
            self.event_desc = m.get('eventDesc')
        return self


class QueryAttackLogDetailInfoAttackLogApiRuleDto(TeaModel):
    def __init__(
        self,
        rule_action: str = None,
        policy_name: str = None,
        api_name: str = None,
        api_id: str = None,
        explain_en: str = None,
        explain_cn: str = None,
    ):
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Policy name.', 'zh_CN':'策略名称。'}
        self.policy_name = policy_name
        # {'en':'API name.', 'zh_CN':'API名称。'}
        self.api_name = api_name
        # {'en':'API ID.', 'zh_CN':'API ID。'}
        self.api_id = api_id
        # {'en':'English instructions.', 'zh_CN':'英文说明。'}
        self.explain_en = explain_en
        # {'en':'Chinese instructions, only supported in language=zh_CN', 'zh_CN':'中文说明，仅当language=zh_CN支持。'}
        self.explain_cn = explain_cn

    def validate(self):
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.explain_en, 'explain_en')
        self.validate_required(self.explain_cn, 'explain_cn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.explain_en is not None:
            result['explainEn'] = self.explain_en
        if self.explain_cn is not None:
            result['explainCn'] = self.explain_cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('explainEn') is not None:
            self.explain_en = m.get('explainEn')
        if m.get('explainCn') is not None:
            self.explain_cn = m.get('explainCn')
        return self


class QueryAttackLogDetailInfoAttackLogIntelligentDto(TeaModel):
    def __init__(
        self,
        intelligent_type: str = None,
        rule_action: str = None,
        intelligent_module: str = None,
    ):
        # {'en':'Threat type.', 'zh_CN':'情报类型。'}
        self.intelligent_type = intelligent_type
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'Intelligence module.', 'zh_CN':'情报模块。'}
        self.intelligent_module = intelligent_module

    def validate(self):
        self.validate_required(self.intelligent_type, 'intelligent_type')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.intelligent_module, 'intelligent_module')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intelligent_type is not None:
            result['intelligentType'] = self.intelligent_type
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.intelligent_module is not None:
            result['intelligentModule'] = self.intelligent_module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intelligentType') is not None:
            self.intelligent_type = m.get('intelligentType')
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('intelligentModule') is not None:
            self.intelligent_module = m.get('intelligentModule')
        return self


class QueryAttackLogDetailInfoAttackLogRateLimitDto(TeaModel):
    def __init__(
        self,
        rule_action: str = None,
        api_name: str = None,
        api_id: str = None,
        rule_name: str = None,
        rule_id: str = None,
        rule_desc: str = None,
    ):
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'API name.', 'zh_CN':'API名称。'}
        self.api_name = api_name
        # {'en':'API ID.', 'zh_CN':'API ID。'}
        self.api_id = api_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule description.', 'zh_CN':'规则描述。'}
        self.rule_desc = rule_desc

    def validate(self):
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_desc, 'rule_desc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')
        return self


class QueryAttackLogDetailInfoAttackLogCustomizeRuleDto(TeaModel):
    def __init__(
        self,
        rule_action: str = None,
        api_name: str = None,
        api_id: str = None,
        rule_name: str = None,
        rule_id: str = None,
        rule_desc: str = None,
    ):
        # {'en':'Rule action.', 'zh_CN':'规则动作。'}
        self.rule_action = rule_action
        # {'en':'API name.', 'zh_CN':'API名称。'}
        self.api_name = api_name
        # {'en':'API ID.', 'zh_CN':'API ID。'}
        self.api_id = api_id
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.rule_id = rule_id
        # {'en':'Rule description.', 'zh_CN':'规则描述。'}
        self.rule_desc = rule_desc

    def validate(self):
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.api_name, 'api_name')
        self.validate_required(self.api_id, 'api_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_desc, 'rule_desc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action is not None:
            result['ruleAction'] = self.rule_action
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_desc is not None:
            result['ruleDesc'] = self.rule_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleAction') is not None:
            self.rule_action = m.get('ruleAction')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleDesc') is not None:
            self.rule_desc = m.get('ruleDesc')
        return self


class QueryAttackLogDetailInfoAttackLogDetailDto(TeaModel):
    def __init__(
        self,
        block_policy_name: str = None,
        block: QueryAttackLogDetailInfoAttackLogIpBlockDto = None,
        waf__defend: List[QueryAttackLogDetailInfoAttackLogWafRuleDto] = None,
        dms__defend: List[QueryAttackLogDetailInfoAttackLogDdosRuleDto] = None,
        bot__manage: List[QueryAttackLogDetailInfoAttackLogBotRuleDto] = None,
        api__defend: List[QueryAttackLogDetailInfoAttackLogApiRuleDto] = None,
        intelligence: List[QueryAttackLogDetailInfoAttackLogIntelligentDto] = None,
        rate__limit: List[QueryAttackLogDetailInfoAttackLogRateLimitDto] = None,
        customize__rule: List[QueryAttackLogDetailInfoAttackLogCustomizeRuleDto] = None,
    ):
        # {'en':'The policy type of hit interception, empty when not intercepted. 
        #  DMS_DEFEND: DDoS Protection
        #  BOT_MANAGE: Bot Management
        #  API_DEFEND: API Security
        #  WAF_DEFEND: WAF
        #  BLOCK: IP/Geo Block
        #  CUSTOMIZE_RULE: Custom Rules
        #  RATE_LIMIT: Rate Limiting
        #  INTELLIGENCE: Threat Intelligence', 'zh_CN':'命中拦截的策略类型，没有被拦截时为空。
        #  DMS_DEFEND：DDoS防护
        #  BOT_MANAGE：Bot管理
        #  API_DEFEND：API安全
        #  WAF_DEFEND：WAF
        #  BLOCK：IP/区域封禁
        #  CUSTOMIZE_RULE：自定义规则
        #  RATE_LIMIT：频率限制
        #  INTELLIGENCE：威胁情报'}
        self.block_policy_name = block_policy_name
        # {'en':'IP/Geo Block.', 'zh_CN':'IP区域封禁。'}
        self.block = block
        # {'en':'WAF.', 'zh_CN':'WAF。'}
        self.waf__defend = waf__defend
        # {'en':'DDoS Protection.', 'zh_CN':'DDos防护。'}
        self.dms__defend = dms__defend
        # {'en':'Bot Management.', 'zh_CN':'Bot管理。'}
        self.bot__manage = bot__manage
        # {'en':'API Security.', 'zh_CN':'API安全。'}
        self.api__defend = api__defend
        # {'en':'Threat Intelligence.', 'zh_CN':'威胁情报。'}
        self.intelligence = intelligence
        # {'en':'Rate Limiting.', 'zh_CN':'频率限制。'}
        self.rate__limit = rate__limit
        # {'en':'Custom Rules.', 'zh_CN':'自定义规则。'}
        self.customize__rule = customize__rule

    def validate(self):
        self.validate_required(self.block_policy_name, 'block_policy_name')
        self.validate_required(self.block, 'block')
        if self.block:
            self.block.validate()
        self.validate_required(self.waf__defend, 'waf__defend')
        if self.waf__defend:
            for k in self.waf__defend:
                if k:
                    k.validate()
        self.validate_required(self.dms__defend, 'dms__defend')
        if self.dms__defend:
            for k in self.dms__defend:
                if k:
                    k.validate()
        self.validate_required(self.bot__manage, 'bot__manage')
        if self.bot__manage:
            for k in self.bot__manage:
                if k:
                    k.validate()
        self.validate_required(self.api__defend, 'api__defend')
        if self.api__defend:
            for k in self.api__defend:
                if k:
                    k.validate()
        self.validate_required(self.intelligence, 'intelligence')
        if self.intelligence:
            for k in self.intelligence:
                if k:
                    k.validate()
        self.validate_required(self.rate__limit, 'rate__limit')
        if self.rate__limit:
            for k in self.rate__limit:
                if k:
                    k.validate()
        self.validate_required(self.customize__rule, 'customize__rule')
        if self.customize__rule:
            for k in self.customize__rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_policy_name is not None:
            result['blockPolicyName'] = self.block_policy_name
        if self.block is not None:
            result['BLOCK'] = self.block.to_map()
        if self.waf__defend is not None:
            result['WAF_DEFEND'] = []
            for k in self.waf__defend:
                result['WAF_DEFEND'].append(k.to_map() if k else None)
        if self.dms__defend is not None:
            result['DMS_DEFEND'] = []
            for k in self.dms__defend:
                result['DMS_DEFEND'].append(k.to_map() if k else None)
        if self.bot__manage is not None:
            result['BOT_MANAGE'] = []
            for k in self.bot__manage:
                result['BOT_MANAGE'].append(k.to_map() if k else None)
        if self.api__defend is not None:
            result['API_DEFEND'] = []
            for k in self.api__defend:
                result['API_DEFEND'].append(k.to_map() if k else None)
        if self.intelligence is not None:
            result['INTELLIGENCE'] = []
            for k in self.intelligence:
                result['INTELLIGENCE'].append(k.to_map() if k else None)
        if self.rate__limit is not None:
            result['RATE_LIMIT'] = []
            for k in self.rate__limit:
                result['RATE_LIMIT'].append(k.to_map() if k else None)
        if self.customize__rule is not None:
            result['CUSTOMIZE_RULE'] = []
            for k in self.customize__rule:
                result['CUSTOMIZE_RULE'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blockPolicyName') is not None:
            self.block_policy_name = m.get('blockPolicyName')
        if m.get('BLOCK') is not None:
            temp_model = QueryAttackLogDetailInfoAttackLogIpBlockDto()
            self.block = temp_model.from_map(m['BLOCK'])
        if m.get('WAF_DEFEND') is not None:
            self.waf__defend = []
            for k in m.get('WAF_DEFEND'):
                temp_model = QueryAttackLogDetailInfoAttackLogWafRuleDto()
                self.waf__defend.append(temp_model.from_map(k))
        if m.get('DMS_DEFEND') is not None:
            self.dms__defend = []
            for k in m.get('DMS_DEFEND'):
                temp_model = QueryAttackLogDetailInfoAttackLogDdosRuleDto()
                self.dms__defend.append(temp_model.from_map(k))
        if m.get('BOT_MANAGE') is not None:
            self.bot__manage = []
            for k in m.get('BOT_MANAGE'):
                temp_model = QueryAttackLogDetailInfoAttackLogBotRuleDto()
                self.bot__manage.append(temp_model.from_map(k))
        if m.get('API_DEFEND') is not None:
            self.api__defend = []
            for k in m.get('API_DEFEND'):
                temp_model = QueryAttackLogDetailInfoAttackLogApiRuleDto()
                self.api__defend.append(temp_model.from_map(k))
        if m.get('INTELLIGENCE') is not None:
            self.intelligence = []
            for k in m.get('INTELLIGENCE'):
                temp_model = QueryAttackLogDetailInfoAttackLogIntelligentDto()
                self.intelligence.append(temp_model.from_map(k))
        if m.get('RATE_LIMIT') is not None:
            self.rate__limit = []
            for k in m.get('RATE_LIMIT'):
                temp_model = QueryAttackLogDetailInfoAttackLogRateLimitDto()
                self.rate__limit.append(temp_model.from_map(k))
        if m.get('CUSTOMIZE_RULE') is not None:
            self.customize__rule = []
            for k in m.get('CUSTOMIZE_RULE'):
                temp_model = QueryAttackLogDetailInfoAttackLogCustomizeRuleDto()
                self.customize__rule.append(temp_model.from_map(k))
        return self


class QueryAttackLogDetailInfoAttackLogAllDetailDto(TeaModel):
    def __init__(
        self,
        basic_info: QueryAttackLogDetailInfoAttackLogBasicInfoDto = None,
        detail_info: QueryAttackLogDetailInfoAttackLogDetailDto = None,
    ):
        # {'en':'Basic Information.', 'zh_CN':'基础信息。'}
        self.basic_info = basic_info
        # {'en':'Details.', 'zh_CN':'详细信息。'}
        self.detail_info = detail_info

    def validate(self):
        self.validate_required(self.basic_info, 'basic_info')
        if self.basic_info:
            self.basic_info.validate()
        self.validate_required(self.detail_info, 'detail_info')
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()
        if self.detail_info is not None:
            result['detailInfo'] = self.detail_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicInfo') is not None:
            temp_model = QueryAttackLogDetailInfoAttackLogBasicInfoDto()
            self.basic_info = temp_model.from_map(m['basicInfo'])
        if m.get('detailInfo') is not None:
            temp_model = QueryAttackLogDetailInfoAttackLogDetailDto()
            self.detail_info = temp_model.from_map(m['detailInfo'])
        return self


class QueryAttackLogDetailInfoResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: QueryAttackLogDetailInfoAttackLogAllDetailDto = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
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
            temp_model = QueryAttackLogDetailInfoAttackLogAllDetailDto()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryAttackLogDetailInfoPaths(TeaModel):
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


class QueryAttackLogDetailInfoParameters(TeaModel):
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


class QueryAttackLogDetailInfoRequestHeader(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_type: str = None,
    ):
        # {'en':'The language of response data, default value: en.
        # zh_CN: Chinese
        # en: English', 'zh_CN':'返回内容的语言版本，默认值: en。
        # zh_CN：中文
        # en：英文'}
        self.language = language
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class QueryAttackLogDetailInfoResponseHeader(TeaModel):
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






class GetPrivacyStatusDistributionRequest(TeaModel):
    def __init__(
        self,
        api_groups: List[str] = None,
        api_ids: List[str] = None,
        domains: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        front_path: str = None,
    ):
        # {"en":"List of API group.", "zh_CN":"API分组列表。"}
        self.api_groups = api_groups
        # {"en":"List of API name.", "zh_CN":"API名称列表。"}
        self.api_ids = api_ids
        # {"en":"List of domain.", "zh_CN":"域名列表。"}
        self.domains = domains
        # {"en":"Start time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.start_time = start_time
        # {"en":"End time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.end_time = end_time
        # {"en":"Endpoint path.", "zh_CN":"前端路径。"}
        self.front_path = front_path

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_groups is not None:
            result['apiGroups'] = self.api_groups
        if self.api_ids is not None:
            result['apiIds'] = self.api_ids
        if self.domains is not None:
            result['domains'] = self.domains
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.front_path is not None:
            result['frontPath'] = self.front_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroups') is not None:
            self.api_groups = m.get('apiGroups')
        if m.get('apiIds') is not None:
            self.api_ids = m.get('apiIds')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('frontPath') is not None:
            self.front_path = m.get('frontPath')
        return self


class GetPrivacyStatusDistributionVo(TeaModel):
    def __init__(
        self,
        private_num: int = None,
        public_num: int = None,
    ):
        # {"en":"The number of private API.", "zh_CN":"私有API个数。"}
        self.private_num = private_num
        # {"en":"The number of public API.", "zh_CN":"公共API个数。"}
        self.public_num = public_num

    def validate(self):
        self.validate_required(self.private_num, 'private_num')
        self.validate_required(self.public_num, 'public_num')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_num is not None:
            result['privateNum'] = self.private_num
        if self.public_num is not None:
            result['publicNum'] = self.public_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privateNum') is not None:
            self.private_num = m.get('privateNum')
        if m.get('publicNum') is not None:
            self.public_num = m.get('publicNum')
        return self


class GetPrivacyStatusDistributionResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetPrivacyStatusDistributionVo = None,
    ):
        # {"en":"Return 200 means success.", "zh_CN":"200状态码表示请求成功。"}
        self.code = code
        # {"en":"Message.", "zh_CN":"返回信息。"}
        self.msg = msg
        # {"en":"Data", "zh_CN":"数据。"}
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
            temp_model = GetPrivacyStatusDistributionVo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPrivacyStatusDistributionPaths(TeaModel):
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


class GetPrivacyStatusDistributionParameters(TeaModel):
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


class GetPrivacyStatusDistributionRequestHeader(TeaModel):
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


class GetPrivacyStatusDistributionResponseHeader(TeaModel):
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




