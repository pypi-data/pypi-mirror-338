# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryEdgeHostnamesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnamesResponseDataEdgeHostnamesHostnames(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        target: str = None,
    ):
        # {"en":"name of the domain which use this edge-hostname.", "zh_CN":"域名。"}
        self.hostname = hostname
        # {"en":"the deploy target of this hostname.", "zh_CN":"部署环境。"}
        self.target = target

    def validate(self):
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.target, 'target')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class QueryEdgeHostnamesResponseDataEdgeHostnames(TeaModel):
    def __init__(
        self,
        edge_hostname_id: int = None,
        edge_hostname: str = None,
        dns_service_status: str = None,
        deploy_status: str = None,
        allow_china_cdn: str = None,
        comment: str = None,
        creation_time: str = None,
        last_update_time: str = None,
        hostnames: List[QueryEdgeHostnamesResponseDataEdgeHostnamesHostnames] = None,
    ):
        # {"en":"Edge-Hostname ID.", "zh_CN":"调度域名标识"}
        self.edge_hostname_id = edge_hostname_id
        # {"en":"Edge-Hostname.", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname
        # {"en":"dns service status.data range:[inactive, active]", "zh_CN":"DNS服务状态。取值范围：[inactive, active]"}
        self.dns_service_status = dns_service_status
        # {"en":"deploy status.data range:[pending, deploying, success, fail].", "zh_CN":"部署状态。取值范围：[pending, deploying, success, fail]"}
        self.deploy_status = deploy_status
        # {"en":"allow china cdn.,data range:[0,1].remark: 0 no, 1 yes.", "zh_CN":"是否允许中国大陆加速。取值范围：[0,1]。备注：0 否，1 是。"}
        self.allow_china_cdn = allow_china_cdn
        # {"en":"Edge-Hostname comment.", "zh_CN":"调度域名描述。"}
        self.comment = comment
        # {"en":"RFC3339 format date indicating when the Edge-Hostname was created.", "zh_CN":"RFC 3339格式的日期，表示创建调度域名的时间。"}
        self.creation_time = creation_time
        # {"en":"RFC3339 date indicating when the Edge-Hostname was last updated.", "zh_CN":"RFC 3339格式的日期，表示调度域名的最近更新时间。"}
        self.last_update_time = last_update_time
        # {"en":"hostnames.", "zh_CN":"域名列表"}
        self.hostnames = hostnames

    def validate(self):
        self.validate_required(self.edge_hostname_id, 'edge_hostname_id')
        self.validate_required(self.edge_hostname, 'edge_hostname')
        self.validate_required(self.dns_service_status, 'dns_service_status')
        self.validate_required(self.deploy_status, 'deploy_status')
        self.validate_required(self.allow_china_cdn, 'allow_china_cdn')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.last_update_time, 'last_update_time')
        if self.hostnames:
            for k in self.hostnames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname_id is not None:
            result['edgeHostnameId'] = self.edge_hostname_id
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.dns_service_status is not None:
            result['dnsServiceStatus'] = self.dns_service_status
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.allow_china_cdn is not None:
            result['allowChinaCdn'] = self.allow_china_cdn
        if self.comment is not None:
            result['comment'] = self.comment
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.hostnames is not None:
            result['hostnames'] = []
            for k in self.hostnames:
                result['hostnames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnameId') is not None:
            self.edge_hostname_id = m.get('edgeHostnameId')
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('dnsServiceStatus') is not None:
            self.dns_service_status = m.get('dnsServiceStatus')
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('allowChinaCdn') is not None:
            self.allow_china_cdn = m.get('allowChinaCdn')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('hostnames') is not None:
            self.hostnames = []
            for k in m.get('hostnames'):
                temp_model = QueryEdgeHostnamesResponseDataEdgeHostnamesHostnames()
                self.hostnames.append(temp_model.from_map(k))
        return self


