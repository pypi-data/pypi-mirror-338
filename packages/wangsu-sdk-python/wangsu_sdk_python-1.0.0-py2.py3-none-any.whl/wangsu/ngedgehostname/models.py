# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetAListOfEdgeHostnamesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfEdgeHostnamesParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        offset: int = None,
        limit: int = None,
        sort_by: str = None,
        sort_order: str = None,
        has_beian: bool = None,
    ):
        # {"en" : "The value is matched against the 'description' and 'edgeHostname' fields of each edge hostname.", "zh_CN": "通过搜索关键字匹配调度域名的前缀和描述进行过滤。"}
        self.search = search
        # {"en" : "Default: 0 Range: >= 0 
        # Indicates the first edge hostname to return. The first has an offset of 0.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: <= 200 
        # Maximum number of edge hostnames to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: creationTime,lastUpdateTime 
        # Default: lastUpdateTime 
        # Order the list of edge hostnames.", "zh_CN": "取值范围: creationTime,lastUpdateTime 
        # 默认值: lastUpdateTime 
        # 返回结果的排序依据。支持按创建时间或最后一次更新时间进行排序。"}
        self.sort_by = sort_by
        # {"en" : "Range: >= 0 characters 
        # Enum: asc,desc 
        # Default: desc 
        # Indicates the order of edge hostnames returned. Use 'asc' for ascending order or 'desc' for descending order.", "zh_CN": "取值范围: >= 0 字符 
        # 取值范围: asc,desc 
        # 默认值: desc 
        # 返回结果的排序顺序。'asc'表示升序，'desc'表示降序。"}
        self.sort_order = sort_order
        # {"en" : "Specify true to obtain a list of edge hostnames flagged for use with hostnames that have a Beian license, allowing them to be served by servers in mainland China. Specify false to retrieve only those edge hostnames without the Beian flag. By default, all edge hostnames are returned.", "zh_CN": "根据是否备案查询调度域名。"}
        self.has_beian = has_beian

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        return self


class GetAListOfEdgeHostnamesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfEdgeHostnamesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfEdgeHostnamesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfEdgeHostnamesResponseEdgeHostnames(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
        description: str = None,
        last_update_time: str = None,
        creation_time: str = None,
        has_beian: bool = None,
        highest_server_group: str = None,
    ):
        # {"en" : "An edge hostname.", "zh_CN": "调度域名。"}
        self.edge_hostname = edge_hostname
        # {"en" : "Description of the edge hostname.", "zh_CN": "调度域名的描述。"}
        self.description = description
        # {"en" : "RFC3339 format string indicating when the edge hostname was last updated.", "zh_CN": "RFC 3339格式的日期，表示调度域名最后一次更新的时间。"}
        self.last_update_time = last_update_time
        # {"en" : "RFC3339 format string indicating when the edge hostname was created.", "zh_CN": "RFC 3339格式的日期，表示调度域名的创建时间。"}
        self.creation_time = creation_time
        # {"en" : "true indicates that domains being accelerated have a Beian license allowing content to be served by servers in mainland China.", "zh_CN": "是否备案的标记。当值为true时，将使用包括中国大陆的服务器提供内容加速服务。"}
        self.has_beian = has_beian
        # {"en" : "Enum: standard,premium,deluxe,ultra 
        # Indicates the highest server group that can be used to serve this edge hostname. The server groups are specified when you create a client zone rule for a new edge hostname. ", "zh_CN": "取值范围: standard,premium,deluxe,ultra 
        # 指该调度域名可使用的最高等级的节点组。当您在'创建调度域名'接口中定义访客分区规则时，可指定节点组。 "}
        self.highest_server_group = highest_server_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.description is not None:
            result['description'] = self.description
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.highest_server_group is not None:
            result['highestServerGroup'] = self.highest_server_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('highestServerGroup') is not None:
            self.highest_server_group = m.get('highestServerGroup')
        return self


class GetAListOfEdgeHostnamesResponse(TeaModel):
    def __init__(
        self,
        edge_hostnames: List[GetAListOfEdgeHostnamesResponseEdgeHostnames] = None,
        count: int = None,
    ):
        # {"en" : "List of edge hostnames.", "zh_CN": "调度域名列表。"}
        self.edge_hostnames = edge_hostnames
        # {"en" : "Range: >= 0 
        # Total number of edge hostnames in the account. The actual number of edge hostnames returned in the edgehostnames field may be smaller if query parameters are specified.", "zh_CN": "取值范围: >= 0 
        # 调度域名的总数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.edge_hostnames, 'edge_hostnames')
        if self.edge_hostnames:
            for k in self.edge_hostnames:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostnames is not None:
            result['edgeHostnames'] = []
            for k in self.edge_hostnames:
                result['edgeHostnames'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnames') is not None:
            self.edge_hostnames = []
            for k in m.get('edgeHostnames'):
                temp_model = GetAListOfEdgeHostnamesResponseEdgeHostnames()
                self.edge_hostnames.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self






class GetClientRegionsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetClientRegionsParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        sort_order: str = None,
        isp_code: str = None,
    ):
        # {"en" : "Return regions whose code or name contains the specified value.
        # ", "zh_CN": "通过搜索关键字匹配访客区域的代码或名称进行过滤。"}
        self.search = search
        # {"en" : "Enum: asc,desc 
        # Default: asc 
        # Order of client regions returned. Use 'asc' for ascending order or 'desc' for descending order.", "zh_CN": "取值范围: asc,desc 
        # 默认值: asc 
        # 返回结果的排序顺序。使用'asc'表示升序，'desc'表示降序。"}
        self.sort_order = sort_order
        # {"en" : "Limit the returned regions to those where an ISP operates. The value should be one of the ISP codes returned by the ISPs API.", "zh_CN": "仅返回某个运营商有提供服务的访客区域。运营商是指'查询支持的ISP运营商列表'接口所支持的运营商。"}
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.isp_code is not None:
            result['ispCode'] = self.isp_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('ispCode') is not None:
            self.isp_code = m.get('ispCode')
        return self


class GetClientRegionsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetClientRegionsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetClientRegionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetClientRegionsResponseData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # {"en" : "Regions code.", "zh_CN": "访客区域的代码。"}
        self.code = code
        # {"en" : "Regions name.", "zh_CN": "访客区域的名称。"}
        self.name = name

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetClientRegionsResponse(TeaModel):
    def __init__(
        self,
        data: List[GetClientRegionsResponseData] = None,
    ):
        # {"en" : "Regions list.", "zh_CN": "访客区域的代码和名称的集合。"}
        self.data = data

    def validate(self):
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
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetClientRegionsResponseData()
                self.data.append(temp_model.from_map(k))
        return self






class GetAListOfIspsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfIspsParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        sort_order: str = None,
        region_code: str = None,
    ):
        # {"en" : "Return ISPs whose code or name contains this value.", "zh_CN": "通过搜索关键字匹配运营商的代码或名称进行过滤。"}
        self.search = search
        # {"en" : "Enum: asc,desc 
        # Default: asc 
        # Order of ISPs returned. Use 'asc' for ascending order or 'desc' for descending order.", "zh_CN": "取值范围: asc,desc 
        # 默认值: asc 
        # 返回结果的排序顺序。使用'asc'表示升序，'desc'表示降序。"}
        self.sort_order = sort_order
        # {"en" : "Limit returned ISPs to those operating in a particular region. The value of regionCode should be one of the codes representing a region returned by the client regions API.", "zh_CN": "仅返回在某个访客区域有提供服务的运营商。访客区域是指'查询支持的区域列表'接口中支持的访客区域。"}
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.region_code is not None:
            result['regionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('regionCode') is not None:
            self.region_code = m.get('regionCode')
        return self


class GetAListOfIspsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfIspsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfIspsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfIspsResponseData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # {"en" : "ISPs code.", "zh_CN": "运营商的代码。"}
        self.code = code
        # {"en" : "ISPs name.", "zh_CN": "运营商的名称。"}
        self.name = name

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetAListOfIspsResponse(TeaModel):
    def __init__(
        self,
        data: List[GetAListOfIspsResponseData] = None,
    ):
        # {"en" : "ISPs list.", "zh_CN": "运营商的代码和名称的集合。"}
        self.data = data

    def validate(self):
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
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetAListOfIspsResponseData()
                self.data.append(temp_model.from_map(k))
        return self






class UpdateAnEdgeHostnamePartPaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en" : "an edge hostname", "zh_CN": "调度域名。"}
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


class UpdateAnEdgeHostnamePartParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnamePartRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnamePartRequestClientZonesAction(TeaModel):
    def __init__(
        self,
        type: str = None,
        by: List[str] = None,
        to: List[str] = None,
        enable_ipv_6: bool = None,
    ):
        # {"en" : "Enum: deliver,redirect,reject 
        # Defines the action to take for requests to the zone. Options are to deliver using one or more server groups, to reject the request altogether, or to redirect to another domain. If 'reject' is specified, the client request will be redirected to a server that always responds with HTTP response code 403 representing 'Forbidden'. Up to one 'reject' action is allowed for each client zone.
        # ", "zh_CN": "取值范围: deliver,redirect,reject 
        # 当规则匹配时，对客户端请求执行的动作的类型。包括分发，拒绝和跳转3个类型。如果指定了'拒绝'，则客户端请求将被调度到一台服务器，该服务器总是响应403状态码，表示'Forbidden'拒绝访问。每个访客分区最多只允许一个'拒绝'动作。"}
        self.type = type
        # {"en" : "This field is used if the action is of type 'deliver'. Specify one or more of the server groups (standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) to control the servers used to deliver content. If unspecified, 'standard' is used. <br/><br/>'nearChina' is a special server group that can be enabled for you if your domains lack ICP Beian, but you want optimal performance serving Chinese visitors. A client zone rule using nearChina cannot be configured to simultaneously deliver to other server groups, though you may create separate client zone rules to use other server groups.<br/><br/>If you have an ICP Beian license and want your content to be delivered by servers within China, you can opt to use 'ChinaStandard' and 'ChinaPremium.' Please contact our support team if you require nearChina, ChinaStandard, or ChinaPremium.<br/><br/>If an edge hostname is not initially configured to use ChinaStandard or ChinaPremium, you will not be able to modify it later to use these two server groups. Instead, you will need to create a new edge hostname with client zone rules delivering to those server groups.", "zh_CN": "如果动作类型为'分发'，则使用此字段指定一个或多个节点组(standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) 来选择提供内容分发服务的缓存节点。如果未指定，则使用'standard'。<br/><br/>'nearChina'  是一个特殊的节点组。如果您需要使用nearChina节点组，请联系我们的技术支持开通。不能在同一条规则中同时指定nearChina节点组和其他节点组。如果要使用其他节点组，需要创建单独的访客分区规则。<br/><br/>如果您的加速域名有ICP备案，希望由中国大陆的服务器提供内容分发服务，您可以选择使用'ChinaStandard'和'ChinaPremium'节点组。
        # <br/><br/>如果调度域名创建时没有指定使用ChinaStandard或ChinaPremium节点组，则无法通过更新调度域名来使用这两个节点组。您需要创建一个新的调度域名，在新的调度域名中指定使用ChinaStandard或ChinaPremium，才能使用这2个节点组。"}
        self.by = by
        # {"en" : "This field is used if the action is of type 'redirect'. It indicates the hostname or IP address to redirect to. This is typically an origin server or another CDN provider.", "zh_CN": "如果动作类型为'跳转'，则通过该字段指定跳转的目标域名或IP地址。'跳转'目标通常是源站服务器或其它CDN厂商。"}
        self.to = to
        # {"en" : "Default: True 
        # Indicates whether an IPv6 address can be used. This value is used only if the client zone rule's action type is 'deliver'.", "zh_CN": "默认值: True 
        # 指定是否允许使用IPv6地址进行内容分发。仅当动作类型为'分发'时该值才有效。"}
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.by is not None:
            result['by'] = self.by
        if self.to is not None:
            result['to'] = self.to
        if self.enable_ipv_6 is not None:
            result['enableIPv6'] = self.enable_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('by') is not None:
            self.by = m.get('by')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('enableIPv6') is not None:
            self.enable_ipv_6 = m.get('enableIPv6')
        return self


class UpdateAnEdgeHostnamePartRequestClientZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        weight: int = None,
        action: UpdateAnEdgeHostnamePartRequestClientZonesAction = None,
        isp: str = None,
    ):
        # {"en" : "This field indicates the region in which the rule applies. Refer to our API to get client regions to get valid region codes. For example, if you wish to create a rule that covers all of Europe, simply specify 'eu' as the region. You can indicate specific countries. For example, 'na.us' represents the 'United States of America', and 'eu.fr' represents 'France'.  
        # 
        # A special client region 'all' can be used to specify that the rule applies to the entire world. If overlapping regions are specified, the more specific one takes precedence. For example, if you specify 'as' in one rule and 'as.cn' in another, a request from China will follow the rule for 'as.cn'.", "zh_CN": "该规则适用的区域。可调用'查询支持的区域列表'接口来查看区域信息。例如，如果您希望创建规则覆盖整个欧洲，则指定'eu'为区域。 您可以指定具体的国家。例如，'na.us'代表'美国'，而'eu.fr'代表'法国'。
        # 
        # 'all'是一个特殊的区域，可用于指定适用于全球的规则。如果不同规则指定的区域存在重叠，则以更细粒度的区域优先。例如，如果您在一条规则中指定'as'，在另一条规则中指定'as.cn'，则来自中国的请求将优先匹配'as.cn'的规则。"}
        self.region = region
        # {"en" : "Default: 100 Range: [ 0 .. 100 ] 
        # When multiple actions are specified for a client zone, the weight is used to adjust the probability of a client zone rule applying to a client request.
        # Consider two rules that apply to 'as.cn': {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        #  The probability of 'deliver' will be 100/(100+10) or 0.909 while the probability of 'redirect' will be 10/(100+10) or 0.091.
        #  
        # ", "zh_CN": "默认值: 100 取值范围: [ 0 .. 100 ] 
        # 可以为同个访客分区指定多条规则。通过在规则中指定weight字段，可控制规则匹配的权重。
        # 以'as.cn'区域的2条规则为例: {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        # 按照以上规则，客户端请求匹配规则1进行'分发'的比例为100/(100+10)，即0.909，匹配规则2进行'跳转'的比例为10/(100+10)，即0.091。
        #  
        # "}
        self.weight = weight
        # {"en" : "This object describes the action to take for requests matching the rule.", "zh_CN": "当规则匹配时执行的动作。"}
        self.action = action
        # {"en" : "Specify the code representing an ISP (Internet Service Provider) if the rule only applies to requests from a particular ISP. Call our API to get a list of supported ISPs. Specify 'all' to indicate all ISPs rather than a particular one. Specify a comma-separated list of up to 10 ISP codes if you want your rule to apply to more than one ISP.", "zh_CN": "该规则适用的运营商。可调用我们的'查询支持的ISP运营商列表'接口查看运营商信息。指定'all'表示所有运营商。如果希望该规则应用于多个运营商，则可指定多个运营商，用逗号分隔，但最多只能包含10个运营商。"}
        self.isp = isp

    def validate(self):
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.weight is not None:
            result['weight'] = self.weight
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('action') is not None:
            temp_model = UpdateAnEdgeHostnamePartRequestClientZonesAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class UpdateAnEdgeHostnamePartRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        pci_required: bool = None,
        grpr_compliant: bool = None,
        client_zones: List[UpdateAnEdgeHostnamePartRequestClientZones] = None,
        estimated_bandwidth: str = None,
    ):
        # {"en" : "A description of the edge hostname.", "zh_CN": "调度域名的描述。"}
        self.description = description
        # {"en" : "Whether PCI compliance is required.  true means content will only be served by PCI certified PoPs.", "zh_CN": "表示流量调度是否需要遵循PCI规范。当值为true时，表示只能使用已通过PCI认证的节点提供内容分发服务。"}
        self.pci_required = pci_required
        # {"en" : "If set to 'true', clients from European Economic Area (EEA) countries will only be served by IP addresses in EEA countries.", "zh_CN": "表示流量调度是否需要遵循GDPR的规定。当值为'true'时，对于来自欧洲经济区(EEA)国家的请求，将仅使用归属EEA国家的IP地址提供服务。"}
        self.grpr_compliant = grpr_compliant
        # {"en" : "Specify rules to control how requests from client zones are handled. There must be a rule that covers all regions and all ISPs.", "zh_CN": "自定义规则来控制如何处理不同访客分区的请求。您必须至少创建一条覆盖所有区域和所有运营商的规则。"}
        self.client_zones = client_zones
        # {"en" : "An estimate of the bandwidth required to serve content using this edge hostname. Units of measurement should be in Tbps, Gbps, Mbps, or kbps. Example: 100Gbps", "zh_CN": "通过该调度域名进行CDN加速预计需要的带宽。单位应为Tbps、Gbps、Mbps或kbps。示例：100 Gbps。"}
        self.estimated_bandwidth = estimated_bandwidth

    def validate(self):
        if self.client_zones:
            for k in self.client_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.pci_required is not None:
            result['pciRequired'] = self.pci_required
        if self.grpr_compliant is not None:
            result['grprCompliant'] = self.grpr_compliant
        if self.client_zones is not None:
            result['clientZones'] = []
            for k in self.client_zones:
                result['clientZones'].append(k.to_map() if k else None)
        if self.estimated_bandwidth is not None:
            result['estimatedBandwidth'] = self.estimated_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('pciRequired') is not None:
            self.pci_required = m.get('pciRequired')
        if m.get('grprCompliant') is not None:
            self.grpr_compliant = m.get('grprCompliant')
        if m.get('clientZones') is not None:
            self.client_zones = []
            for k in m.get('clientZones'):
                temp_model = UpdateAnEdgeHostnamePartRequestClientZones()
                self.client_zones.append(temp_model.from_map(k))
        if m.get('estimatedBandwidth') is not None:
            self.estimated_bandwidth = m.get('estimatedBandwidth')
        return self


class UpdateAnEdgeHostnamePartResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnamePartResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateAnEdgeHostnameAllPaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en" : "an edge hostname", "zh_CN": "调度域名。"}
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


class UpdateAnEdgeHostnameAllParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnameAllRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnameAllRequestClientZonesAction(TeaModel):
    def __init__(
        self,
        type: str = None,
        by: List[str] = None,
        to: List[str] = None,
        enable_ipv_6: bool = None,
    ):
        # {"en" : "Enum: deliver,redirect,reject 
        # Defines the action to take for requests to the zone. Options are to deliver using one or more server groups, to reject the request altogether, or to redirect to another domain. If 'reject' is specified, the client request will be redirected to a server that always responds with HTTP response code 403 representing 'Forbidden'. Up to one 'reject' action is allowed for each client zone.
        # ", "zh_CN": "取值范围: deliver,redirect,reject 
        # 当规则匹配时，对客户端请求执行的动作的类型。包括分发，拒绝和跳转3个类型。如果指定了'拒绝'，则客户端请求将被调度到一台服务器，该服务器总是响应403状态码，表示'Forbidden'拒绝访问。每个访客分区最多只允许一个'拒绝'动作。"}
        self.type = type
        # {"en" : "This field is used if the action is of type 'deliver'. Specify one or more of the server groups (standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) to control the servers used to deliver content. If unspecified, 'standard' is used. <br/><br/>'nearChina' is a special server group that can be enabled for you if your domains lack ICP Beian, but you want optimal performance serving Chinese visitors. A client zone rule using nearChina cannot be configured to simultaneously deliver to other server groups, though you may create separate client zone rules to use other server groups.<br/><br/>If you have an ICP Beian license and want your content to be delivered by servers within China, you can opt to use 'ChinaStandard' and 'ChinaPremium.' Please contact our support team if you require nearChina, ChinaStandard, or ChinaPremium.<br/><br/>If an edge hostname is not initially configured to use ChinaStandard or ChinaPremium, you will not be able to modify it later to use these two server groups. Instead, you will need to create a new edge hostname with client zone rules delivering to those server groups.", "zh_CN": "如果动作类型为'分发'，则使用此字段指定一个或多个节点组(standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) 来选择提供内容分发服务的缓存节点。如果未指定，则使用'standard'。<br/><br/>'nearChina'  是一个特殊的节点组。如果您需要使用nearChina节点组，请联系我们的技术支持开通。不能在同一条规则中同时指定nearChina节点组和其他节点组。如果要使用其他节点组，需要创建单独的访客分区规则。<br/><br/>如果您的加速域名有ICP备案，希望由中国大陆的服务器提供内容分发服务，您可以选择使用'ChinaStandard'和'ChinaPremium'节点组。
        # <br/><br/>如果调度域名创建时没有指定使用ChinaStandard或ChinaPremium节点组，则无法通过更新调度域名来使用这两个节点组。您需要创建一个新的调度域名，在新的调度域名中指定使用ChinaStandard或ChinaPremium，才能使用这2个节点组。"}
        self.by = by
        # {"en" : "This field is used if the action is of type 'redirect'. It indicates the hostname or IP address to redirect to. This is typically an origin server or another CDN provider.", "zh_CN": "如果动作类型为'跳转'，则通过该字段指定跳转的目标域名或IP地址。'跳转'目标通常是源站服务器或其它CDN厂商。"}
        self.to = to
        # {"en" : "Default: True 
        # Indicates whether an IPv6 address can be used. This value is used only if the client zone rule's action type is 'deliver'.", "zh_CN": "默认值: True 
        # 指定是否允许使用IPv6地址进行内容分发。仅当动作类型为'分发'时该值才有效。"}
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.by is not None:
            result['by'] = self.by
        if self.to is not None:
            result['to'] = self.to
        if self.enable_ipv_6 is not None:
            result['enableIPv6'] = self.enable_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('by') is not None:
            self.by = m.get('by')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('enableIPv6') is not None:
            self.enable_ipv_6 = m.get('enableIPv6')
        return self


