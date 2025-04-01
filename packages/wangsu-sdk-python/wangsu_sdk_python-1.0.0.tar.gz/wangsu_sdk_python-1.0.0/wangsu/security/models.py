# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class EditSecurityGroupRulesSecurityGroupRuleParam(TeaModel):
    def __init__(
        self,
        id: str = None,
        direct: str = None,
        policy: str = None,
        protocol: str = None,
        ethertype: str = None,
        priority: int = None,
        port_range_max: int = None,
        port_range_min: int = None,
        remote_ip_perfix: str = None,
        remark: str = None,
    ):
        # {"en":"Security Group id", "zh_CN":"规则id"}
        self.id = id
        # {"en":"Rule direction:INGRESS;EGRESS", "zh_CN":"规则方向： INGRESS-流入 EGRESS-流出"}
        self.direct = direct
        # {"en":"Authorization policy:ACCEPT;DROP", "zh_CN":"授权策略： ACCEPT-允许 DROP-拒绝"}
        self.policy = policy
        # {"en":"Protocol type: TCP/UDP/ICMP.
        # When selecting ICMP, the maximum/minimum port numbers below cannot be specified.
        # ", "zh_CN":"协议类型：TCP/UDP/ICMP 选择ICMP时，不能指定下方的最大/最小端口号"}
        self.protocol = protocol
        # {"en":"IP protocol:4-IPv4  6-IPv6", "zh_CN":"IP协议： 4-IPv4 6-IPv6"}
        self.ethertype = ethertype
        # {"en":"Priority: 1-100, higher the value, higher the priority", "zh_CN":"优先级：取值范围1-100，值越大优先级越高"}
        self.priority = priority
        # {"en":"The maximum port number.
        # 1) Value 1-65535 and greater than or equal to the minimum port number.
        # 2) When specifying a specific port, the maximum and minimum port numbers should be equal.
        # ", "zh_CN":"最大的端口号
        # 1）取值1-65535且大于等于最小端口号
        # 2）当要指定某个特定端口时，最大和最小端口号取值相等即可"}
        self.port_range_max = port_range_max
        # {"en":"The minimum port number.
        # 1) Value 1-65535 and less than or equal to the maximum port number.
        # 2) When specifying a specific port, the maximum and minimum port numbers should be equal.
        # ", "zh_CN":"最小的端口号
        # 1）取值1-65535且小于等于最大端口号
        # 2）当要指定某个特定端口时，最大和最小端口号取值相等即可'"}
        self.port_range_min = port_range_min
        # {"en":"Authorization object: The IP or CIDR that matches the security group rules.
        # 1) Only a single IP or CIDR can be specified.
        # 2) The specified IP or CIDR must match the IP protocol type mentioned above.
        # ", "zh_CN":"授权对象：匹配该安全组规则的ip或cidr
        # 1）只能指定单个IP或CIDR
        # 2）指定的IP或CIDR必须和上述的IP协议类型一致'"}
        self.remote_ip_perfix = remote_ip_perfix
        # {"en":"Notes,cannot exceed 255 characters", "zh_CN":"备注信息（可选），不能超过255个字符"}
        self.remark = remark

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.direct, 'direct')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ethertype, 'ethertype')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.remote_ip_perfix, 'remote_ip_perfix')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.direct is not None:
            result['direct'] = self.direct
        if self.policy is not None:
            result['policy'] = self.policy
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.priority is not None:
            result['priority'] = self.priority
        if self.port_range_max is not None:
            result['portRangeMax'] = self.port_range_max
        if self.port_range_min is not None:
            result['portRangeMin'] = self.port_range_min
        if self.remote_ip_perfix is not None:
            result['remoteIpPerfix'] = self.remote_ip_perfix
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('portRangeMax') is not None:
            self.port_range_max = m.get('portRangeMax')
        if m.get('portRangeMin') is not None:
            self.port_range_min = m.get('portRangeMin')
        if m.get('remoteIpPerfix') is not None:
            self.remote_ip_perfix = m.get('remoteIpPerfix')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class EditSecurityGroupRulesRequest(TeaModel):
    def __init__(
        self,
        security_group_rule: List[EditSecurityGroupRulesSecurityGroupRuleParam] = None,
    ):
        self.security_group_rule = security_group_rule

    def validate(self):
        self.validate_required(self.security_group_rule, 'security_group_rule')
        if self.security_group_rule:
            for k in self.security_group_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_rule is not None:
            result['securityGroupRule'] = []
            for k in self.security_group_rule:
                result['securityGroupRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupRule') is not None:
            self.security_group_rule = []
            for k in m.get('securityGroupRule'):
                temp_model = EditSecurityGroupRulesSecurityGroupRuleParam()
                self.security_group_rule.append(temp_model.from_map(k))
        return self


class EditSecurityGroupRulesResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupRulesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupRulesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddSecurityGroupRulesSecurityGroupRuleParam(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        direct: str = None,
        policy: str = None,
        protocol: str = None,
        ethertype: str = None,
        priority: int = None,
        port_range_max: int = None,
        port_range_min: int = None,
        remote_ip_perfix: str = None,
        remark: str = None,
    ):
        # {"en":"Security Group id", "zh_CN":"安全组id"}
        self.security_group_id = security_group_id
        # {"en":"Rule direction:INGRESS;EGRESS", "zh_CN":"规则方向：
        # INGRESS-流入
        # EGRESS-流出"}
        self.direct = direct
        # {"en":"Authorization policy:ACCEPT;DROP", "zh_CN":"授权策略：
        # ACCEPT-允许
        # DROP-拒绝"}
        self.policy = policy
        # {"en":"Protocol type: TCP/UDP/ICMP.
        # When selecting ICMP, the maximum/minimum port numbers below cannot be specified.", "zh_CN":"协议类型：TCP/UDP/ICMP
        # 选择ICMP时，不能指定下方的最大/最小端口号"}
        self.protocol = protocol
        # {"en":"IP protocol:
        # 4-IPv4
        # 6-IPv6", "zh_CN":"IP协议：
        # 4-IPv4
        # 6-IPv6"}
        self.ethertype = ethertype
        # {"en":"Priority: 1-100, higher the value, higher the priority", "zh_CN":"优先级：取值范围1-100，值越大优先级越高"}
        self.priority = priority
        # {"en":"The maximum port number.
        # 1) Value 1-65535 and greater than or equal to the minimum port number.
        # 2) When specifying a specific port, the maximum and minimum port numbers should be equal.",
        # "zh_CN":"最大的端口号
        # 1）取值1-65535且大于等于最小端口号
        # 2）当要指定某个特定端口时，最大和最小端口号取值相等即可"}
        self.port_range_max = port_range_max
        # {"en":"The minimum port number.
        # 1) Value 1-65535 and less than or equal to the maximum port number.
        # 2) When specifying a specific port, the maximum and minimum port numbers should be equal.
        # ", "zh_CN":"最小的端口号
        # 1）取值1-65535且小于等于最大端口号
        # 2）当要指定某个特定端口时，最大和最小端口号取值相等即可"}
        self.port_range_min = port_range_min
        # {"en":"Authorization object: The IP or CIDR that matches the security group rules.
        # 1) Only a single IP or CIDR can be specified.
        # 2) The specified IP or CIDR must match the IP protocol type mentioned above.", "zh_CN":"授权对象：匹配该安全组规则的ip或cidr
        # 1）只能指定单个IP或CIDR
        # 2）指定的IP或CIDR必须和上述的IP协议类型一致"}
        self.remote_ip_perfix = remote_ip_perfix
        # {"en":"Notes,cannot exceed 255 characters", "zh_CN":"备注信息，不能超过255个字符"}
        self.remark = remark

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.direct, 'direct')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ethertype, 'ethertype')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.remote_ip_perfix, 'remote_ip_perfix')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.direct is not None:
            result['direct'] = self.direct
        if self.policy is not None:
            result['policy'] = self.policy
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.priority is not None:
            result['priority'] = self.priority
        if self.port_range_max is not None:
            result['portRangeMax'] = self.port_range_max
        if self.port_range_min is not None:
            result['portRangeMin'] = self.port_range_min
        if self.remote_ip_perfix is not None:
            result['remoteIpPerfix'] = self.remote_ip_perfix
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('portRangeMax') is not None:
            self.port_range_max = m.get('portRangeMax')
        if m.get('portRangeMin') is not None:
            self.port_range_min = m.get('portRangeMin')
        if m.get('remoteIpPerfix') is not None:
            self.remote_ip_perfix = m.get('remoteIpPerfix')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class AddSecurityGroupRulesRequest(TeaModel):
    def __init__(
        self,
        security_group_rules: List[AddSecurityGroupRulesSecurityGroupRuleParam] = None,
    ):
        self.security_group_rules = security_group_rules

    def validate(self):
        self.validate_required(self.security_group_rules, 'security_group_rules')
        if self.security_group_rules:
            for k in self.security_group_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_rules is not None:
            result['securityGroupRules'] = []
            for k in self.security_group_rules:
                result['securityGroupRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupRules') is not None:
            self.security_group_rules = []
            for k in m.get('securityGroupRules'):
                temp_model = AddSecurityGroupRulesSecurityGroupRuleParam()
                self.security_group_rules.append(temp_model.from_map(k))
        return self


