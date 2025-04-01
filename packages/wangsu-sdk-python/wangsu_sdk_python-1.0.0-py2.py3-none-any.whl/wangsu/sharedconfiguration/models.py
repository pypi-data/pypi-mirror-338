# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ListSharedWhitelistRulesRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
    ):
        # {"en":"Rule name, fuzzy query.", "zh_CN":"规则名称，模糊查询。"}
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class ListSharedWhitelistRulesIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"IP/CIDR.", "zh_CN":"IP/IP段。"}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class ListSharedWhitelistRulesPathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # REGEX: Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：匹配正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"Path.", "zh_CN":"路径。"}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class ListSharedWhitelistRulesUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # REGEX: Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：匹配正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"URI.", "zh_CN":"URI。"}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class ListSharedWhitelistRulesUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # REGEX: Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：匹配正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"User agent.", "zh_CN":"User-Agent。"}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class ListSharedWhitelistRulesRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # REGEX: Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：匹配正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"Referer.", "zh_CN":"Referer。"}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.referer, 'referer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class ListSharedWhitelistRulesHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # REGEX: Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：匹配正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"Request header name.", "zh_CN":"头部名称。"}
        self.key = key
        # {"en":"List of request header values.", "zh_CN":"头部值列表。"}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class ListSharedWhitelistRulesWhitelistRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[ListSharedWhitelistRulesIpOrIpsCondition] = None,
        path_conditions: List[ListSharedWhitelistRulesPathCondition] = None,
        uri_conditions: List[ListSharedWhitelistRulesUriCondition] = None,
        ua_conditions: List[ListSharedWhitelistRulesUaCondition] = None,
        referer_conditions: List[ListSharedWhitelistRulesRefererCondition] = None,
        header_conditions: List[ListSharedWhitelistRulesHeaderCondition] = None,
    ):
        # {"en":"IP/CIDR match conditions.", "zh_CN":"IP/IP段匹配条件。"}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {"en":"Path match conditions.", "zh_CN":"路径匹配条件。"}
        self.path_conditions = path_conditions
        # {"en":"URI match conditions.", "zh_CN":"URI匹配条件。"}
        self.uri_conditions = uri_conditions
        # {"en":"User agent match conditions.", "zh_CN":"User-Agent 匹配条件。"}
        self.ua_conditions = ua_conditions
        # {"en":"Referer match conditions.", "zh_CN":"Referer 匹配条件。"}
        self.referer_conditions = referer_conditions
        # {"en":"Request header match conditions.", "zh_CN":"请求头匹配条件。"}
        self.header_conditions = header_conditions

    def validate(self):
        self.validate_required(self.ip_or_ips_conditions, 'ip_or_ips_conditions')
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        self.validate_required(self.path_conditions, 'path_conditions')
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        self.validate_required(self.uri_conditions, 'uri_conditions')
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ua_conditions, 'ua_conditions')
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        self.validate_required(self.referer_conditions, 'referer_conditions')
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        self.validate_required(self.header_conditions, 'header_conditions')
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = ListSharedWhitelistRulesIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = ListSharedWhitelistRulesPathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = ListSharedWhitelistRulesUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = ListSharedWhitelistRulesUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = ListSharedWhitelistRulesRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = ListSharedWhitelistRulesHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        return self


class ListSharedWhitelistRulesCommonShareWhitelistVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        rule_name: str = None,
        description: str = None,
        creator: str = None,
        imported_domain_count: int = None,
        imported_domain: List[str] = None,
        conditions: ListSharedWhitelistRulesWhitelistRuleCondition = None,
        create_time: str = None,
        update_time: str = None,
    ):
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.id = id
        # {"en":"Rule name.", "zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Description.", "zh_CN":"规则描述。"}
        self.description = description
        # {"en":"creator.", "zh_CN":"创建者。"}
        self.creator = creator
        # {"en":"Number of hostnames associated.", "zh_CN":"关联的域名数。"}
        self.imported_domain_count = imported_domain_count
        # {"en":"Associated hostname.", "zh_CN":"关联的域名。"}
        self.imported_domain = imported_domain
        # {"en":"Match conditions, At least one, at most five.", "zh_CN":"匹配条件，至少一个，至多五个。"}
        self.conditions = conditions
        # {"en":"Created date, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"创建时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.create_time = create_time
        # {"en":"Update date,format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"更新时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.imported_domain_count, 'imported_domain_count')
        self.validate_required(self.imported_domain, 'imported_domain')
        self.validate_required(self.conditions, 'conditions')
        if self.conditions:
            self.conditions.validate()
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.creator is not None:
            result['creator'] = self.creator
        if self.imported_domain_count is not None:
            result['importedDomainCount'] = self.imported_domain_count
        if self.imported_domain is not None:
            result['importedDomain'] = self.imported_domain
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('importedDomainCount') is not None:
            self.imported_domain_count = m.get('importedDomainCount')
        if m.get('importedDomain') is not None:
            self.imported_domain = m.get('importedDomain')
        if m.get('conditions') is not None:
            temp_model = ListSharedWhitelistRulesWhitelistRuleCondition()
            self.conditions = temp_model.from_map(m['conditions'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListSharedWhitelistRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListSharedWhitelistRulesCommonShareWhitelistVO] = None,
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
                temp_model = ListSharedWhitelistRulesCommonShareWhitelistVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListSharedWhitelistRulesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedWhitelistRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedWhitelistRulesRequestHeader(TeaModel):
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


class ListSharedWhitelistRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateShareCustomizeBotsRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享配置ID。","en":"Share configuration ID."}
        self.share_id = share_id
        # {"zh_CN":"待取消关联域名列表。","en":"List of hostname to be disassociated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class DisassociateShareCustomizeBotsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DisassociateShareCustomizeBotsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareCustomizeBotsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareCustomizeBotsRequestHeader(TeaModel):
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


class DisassociateShareCustomizeBotsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateSharedRateLimitingRuleRateLimitEffective(TeaModel):
    def __init__(
        self,
        effective: List[str] = None,
        start: str = None,
        end: str = None,
        timezone: str = None,
    ):
        # {'en':'Effective.
        # MON:Monday
        # TUE:Tuesday
        # WED:Wednesday
        # THU:Thursday
        # FRI:Friday
        # SAT:Saturday
        # SUN:Sunday', 'zh_CN':'周期。
        # MON：星期一
        # TUE：星期二
        # WED：星期三
        # THU：星期四
        # FRI：星期五
        # SAT：星期六
        # SUN：星期天'}
        self.effective = effective
        # {'en':'Start time, format: HH:mm.', 'zh_CN':'开始时间，格式：HH:mm。'}
        self.start = start
        # {'en':'End time, format: HH:mm.', 'zh_CN':'结束时间，格式：HH:mm。'}
        self.end = end
        # {'en':'Timezone,default value: GTM+8.', 'zh_CN':'时区，默认：GTM+8。','dictionary':'belong=WAAP-MS-Ext|dict=waap_timezone'}
        self.timezone = timezone

    def validate(self):
        self.validate_required(self.effective, 'effective')
        self.validate_required(self.start, 'start')
        self.validate_required(self.end, 'end')
        self.validate_required(self.timezone, 'timezone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective is not None:
            result['effective'] = self.effective
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effective') is not None:
            self.effective = m.get('effective')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class CreateSharedRateLimitingRuleIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'IP/CIDR, maximum 500 IP/CIDR.', 'zh_CN':'IP/IP段，最多500个IP/IP段。'}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class CreateSharedRateLimitingRulePathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, path case sensitive
        # NOT_EQUAL: Does not equal, path case sensitive
        # CONTAIN: Contains, path case insensitive
        # NOT_CONTAIN: Does not Contains, path case insensitive
        # REGEX: Regex match, path case insensitive
        # NOT_REGEX: Regular does not match, path case sensitive
        # START_WITH: Starts with, path case sensitive
        # END_WITH: Ends with, path case sensitive
        # WILDCARD: Wildcard matches, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character.
        # NOT_WILDCARD: Wildcard does not match, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character ", "zh_CN":"匹配类型。
        # EQUAL：等于，路径大小写敏感
        # NOT_EQUAL：不等于，路径大小写敏感
        # CONTAIN：包含，路径大小写不敏感
        # NOT_CONTAIN：不包含，路径大小写不敏感
        # REGEX：匹配正则，路径大小写不敏感
        # NOT_REGEX：正则不匹配，路径大小写不敏感
        # START_WITH：开头是，路径大小写不敏感
        # END_WITH：结尾是，路径大小写不敏感
        # WILDCARD：通配符匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Path.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, path needs to start with "/", and no parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html.', 'zh_CN':'路径。
        # 当匹配类型为等于/不等于/开头是/结尾是，路径必须以“/”开头，不含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html。'}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class CreateSharedRateLimitingRuleUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, URI case sensitive
        # NOT_EQUAL: Does not equal, URI case sensitive
        # CONTAIN: Contains, URI case insensitive
        # NOT_CONTAIN: Does not Contains, URI case insensitive
        # REGEX: Regex match, URI case insensitive
        # NOT_REGEX: Regular does not match, URI case insensitive
        # START_WITH: Starts with, URI case insensitive
        # END_WITH: Ends with, URI case insensitive
        # WILDCARD: Wildcard matches, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，URI大小写敏感
        # NOT_EQUAL：不等于，URI大小写敏感
        # CONTAIN：包含，URI大小写不敏感
        # NOT_CONTAIN：不包含，URI大小写不敏感
        # REGEX：匹配正则，URI大小写不敏感
        # NOT_REGEX：正则不匹配，URI大小写不敏感
        # START_WITH：开头是，URI大小写不敏感
        # END_WITH：结尾是，URI大小写不敏感
        # WILDCARD：通配符匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'URI.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, uri needs to start with "/", and includes parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html?id=1.', 'zh_CN':'URI。
        # 当匹配类型为等于/不等于/开头是/结尾是，URI必须以”/“开头，含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html?id=1。'}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class CreateSharedRateLimitingRuleUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, user agent case sensitive
        # NOT_EQUAL: Does not equal, user agent case sensitive
        # CONTAIN: Contains, user agent case insensitive
        # NOT_CONTAIN: Does not Contains, user agent case insensitive
        # NONE:Empty or non-existent
        # REGEX: Regex match, user agent case insensitive
        # NOT_REGEX: Regular does not match, user agent case insensitive
        # START_WITH: Starts with, user agent case insensitive
        # END_WITH: Ends with, user agent case insensitive
        # WILDCARD: Wildcard matches, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，User-Agent大小写敏感
        # NOT_EQUAL：不等于，User-Agent大小写敏感
        # CONTAIN：包含，User-Agent大小写不敏感
        # NOT_CONTAIN：不包含，User-Agent大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，User-Agent大小写不敏感
        # NOT_REGEX：正则不匹配，User-Agent大小写不敏感
        # START_WITH：开头是，User-Agent大小写不敏感
        # END_WITH：结尾是，User-Agent大小写不敏感
        # WILDCARD：通配符匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'User agent.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: go-Http-client/1.1.', 'zh_CN':'User-Agent。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：go-Http-client/1.1。'}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class CreateSharedRateLimitingRuleRequestMethodCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        request_method: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Request method.
        # Supported values: GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY.', 'zh_CN':'请求方法。
        # 支持的值：GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY。'}
        self.request_method = request_method

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.request_method, 'request_method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        return self


class CreateSharedRateLimitingRuleRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, referer case sensitive
        # NOT_EQUAL: Does not equal, referer case sensitive
        # CONTAIN: Contains, referer case insensitive
        # NOT_CONTAIN: Does not Contains, referer case insensitive
        # NONE:Empty or non-existent
        # REGEX: Regex match, referer case insensitive
        # NOT_REGEX: Regular does not match, referer case insensitive
        # START_WITH: Starts with, referer case insensitive
        # END_WITH: Ends with, referer case insensitive
        # WILDCARD: Wildcard matches, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single characte
        # NOT_WILDCARD: Wildcard does not match, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，referer大小写敏感
        # NOT_EQUAL：不等于，referer大小写敏感
        # CONTAIN：包含，referer大小写不敏感
        # NOT_CONTAIN：不包含，referer大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，referer大小写不敏感
        # NOT_REGEX：正则不匹配，referer大小写不敏感
        # START_WITH：开头是，referer大小写不敏感
        # END_WITH：结尾是，referer大小写不敏感
        # WILDCARD：通配符匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Referer.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: http://test.com.', 'zh_CN':'Referer。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：http://test.com。'}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.referer, 'referer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class CreateSharedRateLimitingRuleHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, request header values case sensitive
        # NOT_EQUAL: Does not equal, request header values case sensitive
        # CONTAIN: Contains, request header values case insensitive
        # NOT_CONTAIN: Does not Contains, request header values case insensitive
        # NONE: Empty or non-existent
        # REGEX: Regex match, request header values case insensitive
        # NOT_REGEX: Regular does not match, request header values case insensitive
        # START_WITH: Starts with, request header values case insensitive
        # END_WITH: Ends with, request header values case insensitive
        # WILDCARD: Wildcard matches, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，头部值大小写敏感
        # NOT_EQUAL：不等于，头部值大小写敏感
        # CONTAIN：包含，头部值大小写不敏感
        # NOT_CONTAIN：不包含，头部值大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，头部值大小写不敏感
        # NOT_REGEX：正则不匹配，头部值大小写不敏感
        # START_WITH：开头是，头部值大小写不敏感
        # END_WITH：结尾是，头部值大小写不敏感
        # WILDCARD：通配符匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Header name,case insensitive,up to 100 characters.
        # Example: Accept.', 'zh_CN':'头部名称，大小写不敏感，最多100个字符。
        # 示例：Accept。'}
        self.key = key
        # {'en':'Header value.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed.', 'zh_CN':'头部值。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。'}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class CreateSharedRateLimitingRuleAreaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        areas: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Geo.', 'zh_CN':'区域。','dictionary':'belong=WAAP-MS-Ext|dict=waap_areaCityAndCountry'}
        self.areas = areas

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.areas, 'areas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.areas is not None:
            result['areas'] = self.areas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('areas') is not None:
            self.areas = m.get('areas')
        return self


class CreateSharedRateLimitingRuleStatusCodeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        status_code: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Response Code.', 'zh_CN':'状态码。'}
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateSharedRateLimitingRuleSchemeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        scheme: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'HTTP/S.
        # Supported values: HTTP/HTTPS.', 'zh_CN':'应用层协议。
        # 支持的值：HTTP/HTTPS。'}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.scheme, 'scheme')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class CreateSharedRateLimitingRuleShareRateLimitRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[CreateSharedRateLimitingRuleIpOrIpsCondition] = None,
        path_conditions: List[CreateSharedRateLimitingRulePathCondition] = None,
        uri_conditions: List[CreateSharedRateLimitingRuleUriCondition] = None,
        ua_conditions: List[CreateSharedRateLimitingRuleUaCondition] = None,
        method_conditions: List[CreateSharedRateLimitingRuleRequestMethodCondition] = None,
        referer_conditions: List[CreateSharedRateLimitingRuleRefererCondition] = None,
        header_conditions: List[CreateSharedRateLimitingRuleHeaderCondition] = None,
        area_conditions: List[CreateSharedRateLimitingRuleAreaCondition] = None,
        status_code_conditions: List[CreateSharedRateLimitingRuleStatusCodeCondition] = None,
        scheme_conditions: List[CreateSharedRateLimitingRuleSchemeCondition] = None,
    ):
        # {'en':'IP/CIDR, match type cannot be repeated.', 'zh_CN':'IP/IP段，匹配类型不可重复。'}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {'en':'Path, match type cannot be repeated.
        # When the business scenario is API, this matching condition is not supported.', 'zh_CN':'路径，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.path_conditions = path_conditions
        # {'en':'URI, match type cannot be repeated.
        # 
        # When the business scenario is API, this matching condition is not supported.', 'zh_CN':'URI，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.uri_conditions = uri_conditions
        # {'en':'User Agent, match type cannot be repeated.', 'zh_CN':'User-Agent，匹配类型不可重复。'}
        self.ua_conditions = ua_conditions
        # {'en':'Request Method.
        # When the business scenario is API,this matching condition is not supported.', 'zh_CN':'请求方法，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.method_conditions = method_conditions
        # {'en':'Referer, match type cannot be repeated.', 'zh_CN':'Referer，匹配类型不可重复。'}
        self.referer_conditions = referer_conditions
        # {'en':'Request Header, match type can be repeated.', 'zh_CN':'请求头，匹配类型可重复。'}
        self.header_conditions = header_conditions
        # {'en':'Geo,match type cannot be repeated.', 'zh_CN':'区域，匹配类型不可重复。'}
        self.area_conditions = area_conditions
        # {'en':'Response Code, match type cannot be repeated.', 'zh_CN':'状态码，匹配类型不可重复。'}
        self.status_code_conditions = status_code_conditions
        # {'en':'HTTP/S, match type cannot be repeated.', 'zh_CN':'应用层协议，匹配类型不可重复。'}
        self.scheme_conditions = scheme_conditions

    def validate(self):
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        if self.method_conditions:
            for k in self.method_conditions:
                if k:
                    k.validate()
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()
        if self.area_conditions:
            for k in self.area_conditions:
                if k:
                    k.validate()
        if self.status_code_conditions:
            for k in self.status_code_conditions:
                if k:
                    k.validate()
        if self.scheme_conditions:
            for k in self.scheme_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.method_conditions is not None:
            result['methodConditions'] = []
            for k in self.method_conditions:
                result['methodConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        if self.area_conditions is not None:
            result['areaConditions'] = []
            for k in self.area_conditions:
                result['areaConditions'].append(k.to_map() if k else None)
        if self.status_code_conditions is not None:
            result['statusCodeConditions'] = []
            for k in self.status_code_conditions:
                result['statusCodeConditions'].append(k.to_map() if k else None)
        if self.scheme_conditions is not None:
            result['schemeConditions'] = []
            for k in self.scheme_conditions:
                result['schemeConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = CreateSharedRateLimitingRuleIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = CreateSharedRateLimitingRulePathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = CreateSharedRateLimitingRuleUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = CreateSharedRateLimitingRuleUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('methodConditions') is not None:
            self.method_conditions = []
            for k in m.get('methodConditions'):
                temp_model = CreateSharedRateLimitingRuleRequestMethodCondition()
                self.method_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = CreateSharedRateLimitingRuleRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = CreateSharedRateLimitingRuleHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        if m.get('areaConditions') is not None:
            self.area_conditions = []
            for k in m.get('areaConditions'):
                temp_model = CreateSharedRateLimitingRuleAreaCondition()
                self.area_conditions.append(temp_model.from_map(k))
        if m.get('statusCodeConditions') is not None:
            self.status_code_conditions = []
            for k in m.get('statusCodeConditions'):
                temp_model = CreateSharedRateLimitingRuleStatusCodeCondition()
                self.status_code_conditions.append(temp_model.from_map(k))
        if m.get('schemeConditions') is not None:
            self.scheme_conditions = []
            for k in m.get('schemeConditions'):
                temp_model = CreateSharedRateLimitingRuleSchemeCondition()
                self.scheme_conditions.append(temp_model.from_map(k))
        return self


class CreateSharedRateLimitingRuleRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        description: str = None,
        statistical_item: str = None,
        statistics_key: str = None,
        statistical_period: int = None,
        trigger_threshold: int = None,
        intercept_time: int = None,
        effective_status: str = None,
        rate_limit_effective: CreateSharedRateLimitingRuleRateLimitEffective = None,
        action: str = None,
        rate_limit_rule_condition: CreateSharedRateLimitingRuleShareRateLimitRuleCondition = None,
    ):
        # {'en':'Rule Name, maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'规则名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.rule_name = rule_name
        # {'en':'Description, maximum 200 characters.', 'zh_CN':'规则描述，最多200个字符。'}
        self.description = description
        # {'en':'Client identifier.
        # IP:Client IP
        # IP_UA:Client IP and User-Agent
        # COOKIE:Cookie
        # IP_COOKIE:Client IP and Cookie
        # HEADER:Request Header
        # When there is a status code in the matching condition,this client identifier is not supported.
        # IP_HEADER:Client IP and Request Header
        # When there is a status code in the matching condition,this client identifier is not supported .', 'zh_CN':'统计粒度。
        # IP：客户端IP
        # IP_UA：客户端IP和User-Agent
        # COOKIE：Cookie
        # IP_COOKIE：客户端IP和Cookie
        # HEADER：请求头，当匹配条件中存在状态码时不支持此统计粒度
        # IP_HEADER：客户端IP和请求头，当匹配条件中存在状态码时不支持此统计粒度'}
        self.statistical_item = statistical_item
        # {'en':'Statistical key value.
        # When the client identifier is cookie/header value, the corresponding key value needs to be entered.', 'zh_CN':'统计key值。
        # 当统计粒度cookie/header值，需要输入对应的key值。'}
        self.statistics_key = statistics_key
        # {'en':'Statistics period, unit: seconds, the range is 1 - 3600.', 'zh_CN':'统计周期，单位：秒，范围为 1 - 3600。'}
        self.statistical_period = statistical_period
        # {'en':'Trigger threshold, unit: times.', 'zh_CN':'触发阈值，单位：次。'}
        self.trigger_threshold = trigger_threshold
        # {'en':'Action duration, unit: seconds, the range is 10 - 604800.', 'zh_CN':'处理动作持续时间，单位：秒，范围为 10 - 604800。'}
        self.intercept_time = intercept_time
        # {'en':'Cycle effective status.
        # PERMANENT:All time
        # WITHOUT:Excluded time
        # WITHIN:Selected time', 'zh_CN':'周期生效状态。
        # PERMANENT：永久生效
        # WITHOUT：周期内不生效
        # WITHIN：周期内生效'}
        self.effective_status = effective_status
        # {'en':'Effective time period.
        # When the effective status is effective within the cycle or not effective within the cycle, this field must have a value.', 'zh_CN':'规则生效周期。
        # 生效状态为周期内生效或周期内不生效时，此字段必须有值。'}
        self.rate_limit_effective = rate_limit_effective
        # {'en':'Action.
        # NO_USE:Not Used
        # LOG:Log
        # COOKIE:Cookie verification
        # JS_CHECK:Javascript verification
        # DELAY:Delay
        # BLOCK:Deny
        # RESET:Reset Connection
        # Custom response ID:Custom response ID
        # When there is a status code in the matching condition, the supported actions are Log, Deny, and Reset Connection.', 'zh_CN':'处理动作。
        # NO_USE：不使用
        # LOG：监控
        # COOKIE：Cookie校验
        # JS_CHECK：JavaScript校验
        # DELAY：延迟响应
        # BLOCK：拦截
        # RESET：断开连接
        # 自定义响应ID：自定义响应ID
        # 当匹配条件中存在状态码时，支持处理动作为监控、拦截、断开连接。'}
        self.action = action
        # {'en':'Matching conditions.', 'zh_CN':'匹配条件。'}
        self.rate_limit_rule_condition = rate_limit_rule_condition

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.statistical_item, 'statistical_item')
        self.validate_required(self.statistical_period, 'statistical_period')
        self.validate_required(self.trigger_threshold, 'trigger_threshold')
        self.validate_required(self.intercept_time, 'intercept_time')
        self.validate_required(self.effective_status, 'effective_status')
        if self.rate_limit_effective:
            self.rate_limit_effective.validate()
        self.validate_required(self.action, 'action')
        self.validate_required(self.rate_limit_rule_condition, 'rate_limit_rule_condition')
        if self.rate_limit_rule_condition:
            self.rate_limit_rule_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.statistical_item is not None:
            result['statisticalItem'] = self.statistical_item
        if self.statistics_key is not None:
            result['statisticsKey'] = self.statistics_key
        if self.statistical_period is not None:
            result['statisticalPeriod'] = self.statistical_period
        if self.trigger_threshold is not None:
            result['triggerThreshold'] = self.trigger_threshold
        if self.intercept_time is not None:
            result['interceptTime'] = self.intercept_time
        if self.effective_status is not None:
            result['effectiveStatus'] = self.effective_status
        if self.rate_limit_effective is not None:
            result['rateLimitEffective'] = self.rate_limit_effective.to_map()
        if self.action is not None:
            result['action'] = self.action
        if self.rate_limit_rule_condition is not None:
            result['rateLimitRuleCondition'] = self.rate_limit_rule_condition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statisticalItem') is not None:
            self.statistical_item = m.get('statisticalItem')
        if m.get('statisticsKey') is not None:
            self.statistics_key = m.get('statisticsKey')
        if m.get('statisticalPeriod') is not None:
            self.statistical_period = m.get('statisticalPeriod')
        if m.get('triggerThreshold') is not None:
            self.trigger_threshold = m.get('triggerThreshold')
        if m.get('interceptTime') is not None:
            self.intercept_time = m.get('interceptTime')
        if m.get('effectiveStatus') is not None:
            self.effective_status = m.get('effectiveStatus')
        if m.get('rateLimitEffective') is not None:
            temp_model = CreateSharedRateLimitingRuleRateLimitEffective()
            self.rate_limit_effective = temp_model.from_map(m['rateLimitEffective'])
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('rateLimitRuleCondition') is not None:
            temp_model = CreateSharedRateLimitingRuleShareRateLimitRuleCondition()
            self.rate_limit_rule_condition = temp_model.from_map(m['rateLimitRuleCondition'])
        return self


class CreateSharedRateLimitingRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateSharedRateLimitingRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedRateLimitingRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedRateLimitingRuleRequestHeader(TeaModel):
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


class CreateSharedRateLimitingRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateShareCustomizeRuleRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待取消关联域名列表。","en":"List of hostname to be disassociated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class DisassociateShareCustomizeRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DisassociateShareCustomizeRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareCustomizeRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareCustomizeRuleRequestHeader(TeaModel):
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


class DisassociateShareCustomizeRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListCustomActionsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListCustomActionsCommonShareCustomizeActionVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        main_account: str = None,
        creator: str = None,
        action_name: str = None,
        description: str = None,
        status_code: str = None,
        content_type: str = None,
        cus_block_cnt: str = None,
        domain_list: str = None,
    ):
        # {'en':'Custom response ID.', 'zh_CN':'自定义响应ID。'}
        self.id = id
        # {'en':'Main account.', 'zh_CN':'主账号。'}
        self.main_account = main_account
        # {'en':'Creator.', 'zh_CN':'创建者。'}
        self.creator = creator
        # {'en':'Action name,maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'动作名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.action_name = action_name
        # {'en':'Description,maximum 200 characters.', 'zh_CN':'描述，最多200个字符。'}
        self.description = description
        # {'en':'Status code.
        # Valid value range:200,204,206,400,401,403,404,500,501,503.', 'zh_CN':'状态码。
        # 有效值范围：200，204，206，400，401，403，404，500，501，503。'}
        self.status_code = status_code
        # {'en':'Response Content-Type type,multiple separated by ; sign.', 'zh_CN':'响应Content-Type类型，多个以 ; 隔开。'}
        self.content_type = content_type
        # {'en':'Response content definition, the size of the response content cannot exceed 16KB, if you need to insert static resources such as pictures, it is recommended to use links to import. The following interception information parameters are supported: 
        #  {url}} : Displays the URL information when intercepting 
        #  {client_ip}} : Displays the intercepted user IP information 
        #  {time}} : Displays the intercepted time point 
        #  {event_id} : Displays the ID information of this interception event', 'zh_CN':'自定义响应内容定义，响应内容大小不能超过16KB，如需插入图片等静态资源，建议采用链接引入。
        # 支持引用下列拦截信息参数：
        # {url} ：显示拦截时的URL信息
        # {client_ip} ：显示被拦截的用户IP信息
        # {time} ：显示被拦截的时间点
        # {event_id} ：显示本次拦截事件的ID信息'}
        self.cus_block_cnt = cus_block_cnt
        # {"zh_CN":"关联域名列表。","en":"List of associated hostnames."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.main_account, 'main_account')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.action_name, 'action_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.cus_block_cnt, 'cus_block_cnt')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.main_account is not None:
            result['mainAccount'] = self.main_account
        if self.creator is not None:
            result['creator'] = self.creator
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.description is not None:
            result['description'] = self.description
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.cus_block_cnt is not None:
            result['cusBlockCnt'] = self.cus_block_cnt
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mainAccount') is not None:
            self.main_account = m.get('mainAccount')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('cusBlockCnt') is not None:
            self.cus_block_cnt = m.get('cusBlockCnt')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class ListCustomActionsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListCustomActionsCommonShareCustomizeActionVO] = None,
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
                temp_model = ListCustomActionsCommonShareCustomizeActionVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListCustomActionsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListCustomActionsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListCustomActionsRequestHeader(TeaModel):
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


class ListCustomActionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateDmsShareServiceFeatureRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        dis_ass_domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享配置ID。","en":"Share configuration ID."}
        self.share_id = share_id
        # {"zh_CN":"待解除关联域名列表。","en":"List of hostname to be disassociated."}
        self.dis_ass_domain_list = dis_ass_domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.dis_ass_domain_list, 'dis_ass_domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.dis_ass_domain_list is not None:
            result['disAssDomainList'] = self.dis_ass_domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('disAssDomainList') is not None:
            self.dis_ass_domain_list = m.get('disAssDomainList')
        return self


class DisassociateDmsShareServiceFeatureResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DisassociateDmsShareServiceFeaturePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateDmsShareServiceFeatureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateDmsShareServiceFeatureRequestHeader(TeaModel):
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


class DisassociateDmsShareServiceFeatureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateShareRateLimitRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待关联域名列表。","en":"List of hostname to be associated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class AssociateShareRateLimitResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AssociateShareRateLimitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareRateLimitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareRateLimitRequestHeader(TeaModel):
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


class AssociateShareRateLimitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateDmsShareServiceFeatureRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        ass_domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享配置ID。","en":"Share configuration ID."}
        self.share_id = share_id
        # {"zh_CN":"待关联域名列表。","en":"List of hostname to be associated."}
        self.ass_domain_list = ass_domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.ass_domain_list, 'ass_domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.ass_domain_list is not None:
            result['assDomainList'] = self.ass_domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('assDomainList') is not None:
            self.ass_domain_list = m.get('assDomainList')
        return self


class AssociateDmsShareServiceFeatureResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AssociateDmsShareServiceFeaturePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateDmsShareServiceFeatureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateDmsShareServiceFeatureRequestHeader(TeaModel):
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


class AssociateDmsShareServiceFeatureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateSharedWhitelistRuleRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待关联域名列表。","en":"List of hostname to be associated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class AssociateSharedWhitelistRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AssociateSharedWhitelistRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateSharedWhitelistRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateSharedWhitelistRuleRequestHeader(TeaModel):
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


class AssociateSharedWhitelistRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateSharedWAFRuleExceptionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        msg: str = None,
        type: str = None,
        match_type: str = None,
        content_list: List[str] = None,
    ):
        # {'en':'Exception name,maximum 50 character.
        # Does not support special characters and spaces.', 'zh_CN':'例外名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.name = name
        # {'en':'Exception description,maximum 200 characters.', 'zh_CN':'例外描述，最多200个字符。'}
        self.msg = msg
        # {'en':'Matching conditions.
        # ip: IP
        # path: Path
        # uri: URI
        # urlParamName: URI Parameter Name
        # urlParamValue: URI Parameter Value
        # userAgent: User Agent
        # httpHeaderName: Request Header Name
        # httpHeaderValue: Request Header Value
        # cookie: Cookie
        # body: Body
        # bodyParamName: Body Parameter Name
        # bodyParamValue: Body Parameter Value', 'zh_CN':'匹配条件。
        # ip：IP
        # path：路径
        # uri：URI
        # urlParamName：URI参数名
        # urlParamValue：URI参数值
        # userAgent：User Agent
        # httpHeaderName：请求头部名称
        # httpHeaderValue：请求头部值
        # cookie：Cookie
        # body：Body
        # bodyParamName：Body参数名
        # bodyParamValue：Body参数值'}
        self.type = type
        # {'en':'Match type,IP can only be EQUAL.
        # EQUAL: Equal
        # CONTAIN: Contains
        # REGEX: Regular match', 'zh_CN':'匹配类型，IP只能是等于。
        # EQUAL：等于
        # CONTAIN：包含
        # REGEX：正则匹配'}
        self.match_type = match_type
        # {'en':'Rule exceptions.
        # When matchType=EQUAL, case-sensitive, path and uri must start with "/", and body can only pass one value;
        # When matchType=REGEX, only one value can be passed', 'zh_CN':'规则例外内容。
        # matchType=EQUAL时，大小写敏感，path和uri必须以"/"开头，body只能传一个值；
        # matchType=REGEX时，只能传一个值。'}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.content_list, 'content_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.msg is not None:
            result['msg'] = self.msg
        if self.type is not None:
            result['type'] = self.type
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.content_list is not None:
            result['contentList'] = self.content_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('contentList') is not None:
            self.content_list = m.get('contentList')
        return self


class CreateSharedWAFRuleExceptionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Rule exception ID.', 'zh_CN':'规则例外ID。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateSharedWAFRuleExceptionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedWAFRuleExceptionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedWAFRuleExceptionRequestHeader(TeaModel):
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


class CreateSharedWAFRuleExceptionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListSharedCustomRulesRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
    ):
        # {"en":"Rule name, fuzzy query.","zh_CN":"规则名称，模糊查询。"}
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class ListSharedCustomRulesRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。"}
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


class ListSharedCustomRulesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedCustomRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedCustomRulesResponseDataConditionMethodConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        request_method: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"Request method.
        # Supported values: GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY.","zh_CN":"请求方法。
        # 支持的值：GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY"}
        self.request_method = request_method

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.request_method, 'request_method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        return self


class ListSharedCustomRulesResponseDataConditionJa3Conditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ja_3list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal","zh_CN":"匹配类型。
        # EQUAL：等于 
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"JA3 Fingerprint List.","zh_CN":"JA3指纹列表。"}
        self.ja_3list = ja_3list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ja_3list, 'ja_3list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ja_3list is not None:
            result['ja3List'] = self.ja_3list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ja3List') is not None:
            self.ja_3list = m.get('ja3List')
        return self


