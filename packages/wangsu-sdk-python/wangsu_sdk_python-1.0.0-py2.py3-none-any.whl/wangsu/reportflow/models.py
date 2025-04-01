# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportFlowDomainCountryServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        country_code: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Starting time
        # 
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00);
        # 2. Cannot be greater than the current time
        # 3. Get up to the last six months (183 days) of data.", "zh_CN":"开始时间
        # 1. 时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2. 不能大于当前时间
        # 3. 最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. Time format 2016-12-02T10:00:00+08:00
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one untransmitted, throw an exception
        # 4. Allow query maximum time interval: 7 days, that is, the difference between dateFrom and dateTo can&rsquo;t exceed 7 days (can contact technical support adjustment, up to 31 days).", "zh_CN":"结束时间:
        # 1. 时间格式2016-12-02T10:00:00+08:00
        # 2. 结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3. dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常
        # 4. 允许查询最大时间间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整，最长31天)。"}
        self.date_to = date_to
        # {"en":"Data granularity:
        # 1. Support 5m (5 minutes granularity),1d (1 day granularity)
        # 2. Do not pass the default to 5m", "zh_CN":"数据粒度:
        # 1. 支持5m(5分钟粒度),1d(天粒度)
        # 2. 不传默认为5m"}
        self.data_interval = data_interval
        # {"en":"domain name:
        # 
        # 1. The maximum number of deliverable domain names is 20 by default (can be contacted by technical support);
        # 2. Automatically filter out illegal domain names (such as passing illegal domain names, they will be filtered out, and the query results only return data of legitimate domain names).", "zh_CN":"域名:
        # 1. 可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2. 自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)。"}
        self.domain = domain
        # {"en":"Country code:
        # 
        # 1. Do not pass the default query for all countries and regions;
        # 2. The values that can be passed are detailed in the Countrycode list of appendix table on the API Overview page", "zh_CN":"国家地区代号:
        # 1. 不传默认查询全部国家地区;
        # 2. 可传递的值详见概览页国家地区列表说明。"}
        self.country_code = country_code
        # {"en":"Grouping dimension:
        # 
        # 1. Optional values domain, country and aggregatedOversea, can pass in single or multiple values. The aggregatedOversea and country cannot be passed at the same time;
        # 
        # 2. If there is an incoming, the detailed data will be displayed according to the dimension:
        # domain: Group display by domain name dimension;
        # country: Group display by country dimension;
        # aggregatedOversea: Group display according to domestic and overseas dimensions.
        # 3. The result hierarchy is fixed in order, and the order of the parameters does not affect the order of the returned results. For example: 'groupBy': ['domain','country'] and 'groupBy': ['country','domain'] return the same result.",
        # "zh_CN":"1. 可选值domain、country、aggregatedOversea,可传入单个或多个值,其中不能同时传aggregatedOversea 和 country;
        # 2. 有传入则按照该维度展示明细数据:
        #   1.domain:按照域名维度进行分组展示;
        #   2.domain:country:按照国家维度进行分组展示;
        #   3.aggregatedOversea:按照国内 和 海外维度进行分组展示
        # 3. 返回结果层级顺序固定,入参顺序不影响返回结果顺序。例如:groupBy: [domain,country]与groupBy: [country,domain]返回结果一样。"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.domain is not None:
            result['domain'] = self.domain
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowDomainCountryServiceResponseResultCountryDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        bandwidth: str = None,
    ):
        # {"en":"1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value in the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. Returns the time slice contained in the start time and end time.", "zh_CN":"1. 查询的数据粒度为5m时,格式为yyyy-MM-dd  HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd  00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00。2. 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Flow value, in megabytes, 2 decimal places", "zh_CN":"流量值,计量单位MB,保留2位小数"}
        self.value = value
        # {"en":"Bandwidth value. Unit is Mbps and 2 digits of decimals are allowed.", "zh_CN":"带宽值,单位Mbps,保留2位小数"}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self


class ReportFlowDomainCountryServiceResponseResultCountryData(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        country_name: str = None,
        flow_sum: str = None,
        flow_percentage: str = None,
        flow_data: List[ReportFlowDomainCountryServiceResponseResultCountryDataFlowData] = None,
    ):
        # {"en":"Country code", "zh_CN":"国家地区代号"}
        self.country_code = country_code
        # {"en":"Country name", "zh_CN":"国家地区名称"}
        self.country_name = country_name
        # {"en":"Summary of traffic in national regions: Summary of traffic flow in a single country region during the query period, unit of measure MB, retaining 2 decimal places", "zh_CN":"国家地区流量汇总:单个国家地区流量在查询时段内的流量汇总值,计量单位MB,保留2位小数"}
        self.flow_sum = flow_sum
        # {"en":"National regional traffic ratio: the proportion (percentage) of traffic value in a single country region during the query period, retaining 2 decimal places", "zh_CN":"国家地区流量占比:单个国家地区流量在查询时段内的流量值的占比(百分比),保留2位小数"}
        self.flow_percentage = flow_percentage
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.country_name, 'country_name')
        self.validate_required(self.flow_sum, 'flow_sum')
        self.validate_required(self.flow_percentage, 'flow_percentage')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.country_name is not None:
            result['countryName'] = self.country_name
        if self.flow_sum is not None:
            result['flowSum'] = self.flow_sum
        if self.flow_percentage is not None:
            result['flowPercentage'] = self.flow_percentage
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('countryName') is not None:
            self.country_name = m.get('countryName')
        if m.get('flowSum') is not None:
            self.flow_sum = m.get('flowSum')
        if m.get('flowPercentage') is not None:
            self.flow_percentage = m.get('flowPercentage')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportFlowDomainCountryServiceResponseResultCountryDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowDomainCountryServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[ReportFlowDomainCountryServiceResponseResultCountryData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.country_data = country_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.country_data, 'country_data')
        if self.country_data:
            for k in self.country_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.country_data is not None:
            result['countryData'] = []
            for k in self.country_data:
                result['countryData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('countryData') is not None:
            self.country_data = []
            for k in m.get('countryData'):
                temp_model = ReportFlowDomainCountryServiceResponseResultCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class ReportFlowDomainCountryServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowDomainCountryServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowDomainCountryServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowDomainCountryServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainCountryServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainCountryServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainCountryServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QuerySumUpTrafficUnderAccountRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySumUpTrafficUnderAccountResponseFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
    ):
        # {"en":"Date
        # 1.When the data query granularity is fiveminutes, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05 AM, and the last one is yyyy-MM-dd 24:00.
        # 2.When the data query granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is yyyy-MM-dd 24.
        # 3.When the data query granularity is daily, the format is yyyy-MM-dd; the data value of every time slice represents the value of the daily data.
        # 4.Return the time slice contained in start time and the time slice contained in end time", "zh_CN":"时间
        # 1.查询的数据粒度为fiveminutes时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是yyyy-MM-dd 24:00。
        # 2.查询的数据粒度为hourly时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是yyyy-MM-dd 24。
        # 3.查询的数据粒度为daily时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值。
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Traffic. Keep two digits of decimals. Unit: MB", "zh_CN":"流量,保留2位小数,单位为MB"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class QuerySumUpTrafficUnderAccountResponse(TeaModel):
    def __init__(
        self,
        flow_summary: str = None,
        flow_data: List[QuerySumUpTrafficUnderAccountResponseFlowData] = None,
    ):
        # {"en":"Total traffic. Keep two digits of decimals. Unit: MB", "zh_CN":"总流量,保留2位小数,单位为MB"}
        self.flow_summary = flow_summary
        # {"en":"flowData", "zh_CN":"流量数据"}
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.flow_summary, 'flow_summary')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_summary is not None:
            result['flow-summary'] = self.flow_summary
        if self.flow_data is not None:
            result['flow-data'] = []
            for k in self.flow_data:
                result['flow-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flow-summary') is not None:
            self.flow_summary = m.get('flow-summary')
        if m.get('flow-data') is not None:
            self.flow_data = []
            for k in m.get('flow-data'):
                temp_model = QuerySumUpTrafficUnderAccountResponseFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class QuerySumUpTrafficUnderAccountPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySumUpTrafficUnderAccountParameters(TeaModel):
    def __init__(
        self,
        datefrom: str = None,
        dateto: str = None,
        type: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be smaller than the current time and 'dateto';
        # 3.Period between 'datafrom' and 'dateto' cannot be longer than 31 days", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须小于当前时间和dateto;
        # 3.dateFrom和dateTo相差不能超过31天(可联系技术支持调整);4.只能查询最近2年内数据。"}
        self.datefrom = datefrom
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than 'datefrom'; 
        # 3.if it's greater than the current time, then the current time is assigned as the value", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于datefrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.dateto = dateto
        # {"en":"Data granularity
        # 1.fiveminutes: five minutes, hourly: one hour, daily: one day;
        # 2.If not specified, daily is set as the default value;
        # 3.If fiveminutes is specified as the value, then data is returned in actual configured granularity when there is a specific configuration on data collecting granularity for the custome", "zh_CN":"数据粒度
        # 1.fiveminutes:5分钟,hourly:1小时,daily:1天;
        # 2.不传递,默认为daily;
        # 3.传递fiveminutes时,若客户数据采集粒度有特殊配置将按实际配置粒度返回。"}
        self.type = type

    def validate(self):
        self.validate_required(self.datefrom, 'datefrom')
        self.validate_required(self.dateto, 'dateto')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datefrom is not None:
            result['datefrom'] = self.datefrom
        if self.dateto is not None:
            result['dateto'] = self.dateto
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datefrom') is not None:
            self.datefrom = m.get('datefrom')
        if m.get('dateto') is not None:
            self.dateto = m.get('dateto')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QuerySumUpTrafficUnderAccountRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySumUpTrafficUnderAccountResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowDirInfoServiceRequestDomainDir(TeaModel):
    def __init__(
        self,
        domain: str = None,
        dir: List[str] = None,
    ):
        # {"en":"Domain
        # 					1.Need to meet the regular expression rules that are used to validate domains;
        # 					2.Domain number limits can be adjusted depending on different accounts. The default value is 1;", "zh_CN":"域名
        # 					1.需要满足域名的正则校验;
        # 					2.域名个数限制根据账号可调,默认为1个;"}
        self.domain = domain
        # {"en":"Table of contents
        # 					1.Directory number limits can be adjusted depending on different accounts. The default value is 200;
        # 					2.Empty value means to query all directories. Number of directories shall not exceed set limit;
        # 					3.Invalid directories are not returned", "zh_CN":"目录
        # 					1.目录个数限制根据账号可调,默认为200个;
        # 					2.不传代表查询该域名下的所有目录,同时接受目录个数限制;
        # 					3.无效的目录不返回"}
        self.dir = dir

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.dir is not None:
            result['dir'] = self.dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        return self


class ReportFlowDirInfoServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        dir_hierarchy: str = None,
        domain_dir: List[ReportFlowDirInfoServiceRequestDomainDir] = None,
    ):
        # {"en":"Start time
        # 				1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 				2.Must be smaller than the current time and dateTo;
        # 				3.Period between dataFrom and dateTo cannot be longer than 31 days(technical support can be contacted to adjust);
        # 				4.You can only query data for the last 6 months.", "zh_CN":"开始时间
        # 				1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 				2.必须小于当前时间和dateTo;
        # 				3.dateFrom和dateTo相差不能超过31天(可联系技术支持调整);
        # 				4.只能查询最近半年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 				1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 				2.Must be greater than dateFrom;
        # 				3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 				1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 				2.必须大于dateFrom;
        # 				3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Directory levels, value range 1-4. Only one vlaue can be submitted", "zh_CN":"目录层级,取值范围1~4,只能提交单个值"}
        self.dir_hierarchy = dir_hierarchy
        self.domain_dir = domain_dir

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.dir_hierarchy, 'dir_hierarchy')
        self.validate_required(self.domain_dir, 'domain_dir')
        if self.domain_dir:
            for k in self.domain_dir:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.dir_hierarchy is not None:
            result['dirHierarchy'] = self.dir_hierarchy
        if self.domain_dir is not None:
            result['domainDir'] = []
            for k in self.domain_dir:
                result['domainDir'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dirHierarchy') is not None:
            self.dir_hierarchy = m.get('dirHierarchy')
        if m.get('domainDir') is not None:
            self.domain_dir = []
            for k in m.get('domainDir'):
                temp_model = ReportFlowDirInfoServiceRequestDomainDir()
                self.domain_dir.append(temp_model.from_map(k))
        return self


class ReportFlowDirInfoServiceResponseResultDetails(TeaModel):
    def __init__(
        self,
        dir: str = None,
        total_flow: str = None,
        bandwidth_peak_value: str = None,
    ):
        # {"en":"Directory name of corresponding level", "zh_CN":"对应层级的目录名称"}
        self.dir = dir
        # {"en":"Total traffic, unit is MB and 2  digits of decimals allowed", "zh_CN":"总流量,单位MB,保留2位小数"}
        self.total_flow = total_flow
        # {"en":"Bandwidth peak value with granularity of 5 minutes. Unit Mbps, two decimal digits allowed", "zh_CN":"带宽峰值,单位Mbps,保留2位小数"}
        self.bandwidth_peak_value = bandwidth_peak_value

    def validate(self):
        self.validate_required(self.dir, 'dir')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.bandwidth_peak_value, 'bandwidth_peak_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir is not None:
            result['dir'] = self.dir
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.bandwidth_peak_value is not None:
            result['bandwidthPeakValue'] = self.bandwidth_peak_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('bandwidthPeakValue') is not None:
            self.bandwidth_peak_value = m.get('bandwidthPeakValue')
        return self


class ReportFlowDirInfoServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[ReportFlowDirInfoServiceResponseResultDetails] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"details", "zh_CN":"详情数据"}
        self.details = details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportFlowDirInfoServiceResponseResultDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportFlowDirInfoServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowDirInfoServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowDirInfoServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowDirInfoServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDirInfoServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDirInfoServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDirInfoServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowOriginIspProvinceByteServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Starting time:
        #         1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        #         2. Must be greater than the current time -183 days, and less than the current time and dateTo;
        #         3. The difference between dateFrom and dateTo cannot exceed 7 days(technical support can be contacted to adjust);
        #         4. dateFrom and dateTo are either passed or not passed;
        #         5. dateFrom and dateTo are not passed, the default query data for the past 24 hours", "zh_CN":"开始时间
        #         1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2.必须大于当前时间-183天，并且小于当前时间和dateTo;
        #         3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);
        #         4.dateFrom和dateTo要么都传递，要么都不传递;
        #         5.dateFrom和dateTo都未传递，则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End Time:
        #         1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        #         2. Must be greater than dateFrom; if greater than the current time, re-assign the current time;", "zh_CN":"结束时间
        #         1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2.必须大于dateFrom;如果大于当前时间，则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain name: 
        # 		1.The maximum number of deliverable domain names is 20 by default (can be contacted by technical support adjustment). 
        # 		2.All domain names under the account are not passed when the entry is passed, but it cannot be queried when the number of domain names under the account exceeds the limit (error).", "zh_CN":"域名:
        # 		1.可传递域名数量上限默认为20个(可联系技术支持调整)
        # 		2.未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询(报错)。"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5 minutes granularity, 1h: 1 hour granularity", "zh_CN":"数据粒度，5m:5分钟粒度，1h:1小时粒度"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。
        # 
        # "}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Grouping dimension:
        #         1. The optional values are domain,province, and isp, which can pass multiple values.
        #         2. If there is an incoming, the detailed data will be displayed according to the dimension;", "zh_CN":"分组维度:
        #         1.可选值为domain、province、isp，可传入多个值;
        #         2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceDataOriginFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time,
        #         1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00;
        #         2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00;
        #         3. Return to the time slice included in the start time and end time.", "zh_CN":"时间，
        #         1.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05，最后一个时间片是(yyyy-MM-dd+1)00:00;
        #         2.查询的数据粒度为1h时，格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 01，最后一个时间片是(yyyy-MM-dd+1)&nbsp;00;
        #         3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Return source traffic, unit Byte", "zh_CN":"回源流量，单位Byte"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        origin_flow_data: List[ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceDataOriginFlowData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.origin_flow_data = origin_flow_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.origin_flow_data, 'origin_flow_data')
        if self.origin_flow_data:
            for k in self.origin_flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.origin_flow_data is not None:
            result['originFlowData'] = []
            for k in self.origin_flow_data:
                result['originFlowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('originFlowData') is not None:
            self.origin_flow_data = []
            for k in m.get('originFlowData'):
                temp_model = ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceDataOriginFlowData()
                self.origin_flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceByteServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"Internet service providers", "zh_CN":"运营商"}
        self.isp = isp
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowOriginIspProvinceByteServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceByteServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowOriginIspProvinceByteServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowOriginIspProvinceByteServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceByteServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowOriginIspProvinceByteServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowOriginIspProvinceByteServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceByteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceByteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceByteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceByteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowOriginIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days;
        # 
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天;(可联系技术支持调整)
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5-minute granularity, 1h: 1-hour granularity, The default granularity is 5 minutes.", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度, 默认粒度5分钟"}
        self.data_interval = data_interval
        # {"en":"Province:
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。
        # 
        # "}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Group dimension
        # 
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 
        # 2.The data is displayed according to the specified dimension, if not transmitted, aggregate according to all dimensions.", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据, 没传则按照所有维度聚合;"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceDataOriginFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        origin_bandwidth: str = None,
    ):
        # {"en":"Time,
        # 
        #    1.When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        #    2.When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        # 
        #    3.Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间,
        #    1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        #    2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00;
        #    3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Origin traffic. Keep two digits of decimals. Unit: MB", "zh_CN":"回源流量,保留2位小数,单位MB"}
        self.value = value
        # {"en":"Average origin traffic. Keep two decimals. Unit: Mbps", "zh_CN":"回源平均带宽,保留2位小数,单位Mbps"}
        self.origin_bandwidth = origin_bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.origin_bandwidth, 'origin_bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.origin_bandwidth is not None:
            result['originBandwidth'] = self.origin_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('originBandwidth') is not None:
            self.origin_bandwidth = m.get('originBandwidth')
        return self


class ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        origin_flow_data: List[ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceDataOriginFlowData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"originFlowData", "zh_CN":"流量数据"}
        self.origin_flow_data = origin_flow_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.origin_flow_data, 'origin_flow_data')
        if self.origin_flow_data:
            for k in self.origin_flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.origin_flow_data is not None:
            result['originFlowData'] = []
            for k in self.origin_flow_data:
                result['originFlowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('originFlowData') is not None:
            self.origin_flow_data = []
            for k in m.get('originFlowData'):
                temp_model = ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceDataOriginFlowData()
                self.origin_flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"Internet service providers", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"provinceData", "zh_CN":"省份数据"}
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowOriginIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowOriginIspProvinceServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"ispData", "zh_CN":"ISP数据"}
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowOriginIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowOriginIspProvinceServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowOriginIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowOriginIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowOriginIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIspProvinceHitRateDetailServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        query_by: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 24 hours,if the dataInterval is 1m,period between dataFrom and dateTo cannot be longer than 6 hours(you can contact technical support to adjust it);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 30 minutes is queried", "zh_CN":"开始时间
        #         1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        #         3.dateFrom和dateTo相差不能超过24小时;一分钟粒度dateFrom和dateTo相差不能超过6小时(可联系技术支持调整)
        #         4.dateFrom和dateTo要么都传递,要么都不传递;
        #         5.dateFrom和dateTo都未传递,则默认查询过去30分钟的数据;"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        #         1/格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2/必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain
        # 1.domain number limits can be adjusted depending on different accounts. The default value is 20.
        # 2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)", "zh_CN":"域名:
        #         1.可传递域名数量上限默认为20个(可联系技术支持调整);
        #         2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        #         3.域名超过上限,报错"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. Support 1m (1 minute granularity),5m (5 minutes granularity)
        # 2. The default value is 5m", "zh_CN":"数据粒度:
        #         1.1m:1分钟粒度, 5m:5分钟粒度
        #         2.不传默认查询 5m"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。
        # 
        # "}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Query Dimension
        # 1.Optional values: flow, request
        # 2.The default value is flow
        # 3.Flow: flow, two decimal places reserved;
        # 4.Request: Number of requests", "zh_CN":"查询维度
        #         1.可选值 flow、request
        #         2.不传默认 flow
        #         3.flow:流量,保留两位小数;
        #         4.request:请求数"}
        self.query_by = query_by
        # {"en":"Optional values: domain,province,isp. Multiple values can be transferred in;
        # Display detailed data according to this dimension if it is transferred in", "zh_CN":"分组维度
        #         可选值为domain、province、isp,可传入多个值;
        #         有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.query_by is not None:
            result['queryBy'] = self.query_by
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        hit_value: str = None,
        hit_rate: str = None,
    ):
        # {"en":"Time,the format is yyyy-MM-dd HH:mm", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Hit data incording to query by(flow/requests)", "zh_CN":"命中数据 flow:流量,保留两位小数; request:请求数"}
        self.hit_value = hit_value
        # {"en":"Hit rate,keep four decimal places", "zh_CN":"命中率,保留四位小数"}
        self.hit_rate = hit_rate

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.hit_value, 'hit_value')
        self.validate_required(self.hit_rate, 'hit_rate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.hit_value is not None:
            result['hitValue'] = self.hit_value
        if self.hit_rate is not None:
            result['hitRate'] = self.hit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('hitValue') is not None:
            self.hit_value = m.get('hitValue')
        if m.get('hitRate') is not None:
            self.hit_rate = m.get('hitRate')
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        details: List[ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceDataDetails] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"-", "zh_CN":""}
        self.details = details

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponseDataIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"Province data", "zh_CN":"省份数据"}
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowIspProvinceHitRateDetailServiceResponseDataIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowIspProvinceHitRateDetailServiceResponseDataIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"ISP data", "zh_CN":"运营商数据"}
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowIspProvinceHitRateDetailServiceResponseDataIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowIspProvinceHitRateDetailServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result infotmation", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detail data of request result", "zh_CN":"请求结果的详细数据"}
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
                temp_model = ReportFlowIspProvinceHitRateDetailServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceHitRateDetailServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceHitRateDetailServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceHitRateDetailServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceHitRateDetailServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTrafficRequestInTotalAndPeakValueRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. Time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (10:00 on 2nd of December 2016, Beijing Time);
        # 2. No bigger than the current time;
        # 3. Data in the last 183 days at most can be queried.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. the time format is 2016-12-02T10:00:00+08:00;
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used;
        # 3.  If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default, if only one field is filled in and one is left empty, then exception will be occur;
        # 4. Allowable maximum time range for query: 1 day, means the period between dateFrom to dateTo should not exceed 1 day (can be adjusted by contacting technical support up to 31 days).", "zh_CN":"结束时间：
        # 1.时间格式2016-12-02T10:00:00+08:00;
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间;
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时，如仅有一个未传，抛异常;
        # 4.允许查询最大时间间隔：1天，即dateFrom和dateTo相差不能超过1天（可联系技术支持调整，最大不超过31天）。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The default upper limit to domains that can be entered is 200 (Contact technical support to adjust, the upper limit is 500);
        # 2. All domains under the account are queried if this input parameter is not specified, but if the number of domains under the account exceeds limits, no query will be done (Error).", "zh_CN":"域名：
        # 1.可传递域名数量上限默认200个（可联系技术支持调整，最高上限500）;
        # 2.未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询（报错）。"}
        self.domain = domain
        # {"en":"Group keywords:
        # 1. By default, group data will be displayed;
        # 2. If there are keywords entered, value details shall be displayed by keywords;
        # If domain is specified to groupBy, it means results are returned according to domains;
        # 3. Only domain can be specified.", "zh_CN":"分组关键词：
        # 1.默认聚合展示；
        # 2.传入关键词则代表需要按照关键词对应的值展示明细；
        # 例如groupBy传domain，则代表返回按照domain明细展开。
        # 3.只能传递domain。"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryTrafficRequestInTotalAndPeakValueResponseResultFlowRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
        bandwidth: str = None,
        request: str = None,
    ):
        # {"en":"timestamp
        # 1. When the data granularity of query is 5m, the format is yyyy-mm-dd HH: MM;Each time slice data value represents the data value in the previous time granularity range.The time slice at the beginning of the day is yyyy-mm-dd 00:05, and the last time slice is (yyyy-mm-dd +1) 00:00;
        # 2. Return the time slice of start time and end time.", "zh_CN":"时间片
        # 1.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00;
        # 2.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"flow", "zh_CN":"流量值，单位MB，保留2位小数；"}
        self.flow = flow
        # {"en":"Bandwidth, unit: Mbps, 2 decimal places reserved, example (931556.21)", "zh_CN":"带宽值，单位: Mbps，保留2位小数，示例 （931556.21）"}
        self.bandwidth = bandwidth
        # {"en":"request", "zh_CN":"请求数"}
        self.request = request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class QueryTrafficRequestInTotalAndPeakValueResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        total_flow: str = None,
        total_request: str = None,
        peak_bandwidth: str = None,
        peak_time: str = None,
        peak_request: str = None,
        peak_request_time: str = None,
        flow_request_data: List[QueryTrafficRequestInTotalAndPeakValueResponseResultFlowRequestData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"totalFlow, unit: MB, 2 decimal places reserved, example (74099.92)", "zh_CN":"总流量，单位:MB ，保留2位小数，示例 ( 74099.92 )"}
        self.total_flow = total_flow
        # {"en":"totalRequest", "zh_CN":"总请求数"}
        self.total_request = total_request
        # {"en":"peakBandwidth, unit: Mbps, 2 decimal places reserved, example (74099.92)", "zh_CN":"峰值带宽，单位: Mbps，保留2位小数，示例 （931556.21）"}
        self.peak_bandwidth = peak_bandwidth
        # {"en":"peakTime", "zh_CN":"峰值时间，示例（2019-02-13 18:01）"}
        self.peak_time = peak_time
        # {"en":"Peak request", "zh_CN":"请求数峰值"}
        self.peak_request = peak_request
        # {"en":"Peak time of request", "zh_CN":"请求数峰值时间"}
        self.peak_request_time = peak_request_time
        # {"en":"", "zh_CN":""}
        self.flow_request_data = flow_request_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.peak_bandwidth, 'peak_bandwidth')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_request, 'peak_request')
        self.validate_required(self.peak_request_time, 'peak_request_time')
        self.validate_required(self.flow_request_data, 'flow_request_data')
        if self.flow_request_data:
            for k in self.flow_request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.peak_bandwidth is not None:
            result['peakBandwidth'] = self.peak_bandwidth
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_request is not None:
            result['peakRequest'] = self.peak_request
        if self.peak_request_time is not None:
            result['peakRequestTime'] = self.peak_request_time
        if self.flow_request_data is not None:
            result['flowRequestData'] = []
            for k in self.flow_request_data:
                result['flowRequestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('peakBandwidth') is not None:
            self.peak_bandwidth = m.get('peakBandwidth')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakRequest') is not None:
            self.peak_request = m.get('peakRequest')
        if m.get('peakRequestTime') is not None:
            self.peak_request_time = m.get('peakRequestTime')
        if m.get('flowRequestData') is not None:
            self.flow_request_data = []
            for k in m.get('flowRequestData'):
                temp_model = QueryTrafficRequestInTotalAndPeakValueResponseResultFlowRequestData()
                self.flow_request_data.append(temp_model.from_map(k))
        return self


class QueryTrafficRequestInTotalAndPeakValueResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryTrafficRequestInTotalAndPeakValueResponseResult] = None,
    ):
        # {"en":"", "zh_CN":""}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryTrafficRequestInTotalAndPeakValueResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryTrafficRequestInTotalAndPeakValuePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficRequestInTotalAndPeakValueParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficRequestInTotalAndPeakValueRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficRequestInTotalAndPeakValueResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIspProvinceByteServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {'en':'Starting time
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. Must be greater than the current time -183 days, and less than the current time and dateTo;
        # 
        # 3. The difference between dateFrom and dateTo cannot exceed 7 days (You can contact technical support for adjustment, up to 31 days);
        # 
        # 4.dateFrom and dateTo are either passed or not passed;
        # 
        # 5. DateFrom and dateTo are not passed, the default query data for the past 24 hours;', 'zh_CN':'开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于当前时间-183天，并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过7天（可联系技术支持调整，最大31天）；
        # 4.dateFrom和dateTo要么都传递，要么都不传递；
        # 5.dateFrom和dateTo都未传递，则默认查询过去24小时的数据；'}
        self.date_from = date_from
        # {'en':'End Time
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. Must be greater than dateFrom; if greater than the current time, re-assign the current time;', 'zh_CN':'结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；如果大于当前时间，则重新赋值为当前时间；'}
        self.date_to = date_to
        # {'en':'The domain name and the number of domain names are adjustable according to the account number. The default is 20', 'zh_CN':'域名，域名个数限制根据账号可调，默认为20个'}
        self.domain = domain
        # {'en':'Data granularity, 5m: 5 minutes granularity, 1h: 1 hour granularity', 'zh_CN':'数据粒度，5m：5分钟粒度，1h：1小时粒度'}
        self.data_interval = data_interval
        # {'en':'Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.', 'zh_CN':'省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。'}
        self.province = province
        # {'en':'ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.', 'zh_CN':'运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节'}
        self.isp = isp
        # {'en':'Grouping dimension
        # 
        # 1. The optional values are domain,province, and isp, which can pass multiple values.
        # 
        # 2. If there is an incoming, the detailed data will be displayed according to the dimension;', 'zh_CN':'分组维度
        # 1.可选值为domain、province、isp，可传入多个值；
        # 2.有传入则按照该维度展示明细数据；'}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'time
        # 1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00.
        # 3. Return to the time slice included in the start time and end time.', 'zh_CN':'时间
        # 1.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05，最后一个时间片是（yyyy-MM-dd+1）00:00。
        # 2.查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 01，最后一个时间片是（yyyy-MM-dd+1）&nbsp;00。
        # 3.返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Flow value in Byte', 'zh_CN':'流量值，单位为Byte'}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        flow_data: List[ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceDataFlowData] = None,
    ):
        # {'en':'province', 'zh_CN':'省份'}
        self.province = province
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceByteServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceData] = None,
    ):
        # {'en':'Internet service providers', 'zh_CN':'运营商'}
        self.isp = isp
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowIspProvinceByteServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceByteServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowIspProvinceByteServiceResponseResultIspData] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowIspProvinceByteServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceByteServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowIspProvinceByteServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowIspProvinceByteServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceByteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceByteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceByteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceByteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryOutputTrafficUnderShieldPoPRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it&rsquo;s greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, support 5m (granularity of 5 minutes)", "zh_CN":"数据粒度,支持5m:5分钟粒度"}
        self.data_interval = data_interval
        # {"en":"Group dimension
        # 
        # 1.The value can be selected is domain;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryOutputTrafficUnderShieldPoPResponseResultFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00.", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00:00。"}
        self.timestamp = timestamp
        # {"en":"Traffic unit is MB and 2 digits &nbsp; of decimals allowed", "zh_CN":"流量值,单位MB,保留2位小数"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryOutputTrafficUnderShieldPoPResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        total_flow: str = None,
        flow_data: List[QueryOutputTrafficUnderShieldPoPResponseResultFlowData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Total traffic", "zh_CN":"总流量"}
        self.total_flow = total_flow
        # {"en":"flowData", "zh_CN":"流量值数据"}
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = QueryOutputTrafficUnderShieldPoPResponseResultFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class QueryOutputTrafficUnderShieldPoPResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryOutputTrafficUnderShieldPoPResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryOutputTrafficUnderShieldPoPResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryOutputTrafficUnderShieldPoPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOutputTrafficUnderShieldPoPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOutputTrafficUnderShieldPoPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOutputTrafficUnderShieldPoPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowHitRateIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must   be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days;
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last   24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天;(可联系技术支持调整)
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it&rsquo;s greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number   limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5-minute granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Group dimension
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        hit_flow: str = None,
    ):
        # {"en":"Time,
        # 1.When   the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 2.When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        # 3.Return the time slice contained in start time and the time slice contained in end   time.", "zh_CN":"时间,
        # 1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00;
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Byte hit rate. Four digits of &nbsp; decimals are allowed", "zh_CN":"字节命中率,保留4位小数"}
        self.value = value
        # {"en":"Hit traffic. Unit is MB and 2 &nbsp; digits of decimals are allowed", "zh_CN":"命中流量值,单位MB,保留2位小数;
        # 默认不返回该字段,需要返回的请联系技术支持"}
        self.hit_flow = hit_flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.hit_flow, 'hit_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.hit_flow is not None:
            result['hitFlow'] = self.hit_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('hitFlow') is not None:
            self.hit_flow = m.get('hitFlow')
        return self


class ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        hit_rate_data: List[ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.hit_rate_data = hit_rate_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.hit_rate_data, 'hit_rate_data')
        if self.hit_rate_data:
            for k in self.hit_rate_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.hit_rate_data is not None:
            result['hitRateData'] = []
            for k in self.hit_rate_data:
                result['hitRateData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('hitRateData') is not None:
            self.hit_rate_data = []
            for k in m.get('hitRateData'):
                temp_model = ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData()
                self.hit_rate_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
        self.isp = isp
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowHitRateIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowHitRateIspProvinceServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowHitRateIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowHitRateIspProvinceServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowHitRateIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowExactDomainServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        exact_domain: List[str] = None,
    ):
        # {'en':'Starting time
        # 
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00) );
        # 
        # 2. Cannot be greater than the current time
        # 
        # 3. Get up to the last six months (183 days) of data.', 'zh_CN':'开始时间
        # 1.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;不能大于当前时间
        # 3.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End Time
        # 
        # 1. Time format yyyy-MM-ddTHH:mm:ss+08:00, for example: 2016-12-02T10:00:00+08:00
        # 
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 
        # 3. dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one untransmitted, throw an exception
        # 
        # 4. Allow query maximum time interval: default 1 day, that is, the difference between dateFrom and dateTo can't exceed 1 day (can contact technical support adjustment).', 'zh_CN':'结束时间
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00，例如：2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：默认1天，即dateFrom和dateTo相差不能超过1天（可联系技术支持调整）。'}
        self.date_to = date_to
        # {'en':'Data granularity:
        # 
        # 1. Support 5m (5 minutes granularity), 1d (1 day granularity)
        # 
        # 2. Do not pass the default to 5m', 'zh_CN':'数据粒度：
        # 1.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;支持5m（5分钟粒度）、1d（1天粒度）
        # 2.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;不传默认为5m'}
        self.data_interval = data_interval
        # {'en':'Domain name:
        # 
        # 1. The maximum number of passable domain names is 20 by default (you can contact technical support adjustment).
        # 
        # 2. When the total number of precise domain names under multiple generic domain names exceeds the number of transmittables configured by exactDomain, it is not possible to check (error prompt).
        # 
        # 3. Automatically filter out illegal domain names (such as passing illegal domain names, they will be filtered out, and the query results only return data of legitimate domain names).', 'zh_CN':'域名（即泛域名）：
        # 1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可传递域名数量上限默认为20个（可联系技术支持调整）。
        # 2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当传入的多个泛域名下的精确域名总数量超过exactDomain配置的可传数量时不可查（报错提示）。
        # 3.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。'}
        self.domain = domain
        # {'en':'Exact domain name
        # 
        # 1. The maximum number of passable precise domain names is 200 by default (can be contacted for technical support adjustment)
        # 
        # 2. Can be an exact domain name under different pan-domain names.', 'zh_CN':'精确域名
        # 1.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;可传递精确域名数量上限默认为200个（可联系技术支持调整）
        # 2.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;可以是不同泛域名下的精确域名。'}
        self.exact_domain = exact_domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.domain is not None:
            result['domain'] = self.domain
        if self.exact_domain is not None:
            result['exactDomain'] = self.exact_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('exactDomain') is not None:
            self.exact_domain = m.get('exactDomain')
        return self


class ReportFlowExactDomainServiceResponseResultFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'time
        # 1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value in the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. When the data granularity of the query is 1d, the format is yyyy-MM-dd; the data value of the day represented by each time slice data value.
        # 3. Returns the time slice contained in the start time and end time.', 'zh_CN':'时间
        # 1.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;查询的数据粒度为5m时，格式为yyyy-MM-dd &nbsp; HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00。
        # 2.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;查询的数据粒度为1d时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值。
        # 3.&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Flow, unit of measure MB, retain 2 decimal places', 'zh_CN':'流量，计量单位MB，保留2位小数'}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportFlowExactDomainServiceResponseResult(TeaModel):
    def __init__(
        self,
        exact_domain: str = None,
        flow_data: List[ReportFlowExactDomainServiceResponseResultFlowData] = None,
    ):
        # {'en':'Exact domain name', 'zh_CN':'精确域名'}
        self.exact_domain = exact_domain
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.exact_domain, 'exact_domain')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exact_domain is not None:
            result['exactDomain'] = self.exact_domain
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exactDomain') is not None:
            self.exact_domain = m.get('exactDomain')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportFlowExactDomainServiceResponseResultFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowExactDomainServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowExactDomainServiceResponseResult] = None,
    ):
        # {'en':'result', 'zh_CN':'结果'}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowExactDomainServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowExactDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowExactDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowExactDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowExactDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowHitRateIspProvinceByteServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Starting time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.Must be greater than the current time -183 days, and less than the current time and dateTo;
        # 
        # 3.The difference between dateFrom and dateTo cannot exceed 7 days(technical support can be contacted to adjust);
        # 
        # 4.DateFrom and dateTo are either passed or not passed;
        # 
        # 5.DateFrom and dateTo are not passed, the default query data for the past 24 hours", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"Starting time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.Must be greater than the current time -183 days, and less than the current time and dateTo;
        # 
        # 3.The difference between dateFrom and dateTo cannot exceed 7 days;
        # 
        # 4.DateFrom and dateTo are either passed or not passed;
        # 
        # 5.DateFrom and dateTo are not passed, the default query data for the past 24 hours", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"The domain name and the number of domain names are adjustable according to the account number. The default is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5 minutes granularity, 1h: 1 hour granularity", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Grouping dimension
        # 
        # 1. The optional values are domain,province, and isp, which can pass multiple values.
        # 
        # 2. If there is an incoming, the detailed data will be displayed according to the dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceDataHitRateData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        hit_flow: str = None,
    ):
        # {"en":"time,
        # 
        # 1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00;
        # 
        # 2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1)00;
        # 
        # 3. Return to the time slice included in the start time and end time.", "zh_CN":"时间,
        # 1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00:00;
        # 2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 01,最后一个时间片是(yyyy-MM-dd+1)00;
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Byte hit ratio, retain 4 decimal places", "zh_CN":"字节命中率,保留4位小数"}
        self.value = value
        # {"en":"Hit traffic value, unit Byte", "zh_CN":"命中流量值,单位Byte"}
        self.hit_flow = hit_flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.hit_flow, 'hit_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.hit_flow is not None:
            result['hitFlow'] = self.hit_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('hitFlow') is not None:
            self.hit_flow = m.get('hitFlow')
        return self


class ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        hit_rate_data: List[ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceDataHitRateData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.hit_rate_data = hit_rate_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.hit_rate_data, 'hit_rate_data')
        if self.hit_rate_data:
            for k in self.hit_rate_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.hit_rate_data is not None:
            result['hitRateData'] = []
            for k in self.hit_rate_data:
                result['hitRateData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('hitRateData') is not None:
            self.hit_rate_data = []
            for k in m.get('hitRateData'):
                temp_model = ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceDataHitRateData()
                self.hit_rate_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceByteServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"Internet service providers", "zh_CN":"运营商"}
        self.isp = isp
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowHitRateIspProvinceByteServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceByteServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowHitRateIspProvinceByteServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowHitRateIspProvinceByteServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceByteServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowHitRateIspProvinceByteServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowHitRateIspProvinceByteServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowHitRateIspProvinceByteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceByteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceByteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowHitRateIspProvinceByteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainTotalTrafficDomainList(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        return self


class QueryDomainTotalTrafficRequest(TeaModel):
    def __init__(
        self,
        domain_list: QueryDomainTotalTrafficDomainList = None,
    ):
        # {"en":"Domain list.
        #   Domain number limits can be adjusted depending on different accounts. The default value is 20(if you want to adjust,please, contact technical support)", "zh_CN":"域名列表
        #   1.域名个数限制根据账号可调,默认为20个(可联系技术支持下单调整);"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            self.domain_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domain-list'] = self.domain_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-list') is not None:
            temp_model = QueryDomainTotalTrafficDomainList()
            self.domain_list = temp_model.from_map(m['domain-list'])
        return self


class QueryDomainTotalTrafficResponseFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: int = None,
    ):
        # {"en":"Date
        #   1.When the data query granularity is fiveminutes, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05 AM, and the last one is yyyy-MM-dd 24:00.
        #   2.When the data query granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is yyyy-MM-dd 24.
        #   3.When the data query granularity is daily, the format is yyyy-MM-dd; the data value of every time slice represents the value of the daily data.Return the time slice contained in start time and the time slice contained in end time", "zh_CN":"时间
        #   1.查询的数据粒度为fiveminutes时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是yyyy-MM-dd 24:00。
        #   2.查询的数据粒度为hourly时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是yyyy-MM-dd 24。
        #   3.查询的数据粒度为daily时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值。
        #   4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Traffic. Keep two digits of decimals. Unit: MB", "zh_CN":"流量,保留2位小数,单位为MB"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class QueryDomainTotalTrafficResponse(TeaModel):
    def __init__(
        self,
        flow_summary: int = None,
        flow_data: List[QueryDomainTotalTrafficResponseFlowData] = None,
    ):
        # {"en":"Total traffic. Keep two digits of decimals. Unit: MB", "zh_CN":"总流量,保留2位小数,单位为MB"}
        self.flow_summary = flow_summary
        # {"en":"flowData", "zh_CN":"流量数据"}
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.flow_summary, 'flow_summary')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_summary is not None:
            result['flow-summary'] = self.flow_summary
        if self.flow_data is not None:
            result['flow-data'] = []
            for k in self.flow_data:
                result['flow-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flow-summary') is not None:
            self.flow_summary = m.get('flow-summary')
        if m.get('flow-data') is not None:
            self.flow_data = []
            for k in m.get('flow-data'):
                temp_model = QueryDomainTotalTrafficResponseFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class QueryDomainTotalTrafficPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTotalTrafficParameters(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        type: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.And smaller than the current time and 'dateTo';
        # 3.Period between 'dataFrom' and 'dateTo' cannot be longer than 31 days", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过31天;4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than 'dateFrom';
        # 3.If it's greater than the current time, then the current time is assigned as the value", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Data granularity
        # 1.fiveminutes: five minutes, hourly: one hour, daily: one day;
        # 2.If not specified, daily is set as the default value;
        # 3.If fiveminutes is specified as the value, then data is returned in actual configured granularity when there is specific configuration to data collecting granularity for the customer.", "zh_CN":"数据粒度
        # 1.fiveminutes:5分钟,hourly:1小时,daily:1天;
        # 2.不传递,默认为daily;
        # 3.传递fiveminutes时,若客户数据采集粒度有特殊配置将按实际配置粒度返回。"}
        self.type = type

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryDomainTotalTrafficRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTotalTrafficResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class FlowChannelRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        is_exact_match: str = None,
        isp: str = None,
        result_type: str = None,
        optional_fields: str = None,
    ):
        # {"en":"cust_en_name ", "zh_CN":"客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM若没有输入时、分，则时分默认为00:01；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM,若没有输入时、分，则时分默认为24:00；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type:
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1.If there isp multiple inputs,use ';' as demimeter.
        # 2.optional values of isp: refers to the ISP-section of appendix.
        # 3.If not specified,means all the isp.", "zh_CN":"&nbsp;要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp = isp
        # {"en":"Display statistic result in merged or separate way:
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"flowInfo:displays bandwidth peak, peak time,and total flow information;", "zh_CN":"flowInfo ：展示带宽峰值、峰值时间、总流量信息；"}
        self.optional_fields = optional_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.isp is not None:
            result['isp'] = self.isp
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.optional_fields is not None:
            result['optionalFields'] = self.optional_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('optionalFields') is not None:
            self.optional_fields = m.get('optionalFields')
        return self