class AddSecurityGroupRulesSecurityGroupRule(TeaModel):
    def __init__(
        self,
        id: str = None,
        direct: str = None,
        policy: str = None,
        protocol: str = None,
        ethertype: str = None,
        priority: int = None,
        port_range_max: int = None,
        port_range_min: int = None,
        remote_ip_perfix: str = None,
        remark: str = None,
        create_time: str = None,
        modify_time: str = None,
    ):
        # {"en":"Rule id", "zh_CN":"规则id"}
        self.id = id
        # {"en":"Rule direction:INGRESS;EGRESS", "zh_CN":"规则方向：
        # INGRESS-流入
        # EGRESS-流出"}
        self.direct = direct
        # {"en":"Authorization policy:ACCEPT;DROP", "zh_CN":"授权策略：
        # ACCEPT-允许
        # DROP-拒绝"}
        self.policy = policy
        # {"en":"Protocol type: TCP/UDP/ICMP", "zh_CN":"协议类型：TCP/UDP/ICMP"}
        self.protocol = protocol
        # {"en":"IP protocol:
        # 4-IPv4
        # 6-IPv6
        # ", "zh_CN":"IP协议：
        # 4-IPv4
        # 6-IPv6"}
        self.ethertype = ethertype
        # {"en":"Priority, the higher the value, the higher the priority", "zh_CN":"优先级，值越大优先级越高"}
        self.priority = priority
        # {"en":"Maximum Port Number", "zh_CN":"最大的端口号"}
        self.port_range_max = port_range_max
        # {"en":"Minimum Port Number", "zh_CN":"最小的端口号"}
        self.port_range_min = port_range_min
        # {"en":"Authorization object: IP or CIDR that matches the security group rules", "zh_CN":"授权对象：匹配该安全组规则的IP或CIDR"}
        self.remote_ip_perfix = remote_ip_perfix
        # {"en":"Notes", "zh_CN":"备注信息"}
        self.remark = remark
        # {"en":"Create Time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"Modify Time", "zh_CN":"修改时间"}
        self.modify_time = modify_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.direct, 'direct')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ethertype, 'ethertype')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.port_range_max, 'port_range_max')
        self.validate_required(self.port_range_min, 'port_range_min')
        self.validate_required(self.remote_ip_perfix, 'remote_ip_perfix')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.direct is not None:
            result['direct'] = self.direct
        if self.policy is not None:
            result['policy'] = self.policy
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.priority is not None:
            result['priority'] = self.priority
        if self.port_range_max is not None:
            result['portRangeMax'] = self.port_range_max
        if self.port_range_min is not None:
            result['portRangeMin'] = self.port_range_min
        if self.remote_ip_perfix is not None:
            result['remoteIpPerfix'] = self.remote_ip_perfix
        if self.remark is not None:
            result['remark'] = self.remark
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('portRangeMax') is not None:
            self.port_range_max = m.get('portRangeMax')
        if m.get('portRangeMin') is not None:
            self.port_range_min = m.get('portRangeMin')
        if m.get('remoteIpPerfix') is not None:
            self.remote_ip_perfix = m.get('remoteIpPerfix')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        return self


