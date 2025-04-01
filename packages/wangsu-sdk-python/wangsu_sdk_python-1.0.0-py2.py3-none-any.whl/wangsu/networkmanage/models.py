# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VMPQueryEdgePrivateIPRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgePrivateIPVMPEdgePrivateIP(TeaModel):
    def __init__(
        self,
        edge_ip: str = None,
        state: str = None,
        instance_id: str = None,
        public_edge_ip: str = None,
        node_name: str = None,
    ):
        # {"en":"extra Ip", "zh_CN":"额外内网Ip"}
        self.edge_ip = edge_ip
        # {"en":"IP state", "zh_CN":"IP状态：FREE-空闲未绑定；ASSIGNED-已绑定"}
        self.state = state
        # {"en":"binding virtual machine ID", "zh_CN":"绑定的虚拟机ID"}
        self.instance_id = instance_id
        # {"en":"binding edge public IP", "zh_CN":"绑定的额外公网IP"}
        self.public_edge_ip = public_edge_ip
        # {"en":"node name", "zh_CN":"所属节点名称"}
        self.node_name = node_name

    def validate(self):
        self.validate_required(self.edge_ip, 'edge_ip')
        self.validate_required(self.state, 'state')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.public_edge_ip, 'public_edge_ip')
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ip is not None:
            result['edgeIp'] = self.edge_ip
        if self.state is not None:
            result['state'] = self.state
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.public_edge_ip is not None:
            result['publicEdgeIp'] = self.public_edge_ip
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIp') is not None:
            self.edge_ip = m.get('edgeIp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('publicEdgeIp') is not None:
            self.public_edge_ip = m.get('publicEdgeIp')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class VMPQueryEdgePrivateIPResponse(TeaModel):
    def __init__(
        self,
        edge_ips: List[VMPQueryEdgePrivateIPVMPEdgePrivateIP] = None,
    ):
        # {"en":"additional IP details", "zh_CN":"额外内网Ip详细信息"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')
        if self.edge_ips:
            for k in self.edge_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = []
            for k in self.edge_ips:
                result['edgeIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = []
            for k in m.get('edgeIps'):
                temp_model = VMPQueryEdgePrivateIPVMPEdgePrivateIP()
                self.edge_ips.append(temp_model.from_map(k))
        return self


class VMPQueryEdgePrivateIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgePrivateIPParameters(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        instance_id: str = None,
        edge_ip: str = None,
        public_edge_ip: str = None,
        state: str = None,
    ):
        # {"en":"node name", "zh_CN":"可选
        # 节点名称，多个用英文逗号分隔"}
        self.node_name = node_name
        # {"en":"virtual machine ID", "zh_CN":"可选
        # 虚拟机ID，多个用英文逗号分隔"}
        self.instance_id = instance_id
        # {"en":"extra Ip", "zh_CN":"可选
        # 额外Ip，多个用英文逗号分隔"}
        self.edge_ip = edge_ip
        # {"en":"extra Ip", "zh_CN":"可选
        # 额外公网Ip，多个用英文逗号分隔"}
        self.public_edge_ip = public_edge_ip
        # {"en":"IP state", "zh_CN":"可选
        # IP状态：FREE-空闲未绑定；ASSIGNED-已绑定"}
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.edge_ip is not None:
            result['edgeIp'] = self.edge_ip
        if self.public_edge_ip is not None:
            result['publicEdgeIp'] = self.public_edge_ip
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('edgeIp') is not None:
            self.edge_ip = m.get('edgeIp')
        if m.get('publicEdgeIp') is not None:
            self.public_edge_ip = m.get('publicEdgeIp')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class VMPQueryEdgePrivateIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgePrivateIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQueryAvailableCidrsDetailRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsDetailCidrDetail(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        native_attribute: str = None,
        free_ips: int = None,
        freezing_ips: int = None,
        used_ips: int = None,
    ):
        # {"en":"CIDR", "zh_CN":"网段 CIDR"}
        self.cidr = cidr
        # {"en":"IP native attribute.(-1: Native, 1: Non-native)", "zh_CN":"原生属性. (-1: 原生, 1: 非原生)"}
        self.native_attribute = native_attribute
        # {"en":"Number of free and available IPs", "zh_CN":"空闲可用IP数"}
        self.free_ips = free_ips
        # {"en":"Freezing IP number", "zh_CN":"冷却IP数"}
        self.freezing_ips = freezing_ips
        # {"en":"Number of IPs already used", "zh_CN":"已用IP数"}
        self.used_ips = used_ips

    def validate(self):
        self.validate_required(self.cidr, 'cidr')
        self.validate_required(self.native_attribute, 'native_attribute')
        self.validate_required(self.free_ips, 'free_ips')
        self.validate_required(self.freezing_ips, 'freezing_ips')
        self.validate_required(self.used_ips, 'used_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.native_attribute is not None:
            result['nativeAttribute'] = self.native_attribute
        if self.free_ips is not None:
            result['freeIps'] = self.free_ips
        if self.freezing_ips is not None:
            result['freezingIps'] = self.freezing_ips
        if self.used_ips is not None:
            result['usedIps'] = self.used_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('nativeAttribute') is not None:
            self.native_attribute = m.get('nativeAttribute')
        if m.get('freeIps') is not None:
            self.free_ips = m.get('freeIps')
        if m.get('freezingIps') is not None:
            self.freezing_ips = m.get('freezingIps')
        if m.get('usedIps') is not None:
            self.used_ips = m.get('usedIps')
        return self


class VMPQueryAvailableCidrsDetailNodeResource(TeaModel):
    def __init__(
        self,
        node: str = None,
        cidrs: List[VMPQueryAvailableCidrsDetailCidrDetail] = None,
    ):
        # {"en":"Node name.", "zh_CN":"节点名称"}
        self.node = node
        # {"en":"CIDR detail.", "zh_CN":"网段详情"}
        self.cidrs = cidrs

    def validate(self):
        self.validate_required(self.node, 'node')
        self.validate_required(self.cidrs, 'cidrs')
        if self.cidrs:
            for k in self.cidrs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node is not None:
            result['node'] = self.node
        if self.cidrs is not None:
            result['cidrs'] = []
            for k in self.cidrs:
                result['cidrs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('cidrs') is not None:
            self.cidrs = []
            for k in m.get('cidrs'):
                temp_model = VMPQueryAvailableCidrsDetailCidrDetail()
                self.cidrs.append(temp_model.from_map(k))
        return self


class VMPQueryAvailableCidrsDetailResponse(TeaModel):
    def __init__(
        self,
        nodes: List[VMPQueryAvailableCidrsDetailNodeResource] = None,
    ):
        # {"en":"available cidrs", "zh_CN":"可用的cidr列表"}
        self.nodes = nodes

    def validate(self):
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = []
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = []
            for k in m.get('nodes'):
                temp_model = VMPQueryAvailableCidrsDetailNodeResource()
                self.nodes.append(temp_model.from_map(k))
        return self


class VMPQueryAvailableCidrsDetailPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsDetailParameters(TeaModel):
    def __init__(
        self,
        node: str = None,
        cidr: str = None,
        native_attribute: str = None,
        need_ipv_6: str = None,
    ):
        # {"en":"Node name.", "zh_CN":"节点名称，多个节点用英文逗号分隔，最多填写20个"}
        self.node = node
        # {"en":"CIDR", "zh_CN":"网段 CIDR"}
        self.cidr = cidr
        # {"en":"IP native attribute.(-1: Native, 1: Non-native)", "zh_CN":"原生属性. (-1: 原生, 1: 非原生)"}
        self.native_attribute = native_attribute
        # {"en":"IPv6 segment(1: yes, -1: no)", "zh_CN":"是否返回IPV6网段(1: 是, -1: 否)"}
        self.need_ipv_6 = need_ipv_6

    def validate(self):
        self.validate_required(self.node, 'node')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node is not None:
            result['node'] = self.node
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.native_attribute is not None:
            result['nativeAttribute'] = self.native_attribute
        if self.need_ipv_6 is not None:
            result['needIPv6'] = self.need_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('nativeAttribute') is not None:
            self.native_attribute = m.get('nativeAttribute')
        if m.get('needIPv6') is not None:
            self.need_ipv_6 = m.get('needIPv6')
        return self


class VMPQueryAvailableCidrsDetailRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsDetailResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteServiceStatusDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        group: str = None,
        uid: str = None,
    ):
        # {"en":"The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described)", "zh_CN":"与状态 StatusReason 关联的资源的名称属性（当有一个可以描述的名称时）"}
        self.name = name
        # {"en":"The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind", "zh_CN":"与状态 StatusReason 关联的资源的种类属性"}
        self.kind = kind
        # {"en":"The group attribute of the resource associated with the status StatusReason", "zh_CN":"与状态 StatusReason 关联的资源的组属性"}
        self.group = group
        # {"en":"UID of the resource. (when there is a single resource which can be described)", "zh_CN":"资源的 UID（当有单个可以描述的资源时）"}
        self.uid = uid

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.group, 'group')
        self.validate_required(self.uid, 'uid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.group is not None:
            result['group'] = self.group
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class DeleteServiceStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteServiceStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteServiceStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
        self.status = status
        # {"en":"Suggested HTTP return code for this status, 0 if not set", "zh_CN":"此状态的建议 HTTP 返回代码，如果未设置，则为 0"}
        self.code = code
        # {"en":"Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type", "zh_CN":"与原因（Reason）相关的扩展数据。每个原因都可以定义自己的扩展细节。 此字段是可选的，并且不保证返回的数据符合任何模式，除非由原因类型定义"}
        self.details = details

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.status, 'status')
        self.validate_required(self.code, 'code')
        self.validate_required(self.details, 'details')
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.status is not None:
            result['status'] = self.status
        if self.code is not None:
            result['code'] = self.code
        if self.details is not None:
            result['details'] = self.details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('details') is not None:
            temp_model = DeleteServiceStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteServiceStatus = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"status", "zh_CN":"status"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = DeleteServiceStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"service name", "zh_CN":"service 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateServiceOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class CreateServiceFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateServiceManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateServiceFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateServiceManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateServiceFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateServiceFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateServiceFieldsV1 holds the first JSON version format as described in the 'CreateServiceFieldsV1' type", "zh_CN":"CreateServiceFieldsV1 包含类型 “CreateServiceFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = CreateServiceFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateServiceObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[CreateServiceOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateServiceManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 CreateServiceService 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = CreateServiceOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateServiceManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateServiceServicePort(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        app_protocol: str = None,
        port: int = None,
        target_port: int = None,
        node_port: int = None,
    ):
        # {"en":"The name of this port within the service. This must be a DNS_LABEL. All ports within a CreateServiceServiceSpec must have unique names. When considering the endpoints for a CreateServiceService, this must match the 'name' field in the EndpointPort. Optional if only one CreateServiceServicePort is defined on this service", "zh_CN":"CreateServiceService 中此端口的名称。这必须是 DNS_LABEL。 CreateServiceServiceSpec 中的所有端口的名称都必须唯一。 在考虑 CreateServiceService 的端点时，这一字段值必须与 EndpointPort 中的 name 字段相同。 如果此服务上仅定义一个 CreateServiceServicePort，则为此字段为可选"}
        self.name = name
        # {"en":"The IP protocol for this port. Supports TCP, UDP, and SCTP. Default is TCP", "zh_CN":"此端口的 IP 协议。支持 “TCP”、“UDP” 和 “SCTP”。默认为 TCP"}
        self.protocol = protocol
        # {"en":"The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol", "zh_CN":"此端口的应用协议，遵循标准的 Kubernetes 标签语法，无前缀名称按照 IANA 标准服务名称 （参见 RFC-6335 和 https://www.iana.org/assignments/service-names）。 非标准协议应该使用前缀名称，如 mycompany.com/my-custom-protocol"}
        self.app_protocol = app_protocol
        # {"en":"The port that will be exposed by this service", "zh_CN":"CreateServiceService 将公开的端口"}
        self.port = port
        # {"en":"Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field", "zh_CN":"在 CreateServiceService 所针对的 Pod 上要访问的端口号或名称。 编号必须在 1 到 65535 的范围内。名称必须是 IANA_SVC_NAME。 如果此值是一个字符串，将在目标 Pod 的容器端口中作为命名端口进行查找。 如果未指定字段，则使用 “port” 字段的值（直接映射）。 对于 clusterIP 为 None 的服务，此字段将被忽略， 应忽略不设或设置为 “port” 字段的取值"}
        self.target_port = target_port
        # {"en":"The port on each node on which this service is exposed when type is NodePort or LoadBalancer. Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail. If not specified, a port will be allocated if this CreateServiceService requires one. If this field is specified when creating a CreateServiceService which does not need it, creation will fail. This field will be wiped when updating a CreateServiceService to no longer need it (e.g. changing type from NodePort to ClusterIP).", "zh_CN":"当类型为 NodePort 或 LoadBalancer 时，CreateServiceService 公开在节点上的端口， 通常由系统分配。如果指定了一个在范围内且未使用的值，则将使用该值，否则操作将失败。 如果在创建的 CreateServiceService 需要该端口时未指定该字段，则会分配端口。 如果在创建不需要该端口的 Service时指定了该字段，则会创建失败。 当更新 CreateServiceService 时，如果不再需要此字段（例如，将类型从 NodePort 更改为 ClusterIP），这个字段将被擦除"}
        self.node_port = node_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.app_protocol is not None:
            result['appProtocol'] = self.app_protocol
        if self.port is not None:
            result['port'] = self.port
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        if self.node_port is not None:
            result['nodePort'] = self.node_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('appProtocol') is not None:
            self.app_protocol = m.get('appProtocol')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        if m.get('nodePort') is not None:
            self.node_port = m.get('nodePort')
        return self


class CreateServiceClientIPConfig(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
    ):
        # {"en":"timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3 hours).", "zh_CN":"timeoutSeconds 指定 ClientIP 类型会话的维系时间秒数。 如果 ServiceAffinity == 'ClientIP'，则该值必须 >0 && <=86400（1 天）。默认值为 10800（3 小时）"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class CreateServiceSessionAffinityConfig(TeaModel):
    def __init__(
        self,
        client_ip: CreateServiceClientIPConfig = None,
    ):
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"clientIP 包含基于客户端 IP 的会话亲和性的配置"}
        self.client_ip = client_ip

    def validate(self):
        if self.client_ip:
            self.client_ip.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIP') is not None:
            temp_model = CreateServiceClientIPConfig()
            self.client_ip = temp_model.from_map(m['clientIP'])
        return self


class CreateServiceServiceSpec(TeaModel):
    def __init__(
        self,
        ports: List[CreateServiceServicePort] = None,
        selector: Dict[str, str] = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        type: str = None,
        external_ips: List[str] = None,
        session_affinity: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        publish_not_ready_addresses: bool = None,
        session_affinity_config: CreateServiceSessionAffinityConfig = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        allocate_load_balancer_node_ports: bool = None,
        load_balancer_class: str = None,
        internal_traffic_policy: str = None,
    ):
        # {"en":"The list of ports that are exposed by this service", "zh_CN":"此 CreateServiceService 公开的端口列表"}
        self.ports = ports
        # {"en":"Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName", "zh_CN":"将 CreateServiceService 流量路由到具有与此 selector 匹配的标签键值对的 Pod。 如果为空或不存在，则假定该服务有一个外部进程管理其端点，Kubernetes 不会修改该端点。 仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型。如果类型为 ExternalName，则忽略"}
        self.selector = selector
        # {"en":"clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a CreateServiceService of type ExternalName, creation will fail. This field will be wiped when updating a CreateServiceService to type ExternalName", "zh_CN":"clusterIP 是服务的 IP 地址，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给服务，否则创建服务将失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIP 为空）或 type 已经是 ExternalName 时，可以更改 clusterIP（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIP 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 仅适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 CreateServiceService 时指定了 clusterIP，则创建将失败。 更新 CreateServiceService type 为 ExternalName 时，clusterIP 会被移除"}
        self.cluster_ip = cluster_ip
        # {"en":"ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a CreateServiceService of type ExternalName, creation will fail. This field will be wiped when updating a CreateServiceService to type ExternalName. If this field is not specified, it will be initialized from the clusterIP field. If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"clusterIPs 是分配给该 CreateServiceService 的 IP 地址列表，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给 CreateServiceService；否则创建 CreateServiceService 失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIPs 为空）或 type 已经是 ExternalName 时，可以更改 clusterIPs（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIPs 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 CreateServiceService 时指定了 clusterIPs，则会创建失败。 更新 CreateServiceService type 为 ExternalName 时，该字段将被移除。如果未指定此字段，则将从 clusterIP 字段初始化。 如果指定 clusterIPs，客户端必须确保 clusterIPs[0] 和 clusterIP 一致。clusterIPs 最多可包含两个条目（双栈系列，按任意顺序）。 这些 IP 必须与 ipFamilies 的值相对应。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 管理"}
        self.cluster_ips = cluster_ips
        # {"en":"type determines how the CreateServiceService is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName. Several other fields do not apply to ExternalName services", "zh_CN":"type 确定 CreateServiceService 的公开方式。默认为 ClusterIP。 有效选项为 ExternalName、ClusterIP、NodePort 和 LoadBalancer。 “ClusterIP” 为端点分配一个集群内部 IP 地址用于负载均衡。 Endpoints 由 selector 确定，如果未设置 selector，则需要通过手动构造 Endpoints 或 EndpointSlice 的对象来确定。 如果 clusterIP 为 “None”，则不分配虚拟 IP，并且 Endpoints 作为一组端点而不是虚拟 IP 发布。 “NodePort” 建立在 ClusterIP 之上，并在每个节点上分配一个端口，该端口路由到与 clusterIP 相同的 Endpoints。 “LoadBalancer” 基于 NodePort 构建并创建一个外部负载均衡器（如果当前云支持），该负载均衡器路由到与 clusterIP 相同的 Endpoints。 “externalName” 将此 CreateServiceService 别名为指定的 externalName。其他几个字段不适用于 ExternalName CreateServiceService"}
        self.type = type
        # {"en":"externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system", "zh_CN":"externalIPs 是一个 IP 列表，集群中的节点会为此 CreateServiceService 接收针对这些 IP 地址的流量。 这些 IP 不被 Kubernetes 管理。用户需要确保流量可以到达具有此 IP 的节点。 一个常见的例子是不属于 Kubernetes 系统的外部负载均衡器"}
        self.external_ips = external_ips
        # {"en":"Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None", "zh_CN":"支持 “ClientIP” 和 “None”。用于维护会话亲和性。 启用基于客户端 IP 的会话亲和性。必须是 ClientIP 或 None。默认为 None"}
        self.session_affinity = session_affinity
        # {"en":"Only applies to CreateServiceService Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations, and it cannot support dual-stack. As of Kubernetes v1.24, users are encouraged to use implementation-specific annotations when available. This field may be removed in a future API version", "zh_CN":"仅适用于服务类型: LoadBalancer。此功能取决于底层云提供商是否支持负载均衡器。 如果云提供商不支持该功能，该字段将被忽略。 已弃用: 该字段信息不足，且其含义因实现而异，而且不支持双栈。 从 Kubernetes v1.24 开始，鼓励用户在可用时使用特定于实现的注释。在未来的 API 版本中可能会删除此字段"}
        self.load_balancer_ip = load_balancer_ip
        # {"en":"If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature", "zh_CN":"如果设置了此字段并且被平台支持，将限制通过云厂商的负载均衡器的流量到指定的客户端 IP。 如果云提供商不支持该功能，该字段将被忽略"}
        self.load_balancer_source_ranges = load_balancer_source_ranges
        # {"en":"externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved. Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires type to be 'ExternalName'", "zh_CN":"externalName 是发现机制将返回的外部引用，作为此服务的别名（例如 DNS CNAME 记录）。 不涉及代理。必须是小写的 RFC-1123 主机名 (https://tools.ietf.org/html/rfc1123)， 并且要求 type 为 “ExternalName”"}
        self.external_name = external_name
        # {"en":"externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the CreateServiceService's 'externally-facing' addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node", "zh_CN":"externalTrafficPolicy 描述了节点如何分发它们在 CreateServiceService 的“外部访问”地址 （NodePort、ExternalIP 和 LoadBalancer IP）接收到的服务流量。 如果设置为 “Local”，代理将以一种假设外部负载均衡器将负责在节点之间服务流量负载均衡， 因此每个节点将仅向服务的节点本地端点传递流量，而不会伪装客户端源 IP。 （将丢弃错误发送到没有端点的节点的流量。） “Cluster” 默认值使用负载均衡路由到所有端点的策略（可能会根据拓扑和其他特性进行修改）。 请注意，从集群内部发送到 External IP 或 LoadBalancer IP 的流量始终具有 “Cluster” 语义， 但是从集群内部发送到 NodePort 的客户端需要在选择节点时考虑流量路由策略"}
        self.external_traffic_policy = external_traffic_policy
        # {"en":"healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used. If not specified, a value will be automatically allocated. External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not. If this field is specified when creating a CreateServiceService which does not need it, creation will fail. This field will be wiped when updating a CreateServiceService to no longer need it (e.g. changing type). This field cannot be updated once set", "zh_CN":"healthCheckNodePort 指定 CreateServiceService 的健康检查节点端口。 仅适用于 type 为 LoadBalancer 且 externalTrafficPolicy 设置为 Local 的情况。 如果为此字段设定了一个值，该值在合法范围内且没有被使用，则使用所指定的值。 如果未设置此字段，则自动分配字段值。外部系统（例如负载平衡器）可以使用此端口来确定给定节点是否拥有此服务的端点。 在创建不需要 healthCheckNodePort 的 CreateServiceService 时指定了此字段，则 CreateServiceService 创建会失败。 要移除 healthCheckNodePort，需要更改 CreateServiceService 的 type。 该字段一旦设置就无法更改"}
        self.health_check_node_port = health_check_node_port
        # {"en":"publishNotReadyAddresses indicates that any agent which deals with endpoints for this CreateServiceService should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless CreateServiceService to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered 'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior", "zh_CN":"publishNotReadyAddresses 表示任何处理此 CreateServiceService 端点的代理都应忽略任何准备就绪/未准备就绪的指示。 设置此字段的主要场景是为 StatefulSet 的服务提供支持，使之能够为其 Pod 传播 SRV DNS 记录，以实现对等发现。 为 CreateServiceService 生成 Endpoints 和 EndpointSlice 资源的 Kubernetes 控制器对字段的解读是， 即使 Pod 本身还没有准备好，所有端点都可被视为 “已就绪”。 对于代理而言，如果仅使用 Kubernetes 通过 Endpoints 或 EndpointSlice 资源所生成的端点， 则可以安全地假设这种行为"}
        self.publish_not_ready_addresses = publish_not_ready_addresses
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"sessionAffinityConfig 包含会话亲和性的配置"}
        self.session_affinity_config = session_affinity_config
        # {"en":"IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the CreateServiceService. Valid values are 'IPv4' and 'IPv6'. This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to 'headless' services. This field will be wiped when updating a CreateServiceService to type ExternalName.This field may hold a maximum of two entries (dual-stack families, in either order). These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"iPFamilies 是分配给此服务的 IP 协议（例如 IPv4、IPv6）的列表。 该字段通常根据集群配置和 ipFamilyPolicy 字段自动设置。 如果手动指定该字段，且请求的协议在集群中可用，且 ipFamilyPolicy 允许，则使用；否则服务创建将失败。 该字段修改是有条件的：它允许添加或删除辅助 IP 协议，但不允许更改服务的主要 IP 协议。 有效值为 “IPv4” 和 “IPv6”。 该字段仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型的服务，并且确实可用于“无头”服务。 更新服务设置类型为 ExternalName 时，该字段将被擦除。该字段最多可以包含两个条目（双栈系列，按任意顺序）。 如果指定，这些协议栈必须对应于 clusterIPs 字段的值。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 字段管理"}
        self.ip_families = ip_families
        # {"en":"IPFamilyPolicy represents the dual-stack-ness requested or required by this CreateServiceService. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName", "zh_CN":"iPFamilyPolicy 表示此服务请求或要求的双栈特性。 如果没有提供值，则此字段将被设置为 SingleStack。 服务可以是 “SingleStack”（单个 IP 协议）、 “PreferDualStack”（双栈配置集群上的两个 IP 协议或单栈集群上的单个 IP 协议） 或 “RequireDualStack”（双栈上的两个 IP 协议配置的集群，否则失败）。 ipFamilies 和 clusterIPs 字段取决于此字段的值。 更新服务设置类型为 ExternalName 时，此字段将被擦除"}
        self.ip_family_policy = ip_family_policy
        # {"en":"allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer. Default is 'true'. It may be set to 'false' if the cluster load-balancer does not rely on NodePorts. If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type", "zh_CN":"allocateLoadBalancerNodePorts 定义了是否会自动为 LoadBalancer 类型的 CreateServiceService 分配 NodePort。默认为 true。 如果集群负载均衡器不依赖 NodePort，则可以设置此字段为 false。 如果调用者（通过指定一个值）请求特定的 NodePort，则无论此字段如何，都会接受这些请求。 该字段只能设置在 type 为 LoadBalancer 的 CreateServiceService 上，如果 type 更改为任何其他类型，该字段将被移除"}
        self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        # {"en":"loadBalancerClass is the class of the load balancer implementation this CreateServiceService belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved for end-users. This field can only be set when the CreateServiceService type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a CreateServiceService to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type", "zh_CN":"loadBalancerClass 是此 CreateServiceService 所属的负载均衡器实现的类。 如果设置了此字段，则字段值必须是标签风格的标识符，带有可选前缀，例如 ”internal-vip” 或 “example.com/internal-vip”。 无前缀名称是为最终用户保留的。该字段只能在 CreateServiceService 类型为 “LoadBalancer” 时设置。 如果未设置此字段，则使用默认负载均衡器实现。默认负载均衡器现在通常通过云提供商集成完成，但应适用于任何默认实现。 如果设置了此字段，则假定负载均衡器实现正在监测具有对应负载均衡器类的 CreateServiceService。 任何默认负载均衡器实现（例如云提供商）都应忽略设置此字段的 CreateServiceService。 只有在创建或更新的 CreateServiceService 的 type 为 “LoadBalancer” 时，才可设置此字段。 一经设定，不可更改。当 CreateServiceService 的 type 更新为 “LoadBalancer” 之外的其他类型时，此字段将被移除"}
        self.load_balancer_class = load_balancer_class
        # {"en":"InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features)", "zh_CN":"InternalTrafficPolicy 描述节点如何分发它们在 ClusterIP 上接收到的服务流量。 如果设置为 “Local”，代理将假定 Pod 只想与在同一节点上的服务端点通信，如果没有本地端点，它将丢弃流量。 “Cluster” 默认将流量路由到所有端点（可能会根据拓扑和其他特性进行修改）"}
        self.internal_traffic_policy = internal_traffic_policy

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.session_affinity_config:
            self.session_affinity_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['selector'] = self.selector
        if self.cluster_ip is not None:
            result['clusterIP'] = self.cluster_ip
        if self.cluster_ips is not None:
            result['clusterIPs'] = self.cluster_ips
        if self.type is not None:
            result['type'] = self.type
        if self.external_ips is not None:
            result['externalIPs'] = self.external_ips
        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity
        if self.load_balancer_ip is not None:
            result['loadBalancerIP'] = self.load_balancer_ip
        if self.load_balancer_source_ranges is not None:
            result['loadBalancerSourceRanges'] = self.load_balancer_source_ranges
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.external_traffic_policy is not None:
            result['externalTrafficPolicy'] = self.external_traffic_policy
        if self.health_check_node_port is not None:
            result['healthCheckNodePort'] = self.health_check_node_port
        if self.publish_not_ready_addresses is not None:
            result['publishNotReadyAddresses'] = self.publish_not_ready_addresses
        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config.to_map()
        if self.ip_families is not None:
            result['ipFamilies'] = self.ip_families
        if self.ip_family_policy is not None:
            result['ipFamilyPolicy'] = self.ip_family_policy
        if self.allocate_load_balancer_node_ports is not None:
            result['allocateLoadBalancerNodePorts'] = self.allocate_load_balancer_node_ports
        if self.load_balancer_class is not None:
            result['loadBalancerClass'] = self.load_balancer_class
        if self.internal_traffic_policy is not None:
            result['internalTrafficPolicy'] = self.internal_traffic_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = CreateServiceServicePort()
                self.ports.append(temp_model.from_map(k))
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('clusterIP') is not None:
            self.cluster_ip = m.get('clusterIP')
        if m.get('clusterIPs') is not None:
            self.cluster_ips = m.get('clusterIPs')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('externalIPs') is not None:
            self.external_ips = m.get('externalIPs')
        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')
        if m.get('loadBalancerIP') is not None:
            self.load_balancer_ip = m.get('loadBalancerIP')
        if m.get('loadBalancerSourceRanges') is not None:
            self.load_balancer_source_ranges = m.get('loadBalancerSourceRanges')
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('externalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('externalTrafficPolicy')
        if m.get('healthCheckNodePort') is not None:
            self.health_check_node_port = m.get('healthCheckNodePort')
        if m.get('publishNotReadyAddresses') is not None:
            self.publish_not_ready_addresses = m.get('publishNotReadyAddresses')
        if m.get('sessionAffinityConfig') is not None:
            temp_model = CreateServiceSessionAffinityConfig()
            self.session_affinity_config = temp_model.from_map(m['sessionAffinityConfig'])
        if m.get('ipFamilies') is not None:
            self.ip_families = m.get('ipFamilies')
        if m.get('ipFamilyPolicy') is not None:
            self.ip_family_policy = m.get('ipFamilyPolicy')
        if m.get('allocateLoadBalancerNodePorts') is not None:
            self.allocate_load_balancer_node_ports = m.get('allocateLoadBalancerNodePorts')
        if m.get('loadBalancerClass') is not None:
            self.load_balancer_class = m.get('loadBalancerClass')
        if m.get('internalTrafficPolicy') is not None:
            self.internal_traffic_policy = m.get('internalTrafficPolicy')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateServiceObjectMeta = None,
        spec: CreateServiceServiceSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 CreateServiceService 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateServicePortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"the port number of the service port of which status is recorded here", "zh_CN":"port 是所记录的服务端口状态的端口号"}
        self.port = port
        # {"en":"the protocol of the service port of which status is recorded here The supported values are: 'TCP', 'UDP', 'SCTP'", "zh_CN":"protocol 是所记录的服务端口状态的协议。支持的值为：“TCP”、”UDP”、“SCTP”"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use CamelCase names - cloud provider specific error values must have names that comply with the format foo.example.com/CamelCase", "zh_CN":"error 是记录 CreateServiceService 端口的问题。 错误的格式应符合以下规则:内置错误原因应在此文件中指定，应使用 CamelCase 名称。云提供商特定错误原因的名称必须符合格式 foo.example.com/CamelCase"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class CreateServiceLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        host_name: str = None,
        ports: List[CreateServicePortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)", "zh_CN":"ip 是为基于 IP 的负载均衡器 Ingress 点（通常是 GCE 或 OpenStack 负载均衡器）设置的"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)", "zh_CN":"hostname 是为基于 DNS 的负载均衡器 Ingress 点（通常是 AWS 负载均衡器）设置的"}
        self.host_name = host_name
        # {"en":"Ports is a list of records of service ports If used, every port defined in the service should have an entry in it", "zh_CN":"ports 是 CreateServiceService 的端口列表。如果设置了此字段，CreateServiceService 中定义的每个端口都应该在此列表中"}
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = CreateServicePortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class CreateServiceLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[CreateServiceLoadBalancerIngress] = None,
    ):
        # {"en":"Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points", "zh_CN":"ingress 是一个包含负载均衡器 Ingress 点的列表。CreateServiceService 的流量需要被发送到这些 Ingress 点"}
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = CreateServiceLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class CreateServiceMetaV1Condition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        observed_generation: int = None,
        last_transition_time: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type of condition in CamelCase or in foo.example.com/CamelCase", "zh_CN":"CamelCase 或 foo.example.com/CamelCase 中的条件类型"}
        self.type = type
        # {"en":"status of the condition, one of True, False, Unknown", "zh_CN":"condition 的状态，True、False、Unknown 之一"}
        self.status = status
        # {"en":"observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance", "zh_CN":"表示设置 condition 基于的 .metadata.generation 的过期次数。 例如，如果 .metadata.generation 当前为 12，但 .status.conditions[x].observedGeneration 为 9， 则 condition 相对于实例的当前状态已过期"}
        self.observed_generation = observed_generation
        # {"en":"lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable", "zh_CN":"状况最近一次状态转化的时间。 变化应该发生在下层状况发生变化的时候。如果不知道下层状况发生变化的时间， 那么使用 API 字段更改的时间是可以接受的"}
        self.last_transition_time = last_transition_time
        # {"en":"reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty", "zh_CN":"reason 包含一个程序标识符，指示 condition 最后一次转换的原因。 特定条件类型的生产者可以定义该字段的预期值和含义，以及这些值是否被视为有保证的 API。 该值应该是 CamelCase 字符串且不能为空"}
        self.reason = reason
        # {"en":"message is a human readable message indicating details about the transition. This may be an empty string", "zh_CN":"message 是人类可读的消息，有关转换的详细信息，可以是空字符串"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateServiceServiceStatus(TeaModel):
    def __init__(
        self,
        load_balancer: CreateServiceLoadBalancerStatus = None,
        conditions: List[CreateServiceMetaV1Condition] = None,
    ):
        # {"en":"Current service state", "zh_CN":"loadBalancer 包含负载均衡器的当前状态（如果存在）"}
        self.load_balancer = load_balancer
        # {"en":"LoadBalancer contains the current status of the load-balancer, if one is present", "zh_CN":"服务的当前状态"}
        self.conditions = conditions

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = CreateServiceLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = CreateServiceMetaV1Condition()
                self.conditions.append(temp_model.from_map(k))
        return self


