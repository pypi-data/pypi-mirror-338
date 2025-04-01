# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetAListOfOriginShieldsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfOriginShieldsParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        sort_by: str = None,
        sort_order: str = None,
        used_in_properties: str = None,
    ):
        # {"en" : "The value of the search parameter is matched on the shields' name, id, regions, ipV4 , and ipV6 fields. Only those shields that match will be returned in the response.", "zh_CN": "输入搜索关键字查询shield。接口将返回名称，id，区域或ip地址中含有关键字的shield。"}
        self.search = search
        # {"en" : "Enum: lastUpdated,effectiveDate 
        # Default: lastUpdated 
        # Returns shields sorted by when they were last updated or when they became active.", "zh_CN": "取值范围: lastUpdated,effectiveDate 
        # 默认值: lastUpdated 
        # 按最近更新时间或生效时间对shield进行排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc,desc 
        # Default: desc 
        # Returns shields in sorted order, either 'asc' for ascending or 'desc' for descending. The default is to return the last shield updated first.", "zh_CN": "取值范围: asc,desc 
        # 默认值: desc 
        # 按升序或降序对shield进行排序。"}
        self.sort_order = sort_order
        # {"en" : "Enum: false,true 
        # Filter results based on whether shields are used in properties deployed to staging or production. If unspecified, all available shields are returned.", "zh_CN": "取值范围: false,true 
        # 按照shield是否在已部署的加速项目中使用来查询。默认查询所有shield。"}
        self.used_in_properties = used_in_properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.used_in_properties is not None:
            result['usedInProperties'] = self.used_in_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('usedInProperties') is not None:
            self.used_in_properties = m.get('usedInProperties')
        return self


class GetAListOfOriginShieldsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfOriginShieldsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfOriginShieldsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfOriginShieldsResponseShields(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        region: str = None,
        ip_v4: List[str] = None,
        ip_v6: List[str] = None,
        last_updated: str = None,
        effective_date: str = None,
        used_in_properties: bool = None,
    ):
        # {"en" : "Name of the shield.", "zh_CN": "shield名称。"}
        self.name = name
        # {"en" : "A unique identifier representing the shield. This ID is referenced in properties using the shield.", "zh_CN": "shield唯一标识的ID。在加速项目中以该ID引用shield。"}
        self.id = id
        # {"en" : "Indicates the region of the origin shield. It is typically an ISO-3166-1 code representing a country. When choosing an origin shield for your property, it is best to select one closer to your origin servers.
        # Use of a shield located in the 'cn' region (China) requires your property to have 'hasBeian' set to true which means all of its hostnames have an ICP Beian license required by the Chinese government.", "zh_CN": "shield所在区域。通常以ISO-3166-1的国家码表示。当您选择shield时，建议选择离源站最近的shield，以达到最佳效果。如您需要使用位于中国区域的shield，则您的加速项目配置中是否备案需要设为'是'，您相关的加速域名必须已取得备案。"}
        self.region = region
        # {"en" : "A list of IPv4 addresses used by the shield. If your origin server has an access control list, include these IP addresses.", "zh_CN": "shield所使用到的IPv4地址。如果您的源站开启了访问控制，需要对此处的IP列表进行加白。"}
        self.ip_v4 = ip_v4
        # {"en" : "A list of IPv6 addresses used by the shield. If your origin server has an access control list, include these IP addresses.", "zh_CN": "shield所使用到的IPv6地址。如果您的源站开启了访问控制，需要对此处的IP列表进行加白。"}
        self.ip_v6 = ip_v6
        # {"en" : "An RFC 3339 date indicating when the shield was last updated.", "zh_CN": "shield最近一次更新的时间，以RFC 3339日期格式表示。"}
        self.last_updated = last_updated
        # {"en" : "An RFC 3339 date indicating when the shield became active.", "zh_CN": "shield的生效时间，以RFC 3339日期格式表示。"}
        self.effective_date = effective_date
        # {"en" : "Whether the shield is used in any properties deployed to staging or production.", "zh_CN": "该shield是否在已部署的加速项目中使用。"}
        self.used_in_properties = used_in_properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.region is not None:
            result['region'] = self.region
        if self.ip_v4 is not None:
            result['ipV4'] = self.ip_v4
        if self.ip_v6 is not None:
            result['ipV6'] = self.ip_v6
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.effective_date is not None:
            result['effectiveDate'] = self.effective_date
        if self.used_in_properties is not None:
            result['usedInProperties'] = self.used_in_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('ipV4') is not None:
            self.ip_v4 = m.get('ipV4')
        if m.get('ipV6') is not None:
            self.ip_v6 = m.get('ipV6')
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('effectiveDate') is not None:
            self.effective_date = m.get('effectiveDate')
        if m.get('usedInProperties') is not None:
            self.used_in_properties = m.get('usedInProperties')
        return self


