# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteALogConfigurationPaths(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # {"en" : "ID of a log configuration", "zh_CN": "日志配置的id。"}
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


class DeleteALogConfigurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteALogConfigurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteALogConfigurationRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteALogConfigurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteALogConfigurationResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetAListOfLogConfigurationsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfLogConfigurationsParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        offset: int = None,
        limit: int = None,
    ):
        # {"en" : "Search for hostnames affected by the log configuration.", "zh_CN": "根据域名查询相关的日志配置。"}
        self.search = search
        # {"en" : "Range: >= 0 
        # Index of the first log configuration to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: [ 1 .. 200 ] 
        # Maximum number of log configurations to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class GetAListOfLogConfigurationsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfLogConfigurationsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfLogConfigurationsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfLogConfigurationsResponseLogConfigs(TeaModel):
    def __init__(
        self,
        log_config_id: int = None,
        hostnames: List[str] = None,
        description: str = None,
        last_update_time: str = None,
        creation_time: str = None,
    ):
        # {"en" : "An ID representating the log configuration. Use the ID to get, update, or delete the configuration later.", "zh_CN": "日志配置唯一标识ID。可用该ID查询，更新或删除日志配置。"}
        self.log_config_id = log_config_id
        # {"en" : "A list of hostnames to which the log configuration applies. A hostname should be a fully qualified domain name like domain.com, a wildcard domain name with a leading '*' like *.domain.com, or '*' if you want the log configuration to apply to all hostnames.", "zh_CN": "适用该日志配置的域名列表。每个域名必须是完整的FQDN域名如domain.com，或者是带星号的泛域名如*.domain.com。如果该日志配置适用于所有域名，则直接用星号*表示。"}
        self.hostnames = hostnames
        # {"en" : "A description of the log configuration.", "zh_CN": "日志配置描述信息。"}
        self.description = description
        # {"en" : "RFC 3339 date indicating when the log configuration was last updated.", "zh_CN": "日志配置最近一次更新时间，以RFC 3339日期格式展示。"}
        self.last_update_time = last_update_time
        # {"en" : "RFC 3339 date indicating when the log configuration was created.", "zh_CN": "日志配置创建时间，以RFC 3339日期格式展示。"}
        self.creation_time = creation_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_config_id is not None:
            result['logConfigId'] = self.log_config_id
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.description is not None:
            result['description'] = self.description
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logConfigId') is not None:
            self.log_config_id = m.get('logConfigId')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        return self