class CreateServiceService(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateServiceObjectMeta = None,
        spec: CreateServiceServiceSpec = None,
        status: CreateServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 CreateServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 CreateServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = CreateServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateServiceService = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"service", "zh_CN":"service"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = CreateServiceService()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class CreateServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPAllocateEdgeIPRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        protocol: str = None,
        native_attribute: str = None,
        cidr: str = None,
        count: int = None,
        random_allocate_ip: int = None,
    ):
        # {"en":"node name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"IP protocol:4-ipv4(default);6-ipv6(temporary unsupported)", "zh_CN":"可选
        # IP协议：4-ipv4(默认)；6-ipv6"}
        self.protocol = protocol
        # {"en":"IP native attribute, 1: non-native;-1: native;", "zh_CN":"IPv4原生属性，1：非原生；-1：原生；不指定默认随机分配原生属性"}
        self.native_attribute = native_attribute
        # {"en":"cidr", "zh_CN":"CIDR，一次只能传入一个CIDR"}
        self.cidr = cidr
        # {"en":"number of applications IP  (the single upper limit is 50)", "zh_CN":"申请IP数（单次申请Ip数上限为50个）"}
        self.count = count
        # {"en":"Allocate IP randomly", "zh_CN":"是否需要随机分配IP（仅对ipv4生效）  
        # 1：是
        # -1：否"}
        self.random_allocate_ip = random_allocate_ip

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.native_attribute is not None:
            result['nativeAttribute'] = self.native_attribute
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.count is not None:
            result['count'] = self.count
        if self.random_allocate_ip is not None:
            result['randomAllocateIp'] = self.random_allocate_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('nativeAttribute') is not None:
            self.native_attribute = m.get('nativeAttribute')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('randomAllocateIp') is not None:
            self.random_allocate_ip = m.get('randomAllocateIp')
        return self