class FlowChannelResponseProviderDateChannelFlow(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'流量'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class FlowChannelResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        flow: List[FlowChannelResponseProviderDateChannelFlow] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'流量数据'}
        self.flow = flow

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.flow, 'flow')
        if self.flow:
            for k in self.flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.flow is not None:
            result['flow'] = []
            for k in self.flow:
                result['flow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('flow') is not None:
            self.flow = []
            for k in m.get('flow'):
                temp_model = FlowChannelResponseProviderDateChannelFlow()
                self.flow.append(temp_model.from_map(k))
        return self


class FlowChannelResponseProviderDate(TeaModel):
    def __init__(
        self,
        name: str = None,
        channel: FlowChannelResponseProviderDateChannel = None,
    ):
        # {'en':'name', 'zh_CN':'日期'}
        self.name = name
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('channel') is not None:
            temp_model = FlowChannelResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class FlowChannelResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: FlowChannelResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'频道流量数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.result_type, 'result_type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('date') is not None:
            temp_model = FlowChannelResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class FlowChannelResponse(TeaModel):
    def __init__(
        self,
        provider: FlowChannelResponseProvider = None,
    ):
        # {'en':'provider', 'zh_CN':'结果'}
        self.provider = provider

    def validate(self):
        self.validate_required(self.provider, 'provider')
        if self.provider:
            self.provider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['provider'] = self.provider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            temp_model = FlowChannelResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class FlowChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIspProvinceTotalServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        query_by: str = None,
        group_by: str = None,
    ):
        # {"en":"Start date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. Cannot exceed current time
        # 3. The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3. Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        # 4. Maximum allowed query time interval: 24 hours (with technical support adjustments), meaning that the difference between Date from and dateTo cannot exceed 24 hours.", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如 2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时;如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔:24小时(可联系技术支持调整)，即dateFrom和dateTo相差不能超过24小时。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The maximum number of TLDs that can be delivered is 20 by default (contact technical support adjustment);
        # 2. Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3. Domain name exceeding limit, misstatement", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        # 3.域名超过上限，提示错误"}
        self.domain = domain
        # {"en":"Data granularity: 
        # 1. default 1m
        # 2. 1m (1 minute), 5m (5 minutes)", "zh_CN":"数据粒度:
        # 1.不传默认1m
        # 2.支持1m(1分钟)、5m(5分钟)"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"query dimensionality:
        # 1. Optional value flow, request,bandwidth
        # 2. Default flow
        # 3. Flow: Flow, keep two decimal places;
        # 4. Request: number of Request;
        # 5. bandwidth: bandwidth, keep two decimal places", "zh_CN":"查询维度:
        # 1.可选值 flow、request、bandwidth
        # 2.传默认 flow
        # 3.flow:流量，保留两位小数;
        # 4.request:请求数;
        # 5.bandwidth:带宽，保留两位小数"}
        self.query_by = query_by
        # {"en":"Optional: domain, all, If it is empty, it defaults to returning by domain dimension;
        # If all is passed, merge and return according to the query domain name.", "zh_CN":"可选项：domain、all, 为空则默认为按domain维度返回;
        # 若传递all，则按查询域名合并返回"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.query_by is not None:
            result['queryBy'] = self.query_by
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowIspProvinceTotalServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time, in yyyy-MM-dd HH:MM", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"1. Flow: Flow, keep two decimal places;
        #             2. Bandwidth: Bandwidth, keep two decimals;
        #             3. Request: number of Request", "zh_CN":"1.flow：流量，保留两位小数；
        #             2.bandwidth: 带宽，保留两位小数；
        #             3.request：请求数"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportFlowIspProvinceTotalServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportFlowIspProvinceTotalServiceResponseDataDetailList] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"detailList", "zh_CN":"数据明细"}
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowIspProvinceTotalServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceTotalServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowIspProvinceTotalServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"data", "zh_CN":"数据结果"}
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
                temp_model = ReportFlowIspProvinceTotalServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceTotalServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceTotalServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceTotalServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceTotalServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class WctQueryRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        transcoding: str = None,
        transcoding_type: str = None,
        space: str = None,
        provider: str = None,
        region: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"trans;hevc;audio_trans;encap_trans;vframe;file_op;trans_nbhd;hevc_nbhd;video_enhance;drm.", "zh_CN":"转码操作类型：trans(H.264视频转码);hevc(H.265视频转码);audio_trans(音频转码);encap_trans(转封装);vframe(截图);file_op(文件处理);trans_nbhd(H.264智控高清视频转码);hevc_nbhd(H.265智控高清视频转码);video_enhance(AI视频增强);drm(DRM加密)"}
        self.transcoding = transcoding
        # {"en":"sd240;sd480;sd720;hd1080;2k;4k.", "zh_CN":"梯度: sd240;sd480;sd720;hd1080;2k;4k"}
        self.transcoding_type = transcoding_type
        # {"en":"space .", "zh_CN":"空间，多个值请用英文分号“;”分割"}
        self.space = space
        # {"en":"provider .", "zh_CN":"功能来源，提供方。多个值请用英文分号“;”分割"}
        self.provider = provider
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.transcoding is not None:
            result['transcoding'] = self.transcoding
        if self.transcoding_type is not None:
            result['transcodingType'] = self.transcoding_type
        if self.space is not None:
            result['space'] = self.space
        if self.provider is not None:
            result['provider'] = self.provider
        if self.region is not None:
            result['region'] = self.region
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('transcoding') is not None:
            self.transcoding = m.get('transcoding')
        if m.get('transcodingType') is not None:
            self.transcoding_type = m.get('transcodingType')
        if m.get('space') is not None:
            self.space = m.get('space')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class WctQueryResponseProviderDateWctData(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'明细数'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class WctQueryResponseProviderDateWct(TeaModel):
    def __init__(
        self,
        type: str = None,
        total: str = None,
        data: List[WctQueryResponseProviderDateWctData] = None,
    ):
        # {'en':'type', 'zh_CN':'类型'}
        self.type = type
        # {'en':'total', 'zh_CN':'总数'}
        self.total = total
        # {'en':'data', 'zh_CN':'明细数据'}
        self.data = data

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.total, 'total')
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
        if self.type is not None:
            result['type'] = self.type
        if self.total is not None:
            result['total'] = self.total
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = WctQueryResponseProviderDateWctData()
                self.data.append(temp_model.from_map(k))
        return self


class WctQueryResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        customer_id: str = None,
        transcoding: str = None,
        transcoding_type: str = None,
        unit: str = None,
        total: str = None,
        wct: WctQueryResponseProviderDateWct = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'customerId', 'zh_CN':'客户id'}
        self.customer_id = customer_id
        # {'en':'transcoding', 'zh_CN':'转码类型'}
        self.transcoding = transcoding
        # {'en':'transcodingType', 'zh_CN':'梯度'}
        self.transcoding_type = transcoding_type
        # {'en':'unit', 'zh_CN':'单位'}
        self.unit = unit
        # {'en':'total', 'zh_CN':'总数'}
        self.total = total
        # {'en':'wct', 'zh_CN':'转码数据'}
        self.wct = wct

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.customer_id, 'customer_id')
        self.validate_required(self.transcoding, 'transcoding')
        self.validate_required(self.transcoding_type, 'transcoding_type')
        self.validate_required(self.unit, 'unit')
        self.validate_required(self.total, 'total')
        self.validate_required(self.wct, 'wct')
        if self.wct:
            self.wct.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.transcoding is not None:
            result['transcoding'] = self.transcoding
        if self.transcoding_type is not None:
            result['transcodingType'] = self.transcoding_type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.total is not None:
            result['total'] = self.total
        if self.wct is not None:
            result['wct'] = self.wct.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('transcoding') is not None:
            self.transcoding = m.get('transcoding')
        if m.get('transcodingType') is not None:
            self.transcoding_type = m.get('transcodingType')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('wct') is not None:
            temp_model = WctQueryResponseProviderDateWct()
            self.wct = temp_model.from_map(m['wct'])
        return self


class WctQueryResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: WctQueryResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'转码数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = WctQueryResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class WctQueryResponse(TeaModel):
    def __init__(
        self,
        provider: WctQueryResponseProvider = None,
    ):
        # {'en':'provider', 'zh_CN':'结果'}
        self.provider = provider

    def validate(self):
        self.validate_required(self.provider, 'provider')
        if self.provider:
            self.provider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['provider'] = self.provider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            temp_model = WctQueryResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class WctQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WctQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WctQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WctQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainTrafficUnderSpecificSettlementAreaRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        area_code: str = None,
    ):
        # {"en":"Start time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.And smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 31 days;4.You can only query data for the last 2 years(technical support can be contacted to adjust).", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过31天(可联系技术支持调整);4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain list, and all domains are queried if this field is not specified;", "zh_CN":"域名列表,不传递则查询全部域名;"}
        self.domain = domain
        # {"en":"Data granularity
        # 
        # 1.Options: 5m(5 minutes), 1h(1 hour) and 1d(1 day);
        # 2.Default value of 1d is used if the field is not specified;
        # 3.If 5m is specified as the value, then data is returned in actual configured granularity when there is specific configuration to data collecting granularity for the customer.", "zh_CN":"数据粒度
        # 1.可选值为:5m(5分钟)、1h(1小时)、1d(1天);
        # 2.不传时默认为1d;
        # 3.传递5m时,若客户数据采集粒度有特殊配置将按实际配置粒度返回。"}
        self.data_interval = data_interval
        # {"en":"Queried area
        # 1.Use  English semicolon to separate two areas;
        # 2.Options: cn, nc, ov, apac, am, euna, emea, sa, af, au, hk, tw 
        #  ...;", "zh_CN":"查询区域
        # 1.多个区域使用英文分号分隔
        # 2.可选值为:cn、nc、ov、apac、am、euna、emea、sa、af、au、hk、tw等;"}
        self.area_code = area_code

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.area_code, 'area_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaResponseFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
    ):
        # {"en":"time
        # 1. When the data granularity of the query is fiveminutes, the format is yyyy-MM-dd HH: MM; Each time slice data value represents the data value in the previous time granularity range. The time slice at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is yyyy-MM-dd 24:00.
        # 2. When the data granularity of query is hourly, the format is yyyy-MM-dd HH. Each time slice data value represents the data value in the previous time granularity range. The time slice at the beginning of the day is yyyy-MM-dd 01, and the last time slice is yyyy-MM-dd 24.
        # 3. when the data granularity of query is daily, the format is yyyy-MM-dd; The value of data for each time slice represents the value of the data within that day;
        # 4. return the time slice contained in the start and end times.", "zh_CN":"时间
        # 1.查询的数据粒度为fiveminutes时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是yyyy-MM-dd 24:00。
        # 2.查询的数据粒度为hourly时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是yyyy-MM-dd 24。
        # 3.查询的数据粒度为daily时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值;
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Traffic, 2 decimal places, in MB", "zh_CN":"流量,保留2位小数,单位为MB"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaResponse(TeaModel):
    def __init__(
        self,
        flow_summary: str = None,
        flow_data: List[QueryDomainTrafficUnderSpecificSettlementAreaResponseFlowData] = None,
    ):
        # {"en":"Total traffic, 2 decimal places, in MB", "zh_CN":"总流量,保留2位小数,单位为MB"}
        self.flow_summary = flow_summary
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.flow_summary, 'flow_summary')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_summary is not None:
            result['flow-summary'] = self.flow_summary
        if self.flow_data is not None:
            result['flow-data'] = []
            for k in self.flow_data:
                result['flow-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flow-summary') is not None:
            self.flow_summary = m.get('flow-summary')
        if m.get('flow-data') is not None:
            self.flow_data = []
            for k in m.get('flow-data'):
                temp_model = QueryDomainTrafficUnderSpecificSettlementAreaResponseFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTrafficUnderSpecificSettlementAreaResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIspProvinceShortTimeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:00:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.;", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 1 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 7 hours, that is, the difference between dateFrom and dateTo can not exceed 2 hours ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的1小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：2小时。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error , you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).", "zh_CN":"域名：
        # 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)；
        # 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1m: 1 minute granularity;
        # 5m: 5 minute granularity, Default value is 5m;
        # 1h: 1 hour granularity.", "zh_CN":"数据粒度：
        # 1m：1分钟粒度；
        # 5m：5分钟粒度。不传默认5分钟粒度；
        # 1h：1小时粒度。"}
        self.data_interval = data_interval
        # {"en":"Province
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces;
        # 2.Province is upload: Send province code, multiple can be sent. Please refer to the appendix description section of the overview page for the provincial information code table.", "zh_CN":"省份
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 2.有传递province时：省份传code，可传多个。省份信息码表详见概览页附录说明章节"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs;
        # 2.ISPs is upload: Send isp code, multiple can be sent. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商： 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 2.有传递isp时：运营商 传code，可传多个。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Group dimension
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 2.The data is displayed according to the specified dimension.", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据。"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        bandwidth: str = None,
    ):
        # {"en":"timestamp", "zh_CN":"时间"}
        self.timestamp = timestamp
        # {"en":"Traffic unit is MB and 2 digits   of decimals allowed", "zh_CN":"流量值,单位为MB,保留两位小数"}
        self.value = value
        # {"en":"Bandwidth value. Unit is Mbps and   2 digits of decimals allowed", "zh_CN":"带宽值,单位为Mbps,保留两位小数"}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self


class ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        flow_data: List[ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceDataFlowData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"flowdata", "zh_CN":"流量数据"}
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceShortTimeServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"province", "zh_CN":"省份数据"}
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowIspProvinceShortTimeServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceShortTimeServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowIspProvinceShortTimeServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"isp", "zh_CN":"ISP数据"}
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowIspProvinceShortTimeServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceShortTimeServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowIspProvinceShortTimeServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowIspProvinceShortTimeServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceShortTimeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceShortTimeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceShortTimeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceShortTimeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryEdgeByteHitRatioServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:00:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.;", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：7天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 1.Domain is not uploaded: Query all domain names of the account (More than 200 domains will error , you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 200 domains are supported (you can contact technical support for adjustment).", "zh_CN":"域名：
        # 1.未传递domain时：查询账号下所有全部域名(域名超过200个则报错，可联系技术支持调整)；
        # 2.有传递domain时：域名最多支持传200个（可联系技术支持调整）。"}
        self.domain = domain

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
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class QueryEdgeByteHitRatioServiceResponseResultHitRatioDatas(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        edge_hit_ratio: str = None,
    ):
        # {"en":"timestamp", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；"}
        self.timestamp = timestamp
        # {"en":"edge node hit ratio,keep 4 decimal places", "zh_CN":"边缘节点缓存字节命中率，保留4位小数"}
        self.edge_hit_ratio = edge_hit_ratio

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.edge_hit_ratio, 'edge_hit_ratio')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.edge_hit_ratio is not None:
            result['edgeHitRatio'] = self.edge_hit_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('edgeHitRatio') is not None:
            self.edge_hit_ratio = m.get('edgeHitRatio')
        return self