class GetAListOfOriginShieldsResponse(TeaModel):
    def __init__(
        self,
        shields: List[GetAListOfOriginShieldsResponseShields] = None,
    ):
        # {"en" : "A list of shields that can be used in a property.", "zh_CN": "shield列表。"}
        self.shields = shields

    def validate(self):
        self.validate_required(self.shields, 'shields')
        if self.shields:
            for k in self.shields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shields is not None:
            result['shields'] = []
            for k in self.shields:
                result['shields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('shields') is not None:
            self.shields = []
            for k in m.get('shields'):
                temp_model = GetAListOfOriginShieldsResponseShields()
                self.shields.append(temp_model.from_map(k))
        return self






class GetSystemConfigurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSystemConfigurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSystemConfigurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSystemConfigurationRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSystemConfigurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSystemConfigurationResponseExtraServicePorts(TeaModel):
    def __init__(
        self,
        http: List[str] = None,
        https: List[str] = None,
    ):
        # {"en" : "Specifies ports other than the default 80 which can be used to handle HTTP requests.", "zh_CN": "可用于监听HTTP请求的非标准端口。80端口默认支持。"}
        self.http = http
        # {"en" : "Specify ports other than the default 443 which can be used to handle HTTPS requests.", "zh_CN": "可用于监听HTTPS请求的非标准端口。443端口默认支持。"}
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class GetSystemConfigurationResponse(TeaModel):
    def __init__(
        self,
        minimum_supported_cache_version: str = None,
        base_directives: List[str] = None,
        advanced_directives: List[str] = None,
        extra_service_ports: GetSystemConfigurationResponseExtraServicePorts = None,
        advanced_feaures: List[str] = None,
        oldest_property_validation_time: str = None,
        base_lb_directives: List[str] = None,
        advanced_lb_directives: List[str] = None,
    ):
        # {"en" : "The minimum version of the cache server required to validate and deploy properties.", "zh_CN": "Cache服务器最低版本。低于该版本，加速项目的验证和部署可能无法正常工作。"}
        self.minimum_supported_cache_version = minimum_supported_cache_version
        # {"en" : "A list of Edge Logic directives that are available to everyone.", "zh_CN": "边缘逻辑基础指令列表。这些指令默认对所有客户开放。"}
        self.base_directives = base_directives
        # {"en" : "A list of advanced Edge Logic directives that can be enabled by contacting our support team.", "zh_CN": "边缘逻辑高级指令列表。这些指令需联系我们的技术支持团队开通。"}
        self.advanced_directives = advanced_directives
        # {"en" : "This field lists nonstandard ports that can be used to handle HTTP and HTTPS requests. If your website uses a nonstandard port which is not listed, please contact our support team. You can specify one of these port numbers in the extraServicePorts field of your property configuration.", "zh_CN": "该字段返回CDN Pro支持的HTTP, HTTPS非标准服务端口。这些端口可以用在加速项目的extraServicePorts配置项中。如果你所使用的非标准端口不在该列表中，可联系我们的技术支持团队开通。"}
        self.extra_service_ports = extra_service_ports
        # {"en" : "List of advanced features that can be enabled for customers via the service quota API. 'realTimeLog' is an advanced feature allowing a customer to monitor requests from visitors to the content as they are received. 'nearChina' is an advanced feature allowing use of a special server group to provide better performance to visitors in China for domains without ICP Beian. 'originShield' allows use of an extra layer of servers in front of a property's origin servers. Please contact our support team if you require an advanced feature.", "zh_CN": "CDN Pro支持的高级功能列表。例如，'realTimeLog'日志可用于实时回传日志。如果需要使用这些高级功能，请联系我们的技术支持团队开通。"}
        self.advanced_feaures = advanced_feaures
        # {"en" : "RFC 3339 date indicating the oldest validated property that can be deployed. Properties validated before this date must be re-validated before you can deploy them. Example: '2021-02-05T00:00:00Z'", "zh_CN": "加速项目验证通过的有效起始时间。如果加速项目的验证早于该时间，则必须重新验证通过后才能部署。采用RFC 3339日期格式，例如'2021-02-05T00:00:00Z'。"}
        self.oldest_property_validation_time = oldest_property_validation_time
        # {"en" : "List of Edge Logic directives that can be used in the loadBalancerLogic field of a property by everyone.", "zh_CN": "可用于加速项目中loadBalancerLogic字段的边缘逻辑指令列表。这些指令默认对所有客户开放。"}
        self.base_lb_directives = base_lb_directives
        # {"en" : "A list of advanced Edge Logic directives that can be enabled for use in the loadBalancerLogic field of a property. If you require one that is not enabled for your account, please contact our support team.", "zh_CN": "可用于加速项目中loadBalancerLogic字段的边缘逻辑高级指令列表。如果需要使用这些指令，请联系我们的技术支持团队开通。"}
        self.advanced_lb_directives = advanced_lb_directives

    def validate(self):
        self.validate_required(self.minimum_supported_cache_version, 'minimum_supported_cache_version')
        self.validate_required(self.base_directives, 'base_directives')
        self.validate_required(self.advanced_directives, 'advanced_directives')
        self.validate_required(self.extra_service_ports, 'extra_service_ports')
        if self.extra_service_ports:
            self.extra_service_ports.validate()
        self.validate_required(self.advanced_feaures, 'advanced_feaures')
        self.validate_required(self.oldest_property_validation_time, 'oldest_property_validation_time')
        self.validate_required(self.base_lb_directives, 'base_lb_directives')
        self.validate_required(self.advanced_lb_directives, 'advanced_lb_directives')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.minimum_supported_cache_version is not None:
            result['minimumSupportedCacheVersion'] = self.minimum_supported_cache_version
        if self.base_directives is not None:
            result['baseDirectives'] = self.base_directives
        if self.advanced_directives is not None:
            result['advancedDirectives'] = self.advanced_directives
        if self.extra_service_ports is not None:
            result['extraServicePorts'] = self.extra_service_ports.to_map()
        if self.advanced_feaures is not None:
            result['advancedFeaures'] = self.advanced_feaures
        if self.oldest_property_validation_time is not None:
            result['oldestPropertyValidationTime'] = self.oldest_property_validation_time
        if self.base_lb_directives is not None:
            result['baseLbDirectives'] = self.base_lb_directives
        if self.advanced_lb_directives is not None:
            result['advancedLbDirectives'] = self.advanced_lb_directives
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minimumSupportedCacheVersion') is not None:
            self.minimum_supported_cache_version = m.get('minimumSupportedCacheVersion')
        if m.get('baseDirectives') is not None:
            self.base_directives = m.get('baseDirectives')
        if m.get('advancedDirectives') is not None:
            self.advanced_directives = m.get('advancedDirectives')
        if m.get('extraServicePorts') is not None:
            temp_model = GetSystemConfigurationResponseExtraServicePorts()
            self.extra_service_ports = temp_model.from_map(m['extraServicePorts'])
        if m.get('advancedFeaures') is not None:
            self.advanced_feaures = m.get('advancedFeaures')
        if m.get('oldestPropertyValidationTime') is not None:
            self.oldest_property_validation_time = m.get('oldestPropertyValidationTime')
        if m.get('baseLbDirectives') is not None:
            self.base_lb_directives = m.get('baseLbDirectives')
        if m.get('advancedLbDirectives') is not None:
            self.advanced_lb_directives = m.get('advancedLbDirectives')
        return self






class GetOriginFastRouteIpListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteIpListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteIpListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteIpListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteIpListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteIpListResponse(TeaModel):
    def __init__(
        self,
        last_updated: str = None,
        effective_date: str = None,
        ip_v4: List[str] = None,
        ip_v6: List[str] = None,
    ):
        # {"en" : "RFC 3339 date indicating when the list of IP addresses was last updated.", "zh_CN": "IP列表最后一次更新的时间，以RFC 3339日期格式表示。"}
        self.last_updated = last_updated
        # {"en" : "RFC 3339 date indicating when the IP addresses became effective.", "zh_CN": "IP列表的生效时间，以RFC 3339日期格式表示。"}
        self.effective_date = effective_date
        # {"en" : "IPv4 addresses used by origin fast route servers.", "zh_CN": "快速回源服务器的IPv4地址。"}
        self.ip_v4 = ip_v4
        # {"en" : "IPv6 addresses used by origin fast route servers.", "zh_CN": "快速回源服务器的IPv6地址。"}
        self.ip_v6 = ip_v6

    def validate(self):
        self.validate_required(self.last_updated, 'last_updated')
        self.validate_required(self.effective_date, 'effective_date')
        self.validate_required(self.ip_v4, 'ip_v4')
        self.validate_required(self.ip_v6, 'ip_v6')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.effective_date is not None:
            result['effectiveDate'] = self.effective_date
        if self.ip_v4 is not None:
            result['ipV4'] = self.ip_v4
        if self.ip_v6 is not None:
            result['ipV6'] = self.ip_v6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('effectiveDate') is not None:
            self.effective_date = m.get('effectiveDate')
        if m.get('ipV4') is not None:
            self.ip_v4 = m.get('ipV4')
        if m.get('ipV6') is not None:
            self.ip_v6 = m.get('ipV6')
        return self






class GetStagingServersListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStagingServersListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStagingServersListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStagingServersListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStagingServersListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStagingServersListResponseStagingServers(TeaModel):
    def __init__(
        self,
        ip: str = None,
        code: str = None,
        location: str = None,
        ip_version: int = None,
    ):
        # {"en" : "IP address. It can be IPv4 or IPv6 format.", "zh_CN": "服务器的IP地址，IPv4或IPv6格式。"}
        self.ip = ip
        # {"en" : "A code representing the staging server.", "zh_CN": "服务器所在的区域的代码。"}
        self.code = code
        # {"en" : "Location of the staging server.", "zh_CN": "服务器所在的区域。"}
        self.location = location
        # {"en" : "Enum: 4,6 
        # Indicates the format of the 'ip' field.", "zh_CN": "取值范围: 4,6 
        # IP协议版本。"}
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.code is not None:
            result['code'] = self.code
        if self.location is not None:
            result['location'] = self.location
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        return self


class GetStagingServersListResponse(TeaModel):
    def __init__(
        self,
        staging_servers: List[GetStagingServersListResponseStagingServers] = None,
    ):
        # {"en" : "Each entry describe a staging server.", "zh_CN": "每个对象代表一台服务器。"}
        self.staging_servers = staging_servers

    def validate(self):
        self.validate_required(self.staging_servers, 'staging_servers')
        if self.staging_servers:
            for k in self.staging_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.staging_servers is not None:
            result['stagingServers'] = []
            for k in self.staging_servers:
                result['stagingServers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stagingServers') is not None:
            self.staging_servers = []
            for k in m.get('stagingServers'):
                temp_model = GetStagingServersListResponseStagingServers()
                self.staging_servers.append(temp_model.from_map(k))
        return self






class GetIpAddressesOfTheCdnPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIpAddressesOfTheCdnParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIpAddressesOfTheCdnRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIpAddressesOfTheCdnRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIpAddressesOfTheCdnResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetIpAddressesOfTheCdnResponse(TeaModel):
    def __init__(
        self,
        last_updated: str = None,
        effective_date: str = None,
        ip_v4: List[str] = None,
        ip_v6: List[str] = None,
    ):
        # {"en" : "RFC 3339 date indicating when the list of IP addresses was last updated.", "zh_CN": "IP地址列表最近一次更新时间，以RFC 3339格式展示。"}
        self.last_updated = last_updated
        # {"en" : "RFC 3339 date indicating when the IP address list became effective.", "zh_CN": "IP地址列表生效时间，以RFC 3339格式展示。"}
        self.effective_date = effective_date
        # {"en" : "IPv4 addresses used by CDN Pro.", "zh_CN": "CDN Pro所使用的IPv4地址。"}
        self.ip_v4 = ip_v4
        # {"en" : "IPv6 addresses used by CDN Pro.", "zh_CN": "CDN Pro所使用的IPv6地址。"}
        self.ip_v6 = ip_v6

    def validate(self):
        self.validate_required(self.last_updated, 'last_updated')
        self.validate_required(self.effective_date, 'effective_date')
        self.validate_required(self.ip_v4, 'ip_v4')
        self.validate_required(self.ip_v6, 'ip_v6')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.effective_date is not None:
            result['effectiveDate'] = self.effective_date
        if self.ip_v4 is not None:
            result['ipV4'] = self.ip_v4
        if self.ip_v6 is not None:
            result['ipV6'] = self.ip_v6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('effectiveDate') is not None:
            self.effective_date = m.get('effectiveDate')
        if m.get('ipV4') is not None:
            self.ip_v4 = m.get('ipV4')
        if m.get('ipV6') is not None:
            self.ip_v6 = m.get('ipV6')
        return self






class GetAShieldByItsIdPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a shield", "zh_CN": "shield id。"}
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


class GetAShieldByItsIdParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAShieldByItsIdRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAShieldByItsIdRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAShieldByItsIdResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAShieldByItsIdResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        region: str = None,
        ip_v4: List[str] = None,
        ip_v6: List[str] = None,
        last_updated: str = None,
        effective_date: str = None,
        used_in_properties: bool = None,
    ):
        # {"en" : "Name of the shield.", "zh_CN": "shield名称。"}
        self.name = name
        # {"en" : "A unique identifier representing the shield. This ID is referenced in properties using the shield.", "zh_CN": "shield唯一标识的ID。在加速项目中以该ID引用shield。"}
        self.id = id
        # {"en" : "Indicates the region of the origin shield. It is typically an ISO-3166-1 code representing a country. When choosing an origin shield for your property, it is best to select one closer to your origin servers.
        # Use of a shield located in the 'cn' region (China) requires your property to have 'hasBeian' set to true which means all of its hostnames have an ICP Beian license required by the Chinese government.", "zh_CN": "shield所在区域。通常以ISO-3166-1的国家码表示。当您选择shield时，建议选择离源站最近的shield，以达到最佳效果。如您需要使用位于中国区域的shield，则您的加速项目配置中是否备案需要设为'是'，您相关的加速域名必须已取得备案。"}
        self.region = region
        # {"en" : "A list of IPv4 addresses used by the shield. If your origin server has an access control list, include these IP addresses.", "zh_CN": "shield所使用到的IPv4地址。如果您的源站开启了访问控制，需要对此处的IP列表进行加白。"}
        self.ip_v4 = ip_v4
        # {"en" : "A list of IPv6 addresses used by the shield. If your origin server has an access control list, include these IP addresses.", "zh_CN": "shield所使用到的IPv6地址。如果您的源站开启了访问控制，需要对此处的IP列表进行加白。"}
        self.ip_v6 = ip_v6
        # {"en" : "An RFC 3339 date indicating when the shield was last updated.", "zh_CN": "shield最近一次更新的时间，以RFC 3339日期格式表示。"}
        self.last_updated = last_updated
        # {"en" : "An RFC 3339 date indicating when the shield became active.", "zh_CN": "shield的生效时间，以RFC 3339日期格式表示。"}
        self.effective_date = effective_date
        # {"en" : "Whether the shield is used in any properties deployed to staging or production.", "zh_CN": "该shield是否在已部署的加速项目中使用。"}
        self.used_in_properties = used_in_properties

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.id, 'id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.ip_v4, 'ip_v4')
        self.validate_required(self.ip_v6, 'ip_v6')
        self.validate_required(self.last_updated, 'last_updated')
        self.validate_required(self.effective_date, 'effective_date')
        self.validate_required(self.used_in_properties, 'used_in_properties')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.region is not None:
            result['region'] = self.region
        if self.ip_v4 is not None:
            result['ipV4'] = self.ip_v4
        if self.ip_v6 is not None:
            result['ipV6'] = self.ip_v6
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.effective_date is not None:
            result['effectiveDate'] = self.effective_date
        if self.used_in_properties is not None:
            result['usedInProperties'] = self.used_in_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('ipV4') is not None:
            self.ip_v4 = m.get('ipV4')
        if m.get('ipV6') is not None:
            self.ip_v6 = m.get('ipV6')
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('effectiveDate') is not None:
            self.effective_date = m.get('effectiveDate')
        if m.get('usedInProperties') is not None:
            self.used_in_properties = m.get('usedInProperties')
        return self