class VMPAllocateEdgeIPResponse(TeaModel):
    def __init__(
        self,
        edge_ips: List[str] = None,
    ):
        # {"en":"successful application for all or part of IP", "zh_CN":"成功申请到的全部或部分IP
        # 说明：不同场景的响应说明如下
        # A、所有IP都申请成功，返回申请到的所有IP
        # B、只申请到部分IP，返回申请到的那部分IP
        # C、未申请到任何IP，返回失败信息
        # D、若出现申请失败的情况，请间隔10S之后再次申请"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPAllocateEdgeIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAllocateEdgeIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAllocateEdgeIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAllocateEdgeIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPAssignEdgePrivateIPVMPEdgeIPMapping(TeaModel):
    def __init__(
        self,
        edge_private_ip: str = None,
        edge_public_ip: str = None,
    ):
        # {"en":"edge private ip", "zh_CN":"额外内网IP"}
        self.edge_private_ip = edge_private_ip
        # {"en":"edge public IP", "zh_CN":"额外公网IP"}
        self.edge_public_ip = edge_public_ip

    def validate(self):
        self.validate_required(self.edge_private_ip, 'edge_private_ip')
        self.validate_required(self.edge_public_ip, 'edge_public_ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_private_ip is not None:
            result['edgePrivateIp'] = self.edge_private_ip
        if self.edge_public_ip is not None:
            result['edgePublicIp'] = self.edge_public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgePrivateIp') is not None:
            self.edge_private_ip = m.get('edgePrivateIp')
        if m.get('edgePublicIp') is not None:
            self.edge_public_ip = m.get('edgePublicIp')
        return self


class VMPAssignEdgePrivateIPRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        edge_ips: List[VMPAssignEdgePrivateIPVMPEdgeIPMapping] = None,
    ):
        # {"en":"target virtual machine id", "zh_CN":"目标实例ID"}
        self.instance_id = instance_id
        # {"en":"additional IP to bind to the virtual machine", "zh_CN":"要绑定到目标实例的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.edge_ips, 'edge_ips')
        if self.edge_ips:
            for k in self.edge_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.edge_ips is not None:
            result['edgeIps'] = []
            for k in self.edge_ips:
                result['edgeIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('edgeIps') is not None:
            self.edge_ips = []
            for k in m.get('edgeIps'):
                temp_model = VMPAssignEdgePrivateIPVMPEdgeIPMapping()
                self.edge_ips.append(temp_model.from_map(k))
        return self


class VMPAssignEdgePrivateIPResponse(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        edge_ips: List[VMPAssignEdgePrivateIPVMPEdgeIPMapping] = None,
    ):
        # {"en":"target virtual machine id", "zh_CN":"目标实例ID"}
        self.instance_id = instance_id
        # {"en":"Additional IP that is bound to the instance", "zh_CN":"已绑定到目标实例的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.edge_ips, 'edge_ips')
        if self.edge_ips:
            for k in self.edge_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.edge_ips is not None:
            result['edgeIps'] = []
            for k in self.edge_ips:
                result['edgeIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('edgeIps') is not None:
            self.edge_ips = []
            for k in m.get('edgeIps'):
                temp_model = VMPAssignEdgePrivateIPVMPEdgeIPMapping()
                self.edge_ips.append(temp_model.from_map(k))
        return self


class VMPAssignEdgePrivateIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgePrivateIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgePrivateIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgePrivateIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListNetworkPolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListNetworkPolicyOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class ListNetworkPolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListNetworkPolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListNetworkPolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListNetworkPolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListNetworkPolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListNetworkPolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListNetworkPolicyFieldsV1 holds the first JSON version format as described in the 'ListNetworkPolicyFieldsV1' type", "zh_CN":"ListNetworkPolicyFieldsV1 包含类型 “ListNetworkPolicyFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = ListNetworkPolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListNetworkPolicyObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[ListNetworkPolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListNetworkPolicyManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = ListNetworkPolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListNetworkPolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListNetworkPolicyNetworkPolicyPort(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # {"en": "The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.", "zh_CN": "端口"}
        self.port = port
        # {"en": "The protocol (TCP, UDP) which traffic must match. If not specified, this field defaults to TCP.", "zh_CN": "协议"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class ListNetworkPolicyIPBlock(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        except_: List[str] = None,
    ):
        # {"en": "CIDR is a string representing the IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64", "zh_CN": "生效IP网段"}
        self.cidr = cidr
        # {"en": "Except is a slice of CIDRs that should not be included within an IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64 Except values will be rejected if they are outside the CIDR range", "zh_CN": "例外IP网段"}
        self.except_ = except_

    def validate(self):
        self.validate_required(self.cidr, 'cidr')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.except_ is not None:
            result['except'] = self.except_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('except') is not None:
            self.except_ = m.get('except')
        return self


class ListNetworkPolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListNetworkPolicyNsLabelSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[ListNetworkPolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListNetworkPolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListNetworkPolicyPodLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self


class ListNetworkPolicyNetworkPolicyPeer(TeaModel):
    def __init__(
        self,
        ip_block: ListNetworkPolicyIPBlock = None,
        namespace_selector: ListNetworkPolicyNsLabelSelector = None,
        pod_selector: ListNetworkPolicyPodLabelSelector = None,
    ):
        # {"en": "ListNetworkPolicyIPBlock defines policy on a particular ListNetworkPolicyIPBlock. If this field is set then neither of the other fields can be.", "zh_CN": "IP规则"}
        self.ip_block = ip_block
        # {"en": "Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.If PodSelector is also set, then the ListNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.", "zh_CN": "namespace选择器"}
        self.namespace_selector = namespace_selector
        # {"en": "This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.If NamespaceSelector is also set, then the ListNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.", "zh_CN": "pod选择器"}
        self.pod_selector = pod_selector

    def validate(self):
        if self.ip_block:
            self.ip_block.validate()
        if self.namespace_selector:
            self.namespace_selector.validate()
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_block is not None:
            result['ipBlock'] = self.ip_block.to_map()
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_map()
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipBlock') is not None:
            temp_model = ListNetworkPolicyIPBlock()
            self.ip_block = temp_model.from_map(m['ipBlock'])
        if m.get('namespaceSelector') is not None:
            temp_model = ListNetworkPolicyNsLabelSelector()
            self.namespace_selector = temp_model.from_map(m['namespaceSelector'])
        if m.get('podSelector') is not None:
            temp_model = ListNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        return self


class ListNetworkPolicyNetworkPolicyEgressRule(TeaModel):
    def __init__(
        self,
        ports: List[ListNetworkPolicyNetworkPolicyPort] = None,
        to: List[ListNetworkPolicyNetworkPolicyPeer] = None,
    ):
        # {"en": "List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports
        # {"en": "List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.", "zh_CN": "出网规则信息"}
        self.to = to

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.to:
            for k in self.to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.to is not None:
            result['to'] = []
            for k in self.to:
                result['to'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = ListNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('to') is not None:
            self.to = []
            for k in m.get('to'):
                temp_model = ListNetworkPolicyNetworkPolicyPeer()
                self.to.append(temp_model.from_map(k))
        return self


class ListNetworkPolicyNetworkPolicyIngressRule(TeaModel):
    def __init__(
        self,
        from_: List[ListNetworkPolicyNetworkPolicyPeer] = None,
        ports: List[ListNetworkPolicyNetworkPolicyPort] = None,
    ):
        # {"en": "List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.", "zh_CN": "入网规则信息"}
        self.from_ = from_
        # {"en": "List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports

    def validate(self):
        if self.from_:
            for k in self.from_:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = []
            for k in self.from_:
                result['from'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = []
            for k in m.get('from'):
                temp_model = ListNetworkPolicyNetworkPolicyPeer()
                self.from_.append(temp_model.from_map(k))
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = ListNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        return self


class ListNetworkPolicyNetworkPolicySpec(TeaModel):
    def __init__(
        self,
        egress: List[ListNetworkPolicyNetworkPolicyEgressRule] = None,
        ingress: List[ListNetworkPolicyNetworkPolicyIngressRule] = None,
        pod_selector: ListNetworkPolicyPodLabelSelector = None,
        policy_types: List[str] = None,
    ):
        # {"en": "List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the ListNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this ListNetworkPolicyNetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8", "zh_CN": "出网规则"}
        self.egress = egress
        # {"en": "List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the ListNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this ListNetworkPolicyNetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)", "zh_CN": "入网规则"}
        self.ingress = ingress
        # {"en": "Selects the pods to which this ListNetworkPolicyNetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.", "zh_CN": "限制pod的选择器"}
        self.pod_selector = pod_selector
        # {"en": "List of rule types that the ListNetworkPolicyNetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ Egress ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include Egress (since such a policy would not include an Egress section and would otherwise default to just [ Ingress ]). This field is beta-level in 1.8", "zh_CN": "策略类型"}
        self.policy_types = policy_types

    def validate(self):
        if self.egress:
            for k in self.egress:
                if k:
                    k.validate()
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()
        self.validate_required(self.pod_selector, 'pod_selector')
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress is not None:
            result['egress'] = []
            for k in self.egress:
                result['egress'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        if self.policy_types is not None:
            result['policyTypes'] = self.policy_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('egress') is not None:
            self.egress = []
            for k in m.get('egress'):
                temp_model = ListNetworkPolicyNetworkPolicyEgressRule()
                self.egress.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = ListNetworkPolicyNetworkPolicyIngressRule()
                self.ingress.append(temp_model.from_map(k))
        if m.get('podSelector') is not None:
            temp_model = ListNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        if m.get('policyTypes') is not None:
            self.policy_types = m.get('policyTypes')
        return self


class ListNetworkPolicyNetworkPolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListNetworkPolicyObjectMeta = None,
        spec: ListNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this ListNetworkPolicyNetworkPolicy.", "zh_CN": "ListNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class ListNetworkPolicyNetworkPolicyList(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListNetworkPolicyObjectMeta = None,
        items: List[ListNetworkPolicyNetworkPolicy] = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "list of networkPolicy", "zh_CN": "网络策略列表"}
        self.items = items

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListNetworkPolicyNetworkPolicy()
                self.items.append(temp_model.from_map(k))
        return self


class ListNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListNetworkPolicyNetworkPolicyList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"networkPolicy", "zh_CN":"网络策略"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListNetworkPolicyNetworkPolicyList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class ListNetworkPolicyParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"networkPolicy name", "zh_CN":"网络策略名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQueryEdgeIPRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgeIPResponse(TeaModel):
    def __init__(
        self,
        edge_ips: List[str] = None,
        edge_ip: str = None,
        state: str = None,
        server_id: str = None,
        server_ip: List[str] = None,
        node_name: str = None,
    ):
        # {"en":"additional IP details", "zh_CN":"额外Ip详细信息"}
        self.edge_ips = edge_ips
        # {"en":"extra Ip", "zh_CN":"额外Ip"}
        self.edge_ip = edge_ip
        # {"en":"IP state", "zh_CN":"IP状态：FREE-空闲未绑定；ASSIGNED-已绑定"}
        self.state = state
        # {"en":"binding virtual machine ID", "zh_CN":"绑定的虚拟机ID"}
        self.server_id = server_id
        # {"en":"binding virtual machine extranet IP", "zh_CN":"绑定的虚拟机外网IP"}
        self.server_ip = server_ip
        # {"en":"node name", "zh_CN":"所属节点名称"}
        self.node_name = node_name

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')
        self.validate_required(self.edge_ip, 'edge_ip')
        self.validate_required(self.state, 'state')
        self.validate_required(self.server_id, 'server_id')
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        if self.edge_ip is not None:
            result['edgeIp'] = self.edge_ip
        if self.state is not None:
            result['state'] = self.state
        if self.server_id is not None:
            result['serverId'] = self.server_id
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        if m.get('edgeIp') is not None:
            self.edge_ip = m.get('edgeIp')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('serverId') is not None:
            self.server_id = m.get('serverId')
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class VMPQueryEdgeIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgeIPParameters(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        server_id: str = None,
        server_ip: str = None,
        edge_ip: str = None,
        state: str = None,
    ):
        # {"en":"node name", "zh_CN":"可选
        # 节点名称，多个用英文逗号分隔"}
        self.node_name = node_name
        # {"en":"virtual machine ID", "zh_CN":"可选
        # 虚拟机ID，多个用英文逗号分隔"}
        self.server_id = server_id
        # {"en":"virtual machine master IP", "zh_CN":"可选
        # 虚拟机主IP，多个用英文逗号分隔"}
        self.server_ip = server_ip
        # {"en":"extra Ip", "zh_CN":"可选
        # 额外Ip，多个用英文逗号分隔"}
        self.edge_ip = edge_ip
        # {"en":"IP state", "zh_CN":"可选
        # IP状态：FREE-空闲未绑定；ASSIGNED-已绑定"}
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.server_id is not None:
            result['serverId'] = self.server_id
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.edge_ip is not None:
            result['edgeIp'] = self.edge_ip
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('serverId') is not None:
            self.server_id = m.get('serverId')
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('edgeIp') is not None:
            self.edge_ip = m.get('edgeIp')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class VMPQueryEdgeIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryEdgeIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VmpEdgeIPrivatepAllocateRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        count: int = None,
    ):
        # {"en":"node name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"number of applications IP  (the single upper limit is 50)", "zh_CN":"申请IP数（单次申请Ip数上限为50个）"}
        self.count = count

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class VmpEdgeIPrivatepAllocateResponse(TeaModel):
    def __init__(
        self,
        edge_ips: List[str] = None,
    ):
        # {"en":"successful application for all or part of IP", "zh_CN":"成功申请到的全部或部分IP
        # 说明：不同场景的响应说明如下
        # A、所有IP都申请成功，返回申请到的所有IP
        # B、只申请到部分IP，返回申请到的那部分IP
        # C、未申请到任何IP，返回失败信息
        # D、若出现申请失败的情况，请间隔10S之后再次申请"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VmpEdgeIPrivatepAllocatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIPrivatepAllocateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIPrivatepAllocateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIPrivatepAllocateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetNetworkPolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetNetworkPolicyOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class GetNetworkPolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetNetworkPolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetNetworkPolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetNetworkPolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetNetworkPolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetNetworkPolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetNetworkPolicyFieldsV1 holds the first JSON version format as described in the 'GetNetworkPolicyFieldsV1' type", "zh_CN":"GetNetworkPolicyFieldsV1 包含类型 “GetNetworkPolicyFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = GetNetworkPolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetNetworkPolicyObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[GetNetworkPolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetNetworkPolicyManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = GetNetworkPolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetNetworkPolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetNetworkPolicyNetworkPolicyPort(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # {"en": "The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.", "zh_CN": "端口"}
        self.port = port
        # {"en": "The protocol (TCP, UDP) which traffic must match. If not specified, this field defaults to TCP.", "zh_CN": "协议"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class GetNetworkPolicyIPBlock(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        except_: List[str] = None,
    ):
        # {"en": "CIDR is a string representing the IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64", "zh_CN": "生效IP网段"}
        self.cidr = cidr
        # {"en": "Except is a slice of CIDRs that should not be included within an IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64 Except values will be rejected if they are outside the CIDR range", "zh_CN": "例外IP网段"}
        self.except_ = except_

    def validate(self):
        self.validate_required(self.cidr, 'cidr')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.except_ is not None:
            result['except'] = self.except_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('except') is not None:
            self.except_ = m.get('except')
        return self


class GetNetworkPolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetNetworkPolicyNsLabelSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[GetNetworkPolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetNetworkPolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetNetworkPolicyPodLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self


class GetNetworkPolicyNetworkPolicyPeer(TeaModel):
    def __init__(
        self,
        ip_block: GetNetworkPolicyIPBlock = None,
        namespace_selector: GetNetworkPolicyNsLabelSelector = None,
        pod_selector: GetNetworkPolicyPodLabelSelector = None,
    ):
        # {"en": "GetNetworkPolicyIPBlock defines policy on a particular GetNetworkPolicyIPBlock. If this field is set then neither of the other fields can be.", "zh_CN": "IP规则"}
        self.ip_block = ip_block
        # {"en": "Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.If PodSelector is also set, then the GetNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.", "zh_CN": "namespace选择器"}
        self.namespace_selector = namespace_selector
        # {"en": "This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.If NamespaceSelector is also set, then the GetNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.", "zh_CN": "pod选择器"}
        self.pod_selector = pod_selector

    def validate(self):
        if self.ip_block:
            self.ip_block.validate()
        if self.namespace_selector:
            self.namespace_selector.validate()
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_block is not None:
            result['ipBlock'] = self.ip_block.to_map()
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_map()
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipBlock') is not None:
            temp_model = GetNetworkPolicyIPBlock()
            self.ip_block = temp_model.from_map(m['ipBlock'])
        if m.get('namespaceSelector') is not None:
            temp_model = GetNetworkPolicyNsLabelSelector()
            self.namespace_selector = temp_model.from_map(m['namespaceSelector'])
        if m.get('podSelector') is not None:
            temp_model = GetNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        return self


class GetNetworkPolicyNetworkPolicyEgressRule(TeaModel):
    def __init__(
        self,
        ports: List[GetNetworkPolicyNetworkPolicyPort] = None,
        to: List[GetNetworkPolicyNetworkPolicyPeer] = None,
    ):
        # {"en": "List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports
        # {"en": "List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.", "zh_CN": "出网规则信息"}
        self.to = to

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.to:
            for k in self.to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.to is not None:
            result['to'] = []
            for k in self.to:
                result['to'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = GetNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('to') is not None:
            self.to = []
            for k in m.get('to'):
                temp_model = GetNetworkPolicyNetworkPolicyPeer()
                self.to.append(temp_model.from_map(k))
        return self


class GetNetworkPolicyNetworkPolicyIngressRule(TeaModel):
    def __init__(
        self,
        from_: List[GetNetworkPolicyNetworkPolicyPeer] = None,
        ports: List[GetNetworkPolicyNetworkPolicyPort] = None,
    ):
        # {"en": "List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.", "zh_CN": "入网规则信息"}
        self.from_ = from_
        # {"en": "List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports

    def validate(self):
        if self.from_:
            for k in self.from_:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = []
            for k in self.from_:
                result['from'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = []
            for k in m.get('from'):
                temp_model = GetNetworkPolicyNetworkPolicyPeer()
                self.from_.append(temp_model.from_map(k))
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = GetNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        return self


class GetNetworkPolicyNetworkPolicySpec(TeaModel):
    def __init__(
        self,
        egress: List[GetNetworkPolicyNetworkPolicyEgressRule] = None,
        ingress: List[GetNetworkPolicyNetworkPolicyIngressRule] = None,
        pod_selector: GetNetworkPolicyPodLabelSelector = None,
        policy_types: List[str] = None,
    ):
        # {"en": "List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the GetNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this GetNetworkPolicyNetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8", "zh_CN": "出网规则"}
        self.egress = egress
        # {"en": "List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the GetNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this GetNetworkPolicyNetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)", "zh_CN": "入网规则"}
        self.ingress = ingress
        # {"en": "Selects the pods to which this GetNetworkPolicyNetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.", "zh_CN": "限制pod的选择器"}
        self.pod_selector = pod_selector
        # {"en": "List of rule types that the GetNetworkPolicyNetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ Egress ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include Egress (since such a policy would not include an Egress section and would otherwise default to just [ Ingress ]). This field is beta-level in 1.8", "zh_CN": "策略类型"}
        self.policy_types = policy_types

    def validate(self):
        if self.egress:
            for k in self.egress:
                if k:
                    k.validate()
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()
        self.validate_required(self.pod_selector, 'pod_selector')
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress is not None:
            result['egress'] = []
            for k in self.egress:
                result['egress'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        if self.policy_types is not None:
            result['policyTypes'] = self.policy_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('egress') is not None:
            self.egress = []
            for k in m.get('egress'):
                temp_model = GetNetworkPolicyNetworkPolicyEgressRule()
                self.egress.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = GetNetworkPolicyNetworkPolicyIngressRule()
                self.ingress.append(temp_model.from_map(k))
        if m.get('podSelector') is not None:
            temp_model = GetNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        if m.get('policyTypes') is not None:
            self.policy_types = m.get('policyTypes')
        return self


class GetNetworkPolicyNetworkPolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetNetworkPolicyObjectMeta = None,
        spec: GetNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this GetNetworkPolicyNetworkPolicy.", "zh_CN": "GetNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class GetNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetNetworkPolicyNetworkPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"networkPolicy", "zh_CN":"网络策略"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetNetworkPolicyNetworkPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class GetNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"networkPolicy name", "zh_CN":"networkPolicy 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetNetworkPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetIngressControllerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressControllerIngressCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        replicate: int = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"replicates", "zh_CN":"副本数"}
        self.replicate = replicate

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.replicate, 'replicate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.replicate is not None:
            result['replicate'] = self.replicate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicate') is not None:
            self.replicate = m.get('replicate')
        return self


class GetIngressControllerIngressController(TeaModel):
    def __init__(
        self,
        name: str = None,
        limit: Dict[str, str] = None,
        clusters: List[GetIngressControllerIngressCluster] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name
        # {"en":"resource limit", "zh_CN":"资源限制"}
        self.limit = limit
        # {"en":"cluster and replicate", "zh_CN":"部署集群和副本数"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = GetIngressControllerIngressCluster()
                self.clusters.append(temp_model.from_map(k))
        return self


class GetIngressControllerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetIngressControllerIngressController = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress controller", "zh_CN":"路由控制器"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetIngressControllerIngressController()
            self.data = temp_model.from_map(m['data'])
        return self


class GetIngressControllerPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetIngressControllerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressControllerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressControllerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPAssignEdgeIPRequest(TeaModel):
    def __init__(
        self,
        server_ip: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"target virtual machine external network Ip", "zh_CN":"目标实例的公网Ip"}
        self.server_ip = server_ip
        # {"en":"additional IP to bind to the virtual machine", "zh_CN":"要绑定到目标实例的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPAssignEdgeIPResponse(TeaModel):
    def __init__(
        self,
        server_ip: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"target virtual machine IP", "zh_CN":"目标实例公网IP"}
        self.server_ip = server_ip
        # {"en":"Additional IP that is bound to the instance", "zh_CN":"已绑定到实例的额外公网IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPAssignEdgeIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgeIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgeIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPAssignEdgeIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateIngressOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class UpdateIngressFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateIngressManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateIngressFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateIngressManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateIngressFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateIngressFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateIngressFieldsV1 holds the first JSON version format as described in the 'UpdateIngressFieldsV1' type", "zh_CN":"UpdateIngressFieldsV1 包含类型 “UpdateIngressFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = UpdateIngressFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateIngressObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[UpdateIngressOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateIngressManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = UpdateIngressOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateIngressManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateIngressServiceBackendPort(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
    ):
        # {"en":"Name is the name of the port on the Service", "zh_CN":"服务端口名称"}
        self.name = name
        # {"en":"Number is the numerical port number on the Service", "zh_CN":"服务数字端口"}
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class UpdateIngressIngressServiceBackend(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: UpdateIngressServiceBackendPort = None,
    ):
        # {"en":"Name is the referenced service", "zh_CN":"服务名称"}
        self.name = name
        # {"en":"Port of the referenced service. A port name or port number", "zh_CN":"服务端口或端口名称"}
        self.port = port

    def validate(self):
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            temp_model = UpdateIngressServiceBackendPort()
            self.port = temp_model.from_map(m['port'])
        return self


class UpdateIngressTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        api_group: str = None,
    ):
        # {"en":"Name is the name of resource being referenced", "zh_CN":"资源名称"}
        self.name = name
        # {"en":"Kind is the type of resource being referenced", "zh_CN":"资源类型"}
        self.kind = kind
        # {"en":"APIGroup is the group for the resource being referenced", "zh_CN":"资源分组"}
        self.api_group = api_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        return self


class UpdateIngressIngressBackend(TeaModel):
    def __init__(
        self,
        service: UpdateIngressIngressServiceBackend = None,
        resource: UpdateIngressTypedLocalObjectReference = None,
    ):
        # {"en":"Service references a Service as a Backend", "zh_CN":"指定后端服务"}
        self.service = service
        # {"en":"Resource is an ObjectRef to another Kubernetes resource in the namespace of the UpdateIngressIngress object", "zh_CN":"路由指定后端资源"}
        self.resource = resource

    def validate(self):
        if self.service:
            self.service.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['service'] = self.service.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service') is not None:
            temp_model = UpdateIngressIngressServiceBackend()
            self.service = temp_model.from_map(m['service'])
        if m.get('resource') is not None:
            temp_model = UpdateIngressTypedLocalObjectReference()
            self.resource = temp_model.from_map(m['resource'])
        return self


class UpdateIngressIngressTLS(TeaModel):
    def __init__(
        self,
        hosts: List[str] = None,
        secret_name: str = None,
    ):
        # {"en":"Hosts are a list of hosts included in the TLS certificate", "zh_CN":"tls证书包含域名"}
        self.hosts = hosts
        # {"en":"SecretName is the name of the secret used to terminate TLS traffic on port 443", "zh_CN":"tls秘钥名称"}
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['hosts'] = self.hosts
        if self.secret_name is not None:
            result['secretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        if m.get('secretName') is not None:
            self.secret_name = m.get('secretName')
        return self


class UpdateIngressHTTPIngressPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        path_type: str = None,
        backend: UpdateIngressIngressBackend = None,
    ):
        # {"en":"Path is matched against the path of an incoming request", "zh_CN":"请求路径"}
        self.path = path
        # {"en":"PathType determines the interpretation of the Path matching,PathType can be one of the following values: Exact,Prefix,ImplementationSpecific", "zh_CN":"路径匹配类型: Exact,Prefix,ImplementationSpecific"}
        self.path_type = path_type
        # {"en":"Backend defines the referenced service endpoint to which the traffic will be forwarded to", "zh_CN":"指定后端服务"}
        self.backend = backend

    def validate(self):
        if self.backend:
            self.backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.path_type is not None:
            result['pathType'] = self.path_type
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        if m.get('backend') is not None:
            temp_model = UpdateIngressIngressBackend()
            self.backend = temp_model.from_map(m['backend'])
        return self


class UpdateIngressHTTPIngressRuleValue(TeaModel):
    def __init__(
        self,
        paths: List[UpdateIngressHTTPIngressPath] = None,
    ):
        # {"en":"A collection of paths that map requests to backends", "zh_CN":"请求路径匹配规则"}
        self.paths = paths

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paths is not None:
            result['paths'] = []
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paths') is not None:
            self.paths = []
            for k in m.get('paths'):
                temp_model = UpdateIngressHTTPIngressPath()
                self.paths.append(temp_model.from_map(k))
        return self


class UpdateIngressIngressRule(TeaModel):
    def __init__(
        self,
        host: str = None,
        http: UpdateIngressHTTPIngressRuleValue = None,
    ):
        # {"en":"Host is the fully qualified domain name of a network host", "zh_CN":"域名"}
        self.host = host
        self.http = http

    def validate(self):
        if self.http:
            self.http.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.http is not None:
            result['http'] = self.http.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('http') is not None:
            temp_model = UpdateIngressHTTPIngressRuleValue()
            self.http = temp_model.from_map(m['http'])
        return self


class UpdateIngressIngressSpec(TeaModel):
    def __init__(
        self,
        ingress_class_name: str = None,
        default_backend: UpdateIngressIngressBackend = None,
        tls: List[UpdateIngressIngressTLS] = None,
        rules: List[UpdateIngressIngressRule] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.ingress_class_name = ingress_class_name
        # {"en":"DefaultBackend is the backend that should handle requests that don't match any rule", "zh_CN":"默认后端,当请求不匹配任何规则时调用"}
        self.default_backend = default_backend
        self.tls = tls
        # {"en":"A list of host rules used to configure the UpdateIngressIngress", "zh_CN":"路由规则列表"}
        self.rules = rules

    def validate(self):
        if self.default_backend:
            self.default_backend.validate()
        if self.tls:
            for k in self.tls:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_class_name is not None:
            result['ingressClassName'] = self.ingress_class_name
        if self.default_backend is not None:
            result['defaultBackend'] = self.default_backend.to_map()
        if self.tls is not None:
            result['tls'] = []
            for k in self.tls:
                result['tls'].append(k.to_map() if k else None)
        if self.rules is not None:
            result['rules'] = []
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressClassName') is not None:
            self.ingress_class_name = m.get('ingressClassName')
        if m.get('defaultBackend') is not None:
            temp_model = UpdateIngressIngressBackend()
            self.default_backend = temp_model.from_map(m['defaultBackend'])
        if m.get('tls') is not None:
            self.tls = []
            for k in m.get('tls'):
                temp_model = UpdateIngressIngressTLS()
                self.tls.append(temp_model.from_map(k))
        if m.get('rules') is not None:
            self.rules = []
            for k in m.get('rules'):
                temp_model = UpdateIngressIngressRule()
                self.rules.append(temp_model.from_map(k))
        return self


class UpdateIngressIngress(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateIngressObjectMeta = None,
        spec: UpdateIngressIngressSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"ingress desired", "zh_CN":"路由期望属性"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateIngressObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateIngressIngressSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdateIngressRequest(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[str] = None,
        ingress: UpdateIngressIngress = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('ingress') is not None:
            temp_model = UpdateIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        return self


class UpdateIngressCustomIngress(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[str] = None,
        ingress: UpdateIngressIngress = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('ingress') is not None:
            temp_model = UpdateIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        return self


class UpdateIngressResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateIngressCustomIngress = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress object", "zh_CN":"路由对象"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = UpdateIngressCustomIngress()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateIngressPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress name", "zh_CN":"路由名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateIngressParameters(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class UpdateIngressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateIngressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateIngressPortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"Port is the port number of the service port of which status is recorded here", "zh_CN":"服务端口"}
        self.port = port
        # {"en":"Protocol is the protocol of the service port of which status is recorded here,The supported values are: TCP, UDP, SCTP", "zh_CN":"服务支持类型: TCP,UDP,SCTP"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port", "zh_CN":"记录服务端口错误信息"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class UpdateIngressLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        hostname: str = None,
        ports: List[UpdateIngressPortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based", "zh_CN":"负载均衡服务ip"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based", "zh_CN":"负载均衡类型服务dns"}
        self.hostname = hostname
        # {"en":"Ports is a list of records of service ports", "zh_CN":"服务端口状态列表"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.ports, 'ports')
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = UpdateIngressPortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class UpdateIngressLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[UpdateIngressLoadBalancerIngress] = None,
    ):
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = UpdateIngressLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class UpdateIngressIngressStatus(TeaModel):
    def __init__(
        self,
        load_balancer: UpdateIngressLoadBalancerStatus = None,
    ):
        # {"en":"LoadBalancer contains the current status of the load-balancer", "zh_CN":"包含当前负载均衡服务的状态"}
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = UpdateIngressLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        return self






class ListIngressRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressCustomCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"cluster cn name", "zh_CN":"集群中文名"}
        self.name_cn = name_cn

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        return self


class ListIngressOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class ListIngressFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListIngressFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListIngressManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListIngressFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListIngressFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListIngressFieldsV1 holds the first JSON version format as described in the 'ListIngressFieldsV1' type", "zh_CN":"ListIngressFieldsV1 包含类型 “ListIngressFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = ListIngressFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListIngressObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[ListIngressOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListIngressManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = ListIngressOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListIngressManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListIngressServiceBackendPort(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
    ):
        # {"en":"Name is the name of the port on the Service", "zh_CN":"服务端口名称"}
        self.name = name
        # {"en":"Number is the numerical port number on the Service", "zh_CN":"服务数字端口"}
        self.number = number

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.number, 'number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class ListIngressIngressServiceBackend(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: ListIngressServiceBackendPort = None,
    ):
        # {"en":"Name is the referenced service", "zh_CN":"服务名称"}
        self.name = name
        # {"en":"Port of the referenced service. A port name or port number", "zh_CN":"服务端口或端口名称"}
        self.port = port

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.port, 'port')
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            temp_model = ListIngressServiceBackendPort()
            self.port = temp_model.from_map(m['port'])
        return self


class ListIngressTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        api_group: str = None,
    ):
        # {"en":"Name is the name of resource being referenced", "zh_CN":"资源名称"}
        self.name = name
        # {"en":"Kind is the type of resource being referenced", "zh_CN":"资源类型"}
        self.kind = kind
        # {"en":"APIGroup is the group for the resource being referenced", "zh_CN":"资源分组"}
        self.api_group = api_group

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_group, 'api_group')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        return self


class ListIngressIngressBackend(TeaModel):
    def __init__(
        self,
        service: ListIngressIngressServiceBackend = None,
        resource: ListIngressTypedLocalObjectReference = None,
    ):
        # {"en":"Service references a Service as a Backend", "zh_CN":"指定后端服务"}
        self.service = service
        # {"en":"Resource is an ObjectRef to another Kubernetes resource in the namespace of the ListIngressIngress object", "zh_CN":"路由指定后端资源"}
        self.resource = resource

    def validate(self):
        self.validate_required(self.service, 'service')
        if self.service:
            self.service.validate()
        self.validate_required(self.resource, 'resource')
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['service'] = self.service.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service') is not None:
            temp_model = ListIngressIngressServiceBackend()
            self.service = temp_model.from_map(m['service'])
        if m.get('resource') is not None:
            temp_model = ListIngressTypedLocalObjectReference()
            self.resource = temp_model.from_map(m['resource'])
        return self


class ListIngressIngressTLS(TeaModel):
    def __init__(
        self,
        hosts: List[str] = None,
        secret_name: str = None,
    ):
        # {"en":"Hosts are a list of hosts included in the TLS certificate", "zh_CN":"tls证书包含域名"}
        self.hosts = hosts
        # {"en":"SecretName is the name of the secret used to terminate TLS traffic on port 443", "zh_CN":"tls秘钥名称"}
        self.secret_name = secret_name

    def validate(self):
        self.validate_required(self.hosts, 'hosts')
        self.validate_required(self.secret_name, 'secret_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['hosts'] = self.hosts
        if self.secret_name is not None:
            result['secretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        if m.get('secretName') is not None:
            self.secret_name = m.get('secretName')
        return self


class ListIngressHTTPIngressPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        path_type: str = None,
        backend: ListIngressIngressBackend = None,
    ):
        # {"en":"Path is matched against the path of an incoming request", "zh_CN":"请求路径"}
        self.path = path
        # {"en":"PathType determines the interpretation of the Path matching,PathType can be one of the following values: Exact,Prefix,ImplementationSpecific", "zh_CN":"路径匹配类型: Exact,Prefix,ImplementationSpecific"}
        self.path_type = path_type
        # {"en":"Backend defines the referenced service endpoint to which the traffic will be forwarded to", "zh_CN":"指定后端服务"}
        self.backend = backend

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.path_type, 'path_type')
        self.validate_required(self.backend, 'backend')
        if self.backend:
            self.backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.path_type is not None:
            result['pathType'] = self.path_type
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        if m.get('backend') is not None:
            temp_model = ListIngressIngressBackend()
            self.backend = temp_model.from_map(m['backend'])
        return self


class ListIngressHTTPIngressRuleValue(TeaModel):
    def __init__(
        self,
        paths: List[ListIngressHTTPIngressPath] = None,
    ):
        # {"en":"A collection of paths that map requests to backends", "zh_CN":"请求路径匹配规则"}
        self.paths = paths

    def validate(self):
        self.validate_required(self.paths, 'paths')
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paths is not None:
            result['paths'] = []
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paths') is not None:
            self.paths = []
            for k in m.get('paths'):
                temp_model = ListIngressHTTPIngressPath()
                self.paths.append(temp_model.from_map(k))
        return self


class ListIngressIngressRule(TeaModel):
    def __init__(
        self,
        host: str = None,
        http: ListIngressHTTPIngressRuleValue = None,
    ):
        # {"en":"Host is the fully qualified domain name of a network host", "zh_CN":"域名"}
        self.host = host
        self.http = http

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.http, 'http')
        if self.http:
            self.http.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.http is not None:
            result['http'] = self.http.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('http') is not None:
            temp_model = ListIngressHTTPIngressRuleValue()
            self.http = temp_model.from_map(m['http'])
        return self


class ListIngressIngressSpec(TeaModel):
    def __init__(
        self,
        ingress_class_name: str = None,
        default_backend: ListIngressIngressBackend = None,
        tls: List[ListIngressIngressTLS] = None,
        rules: List[ListIngressIngressRule] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.ingress_class_name = ingress_class_name
        # {"en":"DefaultBackend is the backend that should handle requests that don't match any rule", "zh_CN":"默认后端,当请求不匹配任何规则时调用"}
        self.default_backend = default_backend
        self.tls = tls
        # {"en":"A list of host rules used to configure the ListIngressIngress", "zh_CN":"路由规则列表"}
        self.rules = rules

    def validate(self):
        self.validate_required(self.ingress_class_name, 'ingress_class_name')
        self.validate_required(self.default_backend, 'default_backend')
        if self.default_backend:
            self.default_backend.validate()
        self.validate_required(self.tls, 'tls')
        if self.tls:
            for k in self.tls:
                if k:
                    k.validate()
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
        if self.ingress_class_name is not None:
            result['ingressClassName'] = self.ingress_class_name
        if self.default_backend is not None:
            result['defaultBackend'] = self.default_backend.to_map()
        if self.tls is not None:
            result['tls'] = []
            for k in self.tls:
                result['tls'].append(k.to_map() if k else None)
        if self.rules is not None:
            result['rules'] = []
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressClassName') is not None:
            self.ingress_class_name = m.get('ingressClassName')
        if m.get('defaultBackend') is not None:
            temp_model = ListIngressIngressBackend()
            self.default_backend = temp_model.from_map(m['defaultBackend'])
        if m.get('tls') is not None:
            self.tls = []
            for k in m.get('tls'):
                temp_model = ListIngressIngressTLS()
                self.tls.append(temp_model.from_map(k))
        if m.get('rules') is not None:
            self.rules = []
            for k in m.get('rules'):
                temp_model = ListIngressIngressRule()
                self.rules.append(temp_model.from_map(k))
        return self


class ListIngressPortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"Port is the port number of the service port of which status is recorded here", "zh_CN":"服务端口"}
        self.port = port
        # {"en":"Protocol is the protocol of the service port of which status is recorded here,The supported values are: TCP, UDP, SCTP", "zh_CN":"服务支持类型: TCP,UDP,SCTP"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port", "zh_CN":"记录服务端口错误信息"}
        self.error = error

    def validate(self):
        self.validate_required(self.port, 'port')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.error, 'error')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListIngressLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        hostname: str = None,
        ports: List[ListIngressPortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based", "zh_CN":"负载均衡服务ip"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based", "zh_CN":"负载均衡类型服务dns"}
        self.hostname = hostname
        # {"en":"Ports is a list of records of service ports", "zh_CN":"服务端口状态列表"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.ports, 'ports')
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = ListIngressPortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class ListIngressLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[ListIngressLoadBalancerIngress] = None,
    ):
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = ListIngressLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class ListIngressIngressStatus(TeaModel):
    def __init__(
        self,
        load_balancer: ListIngressLoadBalancerStatus = None,
    ):
        # {"en":"LoadBalancer contains the current status of the load-balancer", "zh_CN":"包含当前负载均衡服务的状态"}
        self.load_balancer = load_balancer

    def validate(self):
        self.validate_required(self.load_balancer, 'load_balancer')
        if self.load_balancer:
            self.load_balancer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = ListIngressLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        return self


class ListIngressIngress(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListIngressObjectMeta = None,
        spec: ListIngressIngressSpec = None,
        status: ListIngressIngressStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"ingress desired", "zh_CN":"路由期望属性"}
        self.spec = spec
        # {"en":"Status is the current state of the ListIngressIngress", "zh_CN":"路由状态"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListIngressObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListIngressIngressSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ListIngressIngressStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class ListIngressCustomIngressItem(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[ListIngressCustomCluster] = None,
        ingress: ListIngressIngress = None,
        status: str = None,
        update_time: int = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"create time", "zh_CN":"更新时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = ListIngressCustomCluster()
                self.clusters.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            temp_model = ListIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListIngressCustomIngressList(TeaModel):
    def __init__(
        self,
        total: int = None,
        items: List[ListIngressCustomIngressItem] = None,
    ):
        # {"en":"total  count", "zh_CN":"总数"}
        self.total = total
        self.items = items

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListIngressCustomIngressItem()
                self.items.append(temp_model.from_map(k))
        return self


class ListIngressResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListIngressCustomIngressList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress object", "zh_CN":"路由对象"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListIngressCustomIngressList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListIngressPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressParameters(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        keyword: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"keyword", "zh_CN":"关键字"}
        self.keyword = keyword
        # {"en":"page index", "zh_CN":"页数"}
        self.page_index = page_index
        # {"en":"page size", "zh_CN":"每页数量"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListIngressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteIngressRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteIngressResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteIngressPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress name", "zh_CN":"路由名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteIngressParameters(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class DeleteIngressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteIngressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateNetworkPolicyOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class CreateNetworkPolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateNetworkPolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateNetworkPolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateNetworkPolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateNetworkPolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateNetworkPolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateNetworkPolicyFieldsV1 holds the first JSON version format as described in the 'CreateNetworkPolicyFieldsV1' type", "zh_CN":"CreateNetworkPolicyFieldsV1 包含类型 “CreateNetworkPolicyFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = CreateNetworkPolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateNetworkPolicyObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[CreateNetworkPolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateNetworkPolicyManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = CreateNetworkPolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateNetworkPolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateNetworkPolicyNetworkPolicyPort(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # {"en": "The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.", "zh_CN": "端口"}
        self.port = port
        # {"en": "The protocol (TCP, UDP) which traffic must match. If not specified, this field defaults to TCP.", "zh_CN": "协议"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class CreateNetworkPolicyIPBlock(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        except_: List[str] = None,
    ):
        # {"en": "CIDR is a string representing the IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64", "zh_CN": "生效IP网段"}
        self.cidr = cidr
        # {"en": "Except is a slice of CIDRs that should not be included within an IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64 Except values will be rejected if they are outside the CIDR range", "zh_CN": "例外IP网段"}
        self.except_ = except_

    def validate(self):
        self.validate_required(self.cidr, 'cidr')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.except_ is not None:
            result['except'] = self.except_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('except') is not None:
            self.except_ = m.get('except')
        return self


class CreateNetworkPolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateNetworkPolicyNsLabelSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[CreateNetworkPolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreateNetworkPolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreateNetworkPolicyPodLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self


class CreateNetworkPolicyNetworkPolicyPeer(TeaModel):
    def __init__(
        self,
        ip_block: CreateNetworkPolicyIPBlock = None,
        namespace_selector: CreateNetworkPolicyNsLabelSelector = None,
        pod_selector: CreateNetworkPolicyPodLabelSelector = None,
    ):
        # {"en": "CreateNetworkPolicyIPBlock defines policy on a particular CreateNetworkPolicyIPBlock. If this field is set then neither of the other fields can be.", "zh_CN": "IP规则"}
        self.ip_block = ip_block
        # {"en": "Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.If PodSelector is also set, then the CreateNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.", "zh_CN": "namespace选择器"}
        self.namespace_selector = namespace_selector
        # {"en": "This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.If NamespaceSelector is also set, then the CreateNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.", "zh_CN": "pod选择器"}
        self.pod_selector = pod_selector

    def validate(self):
        if self.ip_block:
            self.ip_block.validate()
        if self.namespace_selector:
            self.namespace_selector.validate()
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_block is not None:
            result['ipBlock'] = self.ip_block.to_map()
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_map()
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipBlock') is not None:
            temp_model = CreateNetworkPolicyIPBlock()
            self.ip_block = temp_model.from_map(m['ipBlock'])
        if m.get('namespaceSelector') is not None:
            temp_model = CreateNetworkPolicyNsLabelSelector()
            self.namespace_selector = temp_model.from_map(m['namespaceSelector'])
        if m.get('podSelector') is not None:
            temp_model = CreateNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        return self


class CreateNetworkPolicyNetworkPolicyEgressRule(TeaModel):
    def __init__(
        self,
        ports: List[CreateNetworkPolicyNetworkPolicyPort] = None,
        to: List[CreateNetworkPolicyNetworkPolicyPeer] = None,
    ):
        # {"en": "List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports
        # {"en": "List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.", "zh_CN": "出网规则信息"}
        self.to = to

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.to:
            for k in self.to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.to is not None:
            result['to'] = []
            for k in self.to:
                result['to'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = CreateNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('to') is not None:
            self.to = []
            for k in m.get('to'):
                temp_model = CreateNetworkPolicyNetworkPolicyPeer()
                self.to.append(temp_model.from_map(k))
        return self


class CreateNetworkPolicyNetworkPolicyIngressRule(TeaModel):
    def __init__(
        self,
        from_: List[CreateNetworkPolicyNetworkPolicyPeer] = None,
        ports: List[CreateNetworkPolicyNetworkPolicyPort] = None,
    ):
        # {"en": "List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.", "zh_CN": "入网规则信息"}
        self.from_ = from_
        # {"en": "List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports

    def validate(self):
        if self.from_:
            for k in self.from_:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = []
            for k in self.from_:
                result['from'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = []
            for k in m.get('from'):
                temp_model = CreateNetworkPolicyNetworkPolicyPeer()
                self.from_.append(temp_model.from_map(k))
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = CreateNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        return self


class CreateNetworkPolicyNetworkPolicySpec(TeaModel):
    def __init__(
        self,
        egress: List[CreateNetworkPolicyNetworkPolicyEgressRule] = None,
        ingress: List[CreateNetworkPolicyNetworkPolicyIngressRule] = None,
        pod_selector: CreateNetworkPolicyPodLabelSelector = None,
        policy_types: List[str] = None,
    ):
        # {"en": "List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the CreateNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this CreateNetworkPolicyNetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8", "zh_CN": "出网规则"}
        self.egress = egress
        # {"en": "List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the CreateNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this CreateNetworkPolicyNetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)", "zh_CN": "入网规则"}
        self.ingress = ingress
        # {"en": "Selects the pods to which this CreateNetworkPolicyNetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.", "zh_CN": "限制pod的选择器"}
        self.pod_selector = pod_selector
        # {"en": "List of rule types that the CreateNetworkPolicyNetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ Egress ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include Egress (since such a policy would not include an Egress section and would otherwise default to just [ Ingress ]). This field is beta-level in 1.8", "zh_CN": "策略类型"}
        self.policy_types = policy_types

    def validate(self):
        if self.egress:
            for k in self.egress:
                if k:
                    k.validate()
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()
        self.validate_required(self.pod_selector, 'pod_selector')
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress is not None:
            result['egress'] = []
            for k in self.egress:
                result['egress'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        if self.policy_types is not None:
            result['policyTypes'] = self.policy_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('egress') is not None:
            self.egress = []
            for k in m.get('egress'):
                temp_model = CreateNetworkPolicyNetworkPolicyEgressRule()
                self.egress.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = CreateNetworkPolicyNetworkPolicyIngressRule()
                self.ingress.append(temp_model.from_map(k))
        if m.get('podSelector') is not None:
            temp_model = CreateNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        if m.get('policyTypes') is not None:
            self.policy_types = m.get('policyTypes')
        return self


class CreateNetworkPolicyRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateNetworkPolicyObjectMeta = None,
        spec: CreateNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this CreateNetworkPolicyNetworkPolicy.", "zh_CN": "CreateNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateNetworkPolicyNetworkPolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateNetworkPolicyObjectMeta = None,
        spec: CreateNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this CreateNetworkPolicyNetworkPolicy.", "zh_CN": "CreateNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateNetworkPolicyNetworkPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"networkPolicy", "zh_CN":"网络策略"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = CreateNetworkPolicyNetworkPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class CreateNetworkPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateServiceOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class UpdateServiceFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateServiceManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateServiceFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateServiceManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateServiceFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateServiceFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateServiceFieldsV1 holds the first JSON version format as described in the 'UpdateServiceFieldsV1' type", "zh_CN":"UpdateServiceFieldsV1 包含类型 “UpdateServiceFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = UpdateServiceFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateServiceObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[UpdateServiceOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateServiceManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 UpdateServiceService 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = UpdateServiceOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateServiceManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateServiceServicePort(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        app_protocol: str = None,
        port: int = None,
        target_port: int = None,
        node_port: int = None,
    ):
        # {"en":"The name of this port within the service. This must be a DNS_LABEL. All ports within a UpdateServiceServiceSpec must have unique names. When considering the endpoints for a UpdateServiceService, this must match the 'name' field in the EndpointPort. Optional if only one UpdateServiceServicePort is defined on this service", "zh_CN":"UpdateServiceService 中此端口的名称。这必须是 DNS_LABEL。 UpdateServiceServiceSpec 中的所有端口的名称都必须唯一。 在考虑 UpdateServiceService 的端点时，这一字段值必须与 EndpointPort 中的 name 字段相同。 如果此服务上仅定义一个 UpdateServiceServicePort，则为此字段为可选"}
        self.name = name
        # {"en":"The IP protocol for this port. Supports TCP, UDP, and SCTP. Default is TCP", "zh_CN":"此端口的 IP 协议。支持 “TCP”、“UDP” 和 “SCTP”。默认为 TCP"}
        self.protocol = protocol
        # {"en":"The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol", "zh_CN":"此端口的应用协议，遵循标准的 Kubernetes 标签语法，无前缀名称按照 IANA 标准服务名称 （参见 RFC-6335 和 https://www.iana.org/assignments/service-names）。 非标准协议应该使用前缀名称，如 mycompany.com/my-custom-protocol"}
        self.app_protocol = app_protocol
        # {"en":"The port that will be exposed by this service", "zh_CN":"UpdateServiceService 将公开的端口"}
        self.port = port
        # {"en":"Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field", "zh_CN":"在 UpdateServiceService 所针对的 Pod 上要访问的端口号或名称。 编号必须在 1 到 65535 的范围内。名称必须是 IANA_SVC_NAME。 如果此值是一个字符串，将在目标 Pod 的容器端口中作为命名端口进行查找。 如果未指定字段，则使用 “port” 字段的值（直接映射）。 对于 clusterIP 为 None 的服务，此字段将被忽略， 应忽略不设或设置为 “port” 字段的取值"}
        self.target_port = target_port
        # {"en":"The port on each node on which this service is exposed when type is NodePort or LoadBalancer. Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail. If not specified, a port will be allocated if this UpdateServiceService requires one. If this field is specified when creating a UpdateServiceService which does not need it, creation will fail. This field will be wiped when updating a UpdateServiceService to no longer need it (e.g. changing type from NodePort to ClusterIP).", "zh_CN":"当类型为 NodePort 或 LoadBalancer 时，UpdateServiceService 公开在节点上的端口， 通常由系统分配。如果指定了一个在范围内且未使用的值，则将使用该值，否则操作将失败。 如果在创建的 UpdateServiceService 需要该端口时未指定该字段，则会分配端口。 如果在创建不需要该端口的 Service时指定了该字段，则会创建失败。 当更新 UpdateServiceService 时，如果不再需要此字段（例如，将类型从 NodePort 更改为 ClusterIP），这个字段将被擦除"}
        self.node_port = node_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.app_protocol is not None:
            result['appProtocol'] = self.app_protocol
        if self.port is not None:
            result['port'] = self.port
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        if self.node_port is not None:
            result['nodePort'] = self.node_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('appProtocol') is not None:
            self.app_protocol = m.get('appProtocol')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        if m.get('nodePort') is not None:
            self.node_port = m.get('nodePort')
        return self


class UpdateServiceClientIPConfig(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
    ):
        # {"en":"timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3 hours).", "zh_CN":"timeoutSeconds 指定 ClientIP 类型会话的维系时间秒数。 如果 ServiceAffinity == 'ClientIP'，则该值必须 >0 && <=86400（1 天）。默认值为 10800（3 小时）"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class UpdateServiceSessionAffinityConfig(TeaModel):
    def __init__(
        self,
        client_ip: UpdateServiceClientIPConfig = None,
    ):
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"clientIP 包含基于客户端 IP 的会话亲和性的配置"}
        self.client_ip = client_ip

    def validate(self):
        if self.client_ip:
            self.client_ip.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIP') is not None:
            temp_model = UpdateServiceClientIPConfig()
            self.client_ip = temp_model.from_map(m['clientIP'])
        return self


class UpdateServiceServiceSpec(TeaModel):
    def __init__(
        self,
        ports: List[UpdateServiceServicePort] = None,
        selector: Dict[str, str] = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        type: str = None,
        external_ips: List[str] = None,
        session_affinity: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        publish_not_ready_addresses: bool = None,
        session_affinity_config: UpdateServiceSessionAffinityConfig = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        allocate_load_balancer_node_ports: bool = None,
        load_balancer_class: str = None,
        internal_traffic_policy: str = None,
    ):
        # {"en":"The list of ports that are exposed by this service", "zh_CN":"此 UpdateServiceService 公开的端口列表"}
        self.ports = ports
        # {"en":"Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName", "zh_CN":"将 UpdateServiceService 流量路由到具有与此 selector 匹配的标签键值对的 Pod。 如果为空或不存在，则假定该服务有一个外部进程管理其端点，Kubernetes 不会修改该端点。 仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型。如果类型为 ExternalName，则忽略"}
        self.selector = selector
        # {"en":"clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a UpdateServiceService of type ExternalName, creation will fail. This field will be wiped when updating a UpdateServiceService to type ExternalName", "zh_CN":"clusterIP 是服务的 IP 地址，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给服务，否则创建服务将失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIP 为空）或 type 已经是 ExternalName 时，可以更改 clusterIP（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIP 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 仅适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 UpdateServiceService 时指定了 clusterIP，则创建将失败。 更新 UpdateServiceService type 为 ExternalName 时，clusterIP 会被移除"}
        self.cluster_ip = cluster_ip
        # {"en":"ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a UpdateServiceService of type ExternalName, creation will fail. This field will be wiped when updating a UpdateServiceService to type ExternalName. If this field is not specified, it will be initialized from the clusterIP field. If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"clusterIPs 是分配给该 UpdateServiceService 的 IP 地址列表，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给 UpdateServiceService；否则创建 UpdateServiceService 失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIPs 为空）或 type 已经是 ExternalName 时，可以更改 clusterIPs（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIPs 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 UpdateServiceService 时指定了 clusterIPs，则会创建失败。 更新 UpdateServiceService type 为 ExternalName 时，该字段将被移除。如果未指定此字段，则将从 clusterIP 字段初始化。 如果指定 clusterIPs，客户端必须确保 clusterIPs[0] 和 clusterIP 一致。clusterIPs 最多可包含两个条目（双栈系列，按任意顺序）。 这些 IP 必须与 ipFamilies 的值相对应。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 管理"}
        self.cluster_ips = cluster_ips
        # {"en":"type determines how the UpdateServiceService is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName. Several other fields do not apply to ExternalName services", "zh_CN":"type 确定 UpdateServiceService 的公开方式。默认为 ClusterIP。 有效选项为 ExternalName、ClusterIP、NodePort 和 LoadBalancer。 “ClusterIP” 为端点分配一个集群内部 IP 地址用于负载均衡。 Endpoints 由 selector 确定，如果未设置 selector，则需要通过手动构造 Endpoints 或 EndpointSlice 的对象来确定。 如果 clusterIP 为 “None”，则不分配虚拟 IP，并且 Endpoints 作为一组端点而不是虚拟 IP 发布。 “NodePort” 建立在 ClusterIP 之上，并在每个节点上分配一个端口，该端口路由到与 clusterIP 相同的 Endpoints。 “LoadBalancer” 基于 NodePort 构建并创建一个外部负载均衡器（如果当前云支持），该负载均衡器路由到与 clusterIP 相同的 Endpoints。 “externalName” 将此 UpdateServiceService 别名为指定的 externalName。其他几个字段不适用于 ExternalName UpdateServiceService"}
        self.type = type
        # {"en":"externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system", "zh_CN":"externalIPs 是一个 IP 列表，集群中的节点会为此 UpdateServiceService 接收针对这些 IP 地址的流量。 这些 IP 不被 Kubernetes 管理。用户需要确保流量可以到达具有此 IP 的节点。 一个常见的例子是不属于 Kubernetes 系统的外部负载均衡器"}
        self.external_ips = external_ips
        # {"en":"Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None", "zh_CN":"支持 “ClientIP” 和 “None”。用于维护会话亲和性。 启用基于客户端 IP 的会话亲和性。必须是 ClientIP 或 None。默认为 None"}
        self.session_affinity = session_affinity
        # {"en":"Only applies to UpdateServiceService Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations, and it cannot support dual-stack. As of Kubernetes v1.24, users are encouraged to use implementation-specific annotations when available. This field may be removed in a future API version", "zh_CN":"仅适用于服务类型: LoadBalancer。此功能取决于底层云提供商是否支持负载均衡器。 如果云提供商不支持该功能，该字段将被忽略。 已弃用: 该字段信息不足，且其含义因实现而异，而且不支持双栈。 从 Kubernetes v1.24 开始，鼓励用户在可用时使用特定于实现的注释。在未来的 API 版本中可能会删除此字段"}
        self.load_balancer_ip = load_balancer_ip
        # {"en":"If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature", "zh_CN":"如果设置了此字段并且被平台支持，将限制通过云厂商的负载均衡器的流量到指定的客户端 IP。 如果云提供商不支持该功能，该字段将被忽略"}
        self.load_balancer_source_ranges = load_balancer_source_ranges
        # {"en":"externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved. Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires type to be 'ExternalName'", "zh_CN":"externalName 是发现机制将返回的外部引用，作为此服务的别名（例如 DNS CNAME 记录）。 不涉及代理。必须是小写的 RFC-1123 主机名 (https://tools.ietf.org/html/rfc1123)， 并且要求 type 为 “ExternalName”"}
        self.external_name = external_name
        # {"en":"externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the UpdateServiceService's 'externally-facing' addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node", "zh_CN":"externalTrafficPolicy 描述了节点如何分发它们在 UpdateServiceService 的“外部访问”地址 （NodePort、ExternalIP 和 LoadBalancer IP）接收到的服务流量。 如果设置为 “Local”，代理将以一种假设外部负载均衡器将负责在节点之间服务流量负载均衡， 因此每个节点将仅向服务的节点本地端点传递流量，而不会伪装客户端源 IP。 （将丢弃错误发送到没有端点的节点的流量。） “Cluster” 默认值使用负载均衡路由到所有端点的策略（可能会根据拓扑和其他特性进行修改）。 请注意，从集群内部发送到 External IP 或 LoadBalancer IP 的流量始终具有 “Cluster” 语义， 但是从集群内部发送到 NodePort 的客户端需要在选择节点时考虑流量路由策略"}
        self.external_traffic_policy = external_traffic_policy
        # {"en":"healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used. If not specified, a value will be automatically allocated. External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not. If this field is specified when creating a UpdateServiceService which does not need it, creation will fail. This field will be wiped when updating a UpdateServiceService to no longer need it (e.g. changing type). This field cannot be updated once set", "zh_CN":"healthCheckNodePort 指定 UpdateServiceService 的健康检查节点端口。 仅适用于 type 为 LoadBalancer 且 externalTrafficPolicy 设置为 Local 的情况。 如果为此字段设定了一个值，该值在合法范围内且没有被使用，则使用所指定的值。 如果未设置此字段，则自动分配字段值。外部系统（例如负载平衡器）可以使用此端口来确定给定节点是否拥有此服务的端点。 在创建不需要 healthCheckNodePort 的 UpdateServiceService 时指定了此字段，则 UpdateServiceService 创建会失败。 要移除 healthCheckNodePort，需要更改 UpdateServiceService 的 type。 该字段一旦设置就无法更改"}
        self.health_check_node_port = health_check_node_port
        # {"en":"publishNotReadyAddresses indicates that any agent which deals with endpoints for this UpdateServiceService should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless UpdateServiceService to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered 'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior", "zh_CN":"publishNotReadyAddresses 表示任何处理此 UpdateServiceService 端点的代理都应忽略任何准备就绪/未准备就绪的指示。 设置此字段的主要场景是为 StatefulSet 的服务提供支持，使之能够为其 Pod 传播 SRV DNS 记录，以实现对等发现。 为 UpdateServiceService 生成 Endpoints 和 EndpointSlice 资源的 Kubernetes 控制器对字段的解读是， 即使 Pod 本身还没有准备好，所有端点都可被视为 “已就绪”。 对于代理而言，如果仅使用 Kubernetes 通过 Endpoints 或 EndpointSlice 资源所生成的端点， 则可以安全地假设这种行为"}
        self.publish_not_ready_addresses = publish_not_ready_addresses
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"sessionAffinityConfig 包含会话亲和性的配置"}
        self.session_affinity_config = session_affinity_config
        # {"en":"IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the UpdateServiceService. Valid values are 'IPv4' and 'IPv6'. This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to 'headless' services. This field will be wiped when updating a UpdateServiceService to type ExternalName.This field may hold a maximum of two entries (dual-stack families, in either order). These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"iPFamilies 是分配给此服务的 IP 协议（例如 IPv4、IPv6）的列表。 该字段通常根据集群配置和 ipFamilyPolicy 字段自动设置。 如果手动指定该字段，且请求的协议在集群中可用，且 ipFamilyPolicy 允许，则使用；否则服务创建将失败。 该字段修改是有条件的：它允许添加或删除辅助 IP 协议，但不允许更改服务的主要 IP 协议。 有效值为 “IPv4” 和 “IPv6”。 该字段仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型的服务，并且确实可用于“无头”服务。 更新服务设置类型为 ExternalName 时，该字段将被擦除。该字段最多可以包含两个条目（双栈系列，按任意顺序）。 如果指定，这些协议栈必须对应于 clusterIPs 字段的值。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 字段管理"}
        self.ip_families = ip_families
        # {"en":"IPFamilyPolicy represents the dual-stack-ness requested or required by this UpdateServiceService. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName", "zh_CN":"iPFamilyPolicy 表示此服务请求或要求的双栈特性。 如果没有提供值，则此字段将被设置为 SingleStack。 服务可以是 “SingleStack”（单个 IP 协议）、 “PreferDualStack”（双栈配置集群上的两个 IP 协议或单栈集群上的单个 IP 协议） 或 “RequireDualStack”（双栈上的两个 IP 协议配置的集群，否则失败）。 ipFamilies 和 clusterIPs 字段取决于此字段的值。 更新服务设置类型为 ExternalName 时，此字段将被擦除"}
        self.ip_family_policy = ip_family_policy
        # {"en":"allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer. Default is 'true'. It may be set to 'false' if the cluster load-balancer does not rely on NodePorts. If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type", "zh_CN":"allocateLoadBalancerNodePorts 定义了是否会自动为 LoadBalancer 类型的 UpdateServiceService 分配 NodePort。默认为 true。 如果集群负载均衡器不依赖 NodePort，则可以设置此字段为 false。 如果调用者（通过指定一个值）请求特定的 NodePort，则无论此字段如何，都会接受这些请求。 该字段只能设置在 type 为 LoadBalancer 的 UpdateServiceService 上，如果 type 更改为任何其他类型，该字段将被移除"}
        self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        # {"en":"loadBalancerClass is the class of the load balancer implementation this UpdateServiceService belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved for end-users. This field can only be set when the UpdateServiceService type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a UpdateServiceService to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type", "zh_CN":"loadBalancerClass 是此 UpdateServiceService 所属的负载均衡器实现的类。 如果设置了此字段，则字段值必须是标签风格的标识符，带有可选前缀，例如 ”internal-vip” 或 “example.com/internal-vip”。 无前缀名称是为最终用户保留的。该字段只能在 UpdateServiceService 类型为 “LoadBalancer” 时设置。 如果未设置此字段，则使用默认负载均衡器实现。默认负载均衡器现在通常通过云提供商集成完成，但应适用于任何默认实现。 如果设置了此字段，则假定负载均衡器实现正在监测具有对应负载均衡器类的 UpdateServiceService。 任何默认负载均衡器实现（例如云提供商）都应忽略设置此字段的 UpdateServiceService。 只有在创建或更新的 UpdateServiceService 的 type 为 “LoadBalancer” 时，才可设置此字段。 一经设定，不可更改。当 UpdateServiceService 的 type 更新为 “LoadBalancer” 之外的其他类型时，此字段将被移除"}
        self.load_balancer_class = load_balancer_class
        # {"en":"InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features)", "zh_CN":"InternalTrafficPolicy 描述节点如何分发它们在 ClusterIP 上接收到的服务流量。 如果设置为 “Local”，代理将假定 Pod 只想与在同一节点上的服务端点通信，如果没有本地端点，它将丢弃流量。 “Cluster” 默认将流量路由到所有端点（可能会根据拓扑和其他特性进行修改）"}
        self.internal_traffic_policy = internal_traffic_policy

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.session_affinity_config:
            self.session_affinity_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['selector'] = self.selector
        if self.cluster_ip is not None:
            result['clusterIP'] = self.cluster_ip
        if self.cluster_ips is not None:
            result['clusterIPs'] = self.cluster_ips
        if self.type is not None:
            result['type'] = self.type
        if self.external_ips is not None:
            result['externalIPs'] = self.external_ips
        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity
        if self.load_balancer_ip is not None:
            result['loadBalancerIP'] = self.load_balancer_ip
        if self.load_balancer_source_ranges is not None:
            result['loadBalancerSourceRanges'] = self.load_balancer_source_ranges
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.external_traffic_policy is not None:
            result['externalTrafficPolicy'] = self.external_traffic_policy
        if self.health_check_node_port is not None:
            result['healthCheckNodePort'] = self.health_check_node_port
        if self.publish_not_ready_addresses is not None:
            result['publishNotReadyAddresses'] = self.publish_not_ready_addresses
        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config.to_map()
        if self.ip_families is not None:
            result['ipFamilies'] = self.ip_families
        if self.ip_family_policy is not None:
            result['ipFamilyPolicy'] = self.ip_family_policy
        if self.allocate_load_balancer_node_ports is not None:
            result['allocateLoadBalancerNodePorts'] = self.allocate_load_balancer_node_ports
        if self.load_balancer_class is not None:
            result['loadBalancerClass'] = self.load_balancer_class
        if self.internal_traffic_policy is not None:
            result['internalTrafficPolicy'] = self.internal_traffic_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = UpdateServiceServicePort()
                self.ports.append(temp_model.from_map(k))
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('clusterIP') is not None:
            self.cluster_ip = m.get('clusterIP')
        if m.get('clusterIPs') is not None:
            self.cluster_ips = m.get('clusterIPs')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('externalIPs') is not None:
            self.external_ips = m.get('externalIPs')
        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')
        if m.get('loadBalancerIP') is not None:
            self.load_balancer_ip = m.get('loadBalancerIP')
        if m.get('loadBalancerSourceRanges') is not None:
            self.load_balancer_source_ranges = m.get('loadBalancerSourceRanges')
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('externalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('externalTrafficPolicy')
        if m.get('healthCheckNodePort') is not None:
            self.health_check_node_port = m.get('healthCheckNodePort')
        if m.get('publishNotReadyAddresses') is not None:
            self.publish_not_ready_addresses = m.get('publishNotReadyAddresses')
        if m.get('sessionAffinityConfig') is not None:
            temp_model = UpdateServiceSessionAffinityConfig()
            self.session_affinity_config = temp_model.from_map(m['sessionAffinityConfig'])
        if m.get('ipFamilies') is not None:
            self.ip_families = m.get('ipFamilies')
        if m.get('ipFamilyPolicy') is not None:
            self.ip_family_policy = m.get('ipFamilyPolicy')
        if m.get('allocateLoadBalancerNodePorts') is not None:
            self.allocate_load_balancer_node_ports = m.get('allocateLoadBalancerNodePorts')
        if m.get('loadBalancerClass') is not None:
            self.load_balancer_class = m.get('loadBalancerClass')
        if m.get('internalTrafficPolicy') is not None:
            self.internal_traffic_policy = m.get('internalTrafficPolicy')
        return self


class UpdateServicePortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"the port number of the service port of which status is recorded here", "zh_CN":"port 是所记录的服务端口状态的端口号"}
        self.port = port
        # {"en":"the protocol of the service port of which status is recorded here The supported values are: 'TCP', 'UDP', 'SCTP'", "zh_CN":"protocol 是所记录的服务端口状态的协议。支持的值为：“TCP”、”UDP”、“SCTP”"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use CamelCase names - cloud provider specific error values must have names that comply with the format foo.example.com/CamelCase", "zh_CN":"error 是记录 UpdateServiceService 端口的问题。 错误的格式应符合以下规则:内置错误原因应在此文件中指定，应使用 CamelCase 名称。云提供商特定错误原因的名称必须符合格式 foo.example.com/CamelCase"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class UpdateServiceLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        host_name: str = None,
        ports: List[UpdateServicePortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)", "zh_CN":"ip 是为基于 IP 的负载均衡器 Ingress 点（通常是 GCE 或 OpenStack 负载均衡器）设置的"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)", "zh_CN":"hostname 是为基于 DNS 的负载均衡器 Ingress 点（通常是 AWS 负载均衡器）设置的"}
        self.host_name = host_name
        # {"en":"Ports is a list of records of service ports If used, every port defined in the service should have an entry in it", "zh_CN":"ports 是 UpdateServiceService 的端口列表。如果设置了此字段，UpdateServiceService 中定义的每个端口都应该在此列表中"}
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = UpdateServicePortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class UpdateServiceLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[UpdateServiceLoadBalancerIngress] = None,
    ):
        # {"en":"Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points", "zh_CN":"ingress 是一个包含负载均衡器 Ingress 点的列表。UpdateServiceService 的流量需要被发送到这些 Ingress 点"}
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = UpdateServiceLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class UpdateServiceMetaV1Condition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        observed_generation: int = None,
        last_transition_time: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type of condition in CamelCase or in foo.example.com/CamelCase", "zh_CN":"CamelCase 或 foo.example.com/CamelCase 中的条件类型"}
        self.type = type
        # {"en":"status of the condition, one of True, False, Unknown", "zh_CN":"condition 的状态，True、False、Unknown 之一"}
        self.status = status
        # {"en":"observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance", "zh_CN":"表示设置 condition 基于的 .metadata.generation 的过期次数。 例如，如果 .metadata.generation 当前为 12，但 .status.conditions[x].observedGeneration 为 9， 则 condition 相对于实例的当前状态已过期"}
        self.observed_generation = observed_generation
        # {"en":"lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable", "zh_CN":"状况最近一次状态转化的时间。 变化应该发生在下层状况发生变化的时候。如果不知道下层状况发生变化的时间， 那么使用 API 字段更改的时间是可以接受的"}
        self.last_transition_time = last_transition_time
        # {"en":"reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty", "zh_CN":"reason 包含一个程序标识符，指示 condition 最后一次转换的原因。 特定条件类型的生产者可以定义该字段的预期值和含义，以及这些值是否被视为有保证的 API。 该值应该是 CamelCase 字符串且不能为空"}
        self.reason = reason
        # {"en":"message is a human readable message indicating details about the transition. This may be an empty string", "zh_CN":"message 是人类可读的消息，有关转换的详细信息，可以是空字符串"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateServiceServiceStatus(TeaModel):
    def __init__(
        self,
        load_balancer: UpdateServiceLoadBalancerStatus = None,
        conditions: List[UpdateServiceMetaV1Condition] = None,
    ):
        # {"en":"Current service state", "zh_CN":"loadBalancer 包含负载均衡器的当前状态（如果存在）"}
        self.load_balancer = load_balancer
        # {"en":"LoadBalancer contains the current status of the load-balancer, if one is present", "zh_CN":"服务的当前状态"}
        self.conditions = conditions

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = UpdateServiceLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = UpdateServiceMetaV1Condition()
                self.conditions.append(temp_model.from_map(k))
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateServiceObjectMeta = None,
        spec: UpdateServiceServiceSpec = None,
        status: UpdateServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 UpdateServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 UpdateServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdateServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdateServiceService(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateServiceObjectMeta = None,
        spec: UpdateServiceServiceSpec = None,
        status: UpdateServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 UpdateServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 UpdateServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdateServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateServiceService = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"service", "zh_CN":"service"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = UpdateServiceService()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"service name", "zh_CN":"service 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListServiceListMeta(TeaModel):
    def __init__(
        self,
        self_link: str = None,
        resource_version: str = None,
        continue_: str = None,
        remaining_item_count: int = None,
    ):
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system", "zh_CN":"selfLink 表示此对象的 URL，由系统填充，只读。已弃用：selfLink 是一个遗留的只读字段，不再由系统填充。"}
        self.self_link = self_link
        # {"en":"String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only", "zh_CN":"标识该对象的服务器内部版本的字符串，客户端可以用该字段来确定对象何时被更改。 该值对客户端是不透明的，并且应该原样传回给服务器。该值由系统填充，只读"}
        self.resource_version = resource_version
        # {"en":"continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message", "zh_CN":"如果用户对返回的条目数量设置了限制，则 continue 可能被设置，表示服务器有更多可用的数据。 该值是不透明的，可用于向提供此列表服务的端点发出另一个请求，以检索下一组可用的对象。 如果服务器配置已更改或时间已过去几分钟，则可能无法继续提供一致的列表。 除非你在错误消息中收到此令牌（token），否则使用此 continue 值时返回的 resourceVersion 字段应该和第一个响应中的值是相同的"}
        self.continue_ = continue_
        # {"en":"remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is estimating the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact", "zh_CN":"remainingItemCount 是列表中未包含在此列表响应中的后续项目的数量。 如果列表请求包含标签或字段选择器，则剩余项目的数量是未知的，并且在序列化期间该字段将保持未设置和省略。 如果列表是完整的（因为它没有分块或者这是最后一个块），那么就没有剩余的项目，并且在序列化过程中该字段将保持未设置和省略。 早于 v1.15 的服务器不设置此字段。remainingItemCount 的预期用途是估计集合的大小。 客户端不应依赖于设置准确的 remainingItemCount"}
        self.remaining_item_count = remaining_item_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.continue_ is not None:
            result['continue'] = self.continue_
        if self.remaining_item_count is not None:
            result['remainingItemCount'] = self.remaining_item_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('continue') is not None:
            self.continue_ = m.get('continue')
        if m.get('remainingItemCount') is not None:
            self.remaining_item_count = m.get('remainingItemCount')
        return self


class ListServiceOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class ListServiceFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListServiceManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListServiceFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListServiceManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListServiceFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListServiceFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListServiceFieldsV1 holds the first JSON version format as described in the 'ListServiceFieldsV1' type", "zh_CN":"ListServiceFieldsV1 包含类型 “ListServiceFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = ListServiceFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListServiceObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[ListServiceOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListServiceManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 ListServiceService 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = ListServiceOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListServiceManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListServiceServicePort(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        app_protocol: str = None,
        port: int = None,
        target_port: int = None,
        node_port: int = None,
    ):
        # {"en":"The name of this port within the service. This must be a DNS_LABEL. All ports within a ListServiceServiceSpec must have unique names. When considering the endpoints for a ListServiceService, this must match the 'name' field in the EndpointPort. Optional if only one ListServiceServicePort is defined on this service", "zh_CN":"ListServiceService 中此端口的名称。这必须是 DNS_LABEL。 ListServiceServiceSpec 中的所有端口的名称都必须唯一。 在考虑 ListServiceService 的端点时，这一字段值必须与 EndpointPort 中的 name 字段相同。 如果此服务上仅定义一个 ListServiceServicePort，则为此字段为可选"}
        self.name = name
        # {"en":"The IP protocol for this port. Supports TCP, UDP, and SCTP. Default is TCP", "zh_CN":"此端口的 IP 协议。支持 “TCP”、“UDP” 和 “SCTP”。默认为 TCP"}
        self.protocol = protocol
        # {"en":"The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol", "zh_CN":"此端口的应用协议，遵循标准的 Kubernetes 标签语法，无前缀名称按照 IANA 标准服务名称 （参见 RFC-6335 和 https://www.iana.org/assignments/service-names）。 非标准协议应该使用前缀名称，如 mycompany.com/my-custom-protocol"}
        self.app_protocol = app_protocol
        # {"en":"The port that will be exposed by this service", "zh_CN":"ListServiceService 将公开的端口"}
        self.port = port
        # {"en":"Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field", "zh_CN":"在 ListServiceService 所针对的 Pod 上要访问的端口号或名称。 编号必须在 1 到 65535 的范围内。名称必须是 IANA_SVC_NAME。 如果此值是一个字符串，将在目标 Pod 的容器端口中作为命名端口进行查找。 如果未指定字段，则使用 “port” 字段的值（直接映射）。 对于 clusterIP 为 None 的服务，此字段将被忽略， 应忽略不设或设置为 “port” 字段的取值"}
        self.target_port = target_port
        # {"en":"The port on each node on which this service is exposed when type is NodePort or LoadBalancer. Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail. If not specified, a port will be allocated if this ListServiceService requires one. If this field is specified when creating a ListServiceService which does not need it, creation will fail. This field will be wiped when updating a ListServiceService to no longer need it (e.g. changing type from NodePort to ClusterIP).", "zh_CN":"当类型为 NodePort 或 LoadBalancer 时，ListServiceService 公开在节点上的端口， 通常由系统分配。如果指定了一个在范围内且未使用的值，则将使用该值，否则操作将失败。 如果在创建的 ListServiceService 需要该端口时未指定该字段，则会分配端口。 如果在创建不需要该端口的 Service时指定了该字段，则会创建失败。 当更新 ListServiceService 时，如果不再需要此字段（例如，将类型从 NodePort 更改为 ClusterIP），这个字段将被擦除"}
        self.node_port = node_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.app_protocol is not None:
            result['appProtocol'] = self.app_protocol
        if self.port is not None:
            result['port'] = self.port
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        if self.node_port is not None:
            result['nodePort'] = self.node_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('appProtocol') is not None:
            self.app_protocol = m.get('appProtocol')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        if m.get('nodePort') is not None:
            self.node_port = m.get('nodePort')
        return self


class ListServiceClientIPConfig(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
    ):
        # {"en":"timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3 hours).", "zh_CN":"timeoutSeconds 指定 ClientIP 类型会话的维系时间秒数。 如果 ServiceAffinity == 'ClientIP'，则该值必须 >0 && <=86400（1 天）。默认值为 10800（3 小时）"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class ListServiceSessionAffinityConfig(TeaModel):
    def __init__(
        self,
        client_ip: ListServiceClientIPConfig = None,
    ):
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"clientIP 包含基于客户端 IP 的会话亲和性的配置"}
        self.client_ip = client_ip

    def validate(self):
        if self.client_ip:
            self.client_ip.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIP') is not None:
            temp_model = ListServiceClientIPConfig()
            self.client_ip = temp_model.from_map(m['clientIP'])
        return self


class ListServiceServiceSpec(TeaModel):
    def __init__(
        self,
        ports: List[ListServiceServicePort] = None,
        selector: Dict[str, str] = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        type: str = None,
        external_ips: List[str] = None,
        session_affinity: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        publish_not_ready_addresses: bool = None,
        session_affinity_config: ListServiceSessionAffinityConfig = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        allocate_load_balancer_node_ports: bool = None,
        load_balancer_class: str = None,
        internal_traffic_policy: str = None,
    ):
        # {"en":"The list of ports that are exposed by this service", "zh_CN":"此 ListServiceService 公开的端口列表"}
        self.ports = ports
        # {"en":"Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName", "zh_CN":"将 ListServiceService 流量路由到具有与此 selector 匹配的标签键值对的 Pod。 如果为空或不存在，则假定该服务有一个外部进程管理其端点，Kubernetes 不会修改该端点。 仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型。如果类型为 ExternalName，则忽略"}
        self.selector = selector
        # {"en":"clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a ListServiceService of type ExternalName, creation will fail. This field will be wiped when updating a ListServiceService to type ExternalName", "zh_CN":"clusterIP 是服务的 IP 地址，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给服务，否则创建服务将失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIP 为空）或 type 已经是 ExternalName 时，可以更改 clusterIP（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIP 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 仅适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 ListServiceService 时指定了 clusterIP，则创建将失败。 更新 ListServiceService type 为 ExternalName 时，clusterIP 会被移除"}
        self.cluster_ip = cluster_ip
        # {"en":"ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a ListServiceService of type ExternalName, creation will fail. This field will be wiped when updating a ListServiceService to type ExternalName. If this field is not specified, it will be initialized from the clusterIP field. If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"clusterIPs 是分配给该 ListServiceService 的 IP 地址列表，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给 ListServiceService；否则创建 ListServiceService 失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIPs 为空）或 type 已经是 ExternalName 时，可以更改 clusterIPs（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIPs 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 ListServiceService 时指定了 clusterIPs，则会创建失败。 更新 ListServiceService type 为 ExternalName 时，该字段将被移除。如果未指定此字段，则将从 clusterIP 字段初始化。 如果指定 clusterIPs，客户端必须确保 clusterIPs[0] 和 clusterIP 一致。clusterIPs 最多可包含两个条目（双栈系列，按任意顺序）。 这些 IP 必须与 ipFamilies 的值相对应。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 管理"}
        self.cluster_ips = cluster_ips
        # {"en":"type determines how the ListServiceService is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName. Several other fields do not apply to ExternalName services", "zh_CN":"type 确定 ListServiceService 的公开方式。默认为 ClusterIP。 有效选项为 ExternalName、ClusterIP、NodePort 和 LoadBalancer。 “ClusterIP” 为端点分配一个集群内部 IP 地址用于负载均衡。 Endpoints 由 selector 确定，如果未设置 selector，则需要通过手动构造 Endpoints 或 EndpointSlice 的对象来确定。 如果 clusterIP 为 “None”，则不分配虚拟 IP，并且 Endpoints 作为一组端点而不是虚拟 IP 发布。 “NodePort” 建立在 ClusterIP 之上，并在每个节点上分配一个端口，该端口路由到与 clusterIP 相同的 Endpoints。 “LoadBalancer” 基于 NodePort 构建并创建一个外部负载均衡器（如果当前云支持），该负载均衡器路由到与 clusterIP 相同的 Endpoints。 “externalName” 将此 ListServiceService 别名为指定的 externalName。其他几个字段不适用于 ExternalName ListServiceService"}
        self.type = type
        # {"en":"externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system", "zh_CN":"externalIPs 是一个 IP 列表，集群中的节点会为此 ListServiceService 接收针对这些 IP 地址的流量。 这些 IP 不被 Kubernetes 管理。用户需要确保流量可以到达具有此 IP 的节点。 一个常见的例子是不属于 Kubernetes 系统的外部负载均衡器"}
        self.external_ips = external_ips
        # {"en":"Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None", "zh_CN":"支持 “ClientIP” 和 “None”。用于维护会话亲和性。 启用基于客户端 IP 的会话亲和性。必须是 ClientIP 或 None。默认为 None"}
        self.session_affinity = session_affinity
        # {"en":"Only applies to ListServiceService Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations, and it cannot support dual-stack. As of Kubernetes v1.24, users are encouraged to use implementation-specific annotations when available. This field may be removed in a future API version", "zh_CN":"仅适用于服务类型: LoadBalancer。此功能取决于底层云提供商是否支持负载均衡器。 如果云提供商不支持该功能，该字段将被忽略。 已弃用: 该字段信息不足，且其含义因实现而异，而且不支持双栈。 从 Kubernetes v1.24 开始，鼓励用户在可用时使用特定于实现的注释。在未来的 API 版本中可能会删除此字段"}
        self.load_balancer_ip = load_balancer_ip
        # {"en":"If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature", "zh_CN":"如果设置了此字段并且被平台支持，将限制通过云厂商的负载均衡器的流量到指定的客户端 IP。 如果云提供商不支持该功能，该字段将被忽略"}
        self.load_balancer_source_ranges = load_balancer_source_ranges
        # {"en":"externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved. Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires type to be 'ExternalName'", "zh_CN":"externalName 是发现机制将返回的外部引用，作为此服务的别名（例如 DNS CNAME 记录）。 不涉及代理。必须是小写的 RFC-1123 主机名 (https://tools.ietf.org/html/rfc1123)， 并且要求 type 为 “ExternalName”"}
        self.external_name = external_name
        # {"en":"externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the ListServiceService's 'externally-facing' addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node", "zh_CN":"externalTrafficPolicy 描述了节点如何分发它们在 ListServiceService 的“外部访问”地址 （NodePort、ExternalIP 和 LoadBalancer IP）接收到的服务流量。 如果设置为 “Local”，代理将以一种假设外部负载均衡器将负责在节点之间服务流量负载均衡， 因此每个节点将仅向服务的节点本地端点传递流量，而不会伪装客户端源 IP。 （将丢弃错误发送到没有端点的节点的流量。） “Cluster” 默认值使用负载均衡路由到所有端点的策略（可能会根据拓扑和其他特性进行修改）。 请注意，从集群内部发送到 External IP 或 LoadBalancer IP 的流量始终具有 “Cluster” 语义， 但是从集群内部发送到 NodePort 的客户端需要在选择节点时考虑流量路由策略"}
        self.external_traffic_policy = external_traffic_policy
        # {"en":"healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used. If not specified, a value will be automatically allocated. External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not. If this field is specified when creating a ListServiceService which does not need it, creation will fail. This field will be wiped when updating a ListServiceService to no longer need it (e.g. changing type). This field cannot be updated once set", "zh_CN":"healthCheckNodePort 指定 ListServiceService 的健康检查节点端口。 仅适用于 type 为 LoadBalancer 且 externalTrafficPolicy 设置为 Local 的情况。 如果为此字段设定了一个值，该值在合法范围内且没有被使用，则使用所指定的值。 如果未设置此字段，则自动分配字段值。外部系统（例如负载平衡器）可以使用此端口来确定给定节点是否拥有此服务的端点。 在创建不需要 healthCheckNodePort 的 ListServiceService 时指定了此字段，则 ListServiceService 创建会失败。 要移除 healthCheckNodePort，需要更改 ListServiceService 的 type。 该字段一旦设置就无法更改"}
        self.health_check_node_port = health_check_node_port
        # {"en":"publishNotReadyAddresses indicates that any agent which deals with endpoints for this ListServiceService should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless ListServiceService to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered 'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior", "zh_CN":"publishNotReadyAddresses 表示任何处理此 ListServiceService 端点的代理都应忽略任何准备就绪/未准备就绪的指示。 设置此字段的主要场景是为 StatefulSet 的服务提供支持，使之能够为其 Pod 传播 SRV DNS 记录，以实现对等发现。 为 ListServiceService 生成 Endpoints 和 EndpointSlice 资源的 Kubernetes 控制器对字段的解读是， 即使 Pod 本身还没有准备好，所有端点都可被视为 “已就绪”。 对于代理而言，如果仅使用 Kubernetes 通过 Endpoints 或 EndpointSlice 资源所生成的端点， 则可以安全地假设这种行为"}
        self.publish_not_ready_addresses = publish_not_ready_addresses
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"sessionAffinityConfig 包含会话亲和性的配置"}
        self.session_affinity_config = session_affinity_config
        # {"en":"IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the ListServiceService. Valid values are 'IPv4' and 'IPv6'. This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to 'headless' services. This field will be wiped when updating a ListServiceService to type ExternalName.This field may hold a maximum of two entries (dual-stack families, in either order). These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"iPFamilies 是分配给此服务的 IP 协议（例如 IPv4、IPv6）的列表。 该字段通常根据集群配置和 ipFamilyPolicy 字段自动设置。 如果手动指定该字段，且请求的协议在集群中可用，且 ipFamilyPolicy 允许，则使用；否则服务创建将失败。 该字段修改是有条件的：它允许添加或删除辅助 IP 协议，但不允许更改服务的主要 IP 协议。 有效值为 “IPv4” 和 “IPv6”。 该字段仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型的服务，并且确实可用于“无头”服务。 更新服务设置类型为 ExternalName 时，该字段将被擦除。该字段最多可以包含两个条目（双栈系列，按任意顺序）。 如果指定，这些协议栈必须对应于 clusterIPs 字段的值。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 字段管理"}
        self.ip_families = ip_families
        # {"en":"IPFamilyPolicy represents the dual-stack-ness requested or required by this ListServiceService. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName", "zh_CN":"iPFamilyPolicy 表示此服务请求或要求的双栈特性。 如果没有提供值，则此字段将被设置为 SingleStack。 服务可以是 “SingleStack”（单个 IP 协议）、 “PreferDualStack”（双栈配置集群上的两个 IP 协议或单栈集群上的单个 IP 协议） 或 “RequireDualStack”（双栈上的两个 IP 协议配置的集群，否则失败）。 ipFamilies 和 clusterIPs 字段取决于此字段的值。 更新服务设置类型为 ExternalName 时，此字段将被擦除"}
        self.ip_family_policy = ip_family_policy
        # {"en":"allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer. Default is 'true'. It may be set to 'false' if the cluster load-balancer does not rely on NodePorts. If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type", "zh_CN":"allocateLoadBalancerNodePorts 定义了是否会自动为 LoadBalancer 类型的 ListServiceService 分配 NodePort。默认为 true。 如果集群负载均衡器不依赖 NodePort，则可以设置此字段为 false。 如果调用者（通过指定一个值）请求特定的 NodePort，则无论此字段如何，都会接受这些请求。 该字段只能设置在 type 为 LoadBalancer 的 ListServiceService 上，如果 type 更改为任何其他类型，该字段将被移除"}
        self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        # {"en":"loadBalancerClass is the class of the load balancer implementation this ListServiceService belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved for end-users. This field can only be set when the ListServiceService type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a ListServiceService to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type", "zh_CN":"loadBalancerClass 是此 ListServiceService 所属的负载均衡器实现的类。 如果设置了此字段，则字段值必须是标签风格的标识符，带有可选前缀，例如 ”internal-vip” 或 “example.com/internal-vip”。 无前缀名称是为最终用户保留的。该字段只能在 ListServiceService 类型为 “LoadBalancer” 时设置。 如果未设置此字段，则使用默认负载均衡器实现。默认负载均衡器现在通常通过云提供商集成完成，但应适用于任何默认实现。 如果设置了此字段，则假定负载均衡器实现正在监测具有对应负载均衡器类的 ListServiceService。 任何默认负载均衡器实现（例如云提供商）都应忽略设置此字段的 ListServiceService。 只有在创建或更新的 ListServiceService 的 type 为 “LoadBalancer” 时，才可设置此字段。 一经设定，不可更改。当 ListServiceService 的 type 更新为 “LoadBalancer” 之外的其他类型时，此字段将被移除"}
        self.load_balancer_class = load_balancer_class
        # {"en":"InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features)", "zh_CN":"InternalTrafficPolicy 描述节点如何分发它们在 ClusterIP 上接收到的服务流量。 如果设置为 “Local”，代理将假定 Pod 只想与在同一节点上的服务端点通信，如果没有本地端点，它将丢弃流量。 “Cluster” 默认将流量路由到所有端点（可能会根据拓扑和其他特性进行修改）"}
        self.internal_traffic_policy = internal_traffic_policy

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.session_affinity_config:
            self.session_affinity_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['selector'] = self.selector
        if self.cluster_ip is not None:
            result['clusterIP'] = self.cluster_ip
        if self.cluster_ips is not None:
            result['clusterIPs'] = self.cluster_ips
        if self.type is not None:
            result['type'] = self.type
        if self.external_ips is not None:
            result['externalIPs'] = self.external_ips
        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity
        if self.load_balancer_ip is not None:
            result['loadBalancerIP'] = self.load_balancer_ip
        if self.load_balancer_source_ranges is not None:
            result['loadBalancerSourceRanges'] = self.load_balancer_source_ranges
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.external_traffic_policy is not None:
            result['externalTrafficPolicy'] = self.external_traffic_policy
        if self.health_check_node_port is not None:
            result['healthCheckNodePort'] = self.health_check_node_port
        if self.publish_not_ready_addresses is not None:
            result['publishNotReadyAddresses'] = self.publish_not_ready_addresses
        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config.to_map()
        if self.ip_families is not None:
            result['ipFamilies'] = self.ip_families
        if self.ip_family_policy is not None:
            result['ipFamilyPolicy'] = self.ip_family_policy
        if self.allocate_load_balancer_node_ports is not None:
            result['allocateLoadBalancerNodePorts'] = self.allocate_load_balancer_node_ports
        if self.load_balancer_class is not None:
            result['loadBalancerClass'] = self.load_balancer_class
        if self.internal_traffic_policy is not None:
            result['internalTrafficPolicy'] = self.internal_traffic_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = ListServiceServicePort()
                self.ports.append(temp_model.from_map(k))
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('clusterIP') is not None:
            self.cluster_ip = m.get('clusterIP')
        if m.get('clusterIPs') is not None:
            self.cluster_ips = m.get('clusterIPs')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('externalIPs') is not None:
            self.external_ips = m.get('externalIPs')
        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')
        if m.get('loadBalancerIP') is not None:
            self.load_balancer_ip = m.get('loadBalancerIP')
        if m.get('loadBalancerSourceRanges') is not None:
            self.load_balancer_source_ranges = m.get('loadBalancerSourceRanges')
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('externalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('externalTrafficPolicy')
        if m.get('healthCheckNodePort') is not None:
            self.health_check_node_port = m.get('healthCheckNodePort')
        if m.get('publishNotReadyAddresses') is not None:
            self.publish_not_ready_addresses = m.get('publishNotReadyAddresses')
        if m.get('sessionAffinityConfig') is not None:
            temp_model = ListServiceSessionAffinityConfig()
            self.session_affinity_config = temp_model.from_map(m['sessionAffinityConfig'])
        if m.get('ipFamilies') is not None:
            self.ip_families = m.get('ipFamilies')
        if m.get('ipFamilyPolicy') is not None:
            self.ip_family_policy = m.get('ipFamilyPolicy')
        if m.get('allocateLoadBalancerNodePorts') is not None:
            self.allocate_load_balancer_node_ports = m.get('allocateLoadBalancerNodePorts')
        if m.get('loadBalancerClass') is not None:
            self.load_balancer_class = m.get('loadBalancerClass')
        if m.get('internalTrafficPolicy') is not None:
            self.internal_traffic_policy = m.get('internalTrafficPolicy')
        return self


class ListServicePortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"the port number of the service port of which status is recorded here", "zh_CN":"port 是所记录的服务端口状态的端口号"}
        self.port = port
        # {"en":"the protocol of the service port of which status is recorded here The supported values are: 'TCP', 'UDP', 'SCTP'", "zh_CN":"protocol 是所记录的服务端口状态的协议。支持的值为：“TCP”、”UDP”、“SCTP”"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use CamelCase names - cloud provider specific error values must have names that comply with the format foo.example.com/CamelCase", "zh_CN":"error 是记录 ListServiceService 端口的问题。 错误的格式应符合以下规则:内置错误原因应在此文件中指定，应使用 CamelCase 名称。云提供商特定错误原因的名称必须符合格式 foo.example.com/CamelCase"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class ListServiceLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        host_name: str = None,
        ports: List[ListServicePortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)", "zh_CN":"ip 是为基于 IP 的负载均衡器 Ingress 点（通常是 GCE 或 OpenStack 负载均衡器）设置的"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)", "zh_CN":"hostname 是为基于 DNS 的负载均衡器 Ingress 点（通常是 AWS 负载均衡器）设置的"}
        self.host_name = host_name
        # {"en":"Ports is a list of records of service ports If used, every port defined in the service should have an entry in it", "zh_CN":"ports 是 ListServiceService 的端口列表。如果设置了此字段，ListServiceService 中定义的每个端口都应该在此列表中"}
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = ListServicePortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class ListServiceLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[ListServiceLoadBalancerIngress] = None,
    ):
        # {"en":"Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points", "zh_CN":"ingress 是一个包含负载均衡器 Ingress 点的列表。ListServiceService 的流量需要被发送到这些 Ingress 点"}
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = ListServiceLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class ListServiceMetaV1Condition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        observed_generation: int = None,
        last_transition_time: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type of condition in CamelCase or in foo.example.com/CamelCase", "zh_CN":"CamelCase 或 foo.example.com/CamelCase 中的条件类型"}
        self.type = type
        # {"en":"status of the condition, one of True, False, Unknown", "zh_CN":"condition 的状态，True、False、Unknown 之一"}
        self.status = status
        # {"en":"observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance", "zh_CN":"表示设置 condition 基于的 .metadata.generation 的过期次数。 例如，如果 .metadata.generation 当前为 12，但 .status.conditions[x].observedGeneration 为 9， 则 condition 相对于实例的当前状态已过期"}
        self.observed_generation = observed_generation
        # {"en":"lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable", "zh_CN":"状况最近一次状态转化的时间。 变化应该发生在下层状况发生变化的时候。如果不知道下层状况发生变化的时间， 那么使用 API 字段更改的时间是可以接受的"}
        self.last_transition_time = last_transition_time
        # {"en":"reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty", "zh_CN":"reason 包含一个程序标识符，指示 condition 最后一次转换的原因。 特定条件类型的生产者可以定义该字段的预期值和含义，以及这些值是否被视为有保证的 API。 该值应该是 CamelCase 字符串且不能为空"}
        self.reason = reason
        # {"en":"message is a human readable message indicating details about the transition. This may be an empty string", "zh_CN":"message 是人类可读的消息，有关转换的详细信息，可以是空字符串"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListServiceServiceStatus(TeaModel):
    def __init__(
        self,
        load_balancer: ListServiceLoadBalancerStatus = None,
        conditions: List[ListServiceMetaV1Condition] = None,
    ):
        # {"en":"Current service state", "zh_CN":"loadBalancer 包含负载均衡器的当前状态（如果存在）"}
        self.load_balancer = load_balancer
        # {"en":"LoadBalancer contains the current status of the load-balancer, if one is present", "zh_CN":"服务的当前状态"}
        self.conditions = conditions

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = ListServiceLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = ListServiceMetaV1Condition()
                self.conditions.append(temp_model.from_map(k))
        return self


class ListServiceService(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListServiceObjectMeta = None,
        spec: ListServiceServiceSpec = None,
        status: ListServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 ListServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 ListServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ListServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class ListServiceServiceList(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: ListServiceListMeta = None,
        items: List[ListServiceService] = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of services", "zh_CN":"ListServiceService 列表"}
        self.items = items

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = ListServiceListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListServiceService()
                self.items.append(temp_model.from_map(k))
        return self


class ListServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListServiceServiceList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"service list", "zh_CN":"service 列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListServiceServiceList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class ListServiceParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"service name", "zh_CN":"service 名称"}
        self.name = name
        # {"en":"labelSelector", "zh_CN":"labelSelector"}
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQueryAvailableCidrsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsResponse(TeaModel):
    def __init__(
        self,
        cidrs: List[str] = None,
    ):
        # {"en":"available cidrs", "zh_CN":"可用的cidr列表"}
        self.cidrs = cidrs

    def validate(self):
        self.validate_required(self.cidrs, 'cidrs')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['cidrs'] = self.cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidrs') is not None:
            self.cidrs = m.get('cidrs')
        return self


class VMPQueryAvailableCidrsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsParameters(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # {"en":"node name", "zh_CN":"节点英文名称"}
        self.node_name = node_name

    def validate(self):
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class VMPQueryAvailableCidrsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryAvailableCidrsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPUnassignEdgePrivateIPRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"target virtual machine id", "zh_CN":"目标实例id"}
        self.instance_id = instance_id
        # {"en":"additional Ip to unbind", "zh_CN":"要解除绑定的额外内网IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPUnassignEdgePrivateIPVMPEdgeIPMapping(TeaModel):
    def __init__(
        self,
        edge_private_ip: str = None,
        edge_public_ip: str = None,
    ):
        # {"en":"edge private ip", "zh_CN":"额外内网IP"}
        self.edge_private_ip = edge_private_ip
        # {"en":"edge public IP", "zh_CN":"额外公网IP"}
        self.edge_public_ip = edge_public_ip

    def validate(self):
        self.validate_required(self.edge_private_ip, 'edge_private_ip')
        self.validate_required(self.edge_public_ip, 'edge_public_ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_private_ip is not None:
            result['edgePrivateIp'] = self.edge_private_ip
        if self.edge_public_ip is not None:
            result['edgePublicIp'] = self.edge_public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgePrivateIp') is not None:
            self.edge_private_ip = m.get('edgePrivateIp')
        if m.get('edgePublicIp') is not None:
            self.edge_public_ip = m.get('edgePublicIp')
        return self


class VMPUnassignEdgePrivateIPResponse(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        edge_ips: List[VMPUnassignEdgePrivateIPVMPEdgeIPMapping] = None,
    ):
        # {"en":"target virtual machine id", "zh_CN":"目标实例ID"}
        self.instance_id = instance_id
        # {"en":"Additional IP that is bound to the instance", "zh_CN":"已绑定到目标实例的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.edge_ips, 'edge_ips')
        if self.edge_ips:
            for k in self.edge_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.edge_ips is not None:
            result['edgeIps'] = []
            for k in self.edge_ips:
                result['edgeIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('edgeIps') is not None:
            self.edge_ips = []
            for k in m.get('edgeIps'):
                temp_model = VMPUnassignEdgePrivateIPVMPEdgeIPMapping()
                self.edge_ips.append(temp_model.from_map(k))
        return self


class VMPUnassignEdgePrivateIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgePrivateIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgePrivateIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgePrivateIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPReleaseEdgeIPRequest(TeaModel):
    def __init__(
        self,
        edge_ips: List[str] = None,
    ):
        # {"en":"additional IP to be released", "zh_CN":"要释放的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPReleaseEdgeIPResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgeIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgeIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgeIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgeIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateNetworkPolicyOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class UpdateNetworkPolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateNetworkPolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateNetworkPolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateNetworkPolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateNetworkPolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateNetworkPolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateNetworkPolicyFieldsV1 holds the first JSON version format as described in the 'UpdateNetworkPolicyFieldsV1' type", "zh_CN":"UpdateNetworkPolicyFieldsV1 包含类型 “UpdateNetworkPolicyFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = UpdateNetworkPolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateNetworkPolicyObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[UpdateNetworkPolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateNetworkPolicyManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = UpdateNetworkPolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateNetworkPolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateNetworkPolicyNetworkPolicyPort(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # {"en": "The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.", "zh_CN": "端口"}
        self.port = port
        # {"en": "The protocol (TCP, UDP) which traffic must match. If not specified, this field defaults to TCP.", "zh_CN": "协议"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class UpdateNetworkPolicyIPBlock(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        except_: List[str] = None,
    ):
        # {"en": "CIDR is a string representing the IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64", "zh_CN": "生效IP网段"}
        self.cidr = cidr
        # {"en": "Except is a slice of CIDRs that should not be included within an IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64 Except values will be rejected if they are outside the CIDR range", "zh_CN": "例外IP网段"}
        self.except_ = except_

    def validate(self):
        self.validate_required(self.cidr, 'cidr')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.except_ is not None:
            result['except'] = self.except_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('except') is not None:
            self.except_ = m.get('except')
        return self


class UpdateNetworkPolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateNetworkPolicyNsLabelSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[UpdateNetworkPolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = UpdateNetworkPolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdateNetworkPolicyPodLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self


class UpdateNetworkPolicyNetworkPolicyPeer(TeaModel):
    def __init__(
        self,
        ip_block: UpdateNetworkPolicyIPBlock = None,
        namespace_selector: UpdateNetworkPolicyNsLabelSelector = None,
        pod_selector: UpdateNetworkPolicyPodLabelSelector = None,
    ):
        # {"en": "UpdateNetworkPolicyIPBlock defines policy on a particular UpdateNetworkPolicyIPBlock. If this field is set then neither of the other fields can be.", "zh_CN": "IP规则"}
        self.ip_block = ip_block
        # {"en": "Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.If PodSelector is also set, then the UpdateNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.", "zh_CN": "namespace选择器"}
        self.namespace_selector = namespace_selector
        # {"en": "This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.If NamespaceSelector is also set, then the UpdateNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.", "zh_CN": "pod选择器"}
        self.pod_selector = pod_selector

    def validate(self):
        if self.ip_block:
            self.ip_block.validate()
        if self.namespace_selector:
            self.namespace_selector.validate()
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_block is not None:
            result['ipBlock'] = self.ip_block.to_map()
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_map()
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipBlock') is not None:
            temp_model = UpdateNetworkPolicyIPBlock()
            self.ip_block = temp_model.from_map(m['ipBlock'])
        if m.get('namespaceSelector') is not None:
            temp_model = UpdateNetworkPolicyNsLabelSelector()
            self.namespace_selector = temp_model.from_map(m['namespaceSelector'])
        if m.get('podSelector') is not None:
            temp_model = UpdateNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        return self


class UpdateNetworkPolicyNetworkPolicyEgressRule(TeaModel):
    def __init__(
        self,
        ports: List[UpdateNetworkPolicyNetworkPolicyPort] = None,
        to: List[UpdateNetworkPolicyNetworkPolicyPeer] = None,
    ):
        # {"en": "List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports
        # {"en": "List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.", "zh_CN": "出网规则信息"}
        self.to = to

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.to:
            for k in self.to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.to is not None:
            result['to'] = []
            for k in self.to:
                result['to'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = UpdateNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('to') is not None:
            self.to = []
            for k in m.get('to'):
                temp_model = UpdateNetworkPolicyNetworkPolicyPeer()
                self.to.append(temp_model.from_map(k))
        return self


class UpdateNetworkPolicyNetworkPolicyIngressRule(TeaModel):
    def __init__(
        self,
        from_: List[UpdateNetworkPolicyNetworkPolicyPeer] = None,
        ports: List[UpdateNetworkPolicyNetworkPolicyPort] = None,
    ):
        # {"en": "List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.", "zh_CN": "入网规则信息"}
        self.from_ = from_
        # {"en": "List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports

    def validate(self):
        if self.from_:
            for k in self.from_:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = []
            for k in self.from_:
                result['from'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = []
            for k in m.get('from'):
                temp_model = UpdateNetworkPolicyNetworkPolicyPeer()
                self.from_.append(temp_model.from_map(k))
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = UpdateNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        return self


class UpdateNetworkPolicyNetworkPolicySpec(TeaModel):
    def __init__(
        self,
        egress: List[UpdateNetworkPolicyNetworkPolicyEgressRule] = None,
        ingress: List[UpdateNetworkPolicyNetworkPolicyIngressRule] = None,
        pod_selector: UpdateNetworkPolicyPodLabelSelector = None,
        policy_types: List[str] = None,
    ):
        # {"en": "List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the UpdateNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this UpdateNetworkPolicyNetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8", "zh_CN": "出网规则"}
        self.egress = egress
        # {"en": "List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the UpdateNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this UpdateNetworkPolicyNetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)", "zh_CN": "入网规则"}
        self.ingress = ingress
        # {"en": "Selects the pods to which this UpdateNetworkPolicyNetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.", "zh_CN": "限制pod的选择器"}
        self.pod_selector = pod_selector
        # {"en": "List of rule types that the UpdateNetworkPolicyNetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ Egress ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include Egress (since such a policy would not include an Egress section and would otherwise default to just [ Ingress ]). This field is beta-level in 1.8", "zh_CN": "策略类型"}
        self.policy_types = policy_types

    def validate(self):
        if self.egress:
            for k in self.egress:
                if k:
                    k.validate()
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()
        self.validate_required(self.pod_selector, 'pod_selector')
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress is not None:
            result['egress'] = []
            for k in self.egress:
                result['egress'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        if self.policy_types is not None:
            result['policyTypes'] = self.policy_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('egress') is not None:
            self.egress = []
            for k in m.get('egress'):
                temp_model = UpdateNetworkPolicyNetworkPolicyEgressRule()
                self.egress.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = UpdateNetworkPolicyNetworkPolicyIngressRule()
                self.ingress.append(temp_model.from_map(k))
        if m.get('podSelector') is not None:
            temp_model = UpdateNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        if m.get('policyTypes') is not None:
            self.policy_types = m.get('policyTypes')
        return self


class UpdateNetworkPolicyRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateNetworkPolicyObjectMeta = None,
        spec: UpdateNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this UpdateNetworkPolicyNetworkPolicy.", "zh_CN": "UpdateNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdateNetworkPolicyNetworkPolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateNetworkPolicyObjectMeta = None,
        spec: UpdateNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this UpdateNetworkPolicyNetworkPolicy.", "zh_CN": "UpdateNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdateNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateNetworkPolicyNetworkPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"networkPolicy", "zh_CN":"网络策略"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = UpdateNetworkPolicyNetworkPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"networkPolicy name", "zh_CN":"networkPolicy 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateNetworkPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPReleaseEdgePrivateIPRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"node name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"additional IP to be released", "zh_CN":"要释放的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPReleaseEdgePrivateIPResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgePrivateIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgePrivateIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgePrivateIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPReleaseEdgePrivateIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteNetworkPolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteNetworkPolicyStatusDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        group: str = None,
        uid: str = None,
    ):
        # {"en":"The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described)", "zh_CN":"与状态 StatusReason 关联的资源的名称属性（当有一个可以描述的名称时）"}
        self.name = name
        # {"en":"The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind", "zh_CN":"与状态 StatusReason 关联的资源的种类属性"}
        self.kind = kind
        # {"en":"The group attribute of the resource associated with the status StatusReason", "zh_CN":"与状态 StatusReason 关联的资源的组属性"}
        self.group = group
        # {"en":"UID of the resource. (when there is a single resource which can be described)", "zh_CN":"资源的 UID（当有单个可以描述的资源时）"}
        self.uid = uid

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.group, 'group')
        self.validate_required(self.uid, 'uid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.group is not None:
            result['group'] = self.group
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class DeleteNetworkPolicyStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteNetworkPolicyStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteNetworkPolicyStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
        self.status = status
        # {"en":"Suggested HTTP return code for this status, 0 if not set", "zh_CN":"此状态的建议 HTTP 返回代码，如果未设置，则为 0"}
        self.code = code
        # {"en":"Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type", "zh_CN":"与原因（Reason）相关的扩展数据。每个原因都可以定义自己的扩展细节。 此字段是可选的，并且不保证返回的数据符合任何模式，除非由原因类型定义"}
        self.details = details

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.status, 'status')
        self.validate_required(self.code, 'code')
        self.validate_required(self.details, 'details')
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.status is not None:
            result['status'] = self.status
        if self.code is not None:
            result['code'] = self.code
        if self.details is not None:
            result['details'] = self.details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('details') is not None:
            temp_model = DeleteNetworkPolicyStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteNetworkPolicyStatus = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"status", "zh_CN":"status"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = DeleteNetworkPolicyStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"networkPolicy name", "zh_CN":"networkPolicy 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteNetworkPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateIngressOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class CreateIngressFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateIngressFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateIngressManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateIngressFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateIngressFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateIngressFieldsV1 holds the first JSON version format as described in the 'CreateIngressFieldsV1' type", "zh_CN":"CreateIngressFieldsV1 包含类型 “CreateIngressFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = CreateIngressFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateIngressObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[CreateIngressOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateIngressManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = CreateIngressOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateIngressManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateIngressServiceBackendPort(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
    ):
        # {"en":"Name is the name of the port on the Service", "zh_CN":"服务端口名称"}
        self.name = name
        # {"en":"Number is the numerical port number on the Service", "zh_CN":"服务数字端口"}
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class CreateIngressIngressServiceBackend(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: CreateIngressServiceBackendPort = None,
    ):
        # {"en":"Name is the referenced service", "zh_CN":"服务名称"}
        self.name = name
        # {"en":"Port of the referenced service. A port name or port number", "zh_CN":"服务端口或端口名称"}
        self.port = port

    def validate(self):
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            temp_model = CreateIngressServiceBackendPort()
            self.port = temp_model.from_map(m['port'])
        return self


class CreateIngressTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        api_group: str = None,
    ):
        # {"en":"Name is the name of resource being referenced", "zh_CN":"资源名称"}
        self.name = name
        # {"en":"Kind is the type of resource being referenced", "zh_CN":"资源类型"}
        self.kind = kind
        # {"en":"APIGroup is the group for the resource being referenced", "zh_CN":"资源分组"}
        self.api_group = api_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        return self


class CreateIngressIngressBackend(TeaModel):
    def __init__(
        self,
        service: CreateIngressIngressServiceBackend = None,
        resource: CreateIngressTypedLocalObjectReference = None,
    ):
        # {"en":"Service references a Service as a Backend", "zh_CN":"指定后端服务"}
        self.service = service
        # {"en":"Resource is an ObjectRef to another Kubernetes resource in the namespace of the CreateIngressIngress object", "zh_CN":"路由指定后端资源"}
        self.resource = resource

    def validate(self):
        if self.service:
            self.service.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['service'] = self.service.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service') is not None:
            temp_model = CreateIngressIngressServiceBackend()
            self.service = temp_model.from_map(m['service'])
        if m.get('resource') is not None:
            temp_model = CreateIngressTypedLocalObjectReference()
            self.resource = temp_model.from_map(m['resource'])
        return self


class CreateIngressIngressTLS(TeaModel):
    def __init__(
        self,
        hosts: List[str] = None,
        secret_name: str = None,
    ):
        # {"en":"Hosts are a list of hosts included in the TLS certificate", "zh_CN":"tls证书包含域名"}
        self.hosts = hosts
        # {"en":"SecretName is the name of the secret used to terminate TLS traffic on port 443", "zh_CN":"tls秘钥名称"}
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['hosts'] = self.hosts
        if self.secret_name is not None:
            result['secretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        if m.get('secretName') is not None:
            self.secret_name = m.get('secretName')
        return self


class CreateIngressHTTPIngressPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        path_type: str = None,
        backend: CreateIngressIngressBackend = None,
    ):
        # {"en":"Path is matched against the path of an incoming request", "zh_CN":"请求路径"}
        self.path = path
        # {"en":"PathType determines the interpretation of the Path matching,PathType can be one of the following values: Exact,Prefix,ImplementationSpecific", "zh_CN":"路径匹配类型: Exact,Prefix,ImplementationSpecific"}
        self.path_type = path_type
        # {"en":"Backend defines the referenced service endpoint to which the traffic will be forwarded to", "zh_CN":"指定后端服务"}
        self.backend = backend

    def validate(self):
        if self.backend:
            self.backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.path_type is not None:
            result['pathType'] = self.path_type
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        if m.get('backend') is not None:
            temp_model = CreateIngressIngressBackend()
            self.backend = temp_model.from_map(m['backend'])
        return self


class CreateIngressHTTPIngressRuleValue(TeaModel):
    def __init__(
        self,
        paths: List[CreateIngressHTTPIngressPath] = None,
    ):
        # {"en":"A collection of paths that map requests to backends", "zh_CN":"请求路径匹配规则"}
        self.paths = paths

    def validate(self):
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paths is not None:
            result['paths'] = []
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paths') is not None:
            self.paths = []
            for k in m.get('paths'):
                temp_model = CreateIngressHTTPIngressPath()
                self.paths.append(temp_model.from_map(k))
        return self


class CreateIngressIngressRule(TeaModel):
    def __init__(
        self,
        host: str = None,
        http: CreateIngressHTTPIngressRuleValue = None,
    ):
        # {"en":"Host is the fully qualified domain name of a network host", "zh_CN":"域名"}
        self.host = host
        self.http = http

    def validate(self):
        if self.http:
            self.http.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.http is not None:
            result['http'] = self.http.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('http') is not None:
            temp_model = CreateIngressHTTPIngressRuleValue()
            self.http = temp_model.from_map(m['http'])
        return self


class CreateIngressIngressSpec(TeaModel):
    def __init__(
        self,
        ingress_class_name: str = None,
        default_backend: CreateIngressIngressBackend = None,
        tls: List[CreateIngressIngressTLS] = None,
        rules: List[CreateIngressIngressRule] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.ingress_class_name = ingress_class_name
        # {"en":"DefaultBackend is the backend that should handle requests that don't match any rule", "zh_CN":"默认后端,当请求不匹配任何规则时调用"}
        self.default_backend = default_backend
        self.tls = tls
        # {"en":"A list of host rules used to configure the CreateIngressIngress", "zh_CN":"路由规则列表"}
        self.rules = rules

    def validate(self):
        if self.default_backend:
            self.default_backend.validate()
        if self.tls:
            for k in self.tls:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_class_name is not None:
            result['ingressClassName'] = self.ingress_class_name
        if self.default_backend is not None:
            result['defaultBackend'] = self.default_backend.to_map()
        if self.tls is not None:
            result['tls'] = []
            for k in self.tls:
                result['tls'].append(k.to_map() if k else None)
        if self.rules is not None:
            result['rules'] = []
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressClassName') is not None:
            self.ingress_class_name = m.get('ingressClassName')
        if m.get('defaultBackend') is not None:
            temp_model = CreateIngressIngressBackend()
            self.default_backend = temp_model.from_map(m['defaultBackend'])
        if m.get('tls') is not None:
            self.tls = []
            for k in m.get('tls'):
                temp_model = CreateIngressIngressTLS()
                self.tls.append(temp_model.from_map(k))
        if m.get('rules') is not None:
            self.rules = []
            for k in m.get('rules'):
                temp_model = CreateIngressIngressRule()
                self.rules.append(temp_model.from_map(k))
        return self


class CreateIngressIngress(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateIngressObjectMeta = None,
        spec: CreateIngressIngressSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"ingress desired", "zh_CN":"路由期望属性"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateIngressObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateIngressIngressSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateIngressRequest(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[str] = None,
        ingress: CreateIngressIngress = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('ingress') is not None:
            temp_model = CreateIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        return self


class CreateIngressCustomIngress(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[str] = None,
        ingress: CreateIngressIngress = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('ingress') is not None:
            temp_model = CreateIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        return self


class CreateIngressResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateIngressCustomIngress = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress object", "zh_CN":"路由对象"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = CreateIngressCustomIngress()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateIngressPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressPortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"Port is the port number of the service port of which status is recorded here", "zh_CN":"服务端口"}
        self.port = port
        # {"en":"Protocol is the protocol of the service port of which status is recorded here,The supported values are: TCP, UDP, SCTP", "zh_CN":"服务支持类型: TCP,UDP,SCTP"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port", "zh_CN":"记录服务端口错误信息"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class CreateIngressLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        hostname: str = None,
        ports: List[CreateIngressPortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based", "zh_CN":"负载均衡服务ip"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based", "zh_CN":"负载均衡类型服务dns"}
        self.hostname = hostname
        # {"en":"Ports is a list of records of service ports", "zh_CN":"服务端口状态列表"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.ports, 'ports')
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = CreateIngressPortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class CreateIngressLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[CreateIngressLoadBalancerIngress] = None,
    ):
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = CreateIngressLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class CreateIngressIngressStatus(TeaModel):
    def __init__(
        self,
        load_balancer: CreateIngressLoadBalancerStatus = None,
    ):
        # {"en":"LoadBalancer contains the current status of the load-balancer", "zh_CN":"包含当前负载均衡服务的状态"}
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = CreateIngressLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        return self






class UpdateIngressControllerIngressCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        replicate: int = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"replicates", "zh_CN":"副本数"}
        self.replicate = replicate

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.replicate, 'replicate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.replicate is not None:
            result['replicate'] = self.replicate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicate') is not None:
            self.replicate = m.get('replicate')
        return self


class UpdateIngressControllerRequest(TeaModel):
    def __init__(
        self,
        limit: Dict[str, str] = None,
        request: Dict[str, str] = None,
        clusters: List[UpdateIngressControllerIngressCluster] = None,
    ):
        # {"en":"resource limit", "zh_CN":"资源限制"}
        self.limit = limit
        # {"en":"resource request", "zh_CN":"所需资源"}
        self.request = request
        # {"en":"cluster and replicate", "zh_CN":"部署集群和副本数"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.request, 'request')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.request is not None:
            result['request'] = self.request
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = UpdateIngressControllerIngressCluster()
                self.clusters.append(temp_model.from_map(k))
        return self


class UpdateIngressControllerIngressController(TeaModel):
    def __init__(
        self,
        name: str = None,
        limit: Dict[str, str] = None,
        request: Dict[str, str] = None,
        clusters: List[UpdateIngressControllerIngressCluster] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name
        # {"en":"resource limit", "zh_CN":"资源限制"}
        self.limit = limit
        # {"en":"resource request", "zh_CN":"所需资源"}
        self.request = request
        # {"en":"cluster and replicate", "zh_CN":"部署集群和副本数"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.request, 'request')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.request is not None:
            result['request'] = self.request
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = UpdateIngressControllerIngressCluster()
                self.clusters.append(temp_model.from_map(k))
        return self


class UpdateIngressControllerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateIngressControllerIngressController = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress controller", "zh_CN":"路由控制器"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = UpdateIngressControllerIngressController()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateIngressControllerPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateIngressControllerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateIngressControllerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateIngressControllerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetServiceOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class GetServiceFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetServiceManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetServiceFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetServiceManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetServiceFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetServiceFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetServiceFieldsV1 holds the first JSON version format as described in the 'GetServiceFieldsV1' type", "zh_CN":"GetServiceFieldsV1 包含类型 “GetServiceFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = GetServiceFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetServiceObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[GetServiceOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetServiceManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 GetServiceService 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = GetServiceOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetServiceManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetServiceServicePort(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        app_protocol: str = None,
        port: int = None,
        target_port: int = None,
        node_port: int = None,
    ):
        # {"en":"The name of this port within the service. This must be a DNS_LABEL. All ports within a GetServiceServiceSpec must have unique names. When considering the endpoints for a GetServiceService, this must match the 'name' field in the EndpointPort. Optional if only one GetServiceServicePort is defined on this service", "zh_CN":"GetServiceService 中此端口的名称。这必须是 DNS_LABEL。 GetServiceServiceSpec 中的所有端口的名称都必须唯一。 在考虑 GetServiceService 的端点时，这一字段值必须与 EndpointPort 中的 name 字段相同。 如果此服务上仅定义一个 GetServiceServicePort，则为此字段为可选"}
        self.name = name
        # {"en":"The IP protocol for this port. Supports TCP, UDP, and SCTP. Default is TCP", "zh_CN":"此端口的 IP 协议。支持 “TCP”、“UDP” 和 “SCTP”。默认为 TCP"}
        self.protocol = protocol
        # {"en":"The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol", "zh_CN":"此端口的应用协议，遵循标准的 Kubernetes 标签语法，无前缀名称按照 IANA 标准服务名称 （参见 RFC-6335 和 https://www.iana.org/assignments/service-names）。 非标准协议应该使用前缀名称，如 mycompany.com/my-custom-protocol"}
        self.app_protocol = app_protocol
        # {"en":"The port that will be exposed by this service", "zh_CN":"GetServiceService 将公开的端口"}
        self.port = port
        # {"en":"Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field", "zh_CN":"在 GetServiceService 所针对的 Pod 上要访问的端口号或名称。 编号必须在 1 到 65535 的范围内。名称必须是 IANA_SVC_NAME。 如果此值是一个字符串，将在目标 Pod 的容器端口中作为命名端口进行查找。 如果未指定字段，则使用 “port” 字段的值（直接映射）。 对于 clusterIP 为 None 的服务，此字段将被忽略， 应忽略不设或设置为 “port” 字段的取值"}
        self.target_port = target_port
        # {"en":"The port on each node on which this service is exposed when type is NodePort or LoadBalancer. Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail. If not specified, a port will be allocated if this GetServiceService requires one. If this field is specified when creating a GetServiceService which does not need it, creation will fail. This field will be wiped when updating a GetServiceService to no longer need it (e.g. changing type from NodePort to ClusterIP).", "zh_CN":"当类型为 NodePort 或 LoadBalancer 时，GetServiceService 公开在节点上的端口， 通常由系统分配。如果指定了一个在范围内且未使用的值，则将使用该值，否则操作将失败。 如果在创建的 GetServiceService 需要该端口时未指定该字段，则会分配端口。 如果在创建不需要该端口的 Service时指定了该字段，则会创建失败。 当更新 GetServiceService 时，如果不再需要此字段（例如，将类型从 NodePort 更改为 ClusterIP），这个字段将被擦除"}
        self.node_port = node_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.app_protocol is not None:
            result['appProtocol'] = self.app_protocol
        if self.port is not None:
            result['port'] = self.port
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        if self.node_port is not None:
            result['nodePort'] = self.node_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('appProtocol') is not None:
            self.app_protocol = m.get('appProtocol')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        if m.get('nodePort') is not None:
            self.node_port = m.get('nodePort')
        return self


class GetServiceClientIPConfig(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
    ):
        # {"en":"timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3 hours).", "zh_CN":"timeoutSeconds 指定 ClientIP 类型会话的维系时间秒数。 如果 ServiceAffinity == 'ClientIP'，则该值必须 >0 && <=86400（1 天）。默认值为 10800（3 小时）"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class GetServiceSessionAffinityConfig(TeaModel):
    def __init__(
        self,
        client_ip: GetServiceClientIPConfig = None,
    ):
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"clientIP 包含基于客户端 IP 的会话亲和性的配置"}
        self.client_ip = client_ip

    def validate(self):
        if self.client_ip:
            self.client_ip.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIP') is not None:
            temp_model = GetServiceClientIPConfig()
            self.client_ip = temp_model.from_map(m['clientIP'])
        return self


class GetServiceServiceSpec(TeaModel):
    def __init__(
        self,
        ports: List[GetServiceServicePort] = None,
        selector: Dict[str, str] = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        type: str = None,
        external_ips: List[str] = None,
        session_affinity: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        publish_not_ready_addresses: bool = None,
        session_affinity_config: GetServiceSessionAffinityConfig = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        allocate_load_balancer_node_ports: bool = None,
        load_balancer_class: str = None,
        internal_traffic_policy: str = None,
    ):
        # {"en":"The list of ports that are exposed by this service", "zh_CN":"此 GetServiceService 公开的端口列表"}
        self.ports = ports
        # {"en":"Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName", "zh_CN":"将 GetServiceService 流量路由到具有与此 selector 匹配的标签键值对的 Pod。 如果为空或不存在，则假定该服务有一个外部进程管理其端点，Kubernetes 不会修改该端点。 仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型。如果类型为 ExternalName，则忽略"}
        self.selector = selector
        # {"en":"clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a GetServiceService of type ExternalName, creation will fail. This field will be wiped when updating a GetServiceService to type ExternalName", "zh_CN":"clusterIP 是服务的 IP 地址，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给服务，否则创建服务将失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIP 为空）或 type 已经是 ExternalName 时，可以更改 clusterIP（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIP 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 仅适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 GetServiceService 时指定了 clusterIP，则创建将失败。 更新 GetServiceService type 为 ExternalName 时，clusterIP 会被移除"}
        self.cluster_ip = cluster_ip
        # {"en":"ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a GetServiceService of type ExternalName, creation will fail. This field will be wiped when updating a GetServiceService to type ExternalName. If this field is not specified, it will be initialized from the clusterIP field. If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"clusterIPs 是分配给该 GetServiceService 的 IP 地址列表，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给 GetServiceService；否则创建 GetServiceService 失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIPs 为空）或 type 已经是 ExternalName 时，可以更改 clusterIPs（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIPs 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 GetServiceService 时指定了 clusterIPs，则会创建失败。 更新 GetServiceService type 为 ExternalName 时，该字段将被移除。如果未指定此字段，则将从 clusterIP 字段初始化。 如果指定 clusterIPs，客户端必须确保 clusterIPs[0] 和 clusterIP 一致。clusterIPs 最多可包含两个条目（双栈系列，按任意顺序）。 这些 IP 必须与 ipFamilies 的值相对应。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 管理"}
        self.cluster_ips = cluster_ips
        # {"en":"type determines how the GetServiceService is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName. Several other fields do not apply to ExternalName services", "zh_CN":"type 确定 GetServiceService 的公开方式。默认为 ClusterIP。 有效选项为 ExternalName、ClusterIP、NodePort 和 LoadBalancer。 “ClusterIP” 为端点分配一个集群内部 IP 地址用于负载均衡。 Endpoints 由 selector 确定，如果未设置 selector，则需要通过手动构造 Endpoints 或 EndpointSlice 的对象来确定。 如果 clusterIP 为 “None”，则不分配虚拟 IP，并且 Endpoints 作为一组端点而不是虚拟 IP 发布。 “NodePort” 建立在 ClusterIP 之上，并在每个节点上分配一个端口，该端口路由到与 clusterIP 相同的 Endpoints。 “LoadBalancer” 基于 NodePort 构建并创建一个外部负载均衡器（如果当前云支持），该负载均衡器路由到与 clusterIP 相同的 Endpoints。 “externalName” 将此 GetServiceService 别名为指定的 externalName。其他几个字段不适用于 ExternalName GetServiceService"}
        self.type = type
        # {"en":"externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system", "zh_CN":"externalIPs 是一个 IP 列表，集群中的节点会为此 GetServiceService 接收针对这些 IP 地址的流量。 这些 IP 不被 Kubernetes 管理。用户需要确保流量可以到达具有此 IP 的节点。 一个常见的例子是不属于 Kubernetes 系统的外部负载均衡器"}
        self.external_ips = external_ips
        # {"en":"Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None", "zh_CN":"支持 “ClientIP” 和 “None”。用于维护会话亲和性。 启用基于客户端 IP 的会话亲和性。必须是 ClientIP 或 None。默认为 None"}
        self.session_affinity = session_affinity
        # {"en":"Only applies to GetServiceService Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations, and it cannot support dual-stack. As of Kubernetes v1.24, users are encouraged to use implementation-specific annotations when available. This field may be removed in a future API version", "zh_CN":"仅适用于服务类型: LoadBalancer。此功能取决于底层云提供商是否支持负载均衡器。 如果云提供商不支持该功能，该字段将被忽略。 已弃用: 该字段信息不足，且其含义因实现而异，而且不支持双栈。 从 Kubernetes v1.24 开始，鼓励用户在可用时使用特定于实现的注释。在未来的 API 版本中可能会删除此字段"}
        self.load_balancer_ip = load_balancer_ip
        # {"en":"If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature", "zh_CN":"如果设置了此字段并且被平台支持，将限制通过云厂商的负载均衡器的流量到指定的客户端 IP。 如果云提供商不支持该功能，该字段将被忽略"}
        self.load_balancer_source_ranges = load_balancer_source_ranges
        # {"en":"externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved. Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires type to be 'ExternalName'", "zh_CN":"externalName 是发现机制将返回的外部引用，作为此服务的别名（例如 DNS CNAME 记录）。 不涉及代理。必须是小写的 RFC-1123 主机名 (https://tools.ietf.org/html/rfc1123)， 并且要求 type 为 “ExternalName”"}
        self.external_name = external_name
        # {"en":"externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the GetServiceService's 'externally-facing' addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node", "zh_CN":"externalTrafficPolicy 描述了节点如何分发它们在 GetServiceService 的“外部访问”地址 （NodePort、ExternalIP 和 LoadBalancer IP）接收到的服务流量。 如果设置为 “Local”，代理将以一种假设外部负载均衡器将负责在节点之间服务流量负载均衡， 因此每个节点将仅向服务的节点本地端点传递流量，而不会伪装客户端源 IP。 （将丢弃错误发送到没有端点的节点的流量。） “Cluster” 默认值使用负载均衡路由到所有端点的策略（可能会根据拓扑和其他特性进行修改）。 请注意，从集群内部发送到 External IP 或 LoadBalancer IP 的流量始终具有 “Cluster” 语义， 但是从集群内部发送到 NodePort 的客户端需要在选择节点时考虑流量路由策略"}
        self.external_traffic_policy = external_traffic_policy
        # {"en":"healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used. If not specified, a value will be automatically allocated. External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not. If this field is specified when creating a GetServiceService which does not need it, creation will fail. This field will be wiped when updating a GetServiceService to no longer need it (e.g. changing type). This field cannot be updated once set", "zh_CN":"healthCheckNodePort 指定 GetServiceService 的健康检查节点端口。 仅适用于 type 为 LoadBalancer 且 externalTrafficPolicy 设置为 Local 的情况。 如果为此字段设定了一个值，该值在合法范围内且没有被使用，则使用所指定的值。 如果未设置此字段，则自动分配字段值。外部系统（例如负载平衡器）可以使用此端口来确定给定节点是否拥有此服务的端点。 在创建不需要 healthCheckNodePort 的 GetServiceService 时指定了此字段，则 GetServiceService 创建会失败。 要移除 healthCheckNodePort，需要更改 GetServiceService 的 type。 该字段一旦设置就无法更改"}
        self.health_check_node_port = health_check_node_port
        # {"en":"publishNotReadyAddresses indicates that any agent which deals with endpoints for this GetServiceService should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless GetServiceService to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered 'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior", "zh_CN":"publishNotReadyAddresses 表示任何处理此 GetServiceService 端点的代理都应忽略任何准备就绪/未准备就绪的指示。 设置此字段的主要场景是为 StatefulSet 的服务提供支持，使之能够为其 Pod 传播 SRV DNS 记录，以实现对等发现。 为 GetServiceService 生成 Endpoints 和 EndpointSlice 资源的 Kubernetes 控制器对字段的解读是， 即使 Pod 本身还没有准备好，所有端点都可被视为 “已就绪”。 对于代理而言，如果仅使用 Kubernetes 通过 Endpoints 或 EndpointSlice 资源所生成的端点， 则可以安全地假设这种行为"}
        self.publish_not_ready_addresses = publish_not_ready_addresses
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"sessionAffinityConfig 包含会话亲和性的配置"}
        self.session_affinity_config = session_affinity_config
        # {"en":"IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the GetServiceService. Valid values are 'IPv4' and 'IPv6'. This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to 'headless' services. This field will be wiped when updating a GetServiceService to type ExternalName.This field may hold a maximum of two entries (dual-stack families, in either order). These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"iPFamilies 是分配给此服务的 IP 协议（例如 IPv4、IPv6）的列表。 该字段通常根据集群配置和 ipFamilyPolicy 字段自动设置。 如果手动指定该字段，且请求的协议在集群中可用，且 ipFamilyPolicy 允许，则使用；否则服务创建将失败。 该字段修改是有条件的：它允许添加或删除辅助 IP 协议，但不允许更改服务的主要 IP 协议。 有效值为 “IPv4” 和 “IPv6”。 该字段仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型的服务，并且确实可用于“无头”服务。 更新服务设置类型为 ExternalName 时，该字段将被擦除。该字段最多可以包含两个条目（双栈系列，按任意顺序）。 如果指定，这些协议栈必须对应于 clusterIPs 字段的值。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 字段管理"}
        self.ip_families = ip_families
        # {"en":"IPFamilyPolicy represents the dual-stack-ness requested or required by this GetServiceService. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName", "zh_CN":"iPFamilyPolicy 表示此服务请求或要求的双栈特性。 如果没有提供值，则此字段将被设置为 SingleStack。 服务可以是 “SingleStack”（单个 IP 协议）、 “PreferDualStack”（双栈配置集群上的两个 IP 协议或单栈集群上的单个 IP 协议） 或 “RequireDualStack”（双栈上的两个 IP 协议配置的集群，否则失败）。 ipFamilies 和 clusterIPs 字段取决于此字段的值。 更新服务设置类型为 ExternalName 时，此字段将被擦除"}
        self.ip_family_policy = ip_family_policy
        # {"en":"allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer. Default is 'true'. It may be set to 'false' if the cluster load-balancer does not rely on NodePorts. If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type", "zh_CN":"allocateLoadBalancerNodePorts 定义了是否会自动为 LoadBalancer 类型的 GetServiceService 分配 NodePort。默认为 true。 如果集群负载均衡器不依赖 NodePort，则可以设置此字段为 false。 如果调用者（通过指定一个值）请求特定的 NodePort，则无论此字段如何，都会接受这些请求。 该字段只能设置在 type 为 LoadBalancer 的 GetServiceService 上，如果 type 更改为任何其他类型，该字段将被移除"}
        self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        # {"en":"loadBalancerClass is the class of the load balancer implementation this GetServiceService belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved for end-users. This field can only be set when the GetServiceService type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a GetServiceService to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type", "zh_CN":"loadBalancerClass 是此 GetServiceService 所属的负载均衡器实现的类。 如果设置了此字段，则字段值必须是标签风格的标识符，带有可选前缀，例如 ”internal-vip” 或 “example.com/internal-vip”。 无前缀名称是为最终用户保留的。该字段只能在 GetServiceService 类型为 “LoadBalancer” 时设置。 如果未设置此字段，则使用默认负载均衡器实现。默认负载均衡器现在通常通过云提供商集成完成，但应适用于任何默认实现。 如果设置了此字段，则假定负载均衡器实现正在监测具有对应负载均衡器类的 GetServiceService。 任何默认负载均衡器实现（例如云提供商）都应忽略设置此字段的 GetServiceService。 只有在创建或更新的 GetServiceService 的 type 为 “LoadBalancer” 时，才可设置此字段。 一经设定，不可更改。当 GetServiceService 的 type 更新为 “LoadBalancer” 之外的其他类型时，此字段将被移除"}
        self.load_balancer_class = load_balancer_class
        # {"en":"InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features)", "zh_CN":"InternalTrafficPolicy 描述节点如何分发它们在 ClusterIP 上接收到的服务流量。 如果设置为 “Local”，代理将假定 Pod 只想与在同一节点上的服务端点通信，如果没有本地端点，它将丢弃流量。 “Cluster” 默认将流量路由到所有端点（可能会根据拓扑和其他特性进行修改）"}
        self.internal_traffic_policy = internal_traffic_policy

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.session_affinity_config:
            self.session_affinity_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['selector'] = self.selector
        if self.cluster_ip is not None:
            result['clusterIP'] = self.cluster_ip
        if self.cluster_ips is not None:
            result['clusterIPs'] = self.cluster_ips
        if self.type is not None:
            result['type'] = self.type
        if self.external_ips is not None:
            result['externalIPs'] = self.external_ips
        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity
        if self.load_balancer_ip is not None:
            result['loadBalancerIP'] = self.load_balancer_ip
        if self.load_balancer_source_ranges is not None:
            result['loadBalancerSourceRanges'] = self.load_balancer_source_ranges
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.external_traffic_policy is not None:
            result['externalTrafficPolicy'] = self.external_traffic_policy
        if self.health_check_node_port is not None:
            result['healthCheckNodePort'] = self.health_check_node_port
        if self.publish_not_ready_addresses is not None:
            result['publishNotReadyAddresses'] = self.publish_not_ready_addresses
        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config.to_map()
        if self.ip_families is not None:
            result['ipFamilies'] = self.ip_families
        if self.ip_family_policy is not None:
            result['ipFamilyPolicy'] = self.ip_family_policy
        if self.allocate_load_balancer_node_ports is not None:
            result['allocateLoadBalancerNodePorts'] = self.allocate_load_balancer_node_ports
        if self.load_balancer_class is not None:
            result['loadBalancerClass'] = self.load_balancer_class
        if self.internal_traffic_policy is not None:
            result['internalTrafficPolicy'] = self.internal_traffic_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = GetServiceServicePort()
                self.ports.append(temp_model.from_map(k))
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('clusterIP') is not None:
            self.cluster_ip = m.get('clusterIP')
        if m.get('clusterIPs') is not None:
            self.cluster_ips = m.get('clusterIPs')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('externalIPs') is not None:
            self.external_ips = m.get('externalIPs')
        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')
        if m.get('loadBalancerIP') is not None:
            self.load_balancer_ip = m.get('loadBalancerIP')
        if m.get('loadBalancerSourceRanges') is not None:
            self.load_balancer_source_ranges = m.get('loadBalancerSourceRanges')
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('externalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('externalTrafficPolicy')
        if m.get('healthCheckNodePort') is not None:
            self.health_check_node_port = m.get('healthCheckNodePort')
        if m.get('publishNotReadyAddresses') is not None:
            self.publish_not_ready_addresses = m.get('publishNotReadyAddresses')
        if m.get('sessionAffinityConfig') is not None:
            temp_model = GetServiceSessionAffinityConfig()
            self.session_affinity_config = temp_model.from_map(m['sessionAffinityConfig'])
        if m.get('ipFamilies') is not None:
            self.ip_families = m.get('ipFamilies')
        if m.get('ipFamilyPolicy') is not None:
            self.ip_family_policy = m.get('ipFamilyPolicy')
        if m.get('allocateLoadBalancerNodePorts') is not None:
            self.allocate_load_balancer_node_ports = m.get('allocateLoadBalancerNodePorts')
        if m.get('loadBalancerClass') is not None:
            self.load_balancer_class = m.get('loadBalancerClass')
        if m.get('internalTrafficPolicy') is not None:
            self.internal_traffic_policy = m.get('internalTrafficPolicy')
        return self


class GetServicePortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"the port number of the service port of which status is recorded here", "zh_CN":"port 是所记录的服务端口状态的端口号"}
        self.port = port
        # {"en":"the protocol of the service port of which status is recorded here The supported values are: 'TCP', 'UDP', 'SCTP'", "zh_CN":"protocol 是所记录的服务端口状态的协议。支持的值为：“TCP”、”UDP”、“SCTP”"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use CamelCase names - cloud provider specific error values must have names that comply with the format foo.example.com/CamelCase", "zh_CN":"error 是记录 GetServiceService 端口的问题。 错误的格式应符合以下规则:内置错误原因应在此文件中指定，应使用 CamelCase 名称。云提供商特定错误原因的名称必须符合格式 foo.example.com/CamelCase"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class GetServiceLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        host_name: str = None,
        ports: List[GetServicePortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)", "zh_CN":"ip 是为基于 IP 的负载均衡器 Ingress 点（通常是 GCE 或 OpenStack 负载均衡器）设置的"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)", "zh_CN":"hostname 是为基于 DNS 的负载均衡器 Ingress 点（通常是 AWS 负载均衡器）设置的"}
        self.host_name = host_name
        # {"en":"Ports is a list of records of service ports If used, every port defined in the service should have an entry in it", "zh_CN":"ports 是 GetServiceService 的端口列表。如果设置了此字段，GetServiceService 中定义的每个端口都应该在此列表中"}
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = GetServicePortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class GetServiceLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[GetServiceLoadBalancerIngress] = None,
    ):
        # {"en":"Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points", "zh_CN":"ingress 是一个包含负载均衡器 Ingress 点的列表。GetServiceService 的流量需要被发送到这些 Ingress 点"}
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = GetServiceLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class GetServiceMetaV1Condition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        observed_generation: int = None,
        last_transition_time: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type of condition in CamelCase or in foo.example.com/CamelCase", "zh_CN":"CamelCase 或 foo.example.com/CamelCase 中的条件类型"}
        self.type = type
        # {"en":"status of the condition, one of True, False, Unknown", "zh_CN":"condition 的状态，True、False、Unknown 之一"}
        self.status = status
        # {"en":"observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance", "zh_CN":"表示设置 condition 基于的 .metadata.generation 的过期次数。 例如，如果 .metadata.generation 当前为 12，但 .status.conditions[x].observedGeneration 为 9， 则 condition 相对于实例的当前状态已过期"}
        self.observed_generation = observed_generation
        # {"en":"lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable", "zh_CN":"状况最近一次状态转化的时间。 变化应该发生在下层状况发生变化的时候。如果不知道下层状况发生变化的时间， 那么使用 API 字段更改的时间是可以接受的"}
        self.last_transition_time = last_transition_time
        # {"en":"reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty", "zh_CN":"reason 包含一个程序标识符，指示 condition 最后一次转换的原因。 特定条件类型的生产者可以定义该字段的预期值和含义，以及这些值是否被视为有保证的 API。 该值应该是 CamelCase 字符串且不能为空"}
        self.reason = reason
        # {"en":"message is a human readable message indicating details about the transition. This may be an empty string", "zh_CN":"message 是人类可读的消息，有关转换的详细信息，可以是空字符串"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetServiceServiceStatus(TeaModel):
    def __init__(
        self,
        load_balancer: GetServiceLoadBalancerStatus = None,
        conditions: List[GetServiceMetaV1Condition] = None,
    ):
        # {"en":"Current service state", "zh_CN":"loadBalancer 包含负载均衡器的当前状态（如果存在）"}
        self.load_balancer = load_balancer
        # {"en":"LoadBalancer contains the current status of the load-balancer, if one is present", "zh_CN":"服务的当前状态"}
        self.conditions = conditions

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = GetServiceLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = GetServiceMetaV1Condition()
                self.conditions.append(temp_model.from_map(k))
        return self


class GetServiceService(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetServiceObjectMeta = None,
        spec: GetServiceServiceSpec = None,
        status: GetServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 GetServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 GetServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = GetServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetServiceService = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"service", "zh_CN":"service"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetServiceService()
            self.data = temp_model.from_map(m['data'])
        return self


class GetServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"service name", "zh_CN":"service 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutPatchServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchServiceOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class PutPatchServiceFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchServiceManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutPatchServiceFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutPatchServiceManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutPatchServiceFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutPatchServiceFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutPatchServiceFieldsV1 holds the first JSON version format as described in the 'PutPatchServiceFieldsV1' type", "zh_CN":"PutPatchServiceFieldsV1 包含类型 “PutPatchServiceFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = PutPatchServiceFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutPatchServiceObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[PutPatchServiceOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutPatchServiceManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 PutPatchServiceService 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = PutPatchServiceOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutPatchServiceManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutPatchServiceServicePort(TeaModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
        app_protocol: str = None,
        port: int = None,
        target_port: int = None,
        node_port: int = None,
    ):
        # {"en":"The name of this port within the service. This must be a DNS_LABEL. All ports within a PutPatchServiceServiceSpec must have unique names. When considering the endpoints for a PutPatchServiceService, this must match the 'name' field in the EndpointPort. Optional if only one PutPatchServiceServicePort is defined on this service", "zh_CN":"PutPatchServiceService 中此端口的名称。这必须是 DNS_LABEL。 PutPatchServiceServiceSpec 中的所有端口的名称都必须唯一。 在考虑 PutPatchServiceService 的端点时，这一字段值必须与 EndpointPort 中的 name 字段相同。 如果此服务上仅定义一个 PutPatchServiceServicePort，则为此字段为可选"}
        self.name = name
        # {"en":"The IP protocol for this port. Supports TCP, UDP, and SCTP. Default is TCP", "zh_CN":"此端口的 IP 协议。支持 “TCP”、“UDP” 和 “SCTP”。默认为 TCP"}
        self.protocol = protocol
        # {"en":"The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol", "zh_CN":"此端口的应用协议，遵循标准的 Kubernetes 标签语法，无前缀名称按照 IANA 标准服务名称 （参见 RFC-6335 和 https://www.iana.org/assignments/service-names）。 非标准协议应该使用前缀名称，如 mycompany.com/my-custom-protocol"}
        self.app_protocol = app_protocol
        # {"en":"The port that will be exposed by this service", "zh_CN":"PutPatchServiceService 将公开的端口"}
        self.port = port
        # {"en":"Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field", "zh_CN":"在 PutPatchServiceService 所针对的 Pod 上要访问的端口号或名称。 编号必须在 1 到 65535 的范围内。名称必须是 IANA_SVC_NAME。 如果此值是一个字符串，将在目标 Pod 的容器端口中作为命名端口进行查找。 如果未指定字段，则使用 “port” 字段的值（直接映射）。 对于 clusterIP 为 None 的服务，此字段将被忽略， 应忽略不设或设置为 “port” 字段的取值"}
        self.target_port = target_port
        # {"en":"The port on each node on which this service is exposed when type is NodePort or LoadBalancer. Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail. If not specified, a port will be allocated if this PutPatchServiceService requires one. If this field is specified when creating a PutPatchServiceService which does not need it, creation will fail. This field will be wiped when updating a PutPatchServiceService to no longer need it (e.g. changing type from NodePort to ClusterIP).", "zh_CN":"当类型为 NodePort 或 LoadBalancer 时，PutPatchServiceService 公开在节点上的端口， 通常由系统分配。如果指定了一个在范围内且未使用的值，则将使用该值，否则操作将失败。 如果在创建的 PutPatchServiceService 需要该端口时未指定该字段，则会分配端口。 如果在创建不需要该端口的 Service时指定了该字段，则会创建失败。 当更新 PutPatchServiceService 时，如果不再需要此字段（例如，将类型从 NodePort 更改为 ClusterIP），这个字段将被擦除"}
        self.node_port = node_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.app_protocol is not None:
            result['appProtocol'] = self.app_protocol
        if self.port is not None:
            result['port'] = self.port
        if self.target_port is not None:
            result['targetPort'] = self.target_port
        if self.node_port is not None:
            result['nodePort'] = self.node_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('appProtocol') is not None:
            self.app_protocol = m.get('appProtocol')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('targetPort') is not None:
            self.target_port = m.get('targetPort')
        if m.get('nodePort') is not None:
            self.node_port = m.get('nodePort')
        return self


class PutPatchServiceClientIPConfig(TeaModel):
    def __init__(
        self,
        timeout_seconds: int = None,
    ):
        # {"en":"timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3 hours).", "zh_CN":"timeoutSeconds 指定 ClientIP 类型会话的维系时间秒数。 如果 ServiceAffinity == 'ClientIP'，则该值必须 >0 && <=86400（1 天）。默认值为 10800（3 小时）"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class PutPatchServiceSessionAffinityConfig(TeaModel):
    def __init__(
        self,
        client_ip: PutPatchServiceClientIPConfig = None,
    ):
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"clientIP 包含基于客户端 IP 的会话亲和性的配置"}
        self.client_ip = client_ip

    def validate(self):
        if self.client_ip:
            self.client_ip.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIP') is not None:
            temp_model = PutPatchServiceClientIPConfig()
            self.client_ip = temp_model.from_map(m['clientIP'])
        return self


class PutPatchServiceServiceSpec(TeaModel):
    def __init__(
        self,
        ports: List[PutPatchServiceServicePort] = None,
        selector: Dict[str, str] = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        type: str = None,
        external_ips: List[str] = None,
        session_affinity: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        publish_not_ready_addresses: bool = None,
        session_affinity_config: PutPatchServiceSessionAffinityConfig = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        allocate_load_balancer_node_ports: bool = None,
        load_balancer_class: str = None,
        internal_traffic_policy: str = None,
    ):
        # {"en":"The list of ports that are exposed by this service", "zh_CN":"此 PutPatchServiceService 公开的端口列表"}
        self.ports = ports
        # {"en":"Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName", "zh_CN":"将 PutPatchServiceService 流量路由到具有与此 selector 匹配的标签键值对的 Pod。 如果为空或不存在，则假定该服务有一个外部进程管理其端点，Kubernetes 不会修改该端点。 仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型。如果类型为 ExternalName，则忽略"}
        self.selector = selector
        # {"en":"clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a PutPatchServiceService of type ExternalName, creation will fail. This field will be wiped when updating a PutPatchServiceService to type ExternalName", "zh_CN":"clusterIP 是服务的 IP 地址，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给服务，否则创建服务将失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIP 为空）或 type 已经是 ExternalName 时，可以更改 clusterIP（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIP 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 仅适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 PutPatchServiceService 时指定了 clusterIP，则创建将失败。 更新 PutPatchServiceService type 为 ExternalName 时，clusterIP 会被移除"}
        self.cluster_ip = cluster_ip
        # {"en":"ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above). Valid values are 'None', empty string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a PutPatchServiceService of type ExternalName, creation will fail. This field will be wiped when updating a PutPatchServiceService to type ExternalName. If this field is not specified, it will be initialized from the clusterIP field. If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"clusterIPs 是分配给该 PutPatchServiceService 的 IP 地址列表，通常是随机分配的。 如果地址是手动指定的，在范围内（根据系统配置），且没有被使用，它将被分配给 PutPatchServiceService；否则创建 PutPatchServiceService 失败。 clusterIP 一般不会被更改，除非 type 被更改为 ExternalName （ExternalName 需要 clusterIPs 为空）或 type 已经是 ExternalName 时，可以更改 clusterIPs（在这种情况下，可以选择指定此字段）。 可选值 “None”、空字符串 (“”) 或有效的 IP 地址。 clusterIPs 为 “None” 时会生成“无头服务”（无虚拟 IP），这在首选直接 Endpoint 连接且不需要代理时很有用。 适用于 ClusterIP、NodePort、和 LoadBalancer 类型的服务。 如果在创建 ExternalName 类型的 PutPatchServiceService 时指定了 clusterIPs，则会创建失败。 更新 PutPatchServiceService type 为 ExternalName 时，该字段将被移除。如果未指定此字段，则将从 clusterIP 字段初始化。 如果指定 clusterIPs，客户端必须确保 clusterIPs[0] 和 clusterIP 一致。clusterIPs 最多可包含两个条目（双栈系列，按任意顺序）。 这些 IP 必须与 ipFamilies 的值相对应。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 管理"}
        self.cluster_ips = cluster_ips
        # {"en":"type determines how the PutPatchServiceService is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName. Several other fields do not apply to ExternalName services", "zh_CN":"type 确定 PutPatchServiceService 的公开方式。默认为 ClusterIP。 有效选项为 ExternalName、ClusterIP、NodePort 和 LoadBalancer。 “ClusterIP” 为端点分配一个集群内部 IP 地址用于负载均衡。 Endpoints 由 selector 确定，如果未设置 selector，则需要通过手动构造 Endpoints 或 EndpointSlice 的对象来确定。 如果 clusterIP 为 “None”，则不分配虚拟 IP，并且 Endpoints 作为一组端点而不是虚拟 IP 发布。 “NodePort” 建立在 ClusterIP 之上，并在每个节点上分配一个端口，该端口路由到与 clusterIP 相同的 Endpoints。 “LoadBalancer” 基于 NodePort 构建并创建一个外部负载均衡器（如果当前云支持），该负载均衡器路由到与 clusterIP 相同的 Endpoints。 “externalName” 将此 PutPatchServiceService 别名为指定的 externalName。其他几个字段不适用于 ExternalName PutPatchServiceService"}
        self.type = type
        # {"en":"externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service. These IPs are not managed by Kubernetes. The user is responsible for ensuring that traffic arrives at a node with this IP. A common example is external load-balancers that are not part of the Kubernetes system", "zh_CN":"externalIPs 是一个 IP 列表，集群中的节点会为此 PutPatchServiceService 接收针对这些 IP 地址的流量。 这些 IP 不被 Kubernetes 管理。用户需要确保流量可以到达具有此 IP 的节点。 一个常见的例子是不属于 Kubernetes 系统的外部负载均衡器"}
        self.external_ips = external_ips
        # {"en":"Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None", "zh_CN":"支持 “ClientIP” 和 “None”。用于维护会话亲和性。 启用基于客户端 IP 的会话亲和性。必须是 ClientIP 或 None。默认为 None"}
        self.session_affinity = session_affinity
        # {"en":"Only applies to PutPatchServiceService Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations, and it cannot support dual-stack. As of Kubernetes v1.24, users are encouraged to use implementation-specific annotations when available. This field may be removed in a future API version", "zh_CN":"仅适用于服务类型: LoadBalancer。此功能取决于底层云提供商是否支持负载均衡器。 如果云提供商不支持该功能，该字段将被忽略。 已弃用: 该字段信息不足，且其含义因实现而异，而且不支持双栈。 从 Kubernetes v1.24 开始，鼓励用户在可用时使用特定于实现的注释。在未来的 API 版本中可能会删除此字段"}
        self.load_balancer_ip = load_balancer_ip
        # {"en":"If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature", "zh_CN":"如果设置了此字段并且被平台支持，将限制通过云厂商的负载均衡器的流量到指定的客户端 IP。 如果云提供商不支持该功能，该字段将被忽略"}
        self.load_balancer_source_ranges = load_balancer_source_ranges
        # {"en":"externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved. Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires type to be 'ExternalName'", "zh_CN":"externalName 是发现机制将返回的外部引用，作为此服务的别名（例如 DNS CNAME 记录）。 不涉及代理。必须是小写的 RFC-1123 主机名 (https://tools.ietf.org/html/rfc1123)， 并且要求 type 为 “ExternalName”"}
        self.external_name = external_name
        # {"en":"externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the PutPatchServiceService's 'externally-facing' addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node", "zh_CN":"externalTrafficPolicy 描述了节点如何分发它们在 PutPatchServiceService 的“外部访问”地址 （NodePort、ExternalIP 和 LoadBalancer IP）接收到的服务流量。 如果设置为 “Local”，代理将以一种假设外部负载均衡器将负责在节点之间服务流量负载均衡， 因此每个节点将仅向服务的节点本地端点传递流量，而不会伪装客户端源 IP。 （将丢弃错误发送到没有端点的节点的流量。） “Cluster” 默认值使用负载均衡路由到所有端点的策略（可能会根据拓扑和其他特性进行修改）。 请注意，从集群内部发送到 External IP 或 LoadBalancer IP 的流量始终具有 “Cluster” 语义， 但是从集群内部发送到 NodePort 的客户端需要在选择节点时考虑流量路由策略"}
        self.external_traffic_policy = external_traffic_policy
        # {"en":"healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used. If not specified, a value will be automatically allocated. External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not. If this field is specified when creating a PutPatchServiceService which does not need it, creation will fail. This field will be wiped when updating a PutPatchServiceService to no longer need it (e.g. changing type). This field cannot be updated once set", "zh_CN":"healthCheckNodePort 指定 PutPatchServiceService 的健康检查节点端口。 仅适用于 type 为 LoadBalancer 且 externalTrafficPolicy 设置为 Local 的情况。 如果为此字段设定了一个值，该值在合法范围内且没有被使用，则使用所指定的值。 如果未设置此字段，则自动分配字段值。外部系统（例如负载平衡器）可以使用此端口来确定给定节点是否拥有此服务的端点。 在创建不需要 healthCheckNodePort 的 PutPatchServiceService 时指定了此字段，则 PutPatchServiceService 创建会失败。 要移除 healthCheckNodePort，需要更改 PutPatchServiceService 的 type。 该字段一旦设置就无法更改"}
        self.health_check_node_port = health_check_node_port
        # {"en":"publishNotReadyAddresses indicates that any agent which deals with endpoints for this PutPatchServiceService should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless PutPatchServiceService to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered 'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior", "zh_CN":"publishNotReadyAddresses 表示任何处理此 PutPatchServiceService 端点的代理都应忽略任何准备就绪/未准备就绪的指示。 设置此字段的主要场景是为 StatefulSet 的服务提供支持，使之能够为其 Pod 传播 SRV DNS 记录，以实现对等发现。 为 PutPatchServiceService 生成 Endpoints 和 EndpointSlice 资源的 Kubernetes 控制器对字段的解读是， 即使 Pod 本身还没有准备好，所有端点都可被视为 “已就绪”。 对于代理而言，如果仅使用 Kubernetes 通过 Endpoints 或 EndpointSlice 资源所生成的端点， 则可以安全地假设这种行为"}
        self.publish_not_ready_addresses = publish_not_ready_addresses
        # {"en":"sessionAffinityConfig contains the configurations of session affinity", "zh_CN":"sessionAffinityConfig 包含会话亲和性的配置"}
        self.session_affinity_config = session_affinity_config
        # {"en":"IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the PutPatchServiceService. Valid values are 'IPv4' and 'IPv6'. This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to 'headless' services. This field will be wiped when updating a PutPatchServiceService to type ExternalName.This field may hold a maximum of two entries (dual-stack families, in either order). These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field", "zh_CN":"iPFamilies 是分配给此服务的 IP 协议（例如 IPv4、IPv6）的列表。 该字段通常根据集群配置和 ipFamilyPolicy 字段自动设置。 如果手动指定该字段，且请求的协议在集群中可用，且 ipFamilyPolicy 允许，则使用；否则服务创建将失败。 该字段修改是有条件的：它允许添加或删除辅助 IP 协议，但不允许更改服务的主要 IP 协议。 有效值为 “IPv4” 和 “IPv6”。 该字段仅适用于 ClusterIP、NodePort 和 LoadBalancer 类型的服务，并且确实可用于“无头”服务。 更新服务设置类型为 ExternalName 时，该字段将被擦除。该字段最多可以包含两个条目（双栈系列，按任意顺序）。 如果指定，这些协议栈必须对应于 clusterIPs 字段的值。 clusterIP 和 ipFamilies 都由 ipFamilyPolicy 字段管理"}
        self.ip_families = ip_families
        # {"en":"IPFamilyPolicy represents the dual-stack-ness requested or required by this PutPatchServiceService. If there is no value provided, then this field will be set to SingleStack. Services can be 'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName", "zh_CN":"iPFamilyPolicy 表示此服务请求或要求的双栈特性。 如果没有提供值，则此字段将被设置为 SingleStack。 服务可以是 “SingleStack”（单个 IP 协议）、 “PreferDualStack”（双栈配置集群上的两个 IP 协议或单栈集群上的单个 IP 协议） 或 “RequireDualStack”（双栈上的两个 IP 协议配置的集群，否则失败）。 ipFamilies 和 clusterIPs 字段取决于此字段的值。 更新服务设置类型为 ExternalName 时，此字段将被擦除"}
        self.ip_family_policy = ip_family_policy
        # {"en":"allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer. Default is 'true'. It may be set to 'false' if the cluster load-balancer does not rely on NodePorts. If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type", "zh_CN":"allocateLoadBalancerNodePorts 定义了是否会自动为 LoadBalancer 类型的 PutPatchServiceService 分配 NodePort。默认为 true。 如果集群负载均衡器不依赖 NodePort，则可以设置此字段为 false。 如果调用者（通过指定一个值）请求特定的 NodePort，则无论此字段如何，都会接受这些请求。 该字段只能设置在 type 为 LoadBalancer 的 PutPatchServiceService 上，如果 type 更改为任何其他类型，该字段将被移除"}
        self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        # {"en":"loadBalancerClass is the class of the load balancer implementation this PutPatchServiceService belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved for end-users. This field can only be set when the PutPatchServiceService type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a PutPatchServiceService to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type", "zh_CN":"loadBalancerClass 是此 PutPatchServiceService 所属的负载均衡器实现的类。 如果设置了此字段，则字段值必须是标签风格的标识符，带有可选前缀，例如 ”internal-vip” 或 “example.com/internal-vip”。 无前缀名称是为最终用户保留的。该字段只能在 PutPatchServiceService 类型为 “LoadBalancer” 时设置。 如果未设置此字段，则使用默认负载均衡器实现。默认负载均衡器现在通常通过云提供商集成完成，但应适用于任何默认实现。 如果设置了此字段，则假定负载均衡器实现正在监测具有对应负载均衡器类的 PutPatchServiceService。 任何默认负载均衡器实现（例如云提供商）都应忽略设置此字段的 PutPatchServiceService。 只有在创建或更新的 PutPatchServiceService 的 type 为 “LoadBalancer” 时，才可设置此字段。 一经设定，不可更改。当 PutPatchServiceService 的 type 更新为 “LoadBalancer” 之外的其他类型时，此字段将被移除"}
        self.load_balancer_class = load_balancer_class
        # {"en":"InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features)", "zh_CN":"InternalTrafficPolicy 描述节点如何分发它们在 ClusterIP 上接收到的服务流量。 如果设置为 “Local”，代理将假定 Pod 只想与在同一节点上的服务端点通信，如果没有本地端点，它将丢弃流量。 “Cluster” 默认将流量路由到所有端点（可能会根据拓扑和其他特性进行修改）"}
        self.internal_traffic_policy = internal_traffic_policy

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.session_affinity_config:
            self.session_affinity_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.selector is not None:
            result['selector'] = self.selector
        if self.cluster_ip is not None:
            result['clusterIP'] = self.cluster_ip
        if self.cluster_ips is not None:
            result['clusterIPs'] = self.cluster_ips
        if self.type is not None:
            result['type'] = self.type
        if self.external_ips is not None:
            result['externalIPs'] = self.external_ips
        if self.session_affinity is not None:
            result['sessionAffinity'] = self.session_affinity
        if self.load_balancer_ip is not None:
            result['loadBalancerIP'] = self.load_balancer_ip
        if self.load_balancer_source_ranges is not None:
            result['loadBalancerSourceRanges'] = self.load_balancer_source_ranges
        if self.external_name is not None:
            result['externalName'] = self.external_name
        if self.external_traffic_policy is not None:
            result['externalTrafficPolicy'] = self.external_traffic_policy
        if self.health_check_node_port is not None:
            result['healthCheckNodePort'] = self.health_check_node_port
        if self.publish_not_ready_addresses is not None:
            result['publishNotReadyAddresses'] = self.publish_not_ready_addresses
        if self.session_affinity_config is not None:
            result['sessionAffinityConfig'] = self.session_affinity_config.to_map()
        if self.ip_families is not None:
            result['ipFamilies'] = self.ip_families
        if self.ip_family_policy is not None:
            result['ipFamilyPolicy'] = self.ip_family_policy
        if self.allocate_load_balancer_node_ports is not None:
            result['allocateLoadBalancerNodePorts'] = self.allocate_load_balancer_node_ports
        if self.load_balancer_class is not None:
            result['loadBalancerClass'] = self.load_balancer_class
        if self.internal_traffic_policy is not None:
            result['internalTrafficPolicy'] = self.internal_traffic_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = PutPatchServiceServicePort()
                self.ports.append(temp_model.from_map(k))
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('clusterIP') is not None:
            self.cluster_ip = m.get('clusterIP')
        if m.get('clusterIPs') is not None:
            self.cluster_ips = m.get('clusterIPs')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('externalIPs') is not None:
            self.external_ips = m.get('externalIPs')
        if m.get('sessionAffinity') is not None:
            self.session_affinity = m.get('sessionAffinity')
        if m.get('loadBalancerIP') is not None:
            self.load_balancer_ip = m.get('loadBalancerIP')
        if m.get('loadBalancerSourceRanges') is not None:
            self.load_balancer_source_ranges = m.get('loadBalancerSourceRanges')
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')
        if m.get('externalTrafficPolicy') is not None:
            self.external_traffic_policy = m.get('externalTrafficPolicy')
        if m.get('healthCheckNodePort') is not None:
            self.health_check_node_port = m.get('healthCheckNodePort')
        if m.get('publishNotReadyAddresses') is not None:
            self.publish_not_ready_addresses = m.get('publishNotReadyAddresses')
        if m.get('sessionAffinityConfig') is not None:
            temp_model = PutPatchServiceSessionAffinityConfig()
            self.session_affinity_config = temp_model.from_map(m['sessionAffinityConfig'])
        if m.get('ipFamilies') is not None:
            self.ip_families = m.get('ipFamilies')
        if m.get('ipFamilyPolicy') is not None:
            self.ip_family_policy = m.get('ipFamilyPolicy')
        if m.get('allocateLoadBalancerNodePorts') is not None:
            self.allocate_load_balancer_node_ports = m.get('allocateLoadBalancerNodePorts')
        if m.get('loadBalancerClass') is not None:
            self.load_balancer_class = m.get('loadBalancerClass')
        if m.get('internalTrafficPolicy') is not None:
            self.internal_traffic_policy = m.get('internalTrafficPolicy')
        return self


class PutPatchServicePortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"the port number of the service port of which status is recorded here", "zh_CN":"port 是所记录的服务端口状态的端口号"}
        self.port = port
        # {"en":"the protocol of the service port of which status is recorded here The supported values are: 'TCP', 'UDP', 'SCTP'", "zh_CN":"protocol 是所记录的服务端口状态的协议。支持的值为：“TCP”、”UDP”、“SCTP”"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use CamelCase names - cloud provider specific error values must have names that comply with the format foo.example.com/CamelCase", "zh_CN":"error 是记录 PutPatchServiceService 端口的问题。 错误的格式应符合以下规则:内置错误原因应在此文件中指定，应使用 CamelCase 名称。云提供商特定错误原因的名称必须符合格式 foo.example.com/CamelCase"}
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class PutPatchServiceLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        host_name: str = None,
        ports: List[PutPatchServicePortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)", "zh_CN":"ip 是为基于 IP 的负载均衡器 Ingress 点（通常是 GCE 或 OpenStack 负载均衡器）设置的"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)", "zh_CN":"hostname 是为基于 DNS 的负载均衡器 Ingress 点（通常是 AWS 负载均衡器）设置的"}
        self.host_name = host_name
        # {"en":"Ports is a list of records of service ports If used, every port defined in the service should have an entry in it", "zh_CN":"ports 是 PutPatchServiceService 的端口列表。如果设置了此字段，PutPatchServiceService 中定义的每个端口都应该在此列表中"}
        self.ports = ports

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = PutPatchServicePortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class PutPatchServiceLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[PutPatchServiceLoadBalancerIngress] = None,
    ):
        # {"en":"Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points", "zh_CN":"ingress 是一个包含负载均衡器 Ingress 点的列表。PutPatchServiceService 的流量需要被发送到这些 Ingress 点"}
        self.ingress = ingress

    def validate(self):
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = PutPatchServiceLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class PutPatchServiceMetaV1Condition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        observed_generation: int = None,
        last_transition_time: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type of condition in CamelCase or in foo.example.com/CamelCase", "zh_CN":"CamelCase 或 foo.example.com/CamelCase 中的条件类型"}
        self.type = type
        # {"en":"status of the condition, one of True, False, Unknown", "zh_CN":"condition 的状态，True、False、Unknown 之一"}
        self.status = status
        # {"en":"observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance", "zh_CN":"表示设置 condition 基于的 .metadata.generation 的过期次数。 例如，如果 .metadata.generation 当前为 12，但 .status.conditions[x].observedGeneration 为 9， 则 condition 相对于实例的当前状态已过期"}
        self.observed_generation = observed_generation
        # {"en":"lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable", "zh_CN":"状况最近一次状态转化的时间。 变化应该发生在下层状况发生变化的时候。如果不知道下层状况发生变化的时间， 那么使用 API 字段更改的时间是可以接受的"}
        self.last_transition_time = last_transition_time
        # {"en":"reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty", "zh_CN":"reason 包含一个程序标识符，指示 condition 最后一次转换的原因。 特定条件类型的生产者可以定义该字段的预期值和含义，以及这些值是否被视为有保证的 API。 该值应该是 CamelCase 字符串且不能为空"}
        self.reason = reason
        # {"en":"message is a human readable message indicating details about the transition. This may be an empty string", "zh_CN":"message 是人类可读的消息，有关转换的详细信息，可以是空字符串"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PutPatchServiceServiceStatus(TeaModel):
    def __init__(
        self,
        load_balancer: PutPatchServiceLoadBalancerStatus = None,
        conditions: List[PutPatchServiceMetaV1Condition] = None,
    ):
        # {"en":"Current service state", "zh_CN":"loadBalancer 包含负载均衡器的当前状态（如果存在）"}
        self.load_balancer = load_balancer
        # {"en":"LoadBalancer contains the current status of the load-balancer, if one is present", "zh_CN":"服务的当前状态"}
        self.conditions = conditions

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = PutPatchServiceLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = PutPatchServiceMetaV1Condition()
                self.conditions.append(temp_model.from_map(k))
        return self