class GetAListOfLogConfigurationsResponse(TeaModel):
    def __init__(
        self,
        log_configs: List[GetAListOfLogConfigurationsResponseLogConfigs] = None,
        count: int = None,
    ):
        # {"en" : "List of log configurations.", "zh_CN": "日志配置列表。"}
        self.log_configs = log_configs
        # {"en" : "Range: >= 0 
        # Number of log configurations.", "zh_CN": "取值范围: >= 0 
        # 日志配置数量。"}
        self.count = count

    def validate(self):
        self.validate_required(self.log_configs, 'log_configs')
        if self.log_configs:
            for k in self.log_configs:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_configs is not None:
            result['logConfigs'] = []
            for k in self.log_configs:
                result['logConfigs'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logConfigs') is not None:
            self.log_configs = []
            for k in m.get('logConfigs'):
                temp_model = GetAListOfLogConfigurationsResponseLogConfigs()
                self.log_configs.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self






class CreateALogConfigurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateALogConfigurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateALogConfigurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateALogConfigurationRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        hostnames: List[str] = None,
        log_download_format: str = None,
        log_download_storage_days: int = None,
        log_download_file_span_minutes: int = None,
    ):
        # {"en" : "A description of the log configuration.", "zh_CN": "日志配置描述。"}
        self.description = description
        # {"en" : "A list of hostnames to which the log configuration applies. A hostname should be a fully qualified domain name like domain.com, a wildcard domain name with a leading '*' like *.domain.com, or '*' if you want the log configuration to apply to all hostnames. You should ensure that only one log configuration applies to each hostname.", "zh_CN": "适用该日志配置的域名列表。每个域名必须是完整的FQDN域名如domain.com，或者是带星号的泛域名如*.domain.com。如果该日志配置适用于所有域名，则直接用星号*表示。每个域名有且只能有一个对应的日志配置。"}
        self.hostnames = hostnames
        # {"en" : "Default: %cltip %rmtuser  [%utctime] '%method %url %protocol' %statuscode %rspsize '%referer' '%ua' %rsptime 
        # Format of the log entry. You can use the following variables to create a custom format:
        # <table><tr><th>Variable</th><th>Meaning</th></tr><tr><td>%cachestate</td><td>HIT, MISS, or REVALIDATE</td></tr><tr><td>%cltip</td><td>Client IP address</td></tr><tr><td>%cltisp</td><td>Client ISP</td></tr><tr><td>%cltport</td><td>Client port number</td></tr><tr><td>%cltregion</td><td>Client region</td></tr><tr><td>%cpu_ns</td><td>CPU time in nanoseconds for this request</td></tr><tr><td>%custom1</td><td>Refers to a custom log field with ID 1 you define using the custom_log_field directive.</td></tr>      <tr><td>%custom2</td><td>Refers to a custom log field with ID 2 you define using the custom_log_field directive.</td></tr>      <tr><td>%hostname</td><td>Host header</td></tr><tr><td>%method</td><td>HTTP method used to access the content, for example, GET</td></tr><tr><td>%protocol</td><td>HTTP/1.0 or HTTP/1.1 or HTTP2.0</td></tr><tr><td>%querystr</td><td>Query string</td></tr>      <tr><td>%referer</td><td>Referer request header</td></tr><tr><td>%reqhdrsize</td><td>Request header size in bytes</td></tr><tr><td>%reqrange</td><td>Range header in requests from client</td></tr><tr><td>%reqsize</td><td>Request size in bytes including the request line, header, and request body</td></tr><tr><td>%rmtuser</td><td>User name extracted from the Authorization header when basic authentication is used</td></tr><tr><td>%rspsize</td><td>HTTP response size, in bytes, including header and body, but not including TCP/IP/MAC</td></tr><tr><td>%rsptime</td><td>Response time in milliseconds</td></tr><tr><td>%samplerate</td><td>Number of requests corresponding to each log entry</td></tr><tr><td>%scheme</td><td>http or https</td></tr><tr><td>%statuscode</td><td>Response's status code, for example, 200</td></tr><tr><td>%srvip</td><td>IP address of the CDN server handling the request</td></tr><tr><td>%svrnode</td><td>Cache server node name</td></tr><tr><td>%tcprtt</td><td>Round-trip time between server and client in microseconds</td></tr>      <tr><td>%ua</td><td>User-Agent header</td></tr><tr><td>%uniqueid</td><td>A string uniquely identifying this request</td></tr>       <tr><td>%url</td><td>Full URL with query string, if any</td></tr><tr><td>%utctime</td><td>RFC 3339 timestamp of the response, for example, 2021-10-05T12:34:56Z</td></tr></table>
        # If any variable value contains non-printable characters (ASCII characters <=0x1F or >=0x7F), double quotes, or a backslash, each of those characters will be escaped to a format like '\xXX'. For example, double quotes will become '\x22' and backslash will become '\x5C'.
        # Note that space is not escaped. You must quote variables that may contain spaces to facilitate parsing.", "zh_CN": "默认值: %cltip %rmtuser  [%utctime] '%method %url %protocol' %statuscode %rspsize '%referer' '%ua' %rsptime 
        # 日志格式。可使用以下变量来自定义日志输出格式：
        # <table><tr><th>变量</th><th>变量说明</th></tr><tr><td>%cachestate</td><td>缓存状态，取值为HIT，MISS 或者 REVALIDATE。</td></tr><tr><td>%cltip</td><td>客户端IP地址。</td></tr><tr><td>%cltisp</td><td>客户端所属运营商。</td></tr><tr><td>%cltport</td><td>客户端端口号。</td></tr><tr><td>%cltregion</td><td>客户端所属区域。</td></tr><tr><td>%cpu_ns</td><td>此次请求所消耗的CPU时间，以纳秒计算。</td></tr><tr><td>%custom1</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段1的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%custom2</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段2的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%hostname</td><td>Host 请求头。</td></tr><tr><td>%method</td><td>HTTP请求方法，例如 GET。</td></tr><tr><td>%protocol</td><td>HTTP/1.0，HTTP/1.1 或者 HTTP2.0协议。</td></tr><tr><td>%querystr</td><td>查询参数字符串。</td></tr>      <tr><td>%referer</td><td>Referer 请求头。</td></tr><tr><td>%reqhdrsize</td><td>请求头大小，单位为bytes。</td></tr><tr><td>%reqrange</td><td>客户端请求所携带的Range请求头。</td></tr><tr><td>%reqsize</td><td>请求的大小，单位为bytes。包括请求行，请求头和请求体。</td></tr><tr><td>%rmtuser</td><td>从Authorization请求头解析出的用户名。当您使用HTTP basic对用户请求进行鉴权时，可通过该变量获取用户名。</td></tr><tr><td>%rspsize</td><td>HTTP响应的大小，单位为bytes。包括响应头和响应体，但不包括TCP/IP/MAC头部开销。</td></tr><tr><td>%rsptime</td><td>响应时间，单位为毫秒。</td></tr><tr><td>%samplerate</td><td>采样率，即每几次请求输出一条日志。</td></tr><tr><td>%sheme</td><td>http或https协议。</td></tr><tr><td>%statuscode</td><td>响应状态码，例如200。</td></tr><tr><td>%srvip</td><td>处理此次请求的CDN服务器的IP地址。</td></tr><tr><td>%svrnode</td><td>CDN服务器所在的节点名称。</td></tr><tr><td>%tcprtt</td><td>服务器与客户端之间的RTT时长，单位为毫秒。</td></tr>      <tr><td>%ua</td><td>User-Agent 请求头。</td></tr><tr><td>%uniqueid</td><td>此次请求的唯一标识，字符串类型。</td></tr>       <tr><td>%url</td><td>完整的URL，包括查询参数字符串。</td></tr><tr><td>%utctime</td><td>响应时间，以RFC 3339格式表示，例如 2021-10-05T12:34:56Z。</td></tr></table>
        # 
        # 变量如果包含了不可打印的字符（ASCII码<=0x1F 或 >=0x7F的字符），双引号或者反斜杆，则这些字符会被转义，用'\xXX'的格式表示。例如，双引号以'\x22'表示，反斜杆以'\x5C'表示。需要注意的是，空格不会被转义。如果变量包含空格，则必须加上双引号，才能被正确解析。"}
        self.log_download_format = log_download_format
        # {"en" : "Default: 14 Range: [ 1 .. 30 ] 
        # Number of days to store the logs.", "zh_CN": "默认值: 14 取值范围: [ 1 .. 30 ] 
        # 日志保存天数。"}
        self.log_download_storage_days = log_download_storage_days
        # {"en" : "Enum: 5,15,30,60,120,240,480,1440 
        # Default: 30 
        # Time span of each log file in minutes. When the count of logs tend to increase drastically, logs within a same time span might be truncated and put into multiple log files. When there is significant delay of logs ingestion, the logs delayed might be written to separate log files.", "zh_CN": "取值范围: 5,15,30,60,120,240,480,1440 
        # 默认值: 30 
        # 每几分钟生成日志文件。为避免单个日志文件过大，当日志条目增长过快时，同一个时间段内的日志可能被分割为多个文件。当日志入库发生显著延迟时，延迟入库的部分会被写入单独的日志文件。"}
        self.log_download_file_span_minutes = log_download_file_span_minutes

    def validate(self):
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.log_download_format is not None:
            result['logDownloadFormat'] = self.log_download_format
        if self.log_download_storage_days is not None:
            result['logDownloadStorageDays'] = self.log_download_storage_days
        if self.log_download_file_span_minutes is not None:
            result['logDownloadFileSpanMinutes'] = self.log_download_file_span_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('logDownloadFormat') is not None:
            self.log_download_format = m.get('logDownloadFormat')
        if m.get('logDownloadStorageDays') is not None:
            self.log_download_storage_days = m.get('logDownloadStorageDays')
        if m.get('logDownloadFileSpanMinutes') is not None:
            self.log_download_file_span_minutes = m.get('logDownloadFileSpanMinutes')
        return self


class CreateALogConfigurationResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateALogConfigurationResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"A reference to the new log configuration. Example:<code>Location: https://{domain}/cdn/report/logConfigs/4427</code>.", "zh_CN":"通过Location响应头返回新建的日志配置的URL。URL中包含日志配置的ID，可使用该ID调用'查询日志配置详情'接口来查看日志配置的详细信息。URL示例：<code>Location: https://{domain}/cdn/report/logConfigs/4427"}
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






class GetAccessLogsForHostnamesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccessLogsForHostnamesParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. It should be within the past 14 days. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2021-10-30T00:00:00Z ", "zh_CN": "查询范围的开始时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：startdate=2019-10-30T00:00:00Z。 查询开始时间不得早于14天之前。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2021-11-14T00:00:00Z ", "zh_CN": "查询范围的结束时间，以RFC 3339日期格式表示。必须使用UTC时区指定时间。示例：enddate=2019-11-14T00:00:00Z。"}
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


class GetAccessLogsForHostnamesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccessLogsForHostnamesRequestFilters(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
    ):
        # {"en" : "Specify the hostnames that interest you.", "zh_CN": "指定加速域名。"}
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


class GetAccessLogsForHostnamesRequest(TeaModel):
    def __init__(
        self,
        filters: GetAccessLogsForHostnamesRequestFilters = None,
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
            temp_model = GetAccessLogsForHostnamesRequestFilters()
            self.filters = temp_model.from_map(m['filters'])
        return self


class GetAccessLogsForHostnamesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAccessLogsForHostnamesResponseLogs(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        file_size: int = None,
        log_url: str = None,
        hostname: str = None,
    ):
        # {"en" : "An RFC 3339 date indicate the beginning of the log file.", "zh_CN": "RFC 3339格式的日期，表示日志文件的开始时间。"}
        self.date_from = date_from
        # {"en" : "An RFC 3339 date indicating the end of the log file.", "zh_CN": "RFC 3339格式的日期，表示日志文件的结束时间。"}
        self.date_to = date_to
        # {"en" : "Range: >= 0 
        # Size of log file in megabytes.", "zh_CN": "取值范围: >= 0 
        # 日志文件的大小（MB）。"}
        self.file_size = file_size
        # {"en" : "URL to the log file. The file has been compressed using gzip. Refer to the API description for details about the format.", "zh_CN": "日志文件的下载链接。该文件已使用gzip压缩。"}
        self.log_url = log_url
        # {"en" : "The log file contains entries for this hostname.", "zh_CN": "日志文件对应的加速域名。"}
        self.hostname = hostname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.hostname is not None:
            result['hostname'] = self.hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        return self


class GetAccessLogsForHostnamesResponse(TeaModel):
    def __init__(
        self,
        logs: List[GetAccessLogsForHostnamesResponseLogs] = None,
    ):
        # {"en" : "List of objects describing logs you can download.", "zh_CN": "日志信息列表。"}
        self.logs = logs

    def validate(self):
        self.validate_required(self.logs, 'logs')
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['logs'] = []
            for k in self.logs:
                result['logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logs') is not None:
            self.logs = []
            for k in m.get('logs'):
                temp_model = GetAccessLogsForHostnamesResponseLogs()
                self.logs.append(temp_model.from_map(k))
        return self






class GetALogConfigurationPaths(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # {"en" : "ID of a log configuration", "zh_CN": "日志配置的id。"}
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


class GetALogConfigurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetALogConfigurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetALogConfigurationRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetALogConfigurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetALogConfigurationResponseConfigs(TeaModel):
    def __init__(
        self,
        description: str = None,
        hostnames: List[str] = None,
        log_download_format: str = None,
        log_download_storage_days: int = None,
        log_download_file_span_minutes: int = None,
    ):
        # {"en" : "A description of the log configuration.", "zh_CN": "日志配置描述信息。"}
        self.description = description
        # {"en" : "A list of hostnames to which the log configuration applies. A hostname should be a fully qualified domain name like domain.com, a wildcard domain name with a leading '*' like *.domain.com, or '*' if you want the log configuration to apply to all hostnames. You should ensure that only one log configuration applies to each hostname.", "zh_CN": "适用该日志配置的域名列表。每个域名必须是完整的FQDN域名如domain.com，或者是带星号的泛域名如*.domain.com。如果该日志配置适用于所有域名，则直接用星号*表示。每个域名有且只能有一个对应的日志配置。"}
        self.hostnames = hostnames
        # {"en" : "Format of the log entry. You can use the following variables to create a custom format:
        # <table><tr><th>Variable</th><th>Meaning</th></tr><tr><td>%cachestate</td><td>HIT, MISS, or REVALIDATE</td></tr><tr><td>%cltip</td><td>Client IP address</td></tr><tr><td>%cltisp</td><td>Client ISP</td></tr><tr><td>%cltport</td><td>Client port number</td></tr><tr><td>%cltregion</td><td>Client region</td></tr><tr><td>%cpu_ns</td><td>CPU time in nanoseconds for this request</td></tr>      <tr><td>%custom1</td><td>Refers to a custom log field with ID 1 you define using the custom_log_field directive.</td></tr>      <tr><td>%custom2</td><td>Refers to a custom log field with ID 2 you define using the custom_log_field directive.</td></tr>      <tr><td>%hostname</td><td>Host header</td></tr><tr><td>%method</td><td>HTTP method used to access the content, for example, GET</td></tr><tr><td>%protocol</td><td>HTTP/1.0 or HTTP/1.1 or HTTP2.0</td></tr><tr><td>%querystr</td><td>Query string</td></tr><tr><td>%referer</td><td>Referer request header</td></tr><tr><td>%reqhdrsize</td><td>Request header size in bytes</td></tr>      <tr><td>%reqrange</td><td>Range header in requests from client</td></tr><tr><td>%reqsize</td><td>Request size in bytes including the request line, header, and request body</td></tr><tr><td>%rmtuser</td><td>User name extracted from the Authorization header when basic authentication is used</td></tr><tr><td>%rspsize</td><td>HTTP response size, in bytes, including header and body, but not including TCP/IP/MAC</td></tr><tr><td>%rsptime</td><td>Response time in milliseconds</td></tr><tr><td>%samplerate</td><td>Number of requests corresponding to each log entry</td></tr><tr><td>%scheme</td><td>http or https</td></tr><tr><td>%statuscode</td><td>Response's status code, for example, 200</td></tr><tr><td>%srvip</td><td>IP address of the CDN server handling the request</td></tr><tr><td>%svrnode</td><td>Cache server node name</td></tr><tr><td>%tcprtt</td><td>Round-trip time between server and client in microseconds</td></tr>      <tr><td>%ua</td><td>User-Agent header</td></tr><tr><td>%uniqueid</td><td>A string uniquely identifying this request</td></tr>       <tr><td>%url</td><td>Full URL with query string, if any</td></tr><tr><td>%utctime</td><td>RFC 3339 timestamp of the response, for example, 2021-10-05T12:34:56Z</td></tr></table>
        # If any variable value contains non-printable characters (ASCII characters <=0x1F or >=0x7F), double quotes, or a backslash, each of those characters will be escaped to a format like '\xXX'. For example, double quotes will become '\x22' and backslash will become '\x5C'.
        # Note that space is not escaped. You must quote variables that may contain spaces to facilitate parsing.", "zh_CN": "日志格式。可使用以下变量来自定义日志输出格式：
        # <table><tr><th>变量</th><th>变量说明</th></tr><tr><td>%cachestate</td><td>缓存状态，取值为HIT，MISS 或者 REVALIDATE。</td></tr><tr><td>%cltip</td><td>客户端IP地址。</td></tr><tr><td>%cltisp</td><td>客户端所属运营商。</td></tr><tr><td>%cltport</td><td>客户端端口号。</td></tr><tr><td>%cltregion</td><td>客户端所属区域。</td></tr><tr><td>%cpu_ns</td><td>此次请求所消耗的CPU时间，以纳秒计算。</td></tr><tr><td>%custom1</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段1的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%custom2</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段2的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%hostname</td><td>Host 请求头。</td></tr><tr><td>%method</td><td>HTTP请求方法，例如 GET。</td></tr><tr><td>%protocol</td><td>HTTP/1.0，HTTP/1.1 或者 HTTP2.0协议。</td></tr><tr><td>%querystr</td><td>查询参数字符串。</td></tr>      <tr><td>%referer</td><td>Referer 请求头。</td></tr><tr><td>%reqhdrsize</td><td>请求头大小，单位为bytes。</td></tr><tr><td>%reqrange</td><td>客户端请求所携带的Range请求头。</td></tr><tr><td>%reqsize</td><td>请求的大小，单位为bytes。包括请求行，请求头和请求体。</td></tr><tr><td>%rmtuser</td><td>从Authorization请求头解析出的用户名。当您使用HTTP basic对用户请求进行鉴权时，可通过该变量获取用户名。</td></tr><tr><td>%rspsize</td><td>HTTP响应的大小，单位为bytes。包括响应头和响应体，但不包括TCP/IP/MAC头部开销。</td></tr><tr><td>%rsptime</td><td>响应时间，单位为毫秒。</td></tr><tr><td>%samplerate</td><td>采样率，即每几个请求输出一条日志。</td></tr><tr><td>%sheme</td><td>http或https协议。</td></tr><tr><td>%statuscode</td><td>响应状态码，例如200。</td></tr><tr><td>%srvip</td><td>处理此次请求的CDN服务器的IP地址。</td></tr><tr><td>%svrnode</td><td>CDN服务器所在的节点名称。</td></tr><tr><td>%tcprtt</td><td>服务器与客户端之间的RTT时长，单位为毫秒。</td></tr>      <tr><td>%ua</td><td>User-Agent 请求头。</td></tr><tr><td>%uniqueid</td><td>此次请求的唯一标识，字符串类型。</td></tr>       <tr><td>%url</td><td>完整的URL，包括查询参数字符串。</td></tr><tr><td>%utctime</td><td>响应时间，以RFC 3339格式表示，例如 2021-10-05T12:34:56Z。</td></tr></table>
        # 
        # 变量如果包含了不可打印的字符（ASCII码<=0x1F 或 >=0x7F的字符），双引号或者反斜杆，则这些字符会被转义，用'\xXX'的格式表示。例如，双引号以'\x22'表示，反斜杆以'\x5C'表示。需要注意的是，空格不会被转义。如果变量包含空格，则必须加上双引号，才能被正确解析。"}
        self.log_download_format = log_download_format
        # {"en" : "Default: 14 Range: [ 1 .. 30 ] 
        # Number of days to store the logs.", "zh_CN": "默认值: 14 取值范围: [ 1 .. 30 ] 
        # 日志保存天数。"}
        self.log_download_storage_days = log_download_storage_days
        # {"en" : "Enum: 5,15,30,60,120,240,480,1440 
        # Default: 30 
        # Time span of each log file in minutes.", "zh_CN": "取值范围: 5,15,30,60,120,240,480,1440 
        # 默认值: 30 
        # 每几分钟生成日志文件。"}
        self.log_download_file_span_minutes = log_download_file_span_minutes

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.hostnames, 'hostnames')
        self.validate_required(self.log_download_format, 'log_download_format')
        self.validate_required(self.log_download_storage_days, 'log_download_storage_days')
        self.validate_required(self.log_download_file_span_minutes, 'log_download_file_span_minutes')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.log_download_format is not None:
            result['logDownloadFormat'] = self.log_download_format
        if self.log_download_storage_days is not None:
            result['logDownloadStorageDays'] = self.log_download_storage_days
        if self.log_download_file_span_minutes is not None:
            result['logDownloadFileSpanMinutes'] = self.log_download_file_span_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('logDownloadFormat') is not None:
            self.log_download_format = m.get('logDownloadFormat')
        if m.get('logDownloadStorageDays') is not None:
            self.log_download_storage_days = m.get('logDownloadStorageDays')
        if m.get('logDownloadFileSpanMinutes') is not None:
            self.log_download_file_span_minutes = m.get('logDownloadFileSpanMinutes')
        return self


class GetALogConfigurationResponse(TeaModel):
    def __init__(
        self,
        id: int = None,
        configs: GetALogConfigurationResponseConfigs = None,
        last_update_time: str = None,
        creation_time: str = None,
    ):
        # {"en" : "Range: >= 1 
        # ID of the log configuration", "zh_CN": "取值范围: >= 1 
        # 日志配置的ID。"}
        self.id = id
        # {"en" : "Describes a log configuration", "zh_CN": "日志配置。"}
        self.configs = configs
        # {"en" : "RFC 3339 date indicating when the log configuration was last updated.", "zh_CN": "日志配置最近一次更新时间，以RFC 3339日期格式展示。"}
        self.last_update_time = last_update_time
        # {"en" : "RFC 3339 date indicating when the log configuration was created.", "zh_CN": "日志配置创建时间，以RFC 3339日期格式展示。"}
        self.creation_time = creation_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.configs, 'configs')
        if self.configs:
            self.configs.validate()
        self.validate_required(self.last_update_time, 'last_update_time')
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.configs is not None:
            result['configs'] = self.configs.to_map()
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('configs') is not None:
            temp_model = GetALogConfigurationResponseConfigs()
            self.configs = temp_model.from_map(m['configs'])
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        return self






