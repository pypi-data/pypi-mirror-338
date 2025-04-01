# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetListOfHostnamesThatHaveBeenDeployedPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfHostnamesThatHaveBeenDeployedParameters(TeaModel):
    def __init__(
        self,
        offset: int = None,
        limit: int = None,
        target: str = None,
    ):
        # {"en" : "Default: 0 >= 0 
        # Index of the first hostname to return. Defaults to 0.", "zh_CN": "默认值: 0 取值范围：>= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 [ 1 .. 200 ] 
        # Maximum number of hostnames to return.", "zh_CN": "默认值: 100 取值范围：<= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: all staging production 
        # Default: all 
        # Limit the response to hostnames from properties deployed to staging only or production only. By default, all hostnames from properties deployed to either production or staging are returned.", "zh_CN": "取值范围: all, staging, production 
        # 默认值: all 
        # 根据部署环境来查询加速域名。默认情况下，查询部署到演练和生产环境下的所有域名。"}
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class GetListOfHostnamesThatHaveBeenDeployedRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfHostnamesThatHaveBeenDeployedRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfHostnamesThatHaveBeenDeployedResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfHostnamesThatHaveBeenDeployedResponseHostnames(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        property_in_production: str = None,
        property_in_staging: str = None,
    ):
        # {"en" : "A hostname whose property has been deployed to production or staging.", "zh_CN": "加速域名。"}
        self.hostname = hostname
        # {"en" : "Describes the property deployed to production. It can be 'null' if the property is not deployed to production.", "zh_CN": "如果加速域名对应的加速项目已部署到生产环境，则该字段返回该加速项目的相关信息。如果加速项目未部署到生产环境，则该字段返回'null'。"}
        self.property_in_production = property_in_production
        # {"en" : "Describes the property deployed to staging. It can be 'null' if the property is not deployed to staging.", "zh_CN": "如果加速域名对应的加速项目已部署到演练环境，则该字段返回该加速项目的相关信息。如果加速项目未部署到演练环境，则该字段返回'null'。"}
        self.property_in_staging = property_in_staging

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.property_in_production is not None:
            result['propertyInProduction'] = self.property_in_production
        if self.property_in_staging is not None:
            result['propertyInStaging'] = self.property_in_staging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('propertyInProduction') is not None:
            self.property_in_production = m.get('propertyInProduction')
        if m.get('propertyInStaging') is not None:
            self.property_in_staging = m.get('propertyInStaging')
        return self