class QueryEdgeHostnamesResponseData(TeaModel):
    def __init__(
        self,
        count: int = None,
        edge_hostnames: List[QueryEdgeHostnamesResponseDataEdgeHostnames] = None,
    ):
        # {"en":"Number of properties.", "zh_CN":"调度域名数量。"}
        self.count = count
        # {"en":"List of properties.", "zh_CN":"项目列表。"}
        self.edge_hostnames = edge_hostnames

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.edge_hostnames, 'edge_hostnames')
        if self.edge_hostnames:
            for k in self.edge_hostnames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.edge_hostnames is not None:
            result['edgeHostnames'] = []
            for k in self.edge_hostnames:
                result['edgeHostnames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('edgeHostnames') is not None:
            self.edge_hostnames = []
            for k in m.get('edgeHostnames'):
                temp_model = QueryEdgeHostnamesResponseDataEdgeHostnames()
                self.edge_hostnames.append(temp_model.from_map(k))
        return self


class QueryEdgeHostnamesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryEdgeHostnamesResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data.", "zh_CN":"接口响应数据"}
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
            temp_model = QueryEdgeHostnamesResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryEdgeHostnamesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnamesParameters(TeaModel):
    def __init__(
        self,
        edge_hostnames: str = None,
        hostnames: str = None,
        comment: str = None,
        dns_service_status: str = None,
        deploy_status: str = None,
        is_like: bool = None,
        allow_china_cdn: str = None,
        offset: int = None,
        limit: int = None,
        sort_order: str = None,
        sort_by: str = None,
    ):
        # {"en":"edgeHostnames.", "zh_CN":"调度域名列表。多个以英文逗号分割"}
        self.edge_hostnames = edge_hostnames
        # {"en":"hostnames.", "zh_CN":"域名列表。多个以英文逗号分割"}
        self.hostnames = hostnames
        # {"en":"comment.", "zh_CN":"调度域名描述	。"}
        self.comment = comment
        # {"en":"The value can be 'inactive', or 'active' to filter the results based on dns service status.", "zh_CN":"DNS服务状态。取值范围：[inactive, active]"}
        self.dns_service_status = dns_service_status
        # {"en":"The value can be 'pending', or 'deploying', or 'success', or 'fail' to filter the results based on deploy status.remark:split with comma", "zh_CN":"部署状态。多个以英文逗号分割"}
        self.deploy_status = deploy_status
        # {"en":"fuzzy query.only used for edgeHostnames,hostnames and comment", "zh_CN":"是否模糊匹配。只对edgeHostnames、hostnames与comment有效"}
        self.is_like = is_like
        # {"en":"The value can be '0', or '1' to filter the results based on allow china cdn .", "zh_CN":"是否允许中国大陆加速。"}
        self.allow_china_cdn = allow_china_cdn
        # {"en":"Indicates the first item to return. The default is '0'.", "zh_CN":"查询起始位置。默认值: 0 取值范围: >= 0"}
        self.offset = offset
        # {"en":"Maximum number of properties to return.  Default: 100 Range: <= 200", "zh_CN":"每次查询的最大条数。默认值: 100 取值范围: <= 200"}
        self.limit = limit
        # {"en":"Order of properties to return. Enum: asc,desc Default: desc", "zh_CN":"返回结果的顺序。默认按最后更新时间降序。取值范围: asc,desc 默认值: desc"}
        self.sort_order = sort_order
        # {"en":"Returns results in sorted order. Enum: creationTime,lastUpdateTime,edgeHostname Default: lastUpdateTime", "zh_CN":"返回结果的排序依据。取值范围: creationTime,lastUpdateTime,edgeHostname 默认值: lastUpdateTime"}
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostnames is not None:
            result['edgeHostnames'] = self.edge_hostnames
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.comment is not None:
            result['comment'] = self.comment
        if self.dns_service_status is not None:
            result['dnsServiceStatus'] = self.dns_service_status
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.is_like is not None:
            result['isLike'] = self.is_like
        if self.allow_china_cdn is not None:
            result['allowChinaCdn'] = self.allow_china_cdn
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnames') is not None:
            self.edge_hostnames = m.get('edgeHostnames')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('dnsServiceStatus') is not None:
            self.dns_service_status = m.get('dnsServiceStatus')
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('isLike') is not None:
            self.is_like = m.get('isLike')
        if m.get('allowChinaCdn') is not None:
            self.allow_china_cdn = m.get('allowChinaCdn')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        return self


class QueryEdgeHostnamesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnamesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class DeleteEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class DeleteEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EnableEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class EnableEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class EnableEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeployAkcdnEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployAkcdnEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class DeployAkcdnEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class DeployAkcdnEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployAkcdnEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployAkcdnEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnameResponseDataHostnames(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        target: str = None,
        property_id: int = None,
        property_version: int = None,
        property_name: str = None,
    ):
        # {"en":"hostname", "zh_CN":"域名"}
        self.hostname = hostname
        # {"en":"deploy target", "zh_CN":"部署环境"}
        self.target = target
        # {"en":"property id", "zh_CN":"项目ID"}
        self.property_id = property_id
        # {"en":"property version", "zh_CN":"项目版本"}
        self.property_version = property_version
        # {"en":"property name", "zh_CN":"项目名称"}
        self.property_name = property_name

    def validate(self):
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.target, 'target')
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.property_version, 'property_version')
        self.validate_required(self.property_name, 'property_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.target is not None:
            result['target'] = self.target
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.property_version is not None:
            result['propertyVersion'] = self.property_version
        if self.property_name is not None:
            result['propertyName'] = self.property_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('propertyVersion') is not None:
            self.property_version = m.get('propertyVersion')
        if m.get('propertyName') is not None:
            self.property_name = m.get('propertyName')
        return self


class QueryEdgeHostnameResponseDataRegionConfigs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        action_type: str = None,
        config_type: str = None,
        config_value: str = None,
        ip_protocol: str = None,
        ttl: str = None,
        weight: int = None,
    ):
        # {"en":"region id", "zh_CN":"区域ID"}
        self.region_id = region_id
        # {"en":"action type", "zh_CN":"调度方式。"}
        self.action_type = action_type
        # {"en":"config type", "zh_CN":"记录类型。"}
        self.config_type = config_type
        # {"en":"config value", "zh_CN":"记录值。"}
        self.config_value = config_value
        # {"en":"ip protocol.", "zh_CN":"ip协议。"}
        self.ip_protocol = ip_protocol
        # {"en":"ttl", "zh_CN":"生存时间。"}
        self.ttl = ttl
        # {"en":"weight", "zh_CN":"权重。"}
        self.weight = weight

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.action_type, 'action_type')
        self.validate_required(self.config_type, 'config_type')
        self.validate_required(self.config_value, 'config_value')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.config_value is not None:
            result['configValue'] = self.config_value
        if self.ip_protocol is not None:
            result['ipProtocol'] = self.ip_protocol
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        if m.get('ipProtocol') is not None:
            self.ip_protocol = m.get('ipProtocol')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class QueryEdgeHostnameResponseData(TeaModel):
    def __init__(
        self,
        edge_hostname_id: int = None,
        edge_hostname: str = None,
        comment: str = None,
        dns_service_status: str = None,
        deploy_status: str = None,
        allow_china_cdn: str = None,
        gdpr_compliant: str = None,
        geo_fence: str = None,
        creation_time: str = None,
        last_update_time: str = None,
        hostnames: List[QueryEdgeHostnameResponseDataHostnames] = None,
        region_configs: QueryEdgeHostnameResponseDataRegionConfigs = None,
    ):
        # {"en":"Edge-Hostname ID", "zh_CN":"调度域名ID"}
        self.edge_hostname_id = edge_hostname_id
        # {"en":"Edge-Hostname Name", "zh_CN":"调度域名。"}
        self.edge_hostname = edge_hostname
        # {"en":"Edge-Hostname comment.", "zh_CN":"调度域名描述。"}
        self.comment = comment
        # {"en":"dns service status.data range:[inactive, active]", "zh_CN":"DNS服务状态。取值范围：[inactive, active]"}
        self.dns_service_status = dns_service_status
        # {"en":"deploy status.data range:[pending, deploying, success, fail]", "zh_CN":"部署状态。取值范围：[pending, deploying, success, fail]"}
        self.deploy_status = deploy_status
        # {"en":"allow china cdn.,data range:[0,1].remark: 0 no, 1 yes.", "zh_CN":"是否允许中国大陆加速。取值范围：[0,1]。备注：0 否，1 是。"}
        self.allow_china_cdn = allow_china_cdn
        # {"en":"gdpr compliant,data range:[0,1,2].", "zh_CN":"遵循GDPR,取值范围：[0,1,2]。"}
        self.gdpr_compliant = gdpr_compliant
        # {"en":"geoFence, data range: [global,inside_china_mainland,exclude_china_mainland].", "zh_CN":"加速区域限定。取值范围：[global,inside_china_mainland,exclude_china_mainland]。"}
        self.geo_fence = geo_fence
        # {"en":"RFC3339 format date indicating when the edge-hostname was created.", "zh_CN":"RFC 3339格式的日期，表示创建edge-hostname的时间。"}
        self.creation_time = creation_time
        # {"en":"RFC3339 date indicating when the edge-hostname was last updated.", "zh_CN":"RFC 3339格式的日期，表示edge-hostname的最近更新时间。"}
        self.last_update_time = last_update_time
        # {"en":"hostnames", "zh_CN":"关联的加速域名"}
        self.hostnames = hostnames
        # {"en":"region configuration", "zh_CN":"区域配置列表 "}
        self.region_configs = region_configs

    def validate(self):
        self.validate_required(self.edge_hostname_id, 'edge_hostname_id')
        self.validate_required(self.edge_hostname, 'edge_hostname')
        self.validate_required(self.dns_service_status, 'dns_service_status')
        self.validate_required(self.deploy_status, 'deploy_status')
        self.validate_required(self.allow_china_cdn, 'allow_china_cdn')
        self.validate_required(self.geo_fence, 'geo_fence')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.last_update_time, 'last_update_time')
        if self.hostnames:
            for k in self.hostnames:
                if k:
                    k.validate()
        self.validate_required(self.region_configs, 'region_configs')
        if self.region_configs:
            self.region_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname_id is not None:
            result['edgeHostnameId'] = self.edge_hostname_id
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.comment is not None:
            result['comment'] = self.comment
        if self.dns_service_status is not None:
            result['dnsServiceStatus'] = self.dns_service_status
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.allow_china_cdn is not None:
            result['allowChinaCdn'] = self.allow_china_cdn
        if self.gdpr_compliant is not None:
            result['gdprCompliant'] = self.gdpr_compliant
        if self.geo_fence is not None:
            result['geoFence'] = self.geo_fence
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.hostnames is not None:
            result['hostnames'] = []
            for k in self.hostnames:
                result['hostnames'].append(k.to_map() if k else None)
        if self.region_configs is not None:
            result['regionConfigs'] = self.region_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnameId') is not None:
            self.edge_hostname_id = m.get('edgeHostnameId')
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('dnsServiceStatus') is not None:
            self.dns_service_status = m.get('dnsServiceStatus')
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('allowChinaCdn') is not None:
            self.allow_china_cdn = m.get('allowChinaCdn')
        if m.get('gdprCompliant') is not None:
            self.gdpr_compliant = m.get('gdprCompliant')
        if m.get('geoFence') is not None:
            self.geo_fence = m.get('geoFence')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('hostnames') is not None:
            self.hostnames = []
            for k in m.get('hostnames'):
                temp_model = QueryEdgeHostnameResponseDataHostnames()
                self.hostnames.append(temp_model.from_map(k))
        if m.get('regionConfigs') is not None:
            temp_model = QueryEdgeHostnameResponseDataRegionConfigs()
            self.region_configs = temp_model.from_map(m['regionConfigs'])
        return self


class QueryEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryEdgeHostnameResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data.", "zh_CN":"接口响应数据"}
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
            temp_model = QueryEdgeHostnameResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class QueryEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisableEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class DisableEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class DisableEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateEdgeHostnameRequestRegionConfigs(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        action_type: str = None,
        config_value: str = None,
        ip_protocol: str = None,
        ttl: str = None,
        weight: int = None,
    ):
        # {"en":"region id", "zh_CN":"区域ID"}
        self.region_id = region_id
        # {"en":"action type", "zh_CN":"调度方式。"}
        self.action_type = action_type
        # {"en":"config value", "zh_CN":"记录值。"}
        self.config_value = config_value
        # {"en":"ip protocol.", "zh_CN":"ip协议。"}
        self.ip_protocol = ip_protocol
        # {"en":"ttl", "zh_CN":"生存时间。"}
        self.ttl = ttl
        # {"en":"weight", "zh_CN":"权重。"}
        self.weight = weight

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.action_type, 'action_type')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.config_value is not None:
            result['configValue'] = self.config_value
        if self.ip_protocol is not None:
            result['ipProtocol'] = self.ip_protocol
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        if m.get('ipProtocol') is not None:
            self.ip_protocol = m.get('ipProtocol')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class UpdateEdgeHostnameRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        geo_fence: str = None,
        region_configs: List[UpdateEdgeHostnameRequestRegionConfigs] = None,
    ):
        # {"en":"Edge-Hostname comment.", "zh_CN":"调度域名描述。"}
        self.comment = comment
        # {"en":"geoFence, data range: [global,inside_china_mainland,exclude_china_mainland].", "zh_CN":"加速区域限定。取值范围：[global,inside_china_mainland,exclude_china_mainland]。"}
        self.geo_fence = geo_fence
        # {"en":"region configuration", "zh_CN":"区域配置列表 "}
        self.region_configs = region_configs

    def validate(self):
        self.validate_required(self.region_configs, 'region_configs')
        if self.region_configs:
            for k in self.region_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.geo_fence is not None:
            result['geoFence'] = self.geo_fence
        if self.region_configs is not None:
            result['regionConfigs'] = []
            for k in self.region_configs:
                result['regionConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('geoFence') is not None:
            self.geo_fence = m.get('geoFence')
        if m.get('regionConfigs') is not None:
            self.region_configs = []
            for k in m.get('regionConfigs'):
                temp_model = UpdateEdgeHostnameRequestRegionConfigs()
                self.region_configs.append(temp_model.from_map(k))
        return self


class UpdateEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class UpdateEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en":"edgeHostname", "zh_CN":"调度域名"}
        self.edge_hostname = edge_hostname

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        return self


class UpdateEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