class PutPatchServiceService(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutPatchServiceObjectMeta = None,
        spec: PutPatchServiceServiceSpec = None,
        status: PutPatchServiceServiceStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a service", "zh_CN":"spec 定义 PutPatchServiceService 的行为"}
        self.spec = spec
        # {"en":"Most recently observed status of the service. Populated by the system. Read-only", "zh_CN":"最近观察到的 PutPatchServiceService 状态。由系统填充。只读"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PutPatchServiceObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutPatchServiceServiceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PutPatchServiceServiceStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class PutPatchServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutPatchServiceService = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"service", "zh_CN":"service"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = PutPatchServiceService()
            self.data = temp_model.from_map(m['data'])
        return self


class PutPatchServicePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"service name", "zh_CN":"service 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class PutPatchServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutNetworkPolicyOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class PutNetworkPolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutNetworkPolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutNetworkPolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutNetworkPolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutNetworkPolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutNetworkPolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutNetworkPolicyFieldsV1 holds the first JSON version format as described in the 'PutNetworkPolicyFieldsV1' type", "zh_CN":"PutNetworkPolicyFieldsV1 包含类型 “PutNetworkPolicyFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = PutNetworkPolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutNetworkPolicyObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[PutNetworkPolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutNetworkPolicyManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = PutNetworkPolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutNetworkPolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutNetworkPolicyNetworkPolicyPort(TeaModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # {"en": "The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.", "zh_CN": "端口"}
        self.port = port
        # {"en": "The protocol (TCP, UDP) which traffic must match. If not specified, this field defaults to TCP.", "zh_CN": "协议"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class PutNetworkPolicyIPBlock(TeaModel):
    def __init__(
        self,
        cidr: str = None,
        except_: List[str] = None,
    ):
        # {"en": "CIDR is a string representing the IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64", "zh_CN": "生效IP网段"}
        self.cidr = cidr
        # {"en": "Except is a slice of CIDRs that should not be included within an IP Block Valid examples are 192.168.1.1/24 or 2001:db9::/64 Except values will be rejected if they are outside the CIDR range", "zh_CN": "例外IP网段"}
        self.except_ = except_

    def validate(self):
        self.validate_required(self.cidr, 'cidr')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.except_ is not None:
            result['except'] = self.except_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('except') is not None:
            self.except_ = m.get('except')
        return self


class PutNetworkPolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PutNetworkPolicyNsLabelSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[PutNetworkPolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PutNetworkPolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutNetworkPolicyPodLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        return self


class PutNetworkPolicyNetworkPolicyPeer(TeaModel):
    def __init__(
        self,
        ip_block: PutNetworkPolicyIPBlock = None,
        namespace_selector: PutNetworkPolicyNsLabelSelector = None,
        pod_selector: PutNetworkPolicyPodLabelSelector = None,
    ):
        # {"en": "PutNetworkPolicyIPBlock defines policy on a particular PutNetworkPolicyIPBlock. If this field is set then neither of the other fields can be.", "zh_CN": "IP规则"}
        self.ip_block = ip_block
        # {"en": "Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.If PodSelector is also set, then the PutNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.", "zh_CN": "namespace选择器"}
        self.namespace_selector = namespace_selector
        # {"en": "This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.If NamespaceSelector is also set, then the PutNetworkPolicyNetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.", "zh_CN": "pod选择器"}
        self.pod_selector = pod_selector

    def validate(self):
        if self.ip_block:
            self.ip_block.validate()
        if self.namespace_selector:
            self.namespace_selector.validate()
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_block is not None:
            result['ipBlock'] = self.ip_block.to_map()
        if self.namespace_selector is not None:
            result['namespaceSelector'] = self.namespace_selector.to_map()
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipBlock') is not None:
            temp_model = PutNetworkPolicyIPBlock()
            self.ip_block = temp_model.from_map(m['ipBlock'])
        if m.get('namespaceSelector') is not None:
            temp_model = PutNetworkPolicyNsLabelSelector()
            self.namespace_selector = temp_model.from_map(m['namespaceSelector'])
        if m.get('podSelector') is not None:
            temp_model = PutNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        return self


class PutNetworkPolicyNetworkPolicyEgressRule(TeaModel):
    def __init__(
        self,
        ports: List[PutNetworkPolicyNetworkPolicyPort] = None,
        to: List[PutNetworkPolicyNetworkPolicyPeer] = None,
    ):
        # {"en": "List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports
        # {"en": "List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.", "zh_CN": "出网规则信息"}
        self.to = to

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.to:
            for k in self.to:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.to is not None:
            result['to'] = []
            for k in self.to:
                result['to'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = PutNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('to') is not None:
            self.to = []
            for k in m.get('to'):
                temp_model = PutNetworkPolicyNetworkPolicyPeer()
                self.to.append(temp_model.from_map(k))
        return self


class PutNetworkPolicyNetworkPolicyIngressRule(TeaModel):
    def __init__(
        self,
        from_: List[PutNetworkPolicyNetworkPolicyPeer] = None,
        ports: List[PutNetworkPolicyNetworkPolicyPort] = None,
    ):
        # {"en": "List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.", "zh_CN": "入网规则信息"}
        self.from_ = from_
        # {"en": "List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.", "zh_CN": "限制端口"}
        self.ports = ports

    def validate(self):
        if self.from_:
            for k in self.from_:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = []
            for k in self.from_:
                result['from'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = []
            for k in m.get('from'):
                temp_model = PutNetworkPolicyNetworkPolicyPeer()
                self.from_.append(temp_model.from_map(k))
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = PutNetworkPolicyNetworkPolicyPort()
                self.ports.append(temp_model.from_map(k))
        return self


class PutNetworkPolicyNetworkPolicySpec(TeaModel):
    def __init__(
        self,
        egress: List[PutNetworkPolicyNetworkPolicyEgressRule] = None,
        ingress: List[PutNetworkPolicyNetworkPolicyIngressRule] = None,
        pod_selector: PutNetworkPolicyPodLabelSelector = None,
        policy_types: List[str] = None,
    ):
        # {"en": "List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the PutNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this PutNetworkPolicyNetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8", "zh_CN": "出网规则"}
        self.egress = egress
        # {"en": "List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the PutNetworkPolicyNetworkPolicy objects whose podSelector matches the pod. If this field is empty then this PutNetworkPolicyNetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)", "zh_CN": "入网规则"}
        self.ingress = ingress
        # {"en": "Selects the pods to which this PutNetworkPolicyNetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.", "zh_CN": "限制pod的选择器"}
        self.pod_selector = pod_selector
        # {"en": "List of rule types that the PutNetworkPolicyNetworkPolicy relates to. Valid options are Ingress, Egress, or Ingress,Egress. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ Egress ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include Egress (since such a policy would not include an Egress section and would otherwise default to just [ Ingress ]). This field is beta-level in 1.8", "zh_CN": "策略类型"}
        self.policy_types = policy_types

    def validate(self):
        if self.egress:
            for k in self.egress:
                if k:
                    k.validate()
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()
        self.validate_required(self.pod_selector, 'pod_selector')
        if self.pod_selector:
            self.pod_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress is not None:
            result['egress'] = []
            for k in self.egress:
                result['egress'].append(k.to_map() if k else None)
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        if self.pod_selector is not None:
            result['podSelector'] = self.pod_selector.to_map()
        if self.policy_types is not None:
            result['policyTypes'] = self.policy_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('egress') is not None:
            self.egress = []
            for k in m.get('egress'):
                temp_model = PutNetworkPolicyNetworkPolicyEgressRule()
                self.egress.append(temp_model.from_map(k))
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = PutNetworkPolicyNetworkPolicyIngressRule()
                self.ingress.append(temp_model.from_map(k))
        if m.get('podSelector') is not None:
            temp_model = PutNetworkPolicyPodLabelSelector()
            self.pod_selector = temp_model.from_map(m['podSelector'])
        if m.get('policyTypes') is not None:
            self.policy_types = m.get('policyTypes')
        return self


class PutNetworkPolicyRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutNetworkPolicyObjectMeta = None,
        spec: PutNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this PutNetworkPolicyNetworkPolicy.", "zh_CN": "PutNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PutNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PutNetworkPolicyNetworkPolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutNetworkPolicyObjectMeta = None,
        spec: PutNetworkPolicyNetworkPolicySpec = None,
    ):
        # {"en": "APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", "zh_CN": "版本号"}
        self.api_version = api_version
        # {"en": "Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds", "zh_CN": "被引用资源的类别"}
        self.kind = kind
        # {"en": "Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata", "zh_CN": "标准的对象元数据"}
        self.metadata = metadata
        # {"en": "Specification of the desired behavior for this PutNetworkPolicyNetworkPolicy.", "zh_CN": "PutNetworkPolicyNetworkPolicy 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PutNetworkPolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutNetworkPolicyNetworkPolicySpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PutNetworkPolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutNetworkPolicyNetworkPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"networkPolicy", "zh_CN":"网络策略"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = PutNetworkPolicyNetworkPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class PutNetworkPolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"networkPolicy name", "zh_CN":"networkPolicy 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class PutNetworkPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutNetworkPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutNetworkPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPUnassignEdgeIPRequest(TeaModel):
    def __init__(
        self,
        server_ip: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"target virtual machine external network Ip", "zh_CN":"目标实例外网Ip"}
        self.server_ip = server_ip
        # {"en":"additional Ip to unbind", "zh_CN":"要解除绑定的额外IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPUnassignEdgeIPResponse(TeaModel):
    def __init__(
        self,
        server_ip: str = None,
        edge_ips: List[str] = None,
    ):
        # {"en":"target virtual machine IP", "zh_CN":"目标实例公网IP"}
        self.server_ip = server_ip
        # {"en":"additional Ip that has been bound to the virtual machine", "zh_CN":"已绑定到实例的额外公网IP"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VMPUnassignEdgeIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgeIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgeIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPUnassignEdgeIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetIngressRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class GetIngressFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetIngressFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetIngressManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetIngressFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetIngressFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetIngressFieldsV1 holds the first JSON version format as described in the 'GetIngressFieldsV1' type", "zh_CN":"GetIngressFieldsV1 包含类型 “GetIngressFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = GetIngressFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetIngressObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[GetIngressOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetIngressManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = GetIngressOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetIngressManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetIngressServiceBackendPort(TeaModel):
    def __init__(
        self,
        name: str = None,
        number: int = None,
    ):
        # {"en":"Name is the name of the port on the Service", "zh_CN":"服务端口名称"}
        self.name = name
        # {"en":"Number is the numerical port number on the Service", "zh_CN":"服务数字端口"}
        self.number = number

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.number, 'number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class GetIngressIngressServiceBackend(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: GetIngressServiceBackendPort = None,
    ):
        # {"en":"Name is the referenced service", "zh_CN":"服务名称"}
        self.name = name
        # {"en":"Port of the referenced service. A port name or port number", "zh_CN":"服务端口或端口名称"}
        self.port = port

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.port, 'port')
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            temp_model = GetIngressServiceBackendPort()
            self.port = temp_model.from_map(m['port'])
        return self


class GetIngressTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        api_group: str = None,
    ):
        # {"en":"Name is the name of resource being referenced", "zh_CN":"资源名称"}
        self.name = name
        # {"en":"Kind is the type of resource being referenced", "zh_CN":"资源类型"}
        self.kind = kind
        # {"en":"APIGroup is the group for the resource being referenced", "zh_CN":"资源分组"}
        self.api_group = api_group

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_group, 'api_group')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        return self