class GetListOfHostnamesThatHaveBeenDeployedResponse(TeaModel):
    def __init__(
        self,
        hostnames: List[GetListOfHostnamesThatHaveBeenDeployedResponseHostnames] = None,
        count: int = None,
    ):
        # {"en" : "List of hostnames.", "zh_CN": "加速域名列表。"}
        self.hostnames = hostnames
        # {"en" : ">= 0 
        # Number of hostnames.", "zh_CN": "取值范围: >= 0 
        # 加速域名总数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.hostnames, 'hostnames')
        if self.hostnames:
            for k in self.hostnames:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = []
            for k in self.hostnames:
                result['hostnames'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = []
            for k in m.get('hostnames'):
                temp_model = GetListOfHostnamesThatHaveBeenDeployedResponseHostnames()
                self.hostnames.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self






class GetHistoricalInformationAboutOneHostnamePaths(TeaModel):
    def __init__(
        self,
        hostname: str = None,
    ):
        # {"en" : "A hostname that was defined in a property.", "zh_CN": "加速域名。"}
        self.hostname = hostname

    def validate(self):
        self.validate_required(self.hostname, 'hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        return self


class GetHistoricalInformationAboutOneHostnameParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        target: str = None,
    ):
        # {"en" : "Beginning of the time period in RFC 3339 format. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-11-14T00:00:00Z By default, the value is when you began using CDN Pro.", "zh_CN": "指定查询开始时间，以RFC 3339日期格式表示。必须使用UTC时区，不支持指定其它时区。示例：startdate=2019-11-14T00:00:00Z。如果开始时间未指定，则默认为您开通CDN Pro服务的时间。"}
        self.startdate = startdate
        # {"en" : "End of the time period in RFC 3339 format. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z The default is the current time.", "zh_CN": "指定查询结束时间，以RFC 3339日期格式表示。必须使用UTC时区，不支持指定其它时区。示例：enddate=2019-12-14T00:00:00Z。如果结束时间未指定，则默认为当前时间。"}
        self.enddate = enddate
        # {"en" : "Enum: all,staging,production 
        # Default: all 
        # The value can be 'all', 'staging', or 'production' to filter the results based on where the hostnames have been deployed. 
        # ", "zh_CN": "取值范围: all,staging,production 
        # 默认值: all 
        # 根据加速域名的部署环境过滤。该值可以是'all', 'staging', 或'production'，分别表示所有环境，演练环境和生产环境。"}
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class GetHistoricalInformationAboutOneHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutOneHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutOneHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutOneHostnameResponseHistory(TeaModel):
    def __init__(
        self,
        target: str = None,
        property_id: str = None,
        deployment_date: str = None,
        undeployment_date: str = None,
    ):
        # {"en" : "The environment where the hostname is deployed.", "zh_CN": "加速域名所部署的环境。"}
        self.target = target
        # {"en" : "ID of the property that included the hostname.", "zh_CN": "加速域名对应的加速项目的ID。"}
        self.property_id = property_id
        # {"en" : "RFC 3339 date with UTC time that indicates when the property with the hostname was deployed. Example: '2020-04-24T20:09:15Z'", "zh_CN": "RFC 3339格式的日期，表示加速项目的部署时间，采用UTC时区。示例：'2020-04-24T20:09:15Z'。"}
        self.deployment_date = deployment_date
        # {"en" : "RFC 3339 date with UTC time that indicates when the property with the hostname was undeployed. Example: '2020-04-24T20:09:15Z'", "zh_CN": "RFC 3339格式的日期，表示加速项目的卸载时间，采用UTC时区。示例：'2020-04-24T20:09:15Z'。"}
        self.undeployment_date = undeployment_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target is not None:
            result['target'] = self.target
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.deployment_date is not None:
            result['deploymentDate'] = self.deployment_date
        if self.undeployment_date is not None:
            result['undeploymentDate'] = self.undeployment_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('deploymentDate') is not None:
            self.deployment_date = m.get('deploymentDate')
        if m.get('undeploymentDate') is not None:
            self.undeployment_date = m.get('undeploymentDate')
        return self


class GetHistoricalInformationAboutOneHostnameResponse(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        history: List[GetHistoricalInformationAboutOneHostnameResponseHistory] = None,
    ):
        # {"en" : "A hostname that was defined in a property.", "zh_CN": "加速域名。"}
        self.hostname = hostname
        # {"en" : "The history contains deployment and undeployment dates. It is empty if the hostname has never been deployed to production.", "zh_CN": "加速域名部署到生产环境或从生产环境卸载的历史信息。如果加速域名从未部署到生产环境，则返回空对象。"}
        self.history = history

    def validate(self):
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.history, 'history')
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.history is not None:
            result['history'] = []
            for k in self.history:
                result['history'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('history') is not None:
            self.history = []
            for k in m.get('history'):
                temp_model = GetHistoricalInformationAboutOneHostnameResponseHistory()
                self.history.append(temp_model.from_map(k))
        return self






class GetHistoricalInformationAboutHostnamesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutHostnamesParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        search: str = None,
        target: str = None,
        offset: int = None,
        limit: int = None,
    ):
        # {"en" : "Beginning of the time period in RFC 3339 format. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-11-14T00:00:00Z By default, the value is when you began using CDN Pro.", "zh_CN": "指定查询开始时间，以RFC 3339日期格式表示。必须使用UTC时区，不支持指定其它时区。示例：startdate=2019-11-14T00:00:00Z。如果开始时间未指定，则默认为您开通CDN Pro服务的时间。"}
        self.startdate = startdate
        # {"en" : "End of the time period in RFC 3339 format. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z The default is the current time.", "zh_CN": "指定查询结束时间，以RFC 3339日期格式表示。必须使用UTC时区，不支持指定其它时区。示例：enddate=2019-12-14T00:00:00Z。如果结束时间未指定，默认为当前时间。"}
        self.enddate = enddate
        # {"en" : "Filter by looking up the beginning portion of a hostname.", "zh_CN": "通过搜索关键字匹配加速域名进行过滤。"}
        self.search = search
        # {"en" : "Enum: all,staging,production 
        # Default: all 
        # The value can be 'all', 'staging', or 'production' to filter the results based on where the hostnames have been deployed. 
        # ", "zh_CN": "取值范围: all,staging,production 
        # 默认值: all 
        # 根据加速域名的部署环境过滤。该值可以是'all', 'staging', 或'production'，分别表示所有环境，演练环境和生产环境。"}
        self.target = target
        # {"en" : "Default: 0 Range: >= 0 
        # Index of the first hostname to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: [ 1 .. 10000 ] 
        # Maximum number of hostnames to return.", "zh_CN": "默认值: 100 取值范围: <= 10000 
        # 每次查询的最大条数。"}
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.search is not None:
            result['search'] = self.search
        if self.target is not None:
            result['target'] = self.target
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class GetHistoricalInformationAboutHostnamesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutHostnamesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutHostnamesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHistoricalInformationAboutHostnamesResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        hostnames: List[str] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of historical hostnames. This may be larger than number actually returned.", "zh_CN": "取值范围: >= 0 
        # 历史加速域名的总数。"}
        self.count = count
        # {"en" : "List of hostnames that were deployed during the timeframe.", "zh_CN": "在指定时间段内部署到生产环境过的加速域名列表。"}
        self.hostnames = hostnames

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self