class QueryEdgeByteHitRatioServiceResponseResult(TeaModel):
    def __init__(
        self,
        real_date: str = None,
        total_avg: str = None,
        hit_ratio_datas: List[QueryEdgeByteHitRatioServiceResponseResultHitRatioDatas] = None,
    ):
        # {"en":"Actually processed time.  yyyy-MM-dd HH:mm format", "zh_CN":"实际查询时间，格式 yyyy-MM-dd HH:mm"}
        self.real_date = real_date
        # {"en":"Average of total edge node hit ratio", "zh_CN":"总边缘节点命中率的平均值,2位小数"}
        self.total_avg = total_avg
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
        self.hit_ratio_datas = hit_ratio_datas

    def validate(self):
        self.validate_required(self.real_date, 'real_date')
        self.validate_required(self.total_avg, 'total_avg')
        self.validate_required(self.hit_ratio_datas, 'hit_ratio_datas')
        if self.hit_ratio_datas:
            for k in self.hit_ratio_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_date is not None:
            result['realDate'] = self.real_date
        if self.total_avg is not None:
            result['totalAvg'] = self.total_avg
        if self.hit_ratio_datas is not None:
            result['hitRatioDatas'] = []
            for k in self.hit_ratio_datas:
                result['hitRatioDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('realDate') is not None:
            self.real_date = m.get('realDate')
        if m.get('totalAvg') is not None:
            self.total_avg = m.get('totalAvg')
        if m.get('hitRatioDatas') is not None:
            self.hit_ratio_datas = []
            for k in m.get('hitRatioDatas'):
                temp_model = QueryEdgeByteHitRatioServiceResponseResultHitRatioDatas()
                self.hit_ratio_datas.append(temp_model.from_map(k))
        return self


class QueryEdgeByteHitRatioServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryEdgeByteHitRatioServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryEdgeByteHitRatioServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryEdgeByteHitRatioServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeByteHitRatioServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeByteHitRatioServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeByteHitRatioServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUpFlowDomainCountryServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        country_code: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Starting time
        # 
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00);
        # 2. Cannot be greater than the current time
        # 3. Get up to the last six months (183 days) of data.","zh_CN":"开始时间
        # 1. 时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2. 不能大于当前时间
        # 3. 最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. Time format 2016-12-02T10:00:00+08:00
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one untransmitted, throw an exception
        # 4. Allow query maximum time interval: 7 days, that is, the difference between dateFrom and dateTo can&rsquo;t exceed 7 days (can contact technical support adjustment, up to 31 days).","zh_CN":"结束时间:
        # 1. 时间格式2016-12-02T10:00:00+08:00
        # 2. 结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3. dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常
        # 4. 允许查询最大时间间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整，最长31天)。"}
        self.date_to = date_to
        # {"en":"Domains: 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment); 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).","zh_CN":"域名： 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)； 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. Support 5m (5 minutes granularity),1d (1 day granularity)
        # 2. Do not pass the default to 5m","zh_CN":"数据粒度:
        # 1. 支持5m(5分钟粒度),1d(天粒度)
        # 2. 不传默认为5m"}
        self.data_interval = data_interval
        # {"en":"Country code:
        # 
        # 1. Do not pass the default query for all countries and regions;
        # 2. The values that can be passed are detailed in the Countrycode list of appendix table on the API Overview page","zh_CN":"国家地区代号:
        # 1. 不传默认查询全部国家地区;
        # 2. 可传递的值详见概览页国家地区列表说明。"}
        self.country_code = country_code
        # {"en":"Grouping dimension:
        # 
        # 1. Optional values domain, country and aggregatedOversea, can pass in single or multiple values. The aggregatedOversea and country cannot be passed at the same time;
        # 
        # 2. If there is an incoming, the detailed data will be displayed according to the dimension:
        # domain: Group display by domain name dimension;
        # country: Group display by country dimension;
        # aggregatedOversea: Group display according to domestic and overseas dimensions.
        # 3. The result hierarchy is fixed in order, and the order of the parameters does not affect the order of the returned results. For example: 'groupBy': ['domain','country'] and 'groupBy': ['country','domain'] return the same result.","zh_CN":"1. 可选值domain、country、aggregatedOversea,可传入单个或多个值,其中不能同时传aggregatedOversea 和 country;2. 有传入则按照该维度展示明细数据:1.domain:按照域名维度进行分组展示;2.domain:country:按照国家维度进行分组展示;3.aggregatedOversea:按照国内 和 海外维度进行分组展示3. 返回结果层级顺序固定,入参顺序不影响返回结果顺序。例如:groupBy: [domain,country]与groupBy: [country,domain]返回结果一样。"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportUpFlowDomainCountryServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUpFlowDomainCountryServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUpFlowDomainCountryServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUpFlowDomainCountryServiceResponseDataCountryDataFlowData(TeaModel):
    def __init__(
        self,
        bandwidth: str = None,
        value: str = None,
        timestamp: str = None,
    ):
        # {"en":"Bandwidth value. Unit is Mbps and 2 digits of decimals are allowed.","zh_CN":"带宽值,单位Mbps,保留2位小数"}
        self.bandwidth = bandwidth
        # {"en":"Flow value, in megabytes, 2 decimal places","zh_CN":"流量值,计量单位MB,保留2位小数"}
        self.value = value
        # {"en":"1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value in the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. Returns the time slice contained in the start time and end time.","zh_CN":"1. 查询的数据粒度为5m时,格式为yyyy-MM-dd  HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd  00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00。2. 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp

    def validate(self):
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.value, 'value')
        self.validate_required(self.timestamp, 'timestamp')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.value is not None:
            result['value'] = self.value
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ReportUpFlowDomainCountryServiceResponseDataCountryData(TeaModel):
    def __init__(
        self,
        flow_percentage: str = None,
        country_code: str = None,
        flow_sum: str = None,
        flow_data: List[ReportUpFlowDomainCountryServiceResponseDataCountryDataFlowData] = None,
        country_name: str = None,
    ):
        # {"en":"National regional traffic ratio: the proportion (percentage) of traffic value in a single country region during the query period, retaining 2 decimal places","zh_CN":"国家地区流量占比:单个国家地区流量在查询时段内的流量值的占比(百分比),保留2位小数"}
        self.flow_percentage = flow_percentage
        # {"en":"Country code","zh_CN":"国家地区代号"}
        self.country_code = country_code
        # {"en":"Summary of traffic in national regions: Summary of traffic flow in a single country region during the query period, unit of measure MB, retaining 2 decimal places","zh_CN":"国家地区流量汇总:单个国家地区流量在查询时段内的流量汇总值,计量单位MB,保留2位小数"}
        self.flow_sum = flow_sum
        # {"en":"","zh_CN":""}
        self.flow_data = flow_data
        # {"en":"Country name","zh_CN":"国家地区名称"}
        self.country_name = country_name

    def validate(self):
        self.validate_required(self.flow_percentage, 'flow_percentage')
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.flow_sum, 'flow_sum')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()
        self.validate_required(self.country_name, 'country_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_percentage is not None:
            result['flowPercentage'] = self.flow_percentage
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.flow_sum is not None:
            result['flowSum'] = self.flow_sum
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        if self.country_name is not None:
            result['countryName'] = self.country_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowPercentage') is not None:
            self.flow_percentage = m.get('flowPercentage')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('flowSum') is not None:
            self.flow_sum = m.get('flowSum')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportUpFlowDomainCountryServiceResponseDataCountryDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        if m.get('countryName') is not None:
            self.country_name = m.get('countryName')
        return self


class ReportUpFlowDomainCountryServiceResponseData(TeaModel):
    def __init__(
        self,
        country_data: List[ReportUpFlowDomainCountryServiceResponseDataCountryData] = None,
        domain: str = None,
    ):
        # {"en":"","zh_CN":""}
        self.country_data = country_data
        # {"en":"Domain","zh_CN":"域名"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.country_data, 'country_data')
        if self.country_data:
            for k in self.country_data:
                if k:
                    k.validate()
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_data is not None:
            result['countryData'] = []
            for k in self.country_data:
                result['countryData'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryData') is not None:
            self.country_data = []
            for k in m.get('countryData'):
                temp_model = ReportUpFlowDomainCountryServiceResponseDataCountryData()
                self.country_data.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ReportUpFlowDomainCountryServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ReportUpFlowDomainCountryServiceResponseData] = None,
        message: str = None,
    ):
        # {"en":"Request result status code","zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Data","zh_CN":"结果"}
        self.data = data
        # {"en":"Request result information","zh_CN":"请求结果信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = ReportUpFlowDomainCountryServiceResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ReportUpFlowDomainCountryServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBacktoOriginTrafficAndRequestRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
        backsrc_only: int = None,
    ):
        # {'en':'Start time: 
        # 1. Start time: time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (December 2rd, 2016, 10:00 a.m., Beijing Time); 
        # 2. Not greater than the current time 
        # 3. The data can be queried is the last week (183 days).', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time: 
        # 1. The time format is 2016-12-02T10:00:00+08:00 
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used. 
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default; if one field is filled and one is left empty, then exception will occur. 
        # 4. Maximum query time interval allowed: 1 day by default, that is, the difference between dateFrom and dateTo cannot exceed 1 day (you can contact technical support to adjust it, the maximum adjustment is 31 days)', 'zh_CN':'结束时间：
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 5.允许查询最大时间间隔：默认1天，即dateFrom和dateTo相差不能超过1天（可联系技术支持调整，最大调整到31天）。'}
        self.date_to = date_to
        # {'en':'Data granularity: 
        # 1. Support 5m (granularity of 5 minutes) and 1m
        # 2. 5m by default if the value is empty', 'zh_CN':'数据粒度：
        # 1、支持5m（5分钟）。和 1m（1分钟）
        # 2、不传默认5m。'}
        self.data_interval = data_interval
        # {'en':'Domain name: 
        # 1. The default upper limit of domains that can be entered is 200 (if you want to adjust, please, contact technical support); 
        # 2. All domains under the account will be queried if this input parameter is not specified. But if the number of domains under the account exceeds the limits, no query will be executed (Error)', 'zh_CN':'域名：
        # 1、可传递域名数量上限默认为200个（可联系技术支持调整）；
        # 2、未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询（报错）。'}
        self.domain = domain
        # {'en':'Grouping keywords:
        # 1. By default, data will be displayed by group;
        # 2. If there are keywords entered, value details shall be displayed by keywords; If groupBy is specified as domain, it means the results are returned according to domains. 
        # 3. Only domain can be specified', 'zh_CN':'分组关键词：
        # 1、默认聚合展示；
        # &nbsp; 2、传入关键词则代表需要按照关键词对应的值展示明细；
        # 例如groupBy传domain，则代表返回按照domain明细展开。
        # 3、只能传递domain。'}
        self.group_by = group_by
        # {'en':'Optional values 0, 1. 
        # Input 0 returns all data, input 1 only returns source site data, default is0&nbsp;', 'zh_CN':'可选值 0、1 。入参 0 则返回全部数据，入参 1 则只返回回源站数据，默认为 0'}
        self.backsrc_only = backsrc_only

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
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.domain is not None:
            result['domain'] = self.domain
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        if self.backsrc_only is not None:
            result['backsrcOnly'] = self.backsrc_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        if m.get('backsrcOnly') is not None:
            self.backsrc_only = m.get('backsrcOnly')
        return self