class AddSecurityGroupRulesResponse(TeaModel):
    def __init__(
        self,
        security_group_rules: List[AddSecurityGroupRulesSecurityGroupRule] = None,
    ):
        self.security_group_rules = security_group_rules

    def validate(self):
        self.validate_required(self.security_group_rules, 'security_group_rules')
        if self.security_group_rules:
            for k in self.security_group_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_rules is not None:
            result['securityGroupRules'] = []
            for k in self.security_group_rules:
                result['securityGroupRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupRules') is not None:
            self.security_group_rules = []
            for k in m.get('securityGroupRules'):
                temp_model = AddSecurityGroupRulesSecurityGroupRule()
                self.security_group_rules.append(temp_model.from_map(k))
        return self


class AddSecurityGroupRulesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupRulesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPBindSecurityGroupParam(TeaModel):
    def __init__(
        self,
        server_id: str = None,
        security_group_ids: List[str] = None,
    ):
        # {"en":"Instance ID", "zh_CN":"实例id"}
        self.server_id = server_id
        # {"en":"Security Group ID", "zh_CN":"安全组id"}
        self.security_group_ids = security_group_ids

    def validate(self):
        self.validate_required(self.server_id, 'server_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['serverId'] = self.server_id
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverId') is not None:
            self.server_id = m.get('serverId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        return self


class VMPBindSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        bind_info: List[VMPBindSecurityGroupParam] = None,
    ):
        self.bind_info = bind_info

    def validate(self):
        self.validate_required(self.bind_info, 'bind_info')
        if self.bind_info:
            for k in self.bind_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_info is not None:
            result['bindInfo'] = []
            for k in self.bind_info:
                result['bindInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindInfo') is not None:
            self.bind_info = []
            for k in m.get('bindInfo'):
                temp_model = VMPBindSecurityGroupParam()
                self.bind_info.append(temp_model.from_map(k))
        return self


class VMPBindSecurityGroupResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPBindSecurityGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPBindSecurityGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPBindSecurityGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPBindSecurityGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteSecurityGroupRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecurityGroupPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"Security Group id,multiple values separated by commas", "zh_CN":"安全组id，多个用逗号分隔"}
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


class DeleteSecurityGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecurityGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecurityGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeletionSecurityGroupRulesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletionSecurityGroupRulesResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletionSecurityGroupRulesPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"Security group rule id, multiple separated by commas", "zh_CN":"安全组规则id，多个用逗号分隔"}
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


class DeletionSecurityGroupRulesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletionSecurityGroupRulesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletionSecurityGroupRulesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPCreateSSHKeyKeypairCreate(TeaModel):
    def __init__(
        self,
        name: str = None,
        public_key: str = None,
    ):
        # {"en":"Key pair name, must be unique, otherwise creation will fail", "zh_CN":"密钥对名称，必须保持唯一，否则会创建失败"}
        self.name = name
        # {"en":"Imported public key information. The maximum length of the import public key is 1024 bytes. If this parameter is not specified, it will be generated automatically.", "zh_CN":"导入的公钥信息。导入公钥最大长度为1024字节。如果未指定该参数，系统将自动生成。"}
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        return self


class VMPCreateSSHKeyRequest(TeaModel):
    def __init__(
        self,
        keypair: List[VMPCreateSSHKeyKeypairCreate] = None,
    ):
        # {"en":"Creating array objects for SSH key", "zh_CN":"创建SSH密钥对的数组对象"}
        self.keypair = keypair

    def validate(self):
        self.validate_required(self.keypair, 'keypair')
        if self.keypair:
            for k in self.keypair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keypair is not None:
            result['keypair'] = []
            for k in self.keypair:
                result['keypair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keypair') is not None:
            self.keypair = []
            for k in m.get('keypair'):
                temp_model = VMPCreateSSHKeyKeypairCreate()
                self.keypair.append(temp_model.from_map(k))
        return self


class VMPCreateSSHKeyKeypairResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        public_key: str = None,
        private_key: str = None,
    ):
        # {"en":"Key pair name, must be unique, otherwise creation will fail", "zh_CN":"密钥对名称，必须保持唯一，否则会创建失败"}
        self.name = name
        # {"en":"Imported public key information. The maximum length of the import public key is 1024 bytes. If this parameter is not specified, it will be generated automatically.", "zh_CN":"导入的公钥信息。导入公钥最大长度为1024字节。如果未指定该参数，系统将自动生成。"}
        self.public_key = public_key
        # {"en":"The key corresponds to the privatekey information. If publickey is given in the request parameter, the privatekey will not be returned. Otherwise, the system generated private key will be returned.", "zh_CN":"密钥对应privateKey信息，如果请求参数中给了publicKey，则不会返回privateKey，否则返回系统生成的私钥。"}
        self.private_key = private_key

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.public_key, 'public_key')
        self.validate_required(self.private_key, 'private_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        return self


class VMPCreateSSHKeyResponse(TeaModel):
    def __init__(
        self,
        keypair: List[VMPCreateSSHKeyKeypairResult] = None,
    ):
        self.keypair = keypair

    def validate(self):
        self.validate_required(self.keypair, 'keypair')
        if self.keypair:
            for k in self.keypair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keypair is not None:
            result['keypair'] = []
            for k in self.keypair:
                result['keypair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keypair') is not None:
            self.keypair = []
            for k in m.get('keypair'):
                temp_model = VMPCreateSSHKeyKeypairResult()
                self.keypair.append(temp_model.from_map(k))
        return self


class VMPCreateSSHKeyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateSSHKeyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateSSHKeyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateSSHKeyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditSecurityGroupSecurityGroupParam(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        remark: str = None,
    ):
        # {'en':'Security Group id', 'zh_CN':'安全组id'}
        self.id = id
        # {'en':'Security Group name.
        #     Constraint: can only consist of letters, numbers, and underscores, with a length of no more than 64 characters.
        #     It cannot be named default and must be unique.',
        #     'zh_CN':'安全组名称 约束：只能由字母/数字/下划线组成，长度不超过64个字符，不能命名为default且名称唯一'}
        self.name = name
        # {'en':'Notes,not exceeding 255 characters in length.', 'zh_CN':'备注信息，长度不超过255个字符'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class EditSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        security_group: List[EditSecurityGroupSecurityGroupParam] = None,
    ):
        self.security_group = security_group

    def validate(self):
        self.validate_required(self.security_group, 'security_group')
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['securityGroup'] = []
            for k in self.security_group:
                result['securityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroup') is not None:
            self.security_group = []
            for k in m.get('securityGroup'):
                temp_model = EditSecurityGroupSecurityGroupParam()
                self.security_group.append(temp_model.from_map(k))
        return self


class EditSecurityGroupResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditSecurityGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPRemoveSSHKeyRequest(TeaModel):
    def __init__(
        self,
        keyname: str = None,
    ):
        # {"en":"ssh key name", "zh_CN":"ssh key 名称"}
        self.keyname = keyname

    def validate(self):
        self.validate_required(self.keyname, 'keyname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyname is not None:
            result['keyname'] = self.keyname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyname') is not None:
            self.keyname = m.get('keyname')
        return self


class VMPRemoveSSHKeyResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveSSHKeyPaths(TeaModel):
    def __init__(
        self,
        key_name: str = None,
    ):
        # {"en":"ssh key name", "zh_CN":"ssh key 名称"}
        self.key_name = key_name

    def validate(self):
        self.validate_required(self.key_name, 'key_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_name is not None:
            result['keyName'] = self.key_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        return self


class VMPRemoveSSHKeyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveSSHKeyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveSSHKeyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQuerySecurityGroupRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySecurityGroupSecurityGroupRule(TeaModel):
    def __init__(
        self,
        direct: str = None,
        policy: str = None,
        ethertype: str = None,
        priority: int = None,
        port_range_max: int = None,
        port_range_min: int = None,
        remote_ip_perfix: str = None,
    ):
        # {'en':'Rule direction', 'zh_CN':'规则方向'}
        self.direct = direct
        # {'en':'Authorization policy', 'zh_CN':'授权策略'}
        self.policy = policy
        # {'en':'IP protocol', 'zh_CN':'ip协议'}
        self.ethertype = ethertype
        # {'en':'Priority', 'zh_CN':'优先级'}
        self.priority = priority
        # {'en':'Maximum Port Number', 'zh_CN':'最大端口号'}
        self.port_range_max = port_range_max
        # {'en':'Minimum Port Number', 'zh_CN':'最小端口号'}
        self.port_range_min = port_range_min
        # {'en':'IP or CIDR matching rules', 'zh_CN':'匹配规则的ip或cidr'}
        self.remote_ip_perfix = remote_ip_perfix

    def validate(self):
        self.validate_required(self.direct, 'direct')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.ethertype, 'ethertype')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.port_range_max, 'port_range_max')
        self.validate_required(self.port_range_min, 'port_range_min')
        self.validate_required(self.remote_ip_perfix, 'remote_ip_perfix')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direct is not None:
            result['direct'] = self.direct
        if self.policy is not None:
            result['policy'] = self.policy
        if self.ethertype is not None:
            result['ethertype'] = self.ethertype
        if self.priority is not None:
            result['priority'] = self.priority
        if self.port_range_max is not None:
            result['portRangeMax'] = self.port_range_max
        if self.port_range_min is not None:
            result['portRangeMin'] = self.port_range_min
        if self.remote_ip_perfix is not None:
            result['remoteIpPerfix'] = self.remote_ip_perfix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('ethertype') is not None:
            self.ethertype = m.get('ethertype')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('portRangeMax') is not None:
            self.port_range_max = m.get('portRangeMax')
        if m.get('portRangeMin') is not None:
            self.port_range_min = m.get('portRangeMin')
        if m.get('remoteIpPerfix') is not None:
            self.remote_ip_perfix = m.get('remoteIpPerfix')
        return self


class VMPQuerySecurityGroupSecurityGroup(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        remark: str = None,
        create_time: str = None,
        modify_time: str = None,
        rules: List[VMPQuerySecurityGroupSecurityGroupRule] = None,
    ):
        # {'en':'Security Group ID', 'zh_CN':'安全组id'}
        self.id = id
        # {'en':'Security Group name', 'zh_CN':'安全组名称'}
        self.name = name
        # {'en':'Notes', 'zh_CN':'备注信息'}
        self.remark = remark
        # {'en':'Create Time:yyyy-MM-dd HH:mm:ss', 'zh_CN':'创建时间（yyyy-MM-dd HH:mm:ss）'}
        self.create_time = create_time
        # {'en':'Modify Time:yyyy-MM-dd HH:mm:ss', 'zh_CN':'修改时间（yyyy-MM-dd HH:mm:ss）'}
        self.modify_time = modify_time
        self.rules = rules

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.rules, 'rules')
        if self.rules:
            for k in self.rules:
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
        if self.remark is not None:
            result['remark'] = self.remark
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.rules is not None:
            result['rules'] = []
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('rules') is not None:
            self.rules = []
            for k in m.get('rules'):
                temp_model = VMPQuerySecurityGroupSecurityGroupRule()
                self.rules.append(temp_model.from_map(k))
        return self