class GetIngressIngressBackend(TeaModel):
    def __init__(
        self,
        service: GetIngressIngressServiceBackend = None,
        resource: GetIngressTypedLocalObjectReference = None,
    ):
        # {"en":"Service references a Service as a Backend", "zh_CN":"指定后端服务"}
        self.service = service
        # {"en":"Resource is an ObjectRef to another Kubernetes resource in the namespace of the GetIngressIngress object", "zh_CN":"路由指定后端资源"}
        self.resource = resource

    def validate(self):
        self.validate_required(self.service, 'service')
        if self.service:
            self.service.validate()
        self.validate_required(self.resource, 'resource')
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['service'] = self.service.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service') is not None:
            temp_model = GetIngressIngressServiceBackend()
            self.service = temp_model.from_map(m['service'])
        if m.get('resource') is not None:
            temp_model = GetIngressTypedLocalObjectReference()
            self.resource = temp_model.from_map(m['resource'])
        return self


class GetIngressIngressTLS(TeaModel):
    def __init__(
        self,
        hosts: List[str] = None,
        secret_name: str = None,
    ):
        # {"en":"Hosts are a list of hosts included in the TLS certificate", "zh_CN":"tls证书包含域名"}
        self.hosts = hosts
        # {"en":"SecretName is the name of the secret used to terminate TLS traffic on port 443", "zh_CN":"tls秘钥名称"}
        self.secret_name = secret_name

    def validate(self):
        self.validate_required(self.hosts, 'hosts')
        self.validate_required(self.secret_name, 'secret_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['hosts'] = self.hosts
        if self.secret_name is not None:
            result['secretName'] = self.secret_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        if m.get('secretName') is not None:
            self.secret_name = m.get('secretName')
        return self


class GetIngressHTTPIngressPath(TeaModel):
    def __init__(
        self,
        path: str = None,
        path_type: str = None,
        backend: GetIngressIngressBackend = None,
    ):
        # {"en":"Path is matched against the path of an incoming request", "zh_CN":"请求路径"}
        self.path = path
        # {"en":"PathType determines the interpretation of the Path matching,PathType can be one of the following values: Exact,Prefix,ImplementationSpecific", "zh_CN":"路径匹配类型: Exact,Prefix,ImplementationSpecific"}
        self.path_type = path_type
        # {"en":"Backend defines the referenced service endpoint to which the traffic will be forwarded to", "zh_CN":"指定后端服务"}
        self.backend = backend

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.path_type, 'path_type')
        self.validate_required(self.backend, 'backend')
        if self.backend:
            self.backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.path_type is not None:
            result['pathType'] = self.path_type
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        if m.get('backend') is not None:
            temp_model = GetIngressIngressBackend()
            self.backend = temp_model.from_map(m['backend'])
        return self