class UpdateALogConfigurationPaths(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # {"en" : "ID of a log configuration", "zh_CN": "日志配置的id。"}
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


class UpdateALogConfigurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateALogConfigurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateALogConfigurationRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        hostnames: List[str] = None,
        log_download_format: str = None,
        log_download_storage_days: int = None,
        log_download_file_span_minutes: int = None,
    ):
        # {"en" : "A description of the log configuration.", "zh_CN": "日志配置描述。"}
        self.description = description
        # {"en" : "A list of hostnames to which the log configuration applies. A hostname should be a fully qualified domain name like domain.com, a wildcard domain name with a leading '*' like *.domain.com, or '*' if you want the log configuration to apply to all hostnames. You should ensure that only one log configuration applies to each hostname.", "zh_CN": "适用该日志配置的域名列表。每个域名必须是完整的FQDN域名如domain.com，或者是带星号的泛域名如*.domain.com。如果该日志配置适用于所有域名，则直接用星号*表示。每个域名有且只能有一个对应的日志配置。"}
        self.hostnames = hostnames
        # {"en" : "Default: %cltip %rmtuser  [%utctime] '%method %url %protocol' %statuscode %rspsize '%referer' '%ua' %rsptime 
        # Format of the log entry. You can use the following variables to create a custom format:
        # <table><tr><th>Variable</th><th>Meaning</th></tr><tr><td>%cachestate</td><td>HIT, MISS, or REVALIDATE</td></tr><tr><td>%cltip</td><td>Client IP address</td></tr><tr><td>%cltisp</td><td>Client ISP</td></tr><tr><td>%cltport</td><td>Client port number</td></tr><tr><td>%cltregion</td><td>Client region</td></tr><tr><td>%cpu_ns</td><td>CPU time in nanoseconds for this request</td></tr><tr><td>%custom1</td><td>Refers to a custom log field with ID 1 you define using the custom_log_field directive.</td></tr>      <tr><td>%custom2</td><td>Refers to a custom log field with ID 2 you define using the custom_log_field directive.</td></tr>      <tr><td>%hostname</td><td>Host header</td></tr><tr><td>%method</td><td>HTTP method used to access the content, for example, GET</td></tr><tr><td>%protocol</td><td>HTTP/1.0 or HTTP/1.1 or HTTP2.0</td></tr><tr><td>%querystr</td><td>Query string</td></tr>      <tr><td>%referer</td><td>Referer request header</td></tr><tr><td>%reqhdrsize</td><td>Request header size in bytes</td></tr><tr><td>%reqrange</td><td>Range header in requests from client</td></tr><tr><td>%reqsize</td><td>Request size in bytes including the request line, header, and request body</td></tr><tr><td>%rmtuser</td><td>User name extracted from the Authorization header when basic authentication is used</td></tr><tr><td>%rspsize</td><td>HTTP response size, in bytes, including header and body, but not including TCP/IP/MAC</td></tr><tr><td>%rsptime</td><td>Response time in milliseconds</td></tr><tr><td>%samplerate</td><td>Number of requests corresponding to each log entry</td></tr><tr><td>%scheme</td><td>http or https</td></tr><tr><td>%statuscode</td><td>Response's status code, for example, 200</td></tr><tr><td>%srvip</td><td>IP address of the CDN server handling the request</td></tr><tr><td>%svrnode</td><td>Cache server node name</td></tr><tr><td>%tcprtt</td><td>Round-trip time between server and client in microseconds</td></tr>      <tr><td>%ua</td><td>User-Agent header</td></tr><tr><td>%uniqueid</td><td>A string uniquely identifying this request</td></tr>       <tr><td>%url</td><td>Full URL with query string, if any</td></tr><tr><td>%utctime</td><td>RFC 3339 timestamp of the response, for example, 2021-10-05T12:34:56Z</td></tr></table>
        # If any variable value contains non-printable characters (ASCII characters <=0x1F or >=0x7F), double quotes, or a backslash, each of those characters will be escaped to a format like '\xXX'. For example, double quotes will become '\x22' and backslash will become '\x5C'.
        # Note that space is not escaped. You must quote variables that may contain spaces to facilitate parsing.", "zh_CN": "默认值: %cltip %rmtuser  [%utctime] '%method %url %protocol' %statuscode %rspsize '%referer' '%ua' %rsptime 
        # 日志格式。可使用以下变量来自定义日志输出格式：
        # <table><tr><th>变量</th><th>变量说明</th></tr><tr><td>%cachestate</td><td>缓存状态，取值为HIT，MISS 或者 REVALIDATE。</td></tr><tr><td>%cltip</td><td>客户端IP地址。</td></tr><tr><td>%cltisp</td><td>客户端所属运营商。</td></tr><tr><td>%cltport</td><td>客户端端口号。</td></tr><tr><td>%cltregion</td><td>客户端所属区域。</td></tr><tr><td>%cpu_ns</td><td>此次请求所消耗的CPU时间，以纳秒计算。</td></tr><tr><td>%custom1</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段1的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%custom2</td><td>如果您在加速项目中自定义了日志字段，可以用该变量来获取自定义日志字段2的值。自定义日志字段属于高级功能，如需使用请联系我们的技术支持。</td></tr>      <tr><td>%hostname</td><td>Host 请求头。</td></tr><tr><td>%method</td><td>HTTP请求方法，例如 GET。</td></tr><tr><td>%protocol</td><td>HTTP/1.0，HTTP/1.1 或者 HTTP2.0协议。</td></tr><tr><td>%querystr</td><td>查询参数字符串。</td></tr>      <tr><td>%referer</td><td>Referer 请求头。</td></tr><tr><td>%reqhdrsize</td><td>请求头大小，单位为bytes。</td></tr><tr><td>%reqrange</td><td>客户端请求所携带的Range请求头。</td></tr><tr><td>%reqsize</td><td>请求的大小，单位为bytes。包括请求行，请求头和请求体。</td></tr><tr><td>%rmtuser</td><td>从Authorization请求头解析出的用户名。当您使用HTTP basic对用户请求进行鉴权时，可通过该变量获取用户名。</td></tr><tr><td>%rspsize</td><td>HTTP响应的大小，单位为bytes。包括响应头和响应体，但不包括TCP/IP/MAC头部开销。</td></tr><tr><td>%rsptime</td><td>响应时间，单位为毫秒。</td></tr><tr><td>%samplerate</td><td>采样率，即每几次请求输出一条日志。</td></tr><tr><td>%sheme</td><td>http或https协议。</td></tr><tr><td>%statuscode</td><td>响应状态码，例如200。</td></tr><tr><td>%srvip</td><td>处理此次请求的CDN服务器的IP地址。</td></tr><tr><td>%svrnode</td><td>CDN服务器所在的节点名称。</td></tr><tr><td>%tcprtt</td><td>服务器与客户端之间的RTT时长，单位为毫秒。</td></tr>      <tr><td>%ua</td><td>User-Agent 请求头。</td></tr><tr><td>%uniqueid</td><td>此次请求的唯一标识，字符串类型。</td></tr>       <tr><td>%url</td><td>完整的URL，包括查询参数字符串。</td></tr><tr><td>%utctime</td><td>响应时间，以RFC 3339格式表示，例如 2021-10-05T12:34:56Z。</td></tr></table>
        # 
        # 变量如果包含了不可打印的字符（ASCII码<=0x1F 或 >=0x7F的字符），双引号或者反斜杆，则这些字符会被转义，用'\xXX'的格式表示。例如，双引号以'\x22'表示，反斜杆以'\x5C'表示。需要注意的是，空格不会被转义。如果变量包含空格，则必须加上双引号，才能被正确解析。"}
        self.log_download_format = log_download_format
        # {"en" : "Default: 14 Range: [ 1 .. 30 ] 
        # Number of days to store the logs.", "zh_CN": "默认值: 14 取值范围: [ 1 .. 30 ] 
        # 日志保存天数。"}
        self.log_download_storage_days = log_download_storage_days
        # {"en" : "Enum: 5,15,30,60,120,240,480,1440 
        # Default: 30 
        # Time span of each log file in minutes.", "zh_CN": "取值范围: 5,15,30,60,120,240,480,1440 
        # 默认值: 30 
        # 每几分钟生成日志文件。"}
        self.log_download_file_span_minutes = log_download_file_span_minutes

    def validate(self):
        self.validate_required(self.hostnames, 'hostnames')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.log_download_format is not None:
            result['logDownloadFormat'] = self.log_download_format
        if self.log_download_storage_days is not None:
            result['logDownloadStorageDays'] = self.log_download_storage_days
        if self.log_download_file_span_minutes is not None:
            result['logDownloadFileSpanMinutes'] = self.log_download_file_span_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('logDownloadFormat') is not None:
            self.log_download_format = m.get('logDownloadFormat')
        if m.get('logDownloadStorageDays') is not None:
            self.log_download_storage_days = m.get('logDownloadStorageDays')
        if m.get('logDownloadFileSpanMinutes') is not None:
            self.log_download_file_span_minutes = m.get('logDownloadFileSpanMinutes')
        return self


class UpdateALogConfigurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateALogConfigurationResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




