# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetASummaryOfTrafficBandwidthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficBandwidthParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z. Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: http https all 
        # Default: all 
        # Limit the results to the specified scheme. By default, all traffic is returned.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfTrafficBandwidthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficBandwidthRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetASummaryOfTrafficBandwidthRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfTrafficBandwidthRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters
        # {"en" : "<= 2 items 
        # You can group results using a combination of up to two of the following: 'hostnames', 'serverGroups', and 'customerIds'.", "zh_CN": "<= 2 条目 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfTrafficBandwidthRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfTrafficBandwidthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficBandwidthResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "返回最多10000个分组的数据。如果实际组数超过10000，则isComplete将为false。"}
        self.is_complete = is_complete
        # {"en" : "Indicates the type of data returned. 'edge bandwidth' represents edge bandwidth traffic. ", "zh_CN": "表示返回的数据类型。'edge bandwidth'指边缘带宽。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "表示返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.is_complete, 'is_complete')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfTrafficBandwidthResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of a group.  '__all__' is a special group encompassing all groups.", "zh_CN": "分组名称。'__all__' 是一个特殊分组，表示总带宽。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "每个分组的带宽值。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfTrafficBandwidthResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfTrafficBandwidthResponseMetaData = None,
        groups: List[GetASummaryOfTrafficBandwidthResponseGroups] = None,
    ):
        # {"en" : "Metadata that describes the data in the response.", "zh_CN": "对响应体中的报表数据的相关说明。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of traffic by group. Groups are determined by the request body.", "zh_CN": "每个分组及其带宽。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfTrafficBandwidthResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfTrafficBandwidthResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetEdgeHostnameSummaryStatisticsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameSummaryStatisticsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-11-14T00:00:00Z", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time span. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z. Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        return self


class GetEdgeHostnameSummaryStatisticsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameSummaryStatisticsRequestFilters(TeaModel):
    def __init__(
        self,
        edge_hostnames: List[str] = None,
    ):
        # {"en" : "One or more edge hostnames.", "zh_CN": "指定一个或多个调度域名进行查询。"}
        self.edge_hostnames = edge_hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostnames is not None:
            result['edgeHostnames'] = self.edge_hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnames') is not None:
            self.edge_hostnames = m.get('edgeHostnames')
        return self


class GetEdgeHostnameSummaryStatisticsRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeHostnameSummaryStatisticsRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "Limit statistics to specific edge hostnames.
        # ", "zh_CN": "指定查询范围。"}
        self.filters = filters
        # {"en" : "Specify an array containing 'edgeHostnames' to get data for each edge hostname. Omit to get only a cumulative total.", "zh_CN": "指定edgeHostnames，按调度域名分组汇总返回数据。如未指定，则只返回所有调度域名的汇总数据。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeHostnameSummaryStatisticsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetEdgeHostnameSummaryStatisticsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameSummaryStatisticsResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "该接口最多返回10000个分组的数据。如果实际分组数量大于10000，则isComplete的值将为false。"}
        self.is_complete = is_complete
        # {"en" : "Indicates the type of data returned: 'edgeHostname dns request'", "zh_CN": "返回的数据类型，即调度域名DNS解析请求数。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.is_complete, 'is_complete')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetEdgeHostnameSummaryStatisticsResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of a group.  '__all__' is a special group encompassing all groups.
        # ", "zh_CN": "分组名称。'__all__' 是一个特殊分组，包含其它所有分组的数据。"}
        self.group = group
        # {"en" : "Data value. The units of measurement are determined by the dataUnit field.", "zh_CN": "DNS解析请求数。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeHostnameSummaryStatisticsResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetEdgeHostnameSummaryStatisticsResponseMetaData = None,
        groups: List[GetEdgeHostnameSummaryStatisticsResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of DNS requests by group. Groups are determined by the request body.", "zh_CN": "按调度域名分组汇总的数据。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetEdgeHostnameSummaryStatisticsResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetEdgeHostnameSummaryStatisticsResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetOriginStatusCodeDetailsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginStatusCodeDetailsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetOriginStatusCodeDetailsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginStatusCodeDetailsRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetOriginStatusCodeDetailsRequest(TeaModel):
    def __init__(
        self,
        filters: GetOriginStatusCodeDetailsRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetOriginStatusCodeDetailsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetOriginStatusCodeDetailsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginStatusCodeDetailsResponseDataSeriesDetails(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        data: int = None,
    ):
        # {"en" : "Indicates an HTTP status code, for example, '200'.", "zh_CN": "HTTP状态码，例如'200'。"}
        self.status_code = status_code
        # {"en" : "Range: >= 0 
        # Indicates the number of times the status code was returned.", "zh_CN": "取值范围: >= 0 
        # 状态码出现的次数。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetOriginStatusCodeDetailsResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        details: List[GetOriginStatusCodeDetailsResponseDataSeriesDetails] = None,
    ):
        # {"en" : "RFC 3339 format date indicate the beginning of an interval.", "zh_CN": "RFC 3339格式的日期，表示每个时间段的开始时间。"}
        self.timestamp = timestamp
        # {"en" : "", "zh_CN": ""}
        self.details = details

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = GetOriginStatusCodeDetailsResponseDataSeriesDetails()
                self.details.append(temp_model.from_map(k))
        return self


class GetOriginStatusCodeDetailsResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetOriginStatusCodeDetailsResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Enum: counts 
        # Unit of measurement.  For status code APIs, it will be 'counts', which indicates the number of times a status code appears.", "zh_CN": "取值范围: counts 
        # 计量单位。对于状态码报表接口，单位为'次数'，表示某个状态码出现的次数。"}
        self.data_unit = data_unit
        # {"en" : "Contains information about status codes at different points in time.", "zh_CN": "不同时间点的状态码统计信息。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetOriginStatusCodeDetailsResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetEdgeBandwidthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeBandwidthParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes hourly daily monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes, hourly, daily, monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "[ 0 .. 5 ] characters 
        # Enum: http https all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetEdgeBandwidthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeBandwidthRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Enum: standard premium deluxe ultra 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard, premium, deluxe, ultra 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetEdgeBandwidthRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeBandwidthRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeBandwidthRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetEdgeBandwidthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeBandwidthResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeBandwidthResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetEdgeBandwidthResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetEdgeBandwidthResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetEdgeStatusCodeDetailsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeStatusCodeDetailsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetEdgeStatusCodeDetailsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeStatusCodeDetailsRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetEdgeStatusCodeDetailsRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeStatusCodeDetailsRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeStatusCodeDetailsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetEdgeStatusCodeDetailsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeStatusCodeDetailsResponseDataSeriesDetails(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        data: int = None,
    ):
        # {"en" : "Indicates an HTTP status code, for example, '200'.", "zh_CN": "HTTP状态码，例如'200'。"}
        self.status_code = status_code
        # {"en" : "Range: >= 0 
        # Indicates the number of times the status code was returned.", "zh_CN": "取值范围: >= 0 
        # 状态码出现的次数。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeStatusCodeDetailsResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        details: List[GetEdgeStatusCodeDetailsResponseDataSeriesDetails] = None,
    ):
        # {"en" : "RFC 3339 format date indicate the beginning of an interval.", "zh_CN": "RFC 3339格式的日期，表示每个时间段的开始时间。"}
        self.timestamp = timestamp
        # {"en" : "", "zh_CN": ""}
        self.details = details

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = GetEdgeStatusCodeDetailsResponseDataSeriesDetails()
                self.details.append(temp_model.from_map(k))
        return self


class GetEdgeStatusCodeDetailsResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetEdgeStatusCodeDetailsResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Enum: counts 
        # Unit of measurement.  For status code APIs, it will be 'counts', which indicates the number of times a status code appears.", "zh_CN": "取值范围: counts 
        # 计量单位。对于状态码报表接口，单位为'次数'，表示某个状态码出现的次数。"}
        self.data_unit = data_unit
        # {"en" : "Contains information about status codes at different points in time.", "zh_CN": "不同时间点的状态码统计信息。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetEdgeStatusCodeDetailsResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetTheNumberOfRequestsToOriginPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheNumberOfRequestsToOriginParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetTheNumberOfRequestsToOriginRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheNumberOfRequestsToOriginRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetTheNumberOfRequestsToOriginRequest(TeaModel):
    def __init__(
        self,
        filters: GetTheNumberOfRequestsToOriginRequestFilters = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetTheNumberOfRequestsToOriginRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetTheNumberOfRequestsToOriginResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheNumberOfRequestsToOriginResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetTheNumberOfRequestsToOriginResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetTheNumberOfRequestsToOriginResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetTheNumberOfRequestsToOriginResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetEdgeHostnameStatisticsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameStatisticsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-11-14T00:00:00Z", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time span. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-11-14T00:00:00Z。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetEdgeHostnameStatisticsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameStatisticsRequestFilters(TeaModel):
    def __init__(
        self,
        edge_hostnames: List[str] = None,
    ):
        # {"en" : "One or more edge hostnames.", "zh_CN": "一个或多个调度域名。"}
        self.edge_hostnames = edge_hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostnames is not None:
            result['edgeHostnames'] = self.edge_hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnames') is not None:
            self.edge_hostnames = m.get('edgeHostnames')
        return self


class GetEdgeHostnameStatisticsRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeHostnameStatisticsRequestFilters = None,
    ):
        # {"en" : "Limit statistics to specific edge hostnames.", "zh_CN": "指定调度域名进行查询。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeHostnameStatisticsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetEdgeHostnameStatisticsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeHostnameStatisticsResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeHostnameStatisticsResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetEdgeHostnameStatisticsResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetEdgeHostnameStatisticsResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetCpuTimeUsedPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCpuTimeUsedParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14. For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetCpuTimeUsedRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCpuTimeUsedRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "One or more server groups for which to return data. If unspecified, data for all server groups will be returned.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetCpuTimeUsedRequest(TeaModel):
    def __init__(
        self,
        filters: GetCpuTimeUsedRequestFilters = None,
    ):
        # {"en" : "Filter results by specifying hostnames or server groups.", "zh_CN": "Filter results by specifying hostnames or server groups."}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetCpuTimeUsedRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetCpuTimeUsedResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCpuTimeUsedResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetCpuTimeUsedResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetCpuTimeUsedResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetCpuTimeUsedResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetASummaryOfRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfRequestsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z. Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: http https all 
        # Default: all 
        # Limit the results to the specified scheme. By default, data from HTTPS and HTTP requests is returned.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfRequestsRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetASummaryOfRequestsRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfRequestsRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters
        # {"en" : "<= 2 items 
        # items Enum: hostnames, serverGroups 
        # You can group results using a combination of up to two of the following: 'hostnames', and 'serverGroups'.", "zh_CN": "<= 2 条目 
        # 取值范围: hostnames, serverGroups 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfRequestsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfRequestsResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "该接口最多返回10000个分组的数据。如果实际分组数量大于10000，则isComplete将为false。"}
        self.is_complete = is_complete
        # {"en" : "Indicates the type of data returned. 'edge request' represents edge traffic. 'fast route request' refers to traffic from your origin accelerated through the HDT product. 'origin request' represents origin traffic. 'intermediate request' represents intermediate traffic. The order of the entries in dataNames array corresponds to the order of values returned in the data data array in the response.", "zh_CN": "表示返回的数据类型。'edge request'表示边缘请求数，'fast route request'表示快速回源请求数，'origin request'表示回源请求数，'intermediate request'表示回父节点的请求数。dataNames数组中条目的顺序与groups[].data中返回值的顺序一一对应。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.is_complete, 'is_complete')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfRequestsResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of a group.  '__all__' is a special group encompassing all groups.", "zh_CN": "分组名称。'__all__' 是一个特殊分组，表示总请求数。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "每个分组的请求数。注意：当分组条件包含serverGroups时，极个别情况下，可能会出现'__all__' 组的值明显大于其它组累加的和。这是由于存在未知原因导致某些请求无法映射到serverGroup所致。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfRequestsResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfRequestsResponseMetaData = None,
        groups: List[GetASummaryOfRequestsResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of requests by group.", "zh_CN": "每个分组及其请求数。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfRequestsResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfRequestsResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetOriginFastRouteRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteRequestsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetOriginFastRouteRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteRequestsRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetOriginFastRouteRequestsRequest(TeaModel):
    def __init__(
        self,
        filters: GetOriginFastRouteRequestsRequestFilters = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetOriginFastRouteRequestsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetOriginFastRouteRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteRequestsResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetOriginFastRouteRequestsResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetOriginFastRouteRequestsResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetOriginFastRouteRequestsResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetASummaryOfTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time span. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-10-30T00:00:00Z. Due to latency associated with processing new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: http,https 
        # Limit the results to the specified scheme.", "zh_CN": "取值范围: http,https 
        # 指定协议进行查询。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
        property_ids: List[str] = None,
        property_hostnames: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups
        # {"en" : "IDs of properties for which to return data. If unspecified, data for all properties will be returned.", "zh_CN": "指定加速项目ID进行查询。"}
        self.property_ids = property_ids
        # {"en" : "A list of property hostnames for which to return data. These correspond to values in the hostnames field of a property configuration. These can differ from the value sent in an HTTP request. For example, if you create a property to accelerate '*.test.com', a client could request content and pass a Host header of 'abc.test.com'. In this case, '*.test.com' is a property hostname you can filter by using this field while 'abc.test.com' is a hostname you can filter by using the hostnames field. By default, data for all property hostnames is returned.", "zh_CN": "指定加速域名进行查询。上述hostnames参数将匹配用户请求时访问的hostnames进行查询，而此处的propertyHostnames将匹配加速项目中定义的hostnames进行查询。当加速项目中定义的域名包含泛域名，可使用propertyHostnames参数进行查询。"}
        self.property_hostnames = property_hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        if self.property_ids is not None:
            result['propertyIds'] = self.property_ids
        if self.property_hostnames is not None:
            result['propertyHostnames'] = self.property_hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        if m.get('propertyIds') is not None:
            self.property_ids = m.get('propertyIds')
        if m.get('propertyHostnames') is not None:
            self.property_hostnames = m.get('propertyHostnames')
        return self


class GetASummaryOfTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfTrafficVolumeRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters
        # {"en" : "Range: <= 2 items 
        # You can group results using a combination of up to two of the following: 'hostnames', 'serverGroups',  'customerIds', 'propertyIds', and 'propertyHostnames'.", "zh_CN": "取值范围: <= 2 条目 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfTrafficVolumeResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "该接口最多返回10000个分组的数据。如果实际分组数量大于10000，则isComplete值为false。"}
        self.is_complete = is_complete
        # {"en" : "Indicates the type of data returned. 
        # <table><tr><th>Data Name</th><th>Description</th></tr><tr><td>edge response</td><td>edge traffic to visitors</td></tr><tr><td>edge request</td><td>traffic from visitors to edge servers</td></tr><tr><td>intermediate response</td><td>traffic from intermediate CDN Pro servers to other CDN Pro servers</td></tr><tr><td>intermediate request</td><td>traffic of requests to intermediate CDN Pro servers</td></tr><tr><td>origin response</td><td>traffic from origin servers</td></tr><tr><td>origin request</td><td>traffic to origin servers</td></tr><tr><td>fast route response</td><td>traffic from your origin accelerated through the HDT product</td></tr><tr><td>fast route request</td><td>traffic to your origin accelerated through the HDT product</td></tr></table>
        # The order of the entries in dataNames array corresponds to the order of values returned in the data data array in the response.", "zh_CN": "返回的数据类型。<table><tr><th>数据名称</th><th>描述</th></tr><tr><td>edge response</td><td>边缘服务器的响应流量</td></tr><tr><td>edge request</td><td>从访客到边缘服务器的请求流量</td></tr><tr><td>intermediate response</td><td>CDN Pro中间层服务器的响应流量</td></tr><tr><td>intermediate request</td><td>发往CDN Pro中间层服务器的请求流量</td></tr><tr><td>origin response</td><td>源站的响应流量</td></tr><tr><td>origin request</td><td>回源的请求流量</td></tr><tr><td>fast route response</td><td>快速回源产生的响应流量</td></tr><tr><td>fast route request</td><td>快速回源产生的请求流量</td></tr></table>
        # dataNames数组中条目的顺序与groups[].data数组返回值的顺序一一对应。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "指示返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfTrafficVolumeResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of the group. '__all__' is a special group encompassing all groups.
        # ", "zh_CN": "分组名称。'__all__' 是一个特殊分组，表示总流量。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "每个分组的流量值。注意：每个分组的值，是将每个分组各自查询得到的数据按保留小数点后5位、四舍五入处理后得到的结果。'__all__' 组的值也是按这种方式得到的结果，而不是将其它分组的值直接累加得出和。如果发现'__all__' 组的值不完全等于其他组的值累加的和，属于预期内的结果。此外，当分组条件包含serverGroups时，极个别情况下，可能会出现'__all__' 组的值明显大于其它组累加的和。这是由于存在未知原因导致某些流量无法映射到serverGroup所致。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfTrafficVolumeResponseMetaData = None,
        groups: List[GetASummaryOfTrafficVolumeResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of traffic by group. ", "zh_CN": "每个分组及其流量值。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfTrafficVolumeResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfTrafficVolumeResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetTheEdgeUploadTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheEdgeUploadTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetTheEdgeUploadTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheEdgeUploadTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "items Enum: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetTheEdgeUploadTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetTheEdgeUploadTrafficVolumeRequestFilters = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetTheEdgeUploadTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetTheEdgeUploadTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheEdgeUploadTrafficVolumeResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetTheEdgeUploadTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetTheEdgeUploadTrafficVolumeResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetTheEdgeUploadTrafficVolumeResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetASummaryOfStatusCodesReturnedByEdgeServersPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2021-09-05T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2021-09-05T10:00:00Z Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: http,https,all 
        # Default: all 
        # Limit the results to the specified scheme. By default, data from HTTPS and HTTP requests is returned.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfStatusCodesReturnedByEdgeServersRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters
        # {"en" : "Range: <= 2 items 
        # You can group results using any combination of up to two of 'hostnames', 'serverGroups', and 'customerIds'.", "zh_CN": "取值范围: <= 2 条目 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfStatusCodesReturnedByEdgeServersRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "返回最多10000个分组的数据。如果实际组数超过10000，则isComplete将为false。"}
        self.is_complete = is_complete
        # {"en" : "A list of HTTP status codes represented as strings. The order of the entries in the dataNames array corresponds to the order of values returned in the data array in the response.", "zh_CN": "HTTP状态码列表。dataNames数组中条目的顺序与groups[].data中返回值的顺序一一对应。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "表示返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.is_complete, 'is_complete')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of a group.  '__all__' is a special group encompassing all groups.", "zh_CN": "分组名称。'__all__' 是一个特殊分组，表示每个状态码的总数。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "每个分组的状态码数量。注意：当分组条件包含serverGroups时，极个别情况下，可能会出现'__all__' 组的值明显大于其它组累加的和。这是由于存在未知原因导致某些请求无法映射到serverGroup所致。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfStatusCodesReturnedByEdgeServersResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfStatusCodesReturnedByEdgeServersResponseMetaData = None,
        groups: List[GetASummaryOfStatusCodesReturnedByEdgeServersResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of requests by group.", "zh_CN": "每个分组及其状态码。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfStatusCodesReturnedByEdgeServersResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfStatusCodesReturnedByEdgeServersResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetOriginFastRouteTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes, hourly, daily, monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetOriginFastRouteTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Enum: standard premium deluxe ultra 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard, premium, deluxe, ultra 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetOriginFastRouteTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetOriginFastRouteTrafficVolumeRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetOriginFastRouteTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetOriginFastRouteTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginFastRouteTrafficVolumeResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data_up: int = None,
        data_down: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of  a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "RFC 3339格式的日期，表示每个时间段的开始时间，始终采用<b>UTC</b>时间。例如：'timestamp':'2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "Default: 0 >= 0 
        # Indicates the amount of traffic in megabytes uploaded to the origin using the fast route feature.", "zh_CN": "默认值: 0 取值范围 >= 0 
        # 表示通过快速回源传输的上行流量（以MB为单位）。"}
        self.data_up = data_up
        # {"en" : "Default: 0 >= 0 
        # Indicates the amount of traffic in megabytes downloaded from the origin using the fast route feature.", "zh_CN": "默认值: 0 取值范围 >= 0 
        # 表示通过快速回源传输的下行流量（以MB为单位）。"}
        self.data_down = data_down

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data_up is not None:
            result['dataUp'] = self.data_up
        if self.data_down is not None:
            result['dataDown'] = self.data_down
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('dataUp') is not None:
            self.data_up = m.get('dataUp')
        if m.get('dataDown') is not None:
            self.data_down = m.get('dataDown')
        return self


class GetOriginFastRouteTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetOriginFastRouteTrafficVolumeResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Default: megabytes 
        # Unit of measurement.", "zh_CN": "默认值: megabytes 
        # 计量单位。"}
        self.data_unit = data_unit
        # {"en" : "The data points for the time period include the upload and download traffic.", "zh_CN": "指定时间段的流量，包括上行和下行流量。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetOriginFastRouteTrafficVolumeResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetEdgeRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeRequestsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter endtdate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes hourly daily monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes, hourly, daily, monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "[ 0 .. 5 ] characters 
        # Enum: http https all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetEdgeRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeRequestsRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "items Enum: standard premium deluxe ultra nearChina ChinaStandard ChinaPremium 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard, premium, deluxe, ultra, nearChina, ChinaStandard, ChinaPremium 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetEdgeRequestsRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeRequestsRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeRequestsRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetEdgeRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeRequestsResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeRequestsResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetEdgeRequestsResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetEdgeRequestsResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetASummaryOfStatusCodesReturnedByOriginServersPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2021-09-05T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2021-09-05T10:00:00Z Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: http,https,all 
        # Default: all 
        # Limit the results to the specified scheme. By default, data from HTTPS and HTTP requests is returned.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfStatusCodesReturnedByOriginServersRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters
        # {"en" : "Range: <= 2 items 
        # You can group results using a combination of up to two of the following: 'hostnames', 'serverGroups', and 'customerIds'.", "zh_CN": "取值范围: <= 2 条目 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfStatusCodesReturnedByOriginServersRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "返回最多10000个分组的数据。如果实际组数超过10000，则isComplete将为false。"}
        self.is_complete = is_complete
        # {"en" : "A list of HTTP status codes represented as strings. The order of the entries in the dataNames array corresponds to the order of values returned in the data array in the response.", "zh_CN": "HTTP状态码列表。dataNames数组中条目的顺序与groups[].data中返回值的顺序一一对应。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "表示返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.is_complete, 'is_complete')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of a group.  '__all__' is a special group encompassing all groups.", "zh_CN": "分组名称。'__all__' 是一个特殊分组，包含其它所有分组的数据。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "状态码数量。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfStatusCodesReturnedByOriginServersResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfStatusCodesReturnedByOriginServersResponseMetaData = None,
        groups: List[GetASummaryOfStatusCodesReturnedByOriginServersResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of requests by group.", "zh_CN": "分组汇总数据。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfStatusCodesReturnedByOriginServersResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfStatusCodesReturnedByOriginServersResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self






class GetOriginTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14. For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetOriginTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "items Enum: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetOriginTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetOriginTrafficVolumeRequestFilters = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetOriginTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetOriginTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOriginTrafficVolumeResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetOriginTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetOriginTrafficVolumeResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetOriginTrafficVolumeResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetTheIntermediateTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheIntermediateTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes,hourly,daily,monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14.  For example, type=daily+8  means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes,hourly,daily,monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "Range: [ 0 .. 5 ] characters 
        # Enum: http,https,all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetTheIntermediateTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheIntermediateTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "items Enum: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard,premium,deluxe,ultra,nearChina,ChinaStandard,ChinaPremium 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetTheIntermediateTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetTheIntermediateTrafficVolumeRequestFilters = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetTheIntermediateTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetTheIntermediateTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTheIntermediateTrafficVolumeResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetTheIntermediateTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetTheIntermediateTrafficVolumeResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetTheIntermediateTrafficVolumeResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetEdgeTrafficVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeTrafficVolumeParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        type: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z Your startdate may be rounded down to the nearest minute, hour, or day depending on the type parameter. For example, if you enter startdate=2019-09-05T03:14:01Z&type=hourly, the response includes data beginning 2019-09-05T03:00:00Z.", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 根据type参数对应的粒度，您指定的开始时间可能被向前取整为最近的分钟、小时或天。例如，如果您指定 startdate=2019-09-05T03:14:01Z&type=hourly，则返回从2019-09-05T03:00:00Z开始的数据。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-11-14T00:00:00Z Your enddate may be rounded up to the nearest minute, hour, or day depending on the type parameter. For example, if you enter enddate=2019-09-05T03:14:01Z&type=hourly, the response includes data ending 2019-09-05T04:00:00Z.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。根据type参数对应的粒度，您指定的结束时间可能被向后取整为最近的分钟、小时或天。例如，如果您指定 enddate=2019-09-05T03:14:01Z&type=hourly，则返回截止到2019-09-05T04:00:00Z的数据。"}
        self.enddate = enddate
        # {"en" : "Enum: fiveminutes hourly daily monthly 
        # Indicates the granularity of returned data. By default, 00:00:00 in UTC is used as the beginning of a day. If you wish to use a different offset from UTC, you can append -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, +1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13, +14. For example, type=daily+8 means the day as defined in UTC+8 time.", "zh_CN": "取值范围: fiveminutes, hourly, daily, monthly 
        # 指定返回数据的粒度，支持5分钟，小时，日，月粒度。默认情况下，我们以UTC 00:00:00作为一天的开始。如果您希望指定不同的时区，可以附加时区标识，即-12、-11、-10、-9、-8、-7、-6、-5、-4、-3、-2、-1、+1、+2、+3、+4、+5、+6、+7、+8、+9、+10、+11、+12。例如，type=daily+8表示使用UTC+8时区指定一天的开始时间。"}
        self.type = type
        # {"en" : "[ 0 .. 5 ] characters 
        # Enum: http https all 
        # Default: all 
        # Choose whether to include HTTP and HTTPS traffic in the results. The default 'all' includes both types of traffic.", "zh_CN": "[ 0 .. 5 ] 字符 
        # 取值范围: http, https, all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.type is not None:
            result['type'] = self.type
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetEdgeTrafficVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeTrafficVolumeRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "items Enum: standard premium deluxe ultra nearChina ChinaStandard ChinaPremium 
        # Indicates one or more server groups.", "zh_CN": "取值范围: standard, premium, deluxe, ultra, nearChina, ChinaStandard, ChinaPremium 
        # 指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetEdgeTrafficVolumeRequest(TeaModel):
    def __init__(
        self,
        filters: GetEdgeTrafficVolumeRequestFilters = None,
    ):
        # {"en" : "Specify conditions to filter report data.", "zh_CN": "指定查询条件过滤报表数据。"}
        self.filters = filters

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetEdgeTrafficVolumeRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetEdgeTrafficVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetEdgeTrafficVolumeResponseDataSeries(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data: int = None,
    ):
        # {"en" : "An RFC 3339 format date representing the beginning of a time interval. It is always in <b>UTC</b> time. For example:  'timestamp': '2019-10-29T01:00:00Z'", "zh_CN": "每个时间段的起始时间，以RFC 3339日期格式表示。始终采用UTC时区。例如：'timestamp': '2019-10-29T01:00:00Z'"}
        self.timestamp = timestamp
        # {"en" : "A value at that timestamp. Refer to the dataUnit field for the unit of measurement.", "zh_CN": "该时间段对应的值。计量单位，由dataUnit字段指定。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetEdgeTrafficVolumeResponse(TeaModel):
    def __init__(
        self,
        data_name: str = None,
        data_unit: str = None,
        data_series: List[GetEdgeTrafficVolumeResponseDataSeries] = None,
    ):
        # {"en" : "A brief description of the data.", "zh_CN": "对返回数据的简要描述。"}
        self.data_name = data_name
        # {"en" : "Unit of measurement. This will depend on the report API.", "zh_CN": "计量单位。不同报表类型计量单位不一样。"}
        self.data_unit = data_unit
        # {"en" : "The data points.", "zh_CN": "数据点。"}
        self.data_series = data_series

    def validate(self):
        self.validate_required(self.data_name, 'data_name')
        self.validate_required(self.data_unit, 'data_unit')
        self.validate_required(self.data_series, 'data_series')
        if self.data_series:
            for k in self.data_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_name is not None:
            result['dataName'] = self.data_name
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        if self.data_series is not None:
            result['dataSeries'] = []
            for k in self.data_series:
                result['dataSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataName') is not None:
            self.data_name = m.get('dataName')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        if m.get('dataSeries') is not None:
            self.data_series = []
            for k in m.get('dataSeries'):
                temp_model = GetEdgeTrafficVolumeResponseDataSeries()
                self.data_series.append(temp_model.from_map(k))
        return self






class GetASummaryOfCpuUsagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfCpuUsageParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        scheme: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-11-14T00:00:00Z", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2021-09-05T10:00:00Z Due to latency associated with new traffic data, enddate should be no later than five minutes before the current time. This ensures you get the most accurate results.", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。由于数据处理存在延迟，所指定的结束时间必须至少比当前时间早5分钟，否则返回的数据可能不准确。"}
        self.enddate = enddate
        # {"en" : "Enum: all,http,https 
        # Default: all 
        # Limit the results to the specified scheme. By default, data from HTTPS and HTTP requests is returned.", "zh_CN": "取值范围: [ 0 .. 5 ] 字符 
        # 取值范围: http,https,all 
        # 默认值: all 
        # 指定查询HTTP与/或HTTPS协议的数据。默认查询全部2种协议的数据。"}
        self.scheme = scheme

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
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class GetASummaryOfCpuUsageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfCpuUsageRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        server_groups: List[str] = None,
    ):
        # {"en" : "List of hostnames for which to return data. Wildcard hostnames such as *.domain.com are also permitted. If unspecified, data from all hostnames will be returned.", "zh_CN": "指定加速域名进行查询。可使用泛域名，如*.domain.com。如果未指定，将返回所有加速域名的数据。"}
        self.hostnames = hostnames
        # {"en" : "Indicates one or more server groups.", "zh_CN": "指定serverGroups（节点组）进行查询。"}
        self.server_groups = server_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.server_groups is not None:
            result['serverGroups'] = self.server_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('serverGroups') is not None:
            self.server_groups = m.get('serverGroups')
        return self


class GetASummaryOfCpuUsageRequest(TeaModel):
    def __init__(
        self,
        filters: GetASummaryOfCpuUsageRequestFilters = None,
        group_by: List[str] = None,
    ):
        # {"en" : "", "zh_CN": ""}
        self.filters = filters
        # {"en" : "Range: <= 2 items 
        # You can group results using a combination of up to two of the following: 'hostnames', 'serverGroups'", "zh_CN": "取值范围: <= 2 条目 
        # 指定分组依据对数据进行分组汇总。支持按'hostnames'，'serverGroups'单独进行分组汇总，也支持同时指定这2个参数进行分组汇总。"}
        self.group_by = group_by

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['filters'] = self.filters.to_map()
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filters') is not None:
            temp_model = GetASummaryOfCpuUsageRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetASummaryOfCpuUsageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASummaryOfCpuUsageResponseMetaData(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        is_complete: bool = None,
        data_names: List[str] = None,
        data_unit: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的起始时间。"}
        self.start_time = start_time
        # {"en" : "RFC 3339 date indicating the end of the period.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。"}
        self.end_time = end_time
        # {"en" : "The response can contain up to 10000 groups. If there are more groups, isComplete will be false.", "zh_CN": "该接口最多返回10000个分组的数据。如果实际分组数量大于10000，则isComplete将为false。"}
        self.is_complete = is_complete
        # {"en" : "Indicates the type of data returned. 
        # <table><tr><th>Data Name</th><th>Description</th></tr><tr><td>edge cpu time</td><td>CPU usage by edge servers</td></tr><tr><td>intermediate cpu time</td><td>CPU usage by intermediate CDN Pro servers</td></tr></table>
        # The order of the entries in dataNames array corresponds to the order of values returned in the data data array in the response.", "zh_CN": "表示返回的数据类型。
        # <table><tr><th>数据名称</th><th>描述</th></tr><tr><td>edge cpu time</td><td>边缘服务器的CPU使用时间</td></tr><tr><td>intermediate cpu time</td><td>中间层服务器的CPU使用时间</td></tr></table>
        # dataNames数组中条目的顺序与groups[].data中返回值的顺序一一对应。"}
        self.data_names = data_names
        # {"en" : "Indicates the unit of measurement of the returned values.", "zh_CN": "表示返回值的计量单位。"}
        self.data_unit = data_unit

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.is_complete, 'is_complete')
        self.validate_required(self.data_names, 'data_names')
        self.validate_required(self.data_unit, 'data_unit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_complete is not None:
            result['isComplete'] = self.is_complete
        if self.data_names is not None:
            result['dataNames'] = self.data_names
        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isComplete') is not None:
            self.is_complete = m.get('isComplete')
        if m.get('dataNames') is not None:
            self.data_names = m.get('dataNames')
        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')
        return self


class GetASummaryOfCpuUsageResponseGroups(TeaModel):
    def __init__(
        self,
        group: str = None,
        data: List[str] = None,
    ):
        # {"en" : "Name of the group. '__all__' is a special group encompassing all groups.
        # ", "zh_CN": "分组名称。'__all__' 是一个特殊分组，表示总cpu时间。"}
        self.group = group
        # {"en" : "Data values. The units of measurement are determined by the dataUnit field.", "zh_CN": "每个分组的cpu时间。注意：每个分组的值，是将每个分组各自查询得到的数据按保留小数点后5位、四舍五入处理后得到的结果。'__all__' 组的值也是按这种方式得到的结果，而不是将其它分组的值直接累加得出和。如果发现'__all__' 组的值不完全等于其他组的值累加的和，属于预期内的结果。此外，当分组条件包含serverGroups时，极个别情况下，可能会出现'__all__' 组的值明显大于其它组累加的和。这是由于存在未知原因导致某些请求无法映射到serverGroup所致。"}
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetASummaryOfCpuUsageResponse(TeaModel):
    def __init__(
        self,
        meta_data: GetASummaryOfCpuUsageResponseMetaData = None,
        groups: List[GetASummaryOfCpuUsageResponseGroups] = None,
    ):
        # {"en" : "This object contains fields describing the data returned in the groups object.", "zh_CN": "此对象包含的字段是对groups对象中返回数据的描述。"}
        self.meta_data = meta_data
        # {"en" : "This object contains the breakdown of CPU usage by group. ", "zh_CN": "每个分组及其cpu时间。"}
        self.groups = groups

    def validate(self):
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()
        self.validate_required(self.groups, 'groups')
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        if self.groups is not None:
            result['groups'] = []
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metaData') is not None:
            temp_model = GetASummaryOfCpuUsageResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        if m.get('groups') is not None:
            self.groups = []
            for k in m.get('groups'):
                temp_model = GetASummaryOfCpuUsageResponseGroups()
                self.groups.append(temp_model.from_map(k))
        return self