class GetIngressHTTPIngressRuleValue(TeaModel):
    def __init__(
        self,
        paths: List[GetIngressHTTPIngressPath] = None,
    ):
        # {"en":"A collection of paths that map requests to backends", "zh_CN":"请求路径匹配规则"}
        self.paths = paths

    def validate(self):
        self.validate_required(self.paths, 'paths')
        if self.paths:
            for k in self.paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paths is not None:
            result['paths'] = []
            for k in self.paths:
                result['paths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paths') is not None:
            self.paths = []
            for k in m.get('paths'):
                temp_model = GetIngressHTTPIngressPath()
                self.paths.append(temp_model.from_map(k))
        return self


class GetIngressIngressRule(TeaModel):
    def __init__(
        self,
        host: str = None,
        http: GetIngressHTTPIngressRuleValue = None,
    ):
        # {"en":"Host is the fully qualified domain name of a network host", "zh_CN":"域名"}
        self.host = host
        self.http = http

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.http, 'http')
        if self.http:
            self.http.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.http is not None:
            result['http'] = self.http.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('http') is not None:
            temp_model = GetIngressHTTPIngressRuleValue()
            self.http = temp_model.from_map(m['http'])
        return self


class GetIngressIngressSpec(TeaModel):
    def __init__(
        self,
        ingress_class_name: str = None,
        default_backend: GetIngressIngressBackend = None,
        tls: List[GetIngressIngressTLS] = None,
        rules: List[GetIngressIngressRule] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.ingress_class_name = ingress_class_name
        # {"en":"DefaultBackend is the backend that should handle requests that don't match any rule", "zh_CN":"默认后端,当请求不匹配任何规则时调用"}
        self.default_backend = default_backend
        self.tls = tls
        # {"en":"A list of host rules used to configure the GetIngressIngress", "zh_CN":"路由规则列表"}
        self.rules = rules

    def validate(self):
        self.validate_required(self.ingress_class_name, 'ingress_class_name')
        self.validate_required(self.default_backend, 'default_backend')
        if self.default_backend:
            self.default_backend.validate()
        self.validate_required(self.tls, 'tls')
        if self.tls:
            for k in self.tls:
                if k:
                    k.validate()
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
        if self.ingress_class_name is not None:
            result['ingressClassName'] = self.ingress_class_name
        if self.default_backend is not None:
            result['defaultBackend'] = self.default_backend.to_map()
        if self.tls is not None:
            result['tls'] = []
            for k in self.tls:
                result['tls'].append(k.to_map() if k else None)
        if self.rules is not None:
            result['rules'] = []
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressClassName') is not None:
            self.ingress_class_name = m.get('ingressClassName')
        if m.get('defaultBackend') is not None:
            temp_model = GetIngressIngressBackend()
            self.default_backend = temp_model.from_map(m['defaultBackend'])
        if m.get('tls') is not None:
            self.tls = []
            for k in m.get('tls'):
                temp_model = GetIngressIngressTLS()
                self.tls.append(temp_model.from_map(k))
        if m.get('rules') is not None:
            self.rules = []
            for k in m.get('rules'):
                temp_model = GetIngressIngressRule()
                self.rules.append(temp_model.from_map(k))
        return self


class GetIngressPortStatus(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        error: str = None,
    ):
        # {"en":"Port is the port number of the service port of which status is recorded here", "zh_CN":"服务端口"}
        self.port = port
        # {"en":"Protocol is the protocol of the service port of which status is recorded here,The supported values are: TCP, UDP, SCTP", "zh_CN":"服务支持类型: TCP,UDP,SCTP"}
        self.protocol = protocol
        # {"en":"Error is to record the problem with the service port", "zh_CN":"记录服务端口错误信息"}
        self.error = error

    def validate(self):
        self.validate_required(self.port, 'port')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.error, 'error')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self