class UpdateAnEdgeHostnameAllRequestClientZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        weight: int = None,
        action: UpdateAnEdgeHostnameAllRequestClientZonesAction = None,
        isp: str = None,
    ):
        # {"en" : "This field indicates the region in which the rule applies. Refer to our API to get client regions to get valid region codes. For example, if you wish to create a rule that covers all of Europe, simply specify 'eu' as the region. You can indicate specific countries. For example, 'na.us' represents the 'United States of America', and 'eu.fr' represents 'France'.  
        # 
        # A special client region 'all' can be used to specify that the rule applies to the entire world. If overlapping regions are specified, the more specific one takes precedence. For example, if you specify 'as' in one rule and 'as.cn' in another, a request from China will follow the rule for 'as.cn'.", "zh_CN": "该规则适用的区域。可调用'查询支持的区域列表'接口来查看区域信息。例如，如果您希望创建规则覆盖整个欧洲，则指定'eu'为区域。 您可以指定具体的国家。例如，'na.us'代表'美国'，而'eu.fr'代表'法国'。
        # 
        # 'all'是一个特殊的区域，可用于指定适用于全球的规则。如果不同规则指定的区域存在重叠，则以更细粒度的区域优先。例如，如果您在一条规则中指定'as'，在另一条规则中指定'as.cn'，则来自中国的请求将优先匹配'as.cn'的规则。"}
        self.region = region
        # {"en" : "Default: 100 Range: [ 0 .. 100 ] 
        # When multiple actions are specified for a client zone, the weight is used to adjust the probability of a client zone rule applying to a client request.
        # Consider two rules that apply to 'as.cn': {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        #  The probability of 'deliver' will be 100/(100+10) or 0.909 while the probability of 'redirect' will be 10/(100+10) or 0.091.
        #  
        # ", "zh_CN": "默认值: 100 取值范围: [ 0 .. 100 ] 
        # 可以为同个访客分区指定多条规则。通过在规则中指定weight字段，可控制规则匹配的权重。
        # 以'as.cn'区域的2条规则为例: {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        # 按照以上规则，客户端请求匹配规则1进行'分发'的比例为100/(100+10)，即0.909，匹配规则2进行'跳转'的比例为10/(100+10)，即0.091。
        #  
        # "}
        self.weight = weight
        # {"en" : "This object describes the action to take for requests matching the rule.", "zh_CN": "当规则匹配时执行的动作。"}
        self.action = action
        # {"en" : "Specify the code representing an ISP (Internet Service Provider) if the rule only applies to requests from a particular ISP. Call our API to get a list of supported ISPs. Specify 'all' to indicate all ISPs rather than a particular one. Specify a comma-separated list of up to 10 ISP codes if you want your rule to apply to more than one ISP.", "zh_CN": "该规则适用的运营商。可调用我们的'查询支持的ISP运营商列表'接口查看运营商信息。指定'all'表示所有运营商。如果希望该规则应用于多个运营商，则可指定多个运营商，用逗号分隔，但最多只能包含10个运营商。"}
        self.isp = isp

    def validate(self):
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.weight is not None:
            result['weight'] = self.weight
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('action') is not None:
            temp_model = UpdateAnEdgeHostnameAllRequestClientZonesAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class UpdateAnEdgeHostnameAllRequest(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
        description: str = None,
        pci_required: bool = None,
        gdpr_compliant: bool = None,
        client_zones: List[UpdateAnEdgeHostnameAllRequestClientZones] = None,
        estimated_bandwidth: str = None,
    ):
        # {"en" : "The edge hostname. It cannot be modified.", "zh_CN": "调度域名。该字段不可修改。"}
        self.edge_hostname = edge_hostname
        # {"en" : "A description of the edge hostname.", "zh_CN": "调度域名的描述。"}
        self.description = description
        # {"en" : "Whether PCI compliance is required.  true means content will only be served by PCI certified PoPs.", "zh_CN": "表示流量调度是否需要遵循PCI规范。当值为true时，表示只能使用已通过PCI认证的节点提供内容分发服务。"}
        self.pci_required = pci_required
        # {"en" : "If set to 'true', clients from European Economic Area (EEA) countries will only be served by IP addresses in EEA countries.", "zh_CN": "表示流量调度是否需要遵循GDPR的规定。当值为'true'时，对于来自欧洲经济区(EEA)国家的请求，将仅使用归属EEA国家的IP地址提供服务。"}
        self.gdpr_compliant = gdpr_compliant
        # {"en" : "Specify rules to control how requests from client zones are handled. There must be a rule that covers all regions and all ISPs.", "zh_CN": "自定义规则来控制如何处理不同访客分区的请求。您必须至少创建一条覆盖所有区域和所有运营商的规则。"}
        self.client_zones = client_zones
        # {"en" : "An estimate of the bandwidth required to serve content using this edge hostname. Units of measurement should be in Tbps, Gbps, Mbps, or kbps. Example: 100Gbps", "zh_CN": "通过该调度域名进行CDN加速预计需要的带宽。单位应为Tbps、Gbps、Mbps或kbps。示例：100 Gbps。"}
        self.estimated_bandwidth = estimated_bandwidth

    def validate(self):
        self.validate_required(self.edge_hostname, 'edge_hostname')
        if self.client_zones:
            for k in self.client_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.description is not None:
            result['description'] = self.description
        if self.pci_required is not None:
            result['pciRequired'] = self.pci_required
        if self.gdpr_compliant is not None:
            result['gdprCompliant'] = self.gdpr_compliant
        if self.client_zones is not None:
            result['clientZones'] = []
            for k in self.client_zones:
                result['clientZones'].append(k.to_map() if k else None)
        if self.estimated_bandwidth is not None:
            result['estimatedBandwidth'] = self.estimated_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('pciRequired') is not None:
            self.pci_required = m.get('pciRequired')
        if m.get('gdprCompliant') is not None:
            self.gdpr_compliant = m.get('gdprCompliant')
        if m.get('clientZones') is not None:
            self.client_zones = []
            for k in m.get('clientZones'):
                temp_model = UpdateAnEdgeHostnameAllRequestClientZones()
                self.client_zones.append(temp_model.from_map(k))
        if m.get('estimatedBandwidth') is not None:
            self.estimated_bandwidth = m.get('estimatedBandwidth')
        return self


class UpdateAnEdgeHostnameAllResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAnEdgeHostnameAllResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteAnEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en" : "an edge hostname", "zh_CN": "调度域名。"}
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


class DeleteAnEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAnEdgeHostnameRequestHeader(TeaModel):
    def __init__(
        self,
        check_usage: str = None,
    ):
        # {"en":"When you request to delete an edgeHostname, we check if the edgeHostname is still active. Deletion of the edgeHostname will be rejected if there are DNS requests to the edgeHostname in the past 24 hours. This is to prevent accidental deletion. If you are sure that the edgeHostname can be deleted, you can bypass this check by passing the <i>Check-Usage: no</i> header.", "zh_CN":"当您删除调度域名时，后台会校验调度域名是否处于活跃状态。如果调度域名在过去24小时有DNS解析请求，则会拒绝删除调度域名，避免误操作。如果您确定要删除调度域名，可以在调用接口时传入请求头<i>Check-Usage: no</i>来跳过校验。"}
        self.check_usage = check_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_usage is not None:
            result['Check-Usage'] = self.check_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check-Usage') is not None:
            self.check_usage = m.get('Check-Usage')
        return self


class DeleteAnEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAnEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAnEdgeHostnameResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateAnEdgeHostnamePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAnEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAnEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAnEdgeHostnameRequestClientZonesAction(TeaModel):
    def __init__(
        self,
        type: str = None,
        by: List[str] = None,
        to: List[str] = None,
        enable_ipv_6: bool = None,
    ):
        # {"en" : "Enum: deliver,redirect,reject 
        # Defines the action to take for requests to the zone. Options are to deliver using one or more server groups, to reject the request altogether, or to redirect to another domain. If 'reject' is specified, the client request will be redirected to a server that always responds with HTTP response code 403 representing 'Forbidden'. Up to one 'reject' action is allowed for each client zone.
        # ", "zh_CN": "取值范围: deliver,redirect,reject 
        # 当规则匹配时，对客户端请求执行的动作的类型。包括分发，拒绝和跳转3个类型。如果指定了'拒绝'，则客户端请求将被调度到一台服务器，该服务器总是响应403状态码，表示'Forbidden'拒绝访问。每个访客分区最多只允许一个'拒绝'动作。"}
        self.type = type
        # {"en" : "This field is used if the action is of type 'deliver'. Specify one or more of the server groups (standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) to control the servers used to deliver content. If unspecified, 'standard' is used. <br/><br/>'nearChina' is a special server group that can be enabled for you if your domains lack ICP Beian, but you want optimal performance serving Chinese visitors. A client zone rule using nearChina cannot be configured to simultaneously deliver to other server groups, though you may create separate client zone rules to use other server groups.<br/><br/>If you have an ICP Beian license and want your content to be delivered by servers within China, you can opt to use 'ChinaStandard' and 'ChinaPremium.' Please contact our support team if you require nearChina, ChinaStandard, or ChinaPremium.<br/><br/>If an edge hostname is not initially configured to use ChinaStandard or ChinaPremium, you will not be able to modify it later to use these two server groups. Instead, you will need to create a new edge hostname with client zone rules delivering to those server groups.", "zh_CN": "如果动作类型为'分发'，则使用此字段指定一个或多个节点组(standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) 来选择提供内容分发服务的缓存节点。如果未指定，则使用'standard'。<br/><br/>'nearChina'  是一个特殊的节点组。如果您需要使用nearChina节点组，请联系我们的技术支持开通。不能在同一条规则中同时指定nearChina节点组和其他节点组。如果要使用其他节点组，需要创建单独的访客分区规则。<br/><br/>如果您的加速域名有ICP备案，希望由中国大陆的服务器提供内容分发服务，您可以选择使用'ChinaStandard'和'ChinaPremium'节点组。
        # <br/><br/>如果调度域名创建时没有指定使用ChinaStandard或ChinaPremium节点组，则无法通过更新调度域名来使用这两个节点组。您需要创建一个新的调度域名，在新的调度域名中指定使用ChinaStandard或ChinaPremium，才能使用这2个节点组。"}
        self.by = by
        # {"en" : "This field is used if the action is of type 'redirect'. It indicates the hostname or IP address to redirect to. This is typically an origin server or another CDN provider.", "zh_CN": "如果动作类型为'跳转'，则通过该字段指定跳转的目标域名或IP地址。'跳转'目标通常是源站服务器或其它CDN厂商。"}
        self.to = to
        # {"en" : "Default: True 
        # Indicates whether an IPv6 address can be used. This value is used only if the client zone rule's action type is 'deliver'.", "zh_CN": "默认值: True 
        # 指定是否允许使用IPv6地址进行内容分发。仅当动作类型为'分发'时该值才有效。"}
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.by is not None:
            result['by'] = self.by
        if self.to is not None:
            result['to'] = self.to
        if self.enable_ipv_6 is not None:
            result['enableIPv6'] = self.enable_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('by') is not None:
            self.by = m.get('by')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('enableIPv6') is not None:
            self.enable_ipv_6 = m.get('enableIPv6')
        return self


class CreateAnEdgeHostnameRequestClientZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        weight: int = None,
        action: CreateAnEdgeHostnameRequestClientZonesAction = None,
        isp: str = None,
    ):
        # {"en" : "This field indicates the region in which the rule applies. Refer to our API to get client regions to get valid region codes. For example, if you wish to create a rule that covers all of Europe, simply specify 'eu' as the region. You can indicate specific countries. For example, 'na.us' represents the 'United States of America', and 'eu.fr' represents 'France'.  
        # 
        # A special client region 'all' can be used to specify that the rule applies to the entire world. If overlapping regions are specified, the more specific one takes precedence. For example, if you specify 'as' in one rule and 'as.cn' in another, a request from China will follow the rule for 'as.cn'.", "zh_CN": "该规则适用的区域。可调用'查询支持的区域列表'接口来查看区域信息。例如，如果您希望创建规则覆盖整个欧洲，则指定'eu'为区域。 您可以指定具体的国家。例如，'na.us'代表'美国'，而'eu.fr'代表'法国'。
        # 
        # 'all'是一个特殊的区域，可用于指定适用于全球的规则。如果不同规则指定的区域存在重叠，则以更细粒度的区域优先。例如，如果您在一条规则中指定'as'，在另一条规则中指定'as.cn'，则来自中国的请求将优先匹配'as.cn'的规则。"}
        self.region = region
        # {"en" : "Default: 100 Range: [ 0 .. 100 ] 
        # When multiple actions are specified for a client zone, the weight is used to adjust the probability of a client zone rule applying to a client request.
        # Consider two rules that apply to 'as.cn': {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        #  The probability of 'deliver' will be 100/(100+10) or 0.909 while the probability of 'redirect' will be 10/(100+10) or 0.091.
        #  
        # ", "zh_CN": "默认值: 100 取值范围: [ 0 .. 100 ] 
        # 可以为同个访客分区指定多条规则。通过在规则中指定weight字段，可控制规则匹配的权重。
        # 以'as.cn'区域的2条规则为例: {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        # 按照以上规则，客户端请求匹配规则1进行'分发'的比例为100/(100+10)，即0.909，匹配规则2进行'跳转'的比例为10/(100+10)，即0.091。
        #  
        # "}
        self.weight = weight
        # {"en" : "This object describes the action to take for requests matching the rule.", "zh_CN": "当规则匹配时执行的动作。"}
        self.action = action
        # {"en" : "Specify the code representing an ISP (Internet Service Provider) if the rule only applies to requests from a particular ISP. Call our API to get a list of supported ISPs. Specify 'all' to indicate all ISPs rather than a particular one. Specify a comma-separated list of up to 10 ISP codes if you want your rule to apply to more than one ISP.", "zh_CN": "该规则适用的运营商。可调用我们的'查询支持的ISP运营商列表'接口查看运营商信息。指定'all'表示所有运营商。如果希望该规则应用于多个运营商，则可指定多个运营商，用逗号分隔，但最多只能包含10个运营商。"}
        self.isp = isp

    def validate(self):
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.weight is not None:
            result['weight'] = self.weight
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('action') is not None:
            temp_model = CreateAnEdgeHostnameRequestClientZonesAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class CreateAnEdgeHostnameRequest(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
        description: str = None,
        pci_required: bool = None,
        gdpr_compliant: bool = None,
        client_zones: List[CreateAnEdgeHostnameRequestClientZones] = None,
        estimated_bandwidth: str = None,
    ):
        # {"en" : "A hostname to use in your DNS server settings. When your property has been deployed to production, you should modify your DNS server so that the CNAME records of the property's hostnames refer to this value. The edge hostname should consist of at least ten characters followed by a permitted suffix such as '.qtlcdn.com' (for example, abcdefg123.qtlcdn.com). Your service quota may include an edgeHostnameZones field. If it does, the suffix used for your edge hostname should be one of the listed values. ", "zh_CN": "当您部署加速项目到生产环境后，您应该修改DNS解析，添加一条CNAME记录，将您的加速域名指向该调度域名。每个调度域名由2部组成，即前缀和后缀（例如， abcdefg123.qtlcdn.com）。前缀可自定义，后缀为既定的DNS zone，如'.qtlcdn.com'。如果您需要使用自定义的DNS zone，请联系我们的技术支持。"}
        self.edge_hostname = edge_hostname
        # {"en" : "A description of the edge hostname.", "zh_CN": "调度域名的描述。"}
        self.description = description
        # {"en" : "Default: False 
        # Indicates whether PCI compliance is required.  true means content will only be served by PCI certified PoPs.", "zh_CN": "默认值: False 
        # 表示流量调度是否需要遵循PCI规范。当值为true时，表示只能使用已通过PCI认证的节点提供内容分发服务。"}
        self.pci_required = pci_required
        # {"en" : "Default: False 
        # If set to 'true', clients from European Economic Area (EEA) countries will only be served by IP addresses in EEA countries.", "zh_CN": "默认值: False 
        # 表示流量调度是否需要遵循GDPR的规定。当值为'true'时，对于来自欧洲经济区(EEA)国家的请求，将仅使用归属EEA国家的IP地址提供服务。"}
        self.gdpr_compliant = gdpr_compliant
        # {"en" : "Specify rules to control how requests from client zones are handled. There must be a rule that covers all regions and all ISPs.", "zh_CN": "自定义规则来控制如何处理不同访客分区的请求。您必须至少创建一条覆盖所有区域和所有运营商的规则。"}
        self.client_zones = client_zones
        # {"en" : "An estimate of the bandwidth required to serve content using this edge hostname. Units of measurement should be in Tbps, Gbps, Mbps, or kbps. Example: 100Gbps", "zh_CN": "通过该调度域名进行CDN加速预计需要的带宽。单位应为Tbps、Gbps、Mbps或kbps。示例：100 Gbps。"}
        self.estimated_bandwidth = estimated_bandwidth

    def validate(self):
        if self.client_zones:
            for k in self.client_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.description is not None:
            result['description'] = self.description
        if self.pci_required is not None:
            result['pciRequired'] = self.pci_required
        if self.gdpr_compliant is not None:
            result['gdprCompliant'] = self.gdpr_compliant
        if self.client_zones is not None:
            result['clientZones'] = []
            for k in self.client_zones:
                result['clientZones'].append(k.to_map() if k else None)
        if self.estimated_bandwidth is not None:
            result['estimatedBandwidth'] = self.estimated_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('pciRequired') is not None:
            self.pci_required = m.get('pciRequired')
        if m.get('gdprCompliant') is not None:
            self.gdpr_compliant = m.get('gdprCompliant')
        if m.get('clientZones') is not None:
            self.client_zones = []
            for k in m.get('clientZones'):
                temp_model = CreateAnEdgeHostnameRequestClientZones()
                self.client_zones.append(temp_model.from_map(k))
        if m.get('estimatedBandwidth') is not None:
            self.estimated_bandwidth = m.get('estimatedBandwidth')
        return self


class CreateAnEdgeHostnameResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAnEdgeHostnameResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The value is a URL to the new edge hostname.", "zh_CN":"通过Location响应头返回新建的调度域名的URL。可使用该URL调用'查询调度域名详情'接口来查看调度域名的详细信息。URL示例：<code>Location: http://open.chinanetcenter.com/cdn/edgeHostnames/abcde12345.qtlcdn.com"}
        self.location = location

    def validate(self):
        self.validate_required(self.location, 'location')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self






class GetAnEdgeHostnamePaths(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
    ):
        # {"en" : "an edge hostname", "zh_CN": "调度域名。"}
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


class GetAnEdgeHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAnEdgeHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAnEdgeHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAnEdgeHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAnEdgeHostnameResponseHistoryConfigurationClientZonesAction(TeaModel):
    def __init__(
        self,
        type: str = None,
        by: List[str] = None,
        to: List[str] = None,
        enable_ipv_6: bool = None,
    ):
        # {"en" : "Enum: deliver,redirect,reject 
        # Defines the action to take for requests to the zone. Options are to deliver using one or more server groups, to reject the request altogether, or to redirect to another domain. If 'reject' is specified, the client request will be redirected to a server that always responds with HTTP response code 403 representing 'Forbidden'. Up to one 'reject' action is allowed for each client zone.
        # ", "zh_CN": "取值范围: deliver,redirect,reject 
        # 当规则匹配时，对客户端请求执行的动作的类型。包括分发，拒绝和跳转3个类型。如果指定了'拒绝'，则客户端请求将被调度到一台服务器，该服务器总是响应403状态码，表示'Forbidden'拒绝访问。每个访客分区最多只允许一个'拒绝'动作。"}
        self.type = type
        # {"en" : "This field is used if the action is of type 'deliver'. Specify one or more of the server groups (standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) to control the servers used to deliver content. If unspecified, 'standard' is used. <br/><br/>'nearChina' is a special server group that can be enabled for you if your domains lack ICP Beian, but you want optimal performance serving Chinese visitors. A client zone rule using nearChina cannot be configured to simultaneously deliver to other server groups, though you may create separate client zone rules to use other server groups.<br/><br/>If you have an ICP Beian license and want your content to be delivered by servers within China, you can opt to use 'ChinaStandard' and 'ChinaPremium.' Please contact our support team if you require nearChina, ChinaStandard, or ChinaPremium.<br/><br/>If an edge hostname is not initially configured to use ChinaStandard or ChinaPremium, you will not be able to modify it later to use these two server groups. Instead, you will need to create a new edge hostname with client zone rules delivering to those server groups.", "zh_CN": "如果动作类型为'分发'，则使用此字段指定一个或多个节点组(standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) 来选择提供内容分发服务的缓存节点。如果未指定，则使用'standard'。<br/><br/>'nearChina'  是一个特殊的节点组。如果您需要使用nearChina节点组，请联系我们的技术支持开通。不能在同一条规则中同时指定nearChina节点组和其他节点组。如果要使用其他节点组，需要创建单独的访客分区规则。<br/><br/>如果您的加速域名有ICP备案，希望由中国大陆的服务器提供内容分发服务，您可以选择使用'ChinaStandard'和'ChinaPremium'节点组。
        # <br/><br/>如果调度域名创建时没有指定使用ChinaStandard或ChinaPremium节点组，则无法通过更新调度域名来使用这两个节点组。您需要创建一个新的调度域名，在新的调度域名中指定使用ChinaStandard或ChinaPremium，才能使用这2个节点组。"}
        self.by = by
        # {"en" : "This field is used if the action is of type 'redirect'. It indicates the hostname or IP address to redirect to. This is typically an origin server or another CDN provider.", "zh_CN": "如果动作类型为'跳转'，则通过该字段指定跳转的目标域名或IP地址。'跳转'目标通常是源站服务器或其它CDN厂商。"}
        self.to = to
        # {"en" : "Default: True 
        # Indicates whether an IPv6 address can be used. This value is used only if the client zone rule's action type is 'deliver'.", "zh_CN": "默认值: True 
        # 指定是否允许使用IPv6地址进行内容分发。仅当动作类型为'分发'时该值才有效。"}
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.by is not None:
            result['by'] = self.by
        if self.to is not None:
            result['to'] = self.to
        if self.enable_ipv_6 is not None:
            result['enableIPv6'] = self.enable_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('by') is not None:
            self.by = m.get('by')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('enableIPv6') is not None:
            self.enable_ipv_6 = m.get('enableIPv6')
        return self


class GetAnEdgeHostnameResponseHistoryConfigurationClientZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        weight: int = None,
        action: GetAnEdgeHostnameResponseHistoryConfigurationClientZonesAction = None,
        isp: str = None,
    ):
        # {"en" : "This field indicates the region in which the rule applies. Refer to our API to get client regions to get valid region codes. For example, if you wish to create a rule that covers all of Europe, simply specify 'eu' as the region. You can indicate specific countries. For example, 'na.us' represents the 'United States of America', and 'eu.fr' represents 'France'.  
        # 
        # A special client region 'all' can be used to specify that the rule applies to the entire world. If overlapping regions are specified, the more specific one takes precedence. For example, if you specify 'as' in one rule and 'as.cn' in another, a request from China will follow the rule for 'as.cn'.", "zh_CN": "该规则适用的区域。可调用'查询支持的区域列表'接口来查看区域信息。例如，如果您希望创建规则覆盖整个欧洲，则指定'eu'为区域。 您可以指定具体的国家。例如，'na.us'代表'美国'，而'eu.fr'代表'法国'。
        # 
        # 'all'是一个特殊的区域，可用于指定适用于全球的规则。如果不同规则指定的区域存在重叠，则以更细粒度的区域优先。例如，如果您在一条规则中指定'as'，在另一条规则中指定'as.cn'，则来自中国的请求将优先匹配'as.cn'的规则。"}
        self.region = region
        # {"en" : "Default: 100 Range: [ 0 .. 100 ] 
        # When multiple actions are specified for a client zone, the weight is used to adjust the probability of a client zone rule applying to a client request.
        # Consider two rules that apply to 'as.cn': {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        #  The probability of 'deliver' will be 100/(100+10) or 0.909 while the probability of 'redirect' will be 10/(100+10) or 0.091.
        #  
        # ", "zh_CN": "默认值: 100 取值范围: [ 0 .. 100 ] 
        # 可以为同个访客分区指定多条规则。通过在规则中指定weight字段，可控制规则匹配的权重。
        # 以'as.cn'区域的2条规则为例: {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        # 按照以上规则，客户端请求匹配规则1进行'分发'的比例为100/(100+10)，即0.909，匹配规则2进行'跳转'的比例为10/(100+10)，即0.091。
        #  
        # "}
        self.weight = weight
        # {"en" : "This object describes the action to take for requests matching the rule.", "zh_CN": "当规则匹配时执行的动作。"}
        self.action = action
        # {"en" : "Specify the code representing an ISP (Internet Service Provider) if the rule only applies to requests from a particular ISP. Call our API to get a list of supported ISPs. Specify 'all' to indicate all ISPs rather than a particular one. Specify a comma-separated list of up to 10 ISP codes if you want your rule to apply to more than one ISP.", "zh_CN": "该规则适用的运营商。可调用我们的'查询支持的ISP运营商列表'接口查看运营商信息。指定'all'表示所有运营商。如果希望该规则应用于多个运营商，则可指定多个运营商，用逗号分隔，但最多只能包含10个运营商。"}
        self.isp = isp

    def validate(self):
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.weight is not None:
            result['weight'] = self.weight
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('action') is not None:
            temp_model = GetAnEdgeHostnameResponseHistoryConfigurationClientZonesAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class GetAnEdgeHostnameResponseHistoryConfiguration(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
        has_beian: bool = None,
        client_zones: List[GetAnEdgeHostnameResponseHistoryConfigurationClientZones] = None,
        estimated_bandwidth: str = None,
    ):
        # {"en" : "An edge hostname.", "zh_CN": "调度域名。"}
        self.edge_hostname = edge_hostname
        # {"en" : "Default: False 
        # Indicates whether you have a Beian license for service in China. If you do, content can be served by servers located within mainland China using the ChinaStandard or ChinaPremium server group.
        # ", "zh_CN": "默认值: False 
        # 是否备案的标记。当值为true时，将使用包括中国大陆的服务器提供内容分发服务。"}
        self.has_beian = has_beian
        # {"en" : "Rules control how requests from client zones are handled. There must be a rule that covers all regions and all ISPs. ", "zh_CN": "自定义规则来控制如何处理不同访客分区的请求。您必须至少创建一条覆盖所有区域和所有运营商的规则。"}
        self.client_zones = client_zones
        # {"en" : "An estimate of the bandwidth required to serve content using this edge hostname. Units of measurement should be in Tbps, Gbps, Mbps, or kbps. Example: 100Gbps", "zh_CN": "通过该调度域名进行CDN加速预计需要的带宽。单位应为Tbps、Gbps、Mbps或kbps。示例：100 Gbps。"}
        self.estimated_bandwidth = estimated_bandwidth

    def validate(self):
        if self.client_zones:
            for k in self.client_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.client_zones is not None:
            result['clientZones'] = []
            for k in self.client_zones:
                result['clientZones'].append(k.to_map() if k else None)
        if self.estimated_bandwidth is not None:
            result['estimatedBandwidth'] = self.estimated_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('clientZones') is not None:
            self.client_zones = []
            for k in m.get('clientZones'):
                temp_model = GetAnEdgeHostnameResponseHistoryConfigurationClientZones()
                self.client_zones.append(temp_model.from_map(k))
        if m.get('estimatedBandwidth') is not None:
            self.estimated_bandwidth = m.get('estimatedBandwidth')
        return self