class CheckIfIpAddressesBelongToTheCdnProPlatformPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformRequest(TeaModel):
    def __init__(
        self,
        ip_list: List[str] = None,
    ):
        # {"en" : "Range: <= 128 items 
        # Array of IPv4 or IPv6 addresses to check.", "zh_CN": "取值范围: <= 128 条目 
        # 需要查询的IP地址列表。支持IPv4和IPv6。"}
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformResponseIpDetails(TeaModel):
    def __init__(
        self,
        ip: str = None,
        is_cdn_pro_ip: bool = None,
        protocol: str = None,
    ):
        # {"en" : "An IPv4 or IPv6 address.", "zh_CN": "IPv4或IPv6地址。"}
        self.ip = ip
        # {"en" : "True if the IP address belongs to the CDN Pro platform.", "zh_CN": "IP地址是否来自CDN Pro。"}
        self.is_cdn_pro_ip = is_cdn_pro_ip
        # {"en" : "Enum: IPv4,IPv6 
        # Indicates the protocol of the IP address.", "zh_CN": "取值范围: IPv4,IPv6 
        # IP协议。"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.is_cdn_pro_ip is not None:
            result['isCdnProIp'] = self.is_cdn_pro_ip
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('isCdnProIp') is not None:
            self.is_cdn_pro_ip = m.get('isCdnProIp')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class CheckIfIpAddressesBelongToTheCdnProPlatformResponse(TeaModel):
    def __init__(
        self,
        ip_details: List[CheckIfIpAddressesBelongToTheCdnProPlatformResponseIpDetails] = None,
    ):
        # {"en" : "Describes an IP address.", "zh_CN": "IP地址列表。"}
        self.ip_details = ip_details

    def validate(self):
        self.validate_required(self.ip_details, 'ip_details')
        if self.ip_details:
            for k in self.ip_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_details is not None:
            result['ipDetails'] = []
            for k in self.ip_details:
                result['ipDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipDetails') is not None:
            self.ip_details = []
            for k in m.get('ipDetails'):
                temp_model = CheckIfIpAddressesBelongToTheCdnProPlatformResponseIpDetails()
                self.ip_details.append(temp_model.from_map(k))
        return self