class GetIngressLoadBalancerIngress(TeaModel):
    def __init__(
        self,
        ip: str = None,
        hostname: str = None,
        ports: List[GetIngressPortStatus] = None,
    ):
        # {"en":"IP is set for load-balancer ingress points that are IP based", "zh_CN":"负载均衡服务ip"}
        self.ip = ip
        # {"en":"Hostname is set for load-balancer ingress points that are DNS based", "zh_CN":"负载均衡类型服务dns"}
        self.hostname = hostname
        # {"en":"Ports is a list of records of service ports", "zh_CN":"服务端口状态列表"}
        self.ports = ports

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.ports, 'ports')
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.ports is not None:
            result['ports'] = []
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('ports') is not None:
            self.ports = []
            for k in m.get('ports'):
                temp_model = GetIngressPortStatus()
                self.ports.append(temp_model.from_map(k))
        return self


class GetIngressLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        ingress: List[GetIngressLoadBalancerIngress] = None,
    ):
        self.ingress = ingress

    def validate(self):
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            for k in self.ingress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress is not None:
            result['ingress'] = []
            for k in self.ingress:
                result['ingress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingress') is not None:
            self.ingress = []
            for k in m.get('ingress'):
                temp_model = GetIngressLoadBalancerIngress()
                self.ingress.append(temp_model.from_map(k))
        return self