class GetAnEdgeHostnameResponseHistory(TeaModel):
    def __init__(
        self,
        operation: str = None,
        time: str = None,
        api_request_id: str = None,
        api_name: str = None,
        submission_time: str = None,
        finish_time: str = None,
        status: str = None,
        status_details: str = None,
        configuration: GetAnEdgeHostnameResponseHistoryConfiguration = None,
    ):
        # {"en" : "Enum: creation,update,deletion 
        # Indicates the action taken.", "zh_CN": "取值范围: creation,update,deletion 
        # 操作类型，即创建，更新或删除。"}
        self.operation = operation
        # {"en" : "RFC 3339 format date of the event. Same as submissionTime. ", "zh_CN": "操作时间，以RFC 3339日期格式表示。该字段的值等同于submissionTime。"}
        self.time = time
        # {"en" : "An ID representing the API call that made the change.", "zh_CN": "API请求的ID。"}
        self.api_request_id = api_request_id
        # {"en" : "API account that made the request.", "zh_CN": "调用接口的API账号的名称。"}
        self.api_name = api_name
        # {"en" : "RFC 3339 format date of the event.", "zh_CN": "操作时间，以RFC 3339日期格式表示。"}
        self.submission_time = submission_time
        # {"en" : "RFC 3339 format date indicating when the deployment completes.", "zh_CN": "配置异步部署的结束时间，以RFC 3339日期格式表示。"}
        self.finish_time = finish_time
        # {"en" : "Enum: waiting,in-progress,succeeded,failed
        # Deployment status.", "zh_CN": "取值范围: waiting,in-progress,succeeded,failed
        # 配置部署的状态。"}
        self.status = status
        # {"en" : "Details describing the status.", "zh_CN": "部署状态的描述信息。"}
        self.status_details = status_details
        # {"en" : "Contains settings that can be modified.", "zh_CN": "调度域名的相关设置。"}
        self.configuration = configuration

    def validate(self):
        self.validate_required(self.configuration, 'configuration')
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['operation'] = self.operation
        if self.time is not None:
            result['time'] = self.time
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_details is not None:
            result['statusDetails'] = self.status_details
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDetails') is not None:
            self.status_details = m.get('statusDetails')
        if m.get('configuration') is not None:
            temp_model = GetAnEdgeHostnameResponseHistoryConfiguration()
            self.configuration = temp_model.from_map(m['configuration'])
        return self


class GetAnEdgeHostnameResponseConfigsClientZonesAction(TeaModel):
    def __init__(
        self,
        type: str = None,
        by: List[str] = None,
        to: List[str] = None,
        enable_ipv_6: bool = None,
    ):
        # {"en" : "Enum: deliver,redirect,reject 
        # Defines the action to take for requests to the zone. Options are to deliver using one or more server groups, to reject the request altogether, or to redirect to another domain. If 'reject' is specified, the client request will be redirected to a server that always responds with HTTP response code 403 representing 'Forbidden'. Up to one 'reject' action is allowed for each client zone.
        # ", "zh_CN": "取值范围: deliver,redirect,reject 
        # 当规则匹配时，对客户端请求执行的动作的类型。包括分发，拒绝和跳转3个类型。如果指定了'拒绝'，则客户端请求将被调度到一台服务器，该服务器总是响应403状态码，表示'Forbidden'拒绝访问。每个访客分区最多只允许一个'拒绝'动作。"}
        self.type = type
        # {"en" : "This field is used if the action is of type 'deliver'. Specify one or more of the server groups (standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) to control the servers used to deliver content. If unspecified, 'standard' is used. <br/><br/>'nearChina' is a special server group that can be enabled for you if your domains lack ICP Beian, but you want optimal performance serving Chinese visitors. A client zone rule using nearChina cannot be configured to simultaneously deliver to other server groups, though you may create separate client zone rules to use other server groups.<br/><br/>If you have an ICP Beian license and want your content to be delivered by servers within China, you can opt to use 'ChinaStandard' and 'ChinaPremium.' Please contact our support team if you require nearChina, ChinaStandard, or ChinaPremium.<br/><br/>If an edge hostname is not initially configured to use ChinaStandard or ChinaPremium, you will not be able to modify it later to use these two server groups. Instead, you will need to create a new edge hostname with client zone rules delivering to those server groups.", "zh_CN": "如果动作类型为'分发'，则使用此字段指定一个或多个节点组(standard, premium, deluxe,  ultra, nearChina, ChinaStandard, ChinaPremium) 来选择提供内容分发服务的缓存节点。如果未指定，则使用'standard'。<br/><br/>'nearChina'  是一个特殊的节点组。如果您需要使用nearChina节点组，请联系我们的技术支持开通。不能在同一条规则中同时指定nearChina节点组和其他节点组。如果要使用其他节点组，需要创建单独的访客分区规则。<br/><br/>如果您的加速域名有ICP备案，希望由中国大陆的服务器提供内容分发服务，您可以选择使用'ChinaStandard'和'ChinaPremium'节点组。
        # <br/><br/>如果调度域名创建时没有指定使用ChinaStandard或ChinaPremium节点组，则无法通过更新调度域名来使用这两个节点组。您需要创建一个新的调度域名，在新的调度域名中指定使用ChinaStandard或ChinaPremium，才能使用这2个节点组。"}
        self.by = by
        # {"en" : "This field is used if the action is of type 'redirect'. It indicates the hostname or IP address to redirect to. This is typically an origin server or another CDN provider.", "zh_CN": "如果动作类型为'跳转'，则通过该字段指定跳转的目标域名或IP地址。'跳转'目标通常是源站服务器或其它CDN厂商。"}
        self.to = to
        # {"en" : "Default: True 
        # Indicates whether an IPv6 address can be used. This value is used only if the client zone rule's action type is 'deliver'.", "zh_CN": "默认值: True 
        # 指定是否允许使用IPv6地址进行内容分发。仅当动作类型为'分发'时该值才有效。"}
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.by is not None:
            result['by'] = self.by
        if self.to is not None:
            result['to'] = self.to
        if self.enable_ipv_6 is not None:
            result['enableIPv6'] = self.enable_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('by') is not None:
            self.by = m.get('by')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('enableIPv6') is not None:
            self.enable_ipv_6 = m.get('enableIPv6')
        return self