class QueryBacktoOriginTrafficAndRequestResponseResultFlowRequestOriginData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
        bandwidth: str = None,
        request: str = None,
    ):
        # {'en':'1. When the querying data granularity is 5m, then the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00. 
        #         2. Return the time slices that contained in start time and in end time.', 'zh_CN':'1.查询的数据粒度为5m时，格式为yyyy-MM-dd &nbsp; HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） &nbsp; 00:00。
        #         2.返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Traffic unit is MB and keep the number to two decimal places', 'zh_CN':'流量值，单位MB，保留2位小数；'}
        self.flow = flow
        # {'en':'Bandwidth, unit: Mbps, 2 decimal places reserved, example (931556.21)', 'zh_CN':'带宽，单位：Mbps，保留两位小数'}
        self.bandwidth = bandwidth
        # {'en':'Total number of requests', 'zh_CN':'请求数'}
        self.request = request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class QueryBacktoOriginTrafficAndRequestResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        total_flow: str = None,
        total_request: str = None,
        peak_request: str = None,
        peak_request_time: str = None,
        peak_bandwidth: str = None,
        peak_bandwidth_time: str = None,
        flow_request_origin_data: List[QueryBacktoOriginTrafficAndRequestResponseResultFlowRequestOriginData] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'totalFlow, unit :MB, 2 decimal places reserved, example (74099.92)', 'zh_CN':'总流量，单位MB，保留两位小时'}
        self.total_flow = total_flow
        # {'en':'totalRequest', 'zh_CN':'总请求数'}
        self.total_request = total_request
        # {'en':'peak of Request', 'zh_CN':'请求数峰值'}
        self.peak_request = peak_request
        # {'en':'peaktime of Request', 'zh_CN':'请求数峰值时间'}
        self.peak_request_time = peak_request_time
        # {'en':'peakBandwidth, unit :Mbps, 2 decimal places reserved, example (74099.92)', 'zh_CN':'带宽峰值，单位Mbps，保留2位小数，示例 （931556.21）'}
        self.peak_bandwidth = peak_bandwidth
        # {'en':'Peak time of Bandwidth', 'zh_CN':'带宽峰值时间'}
        self.peak_bandwidth_time = peak_bandwidth_time
        self.flow_request_origin_data = flow_request_origin_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.peak_request, 'peak_request')
        self.validate_required(self.peak_request_time, 'peak_request_time')
        self.validate_required(self.peak_bandwidth, 'peak_bandwidth')
        self.validate_required(self.peak_bandwidth_time, 'peak_bandwidth_time')
        self.validate_required(self.flow_request_origin_data, 'flow_request_origin_data')
        if self.flow_request_origin_data:
            for k in self.flow_request_origin_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.peak_request is not None:
            result['peakRequest'] = self.peak_request
        if self.peak_request_time is not None:
            result['peakRequestTime'] = self.peak_request_time
        if self.peak_bandwidth is not None:
            result['peakBandwidth'] = self.peak_bandwidth
        if self.peak_bandwidth_time is not None:
            result['peakBandwidthTime'] = self.peak_bandwidth_time
        if self.flow_request_origin_data is not None:
            result['flowRequestOriginData'] = []
            for k in self.flow_request_origin_data:
                result['flowRequestOriginData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('peakRequest') is not None:
            self.peak_request = m.get('peakRequest')
        if m.get('peakRequestTime') is not None:
            self.peak_request_time = m.get('peakRequestTime')
        if m.get('peakBandwidth') is not None:
            self.peak_bandwidth = m.get('peakBandwidth')
        if m.get('peakBandwidthTime') is not None:
            self.peak_bandwidth_time = m.get('peakBandwidthTime')
        if m.get('flowRequestOriginData') is not None:
            self.flow_request_origin_data = []
            for k in m.get('flowRequestOriginData'):
                temp_model = QueryBacktoOriginTrafficAndRequestResponseResultFlowRequestOriginData()
                self.flow_request_origin_data.append(temp_model.from_map(k))
        return self


class QueryBacktoOriginTrafficAndRequestResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryBacktoOriginTrafficAndRequestResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryBacktoOriginTrafficAndRequestResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryBacktoOriginTrafficAndRequestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBacktoOriginTrafficAndRequestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBacktoOriginTrafficAndRequestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBacktoOriginTrafficAndRequestResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowRequestMultiIPVersionServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        query_by: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.Cannot exceed current time 
        # 	3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2021-05-19T10:00:00+08:00(为北京时间2021年5月19日10点0分0秒)
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time. 
        # 	3.If both fields of dataFrom and dateTo are left empty, the default query past 1 day; If there is only one unsent, throw an exception 
        # 	4.Maximum allowed query time interval: 1 days, Date from and dateTo, not more than 1 days", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:1天,即dateFrom和dateTo相差不能超过1天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support). 
        # 	2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)", "zh_CN":"域名:
        # 1、可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2、自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"Data granularity: 
        # 	1.Support for 1m(1 minutes), 5m (5 minutes), 1h (1 hour) 
        # 	2.Default 5m
        # ", "zh_CN":"数据粒度:
        # 1、支持1m(1分钟)、5m(5分钟)、1h(1小时)
        # 2、不传默认5m"}
        self.data_interval = data_interval
        # {"en":"1. Optional value:bandwidth, request 2. Default bandwidth", "zh_CN":"1.可选值:bandwidth、request
        # 2.不传默认bandwidth"}
        self.query_by = query_by
        # {"en":"1.Selection:domain 2.If groupBy left empty, merge date of all domains", "zh_CN":"可选值:domain
        # 不传默认聚合所有频道数据"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.query_by is not None:
            result['queryBy'] = self.query_by
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowRequestMultiIPVersionServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        v_4value: str = None,
        v_6value: str = None,
    ):
        # {"en":"timestamp,Returns the timestamp between the start time and end time. 
        # 				 Time format: 
        # 				 Minutes: yyyy-MM-dd HH:mm 
        # 				 Hours: yyyy-MM-dd HH", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。
        # 时间格式:
        # 1/5分钟:yyyy-MM-dd HH:mm
        # 1小时:yyyy-MM-dd HH"}
        self.timestamp = timestamp
        # {"en":"Ipv4 (Bandwidth unit is Mbps, number of requests is in units", "zh_CN":"IPv4数据（带宽单位 Mbps，请求数单位 个）"}
        self.v_4value = v_4value
        # {"en":"Ipv6 (Bandwidth unit is Mbps, number of requests is in units", "zh_CN":"IPv6数据（带宽单位 Mbps，请求数单位 个）"}
        self.v_6value = v_6value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.v_4value, 'v_4value')
        self.validate_required(self.v_6value, 'v_6value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.v_4value is not None:
            result['v4Value'] = self.v_4value
        if self.v_6value is not None:
            result['v6Value'] = self.v_6value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('v4Value') is not None:
            self.v_4value = m.get('v4Value')
        if m.get('v6Value') is not None:
            self.v_6value = m.get('v6Value')
        return self


class ReportFlowRequestMultiIPVersionServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportFlowRequestMultiIPVersionServiceResponseDataDetailList] = None,
    ):
        # {"en":"Domain. If merge date of all domains will not return domain", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
        self.domain = domain
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowRequestMultiIPVersionServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowRequestMultiIPVersionServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowRequestMultiIPVersionServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"request result information", "zh_CN":"请求结果信息"}
        self.message = message
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
                temp_model = ReportFlowRequestMultiIPVersionServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowRequestMultiIPVersionServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowRequestMultiIPVersionServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowRequestMultiIPVersionServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowRequestMultiIPVersionServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried;", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术人员调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据;"}
        self.date_from = date_from
        # {"en":"End time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名:可传递域名数量上限默认为20个(可联系技术支持调整),未传递该入参时查询账号下所有域名,但当账号下域名数量超过限制时不可查询(报错)。"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5-minute  granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Group dimension
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowIspProvinceServiceResponseResultIspDataProvinceDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        bandwidth: str = None,
    ):
        # {"en":"timestamp", "zh_CN":"时间"}
        self.timestamp = timestamp
        # {"en":"Traffic unit is MB and 2 digits   of decimals allowed", "zh_CN":"流量值,单位为MB,保留两位小数"}
        self.value = value
        # {"en":"Bandwidth value. Unit is Mbps and   2 digits of decimals allowed", "zh_CN":"带宽值,单位为Mbps,保留两位小数"}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self


class ReportFlowIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        flow_data: List[ReportFlowIspProvinceServiceResponseResultIspDataProvinceDataFlowData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"flowdata", "zh_CN":"流量数据"}
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = ReportFlowIspProvinceServiceResponseResultIspDataProvinceDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"province", "zh_CN":"省份数据"}
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportFlowIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowIspProvinceServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"isp", "zh_CN":"ISP数据"}
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportFlowIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowIspProvinceServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = ReportFlowIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDirectoryBandwidthTrafficUnderLivestreamDomainRequestDomainDir(TeaModel):
    def __init__(
        self,
        domain: str = None,
        dir: List[str] = None,
    ):
        # {"en":"Domain:
        # 1.Need to meet the regular expression rules that are used to validate domains;
        # 2.Domain number limits can be adjusted depending on different accounts. The default value is 20;", "zh_CN":"域名:
        # 1.需要满足域名的正则校验;
        # 2.域名个数限制根据账号可调,默认为20个;"}
        self.domain = domain
        # {"en":"Table of contents:
        # 1.Empty value means to query all directories under the domain
        # 2.Directory limits can be adjusted depending on different accounts. The default value is 200(this limit applies to the empty value);
        # 3.Invalid directories are not returned", "zh_CN":"目录:
        # 1.目录个数限制根据账号可调,默认为200个;
        # 2.不传代表查询该域名下的所有目录,同时接受目录个数限制;
        # 3.无效的目录不返回"}
        self.dir = dir

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.dir is not None:
            result['dir'] = self.dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain_dir: List[QueryDirectoryBandwidthTrafficUnderLivestreamDomainRequestDomainDir] = None,
        protocol_type: str = None,
        data_interval: str = None,
        data_type: str = None,
    ):
        # {"en":"Start time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);4.You can only query data for the last 2 years.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        self.domain_dir = domain_dir
        # {"en":"Query protocol:
        # 1.Means query statistics with http protocol or with https protocol;
        # 2.Values can be selected: http or https;
        # 3.Empty means both http and https;", "zh_CN":"查询协议:
        # 1.代表统计http协议或https协议;
        # 2.可选值:http 或 https;
        # 3.不传默认代表不区分http和https;"}
        self.protocol_type = protocol_type
        # {"en":"Query granularity:
        # 1.Empty value means 5 minutes of granularity by default;
        # 2.Values can be selected: 5m or 1m;
        # 3.Option of 1m can be configured in flowDirDataIntervalConfig depending on differrent accounts;", "zh_CN":"查询粒度:
        # 1.不传默认代表5分钟粒度;
        # 2.可选值:5m 或 1m;
        # 3.1m选项根据账号在数据字典flowDirDataIntervalConfig中可配;"}
        self.data_interval = data_interval
        # {"en":"Query type
        # 
        # 1.Values can be selected: flow or bandwidth;
        # 
        # 2.bandwidth means to get bandwidth value, flow means to get the flow vaule. By default, data in all regions is queried;", "zh_CN":"查询类型
        # 1.可选值:flow 或bandwidth;
        # 2.bandwidth代表获取带宽值,flow代表获取流量值,默认查询所有区域的数据;"}
        self.data_type = data_type

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.domain_dir, 'domain_dir')
        if self.domain_dir:
            for k in self.domain_dir:
                if k:
                    k.validate()
        self.validate_required(self.data_type, 'data_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain_dir is not None:
            result['domainDir'] = []
            for k in self.domain_dir:
                result['domainDir'].append(k.to_map() if k else None)
        if self.protocol_type is not None:
            result['protocolType'] = self.protocol_type
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.data_type is not None:
            result['dataType'] = self.data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domainDir') is not None:
            self.domain_dir = []
            for k in m.get('domainDir'):
                temp_model = QueryDirectoryBandwidthTrafficUnderLivestreamDomainRequestDomainDir()
                self.domain_dir.append(temp_model.from_map(k))
        if m.get('protocolType') is not None:
            self.protocol_type = m.get('protocolType')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetailsDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Date
        # 1.When the data query granularity is 1m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00;
        # 2.When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 3.Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间
        # 1.查询的数据粒度为1m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd  00:01,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 2.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd  00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Data of the time point, two  decimal digits", "zh_CN":"时间点的数据,保留2位小数"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetails(TeaModel):
    def __init__(
        self,
        dir: str = None,
        total_flow: str = None,
        bandwidth_peak_value: str = None,
        details: List[QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetailsDetails] = None,
    ):
        # {"en":"Directory", "zh_CN":"目录"}
        self.dir = dir
        # {"en":"Return when the dataType is flow; Total flow of every stream. Unit is MB and 2 digits of decimals allowed;", "zh_CN":"当dataType为flow时返回;每路流的总流量单位MB,保留2位小数;"}
        self.total_flow = total_flow
        # {"en":"Return when the dataType is bandwidth;
        # 
        # Bandwidth peak value of every stream within specified time. Unit is Mbps, two decimals digits;", "zh_CN":"当dataType为bandwidth时返回;
        # 每路流在该时间段内的带宽峰值单位Mbps,保留2位小数;"}
        self.bandwidth_peak_value = bandwidth_peak_value
        self.details = details

    def validate(self):
        self.validate_required(self.dir, 'dir')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.bandwidth_peak_value, 'bandwidth_peak_value')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir is not None:
            result['dir'] = self.dir
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.bandwidth_peak_value is not None:
            result['bandwidthPeakValue'] = self.bandwidth_peak_value
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('bandwidthPeakValue') is not None:
            self.bandwidth_peak_value = m.get('bandwidthPeakValue')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetailsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetails] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.details = details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResultDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDirectoryBandwidthTrafficUnderLivestreamDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRequesBandwidthtSavingRatioRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"From date:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example :2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8);
        # 2.Cannot exceed current time;
        # 3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2018年12月2日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"To time:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example :2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8);
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time;
        # 3.Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception;
        # 4.Maximum allowed query time interval: 31 days, Date from and dateTo, not more than 31 days", "zh_CN":"结束时间:
        # 1.时间格式2019-01-02T10:00:00+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The maximum number of deliverable domain names is 200 by default;
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names);
        # 3.The default query accounts for all domains if the number of domain names exceeds the upper limit when the entry is not delivered. If the number of domain names in the account exceeds the limit, an error is raised.", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为200个
        # 2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 3.未传递该入参时,默认查询账号下所有域名,但当账号下域名数量超过上限时提示错误。"}
        self.domain = domain
        # {"en":"Time interval of data: 5m (5 min), 1h (1 hour), 1d (1 day); 
        # 	The default is 1d.", "zh_CN":"数据粒度:
        # 1.支持5m(5分钟)、1h(1小时)、1d(天)
        # 2.不传默认1d。"}
        self.data_interval = data_interval

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        return self


class QueryRequesBandwidthtSavingRatioResponseDataSavingBandwidthDatas(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        saving_bandwidth: str = None,
    ):
        # {"en":"timetamp
        # 1. When the data granularity of the query is fiveminutes, the format is yyyy-MM-dd HH:MM; Each time slice data value represents the data value in the previous time granularity range, For example yyyy-MM-dd 00:05 represents data in the range from 00:00 to 00:05.
        # 2.The data granularity of query is hourly, the format is yyyy-MM-dd HH. Each time slice data value represents data values in the previous time granularity range such as yyyy-MM-dd 01 that represent data from 00 to 01.
        # 3. the data granularity of the query is daily, the format is yyyy-MM-dd; Each time slice data value represents the data value for that day.
        # 4.Returns the timetamp contained in start time and end time.", "zh_CN":"时间片
        # 1.查询的数据粒度为fiveminutes时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值,比如yyyy-MM-dd 00:05,代表00:00到00:05范围内的数据。
        # 2.查询的数据粒度为hourly时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值,比如yyyy-MM-dd 01,代表00到01之间的数据。
        # 3.查询的数据粒度为daily时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值。
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"saving of bandwidth,keep 4 decimal places", "zh_CN":"节省带宽,保留4位小数"}
        self.saving_bandwidth = saving_bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.saving_bandwidth, 'saving_bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.saving_bandwidth is not None:
            result['savingBandwidth'] = self.saving_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('savingBandwidth') is not None:
            self.saving_bandwidth = m.get('savingBandwidth')
        return self