class ListSharedCustomRulesResponseDataConditionAreaConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        areas: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"Geo.","zh_CN":"区域。"}
        self.areas = areas

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.areas, 'areas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.areas is not None:
            result['areas'] = self.areas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('areas') is not None:
            self.areas = m.get('areas')
        return self


class ListSharedCustomRulesResponseDataConditionIpOrIpsConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"IP/CIDR.","zh_CN":"IP/IP段。"}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class ListSharedCustomRulesResponseDataConditionUriConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: equal to
        # NOT_EQUAL: not equal to
        # CONTAIN: contains
        # NOT_CONTAIN: does not contain
        # REGEX: regular
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"URI.","zh_CN":"URI。"}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class ListSharedCustomRulesResponseDataConditionPathConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: equal to
        # NOT_EQUAL: not equal to
        # CONTAIN: contains
        # NOT_CONTAIN: does not contain
        # REGEX: regular
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"Path.","zh_CN":"路径。"}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class ListSharedCustomRulesResponseDataConditionUaConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: equal to
        # NOT_EQUAL: not equal to
        # CONTAIN: contains
        # NOT_CONTAIN: does not contain
        # REGEX: regular
        # NONE: empty or does not exist
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"User-Agent.","zh_CN":"User-Agent。"}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class ListSharedCustomRulesResponseDataConditionHeaderConditions(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        value_list: List[str] = None,
        key: str = None,
    ):
        # {"en":"Match type.
        # EQUAL: equal to
        # NOT_EQUAL: not equal to
        # CONTAIN: contains
        # NOT_CONTAIN: does not contain
        # REGEX: regular
        # NONE: empty or does not exist
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type
        # {"en":"Header value.","zh_CN":"头部值。"}
        self.value_list = value_list
        # {"en":"Request header name.","zh_CN":"头部名称。"}
        self.key = key

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.value_list, 'value_list')
        self.validate_required(self.key, 'key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.value_list is not None:
            result['valueList'] = self.value_list
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListSharedCustomRulesResponseDataConditionRefererConditions(TeaModel):
    def __init__(
        self,
        referer: List[str] = None,
        match_type: str = None,
    ):
        # {"en":"Referer.","zh_CN":"Referer。"}
        self.referer = referer
        # {"en":"Match type.
        # EQUAL: equal to
        # NOT_EQUAL: not equal to
        # CONTAIN: contains
        # NOT_CONTAIN: does not contain
        # REGEX: regular
        # NONE: empty or does not exist
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配"}
        self.match_type = match_type

    def validate(self):
        self.validate_required(self.referer, 'referer')
        self.validate_required(self.match_type, 'match_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.referer is not None:
            result['referer'] = self.referer
        if self.match_type is not None:
            result['matchType'] = self.match_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        return self


class ListSharedCustomRulesResponseDataConditionJa4Conditions(TeaModel):
    def __init__(
        self,
        ja_4list: List[str] = None,
        match_type: str = None,
    ):
        # {"en":"JA4 Fingerprint List.","zh_CN":"JA4指纹列表。"}
        self.ja_4list = ja_4list
        # {"en":"Match type. 
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal
        # CONTAIN: Contains
        # NOT_CONTAIN: Does not Contains
        # START_WITH: Starts with
        # END_WITH: Ends with
        # WILDCARD: Wildcard matches, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, ** represents zero or more arbitrary characters, ? represents any single character","zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type

    def validate(self):
        self.validate_required(self.ja_4list, 'ja_4list')
        self.validate_required(self.match_type, 'match_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ja_4list is not None:
            result['ja4List'] = self.ja_4list
        if self.match_type is not None:
            result['matchType'] = self.match_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ja4List') is not None:
            self.ja_4list = m.get('ja4List')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        return self


class ListSharedCustomRulesResponseDataCondition(TeaModel):
    def __init__(
        self,
        method_conditions: List[ListSharedCustomRulesResponseDataConditionMethodConditions] = None,
        ja_3conditions: List[ListSharedCustomRulesResponseDataConditionJa3Conditions] = None,
        area_conditions: List[ListSharedCustomRulesResponseDataConditionAreaConditions] = None,
        ip_or_ips_conditions: List[ListSharedCustomRulesResponseDataConditionIpOrIpsConditions] = None,
        uri_conditions: List[ListSharedCustomRulesResponseDataConditionUriConditions] = None,
        path_conditions: List[ListSharedCustomRulesResponseDataConditionPathConditions] = None,
        ua_conditions: List[ListSharedCustomRulesResponseDataConditionUaConditions] = None,
        header_conditions: List[ListSharedCustomRulesResponseDataConditionHeaderConditions] = None,
        referer_conditions: List[ListSharedCustomRulesResponseDataConditionRefererConditions] = None,
        ja_4conditions: List[ListSharedCustomRulesResponseDataConditionJa4Conditions] = None,
    ):
        # {"en":"Request Method.","zh_CN":"请求方法。"}
        self.method_conditions = method_conditions
        # {"en":"JA3 Fingerprint, match type cannot be repeated.","zh_CN":"JA3指纹，匹配类型不可重复。"}
        self.ja_3conditions = ja_3conditions
        # {"en":"Geo.","zh_CN":"区域。"}
        self.area_conditions = area_conditions
        # {"en":"IP/CIDR.","zh_CN":"IP/IP段。"}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {"en":"URI.","zh_CN":"URI。"}
        self.uri_conditions = uri_conditions
        # {"en":"Path.","zh_CN":"路径。"}
        self.path_conditions = path_conditions
        # {"en":"User Agent.","zh_CN":"User-Agent。"}
        self.ua_conditions = ua_conditions
        # {"en":"Request Header.","zh_CN":"请求头。"}
        self.header_conditions = header_conditions
        # {"en":"Referer.","zh_CN":"Referer。"}
        self.referer_conditions = referer_conditions
        # {"en":"JA4 Fingerprint, match type cannot be repeated.","zh_CN":"JA4指纹，匹配类型不可重复。"}
        self.ja_4conditions = ja_4conditions

    def validate(self):
        self.validate_required(self.method_conditions, 'method_conditions')
        if self.method_conditions:
            for k in self.method_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ja_3conditions, 'ja_3conditions')
        if self.ja_3conditions:
            for k in self.ja_3conditions:
                if k:
                    k.validate()
        self.validate_required(self.area_conditions, 'area_conditions')
        if self.area_conditions:
            for k in self.area_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ip_or_ips_conditions, 'ip_or_ips_conditions')
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        self.validate_required(self.uri_conditions, 'uri_conditions')
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        self.validate_required(self.path_conditions, 'path_conditions')
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ua_conditions, 'ua_conditions')
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        self.validate_required(self.header_conditions, 'header_conditions')
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()
        self.validate_required(self.referer_conditions, 'referer_conditions')
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ja_4conditions, 'ja_4conditions')
        if self.ja_4conditions:
            for k in self.ja_4conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_conditions is not None:
            result['methodConditions'] = []
            for k in self.method_conditions:
                result['methodConditions'].append(k.to_map() if k else None)
        if self.ja_3conditions is not None:
            result['ja3Conditions'] = []
            for k in self.ja_3conditions:
                result['ja3Conditions'].append(k.to_map() if k else None)
        if self.area_conditions is not None:
            result['areaConditions'] = []
            for k in self.area_conditions:
                result['areaConditions'].append(k.to_map() if k else None)
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.ja_4conditions is not None:
            result['ja4Conditions'] = []
            for k in self.ja_4conditions:
                result['ja4Conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('methodConditions') is not None:
            self.method_conditions = []
            for k in m.get('methodConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionMethodConditions()
                self.method_conditions.append(temp_model.from_map(k))
        if m.get('ja3Conditions') is not None:
            self.ja_3conditions = []
            for k in m.get('ja3Conditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionJa3Conditions()
                self.ja_3conditions.append(temp_model.from_map(k))
        if m.get('areaConditions') is not None:
            self.area_conditions = []
            for k in m.get('areaConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionAreaConditions()
                self.area_conditions.append(temp_model.from_map(k))
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionIpOrIpsConditions()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionUriConditions()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionPathConditions()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionUaConditions()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionHeaderConditions()
                self.header_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionRefererConditions()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('ja4Conditions') is not None:
            self.ja_4conditions = []
            for k in m.get('ja4Conditions'):
                temp_model = ListSharedCustomRulesResponseDataConditionJa4Conditions()
                self.ja_4conditions.append(temp_model.from_map(k))
        return self


class ListSharedCustomRulesResponseData(TeaModel):
    def __init__(
        self,
        condition: ListSharedCustomRulesResponseDataCondition = None,
        creator: str = None,
        act: str = None,
        create_time: str = None,
        relation_domain_count: int = None,
        rule_name: str = None,
        description: str = None,
        update_time: str = None,
        id: str = None,
    ):
        # {"en":"Matching conditions.","zh_CN":"匹配条件。"}
        self.condition = condition
        # {"en":"Creator.","zh_CN":"创建者。"}
        self.creator = creator
        # {"en":"Action.
        # NO_USE: Not Used
        # LOG: Log
        # DELAY: Delay
        # BLOCK: Deny
        # RESET: Reset Connection","zh_CN":"处理动作。
        # NO_USE：不使用
        # LOG：监控
        # DELAY：延迟响应
        # BLOCK：拦截
        # RESET：断开连接"}
        self.act = act
        # {"en":"Create time, format: yyyy-MM-dd HH:mm:ss.","zh_CN":"创建时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.create_time = create_time
        # {"en":"Number of associated hostnames.","zh_CN":"关联域名数。"}
        self.relation_domain_count = relation_domain_count
        # {"en":"Rule Name.","zh_CN":"规则名称。"}
        self.rule_name = rule_name
        # {"en":"Description.","zh_CN":"规则描述。"}
        self.description = description
        # {"en":"Update time, format: yyyy-MM-dd HH:mm:ss.","zh_CN":"更新时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.update_time = update_time
        # {"en":"Rule ID.","zh_CN":"规则ID。"}
        self.id = id

    def validate(self):
        self.validate_required(self.condition, 'condition')
        if self.condition:
            self.condition.validate()
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.act, 'act')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.relation_domain_count, 'relation_domain_count')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.act is not None:
            result['act'] = self.act
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.relation_domain_count is not None:
            result['relationDomainCount'] = self.relation_domain_count
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = ListSharedCustomRulesResponseDataCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('act') is not None:
            self.act = m.get('act')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('relationDomainCount') is not None:
            self.relation_domain_count = m.get('relationDomainCount')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListSharedCustomRulesResponse(TeaModel):
    def __init__(
        self,
        msg: str = None,
        code: str = None,
        data: List[ListSharedCustomRulesResponseData] = None,
    ):
        # {"en":"Description.","zh_CN":"描述信息。"}
        self.msg = msg
        # {"dictionary":"belong=WAAP-MS-Ext|dict=waap_retCodeEnum","en":"Please refer to the error code for exceptions.","zh_CN":"请参照错误码。"}
        self.code = code
        # {"en":"Data.","zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.code, 'code')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = ListSharedCustomRulesResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ListSharedCustomRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateShareRateLimitRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待取消关联域名列表。","en":"List of hostname to be disassociated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class DisassociateShareRateLimitResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DisassociateShareRateLimitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareRateLimitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateShareRateLimitRequestHeader(TeaModel):
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


class DisassociateShareRateLimitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateSharedWAFRuleExceptionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        msg: str = None,
        type: str = None,
        match_type: str = None,
        content_list: List[str] = None,
    ):
        # {'en':'Rule exception ID.', 'zh_CN':'规则例外ID。'}
        self.id = id
        # {'en':'Exception name,maximum 50 character.
        # Does not support special characters and spaces.', 'zh_CN':'例外名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.name = name
        # {'en':'Exception description,maximum 200 characters.', 'zh_CN':'例外描述，最多200个字符。'}
        self.msg = msg
        # {'en':'Matching conditions.
        # ip: IP
        # path: Path
        # uri: URI
        # urlParamName: URI Parameter Name
        # urlParamValue: URI Parameter Value
        # userAgent: User Agent
        # httpHeaderName: Request Header Name
        # httpHeaderValue: Request Header Value
        # cookie: Cookie
        # body: Body
        # bodyParamName: Body Parameter Name
        # bodyParamValue: Body Parameter Value', 'zh_CN':'匹配条件。
        # ip：IP
        # path：路径
        # uri：URI
        # urlParamName：URI参数名
        # urlParamValue：URI参数值
        # userAgent：User Agent
        # httpHeaderName：请求头部名称
        # httpHeaderValue：请求头部值
        # cookie：Cookie
        # body：Body
        # bodyParamName：Body参数名
        # bodyParamValue：Body参数值'}
        self.type = type
        # {'en':'Match type,IP can only be EQUAL.
        # EQUAL: Equal
        # CONTAIN: Contains
        # REGEX: Regular match', 'zh_CN':'匹配类型，IP只能是等于。
        # EQUAL：等于
        # CONTAIN：包含
        # REGEX：正则匹配'}
        self.match_type = match_type
        # {'en':'Rule exceptions.
        # When matchType=EQUAL, case-sensitive, path and uri must start with "/", and body can only pass one value;
        # When matchType=REGEX, only one value can be passed', 'zh_CN':'规则例外内容。
        # matchType=EQUAL时，大小写敏感，path和uri必须以"/"开头，body只能传一个值；
        # matchType=REGEX时，只能传一个值。'}
        self.content_list = content_list

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.content_list, 'content_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.msg is not None:
            result['msg'] = self.msg
        if self.type is not None:
            result['type'] = self.type
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.content_list is not None:
            result['contentList'] = self.content_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('contentList') is not None:
            self.content_list = m.get('contentList')
        return self


class UpdateSharedWAFRuleExceptionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: bool = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Modification success indicator.', 'zh_CN':'修改成功标识。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateSharedWAFRuleExceptionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedWAFRuleExceptionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedWAFRuleExceptionRequestHeader(TeaModel):
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


class UpdateSharedWAFRuleExceptionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateCustomActionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        action_name: str = None,
        description: str = None,
        status_code: str = None,
        content_type: str = None,
        cus_block_cnt: str = None,
    ):
        # {'en':'Custom response ID.', 'zh_CN':'自定义响应ID。'}
        self.id = id
        # {'en':'Action name,maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'动作名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.action_name = action_name
        # {'en':'Description,maximum 200 characters.', 'zh_CN':'描述，最多200个字符。'}
        self.description = description
        # {'en':'Status code.
        # Valid value range:200,204,206,400,401,403,404,500,501,503.', 'zh_CN':'状态码。
        # 有效值范围：200，204，206，400，401，403，404，500，501，503。'}
        self.status_code = status_code
        # {'en':'Response Content-Type type,multiple separated by ; sign.', 'zh_CN':'响应Content-Type类型，多个以 ; 隔开。'}
        self.content_type = content_type
        # {'en':'Response content definition, the size of the response content cannot exceed 16KB, if you need to insert static resources such as pictures, it is recommended to use links to import. 
        # The following interception information parameters are supported: 
        #  {url} : Displays the URL information when intercepting 
        #  {client_ip} : Displays the intercepted user IP information 
        #  {time} : Displays the intercepted time point 
        #  {event_id} : Displays the ID information of this interception event', 'zh_CN':'自定义响应内容定义，响应内容大小不能超过16KB，如需插入图片等静态资源，建议采用链接引入。
        # 支持引用下列拦截信息参数：
        # {url}  ：显示拦截时的URL信息
        # {client_ip}  ：显示被拦截的用户IP信息
        # {time}  ：显示被拦截的时间点
        # {event_id}  ：显示本次拦截事件的ID信息'}
        self.cus_block_cnt = cus_block_cnt

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.description is not None:
            result['description'] = self.description
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.cus_block_cnt is not None:
            result['cusBlockCnt'] = self.cus_block_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('cusBlockCnt') is not None:
            self.cus_block_cnt = m.get('cusBlockCnt')
        return self


class UpdateCustomActionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateCustomActionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateCustomActionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateCustomActionRequestHeader(TeaModel):
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


class UpdateCustomActionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteCustomActionsRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {'en':'Custom response ID list.', 'zh_CN':'自定义响应ID列表。'}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class DeleteCustomActionsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteCustomActionsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCustomActionsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCustomActionsRequestHeader(TeaModel):
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


class DeleteCustomActionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryAppApiExceptionListRequest(TeaModel):
    def __init__(
        self,
        need_domain: bool = None,
    ):
        # {'en':'Do you need to return the number of associated hostnames? The default is false', 'zh_CN':'是否需要返回关联域名数，默认为false'}
        self.need_domain = need_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_domain is not None:
            result['needDomain'] = self.need_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('needDomain') is not None:
            self.need_domain = m.get('needDomain')
        return self