class GetIngressIngressStatus(TeaModel):
    def __init__(
        self,
        load_balancer: GetIngressLoadBalancerStatus = None,
    ):
        # {"en":"LoadBalancer contains the current status of the load-balancer", "zh_CN":"包含当前负载均衡服务的状态"}
        self.load_balancer = load_balancer

    def validate(self):
        self.validate_required(self.load_balancer, 'load_balancer')
        if self.load_balancer:
            self.load_balancer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['loadBalancer'] = self.load_balancer.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loadBalancer') is not None:
            temp_model = GetIngressLoadBalancerStatus()
            self.load_balancer = temp_model.from_map(m['loadBalancer'])
        return self


class GetIngressIngress(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetIngressObjectMeta = None,
        spec: GetIngressIngressSpec = None,
        status: GetIngressIngressStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"ingress desired", "zh_CN":"路由期望属性"}
        self.spec = spec
        # {"en":"Status is the current state of the GetIngressIngress", "zh_CN":"路由状态"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetIngressObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetIngressIngressSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = GetIngressIngressStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class GetIngressCustomIngressDetail(TeaModel):
    def __init__(
        self,
        controller_name: str = None,
        clusters: List[str] = None,
        ingress: GetIngressIngress = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.controller_name = controller_name
        # {"en":"clusters", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"ingress", "zh_CN":"路由"}
        self.ingress = ingress
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"create time", "zh_CN":"更新时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.controller_name, 'controller_name')
        self.validate_required(self.clusters, 'clusters')
        self.validate_required(self.ingress, 'ingress')
        if self.ingress:
            self.ingress.validate()
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.controller_name is not None:
            result['controllerName'] = self.controller_name
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.ingress is not None:
            result['ingress'] = self.ingress.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controllerName') is not None:
            self.controller_name = m.get('controllerName')
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('ingress') is not None:
            temp_model = GetIngressIngress()
            self.ingress = temp_model.from_map(m['ingress'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetIngressResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetIngressCustomIngressDetail = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress object", "zh_CN":"路由对象"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetIngressCustomIngressDetail()
            self.data = temp_model.from_map(m['data'])
        return self


class GetIngressPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress name", "zh_CN":"路由名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetIngressParameters(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class GetIngressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIngressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteIngressControllerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteIngressControllerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteIngressControllerPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteIngressControllerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteIngressControllerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteIngressControllerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateIngressControllerIngressCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        replicate: int = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"replicates", "zh_CN":"副本数"}
        self.replicate = replicate

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.replicate, 'replicate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.replicate is not None:
            result['replicate'] = self.replicate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicate') is not None:
            self.replicate = m.get('replicate')
        return self


class CreateIngressControllerRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        limit: Dict[str, str] = None,
        request: Dict[str, str] = None,
        clusters: List[CreateIngressControllerIngressCluster] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name
        # {"en":"resource limit", "zh_CN":"资源限制"}
        self.limit = limit
        # {"en":"resource request", "zh_CN":"所需资源"}
        self.request = request
        # {"en":"cluster and replicate", "zh_CN":"部署集群和副本数"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.request, 'request')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.request is not None:
            result['request'] = self.request
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = CreateIngressControllerIngressCluster()
                self.clusters.append(temp_model.from_map(k))
        return self


class CreateIngressControllerIngressController(TeaModel):
    def __init__(
        self,
        name: str = None,
        limit: Dict[str, str] = None,
        request: Dict[str, str] = None,
        clusters: List[CreateIngressControllerIngressCluster] = None,
    ):
        # {"en":"ingress controller name", "zh_CN":"路由控制器名称"}
        self.name = name
        # {"en":"resource limit", "zh_CN":"资源限制"}
        self.limit = limit
        # {"en":"resource request", "zh_CN":"所需资源"}
        self.request = request
        # {"en":"cluster and replicate", "zh_CN":"部署集群和副本数"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.request, 'request')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.request is not None:
            result['request'] = self.request
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = CreateIngressControllerIngressCluster()
                self.clusters.append(temp_model.from_map(k))
        return self


class CreateIngressControllerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateIngressControllerIngressController = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress controller", "zh_CN":"路由控制器"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = CreateIngressControllerIngressController()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateIngressControllerPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressControllerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressControllerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateIngressControllerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListIngressControllerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressControllerClusterAttr(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        cluster_name_cn: str = None,
        ip: str = None,
        replicas: int = None,
        ready_replicas: int = None,
        available_replicas: int = None,
        updated_replicas: str = None,
    ):
        # {"en":"cluster name ", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"cluster cn name", "zh_CN":"集群中文名"}
        self.cluster_name_cn = cluster_name_cn
        # {"en":"service ip ", "zh_CN":"服务ip"}
        self.ip = ip
        # {"en":"Total number of non-terminated pods targeted by this deployment (their labels match the selector).", "zh_CN":"期望副本数"}
        self.replicas = replicas
        # {"en":"Total number of ready pods targeted by this deployment", "zh_CN":"就绪副本数"}
        self.ready_replicas = ready_replicas
        # {"en":"Total number of available pods (ready for at least minReadySeconds) targeted by this deployment", "zh_CN":"一段时间内(minReadySeconds)就绪副本数"}
        self.available_replicas = available_replicas
        # {"en":"Total number of non-terminated pods targeted by this deployment that have the desired template spec.", "zh_CN":"可访问副本数"}
        self.updated_replicas = updated_replicas

    def validate(self):
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.cluster_name_cn, 'cluster_name_cn')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.replicas, 'replicas')
        self.validate_required(self.ready_replicas, 'ready_replicas')
        self.validate_required(self.available_replicas, 'available_replicas')
        self.validate_required(self.updated_replicas, 'updated_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cluster_name_cn is not None:
            result['clusterNameCn'] = self.cluster_name_cn
        if self.ip is not None:
            result['ip'] = self.ip
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.ready_replicas is not None:
            result['readyReplicas'] = self.ready_replicas
        if self.available_replicas is not None:
            result['availableReplicas'] = self.available_replicas
        if self.updated_replicas is not None:
            result['updatedReplicas'] = self.updated_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('clusterNameCn') is not None:
            self.cluster_name_cn = m.get('clusterNameCn')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('readyReplicas') is not None:
            self.ready_replicas = m.get('readyReplicas')
        if m.get('availableReplicas') is not None:
            self.available_replicas = m.get('availableReplicas')
        if m.get('updatedReplicas') is not None:
            self.updated_replicas = m.get('updatedReplicas')
        return self


class ListIngressControllerIngressControllerItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
        create_time: int = None,
        update_time: int = None,
        clusters: List[ListIngressControllerClusterAttr] = None,
    ):
        # {"en":"ingress controller name ", "zh_CN":"路由控制器名称"}
        self.name = name
        # {"en":"ingress controller status", "zh_CN":"路由控制器状态"}
        self.status = status
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"update time", "zh_CN":"更新时间"}
        self.update_time = update_time
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = ListIngressControllerClusterAttr()
                self.clusters.append(temp_model.from_map(k))
        return self


class ListIngressControllerIngressControllerList(TeaModel):
    def __init__(
        self,
        total: int = None,
        items: List[ListIngressControllerIngressControllerItem] = None,
    ):
        # {"en":"total  count", "zh_CN":"总数"}
        self.total = total
        self.items = items

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListIngressControllerIngressControllerItem()
                self.items.append(temp_model.from_map(k))
        return self


class ListIngressControllerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListIngressControllerIngressControllerList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ingress controller list", "zh_CN":"路由控制器列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListIngressControllerIngressControllerList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListIngressControllerPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressControllerParameters(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"en":"keyword", "zh_CN":"关键字"}
        self.keyword = keyword
        # {"en":"page index", "zh_CN":"页数"}
        self.page_index = page_index
        # {"en":"page size", "zh_CN":"每页数量"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListIngressControllerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListIngressControllerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VmpEdgeIpAllocate4OccupancyRequest(TeaModel):
    def __init__(
        self,
        server_ip: str = None,
        protocol: str = None,
        native_attribute: str = None,
        cidr: str = None,
        carrier: str = None,
        random_allocate_ip: int = None,
        count: int = None,
    ):
        # {"en":"Instance IP to be bound", "zh_CN":"额外IP要绑定的实例IP"}
        self.server_ip = server_ip
        # {"en":"IP protocol: 4-ipv4(default); 6-ipv6", "zh_CN":"IP协议：4-ipv4（默认）；6-ipv6"}
        self.protocol = protocol
        # {"en":"IP native attribute, 1: non-native;-1: native;", "zh_CN":"指定IPv4原生属性。可选值：1：非原生，-1：原生。不指定默认随机分配原生属性"}
        self.native_attribute = native_attribute
        # {"en":"CIDR", "zh_CN":"指定CIDR申请IP"}
        self.cidr = cidr
        # {"en":"null", "zh_CN":"A、实例有多个运营商IP时，可指定额外IP运营商
        # B、不指定时：
        # 实例单运营商IP，额外IP运营商一致
        # 实例多运营商IP，额外IP选其中一个运营商
        # BGP节点该字段不生效。"}
        self.carrier = carrier
        # {"en":"Allocate ip random", "zh_CN":"IPv4是否随机分配
        # 1：是
        # -1：否"}
        self.random_allocate_ip = random_allocate_ip
        # {"en":"number of applications IP", "zh_CN":"申请个数"}
        self.count = count

    def validate(self):
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.native_attribute is not None:
            result['nativeAttribute'] = self.native_attribute
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.random_allocate_ip is not None:
            result['randomAllocateIp'] = self.random_allocate_ip
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('nativeAttribute') is not None:
            self.native_attribute = m.get('nativeAttribute')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('randomAllocateIp') is not None:
            self.random_allocate_ip = m.get('randomAllocateIp')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class VmpEdgeIpAllocate4OccupancyResponse(TeaModel):
    def __init__(
        self,
        edge_ips: List[str] = None,
    ):
        # {"en":"successful application for all or part of IP", "zh_CN":"成功申请到的全部或部分IP 
        # 说明：不同场景的响应说明如下 A、所有IP都申请成功，返回申请到的所有IP B、只申请到部分IP，返回申请到的那部分IP C、未申请到任何IP，返回失败信息 D、若出现申请失败的情况，请间隔10S之后再次申请"}
        self.edge_ips = edge_ips

    def validate(self):
        self.validate_required(self.edge_ips, 'edge_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_ips is not None:
            result['edgeIps'] = self.edge_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeIps') is not None:
            self.edge_ips = m.get('edgeIps')
        return self


class VmpEdgeIpAllocate4OccupancyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIpAllocate4OccupancyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIpAllocate4OccupancyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmpEdgeIpAllocate4OccupancyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