class VMPQuerySecurityGroupResponse(TeaModel):
    def __init__(
        self,
        security_groups: List[VMPQuerySecurityGroupSecurityGroup] = None,
    ):
        self.security_groups = security_groups

    def validate(self):
        self.validate_required(self.security_groups, 'security_groups')
        if self.security_groups:
            for k in self.security_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_groups is not None:
            result['securityGroups'] = []
            for k in self.security_groups:
                result['securityGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroups') is not None:
            self.security_groups = []
            for k in m.get('securityGroups'):
                temp_model = VMPQuerySecurityGroupSecurityGroup()
                self.security_groups.append(temp_model.from_map(k))
        return self


class VMPQuerySecurityGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySecurityGroupParameters(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # {'en':'Security Group ID', 'zh_CN':'根据安全组id查询'}
        self.id = id
        # {'en':'Security Group name', 'zh_CN':'根据安全组名称查询'}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class VMPQuerySecurityGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySecurityGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddSecurityGroupSecurityGroupParam(TeaModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
    ):
        # {'en':'Security group name. 
        #     Constraint: can only consist of letters, numbers, and underscores, with a length of no more than 64 characters. 
        #     It cannot be named default and must be unique.',
        #     'zh_CN':'安全组名称。约束：只能由字母/数字/下划线组成，长度不超过64个字符，不能命名为default且名称唯一。'}
        self.name = name
        # {'en':'Notes (optional), no more than 255 characters in length', 'zh_CN':'备注（可选），长度不超过255个字符'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class AddSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        security_group: List[AddSecurityGroupSecurityGroupParam] = None,
    ):
        self.security_group = security_group

    def validate(self):
        self.validate_required(self.security_group, 'security_group')
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['securityGroup'] = []
            for k in self.security_group:
                result['securityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroup') is not None:
            self.security_group = []
            for k in m.get('securityGroup'):
                temp_model = AddSecurityGroupSecurityGroupParam()
                self.security_group.append(temp_model.from_map(k))
        return self


class AddSecurityGroupSecurityGroup(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        remark: str = None,
        create_time: str = None,
        modify_time: str = None,
    ):
        # {'en':'Security Group ID', 'zh_CN':'安全组id'}
        self.id = id
        # {'en':'Security Group name', 'zh_CN':'安全组名称'}
        self.name = name
        # {'en':'Notes', 'zh_CN':'备注信息'}
        self.remark = remark
        # {'en':'Create Time', 'zh_CN':'创建时间（yyyy-MM-dd HH:mm:ss）'}
        self.create_time = create_time
        # {'en':'Modify Time', 'zh_CN':'修改时间（yyyy-MM-dd HH:mm:ss）'}
        self.modify_time = modify_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.modify_time, 'modify_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        return self


class AddSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        security_group: List[AddSecurityGroupSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        self.validate_required(self.security_group, 'security_group')
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['securityGroup'] = []
            for k in self.security_group:
                result['securityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroup') is not None:
            self.security_group = []
            for k in m.get('securityGroup'):
                temp_model = AddSecurityGroupSecurityGroup()
                self.security_group.append(temp_model.from_map(k))
        return self


class AddSecurityGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddSecurityGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQuerySSHKeyRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # {"en":"The number of items displayed on each page is 20 by default", "zh_CN":"每个页面显示条数，默认是20"}
        self.limit = limit
        # {"en":"Query from the virtual machine ID specified by the marker", "zh_CN":"从marker指定的实例id开始查询"}
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class VMPQuerySSHKeyResponse(TeaModel):
    def __init__(
        self,
        keypairs: List[str] = None,
        name: str = None,
        public_key: str = None,
    ):
        # {"en":"Key pair", "zh_CN":"密钥对"}
        self.keypairs = keypairs
        # {"en":"Key pair name", "zh_CN":"密钥对名称"}
        self.name = name
        # {"en":"Public key information corresponding to key", "zh_CN":"密钥对应publicKey信息"}
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.keypairs, 'keypairs')
        self.validate_required(self.name, 'name')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keypairs is not None:
            result['keypairs'] = self.keypairs
        if self.name is not None:
            result['name'] = self.name
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keypairs') is not None:
            self.keypairs = m.get('keypairs')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        return self


class VMPQuerySSHKeyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySSHKeyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySSHKeyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQuerySSHKeyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




