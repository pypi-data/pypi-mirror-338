# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ControlResourceClusterRequestParam(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        code: str = None,
    ):
        # {"en":"The policy id", "zh_CN":"策略id"}
        self.policy_id = policy_id
        # {"en":"The start stop code 1111 consists of four digits of 0 or 1, representing the primary source, primary backup source, secondary backup source, and tertiary backup source. 0 is disabled and 1 is enabled. For example, if only the primary backup source needs to be disabled, code=1011, both the primary source and the tertiary backup source need to be disabled. code=0110. If the backup source does not exist, it is defaulted to 1", "zh_CN":"启停代码 1111 四位0或1的数字代表主源 一级备源 二级备源 三级备源  0 停用 1 启用  例如 需要只停用一级备 code=1011  需要同时停用主源和三级备 code=0110  如果备源不存在则默认补1"}
        self.code = code

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class ControlResourceClusterRequest(TeaModel):
    def __init__(
        self,
        param: List[ControlResourceClusterRequestParam] = None,
    ):
        self.param = param

    def validate(self):
        self.validate_required(self.param, 'param')
        if self.param:
            for k in self.param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['param'] = []
            for k in self.param:
                result['param'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('param') is not None:
            self.param = []
            for k in m.get('param'):
                temp_model = ControlResourceClusterRequestParam()
                self.param.append(temp_model.from_map(k))
        return self


class ControlResourceClusterResponseContent(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlResourceClusterResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: List[ControlResourceClusterResponseContent] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"Response message", "zh_CN":"返回说明"}
        self.msg = msg
        # {"en":"return data", "zh_CN":"返回值"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = ControlResourceClusterResponseContent()
                self.content.append(temp_model.from_map(k))
        return self


class ControlResourceClusterPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlResourceClusterParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlResourceClusterRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlResourceClusterResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ControlDispatchPolicyRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        policy_ids: str = None,
        type: int = None,
        language: str = None,
    ):
        # {"en":"Domain that the dispatch policy to be operated on belongs to", "zh_CN":"要操作调度策略所属的域名"}
        self.domain_id = domain_id
        # {"en":"ID of the dispatch policy to be operated on Use English half-width semicolon between two policies if there are multiple to be operated on.", "zh_CN":"要删除的调度策略ID
        # 如果需要删除多个策略，用英文半角分号分隔。"}
        self.policy_ids = policy_ids
        # {"en":"Operation type 0 means to enable policies; 1 means to disable policies", "zh_CN":"操作类型：0表示启用策略；1表示停用策略"}
        self.type = type
        # {"en":"Operation type 0 means to enable policies; 1 means to disable policies", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.policy_ids, 'policy_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_ids is not None:
            result['policyIds'] = self.policy_ids
        if self.type is not None:
            result['type'] = self.type
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyIds') is not None:
            self.policy_ids = m.get('policyIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ControlDispatchPolicyResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: dict = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"policyId:The dispatch policy ID, used to identify the newly added dispatch policy", "zh_CN":"policyId调度策略ID，用于标识调度策略"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ControlDispatchPolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDispatchPoliciesRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        start: int = None,
        limit: int = None,
        language: str = None,
    ):
        # {"en":"Domain that the dispatch policy to be edited belongs to", "zh_CN":"要查询调度策略所属的域名"}
        self.domain_id = domain_id
        # {"en":"Query inital records by page", "zh_CN":"分页查询起始记录"}
        self.start = start
        # {"en":"Number if quried items by page", "zh_CN":"分页查询条数"}
        self.limit = limit
        # {"en":"Number if quried items by page", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.start, 'start')
        self.validate_required(self.limit, 'limit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.start is not None:
            result['start'] = self.start
        if self.limit is not None:
            result['limit'] = self.limit
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class QueryDispatchPoliciesResponseView(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesResponseMonitor(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesResponseWarning(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesResponse(TeaModel):
    def __init__(
        self,
        policy_desc: str = None,
        policy_type: int = None,
        domain_id: int = None,
        view: QueryDispatchPoliciesResponseView = None,
        rate: int = None,
        monitor: QueryDispatchPoliciesResponseMonitor = None,
        warning: QueryDispatchPoliciesResponseWarning = None,
        policy_resource: List[str] = None,
        release: List[str] = None,
    ):
        # {"en":"Policy description", "zh_CN":"策略描述"}
        self.policy_desc = policy_desc
        # {"en":"Policy type, 0: Load balance+primary and redundant, 1: Load balance", "zh_CN":"策略类型，0:负载均衡+主备,1:负载均衡"}
        self.policy_type = policy_type
        # {"en":"Domain ID", "zh_CN":"域名ID标识"}
        self.domain_id = domain_id
        # {"en":"Line information type Line type, 0: Standard line, 1: Custom Line viewId  Line ID, field required when the line type is 0 viewCn  Line in Chinese, field required when the line type is 0 userView Custom line, field required when the line type is 1 viewTag Custom line tag viewMembers Actual lines contained in the custom line viewId Line ID viewCn Line in Chinese", "zh_CN":"线路信息：
        # type 线路类型， 0:标准线路,1:自定义线路
        # 
        # viewId 线路ID  线路类型为0时选项
        # 
        # viewCn线路中文  线路类型为0时选项
        # 
        # viewEn线路英文  线路类型为0时选项
        # 
        # userView 自定义线路  线路类型为1时选项
        # 
        # viewTag自定义线路标签
        # 
        # viewMembers 自定义线路包含的实际线路
        # 
        # viewId线路ID
        # 
        # viewCn 线路中文"}
        self.view = view
        # {"en":"Call frequency Unit is minute(1,2,5,10,30,60)", "zh_CN":"调度频率
        # 以分钟为单位， 可选值1、2、5、10、30、60"}
        self.rate = rate
        # {"en":"Monitor type monitorType Monitor type  0 http, 1 https, 2 udp(not supported presently), 3 tcp, 4 ping monitorNodes Monitor nodes isp ISP of monitor nodes area Area of monitor nodes path Monitor path, options are available when the monitor types are http and https.  port Monitor port, options are available when the monitor types are http, https and tcp.  responseTimeout Reponse timeout time, unit is second. Options are available when the monitor types are http and https.  excludedCodes Excluded status codes. Options are available when the monitor types are http and https. Use semicolon to separate when there are multiple status codes packetLossLimit Packet loss ratio, available when the monitor type is ping.  delayLimit Time delay, unit is millisecond. Available when the monitor type is ping.", "zh_CN":"监控配置：
        # monitorType 监控类型，0 http 1 https 2 udp(暂不支持) 3 tcp 4 ping
        # 
        # monitorNodes 监控节点
        # 
        # isp 监控节点运营商
        # 
        # area 监控节点区域
        # 
        # path 监控路径，当监控方式为http,https 时选项
        # 
        # port监控端口，当监控方式为http,https,tcp 时选项
        # 
        # responseTimeout响应超时时间，单位：秒，当监控方式为http,https时选项
        # 
        # excludedCodes状态排除码，当监控方式为http,https 时选项，多个状态码用英文分号分隔
        # 
        # httpMethod 监控方式为http/https时支持，可选值：0 默认请求方法 1 post请求
        # 
        # requestData 监控方式为http/https时支持，httpMethod为1时 必填(可为空串)
        # 
        # packetLossLimit 丢包率，当监控方式为ping时选项
        # 
        # delayLimit时延，单位：毫秒，当监控方式为ping时选项"}
        self.monitor = monitor
        # {"en":"Warning configurations warnMethod Warning type,1 Warn with email warnInterval How long will the warning last, unit: minute warnEmail The Email box to receive warning messages. Use English semicolon to separate two if there are multiple email boxes exist", "zh_CN":"告警配置：
        # warnMethod告警方式， 1 邮件告警
        # 
        # warnInterval连续告警提醒周期，单位：分钟
        # 
        # warnEmail 告警邮箱，多个邮箱以英文分号分隔"}
        self.warning = warning
        # {"en":"Policy resources partType Resource type, 0 Primary DNS 1 Level-one redundancy 2 Level-two redundancy 3 Level-three redundancy type Resource record type, 0 A record 1 CNAME value Resource record value loadRatio Ratio", "zh_CN":"策略资源：
        # partType资源类型， 0 主解析资源 1 一级备 2 二级备 3 三级备
        # 
        # type 资源记录类型， 0 A记录 1 CNAME
        # 
        # value 资源记录值
        # 
        # loadRatio 比例"}
        self.policy_resource = policy_resource
        # {"en":"DNS details(if release node does not exist or is empty, it means the current policy has not been released) spType Type of the service provider  0 Primary DNS 1 Level-one redundancy 2 Leveltwo redundancy 3 Level-three redundancy spList Resource list of service providers load Load ratio value Resource record value.", "zh_CN":"解析情况(release节点不存在或为空，表示当前策略尚未发布解析 )
        # spType 服务提供者类型 0 主解析资源 1 一级备 2 二级备 3 三级备
        # 
        # spList 服务提供资源列表
        # 
        # load 负载比例
        # 
        # value 资源记录值"}
        self.release = release

    def validate(self):
        self.validate_required(self.policy_desc, 'policy_desc')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.view, 'view')
        if self.view:
            self.view.validate()
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.monitor, 'monitor')
        if self.monitor:
            self.monitor.validate()
        self.validate_required(self.warning, 'warning')
        if self.warning:
            self.warning.validate()
        self.validate_required(self.policy_resource, 'policy_resource')
        self.validate_required(self.release, 'release')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_desc is not None:
            result['policyDesc'] = self.policy_desc
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.view is not None:
            result['view'] = self.view.to_map()
        if self.rate is not None:
            result['rate'] = self.rate
        if self.monitor is not None:
            result['monitor'] = self.monitor.to_map()
        if self.warning is not None:
            result['warning'] = self.warning.to_map()
        if self.policy_resource is not None:
            result['policyResource'] = self.policy_resource
        if self.release is not None:
            result['release'] = self.release
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDesc') is not None:
            self.policy_desc = m.get('policyDesc')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('view') is not None:
            temp_model = QueryDispatchPoliciesResponseView()
            self.view = temp_model.from_map(m['view'])
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('monitor') is not None:
            temp_model = QueryDispatchPoliciesResponseMonitor()
            self.monitor = temp_model.from_map(m['monitor'])
        if m.get('warning') is not None:
            temp_model = QueryDispatchPoliciesResponseWarning()
            self.warning = temp_model.from_map(m['warning'])
        if m.get('policyResource') is not None:
            self.policy_resource = m.get('policyResource')
        if m.get('release') is not None:
            self.release = m.get('release')
        return self


class QueryDispatchPoliciesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SaveDispatchPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_desc: str = None,
        policy_type: int = None,
        domain_id: int = None,
        view: dict = None,
        rate: int = None,
        monitor: dict = None,
        warning: dict = None,
        policy_resource: List[str] = None,
        language: str = None,
    ):
        # {"en":"Policy description Less than 200 characters", "zh_CN":"策略描述
        # 小于200字符"}
        self.policy_desc = policy_desc
        # {"en":"Policy type 0: Load balance+primary and redundant, 1: Load balance", "zh_CN":"策略类型
        # 0:负载均衡+主备,1:负载均衡"}
        self.policy_type = policy_type
        # {"en":"Domain ID", "zh_CN":"域名ID标识"}
        self.domain_id = domain_id
        # {"en":"Line information. Entry rules: type Line type, optional field. Options: 0: Standard line, 1: Custom Line. The default value is Standard line customId ID of the custom line, available and required when the type value is 1 More details about the related table of lines can be found in Appendix II Relations of ViewID and Lines viewId Line ID, available and required when the type value is 0 viewCn Line in Chinese, available and required when the type value is 0", "zh_CN":"线路信息。
        # 填写规则：
        # 
        # type 线路类型，可选，可选值0 标准线路  1 自定义线路。默认值为标准线路
        # 
        # customId 自定义线路ID , type值为1时选项，必填
        # 
        # 线路的对应表请参考附录“附录2 ViewID与线路的对应关系”
        # 
        # viewId 线路ID，type值为0时选项，必填
        # 
        # viewCn线路中文，type值为0时选项，必填"}
        self.view = view
        # {"en":"Call frequency Unit is minute(1,2,5,10,30,60)", "zh_CN":"调度频率
        # 以分钟为单位， 可选值1、2、5、10、30、60"}
        self.rate = rate
        # {"en":"Monitor configurations. Entry rules: monitorType Monitor type, required. Optional values: 0 http, 1 https, 2 udp(not supported presently), 3 tcp, 4 ping monitorNodes Monitor nodes, required isp ISP of monitor nodes area Area of monitor nodes path Monitor path, options are available and required when the monitor types are http and https. Length should be less than 255 port Monitor port, options are available and required when the monitor types are http, https and tcp. Value range is 1-65535. responseTimeout Reponse timeout time, unit is second. Options are available and required when the monitor types are http and https. Value range is 1-20 excludedCodes Excluded status codes. Options are available and optional when the monitor types are http and https. Use semicolon to separate when there are multiple status codes packetLossLimit Packet loss ratio, available when the monitor type is ping. Optional field. Either packet loss ratio or time delay has to be entered delayLimit Time delay, unit is millisecond. Available when the monitor type is ping. Optional field. Either packet loss ratio or time delay has to be entered", "zh_CN":"监控配置。
        # 填写规则：
        # 
        # monitorType 监控类型，必填，可选值0 http 1 https 2 udp(暂不支持) 3 tcp 4 ping
        # 
        # monitorNodes 监控节点，必填
        # 
        # isp 监控节点运营商
        # 
        # area 监控节点区域
        # 
        # path 监控路径，当监控方式为http,https 时选项，必填， 长度不超过255
        # 
        # port监控端口，当监控方式为http,https,tcp 时选项，必填，取值范围 1~65535
        # 
        # responseTimeout响应超时时间，单位：秒，当监控方式为http,https时选项，必填，1 ~ 20
        # 
        # excludedCodes状态排除码，当监控方式为http,https 时选项，选填，多个状态码用英文分号分隔
        # 
        # httpMethod 监控方式为httptps时支持，可选值：0 默认请求方法 1 post请求
        # 
        # requestData 监控方式为httptps时支持，httpMethod为1时 必填(可为空串)
        # 
        # packetLossLimit 丢包率，当监控方式为ping时选项，选填，但丢包率和时延至少填一项
        # 
        # delayLimit时延，单位：毫秒，当监控方式为ping时选项，选填，但丢包率和时延至少填一项"}
        self.monitor = monitor
        # {"en":"Warning configurations. Entry rules: warnMethod Warning type, required filed, 1 Warn with email warnInterval How long will the warning last, unit: minutes. This filed is complusory when the warn type is 0. Warning duration>=call frequency duration warnEmail The email box to receive warning messages, and this field is required if the warn type is 1. Use English semicolon to separate two if there are multiple email boxes exist", "zh_CN":"告警配置。
        # 填写规则：
        # 
        # warnMethod告警方式，必填，1 邮件告警
        # 
        # warnInterval连续告警提醒周期，单位：分钟，告警方式不为0时必填，告警提醒周期>=调度频率周期
        # 
        # warnEmail 告警邮箱，告警方式为1时必填，多个邮箱以英文分号分隔"}
        self.warning = warning
        # {"en":"Policy resources. Entry rules: partType Resource type, field required, optional values: 0 Primary DNS 1 Levelone redundancy 2 Level-two redundancy 3 Level-three redundancy type Resource record type, field required; optional values: 0 A record 1 CNAME value Resource record value, field required  loadRatio Ratio, field required Primary resource has to be entered. When lower levels of redundancies exist, higher levels cannot be empty. When the policy type is load balance+primary and redundancy, the redundant resource cannot be empty. When the policy type is load balance, the entered redundant resource is invalid. No duplicate values of policy resources are allowed", "zh_CN":"策略资源。
        # 填写规则：
        # 
        # partType资源类型，必填，可选值： 0 主解析资源 1 一级备 2 二级备 3 三级备
        # 
        # type 资源记录类型，必填，可选值：0 A记录 1 CNAME
        # 
        # value 资源记录值，必填
        # 
        # loadRatio 比例，必填
        # 
        # 必须填写主资源。
        # 
        # 当有更低级备资源时，较高级备资源不能为空。
        # 
        # 当策略类型为负载均衡+主备时，备资源不能为空。
        # 
        # 当策略类型为负载均衡时，填写的备资源无效。
        # 
        # 策略资源值不能重复"}
        self.policy_resource = policy_resource
        # {"en":"Policy resources. Entry rules: partType Resource type, field required, optional values: 0 Primary DNS 1 Levelone redundancy 2 Level-two redundancy 3 Level-three redundancy type Resource record type, field required; optional values: 0 A record 1 CNAME value Resource record value, field required  loadRatio Ratio, field required Primary resource has to be entered. When lower levels of redundancies exist, higher levels cannot be empty. When the policy type is load balance+primary and redundancy, the redundant resource cannot be empty. When the policy type is load balance, the entered redundant resource is invalid. No duplicate values of policy resources are allowed", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.view, 'view')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.monitor, 'monitor')
        self.validate_required(self.warning, 'warning')
        self.validate_required(self.policy_resource, 'policy_resource')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_desc is not None:
            result['policyDesc'] = self.policy_desc
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.view is not None:
            result['view'] = self.view
        if self.rate is not None:
            result['rate'] = self.rate
        if self.monitor is not None:
            result['monitor'] = self.monitor
        if self.warning is not None:
            result['warning'] = self.warning
        if self.policy_resource is not None:
            result['policyResource'] = self.policy_resource
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDesc') is not None:
            self.policy_desc = m.get('policyDesc')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('view') is not None:
            self.view = m.get('view')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('monitor') is not None:
            self.monitor = m.get('monitor')
        if m.get('warning') is not None:
            self.warning = m.get('warning')
        if m.get('policyResource') is not None:
            self.policy_resource = m.get('policyResource')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class SaveDispatchPolicyResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: dict = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"policyId scheduling policy ID", "zh_CN":"policyId调度策略ID，用于标识新增的调度策略"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class SaveDispatchPolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaveDispatchPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaveDispatchPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaveDispatchPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDispatchPolicyDetailRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        policy_id: int = None,
        language: str = None,
    ):
        # {"en":"Domain ID", "zh_CN":"域名ID"}
        self.domain_id = domain_id
        # {"en":"PolicyID", "zh_CN":"策略ID"}
        self.policy_id = policy_id
        # {"en":"PolicyID", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.policy_id, 'policy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class QueryDispatchPolicyDetailResponse(TeaModel):
    def __init__(
        self,
        policy_desc: str = None,
        policy_type: int = None,
        domain_id: int = None,
        view: dict = None,
        rate: int = None,
        monitor: dict = None,
        warning: dict = None,
        policy_resource: List[str] = None,
    ):
        # {"en":"Policy description", "zh_CN":"策略描述"}
        self.policy_desc = policy_desc
        # {"en":"Policy type, 0: Load balance+primary and redundant, 1: Load balance", "zh_CN":"策略类型，0:负载均衡+主备,1:负载均衡"}
        self.policy_type = policy_type
        # {"en":"Domain ID", "zh_CN":"域名ID标识"}
        self.domain_id = domain_id
        # {"en":"Line information type Line type, 0: Standard line, 1: Custom Line viewId  Line ID, field required when the line type is 0 viewCn  Line in Chinese, field required when the line type is 0 userView Custom line, field required when the line type is 1 viewTag Custom line tag viewMembers Actual lines contained in the custom line viewId Line ID viewCn Line in Chinese", "zh_CN":"线路信息：
        # type 线路类型， 0:标准线路,1:自定义线路
        # 
        # viewId 线路ID  线路类型为0时选项
        # 
        # viewCn线路中文  线路类型为0时选项
        # 
        # viewEn线路英文  线路类型为0时选项
        # 
        # userView 自定义线路  线路类型为1时选项
        # 
        # viewTag自定义线路标签
        # 
        # viewMembers 自定义线路包含的实际线路
        # 
        # viewId线路ID
        # 
        # viewCn 线路中文"}
        self.view = view
        # {"en":"Call frequency Unit is minute(1,2,5,10,30,60)", "zh_CN":"调度频率
        # 以分钟为单位， 可选值1、2、5、10、30、60"}
        self.rate = rate
        # {"en":"Monitor type monitorType Monitor type  0 http, 1 https, 2 udp(not supported presently), 3 tcp, 4 ping monitorNodes Monitor nodes isp ISP of monitor nodes area Area of monitor nodes path Monitor path, options are available when the monitor types are http and https.  port Monitor port, options are available when the monitor types are http, https and tcp.  responseTimeout Reponse timeout time, unit is second. Options are available when the monitor types are http and https.  excludedCodes Excluded status codes. Options are available when the monitor types are http and https. Use semicolon to separate when there are multiple status codes packetLossLimit Packet loss ratio, available when the monitor type is ping.  delayLimit Time delay, unit is millisecond. Available when the monitor type is ping.", "zh_CN":"监控配置：
        # monitorType 监控类型，0 http 1 https 2 udp(暂不支持) 3 tcp 4 ping
        # 
        # monitorNodes 监控节点
        # 
        # isp 监控节点运营商
        # 
        # area 监控节点区域
        # 
        # path 监控路径，当监控方式为http,https 时选项
        # 
        # port监控端口，当监控方式为http,https,tcp 时选项
        # 
        # responseTimeout响应超时时间，单位：秒，当监控方式为http,https时选项
        # 
        # excludedCodes状态排除码，当监控方式为http,https 时选项，多个状态码用英文分号分隔
        # 
        # httpMethod 监控方式为http/https时支持，可选值：0 默认请求方法 1 post请求
        # 
        # requestData 监控方式为http/https时支持，httpMethod为1时 必填(可为空串)
        # 
        # packetLossLimit 丢包率，当监控方式为ping时选项
        # 
        # delayLimit时延，单位：毫秒，当监控方式为ping时选项"}
        self.monitor = monitor
        # {"en":"Warning configurations warnMethod Warning type,1 Warn with email warnInterval How long will the warning last, unit: minute warnEmail The Email box to receive warning messages. Use English semicolon to separate two if there are multiple email boxes exist", "zh_CN":"告警配置：
        # warnMethod告警方式， 1 邮件告警
        # 
        # warnInterval连续告警提醒周期，单位：分钟
        # 
        # warnEmail 告警邮箱，多个邮箱以英文分号分隔"}
        self.warning = warning
        # {"en":"Policy resources partType Resource type, 0 Primary DNS 1 Level-one redundancy 2 Level-two redundancy 3 Level-three redundancy type Resource record type, 0 A record 1 CNAME value Resource record value loadRatio Ratio", "zh_CN":"策略资源：
        # partType资源类型， 0 主解析资源 1 一级备 2 二级备 3 三级备
        # 
        # type 资源记录类型， 0 A记录 1 CNAME
        # 
        # value 资源记录值
        # 
        # loadRatio 比例"}
        self.policy_resource = policy_resource

    def validate(self):
        self.validate_required(self.policy_desc, 'policy_desc')
        self.validate_required(self.policy_type, 'policy_type')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.view, 'view')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.monitor, 'monitor')
        self.validate_required(self.warning, 'warning')
        self.validate_required(self.policy_resource, 'policy_resource')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_desc is not None:
            result['policyDesc'] = self.policy_desc
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.view is not None:
            result['view'] = self.view
        if self.rate is not None:
            result['rate'] = self.rate
        if self.monitor is not None:
            result['monitor'] = self.monitor
        if self.warning is not None:
            result['warning'] = self.warning
        if self.policy_resource is not None:
            result['policyResource'] = self.policy_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDesc') is not None:
            self.policy_desc = m.get('policyDesc')
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('view') is not None:
            self.view = m.get('view')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('monitor') is not None:
            self.monitor = m.get('monitor')
        if m.get('warning') is not None:
            self.warning = m.get('warning')
        if m.get('policyResource') is not None:
            self.policy_resource = m.get('policyResource')
        return self


class QueryDispatchPolicyDetailPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPolicyDetailParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPolicyDetailRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchPolicyDetailResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DelDispatchPolicyRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        policy_ids: str = None,
        language: str = None,
    ):
        # {"en":"Domain that the dispatch policy to be deleted belongs to", "zh_CN":"要删除调度策略所属的域名"}
        self.domain_id = domain_id
        # {"en":"ID of the dispatch policy to be deleted Use English half-width semicolon between two policies if there are multiple to be deleted.", "zh_CN":"要删除的调度策略ID
        # 如果需要删除多个策略，用英文半角分号分隔。"}
        self.policy_ids = policy_ids
        # {"en":"ID of the dispatch policy to be deleted Use English half-width semicolon between two policies if there are multiple to be deleted.", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.policy_ids, 'policy_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_ids is not None:
            result['policyIds'] = self.policy_ids
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyIds') is not None:
            self.policy_ids = m.get('policyIds')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class DelDispatchPolicyResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"Return PolicyID", "zh_CN":"返回策略ID"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class DelDispatchPolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ControlDispatchResourceRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        policy_id: int = None,
        value: str = None,
        operate: int = None,
        language: int = None,
    ):
        # {"en":"The domain id", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"The policy id", "zh_CN":"策略id"}
        self.policy_id = policy_id
        # {"en":"The resource value to operate (for example: 192.168.0.1 or xxxx.com)", "zh_CN":"要操作的资源值（例如:192.168.0.1或者xxxx.com）"}
        self.value = value
        # {"en":"The operation type, where 1 indicates the activation of resources and 0 indicates the deactivation of resources.", "zh_CN":"操作类型，1表示启用资源；0表示停用资源"}
        self.operate = operate
        # {"en":"If it is empty, the Chinese result will be returned by default; otherwise, the English prompt result will be returned.", "zh_CN":"为空返回中文结果(默认)，en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.value, 'value')
        self.validate_required(self.operate, 'operate')
        self.validate_required(self.language, 'language')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.value is not None:
            result['value'] = self.value
        if self.operate is not None:
            result['operate'] = self.operate
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ControlDispatchResourceResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: int = None,
    ):
        # {"en":"The status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"Message", "zh_CN":"详细说明"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ControlDispatchResourcePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchResourceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchResourceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchResourceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