class GetInformationAboutASpecificHostnamePaths(TeaModel):
    def __init__(
        self,
        hostname: str = None,
    ):
        # {"en" : "Hostname to fetch information about.", "zh_CN": "加速域名。"}
        self.hostname = hostname

    def validate(self):
        self.validate_required(self.hostname, 'hostname')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        return self


class GetInformationAboutASpecificHostnameParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetInformationAboutASpecificHostnameRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetInformationAboutASpecificHostnameRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetInformationAboutASpecificHostnameResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetInformationAboutASpecificHostnameResponse(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        property_in_production: str = None,
        property_in_staging: str = None,
    ):
        # {"en" : "A hostname whose property has been deployed to production or staging.", "zh_CN": "加速域名。"}
        self.hostname = hostname
        # {"en" : "Describes the property deployed to production. It can be 'null' if the property is not deployed to production.", "zh_CN": "如果加速域名对应的加速项目已部署到生产环境，则该字段返回该加速项目的相关信息。如果加速项目未部署到生产环境，则该字段返回'null'。"}
        self.property_in_production = property_in_production
        # {"en" : "Describes the property deployed to staging. It can be 'null' if the property is not deployed to staging.", "zh_CN": "如果加速域名对应的加速项目已部署到演练环境，则该字段返回该加速项目的相关信息。如果加速项目未部署到演练环境，则该字段返回'null'。"}
        self.property_in_staging = property_in_staging

    def validate(self):
        self.validate_required(self.hostname, 'hostname')
        self.validate_required(self.property_in_production, 'property_in_production')
        self.validate_required(self.property_in_staging, 'property_in_staging')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.property_in_production is not None:
            result['propertyInProduction'] = self.property_in_production
        if self.property_in_staging is not None:
            result['propertyInStaging'] = self.property_in_staging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('propertyInProduction') is not None:
            self.property_in_production = m.get('propertyInProduction')
        if m.get('propertyInStaging') is not None:
            self.property_in_staging = m.get('propertyInStaging')
        return self






class QueryNgHostNameAndEdgeHostNameForWplusRequest(TeaModel):
    def __init__(
        self,
        host_names: List[str] = None,
        edge_host_names: List[str] = None,
    ):
        # {"en":"Host Name", "zh_CN":"cdnpro加速域名"}
        self.host_names = host_names
        # {"en":"Edge Host Names", "zh_CN":"真实服务域名"}
        self.edge_host_names = edge_host_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_names is not None:
            result['hostNames'] = self.host_names
        if self.edge_host_names is not None:
            result['edgeHostNames'] = self.edge_host_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostNames') is not None:
            self.host_names = m.get('hostNames')
        if m.get('edgeHostNames') is not None:
            self.edge_host_names = m.get('edgeHostNames')
        return self


class QueryNgHostNameAndEdgeHostNameForWplusResponseData(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        edge_host_name: str = None,
    ):
        # {"en":"Host Name", "zh_CN":"cdnpro加速域名"}
        self.host_name = host_name
        # {"en":"Edge Host Names", "zh_CN":"真实服务域名"}
        self.edge_host_name = edge_host_name

    def validate(self):
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.edge_host_name, 'edge_host_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.edge_host_name is not None:
            result['edgeHostName'] = self.edge_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('edgeHostName') is not None:
            self.edge_host_name = m.get('edgeHostName')
        return self


class QueryNgHostNameAndEdgeHostNameForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryNgHostNameAndEdgeHostNameForWplusResponseData] = None,
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
                temp_model = QueryNgHostNameAndEdgeHostNameForWplusResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryNgHostNameAndEdgeHostNameForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryNgHostNameAndEdgeHostNameForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryNgHostNameAndEdgeHostNameForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryNgHostNameAndEdgeHostNameForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