class GetAnEdgeHostnameResponseConfigsClientZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        weight: int = None,
        action: GetAnEdgeHostnameResponseConfigsClientZonesAction = None,
        isp: str = None,
    ):
        # {"en" : "This field indicates the region in which the rule applies. Refer to our API to get client regions to get valid region codes. For example, if you wish to create a rule that covers all of Europe, simply specify 'eu' as the region. You can indicate specific countries. For example, 'na.us' represents the 'United States of America', and 'eu.fr' represents 'France'.  
        # 
        # A special client region 'all' can be used to specify that the rule applies to the entire world. If overlapping regions are specified, the more specific one takes precedence. For example, if you specify 'as' in one rule and 'as.cn' in another, a request from China will follow the rule for 'as.cn'.", "zh_CN": "该规则适用的区域。可调用'查询支持的区域列表'接口来查看区域信息。例如，如果您希望创建规则覆盖整个欧洲，则指定'eu'为区域。 您可以指定具体的国家。例如，'na.us'代表'美国'，而'eu.fr'代表'法国'。
        # 
        # 'all'是一个特殊的区域，可用于指定适用于全球的规则。如果不同规则指定的区域存在重叠，则以更细粒度的区域优先。例如，如果您在一条规则中指定'as'，在另一条规则中指定'as.cn'，则来自中国的请求将优先匹配'as.cn'的规则。"}
        self.region = region
        # {"en" : "Default: 100 Range: [ 0 .. 100 ] 
        # When multiple actions are specified for a client zone, the weight is used to adjust the probability of a client zone rule applying to a client request.
        # Consider two rules that apply to 'as.cn': {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        #  The probability of 'deliver' will be 100/(100+10) or 0.909 while the probability of 'redirect' will be 10/(100+10) or 0.091.
        #  
        # ", "zh_CN": "默认值: 100 取值范围: [ 0 .. 100 ] 
        # 可以为同个访客分区指定多条规则。通过在规则中指定weight字段，可控制规则匹配的权重。
        # 以'as.cn'区域的2条规则为例: {'region':'as.cn', 'isp':'all', 'action':{'type':'deliver', 'by':['standard', 'premium', 'deluxe']}},
        #     {'region':'as.cn', 'isp':'all', 'action':{'type':'redirect', 'to':['alternate.cname.com']}, 'weight':10}
        # 
        # 按照以上规则，客户端请求匹配规则1进行'分发'的比例为100/(100+10)，即0.909，匹配规则2进行'跳转'的比例为10/(100+10)，即0.091。
        #  
        # "}
        self.weight = weight
        # {"en" : "This object describes the action to take for requests matching the rule.", "zh_CN": "当规则匹配时执行的动作。"}
        self.action = action
        # {"en" : "Specify the code representing an ISP (Internet Service Provider) if the rule only applies to requests from a particular ISP. Call our API to get a list of supported ISPs. Specify 'all' to indicate all ISPs rather than a particular one. Specify a comma-separated list of up to 10 ISP codes if you want your rule to apply to more than one ISP.", "zh_CN": "该规则适用的运营商。可调用我们的'查询支持的ISP运营商列表'接口查看运营商信息。指定'all'表示所有运营商。如果希望该规则应用于多个运营商，则可指定多个运营商，用逗号分隔，但最多只能包含10个运营商。"}
        self.isp = isp

    def validate(self):
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.weight is not None:
            result['weight'] = self.weight
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('action') is not None:
            temp_model = GetAnEdgeHostnameResponseConfigsClientZonesAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class GetAnEdgeHostnameResponseConfigs(TeaModel):
    def __init__(
        self,
        edge_hostname: str = None,
        pci_required: bool = None,
        description: str = None,
        has_beian: bool = None,
        client_zones: List[GetAnEdgeHostnameResponseConfigsClientZones] = None,
        estimated_bandwidth: str = None,
    ):
        # {"en" : "An edge hostname.", "zh_CN": "调度域名。"}
        self.edge_hostname = edge_hostname
        # {"en" : "Default: False 
        # Indicates whether PCI compliance is required.  true means content will only be served by PCI certified PoPs.", "zh_CN": "默认值: False 
        # 表示流量调度是否需要遵循PCI规范。当值为true时，表示只能使用已通过PCI认证的节点提供内容分发服务。"}
        self.pci_required = pci_required
        # {"en" : "A description of the edge hostname.", "zh_CN": "调度域名的描述。"}
        self.description = description
        # {"en" : "Default: False 
        # Indicates whether you have a Beian license for service in China. If you do, content can be served by servers located within mainland China using the ChinaStandard or ChinaPremium server group.
        # ", "zh_CN": "默认值: False 
        # 是否备案的标记。当值为true时，将使用包括中国大陆的服务器提供内容分发服务。"}
        self.has_beian = has_beian
        # {"en" : "Rules control how requests from client zones are handled. There must be a rule that covers all regions and all ISPs. ", "zh_CN": "自定义规则来控制如何处理不同访客分区的请求。您必须至少创建一条覆盖所有区域和所有运营商的规则。"}
        self.client_zones = client_zones
        # {"en" : "An estimate of the bandwidth required to serve content using this edge hostname. Units of measurement should be in Tbps, Gbps, Mbps, or kbps. Example: 100Gbps", "zh_CN": "通过该调度域名进行CDN加速预计需要的带宽。单位应为Tbps、Gbps、Mbps或kbps。示例：100 Gbps。"}
        self.estimated_bandwidth = estimated_bandwidth

    def validate(self):
        if self.client_zones:
            for k in self.client_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname
        if self.pci_required is not None:
            result['pciRequired'] = self.pci_required
        if self.description is not None:
            result['description'] = self.description
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.client_zones is not None:
            result['clientZones'] = []
            for k in self.client_zones:
                result['clientZones'].append(k.to_map() if k else None)
        if self.estimated_bandwidth is not None:
            result['estimatedBandwidth'] = self.estimated_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostname') is not None:
            self.edge_hostname = m.get('edgeHostname')
        if m.get('pciRequired') is not None:
            self.pci_required = m.get('pciRequired')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('clientZones') is not None:
            self.client_zones = []
            for k in m.get('clientZones'):
                temp_model = GetAnEdgeHostnameResponseConfigsClientZones()
                self.client_zones.append(temp_model.from_map(k))
        if m.get('estimatedBandwidth') is not None:
            self.estimated_bandwidth = m.get('estimatedBandwidth')
        return self


class GetAnEdgeHostnameResponse(TeaModel):
    def __init__(
        self,
        history: List[GetAnEdgeHostnameResponseHistory] = None,
        last_update_time: str = None,
        creation_time: str = None,
        configs: GetAnEdgeHostnameResponseConfigs = None,
    ):
        # {"en" : "Operation history", "zh_CN": "调度域名的操作记录。"}
        self.history = history
        # {"en" : "RFC 3339 format date indicating when the edge hostname was last updated.", "zh_CN": "RFC 3339格式的日期，表示调度域名最后一次更新的时间。"}
        self.last_update_time = last_update_time
        # {"en" : "RFC 3339 format date indicating when the edge hostname was created.", "zh_CN": "RFC 3339格式的日期，表示调度域名的创建时间。"}
        self.creation_time = creation_time
        # {"en" : "Contains settings of the edge hostname.", "zh_CN": "调度域名的具体配置。此处展示的内容是调度域名当前已部署生效的配置。如果您提交了更新调度域名的请求，但配置仍在部署中还未生效，此处不会展示您修改后的配置。如果调度域名暂时还没有部署生效的配置，此处展示的是最近一次提交的配置。"}
        self.configs = configs

    def validate(self):
        self.validate_required(self.history, 'history')
        if self.history:
            for k in self.history:
                if k:
                    k.validate()
        self.validate_required(self.last_update_time, 'last_update_time')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.configs, 'configs')
        if self.configs:
            self.configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.history is not None:
            result['history'] = []
            for k in self.history:
                result['history'].append(k.to_map() if k else None)
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.configs is not None:
            result['configs'] = self.configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('history') is not None:
            self.history = []
            for k in m.get('history'):
                temp_model = GetAnEdgeHostnameResponseHistory()
                self.history.append(temp_model.from_map(k))
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('configs') is not None:
            temp_model = GetAnEdgeHostnameResponseConfigs()
            self.configs = temp_model.from_map(m['configs'])
        return self