class QueryRequesBandwidthtSavingRatioResponseData(TeaModel):
    def __init__(
        self,
        real_date: str = None,
        total_avg: int = None,
        saving_bandwidth_datas: List[QueryRequesBandwidthtSavingRatioResponseDataSavingBandwidthDatas] = None,
    ):
        # {"en":"Actually processed time.  yyyy-MM-dd HH:mm format", "zh_CN":"实际查询时间,格式 yyyy-MM-dd HH:mm"}
        self.real_date = real_date
        # {"en":"Average of total saving of bandwidth.", "zh_CN":"总节省带宽的平均值"}
        self.total_avg = total_avg
        self.saving_bandwidth_datas = saving_bandwidth_datas

    def validate(self):
        self.validate_required(self.real_date, 'real_date')
        self.validate_required(self.total_avg, 'total_avg')
        self.validate_required(self.saving_bandwidth_datas, 'saving_bandwidth_datas')
        if self.saving_bandwidth_datas:
            for k in self.saving_bandwidth_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_date is not None:
            result['realDate'] = self.real_date
        if self.total_avg is not None:
            result['totalAvg'] = self.total_avg
        if self.saving_bandwidth_datas is not None:
            result['savingBandwidthDatas'] = []
            for k in self.saving_bandwidth_datas:
                result['savingBandwidthDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('realDate') is not None:
            self.real_date = m.get('realDate')
        if m.get('totalAvg') is not None:
            self.total_avg = m.get('totalAvg')
        if m.get('savingBandwidthDatas') is not None:
            self.saving_bandwidth_datas = []
            for k in m.get('savingBandwidthDatas'):
                temp_model = QueryRequesBandwidthtSavingRatioResponseDataSavingBandwidthDatas()
                self.saving_bandwidth_datas.append(temp_model.from_map(k))
        return self


class QueryRequesBandwidthtSavingRatioResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryRequesBandwidthtSavingRatioResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
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
                temp_model = QueryRequesBandwidthtSavingRatioResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryRequesBandwidthtSavingRatioPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequesBandwidthtSavingRatioParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequesBandwidthtSavingRatioRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequesBandwidthtSavingRatioResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryStreamTrafficUnderMALBDomainRequestDomainStream(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream: List[str] = None,
    ):
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"可传递域名数量上限默认为20个(可联系技术支持调整)"}
        self.domain = domain
        # {"en":"Stream name:
        # 				1. If this field is not specified, it means all domains under the domain are queried;
        # 				2. Number of streams can be adjusted depending on different accounts. The default value is 2000(this limit applies to the empty value);", "zh_CN":"流名：'发布点'+'流名'。例如：live/test-20180101-test ,其中live是发布点，test-20180101-test是流名。"}
        self.stream = stream

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class QueryStreamTrafficUnderMALBDomainRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain_stream: List[QueryStreamTrafficUnderMALBDomainRequestDomainStream] = None,
        data_interval: str = None,
        data_type: str = None,
        filter_empty_stream: int = None,
    ):
        # {"en":"Starting time
        # 			1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 			2. Must be less than the current time and dateTo;
        # 			3. The difference between dateFrom and dateTo cannot exceed 1 day(technical support can be contacted to adjust);
        # 			4. Only data within the last 6 months can be queried.", "zh_CN":"开始时间
        # 			1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 			2.必须小于当前时间和dateTo；
        # 			3.dateFrom和dateTo相差不能超过1天(可联系技术支持调整)；
        # 			4.只能查询最近6个月内数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 			1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 			2. Must be greater than dateFrom;
        # 			3. If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 			1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 			2.必须大于dateFrom；
        # 			3.如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Domain and stream name list", "zh_CN":"域名和流名组：
        # 						1.可传递的域名和流名组数量上限默认为20组(可联系技术支持调整)；
        # 						2.域名domain：一组域名和流名组中只能传递单个域名，且域名必须传递；
        # 						3.流名stream：一组域名和流名组下(即单个域名下)可传递的流名数量上限默认为2000个(可联系技术支持调整)，流名未传递时默认查询域名下所有流名，但当域名下流名数量超过限制时不可查询(报错)。"}
        self.domain_stream = domain_stream
        # {"en":"Data granularity:
        # 				1. 1m: 1-minute granularity, 5m: 5-minute granularity;
        # 				2. Data with granularity of 5 minutes is queried by default, if you need to query the granularity of 1 minute, please contact technical support for configuration", "zh_CN":"数据粒度
        # 				1.1m：1分钟粒度，5m：5分钟粒度；
        # 				2.默认查询5分钟粒度数据，若需要查询1m粒度请联系技术支持进行特殊配置"}
        self.data_interval = data_interval
        # {"en":"Data type: flow, bandwidth", "zh_CN":"数据类型，flow：流量，bandwidth：带宽"}
        self.data_type = data_type
        # {"en":"Filter nullname stream:
        # 			1.Enter optional value '0' or '1';
        # 			2. The parameter 0 does not filter the data whose data is null, and the parameter 1 filter the data whose data is null.
        # 			3. the default value is 0;", "zh_CN":"是否过滤空流名:
        # 			1.入参可选值 '0' 或 '1' ；
        # 			2.传参 0 不过滤流名为空的数据，传参 1 则过滤流名为空的数据 ；
        # 			3.默认值为 0 ；"}
        self.filter_empty_stream = filter_empty_stream

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.domain_stream, 'domain_stream')
        if self.domain_stream:
            for k in self.domain_stream:
                if k:
                    k.validate()
        self.validate_required(self.data_type, 'data_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain_stream is not None:
            result['domainStream'] = []
            for k in self.domain_stream:
                result['domainStream'].append(k.to_map() if k else None)
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter_empty_stream is not None:
            result['filterEmptyStream'] = self.filter_empty_stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domainStream') is not None:
            self.domain_stream = []
            for k in m.get('domainStream'):
                temp_model = QueryStreamTrafficUnderMALBDomainRequestDomainStream()
                self.domain_stream.append(temp_model.from_map(k))
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filterEmptyStream') is not None:
            self.filter_empty_stream = m.get('filterEmptyStream')
        return self


class QueryStreamTrafficUnderMALBDomainResponseResultDetailsDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Date:
        # 						1. When the data query granularity is 1m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00.
        # 						2. When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00.", "zh_CN":"时间
        # 						1.查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是(yyyy-MM-dd+1)&nbsp;00:00。
        # 						2.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是(yyyy-MM-dd+1)&nbsp;00:00。"}
        self.timestamp = timestamp
        # {"en":"Data of the time point:
        # 						1. Two decimal digits allowed;
        # 						2. When the input parameter of dataType is flow, the value is the flow/traffic value, with MB as the unit;
        # 						3. When the input parameter of dataType is bandwidth, the value is the bandwidth value, with Mbps as the unit;", "zh_CN":"时间点的数据
        # 						1.保留2位小数；
        # 						2.当入参dataType为flow时，value值为流量，单位为MB；
        # 						3.当入参dataType为bandwidth时，value值为带宽值，单位为Mbps；"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryStreamTrafficUnderMALBDomainResponseResultDetails(TeaModel):
    def __init__(
        self,
        stream: str = None,
        total_flow: str = None,
        bandwidth_peak_value: str = None,
        details: List[QueryStreamTrafficUnderMALBDomainResponseResultDetailsDetails] = None,
    ):
        # {"en":"Stream name", "zh_CN":"流名"}
        self.stream = stream
        # {"en":"Total traffic:
        # 					1. Keep two digits of decimals. Unit: MB;
        # 					2. Return when the input parameter of datatype is flow.", "zh_CN":"总流量
        # 					1.保留2位小数，单位为MB;
        # 					2.当入参dataType为flow时，返回。"}
        self.total_flow = total_flow
        # {"en":"Peak value of bandwidth
        # 					1. Keep two digits of decimals. Unit: Mbps
        # 					2. Return when the input dataType is bandwidth.", "zh_CN":"峰值带宽
        # 					1.保留2位小数，单位Mbps
        # 					2.当入参dataType为bandwidth时，返回。"}
        self.bandwidth_peak_value = bandwidth_peak_value
        self.details = details

    def validate(self):
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.bandwidth_peak_value is not None:
            result['bandwidthPeakValue'] = self.bandwidth_peak_value
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('bandwidthPeakValue') is not None:
            self.bandwidth_peak_value = m.get('bandwidthPeakValue')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = QueryStreamTrafficUnderMALBDomainResponseResultDetailsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryStreamTrafficUnderMALBDomainResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[QueryStreamTrafficUnderMALBDomainResponseResultDetails] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.details = details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = QueryStreamTrafficUnderMALBDomainResponseResultDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryStreamTrafficUnderMALBDomainResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryStreamTrafficUnderMALBDomainResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryStreamTrafficUnderMALBDomainResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryStreamTrafficUnderMALBDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStreamTrafficUnderMALBDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStreamTrafficUnderMALBDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStreamTrafficUnderMALBDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class FlowDayRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        isp: str = None,
        accetype: str = None,
        dataformat: str = None,
        timezone: str = None,
    ):
        # {"en":"main account cust_en_name, cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"主账号客户英文名，合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期，日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions. Common regions: cn: Mainland China, hk: Hong Kong, ov: Oversea average, tw: Taiwan, euna: Europe and North America, apac: Asia-Pacific, sa: South America, af: Africa, am: Americas, emea: Europe/Middle East/Africa, kr: South Korea, au: Australia, in: India, jp: Japan, ru: Russia, indo: Indonesia, me: Middle East, eu: Europe, ph: Philippines", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。常用区域：cn:中国大陆,hk:香港,ov:海外平均,tw:台湾,euna:欧美,apac:亚太,sa:南美,af:非洲,am:美洲,emea:欧洲/中东/非洲,kr:韩国,au:澳大利亚,in:印度,jp:日本,ru:俄罗斯,indo:印尼,me:中东,eu:欧洲,ph:菲律宾 "}
        self.region = region
        # {"en":"1)If there isp multiple inputs,use ';' as demimeter.
        # 2)optional values of isp: refers to the ISP-section of appendix.
        # 3) If not specified,means all the isp.", "zh_CN":"要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp = isp
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes. Common Acceleration Types: Web Acceleration: web, Web-HTTPS: web-https, Whole Site Acceleration: wsa, Whole Site Acceleration-HTTPS: wsa-https, HTTP Download: download, Livestream Media: livestream, Livestream-HTTPS: live-https, VOD-HTTPS: vod-https, Cloud Video on Demand: cloudv-vod, VOD Streaming: vodstream, Financial Security Acceleration Solution: fsa, Government and Enterprise Security Acceleration Solution: gess, E-commerce Security Acceleration Solution: esa, Mobile Acceleration (MAA): maa, Application Security Acceleration Solution: s-appa, Application Acceleration: appa, WAF: waf, Upload Acceleration: upload, Upload Acceleration-HTTPS: upa-https, IPv6 Integration Solution: osv6, Live P2P: livep2p", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型. 常用加速类型：网页加速:web,网页-HTTPS:web-https ,全站加速:wsa,全站加速-https:wsa-https,HTTP下载:download,流媒体直播:livestream,直播-https:live-https,点播-HTTPS:vod-https,云点播:cloudv-vod,流媒体点播:vodstream,金融安全加速解决方案:fsa,政企安全加速解决方案:gess,电商安全加速解决方案:esa,移动加速(MAA):maa,应用安全加速解决方案:s-appa,应用加速:appa,WAF:waf,上传加速:upload,上传加速-https:upa-https,IPv6一体化解决方案:osv6,直播P2P:livep2p"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Greenwich time zone, the parameter format GMT+09:00 means East Nine District, GMT-09:00 means West Nine District, if not passed, the default is the local time zone (East Eight District)", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.region is not None:
            result['region'] = self.region
        if self.isp is not None:
            result['isp'] = self.isp
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class FlowDayResponseProviderDateChannelChannelPeak(TeaModel):
    def __init__(
        self,
        date: str = None,
        peak_time: str = None,
        peak_value: str = None,
        total_flow: str = None,
    ):
        # {'en':'date', 'zh_CN':'日期'}
        self.date = date
        # {'en':'peakTime', 'zh_CN':'峰值时间'}
        self.peak_time = peak_time
        # {'en':'peakvalue(Mbps)', 'zh_CN':'带宽峰值（单位Mbps）'}
        self.peak_value = peak_value
        # {'en':'the total flow', 'zh_CN':'总流量'}
        self.total_flow = total_flow

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.total_flow, 'total_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        return self


class FlowDayResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        channel_peak: List[FlowDayResponseProviderDateChannelChannelPeak] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'channel-peak', 'zh_CN':'频道峰值数据'}
        self.channel_peak = channel_peak

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.channel_peak, 'channel_peak')
        if self.channel_peak:
            for k in self.channel_peak:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.channel_peak is not None:
            result['channel-peak'] = []
            for k in self.channel_peak:
                result['channel-peak'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('channel-peak') is not None:
            self.channel_peak = []
            for k in m.get('channel-peak'):
                temp_model = FlowDayResponseProviderDateChannelChannelPeak()
                self.channel_peak.append(temp_model.from_map(k))
        return self


class FlowDayResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: FlowDayResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始日期'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束日期'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = FlowDayResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class FlowDayResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: FlowDayResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = FlowDayResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class FlowDayResponse(TeaModel):
    def __init__(
        self,
        provider: FlowDayResponseProvider = None,
    ):
        # {'en':'provider', 'zh_CN':'结果'}
        self.provider = provider

    def validate(self):
        self.validate_required(self.provider, 'provider')
        if self.provider:
            self.provider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['provider'] = self.provider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            temp_model = FlowDayResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class FlowDayPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowDayParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowDayRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowDayResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowP2pShareRatioServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        platform: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start date: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.Cannot exceed current time 
        # 	3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2021-05-19T10:00:00+08:00(为北京时间2021年5月19日10点0分0秒)
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time. 
        # 	3.If both fields of dataFrom and dateTo are left empty, the default query past 1 day; If there is only one unsent, throw an exception 
        # 	4.Maximum allowed query time interval: 1 days, Date from and dateTo, not more than 1 days", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:1天,即dateFrom和dateTo相差不能超过1天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support). 
        # 	2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)", "zh_CN":"域名:
        # 1、可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2、自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"Data granularity: 
        # 	1.Support for 1m(1 minutes), 5m (5 minutes)
        # 	2.Default 5m
        # ", "zh_CN":"数据粒度:
        # 1、支持1m(1分钟)、5m(5分钟)
        # 2、不传默认5m"}
        self.data_interval = data_interval
        # {"en":"1. Selection: flash, android, ios, h5, windows 2.Default all platform types", "zh_CN":"1.可选值:flash、android、ios、h5、windows
        # 2.不传默认全部平台类型"}
        self.platform = platform
        # {"en":"1.Selection:domain 2.If groupBy left empty, merge date of all domains", "zh_CN":"可选值:domain
        # 不传默认聚合所有频道数据"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.platform is not None:
            result['platform'] = self.platform
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowP2pShareRatioServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"timestamp,Returns the timestamp between the start time and end time. Time format:  yyyy-MM-dd HH:mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。
        # 时间格式:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"share rate, unit %", "zh_CN":"分享率,单位%"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportFlowP2pShareRatioServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportFlowP2pShareRatioServiceResponseDataDetailList] = None,
    ):
        # {"en":"Domain. If merge date of all domains will not return domain", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
        self.domain = domain
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowP2pShareRatioServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowP2pShareRatioServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowP2pShareRatioServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"request result information", "zh_CN":"请求结果信息"}
        self.message = message
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
                temp_model = ReportFlowP2pShareRatioServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowP2pShareRatioServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowP2pShareRatioServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowP2pShareRatioServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowP2pShareRatioServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDataTransferForAllDomainByteRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
    ):
        # {"en":"Start time:
        # 1. Time format is yyyy-MM-ddTHH:mm:ss+08:00,
        # 2. No bigger than the current time.
        # 3. Data in the last 2 years at most can be queried.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        # 2.不能大于当前时间
        # 3.最多可获取最近2年内的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 1day will be queried by default; if only one field is filled in and one is left empty, then exception will be occur.
        # 4. Allowable maximum time range for query: 31days, means the period between dateFrom to dateTo should not exceed 31days (can be adjusted by contacting technical support).", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间,
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 4.允许查询最大时间间隔31天:,即dateFrom和dateTo相差不能超过31天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Data granularity, 5m: 5-minute   granularity, 1h: 1-hour granularity, 1d: 1-day granularity ", "zh_CN":"数据粒度, 5m:5分钟粒度,1h:1小时粒度, 1d: 1天粒度"}
        self.data_interval = data_interval

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
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        return self


class QueryDataTransferForAllDomainByteResponseDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
    ):
        # {"en":"timestamp", "zh_CN":"时间"}
        self.timestamp = timestamp
        # {"en":"flow", "zh_CN":"流量"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class QueryDataTransferForAllDomainByteResponseData(TeaModel):
    def __init__(
        self,
        flow_summary: str = None,
        flow_data: List[QueryDataTransferForAllDomainByteResponseDataFlowData] = None,
    ):
        # {"en":"flowSummary", "zh_CN":"总流量"}
        self.flow_summary = flow_summary
        self.flow_data = flow_data

    def validate(self):
        self.validate_required(self.flow_summary, 'flow_summary')
        self.validate_required(self.flow_data, 'flow_data')
        if self.flow_data:
            for k in self.flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_summary is not None:
            result['flowSummary'] = self.flow_summary
        if self.flow_data is not None:
            result['flowData'] = []
            for k in self.flow_data:
                result['flowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flowSummary') is not None:
            self.flow_summary = m.get('flowSummary')
        if m.get('flowData') is not None:
            self.flow_data = []
            for k in m.get('flowData'):
                temp_model = QueryDataTransferForAllDomainByteResponseDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class QueryDataTransferForAllDomainByteResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryDataTransferForAllDomainByteResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
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
                temp_model = QueryDataTransferForAllDomainByteResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryDataTransferForAllDomainBytePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDataTransferForAllDomainByteParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDataTransferForAllDomainByteRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDataTransferForAllDomainByteResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTrafficBySpecificProtocolRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        protocol_type: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity:
        # Support for 1m(1 minutes), 5m (5 minutes), 1h (1 hour), 1d (1 day)", "zh_CN":"数据粒度:
        # 支持1m(1分钟),5m(5分钟),1h(1小时),1d(1天)"}
        self.data_interval = data_interval
        # {"en":"Transmission protocol:
        # 1.Options: http, https;
        # 2.https is used as the default value is no value specified;
        # 3.httpFlowData is displayed if http is queried, and httpsFlowData is displayed if https is queried;", "zh_CN":"传输协议
        # 1.可选值为http、https;
        # 2.不传默认查询https;
        # 3.查询http时出参展示httpFlowData,查询https时出参展示httpsFlowData;"}
        self.protocol_type = protocol_type
        # {"en":"Group dimension:
        # 1.The value can be selected is domain;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.protocol_type is not None:
            result['protocolType'] = self.protocol_type
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('protocolType') is not None:
            self.protocol_type = m.get('protocolType')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryTrafficBySpecificProtocolResponseResultHttpsFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime: the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00.", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00。"}
        self.timestamp = timestamp
        # {"en":"Traffic unit is MB and 2 digits  of decimals allowed", "zh_CN":"流量值,单位MB,保留2位小数"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryTrafficBySpecificProtocolResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        https_flow_data: List[QueryTrafficBySpecificProtocolResponseResultHttpsFlowData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.https_flow_data = https_flow_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.https_flow_data, 'https_flow_data')
        if self.https_flow_data:
            for k in self.https_flow_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.https_flow_data is not None:
            result['httpsFlowData'] = []
            for k in self.https_flow_data:
                result['httpsFlowData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('httpsFlowData') is not None:
            self.https_flow_data = []
            for k in m.get('httpsFlowData'):
                temp_model = QueryTrafficBySpecificProtocolResponseResultHttpsFlowData()
                self.https_flow_data.append(temp_model.from_map(k))
        return self


class QueryTrafficBySpecificProtocolResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryTrafficBySpecificProtocolResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryTrafficBySpecificProtocolResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryTrafficBySpecificProtocolPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficBySpecificProtocolParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficBySpecificProtocolRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTrafficBySpecificProtocolResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainRequestDomainStream(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream: List[str] = None,
    ):
        # {"en":"Domain:
        # 1. The maximum number of deliverable domain names is 200 by default
        # 2. Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为200个
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)"}
        self.domain = domain
        # {"en":"Celebrity: Publishing Point  Stream Name. Example: live/test-20180101-test where live is a publishing point and test-20180101-test is a stream name
        # No, the default queries all stream data in the specified domain name", "zh_CN":"
        # 流名:'发布点'+'流名'。例如:live/test-20180101-test,其中live是发布点,test-20180101-test是流名;
        # 不传，默认查询指定域名下的所有流的数据"}
        self.stream = stream

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain_stream: List[QueryMultipleStreamTrafficAndBandwidthUnderTheDomainRequestDomainStream] = None,
        data_interval: str = None,
        data_type: str = None,
        filter_empty_stream: int = None,
        keyword: str = None,
        is_return_online: str = None,
    ):
        # {"en":"From date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example :2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8)
        # 2. Cannot exceed current time
        # 3. The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过 10 分钟 ；
        # 4.只能查询最近半年内数据。
        # 5.dateFrom 和 dateTo 都不填则默认查询过去 10 分钟的数据"}
        self.date_from = date_from
        # {"en":"To time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example :2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8)
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3. Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception", "zh_CN":"
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；
        # 3.如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Domain and stream group:
        # 1. the maximum number of transmissible domain names and stream name groups is 20 by default 
        # 3. stream name stream : the maximum number of stream names that can be passed under a group of domain names and stream name groups ( that is, under a single domain name ) defaults to 2000 ( which can be adjusted with technical support ).", "zh_CN":"域名和流名组:
        # 
        # 1.可传递的域名和流名组数量上限默认为20组(可联系技术支持调整)；
        # 2.域名domain:一组域名和流名组中只能传递单个域名，且域名必须传递；
        # 3.流名stream:一组域名和流名组下(即单个域名下)可传递的流名数量上限默认为2000个(可联系技术支持调整)，流名未传递时默认查询域名下所有流名，但当域名下流名数量超过限制时不可查询(报错)。"}
        self.domain_stream = domain_stream
        # {"en":"data granularity
        # 1m: 1 min granularity, 5m: 5 min granularity
        # Default 5-minute granularity data query", "zh_CN":"数据粒度
        # 1.1m: 1分钟粒度，5m: 5分钟粒度
        # 2.默认查询5分钟粒度数据"}
        self.data_interval = data_interval
        # {"en":"Data type, flow: traffic, bandwidth: bandwidth", "zh_CN":"数据类型，flow:流量，bandwidth:带宽"}
        self.data_type = data_type
        # {"en":"Filter empty stream name:
        # 1. The input optional value '0' or '1';
        # 2. The data whose parameter 0 does not filter flow is null, and the data whose parameter 1 filter stream is null.
        # 3. The default value is 0;", "zh_CN":"是否过滤空流名
        # 1.入参可选值 '0' 或 '1' ；
        # 2.传参 0 不过滤流名为空的数据，传参 1 则过滤流名为空的数据 ；
        # 3.默认值为 0；"}
        self.filter_empty_stream = filter_empty_stream
        # {"en":"Query string, multiple queries are not supported, and fuzzy matching is used by default, allowing regular expression queries", "zh_CN":"查询字符串，不支持多次查询，默认使用模糊匹配，允许正则表达式查询"}
        self.keyword = keyword
        # {"en":"Whether to return the number of online users:
        #     1.If true is passed, the number of online users will only be returned when dataInterval=1m. Does not return when dataInterval=5min;
        #     2.If no or false is passed,the default is not to return the number of online users.", "zh_CN":"是否返回在线人数: 
        #     1.传true, 仅当dataInterval=1m时,返回在线人数,5min时不返回;
        #     2.不传或传false，则默认不返回在线人数."}
        self.is_return_online = is_return_online

    def validate(self):
        self.validate_required(self.domain_stream, 'domain_stream')
        if self.domain_stream:
            for k in self.domain_stream:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain_stream is not None:
            result['domainStream'] = []
            for k in self.domain_stream:
                result['domainStream'].append(k.to_map() if k else None)
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.filter_empty_stream is not None:
            result['filterEmptyStream'] = self.filter_empty_stream
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.is_return_online is not None:
            result['isReturnOnline'] = self.is_return_online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domainStream') is not None:
            self.domain_stream = []
            for k in m.get('domainStream'):
                temp_model = QueryMultipleStreamTrafficAndBandwidthUnderTheDomainRequestDomainStream()
                self.domain_stream.append(temp_model.from_map(k))
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('filterEmptyStream') is not None:
            self.filter_empty_stream = m.get('filterEmptyStream')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('isReturnOnline') is not None:
            self.is_return_online = m.get('isReturnOnline')
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        online_user: int = None,
    ):
        # {"en":"time
        # 1. Each time slice data value represents the data value in the previous time granularity range. 
        # 2. The data granularity of the query is 5m, the format is yyyy-MM-dd HH:MM; Each time slice data value represents the data value in the previous time granularity range.", "zh_CN":"时间
        # 1.查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是(yyyy-MM-dd+1) 00:00。
        # 2.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是(yyyy-MM-dd+1) 00:00。"}
        self.timestamp = timestamp
        # {"en":"Data at the point in time:
        # 1. keep 2 decimal places;
        # 2. When the dataType is flow, value is flow in MB;
        # 3. value is bandwidth value in Mbps when dataType is bandwidth.", "zh_CN":"时间点的数据
        # 1.保留2位小数；
        # 2.当入参dataType为flow时，value值为流量，单位为MB；
        # 3.当入参dataType为bandwidth时，value值为带宽值，单位为Mbps；"}
        self.value = value
        # {"en":"Number of online users at a time point.", "zh_CN":"时间点的在线人数"}
        self.online_user = online_user

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.online_user, 'online_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.online_user is not None:
            result['onlineUser'] = self.online_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('onlineUser') is not None:
            self.online_user = m.get('onlineUser')
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamList(TeaModel):
    def __init__(
        self,
        stream: str = None,
        total_flow: str = None,
        bandwidth_peak_value: str = None,
        detail_list: List[QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamListDetailList] = None,
    ):
        # {"en":"stream name", "zh_CN":"流名"}
        self.stream = stream
        # {"en":"aggregate flow
        # 1. Keep 2 decimal places, in MB;
        # 2. When entering dataType is flow.
        # 3. Only data with traffic greater than0;is returned.", "zh_CN":"总流量
        # 1.保留2位小数，单位为MB;
        # 2.当入参dataType为flow时，返回。
        # 3.仅返回流量大于 0  的数据。"}
        self.total_flow = total_flow
        # {"en":"peak bandwidth
        # 1. keep 2 decimal places in Mbps
        # 2. when entering dataType is bandwidth, return.
        # 3. only returns data with bandwidth greater than 0.", "zh_CN":"峰值带宽
        # 1.保留2位小数，单位Mbps
        # 2.当入参dataType为bandwidth时，返回。
        # 3.仅返回带宽大于 0 的数据。"}
        self.bandwidth_peak_value = bandwidth_peak_value
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.bandwidth_peak_value, 'bandwidth_peak_value')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.bandwidth_peak_value is not None:
            result['bandwidthPeakValue'] = self.bandwidth_peak_value
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('bandwidthPeakValue') is not None:
            self.bandwidth_peak_value = m.get('bandwidthPeakValue')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_of_stream_list: List[QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamList] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        self.domain_of_stream_list = domain_of_stream_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.domain_of_stream_list, 'domain_of_stream_list')
        if self.domain_of_stream_list:
            for k in self.domain_of_stream_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.domain_of_stream_list is not None:
            result['domainOfStreamList'] = []
            for k in self.domain_of_stream_list:
                result['domainOfStreamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainOfStreamList') is not None:
            self.domain_of_stream_list = []
            for k in m.get('domainOfStreamList'):
                temp_model = QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseDataDomainOfStreamList()
                self.domain_of_stream_list.append(temp_model.from_map(k))
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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
                temp_model = QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryMultipleStreamTrafficAndBandwidthUnderTheDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryISPProvinceHitRateRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        query_by: str = None,
        group_by: str = None,
    ):
        # {"en":"Start date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. Cannot exceed current time
        # 3. The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年01月01日10点0分0秒）;
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3. Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        # 4. Maximum allowed query time interval: 24 hours (with technical support adjustments), meaning that the difference between Date from and dateTo cannot exceed 24 hours.", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如 2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时;如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔:24小时（可联系技术支持调整），即dateFrom和dateTo相差不能超过24小时。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The maximum number of TLDs that can be delivered is 20 by default (contact technical support adjustment);
        # 2. Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3. Domain name exceeding limit, misstatement", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）;
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        # 3.域名超过上限，提示错误"}
        self.domain = domain
        # {"en":"Data granularity: 
        # 1. default 1m
        # 2. 1m (1 minute), 5m (5 minutes)", "zh_CN":"数据粒度:
        # 1.不传默认1m
        # 2.支持1m（1分钟）、5m（5分钟）"}
        self.data_interval = data_interval
        # {"en":"Province
        # 
        # 1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"query dimensionality:
        # 1. Optional value flow, request
        # 2. Default flow
        # 3. Flow: Flow, keep two decimal places;
        # 4. Request: number of Request", "zh_CN":"查询维度:
        # 1.可选值 flow、request
        # 2.传默认 flow
        # 3.flow:流量，保留两位小数;
        # 4.request:请求数"}
        self.query_by = query_by
        # {"en":"Optional: domain, all, If it is empty, it defaults to returning by domain dimension;
        # If all is passed, merge and return according to the query domain name.", "zh_CN":"可选项：domain、all, 为空则默认为按domain维度返回;
        # 若传递all，则按查询域名合并返回"}
        self.group_by = group_by

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.query_by is not None:
            result['queryBy'] = self.query_by
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryISPProvinceHitRateResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        hit_value: str = None,
        hit_rate: str = None,
    ):
        # {"en":"time, in yyyy-MM-dd HH:MM", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Hit data:
        # Flow: Flow, keep two decimal places;
        # Request: number of Request", "zh_CN":"命中数据:
        # 1.flow:流量，保留两位小数;
        # 2.request:请求数"}
        self.hit_value = hit_value
        # {"en":"Hit rate, keep four decimal places", "zh_CN":"命中率，保留四位小数"}
        self.hit_rate = hit_rate

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.hit_value, 'hit_value')
        self.validate_required(self.hit_rate, 'hit_rate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.hit_value is not None:
            result['hitValue'] = self.hit_value
        if self.hit_rate is not None:
            result['hitRate'] = self.hit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('hitValue') is not None:
            self.hit_value = m.get('hitValue')
        if m.get('hitRate') is not None:
            self.hit_rate = m.get('hitRate')
        return self


class QueryISPProvinceHitRateResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[QueryISPProvinceHitRateResponseDataDetailList] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = QueryISPProvinceHitRateResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class QueryISPProvinceHitRateResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryISPProvinceHitRateResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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
                temp_model = QueryISPProvinceHitRateResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryISPProvinceHitRatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceHitRateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceHitRateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceHitRateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