class QueryAppApiExceptionListDmsShareServiceFeatureDetailVO(TeaModel):
    def __init__(
        self,
        condition: str = None,
        match_type: str = None,
        condition_value: List[str] = None,
        key: str = None,
    ):
        # {'en':'Matching condition name.
        # PATH         Path
        # URI            URI
        # UA             User-Agent
        # REFERER    Referer
        # HEADER    Request Header
        # ', 'zh_CN':'匹配条件名称。
        # PATH                       路径
        # URI                          URI
        # UA                           User-Agent
        # REFERER                  Referer
        # HEAD                      Request Header
        # '}
        self.condition = condition
        # {'en':'Matching condition function.
        # CONTAIN                  contains
        # NOT_CONTAIN         does not contain
        # EQUAL                      equals
        # NOT_EQUAL             does not equal
        # EMPTY                      does not exist or has no value(When the condition is a path or URI, this value is not optional)
        # REGEX                      regex match
        # ', 'zh_CN':'匹配条件函数。
        # CONTAIN                  包含
        # NOT_CONTAIN         不包含 
        # EQUAL                      等于
        # NOT_EQUAL             不等于
        # EMPTY                      为空或不存在（当condition为路径或者URI时，该值不可选）
        # REGEX                       匹配正则 
        # '}
        self.match_type = match_type
        # {'en':'Condition value list, When matchType is EMPTY, the value is empty;  When matchType is REGEX, only one item is set', 'zh_CN':'条件值列表，当matchType为EMPTY时，该值为空；当matchType为REGEX时，只能传一条'}
        self.condition_value = condition_value
        # {'en':'Head value, If condition=HEAD, then this field is mandatory.', 'zh_CN':'头部值，如果condition为HEAD，则该字段必填'}
        self.key = key

    def validate(self):
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.condition_value, 'condition_value')
        self.validate_required(self.key, 'key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.condition_value is not None:
            result['conditionValue'] = self.condition_value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('conditionValue') is not None:
            self.condition_value = m.get('conditionValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class QueryAppApiExceptionListDmsShareServiceFeatureListVO(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        config: QueryAppApiExceptionListDmsShareServiceFeatureDetailVO = None,
        type: str = None,
        domain_num: int = None,
        creator: str = None,
    ):
        # {'en':'Rule ID', 'zh_CN':'规则ID'}
        self.rule_id = rule_id
        # {'en':'Rule name, duplicate not allowed.', 'zh_CN':'规则名称，不允许重复'}
        self.rule_name = rule_name
        # {'en':'Characteristic.', 'zh_CN':'特征。'}
        self.config = config
        # {
        # 'en':'Type enumeration, for example:
        # NATIVE_ APP        remarks: Native App
        # Callback_ API      	 remarks: Callback API
        # Other_ API       	  remarks: Other program API
        # HYBRID_ APP  	   remarks: Hybrid APP',
        # 'zh_CN':'类型枚举，例如：
        # NATIVE_APP          备注：原生APP
        # CALLBACK_API      备注：回调API
        # OTHER_API            备注：其他程序API
        # HYBRID_APP          备注：混合APP'}
        self.type = type
        # {'en':'Number of associated hostnames', 'zh_CN':'关联域名数量'}
        self.domain_num = domain_num
        # {'en':'Creator', 'zh_CN':'创建者'}
        self.creator = creator

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()
        self.validate_required(self.type, 'type')
        self.validate_required(self.domain_num, 'domain_num')
        self.validate_required(self.creator, 'creator')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.domain_num is not None:
            result['domainNum'] = self.domain_num
        if self.creator is not None:
            result['creator'] = self.creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('config') is not None:
            temp_model = QueryAppApiExceptionListDmsShareServiceFeatureDetailVO()
            self.config = temp_model.from_map(m['config'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('domainNum') is not None:
            self.domain_num = m.get('domainNum')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        return self


class QueryAppApiExceptionListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[QueryAppApiExceptionListDmsShareServiceFeatureListVO] = None,
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
                temp_model = QueryAppApiExceptionListDmsShareServiceFeatureListVO()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAppApiExceptionListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionListRequestHeader(TeaModel):
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


class QueryAppApiExceptionListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateCustomActionRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        description: str = None,
        status_code: str = None,
        content_type: str = None,
        cus_block_cnt: str = None,
    ):
        # {'en':'Action name,maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'动作名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.action_name = action_name
        # {'en':'Description,maximum 200 characters.', 'zh_CN':'描述，最多200个字符。'}
        self.description = description
        # {'en':'Status code.
        # Valid value range:200,204,206,400,401,403,404,500,501,503.', 'zh_CN':'状态码。
        # 有效值范围：200，204，206，400，401，403，404，500，501，503。'}
        self.status_code = status_code
        # {'en':'Response Content-Type type,multiple separated by ; sign.', 'zh_CN':'响应Content-Type类型，多个以 ; 隔开。'}
        self.content_type = content_type
        # {'en':'Response content definition, the size of the response content cannot exceed 16KB, if you need to insert static resources such as pictures, it is recommended to use links to import. 
        # The following interception information parameters are supported: 
        #  {url} : Displays the URL information when intercepting 
        #  {client_ip} : Displays the intercepted user IP information 
        #  {time} : Displays the intercepted time point 
        #  {event_id} : Displays the ID information of this interception event', 'zh_CN':'自定义响应内容定义，响应内容大小不能超过16KB，如需插入图片等静态资源，建议采用链接引入。
        # 支持引用下列拦截信息参数：
        # {url} ：显示拦截时的URL信息
        # {client_ip} ：显示被拦截的用户IP信息
        # {time} ：显示被拦截的时间点
        # {event_id} ：显示本次拦截事件的ID信息'}
        self.cus_block_cnt = cus_block_cnt

    def validate(self):
        self.validate_required(self.action_name, 'action_name')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.cus_block_cnt, 'cus_block_cnt')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.description is not None:
            result['description'] = self.description
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.cus_block_cnt is not None:
            result['cusBlockCnt'] = self.cus_block_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('cusBlockCnt') is not None:
            self.cus_block_cnt = m.get('cusBlockCnt')
        return self


class CreateCustomActionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Customize response ID.', 'zh_CN':'自定义响应ID。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateCustomActionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCustomActionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCustomActionRequestHeader(TeaModel):
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


class CreateCustomActionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateSharedWhitelistRuleIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"IP/CIDR, maximum 500 IP/CIDR.", "zh_CN":"IP/IP段，最多500个IP/IP段。"}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class UpdateSharedWhitelistRulePathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, path case sensitive
        # NOT_EQUAL: Does not equal, path case sensitive
        # CONTAIN: Contains, path case insensitive
        # NOT_CONTAIN: Does not Contains, path case insensitive
        # REGEX: Regex match, path case insensitive
        # NOT_REGEX: Regular does not match, path case sensitive
        # START_WITH: Starts with, path case sensitive
        # END_WITH: Ends with, path case sensitive
        # WILDCARD: Wildcard matches, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character.
        # NOT_WILDCARD: Wildcard does not match, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character ", "zh_CN":"匹配类型。
        # EQUAL：等于，路径大小写敏感
        # NOT_EQUAL：不等于，路径大小写敏感
        # CONTAIN：包含，路径大小写不敏感
        # NOT_CONTAIN：不包含，路径大小写不敏感
        # REGEX：匹配正则，路径大小写不敏感
        # NOT_REGEX：正则不匹配，路径大小写不敏感
        # START_WITH：开头是，路径大小写不敏感
        # END_WITH：结尾是，路径大小写不敏感
        # WILDCARD：通配符匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Path.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, path needs to start with "/", and no parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html.', 'zh_CN':'路径。
        # 当匹配类型为等于/不等于/开头是/结尾是，路径必须以“/”开头，不含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html。'}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class UpdateSharedWhitelistRuleUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, URI case sensitive
        # NOT_EQUAL: Does not equal, URI case sensitive
        # CONTAIN: Contains, URI case insensitive
        # NOT_CONTAIN: Does not Contains, URI case insensitive
        # REGEX: Regex match, URI case insensitive
        # NOT_REGEX: Regular does not match, URI case insensitive
        # START_WITH: Starts with, URI case insensitive
        # END_WITH: Ends with, URI case insensitive
        # WILDCARD: Wildcard matches, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，URI大小写敏感
        # NOT_EQUAL：不等于，URI大小写敏感
        # CONTAIN：包含，URI大小写不敏感
        # NOT_CONTAIN：不包含，URI大小写不敏感
        # REGEX：匹配正则，URI大小写不敏感
        # NOT_REGEX：正则不匹配，URI大小写不敏感
        # START_WITH：开头是，URI大小写不敏感
        # END_WITH：结尾是，URI大小写不敏感
        # WILDCARD：通配符匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'URI.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, uri needs to start with "/", and includes parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html?id=1.', 'zh_CN':'URI。
        # 当匹配类型为等于/不等于/开头是/结尾是，URI必须以”/“开头，含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html?id=1。'}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class UpdateSharedWhitelistRuleUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, user agent case sensitive
        # NOT_EQUAL: Does not equal, user agent case sensitive
        # CONTAIN: Contains, user agent case insensitive
        # NOT_CONTAIN: Does not Contains, user agent case insensitive
        # REGEX: Regex match, user agent case insensitive
        # NOT_REGEX: Regular does not match, user agent case insensitive
        # START_WITH: Starts with, user agent case insensitive
        # END_WITH: Ends with, user agent case insensitive
        # WILDCARD: Wildcard matches, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，User-Agent大小写敏感
        # NOT_EQUAL：不等于，User-Agent大小写敏感
        # CONTAIN：包含，User-Agent大小写不敏感
        # NOT_CONTAIN：不包含，User-Agent大小写不敏感
        # REGEX：匹配正则，User-Agent大小写不敏感
        # NOT_REGEX：正则不匹配，User-Agent大小写不敏感
        # START_WITH：开头是，User-Agent大小写不敏感
        # END_WITH：结尾是，User-Agent大小写不敏感
        # WILDCARD：通配符匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'User agent.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: go-Http-client/1.1.', 'zh_CN':'User-Agent。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：go-Http-client/1.1。'}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class UpdateSharedWhitelistRuleRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, referer case sensitive
        # NOT_EQUAL: Does not equal, referer case sensitive
        # CONTAIN: Contains, referer case insensitive
        # NOT_CONTAIN: Does not Contains, referer case insensitive
        # REGEX: Regex match, referer case insensitive
        # NOT_REGEX: Regular does not match, referer case insensitive
        # START_WITH: Starts with, referer case insensitive
        # END_WITH: Ends with, referer case insensitive
        # WILDCARD: Wildcard matches, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single characte
        # NOT_WILDCARD: Wildcard does not match, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，referer大小写敏感
        # NOT_EQUAL：不等于，referer大小写敏感
        # CONTAIN：包含，referer大小写不敏感
        # NOT_CONTAIN：不包含，referer大小写不敏感
        # REGEX：匹配正则，referer大小写不敏感
        # NOT_REGEX：正则不匹配，referer大小写不敏感
        # START_WITH：开头是，referer大小写不敏感
        # END_WITH：结尾是，referer大小写不敏感
        # WILDCARD：通配符匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Referer.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: http://test.com.', 'zh_CN':'Referer。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：http://test.com。'}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.referer, 'referer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class UpdateSharedWhitelistRuleHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, request header values case sensitive
        # NOT_EQUAL: Does not equal, request header values case sensitive
        # CONTAIN: Contains, request header values case insensitive
        # NOT_CONTAIN: Does not Contains, request header values case insensitive
        # REGEX: Regex match, request header values case insensitive
        # NOT_REGEX: Regular does not match, request header values case insensitive
        # START_WITH: Starts with, request header values case insensitive
        # END_WITH: Ends with, request header values case insensitive
        # WILDCARD: Wildcard matches, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，头部值大小写敏感
        # NOT_EQUAL：不等于，头部值大小写敏感
        # CONTAIN：包含，头部值大小写不敏感
        # NOT_CONTAIN：不包含，头部值大小写不敏感
        # REGEX：匹配正则，头部值大小写不敏感
        # NOT_REGEX：正则不匹配，头部值大小写不敏感
        # START_WITH：开头是，头部值大小写不敏感
        # END_WITH：结尾是，头部值大小写不敏感
        # WILDCARD：通配符匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Header name,case insensitive,up to 100 characters.
        # Example: Accept.', 'zh_CN':'头部名称，大小写不敏感，最多100个字符。
        # 示例：Accept。'}
        self.key = key
        # {'en':'Header value.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed.', 'zh_CN':'头部值。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。'}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class UpdateSharedWhitelistRuleWhitelistRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[UpdateSharedWhitelistRuleIpOrIpsCondition] = None,
        path_conditions: List[UpdateSharedWhitelistRulePathCondition] = None,
        uri_conditions: List[UpdateSharedWhitelistRuleUriCondition] = None,
        ua_conditions: List[UpdateSharedWhitelistRuleUaCondition] = None,
        referer_conditions: List[UpdateSharedWhitelistRuleRefererCondition] = None,
        header_conditions: List[UpdateSharedWhitelistRuleHeaderCondition] = None,
    ):
        # {"en":"IP/CIDR match conditions, match type cannot be repeated.", "zh_CN":"IP/IP段匹配条件，匹配类型不可重复。"}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {"en":"Path match conditions, match type cannot be repeated.", "zh_CN":"路径匹配条件，匹配类型不可重复。"}
        self.path_conditions = path_conditions
        # {"en":"URI match conditions, match type cannot be repeated.", "zh_CN":"URI匹配条件，匹配类型不可重复。"}
        self.uri_conditions = uri_conditions
        # {"en":"User agent match conditions, match type cannot be repeated.", "zh_CN":"User-Agent 匹配条件，匹配类型不可重复。"}
        self.ua_conditions = ua_conditions
        # {"en":"Referer match conditions, match type cannot be repeated.", "zh_CN":"Referer 匹配条件，匹配类型不可重复。"}
        self.referer_conditions = referer_conditions
        # {"en":"Request header match conditions.", "zh_CN":"请求头匹配条件。"}
        self.header_conditions = header_conditions

    def validate(self):
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = UpdateSharedWhitelistRuleIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = UpdateSharedWhitelistRulePathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = UpdateSharedWhitelistRuleUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = UpdateSharedWhitelistRuleUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = UpdateSharedWhitelistRuleRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = UpdateSharedWhitelistRuleHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        return self


class UpdateSharedWhitelistRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        rule_name: str = None,
        description: str = None,
        conditions: UpdateSharedWhitelistRuleWhitelistRuleCondition = None,
    ):
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.id = id
        # {"en":"Rule name, maximum 50 characters.
        #  Does not support special characters and spaces.", "zh_CN":"规则名称，最多50个字符。
        # 不支持特殊字符和空格。"}
        self.rule_name = rule_name
        # {"en":"Description, maximum 200 characters.", "zh_CN":"描述，最多200个字符。"}
        self.description = description
        # {"en":"Match conditions, at least one, at most five.", "zh_CN":"匹配条件，至少一个，至多五个。"}
        self.conditions = conditions

    def validate(self):
        self.validate_required(self.id, 'id')
        if self.conditions:
            self.conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('conditions') is not None:
            temp_model = UpdateSharedWhitelistRuleWhitelistRuleCondition()
            self.conditions = temp_model.from_map(m['conditions'])
        return self


class UpdateSharedWhitelistRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateSharedWhitelistRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedWhitelistRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedWhitelistRuleRequestHeader(TeaModel):
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


class UpdateSharedWhitelistRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryAppApiExceptionFeatureDetailRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {'en':'Rule Id', 'zh_CN':'规则 ID'}
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


class QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureDetailVO(TeaModel):
    def __init__(
        self,
        condition: str = None,
        match_type: str = None,
        condition_value: List[str] = None,
        key: str = None,
    ):
        # {'en':'Matching condition name.
        # PATH         Path
        # URI            URI
        # UA             User-Agent
        # REFERER    Referer
        # HEADER    Request Header
        # ', 'zh_CN':'匹配条件名称。
        # PATH                       路径
        # URI                          URI
        # UA                           User-Agent
        # REFERER                  Referer
        # HEAD                      Request Header
        # '}
        self.condition = condition
        # {'en':'Matching condition function.
        # CONTAIN                  contains
        # NOT_CONTAIN         does not contain
        # EQUAL                      equals
        # NOT_EQUAL             does not equal
        # EMPTY                      does not exist or has no value(When the condition is a path or URI, this value is not optional)
        # REGEX                      regex match
        # ', 'zh_CN':'匹配条件函数。
        # CONTAIN                  包含
        # NOT_CONTAIN         不包含 
        # EQUAL                      等于
        # NOT_EQUAL             不等于
        # EMPTY                      为空或不存在（当condition为路径或者URI时，该值不可选）
        # REGEX                       匹配正则 
        # '}
        self.match_type = match_type
        # {'en':'Condition value list, When matchType is EMPTY, the value is empty;  When matchType is REGEX, only one item is set', 'zh_CN':'条件值列表，当matchType为EMPTY时，该值为空；当matchType为REGEX时，只能传一条'}
        self.condition_value = condition_value
        # {'en':'Head value, If condition=HEAD, then this field is mandatory.', 'zh_CN':'头部值，如果condition为HEAD，则该字段必填'}
        self.key = key

    def validate(self):
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.condition_value, 'condition_value')
        self.validate_required(self.key, 'key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.condition_value is not None:
            result['conditionValue'] = self.condition_value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('conditionValue') is not None:
            self.condition_value = m.get('conditionValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureVO(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        config: QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureDetailVO = None,
        type: str = None,
    ):
        # {'en':'Rule name, duplicate not allowed.', 'zh_CN':'规则名称，不允许重复'}
        self.rule_name = rule_name
        # {'en':'Characteristic.', 'zh_CN':'特征。'}
        self.config = config
        # {
        # 'en':'Type enumeration, for example:
        # NATIVE_ APP        remarks: Native App
        # Callback_ API      	 remarks: Callback API
        # Other_ API       	  remarks: Other program API
        # HYBRID_ APP  	   remarks: Hybrid APP',
        # 'zh_CN':'类型枚举，例如：
        # NATIVE_APP          备注：原生APP
        # CALLBACK_API      备注：回调API
        # OTHER_API            备注：其他程序API
        # HYBRID_APP          备注：混合APP'}
        self.type = type

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('config') is not None:
            temp_model = QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureDetailVO()
            self.config = temp_model.from_map(m['config'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryAppApiExceptionFeatureDetailResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureVO = None,
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
            temp_model = QueryAppApiExceptionFeatureDetailDmsShareServiceFeatureVO()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryAppApiExceptionFeatureDetailPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionFeatureDetailParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionFeatureDetailRequestHeader(TeaModel):
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


class QueryAppApiExceptionFeatureDetailResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteAppApiExceptionFeatureRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {'en':'Rule Ids', 'zh_CN':'规则ID列表'}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class DeleteAppApiExceptionFeatureResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: bool = None,
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteAppApiExceptionFeaturePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAppApiExceptionFeatureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAppApiExceptionFeatureRequestHeader(TeaModel):
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


class DeleteAppApiExceptionFeatureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListSharedRateLimitingRulesRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
    ):
        # {'en':'Rule name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class ListSharedRateLimitingRulesRateLimitEffective(TeaModel):
    def __init__(
        self,
        effective: List[str] = None,
        start: str = None,
        end: str = None,
        timezone: str = None,
    ):
        # {'en':'effective.
        # MON:Monday
        # TUE:Tuesday
        # WED:Wednesday
        # THU:Thursday
        # FRI:Friday
        # SAT:Saturday
        # SUN:Sunday', 'zh_CN':'周期。
        # MON：星期一
        # TUE：星期二
        # WED：星期三
        # THU：星期四
        # FRI：星期五
        # SAT：星期六
        # SUN：星期天'}
        self.effective = effective
        # {'en':'Start time, format: HH:mm.', 'zh_CN':'开始时间，格式：HH:mm。'}
        self.start = start
        # {'en':'End time, format: HH:mm.', 'zh_CN':'结束时间，格式：HH:mm。'}
        self.end = end
        # {'en':'Timezone,default value: GTM+8.', 'zh_CN':'时区，默认：GTM+8。','dictionary':'belong=WAAP-MS-Ext|dict=waap_timezone'}
        self.timezone = timezone

    def validate(self):
        self.validate_required(self.effective, 'effective')
        self.validate_required(self.start, 'start')
        self.validate_required(self.end, 'end')
        self.validate_required(self.timezone, 'timezone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective is not None:
            result['effective'] = self.effective
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effective') is not None:
            self.effective = m.get('effective')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListSharedRateLimitingRulesIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'IP/CIDR.', 'zh_CN':'IP/IP段。'}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class ListSharedRateLimitingRulesPathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal
        # CONTAIN:Contains
        # NOT_CONTAIN:Does not contains
        # REGEX:Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配'}
        self.match_type = match_type
        # {'en':'Path.', 'zh_CN':'路径。'}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class ListSharedRateLimitingRulesUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal
        # CONTAIN:Contains
        # NOT_CONTAIN:Does not contains
        # REGEX:Regex match
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配'}
        self.match_type = match_type
        # {'en':'URI.', 'zh_CN':'URI。'}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class ListSharedRateLimitingRulesUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal
        # CONTAIN:Contains
        # NOT_CONTAIN:Does not contains
        # REGEX:Regex match
        # NONE:Empty or non-existent
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配'}
        self.match_type = match_type
        # {'en':'User agent.', 'zh_CN':'User-Agent。'}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class ListSharedRateLimitingRulesRequestMethodCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        request_method: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Request method.', 'zh_CN':'请求方法。'}
        self.request_method = request_method

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.request_method, 'request_method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        return self


class ListSharedRateLimitingRulesRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal
        # CONTAIN:Contains
        # NOT_CONTAIN:Does not contains
        # REGEX:Regex match
        # NONE:Empty or non-existent
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配'}
        self.match_type = match_type
        # {'en':'Referer.', 'zh_CN':'Referer。'}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class ListSharedRateLimitingRulesHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal
        # CONTAIN:Contains
        # NOT_CONTAIN:Does not contains
        # REGEX:Regex match
        # NONE:Empty or non-existent
        # NOT_REGEX: regular does not match
        # START_WITH: starts with
        # END_WITH: ends with
        # WILDCARD: wildcard matches
        # NOT_WILDCARD: wildcard does not match', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于
        # CONTAIN：包含
        # NOT_CONTAIN：不包含
        # REGEX：正则
        # NONE：为空或不存在
        # NOT_REGEX：正则不匹配
        # START_WITH：开头是
        # END_WITH：结尾是
        # WILDCARD：通配符匹配
        # NOT_WILDCARD：通配符不匹配'}
        self.match_type = match_type
        # {'en':'Header name.', 'zh_CN':'头部名称。'}
        self.key = key
        # {'en':'Header value.', 'zh_CN':'头部值。'}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class ListSharedRateLimitingRulesAreaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        areas: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Geo.', 'zh_CN':'区域。','dictionary':'belong=WAAP-MS-Ext|dict=waap_areaCityAndCountry'}
        self.areas = areas

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.areas, 'areas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.areas is not None:
            result['areas'] = self.areas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('areas') is not None:
            self.areas = m.get('areas')
        return self


class ListSharedRateLimitingRulesStatusCodeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        status_code: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Response Code.', 'zh_CN':'状态码。'}
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ListSharedRateLimitingRulesSchemeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        scheme: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equal
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'HTTP/S.
        # Supported values: HTTP/HTTPS.', 'zh_CN':'应用层协议。
        # 支持的值：HTTP/HTTPS。'}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.scheme, 'scheme')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class ListSharedRateLimitingRulesShareRateLimitRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[ListSharedRateLimitingRulesIpOrIpsCondition] = None,
        path_conditions: List[ListSharedRateLimitingRulesPathCondition] = None,
        uri_conditions: List[ListSharedRateLimitingRulesUriCondition] = None,
        ua_conditions: List[ListSharedRateLimitingRulesUaCondition] = None,
        method_conditions: List[ListSharedRateLimitingRulesRequestMethodCondition] = None,
        referer_conditions: List[ListSharedRateLimitingRulesRefererCondition] = None,
        header_conditions: List[ListSharedRateLimitingRulesHeaderCondition] = None,
        area_conditions: List[ListSharedRateLimitingRulesAreaCondition] = None,
        status_code_conditions: List[ListSharedRateLimitingRulesStatusCodeCondition] = None,
        scheme_conditions: List[ListSharedRateLimitingRulesSchemeCondition] = None,
    ):
        # {'en':'IP/CIDR.', 'zh_CN':'IP/IP段。'}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {'en':'Path.', 'zh_CN':'路径。'}
        self.path_conditions = path_conditions
        # {'en':'URI.', 'zh_CN':'URI。'}
        self.uri_conditions = uri_conditions
        # {'en':'User Agent.', 'zh_CN':'User-Agent。'}
        self.ua_conditions = ua_conditions
        # {'en':'Request Method.', 'zh_CN':'请求方法。'}
        self.method_conditions = method_conditions
        # {'en':'Referer.', 'zh_CN':'Referer。'}
        self.referer_conditions = referer_conditions
        # {'en':'Request Header.', 'zh_CN':'请求头。'}
        self.header_conditions = header_conditions
        # {'en':'Geo.', 'zh_CN':'区域。'}
        self.area_conditions = area_conditions
        # {'en':'Response Code.', 'zh_CN':'状态码。'}
        self.status_code_conditions = status_code_conditions
        # {'en':'HTTP/S.', 'zh_CN':'应用层协议。'}
        self.scheme_conditions = scheme_conditions

    def validate(self):
        self.validate_required(self.ip_or_ips_conditions, 'ip_or_ips_conditions')
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        self.validate_required(self.path_conditions, 'path_conditions')
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        self.validate_required(self.uri_conditions, 'uri_conditions')
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        self.validate_required(self.ua_conditions, 'ua_conditions')
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        self.validate_required(self.method_conditions, 'method_conditions')
        if self.method_conditions:
            for k in self.method_conditions:
                if k:
                    k.validate()
        self.validate_required(self.referer_conditions, 'referer_conditions')
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        self.validate_required(self.header_conditions, 'header_conditions')
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()
        self.validate_required(self.area_conditions, 'area_conditions')
        if self.area_conditions:
            for k in self.area_conditions:
                if k:
                    k.validate()
        self.validate_required(self.status_code_conditions, 'status_code_conditions')
        if self.status_code_conditions:
            for k in self.status_code_conditions:
                if k:
                    k.validate()
        self.validate_required(self.scheme_conditions, 'scheme_conditions')
        if self.scheme_conditions:
            for k in self.scheme_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.method_conditions is not None:
            result['methodConditions'] = []
            for k in self.method_conditions:
                result['methodConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        if self.area_conditions is not None:
            result['areaConditions'] = []
            for k in self.area_conditions:
                result['areaConditions'].append(k.to_map() if k else None)
        if self.status_code_conditions is not None:
            result['statusCodeConditions'] = []
            for k in self.status_code_conditions:
                result['statusCodeConditions'].append(k.to_map() if k else None)
        if self.scheme_conditions is not None:
            result['schemeConditions'] = []
            for k in self.scheme_conditions:
                result['schemeConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = ListSharedRateLimitingRulesIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = ListSharedRateLimitingRulesPathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = ListSharedRateLimitingRulesUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = ListSharedRateLimitingRulesUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('methodConditions') is not None:
            self.method_conditions = []
            for k in m.get('methodConditions'):
                temp_model = ListSharedRateLimitingRulesRequestMethodCondition()
                self.method_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = ListSharedRateLimitingRulesRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = ListSharedRateLimitingRulesHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        if m.get('areaConditions') is not None:
            self.area_conditions = []
            for k in m.get('areaConditions'):
                temp_model = ListSharedRateLimitingRulesAreaCondition()
                self.area_conditions.append(temp_model.from_map(k))
        if m.get('statusCodeConditions') is not None:
            self.status_code_conditions = []
            for k in m.get('statusCodeConditions'):
                temp_model = ListSharedRateLimitingRulesStatusCodeCondition()
                self.status_code_conditions.append(temp_model.from_map(k))
        if m.get('schemeConditions') is not None:
            self.scheme_conditions = []
            for k in m.get('schemeConditions'):
                temp_model = ListSharedRateLimitingRulesSchemeCondition()
                self.scheme_conditions.append(temp_model.from_map(k))
        return self


class ListSharedRateLimitingRulesCommonShareRateLimitRuleVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        creator: str = None,
        rule_name: str = None,
        description: str = None,
        statistical_stage: str = None,
        statistical_item: str = None,
        statistics_key: str = None,
        statistical_period: int = None,
        trigger_threshold: int = None,
        intercept_time: int = None,
        effective_status: str = None,
        rate_limit_effective: ListSharedRateLimitingRulesRateLimitEffective = None,
        action: str = None,
        rate_limit_rule_condition: ListSharedRateLimitingRulesShareRateLimitRuleCondition = None,
        count_share_rate_limit_domain: int = None,
        share_rate_limit_rel_domains: List[str] = None,
        update_time: str = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.id = id
        # {'en':'Creator.', 'zh_CN':'创建者。'}
        self.creator = creator
        # {'en':'Rule Name.', 'zh_CN':'规则名称。'}
        self.rule_name = rule_name
        # {'en':'Description.', 'zh_CN':'规则描述。'}
        self.description = description
        # {'en':'Statistical stage.
        # REQUEST:Request
        # RESPONSE:Response', 'zh_CN':'统计阶段。
        # REQUEST：请求
        # RESPONSE：响应'}
        self.statistical_stage = statistical_stage
        # {'en':'Client identifier.
        # IP:Client IP
        # IP_UA:Client IP and User-Agent
        # COOKIE:Cookie
        # IP_COOKIE:Client IP and Cookie
        # HEADER:Request Header
        # IP_HEADER:Client IP and Request Header', 'zh_CN':'统计粒度。
        # IP：客户端IP
        # IP_UA：客户端IP和User-Agent
        # COOKIE：Cookie
        # IP_COOKIE：客户端IP和Cookie
        # HEADER：请求头
        # IP_HEADER：客户端IP和请求头'}
        self.statistical_item = statistical_item
        # {'en':'Statistical key value.', 'zh_CN':'统计key值。'}
        self.statistics_key = statistics_key
        # {'en':'Statistics period, unit: seconds.', 'zh_CN':'统计周期，单位：秒。'}
        self.statistical_period = statistical_period
        # {'en':'Trigger threshold, unit: times.', 'zh_CN':'触发阈值，单位：次。'}
        self.trigger_threshold = trigger_threshold
        # {'en':'Action duration, unit: seconds.', 'zh_CN':'处理动作持续时间，单位：秒。'}
        self.intercept_time = intercept_time
        # {'en':'Cycle effective status.
        # PERMANENT:All time
        # WITHOUT:Excluded time
        # WITHIN:Selected time', 'zh_CN':'周期生效状态。
        # PERMANENT：永久生效
        # WITHOUT：周期内不生效
        # WITHIN：周期内生效'}
        self.effective_status = effective_status
        # {'en':'Effective time period.', 'zh_CN':'规则生效周期。'}
        self.rate_limit_effective = rate_limit_effective
        # {'en':'Action.
        # NO_USE:Not Used
        # LOG:Log
        # COOKIE:Cookie verification
        # JS_CHECK:Javascript verification
        # DELAY:Delay
        # BLOCK:Deny
        # RESET:Reset Connection
        # Custom action primary key id:Custom action primary key id', 'zh_CN':'处理动作。
        # NO_USE：不使用
        # LOG：监控
        # COOKIE：Cookie校验
        # JS_CHECK：JavaScript校验
        # DELAY：延迟响应
        # BLOCK：拦截
        # RESET：断开连接
        # 自定义处理动作主键id：自定义处理动作主键id'}
        self.action = action
        # {'en':'Matching conditions.', 'zh_CN':'匹配条件。'}
        self.rate_limit_rule_condition = rate_limit_rule_condition
        # {'en':'Associated hostnames.', 'zh_CN':'关联域名数。'}
        self.count_share_rate_limit_domain = count_share_rate_limit_domain
        # {'en':'List of associated hostnames.', 'zh_CN':'关联域名列表。'}
        self.share_rate_limit_rel_domains = share_rate_limit_rel_domains
        # {'en':'Update time.', 'zh_CN':'更新时间。'}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.statistical_stage, 'statistical_stage')
        self.validate_required(self.statistical_item, 'statistical_item')
        self.validate_required(self.statistics_key, 'statistics_key')
        self.validate_required(self.statistical_period, 'statistical_period')
        self.validate_required(self.trigger_threshold, 'trigger_threshold')
        self.validate_required(self.intercept_time, 'intercept_time')
        self.validate_required(self.effective_status, 'effective_status')
        self.validate_required(self.rate_limit_effective, 'rate_limit_effective')
        if self.rate_limit_effective:
            self.rate_limit_effective.validate()
        self.validate_required(self.action, 'action')
        self.validate_required(self.rate_limit_rule_condition, 'rate_limit_rule_condition')
        if self.rate_limit_rule_condition:
            self.rate_limit_rule_condition.validate()
        self.validate_required(self.count_share_rate_limit_domain, 'count_share_rate_limit_domain')
        self.validate_required(self.share_rate_limit_rel_domains, 'share_rate_limit_rel_domains')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.statistical_stage is not None:
            result['statisticalStage'] = self.statistical_stage
        if self.statistical_item is not None:
            result['statisticalItem'] = self.statistical_item
        if self.statistics_key is not None:
            result['statisticsKey'] = self.statistics_key
        if self.statistical_period is not None:
            result['statisticalPeriod'] = self.statistical_period
        if self.trigger_threshold is not None:
            result['triggerThreshold'] = self.trigger_threshold
        if self.intercept_time is not None:
            result['interceptTime'] = self.intercept_time
        if self.effective_status is not None:
            result['effectiveStatus'] = self.effective_status
        if self.rate_limit_effective is not None:
            result['rateLimitEffective'] = self.rate_limit_effective.to_map()
        if self.action is not None:
            result['action'] = self.action
        if self.rate_limit_rule_condition is not None:
            result['rateLimitRuleCondition'] = self.rate_limit_rule_condition.to_map()
        if self.count_share_rate_limit_domain is not None:
            result['countShareRateLimitDomain'] = self.count_share_rate_limit_domain
        if self.share_rate_limit_rel_domains is not None:
            result['shareRateLimitRelDomains'] = self.share_rate_limit_rel_domains
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statisticalStage') is not None:
            self.statistical_stage = m.get('statisticalStage')
        if m.get('statisticalItem') is not None:
            self.statistical_item = m.get('statisticalItem')
        if m.get('statisticsKey') is not None:
            self.statistics_key = m.get('statisticsKey')
        if m.get('statisticalPeriod') is not None:
            self.statistical_period = m.get('statisticalPeriod')
        if m.get('triggerThreshold') is not None:
            self.trigger_threshold = m.get('triggerThreshold')
        if m.get('interceptTime') is not None:
            self.intercept_time = m.get('interceptTime')
        if m.get('effectiveStatus') is not None:
            self.effective_status = m.get('effectiveStatus')
        if m.get('rateLimitEffective') is not None:
            temp_model = ListSharedRateLimitingRulesRateLimitEffective()
            self.rate_limit_effective = temp_model.from_map(m['rateLimitEffective'])
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('rateLimitRuleCondition') is not None:
            temp_model = ListSharedRateLimitingRulesShareRateLimitRuleCondition()
            self.rate_limit_rule_condition = temp_model.from_map(m['rateLimitRuleCondition'])
        if m.get('countShareRateLimitDomain') is not None:
            self.count_share_rate_limit_domain = m.get('countShareRateLimitDomain')
        if m.get('shareRateLimitRelDomains') is not None:
            self.share_rate_limit_rel_domains = m.get('shareRateLimitRelDomains')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListSharedRateLimitingRulesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListSharedRateLimitingRulesCommonShareRateLimitRuleVO] = None,
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
                temp_model = ListSharedRateLimitingRulesCommonShareRateLimitRuleVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListSharedRateLimitingRulesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedRateLimitingRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedRateLimitingRulesRequestHeader(TeaModel):
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


class ListSharedRateLimitingRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListSharedWAFRuleExceptionsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedWAFRuleExceptionsWafShareExceptionDomainRule(TeaModel):
    def __init__(
        self,
        domain: str = None,
        rule_id_list: List[int] = None,
    ):
        # {'en':'Hostname.', 'zh_CN':'域名。'}
        self.domain = domain
        # {'en':'WAF rule ID list.', 'zh_CN':'WAF规则ID列表。'}
        self.rule_id_list = rule_id_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.rule_id_list, 'rule_id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.rule_id_list is not None:
            result['ruleIdList'] = self.rule_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ruleIdList') is not None:
            self.rule_id_list = m.get('ruleIdList')
        return self


class ListSharedWAFRuleExceptionsWafUserShareExceptionListVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        msg: str = None,
        type: str = None,
        match_type: str = None,
        content_list: List[str] = None,
        creator: str = None,
        create_time: str = None,
        update_time: str = None,
        domain_rule_list: List[ListSharedWAFRuleExceptionsWafShareExceptionDomainRule] = None,
    ):
        # {'en':'Rule exception ID.', 'zh_CN':'规则例外ID。'}
        self.id = id
        # {'en':'Exception name,maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'例外名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.name = name
        # {'en':'Exception description,maximum 200 characters..', 'zh_CN':'例外描述，最多200个字符。'}
        self.msg = msg
        # {'en':'Matching conditions.
        # ip: IP
        # path: Path
        # uri: URI
        # urlParamName: URI Parameter Name
        # urlParamValue: URI Parameter Value
        # userAgent: User Agent
        # httpHeaderName: Request Header Name
        # httpHeaderValue: Request Header Value
        # cookie: Cookie
        # body: Body
        # bodyParamName: Body Parameter Name
        # bodyParamValue: Body Parameter Value', 'zh_CN':'匹配条件。
        # ip：IP
        # path：路径
        # uri：URI
        # urlParamName：URI参数名
        # urlParamValue：URI参数值
        # userAgent：User Agent
        # httpHeaderName：请求头部名称
        # httpHeaderValue：请求头部值
        # cookie：Cookie
        # body：Body
        # bodyParamName：Body参数名
        # bodyParamValue：Body参数值'}
        self.type = type
        # {'en':'Match type,IP can only be EQUAL.
        # EQUAL: Equal
        # CONTAIN: Contains
        # REGEX: Regular match', 'zh_CN':'匹配类型，IP只能是等于。
        # EQUAL：等于
        # CONTAIN：包含
        # REGEX：正则匹配'}
        self.match_type = match_type
        # {'en':'Rule exceptions.
        # When matchType=EQUAL, case-sensitive.', 'zh_CN':'规则例外内容。
        # matchType=EQUAL时，大小写敏感。
        # '}
        self.content_list = content_list
        # {'en':'Creator login.', 'zh_CN':'创建者登录名。'}
        self.creator = creator
        # {'en':'Creation time.', 'zh_CN':'创建时间。'}
        self.create_time = create_time
        # {'en':'Update time.', 'zh_CN':'更新时间。'}
        self.update_time = update_time
        # {'en':'List of associated hostnames and rule IDs.', 'zh_CN':'关联的域名以及规则ID列表。'}
        self.domain_rule_list = domain_rule_list

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.type, 'type')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.content_list, 'content_list')
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.domain_rule_list, 'domain_rule_list')
        if self.domain_rule_list:
            for k in self.domain_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.msg is not None:
            result['msg'] = self.msg
        if self.type is not None:
            result['type'] = self.type
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.content_list is not None:
            result['contentList'] = self.content_list
        if self.creator is not None:
            result['creator'] = self.creator
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.domain_rule_list is not None:
            result['domainRuleList'] = []
            for k in self.domain_rule_list:
                result['domainRuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('contentList') is not None:
            self.content_list = m.get('contentList')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('domainRuleList') is not None:
            self.domain_rule_list = []
            for k in m.get('domainRuleList'):
                temp_model = ListSharedWAFRuleExceptionsWafShareExceptionDomainRule()
                self.domain_rule_list.append(temp_model.from_map(k))
        return self


class ListSharedWAFRuleExceptionsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListSharedWAFRuleExceptionsWafUserShareExceptionListVO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Shared configuration WAF rule exception list.', 'zh_CN':'共享配置WAF规则例外列表。'}
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
                temp_model = ListSharedWAFRuleExceptionsWafUserShareExceptionListVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListSharedWAFRuleExceptionsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedWAFRuleExceptionsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSharedWAFRuleExceptionsRequestHeader(TeaModel):
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


class ListSharedWAFRuleExceptionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryAppApiExceptionFeatureReferencedHostnamesRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {'en':'Rule Id, Only supports single rule queries', 'zh_CN':'规则ID，仅支持单个规则查询'}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class QueryAppApiExceptionFeatureReferencedHostnamesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[str] = None,
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryAppApiExceptionFeatureReferencedHostnamesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionFeatureReferencedHostnamesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAppApiExceptionFeatureReferencedHostnamesRequestHeader(TeaModel):
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


class QueryAppApiExceptionFeatureReferencedHostnamesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteSharedWhitelistRuleRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {"en":"Rule ID List.", "zh_CN":"规则ID列表。"}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class DeleteSharedWhitelistRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteSharedWhitelistRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedWhitelistRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedWhitelistRuleRequestHeader(TeaModel):
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


class DeleteSharedWhitelistRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateShareConfigurationsAppApiExceptionFeatureDmsShareServiceFeatureUpdateDTO(TeaModel):
    def __init__(
        self,
        condition: str = None,
        match_type: str = None,
        condition_value: List[str] = None,
        key: str = None,
    ):
        # {'en':'Matching condition name.
        # PATH         Path
        # URI            URI
        # UA             User-Agent
        # REFERER    Referer
        # HEADER    Request Header
        # ', 'zh_CN':'匹配条件名称。
        # PATH                       路径
        # URI                          URI
        # UA                           User-Agent
        # REFERER                  Referer
        # HEAD                      Request Header
        # '}
        self.condition = condition
        # {'en':'Matching condition function.
        # CONTAIN                  contains
        # NOT_CONTAIN         does not contain
        # EQUAL                      equals
        # NOT_EQUAL             does not equal
        # EMPTY                      does not exist or has no value(When the condition is a path or URI, this value is not optional)
        # REGEX                      regex match
        # ', 'zh_CN':'匹配条件函数。
        # CONTAIN                  包含
        # NOT_CONTAIN         不包含 
        # EQUAL                      等于
        # NOT_EQUAL             不等于
        # EMPTY                      为空或不存在（当condition为路径或者URI时，该值不可选）
        # REGEX                       匹配正则 
        # '}
        self.match_type = match_type
        # {'en':'Condition value list, When matchType is EMPTY, the value is empty;  When matchType is REGEX, only one item is set', 'zh_CN':'条件值列表，当matchType为EMPTY时，该值为空；当matchType为REGEX时，只能传一条'}
        self.condition_value = condition_value
        # {'en':'Head value, If condition=HEAD, then this field is mandatory, Otherwise, it is empty.', 'zh_CN':'头部值，如果condition为HEAD，则该字段必填，否则为空。'}
        self.key = key

    def validate(self):
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.condition_value, 'condition_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.condition_value is not None:
            result['conditionValue'] = self.condition_value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('conditionValue') is not None:
            self.condition_value = m.get('conditionValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class UpdateShareConfigurationsAppApiExceptionFeatureRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        type: str = None,
        config: UpdateShareConfigurationsAppApiExceptionFeatureDmsShareServiceFeatureUpdateDTO = None,
    ):
        # {'en':'Rule ID', 'zh_CN':'规则ID'}
        self.rule_id = rule_id
        # {'en':'Rule name, duplicate not allowed.', 'zh_CN':'规则名称，不允许重复'}
        self.rule_name = rule_name
        # {
        # 'en':'Type enumeration, for example:
        # NATIVE_ APP        remarks: Native App
        # Callback_ API      	 remarks: Callback API
        # Other_ API       	  remarks: Other program API
        # HYBRID_ APP  	   remarks: Hybrid APP',
        # 'zh_CN':'类型枚举，例如：
        # NATIVE_APP          备注：原生APP
        # CALLBACK_API      备注：回调API
        # OTHER_API            备注：其他程序API
        # HYBRID_APP          备注：混合APP'}
        self.type = type
        # {'en':'Characteristic.', 'zh_CN':'特征。'}
        self.config = config

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.type is not None:
            result['type'] = self.type
        if self.config is not None:
            result['config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('config') is not None:
            temp_model = UpdateShareConfigurationsAppApiExceptionFeatureDmsShareServiceFeatureUpdateDTO()
            self.config = temp_model.from_map(m['config'])
        return self


class UpdateShareConfigurationsAppApiExceptionFeatureResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateShareConfigurationsAppApiExceptionFeaturePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateShareConfigurationsAppApiExceptionFeatureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateShareConfigurationsAppApiExceptionFeatureRequestHeader(TeaModel):
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


class UpdateShareConfigurationsAppApiExceptionFeatureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteSharedRateLimitingRuleRequest(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
    ):
        # {'en':'Rule ID List.', 'zh_CN':'规则ID列表。'}
        self.ids = ids

    def validate(self):
        self.validate_required(self.ids, 'ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class DeleteSharedRateLimitingRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteSharedRateLimitingRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedRateLimitingRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedRateLimitingRuleRequestHeader(TeaModel):
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


class DeleteSharedRateLimitingRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateShareCustomizeBotsRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享配置ID。","en":"Share configuration ID."}
        self.share_id = share_id
        # {"zh_CN":"待关联域名列表。","en":"List of hostname to be associated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class AssociateShareCustomizeBotsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AssociateShareCustomizeBotsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareCustomizeBotsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareCustomizeBotsRequestHeader(TeaModel):
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


class AssociateShareCustomizeBotsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteSharedWAFRuleExceptionRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {'en':'Rule exception ID list.', 'zh_CN':'规则例外ID列表。'}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class DeleteSharedWAFRuleExceptionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: bool = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Delete success indicator.', 'zh_CN':'删除成功标识。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteSharedWAFRuleExceptionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedWAFRuleExceptionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSharedWAFRuleExceptionRequestHeader(TeaModel):
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


class DeleteSharedWAFRuleExceptionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateAppApiExceptionFeatureDmsShareServiceFeatureAddDTO(TeaModel):
    def __init__(
        self,
        condition: str = None,
        match_type: str = None,
        condition_value: List[str] = None,
        key: str = None,
    ):
        # {'en':'Matching condition name.
        # PATH         Path
        # URI            URI
        # UA             User-Agent
        # REFERER    Referer
        # HEADER    Request Header
        # ', 'zh_CN':'匹配条件名称。
        # PATH                       路径
        # URI                          URI
        # UA                           User-Agent
        # REFERER                  Referer
        # HEAD                      Request Header
        # '}
        self.condition = condition
        # {'en':'Matching condition function.
        # CONTAIN                  contains
        # NOT_CONTAIN         does not contain
        # EQUAL                      equals
        # NOT_EQUAL             does not equal
        # EMPTY                      does not exist or has no value(When the condition is a path or URI, this value is not optional)
        # REGEX                      regex match
        # ', 'zh_CN':'匹配条件函数。
        # CONTAIN                  包含
        # NOT_CONTAIN         不包含 
        # EQUAL                      等于
        # NOT_EQUAL             不等于
        # EMPTY                      为空或不存在（当condition为路径或者URI时，该值不可选）
        # REGEX                       匹配正则 
        # '}
        self.match_type = match_type
        # {'en':'Condition value list, When matchType is EMPTY, the value is empty;  When matchType is REGEX, only one item is set', 'zh_CN':'条件值列表，当matchType为EMPTY时，该值为空；当matchType为REGEX时，只能传一条'}
        self.condition_value = condition_value
        # {'en':'Head value, If condition=HEAD, then this field is mandatory, Otherwise, it is empty.', 'zh_CN':'头部值，如果condition为HEAD，则该字段必填，否则为空。'}
        self.key = key

    def validate(self):
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.condition_value, 'condition_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.condition_value is not None:
            result['conditionValue'] = self.condition_value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('conditionValue') is not None:
            self.condition_value = m.get('conditionValue')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class CreateAppApiExceptionFeatureRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        type: str = None,
        config: CreateAppApiExceptionFeatureDmsShareServiceFeatureAddDTO = None,
    ):
        # {'en':'Rule name, duplicate not allowed.', 'zh_CN':'规则名称，不允许重复'}
        self.rule_name = rule_name
        # {
        # 'en':'Type enumeration, for example:
        # NATIVE_ APP        remarks: Native App
        # Callback_ API      	 remarks: Callback API
        # Other_ API       	  remarks: Other program API
        # HYBRID_ APP  	   remarks: Hybrid APP',
        # 'zh_CN':'类型枚举，例如：
        # NATIVE_APP          备注：原生APP
        # CALLBACK_API      备注：回调API
        # OTHER_API            备注：其他程序API
        # HYBRID_APP          备注：混合APP'}
        self.type = type
        # {'en':'Characteristic.', 'zh_CN':'特征。'}
        self.config = config

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.config, 'config')
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.type is not None:
            result['type'] = self.type
        if self.config is not None:
            result['config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('config') is not None:
            temp_model = CreateAppApiExceptionFeatureDmsShareServiceFeatureAddDTO()
            self.config = temp_model.from_map(m['config'])
        return self


class CreateAppApiExceptionFeatureResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateAppApiExceptionFeaturePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAppApiExceptionFeatureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAppApiExceptionFeatureRequestHeader(TeaModel):
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


class CreateAppApiExceptionFeatureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateSharedWhitelistRuleRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待取消关联域名列表。","en":"List of hostname to be disassociated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class DisassociateSharedWhitelistRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DisassociateSharedWhitelistRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateSharedWhitelistRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateSharedWhitelistRuleRequestHeader(TeaModel):
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


class DisassociateSharedWhitelistRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateSharedRateLimitingRuleRateLimitEffective(TeaModel):
    def __init__(
        self,
        effective: List[str] = None,
        start: str = None,
        end: str = None,
        timezone: str = None,
    ):
        # {'en':'Effective.
        # MON:Monday
        # TUE:Tuesday
        # WED:Wednesday
        # THU:Thursday
        # FRI:Friday
        # SAT:Saturday
        # SUN:Sunday', 'zh_CN':'周期。
        # MON：星期一
        # TUE：星期二
        # WED：星期三
        # THU：星期四
        # FRI：星期五
        # SAT：星期六
        # SUN：星期天'}
        self.effective = effective
        # {'en':'Start time, format: HH:mm.', 'zh_CN':'开始时间，格式：HH:mm。'}
        self.start = start
        # {'en':'End time, format: HH:mm.', 'zh_CN':'结束时间，格式：HH:mm。'}
        self.end = end
        # {'en':'Timezone,default value: GTM+8.', 'zh_CN':'时区，默认：GTM+8。','dictionary':'belong=WAAP-MS-Ext|dict=waap_timezone'}
        self.timezone = timezone

    def validate(self):
        self.validate_required(self.effective, 'effective')
        self.validate_required(self.start, 'start')
        self.validate_required(self.end, 'end')
        self.validate_required(self.timezone, 'timezone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective is not None:
            result['effective'] = self.effective
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effective') is not None:
            self.effective = m.get('effective')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class UpdateSharedRateLimitingRuleIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'IP/CIDR, maximum 500 IP/CIDR.', 'zh_CN':'IP/IP段，最多500个IP/IP段。'}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class UpdateSharedRateLimitingRulePathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, path case sensitive
        # NOT_EQUAL: Does not equal, path case sensitive
        # CONTAIN: Contains, path case insensitive
        # NOT_CONTAIN: Does not Contains, path case insensitive
        # REGEX: Regex match, path case insensitive
        # NOT_REGEX: Regular does not match, path case sensitive
        # START_WITH: Starts with, path case sensitive
        # END_WITH: Ends with, path case sensitive
        # WILDCARD: Wildcard matches, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character.
        # NOT_WILDCARD: Wildcard does not match, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character ", "zh_CN":"匹配类型。
        # EQUAL：等于，路径大小写敏感
        # NOT_EQUAL：不等于，路径大小写敏感
        # CONTAIN：包含，路径大小写不敏感
        # NOT_CONTAIN：不包含，路径大小写不敏感
        # REGEX：匹配正则，路径大小写不敏感
        # NOT_REGEX：正则不匹配，路径大小写不敏感
        # START_WITH：开头是，路径大小写不敏感
        # END_WITH：结尾是，路径大小写不敏感
        # WILDCARD：通配符匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Path.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, path needs to start with "/", and no parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html.', 'zh_CN':'路径。
        # 当匹配类型为等于/不等于/开头是/结尾是，路径必须以“/”开头，不含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html。'}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class UpdateSharedRateLimitingRuleUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, URI case sensitive
        # NOT_EQUAL: Does not equal, URI case sensitive
        # CONTAIN: Contains, URI case insensitive
        # NOT_CONTAIN: Does not Contains, URI case insensitive
        # REGEX: Regex match, URI case insensitive
        # NOT_REGEX: Regular does not match, URI case insensitive
        # START_WITH: Starts with, URI case insensitive
        # END_WITH: Ends with, URI case insensitive
        # WILDCARD: Wildcard matches, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，URI大小写敏感
        # NOT_EQUAL：不等于，URI大小写敏感
        # CONTAIN：包含，URI大小写不敏感
        # NOT_CONTAIN：不包含，URI大小写不敏感
        # REGEX：匹配正则，URI大小写不敏感
        # NOT_REGEX：正则不匹配，URI大小写不敏感
        # START_WITH：开头是，URI大小写不敏感
        # END_WITH：结尾是，URI大小写不敏感
        # WILDCARD：通配符匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'URI.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, uri needs to start with "/", and includes parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html?id=1.', 'zh_CN':'URI。
        # 当匹配类型为等于/不等于/开头是/结尾是，URI必须以”/“开头，含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html?id=1。'}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class UpdateSharedRateLimitingRuleUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, user agent case sensitive
        # NOT_EQUAL: Does not equal, user agent case sensitive
        # CONTAIN: Contains, user agent case insensitive
        # NOT_CONTAIN: Does not Contains, user agent case insensitive
        # NONE:Empty or non-existent
        # REGEX: Regex match, user agent case insensitive
        # NOT_REGEX: Regular does not match, user agent case insensitive
        # START_WITH: Starts with, user agent case insensitive
        # END_WITH: Ends with, user agent case insensitive
        # WILDCARD: Wildcard matches, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，User-Agent大小写敏感
        # NOT_EQUAL：不等于，User-Agent大小写敏感
        # CONTAIN：包含，User-Agent大小写不敏感
        # NOT_CONTAIN：不包含，User-Agent大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，User-Agent大小写不敏感
        # NOT_REGEX：正则不匹配，User-Agent大小写不敏感
        # START_WITH：开头是，User-Agent大小写不敏感
        # END_WITH：结尾是，User-Agent大小写不敏感
        # WILDCARD：通配符匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'User agent.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: go-Http-client/1.1.', 'zh_CN':'User-Agent。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：go-Http-client/1.1。'}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class UpdateSharedRateLimitingRuleRequestMethodCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        request_method: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Request method.
        # Supported values: GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY.', 'zh_CN':'请求方法。
        # 支持的值：GET/POST/DELETE/PUT/HEAD/OPTIONS/COPY。'}
        self.request_method = request_method

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.request_method, 'request_method')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        return self


class UpdateSharedRateLimitingRuleRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, referer case sensitive
        # NOT_EQUAL: Does not equal, referer case sensitive
        # CONTAIN: Contains, referer case insensitive
        # NOT_CONTAIN: Does not Contains, referer case insensitive
        # NONE:Empty or non-existent
        # REGEX: Regex match, referer case insensitive
        # NOT_REGEX: Regular does not match, referer case insensitive
        # START_WITH: Starts with, referer case insensitive
        # END_WITH: Ends with, referer case insensitive
        # WILDCARD: Wildcard matches, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single characte
        # NOT_WILDCARD: Wildcard does not match, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，referer大小写敏感
        # NOT_EQUAL：不等于，referer大小写敏感
        # CONTAIN：包含，referer大小写不敏感
        # NOT_CONTAIN：不包含，referer大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，referer大小写不敏感
        # NOT_REGEX：正则不匹配，referer大小写不敏感
        # START_WITH：开头是，referer大小写不敏感
        # END_WITH：结尾是，referer大小写不敏感
        # WILDCARD：通配符匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Referer.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: http://test.com.', 'zh_CN':'Referer。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：http://test.com。'}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.referer, 'referer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class UpdateSharedRateLimitingRuleHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, request header values case sensitive
        # NOT_EQUAL: Does not equal, request header values case sensitive
        # CONTAIN: Contains, request header values case insensitive
        # NOT_CONTAIN: Does not Contains, request header values case insensitive
        # NONE: Empty or non-existent
        # REGEX: Regex match, request header values case insensitive
        # NOT_REGEX: Regular does not match, request header values case insensitive
        # START_WITH: Starts with, request header values case insensitive
        # END_WITH: Ends with, request header values case insensitive
        # WILDCARD: Wildcard matches, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，头部值大小写敏感
        # NOT_EQUAL：不等于，头部值大小写敏感
        # CONTAIN：包含，头部值大小写不敏感
        # NOT_CONTAIN：不包含，头部值大小写不敏感
        # NONE：为空或不存在
        # REGEX：匹配正则，头部值大小写不敏感
        # NOT_REGEX：正则不匹配，头部值大小写不敏感
        # START_WITH：开头是，头部值大小写不敏感
        # END_WITH：结尾是，头部值大小写不敏感
        # WILDCARD：通配符匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Header name,case insensitive,up to 100 characters.
        # Example: Accept.', 'zh_CN':'头部名称，大小写不敏感，最多100个字符。
        # 示例：Accept。'}
        self.key = key
        # {'en':'Header value.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed.', 'zh_CN':'头部值。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。'}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class UpdateSharedRateLimitingRuleAreaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        areas: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Geo.', 'zh_CN':'区域。','dictionary':'belong=WAAP-MS-Ext|dict=waap_areaCityAndCountry'}
        self.areas = areas

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.areas, 'areas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.areas is not None:
            result['areas'] = self.areas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('areas') is not None:
            self.areas = m.get('areas')
        return self


class UpdateSharedRateLimitingRuleStatusCodeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        status_code: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'Response Code.', 'zh_CN':'状态码。'}
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateSharedRateLimitingRuleSchemeCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        scheme: List[str] = None,
    ):
        # {'en':'Match type.
        # EQUAL:Equals
        # NOT_EQUAL:Does not equal', 'zh_CN':'匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于'}
        self.match_type = match_type
        # {'en':'HTTP/S.
        # Supported values: HTTP/HTTPS.', 'zh_CN':'应用层协议。
        # 支持的值：HTTP/HTTPS。'}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.scheme, 'scheme')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class UpdateSharedRateLimitingRuleShareRateLimitRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[UpdateSharedRateLimitingRuleIpOrIpsCondition] = None,
        path_conditions: List[UpdateSharedRateLimitingRulePathCondition] = None,
        uri_conditions: List[UpdateSharedRateLimitingRuleUriCondition] = None,
        ua_conditions: List[UpdateSharedRateLimitingRuleUaCondition] = None,
        method_conditions: List[UpdateSharedRateLimitingRuleRequestMethodCondition] = None,
        referer_conditions: List[UpdateSharedRateLimitingRuleRefererCondition] = None,
        header_conditions: List[UpdateSharedRateLimitingRuleHeaderCondition] = None,
        area_conditions: List[UpdateSharedRateLimitingRuleAreaCondition] = None,
        status_code_conditions: List[UpdateSharedRateLimitingRuleStatusCodeCondition] = None,
        scheme_conditions: List[UpdateSharedRateLimitingRuleSchemeCondition] = None,
    ):
        # {'en':'IP/CIDR, match type cannot be repeated.', 'zh_CN':'IP/IP段，匹配类型不可重复。'}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {'en':'Path, match type cannot be repeated.
        # When the business scenario is API, this matching condition is not supported.', 'zh_CN':'路径，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.path_conditions = path_conditions
        # {'en':'URI, match type cannot be repeated.
        # 
        # When the business scenario is API, this matching condition is not supported.', 'zh_CN':'URI，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.uri_conditions = uri_conditions
        # {'en':'User Agent, match type cannot be repeated.', 'zh_CN':'User-Agent，匹配类型不可重复。'}
        self.ua_conditions = ua_conditions
        # {'en':'Request Method.
        # When the business scenario is API,this matching condition is not supported.', 'zh_CN':'请求方法，匹配类型不可重复。
        # 当业务场景为API业务时不支持此匹配条件。'}
        self.method_conditions = method_conditions
        # {'en':'Referer, match type cannot be repeated.', 'zh_CN':'Referer，匹配类型不可重复。'}
        self.referer_conditions = referer_conditions
        # {'en':'Request Header, match type can be repeated.', 'zh_CN':'请求头，匹配类型可重复。'}
        self.header_conditions = header_conditions
        # {'en':'Geo,match type cannot be repeated.', 'zh_CN':'区域，匹配类型不可重复。'}
        self.area_conditions = area_conditions
        # {'en':'Response Code, match type cannot be repeated.', 'zh_CN':'状态码，匹配类型不可重复。'}
        self.status_code_conditions = status_code_conditions
        # {'en':'HTTP/S, match type cannot be repeated.', 'zh_CN':'应用层协议，匹配类型不可重复。'}
        self.scheme_conditions = scheme_conditions

    def validate(self):
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        if self.method_conditions:
            for k in self.method_conditions:
                if k:
                    k.validate()
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()
        if self.area_conditions:
            for k in self.area_conditions:
                if k:
                    k.validate()
        if self.status_code_conditions:
            for k in self.status_code_conditions:
                if k:
                    k.validate()
        if self.scheme_conditions:
            for k in self.scheme_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.method_conditions is not None:
            result['methodConditions'] = []
            for k in self.method_conditions:
                result['methodConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        if self.area_conditions is not None:
            result['areaConditions'] = []
            for k in self.area_conditions:
                result['areaConditions'].append(k.to_map() if k else None)
        if self.status_code_conditions is not None:
            result['statusCodeConditions'] = []
            for k in self.status_code_conditions:
                result['statusCodeConditions'].append(k.to_map() if k else None)
        if self.scheme_conditions is not None:
            result['schemeConditions'] = []
            for k in self.scheme_conditions:
                result['schemeConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = UpdateSharedRateLimitingRuleIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = UpdateSharedRateLimitingRulePathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = UpdateSharedRateLimitingRuleUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = UpdateSharedRateLimitingRuleUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('methodConditions') is not None:
            self.method_conditions = []
            for k in m.get('methodConditions'):
                temp_model = UpdateSharedRateLimitingRuleRequestMethodCondition()
                self.method_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = UpdateSharedRateLimitingRuleRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = UpdateSharedRateLimitingRuleHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        if m.get('areaConditions') is not None:
            self.area_conditions = []
            for k in m.get('areaConditions'):
                temp_model = UpdateSharedRateLimitingRuleAreaCondition()
                self.area_conditions.append(temp_model.from_map(k))
        if m.get('statusCodeConditions') is not None:
            self.status_code_conditions = []
            for k in m.get('statusCodeConditions'):
                temp_model = UpdateSharedRateLimitingRuleStatusCodeCondition()
                self.status_code_conditions.append(temp_model.from_map(k))
        if m.get('schemeConditions') is not None:
            self.scheme_conditions = []
            for k in m.get('schemeConditions'):
                temp_model = UpdateSharedRateLimitingRuleSchemeCondition()
                self.scheme_conditions.append(temp_model.from_map(k))
        return self


class UpdateSharedRateLimitingRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        rule_name: str = None,
        description: str = None,
        statistical_item: str = None,
        statistics_key: str = None,
        statistical_period: int = None,
        trigger_threshold: int = None,
        intercept_time: int = None,
        effective_status: str = None,
        rate_limit_effective: UpdateSharedRateLimitingRuleRateLimitEffective = None,
        action: str = None,
        rate_limit_rule_condition: UpdateSharedRateLimitingRuleShareRateLimitRuleCondition = None,
    ):
        # {'en':'Rule ID.', 'zh_CN':'规则ID。'}
        self.id = id
        # {'en':'Rule Name, maximum 50 characters.
        # Does not support special characters and spaces.', 'zh_CN':'规则名称，最多50个字符。
        # 不支持特殊字符和空格。'}
        self.rule_name = rule_name
        # {'en':'Description, maximum 200 characters.', 'zh_CN':'规则描述，最多200个字符。'}
        self.description = description
        # {'en':'Client identifier.
        # IP:Client IP
        # IP_UA:Client IP and User-Agent
        # COOKIE:Cookie
        # IP_COOKIE:Client IP and Cookie
        # HEADER:Request Header
        # When there is a status code in the matching condition,this client identifier is not supported.
        # IP_HEADER:Client IP and Request Header
        # When there is a status code in the matching condition,this client identifier is not supported .', 'zh_CN':'统计粒度。
        # IP：客户端IP
        # IP_UA：客户端IP和User-Agent
        # COOKIE：Cookie
        # IP_COOKIE：客户端IP和Cookie
        # HEADER：请求头，当匹配条件中存在状态码时不支持此统计粒度
        # IP_HEADER：客户端IP和请求头，当匹配条件中存在状态码时不支持此统计粒度'}
        self.statistical_item = statistical_item
        # {'en':'Statistical key value.
        # When the client identifier is cookie/header value, the corresponding key value needs to be entered.', 'zh_CN':'统计key值。
        # 当统计粒度cookie/header值，需要输入对应的key值。'}
        self.statistics_key = statistics_key
        # {'en':'Statistics period, unit: seconds, the range is 1 - 3600.', 'zh_CN':'统计周期，单位：秒，范围为 1 - 3600。'}
        self.statistical_period = statistical_period
        # {'en':'Trigger threshold, unit: times.', 'zh_CN':'触发阈值，单位：次。'}
        self.trigger_threshold = trigger_threshold
        # {'en':'Action duration, unit: seconds, the range is 10 - 604800.', 'zh_CN':'处理动作持续时间，单位：秒，范围为 10 - 604800。'}
        self.intercept_time = intercept_time
        # {'en':'Cycle effective status.
        # PERMANENT:All time
        # WITHOUT:Excluded time
        # WITHIN:Selected time', 'zh_CN':'周期生效状态。
        # PERMANENT：永久生效
        # WITHOUT：周期内不生效
        # WITHIN：周期内生效'}
        self.effective_status = effective_status
        # {'en':'Effective time period.
        # When the effective status is effective within the cycle or not effective within the cycle, this field must have a value.', 'zh_CN':'规则生效周期。
        # 生效状态为周期内生效或周期内不生效时，此字段必须有值。'}
        self.rate_limit_effective = rate_limit_effective
        # {'en':'Action.
        # NO_USE:Not Used
        # LOG:Log
        # COOKIE:Cookie verification
        # JS_CHECK:Javascript verification
        # DELAY:Delay
        # BLOCK:Deny
        # RESET:Reset Connection
        # Custom response ID:Custom response ID
        # (When there is a status code in the matching condition, the supported actions are Log, Deny, and Reset Connection.)', 'zh_CN':'处理动作。
        # NO_USE：不使用
        # LOG：监控
        # COOKIE：Cookie校验
        # JS_CHECK：JavaScript校验
        # DELAY：延迟响应
        # BLOCK：拦截
        # RESET：断开连接
        # 自定义响应ID：自定义响应ID
        # 当匹配条件中存在状态码时，支持处理动作为监控、拦截、断开连接。'}
        self.action = action
        # {'en':'Matching conditions.', 'zh_CN':'匹配条件。'}
        self.rate_limit_rule_condition = rate_limit_rule_condition

    def validate(self):
        self.validate_required(self.id, 'id')
        if self.rate_limit_effective:
            self.rate_limit_effective.validate()
        if self.rate_limit_rule_condition:
            self.rate_limit_rule_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.statistical_item is not None:
            result['statisticalItem'] = self.statistical_item
        if self.statistics_key is not None:
            result['statisticsKey'] = self.statistics_key
        if self.statistical_period is not None:
            result['statisticalPeriod'] = self.statistical_period
        if self.trigger_threshold is not None:
            result['triggerThreshold'] = self.trigger_threshold
        if self.intercept_time is not None:
            result['interceptTime'] = self.intercept_time
        if self.effective_status is not None:
            result['effectiveStatus'] = self.effective_status
        if self.rate_limit_effective is not None:
            result['rateLimitEffective'] = self.rate_limit_effective.to_map()
        if self.action is not None:
            result['action'] = self.action
        if self.rate_limit_rule_condition is not None:
            result['rateLimitRuleCondition'] = self.rate_limit_rule_condition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('statisticalItem') is not None:
            self.statistical_item = m.get('statisticalItem')
        if m.get('statisticsKey') is not None:
            self.statistics_key = m.get('statisticsKey')
        if m.get('statisticalPeriod') is not None:
            self.statistical_period = m.get('statisticalPeriod')
        if m.get('triggerThreshold') is not None:
            self.trigger_threshold = m.get('triggerThreshold')
        if m.get('interceptTime') is not None:
            self.intercept_time = m.get('interceptTime')
        if m.get('effectiveStatus') is not None:
            self.effective_status = m.get('effectiveStatus')
        if m.get('rateLimitEffective') is not None:
            temp_model = UpdateSharedRateLimitingRuleRateLimitEffective()
            self.rate_limit_effective = temp_model.from_map(m['rateLimitEffective'])
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('rateLimitRuleCondition') is not None:
            temp_model = UpdateSharedRateLimitingRuleShareRateLimitRuleCondition()
            self.rate_limit_rule_condition = temp_model.from_map(m['rateLimitRuleCondition'])
        return self


class UpdateSharedRateLimitingRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateSharedRateLimitingRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedRateLimitingRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSharedRateLimitingRuleRequestHeader(TeaModel):
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


class UpdateSharedRateLimitingRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateShareCustomizeRuleRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
        domain_list: List[str] = None,
    ):
        # {"zh_CN":"共享规则ID。","en":"Share rule ID."}
        self.share_id = share_id
        # {"zh_CN":"待关联域名列表。","en":"List of hostname to be associated."}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.share_id, 'share_id')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['shareId'] = self.share_id
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class AssociateShareCustomizeRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AssociateShareCustomizeRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareCustomizeRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateShareCustomizeRuleRequestHeader(TeaModel):
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


class AssociateShareCustomizeRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateSharedWhitelistRuleIpOrIpsCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ip_or_ips: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals
        # NOT_EQUAL: Does not equal", "zh_CN":"匹配类型。
        # EQUAL：等于
        # NOT_EQUAL：不等于"}
        self.match_type = match_type
        # {"en":"IP/CIDR, maximum 500 IP/CIDR.", "zh_CN":"IP/IP段，最多500个IP/IP段。"}
        self.ip_or_ips = ip_or_ips

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ip_or_ips, 'ip_or_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ip_or_ips is not None:
            result['ipOrIps'] = self.ip_or_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ipOrIps') is not None:
            self.ip_or_ips = m.get('ipOrIps')
        return self


class CreateSharedWhitelistRulePathCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        paths: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, path case sensitive
        # NOT_EQUAL: Does not equal, path case sensitive
        # CONTAIN: Contains, path case insensitive
        # NOT_CONTAIN: Does not Contains, path case insensitive
        # REGEX: Regex match, path case insensitive
        # NOT_REGEX: Regular does not match, path case sensitive
        # START_WITH: Starts with, path case sensitive
        # END_WITH: Ends with, path case sensitive
        # WILDCARD: Wildcard matches, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character.
        # NOT_WILDCARD: Wildcard does not match, path case sensitive, ** represents zero or more arbitrary characters, ? represents any single character ", "zh_CN":"匹配类型。
        # EQUAL：等于，路径大小写敏感
        # NOT_EQUAL：不等于，路径大小写敏感
        # CONTAIN：包含，路径大小写不敏感
        # NOT_CONTAIN：不包含，路径大小写不敏感
        # REGEX：匹配正则，路径大小写不敏感
        # NOT_REGEX：正则不匹配，路径大小写不敏感
        # START_WITH：开头是，路径大小写不敏感
        # END_WITH：结尾是，路径大小写不敏感
        # WILDCARD：通配符匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，路径大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Path.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, path needs to start with "/", and no parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html.', 'zh_CN':'路径。
        # 当匹配类型为等于/不等于/开头是/结尾是，路径必须以“/”开头，不含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html。'}
        self.paths = paths

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.paths, 'paths')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.paths is not None:
            result['paths'] = self.paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('paths') is not None:
            self.paths = m.get('paths')
        return self


class CreateSharedWhitelistRuleUriCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        uri: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, URI case sensitive
        # NOT_EQUAL: Does not equal, URI case sensitive
        # CONTAIN: Contains, URI case insensitive
        # NOT_CONTAIN: Does not Contains, URI case insensitive
        # REGEX: Regex match, URI case insensitive
        # NOT_REGEX: Regular does not match, URI case insensitive
        # START_WITH: Starts with, URI case insensitive
        # END_WITH: Ends with, URI case insensitive
        # WILDCARD: Wildcard matches, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, URI case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，URI大小写敏感
        # NOT_EQUAL：不等于，URI大小写敏感
        # CONTAIN：包含，URI大小写不敏感
        # NOT_CONTAIN：不包含，URI大小写不敏感
        # REGEX：匹配正则，URI大小写不敏感
        # NOT_REGEX：正则不匹配，URI大小写不敏感
        # START_WITH：开头是，URI大小写不敏感
        # END_WITH：结尾是，URI大小写不敏感
        # WILDCARD：通配符匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，URI大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'URI.
        # When match type is EQUAL/NOT_EQUAL/START_WITH/END_WITH, uri needs to start with "/", and includes parameters.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: /test.html?id=1.', 'zh_CN':'URI。
        # 当匹配类型为等于/不等于/开头是/结尾是，URI必须以”/“开头，含参数。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：/test.html?id=1。'}
        self.uri = uri

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.uri, 'uri')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class CreateSharedWhitelistRuleUaCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        ua: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, user agent case sensitive
        # NOT_EQUAL: Does not equal, user agent case sensitive
        # CONTAIN: Contains, user agent case insensitive
        # NOT_CONTAIN: Does not Contains, user agent case insensitive
        # REGEX: Regex match, user agent case insensitive
        # NOT_REGEX: Regular does not match, user agent case insensitive
        # START_WITH: Starts with, user agent case insensitive
        # END_WITH: Ends with, user agent case insensitive
        # WILDCARD: Wildcard matches, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, user agent case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，User-Agent大小写敏感
        # NOT_EQUAL：不等于，User-Agent大小写敏感
        # CONTAIN：包含，User-Agent大小写不敏感
        # NOT_CONTAIN：不包含，User-Agent大小写不敏感
        # REGEX：匹配正则，User-Agent大小写不敏感
        # NOT_REGEX：正则不匹配，User-Agent大小写不敏感
        # START_WITH：开头是，User-Agent大小写不敏感
        # END_WITH：结尾是，User-Agent大小写不敏感
        # WILDCARD：通配符匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，User-Agent大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'User agent.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: go-Http-client/1.1.', 'zh_CN':'User-Agent。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：go-Http-client/1.1。'}
        self.ua = ua

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.ua, 'ua')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.ua is not None:
            result['ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('ua') is not None:
            self.ua = m.get('ua')
        return self


class CreateSharedWhitelistRuleRefererCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        referer: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, referer case sensitive
        # NOT_EQUAL: Does not equal, referer case sensitive
        # CONTAIN: Contains, referer case insensitive
        # NOT_CONTAIN: Does not Contains, referer case insensitive
        # REGEX: Regex match, referer case insensitive
        # NOT_REGEX: Regular does not match, referer case insensitive
        # START_WITH: Starts with, referer case insensitive
        # END_WITH: Ends with, referer case insensitive
        # WILDCARD: Wildcard matches, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single characte
        # NOT_WILDCARD: Wildcard does not match, referer case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，referer大小写敏感
        # NOT_EQUAL：不等于，referer大小写敏感
        # CONTAIN：包含，referer大小写不敏感
        # NOT_CONTAIN：不包含，referer大小写不敏感
        # REGEX：匹配正则，referer大小写不敏感
        # NOT_REGEX：正则不匹配，referer大小写不敏感
        # START_WITH：开头是，referer大小写不敏感
        # END_WITH：结尾是，referer大小写不敏感
        # WILDCARD：通配符匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，referer大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Referer.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed. 
        # Example: http://test.com.', 'zh_CN':'Referer。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。
        # 示例：http://test.com。'}
        self.referer = referer

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.referer, 'referer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.referer is not None:
            result['referer'] = self.referer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('referer') is not None:
            self.referer = m.get('referer')
        return self


class CreateSharedWhitelistRuleHeaderCondition(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # {"en":"Match type.
        # EQUAL: Equals, request header values case sensitive
        # NOT_EQUAL: Does not equal, request header values case sensitive
        # CONTAIN: Contains, request header values case insensitive
        # NOT_CONTAIN: Does not Contains, request header values case insensitive
        # REGEX: Regex match, request header values case insensitive
        # NOT_REGEX: Regular does not match, request header values case insensitive
        # START_WITH: Starts with, request header values case insensitive
        # END_WITH: Ends with, request header values case insensitive
        # WILDCARD: Wildcard matches, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character
        # NOT_WILDCARD: Wildcard does not match, request header values case insensitive, ** represents zero or more arbitrary characters, ? represents any single character", "zh_CN":"匹配类型。
        # EQUAL：等于，头部值大小写敏感
        # NOT_EQUAL：不等于，头部值大小写敏感
        # CONTAIN：包含，头部值大小写不敏感
        # NOT_CONTAIN：不包含，头部值大小写不敏感
        # REGEX：匹配正则，头部值大小写不敏感
        # NOT_REGEX：正则不匹配，头部值大小写不敏感
        # START_WITH：开头是，头部值大小写不敏感
        # END_WITH：结尾是，头部值大小写不敏感
        # WILDCARD：通配符匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符
        # NOT_WILDCARD：通配符不匹配，头部值大小写不敏感，*代表零个或多个任意字符，?代表任意单个字符"}
        self.match_type = match_type
        # {'en':'Header name,case insensitive,up to 100 characters.
        # Example: Accept.', 'zh_CN':'头部名称，大小写不敏感，最多100个字符。
        # 示例：Accept。'}
        self.key = key
        # {'en':'Header value.
        # When the match type is REGEX/NOT_REGEX, only one value is allowed.', 'zh_CN':'头部值。
        # 当匹配类型为正则/正则不匹配，则只允许只有一个值。'}
        self.value_list = value_list

    def validate(self):
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_list, 'value_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.key is not None:
            result['key'] = self.key
        if self.value_list is not None:
            result['valueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('valueList') is not None:
            self.value_list = m.get('valueList')
        return self


class CreateSharedWhitelistRuleWhitelistRuleCondition(TeaModel):
    def __init__(
        self,
        ip_or_ips_conditions: List[CreateSharedWhitelistRuleIpOrIpsCondition] = None,
        path_conditions: List[CreateSharedWhitelistRulePathCondition] = None,
        uri_conditions: List[CreateSharedWhitelistRuleUriCondition] = None,
        ua_conditions: List[CreateSharedWhitelistRuleUaCondition] = None,
        referer_conditions: List[CreateSharedWhitelistRuleRefererCondition] = None,
        header_conditions: List[CreateSharedWhitelistRuleHeaderCondition] = None,
    ):
        # {"en":"IP/CIDR match conditions, match type cannot be repeated.", "zh_CN":"IP/IP段匹配条件，匹配类型不可重复。"}
        self.ip_or_ips_conditions = ip_or_ips_conditions
        # {"en":"Path match conditions, match type cannot be repeated.", "zh_CN":"路径匹配条件，匹配类型不可重复。"}
        self.path_conditions = path_conditions
        # {"en":"URI match conditions, match type cannot be repeated.", "zh_CN":"URI匹配条件，匹配类型不可重复。"}
        self.uri_conditions = uri_conditions
        # {"en":"User agent match conditions, match type cannot be repeated.", "zh_CN":"User-Agent 匹配条件，匹配类型不可重复。"}
        self.ua_conditions = ua_conditions
        # {"en":"Referer match conditions, match type cannot be repeated.", "zh_CN":"Referer 匹配条件，匹配类型不可重复。"}
        self.referer_conditions = referer_conditions
        # {"en":"Request header match conditions.", "zh_CN":"请求头匹配条件。"}
        self.header_conditions = header_conditions

    def validate(self):
        if self.ip_or_ips_conditions:
            for k in self.ip_or_ips_conditions:
                if k:
                    k.validate()
        if self.path_conditions:
            for k in self.path_conditions:
                if k:
                    k.validate()
        if self.uri_conditions:
            for k in self.uri_conditions:
                if k:
                    k.validate()
        if self.ua_conditions:
            for k in self.ua_conditions:
                if k:
                    k.validate()
        if self.referer_conditions:
            for k in self.referer_conditions:
                if k:
                    k.validate()
        if self.header_conditions:
            for k in self.header_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_or_ips_conditions is not None:
            result['ipOrIpsConditions'] = []
            for k in self.ip_or_ips_conditions:
                result['ipOrIpsConditions'].append(k.to_map() if k else None)
        if self.path_conditions is not None:
            result['pathConditions'] = []
            for k in self.path_conditions:
                result['pathConditions'].append(k.to_map() if k else None)
        if self.uri_conditions is not None:
            result['uriConditions'] = []
            for k in self.uri_conditions:
                result['uriConditions'].append(k.to_map() if k else None)
        if self.ua_conditions is not None:
            result['uaConditions'] = []
            for k in self.ua_conditions:
                result['uaConditions'].append(k.to_map() if k else None)
        if self.referer_conditions is not None:
            result['refererConditions'] = []
            for k in self.referer_conditions:
                result['refererConditions'].append(k.to_map() if k else None)
        if self.header_conditions is not None:
            result['headerConditions'] = []
            for k in self.header_conditions:
                result['headerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipOrIpsConditions') is not None:
            self.ip_or_ips_conditions = []
            for k in m.get('ipOrIpsConditions'):
                temp_model = CreateSharedWhitelistRuleIpOrIpsCondition()
                self.ip_or_ips_conditions.append(temp_model.from_map(k))
        if m.get('pathConditions') is not None:
            self.path_conditions = []
            for k in m.get('pathConditions'):
                temp_model = CreateSharedWhitelistRulePathCondition()
                self.path_conditions.append(temp_model.from_map(k))
        if m.get('uriConditions') is not None:
            self.uri_conditions = []
            for k in m.get('uriConditions'):
                temp_model = CreateSharedWhitelistRuleUriCondition()
                self.uri_conditions.append(temp_model.from_map(k))
        if m.get('uaConditions') is not None:
            self.ua_conditions = []
            for k in m.get('uaConditions'):
                temp_model = CreateSharedWhitelistRuleUaCondition()
                self.ua_conditions.append(temp_model.from_map(k))
        if m.get('refererConditions') is not None:
            self.referer_conditions = []
            for k in m.get('refererConditions'):
                temp_model = CreateSharedWhitelistRuleRefererCondition()
                self.referer_conditions.append(temp_model.from_map(k))
        if m.get('headerConditions') is not None:
            self.header_conditions = []
            for k in m.get('headerConditions'):
                temp_model = CreateSharedWhitelistRuleHeaderCondition()
                self.header_conditions.append(temp_model.from_map(k))
        return self


class CreateSharedWhitelistRuleRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        description: str = None,
        conditions: CreateSharedWhitelistRuleWhitelistRuleCondition = None,
    ):
        # {"en":"Rule name, maximum 50 characters.
        #  Does not support special characters and spaces.", "zh_CN":"规则名称，最多50个字符。
        # 不支持特殊字符和空格。"}
        self.rule_name = rule_name
        # {"en":"Description, maximum 200 characters.", "zh_CN":"描述，最多200个字符。"}
        self.description = description
        # {"en":"Match conditions, at least one, at most five.", "zh_CN":"匹配条件，至少一个，至多五个。"}
        self.conditions = conditions

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.conditions, 'conditions')
        if self.conditions:
            self.conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.description is not None:
            result['description'] = self.description
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('conditions') is not None:
            temp_model = CreateSharedWhitelistRuleWhitelistRuleCondition()
            self.conditions = temp_model.from_map(m['conditions'])
        return self


class CreateSharedWhitelistRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Rule ID.", "zh_CN":"规则ID。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateSharedWhitelistRulePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedWhitelistRuleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSharedWhitelistRuleRequestHeader(TeaModel):
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


class CreateSharedWhitelistRuleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




