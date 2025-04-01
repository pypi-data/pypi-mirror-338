# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class PerzoneBillingRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        start_date: str = None,
        end_date: str = None,
        timezone: str = None,
        channel: str = None,
        accetype: str = None,
        dwa: str = None,
        type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they specify the query date scope. 2.With format yyyy-mm-dd. 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期，日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.start_date = start_date
        # {"en":"1.Must work with 'startdate' and they specify the query date scope. 2.With format yyyy-mm-dd 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.end_date = end_date
        # {"en":"In Greenwich time zone, the value GMT+09:00 means East Nine, GMT-09:00 means West Nine, and the default is East Eight.", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号“;”，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号“;”分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"Whether it is a DWA product, 1: yes; 0: no, if not fill in, the default is 0", "zh_CN":"是否DWA产品，1:是;0:否,不填默认0"}
        self.dwa = dwa
        # {"en":"Data type (1: bandwidth|2: traffic) default 1", "zh_CN":"数据类型（1:带宽|2:流量）默认1"}
        self.type = type

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
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.channel is not None:
            result['channel'] = self.channel
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dwa is not None:
            result['dwa'] = self.dwa
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dwa') is not None:
            self.dwa = m.get('dwa')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PerzoneBillingResponseProviderDateAreaMapPerzoneDetail(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
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


class PerzoneBillingResponseProviderDateAreaMapPerzone(TeaModel):
    def __init__(
        self,
        name: str = None,
        peak_value: str = None,
        peak_time: str = None,
        total_flow: str = None,
        detail: List[PerzoneBillingResponseProviderDateAreaMapPerzoneDetail] = None,
    ):
        # {'en':'name', 'zh_CN':'perzone区域'}
        self.name = name
        # {'en':'peakValue', 'zh_CN':'峰值'}
        self.peak_value = peak_value
        # {'en':'peakTime', 'zh_CN':'峰值时间点'}
        self.peak_time = peak_time
        # {'en':'totalFlow', 'zh_CN':'总流量'}
        self.total_flow = total_flow
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.detail = detail

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.detail is not None:
            result['detail'] = []
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('detail') is not None:
            self.detail = []
            for k in m.get('detail'):
                temp_model = PerzoneBillingResponseProviderDateAreaMapPerzoneDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class PerzoneBillingResponseProviderDateAreaMap(TeaModel):
    def __init__(
        self,
        perzone: PerzoneBillingResponseProviderDateAreaMapPerzone = None,
    ):
        # {'en':'perzone', 'zh_CN':'perzone数据'}
        self.perzone = perzone

    def validate(self):
        self.validate_required(self.perzone, 'perzone')
        if self.perzone:
            self.perzone.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perzone is not None:
            result['perzone'] = self.perzone.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('perzone') is not None:
            temp_model = PerzoneBillingResponseProviderDateAreaMapPerzone()
            self.perzone = temp_model.from_map(m['perzone'])
        return self


class PerzoneBillingResponseProviderDate(TeaModel):
    def __init__(
        self,
        start_date: str = None,
        end_date: str = None,
        type: str = None,
        area_map: PerzoneBillingResponseProviderDateAreaMap = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.start_date = start_date
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.end_date = end_date
        # {'en':'type', 'zh_CN':'数据类型1:带宽|2:流量'}
        self.type = type
        # {'en':'channel', 'zh_CN':'频道'}
        self.area_map = area_map

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.type, 'type')
        self.validate_required(self.area_map, 'area_map')
        if self.area_map:
            self.area_map.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.type is not None:
            result['type'] = self.type
        if self.area_map is not None:
            result['areaMap'] = self.area_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('areaMap') is not None:
            temp_model = PerzoneBillingResponseProviderDateAreaMap()
            self.area_map = temp_model.from_map(m['areaMap'])
        return self


class PerzoneBillingResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: PerzoneBillingResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'perzone带宽数据'}
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
            temp_model = PerzoneBillingResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class PerzoneBillingResponse(TeaModel):
    def __init__(
        self,
        provider: PerzoneBillingResponseProvider = None,
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
            temp_model = PerzoneBillingResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class PerzoneBillingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PerzoneBillingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PerzoneBillingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PerzoneBillingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDirBandwidthInfoServiceRequestDomainDir(TeaModel):
    def __init__(
        self,
        domain: str = None,
        dir: List[str] = None,
    ):
        # {'en':'Domains.', 'zh_CN':'域名：
        # 
        # 1.域名个数限制根据账号可调,默认为1个'}
        self.domain = domain
        # {'en':'Table of contents
        # 
        # 1.Directory number limits can be adjusted depending on different accounts. The default value is 200;
        # 
        # 2.Empty value means to query all directories. Number of directories shall not exceed set limit;
        # 
        # 3.Invalid directories are not returned', 'zh_CN':'目录
        # 
        # 1.目录个数限制根据账号可调,默认为200个。更多找技术支持调整;
        # 
        # 2.不传代表查询该域名下的所有目录,同时接受目录个数限制;
        # 
        # 3.无效的目录不返回'}
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


class ReportDirBandwidthInfoServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        area_code: List[str] = None,
        dir_hierarchy: str = None,
        domain_dir: List[ReportDirBandwidthInfoServiceRequestDomainDir] = None,
    ):
        # {'en':'Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (10:00:00 Beijing time on December 2, 2016);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.', 'zh_CN':'开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days. ', 'zh_CN':'结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：31天，即dateFrom和dateTo相差不能超过31天。'}
        self.date_to = date_to
        # {'en':'Acceleration area:
        # 
        # 1.Acceleration areaCode is not uploaded: Query all acceleration areas by default.
        # 
        # 2.Acceleration areaCode is uploaded: Multiple can be uploaded, such as cn, af.  Please refer to the appendix description section of the overview page.', 'zh_CN':'加速区域：
        # 
        # 1.未传递areaCode时，默认查询所有加速区域；
        # 
        # 2.有传递areaCode时：可传多个，如cn, af。可传递的值详见概览页附录说明章节'}
        self.area_code = area_code
        # {'en':'Directory levels, value range 1-4. Only one vlaue can be submitted', 'zh_CN':'目录层级,取值范围1~4,只能提交单个值'}
        self.dir_hierarchy = dir_hierarchy
        self.domain_dir = domain_dir

    def validate(self):
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
        if self.area_code is not None:
            result['areaCode'] = self.area_code
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
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('dirHierarchy') is not None:
            self.dir_hierarchy = m.get('dirHierarchy')
        if m.get('domainDir') is not None:
            self.domain_dir = []
            for k in m.get('domainDir'):
                temp_model = ReportDirBandwidthInfoServiceRequestDomainDir()
                self.domain_dir.append(temp_model.from_map(k))
        return self


class ReportDirBandwidthInfoServiceResponseResultDetailsDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        bandwidth: str = None,
        flow: str = None,
    ):
        # {'en':'Time:
        # 
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        # 2. Return the time slices that contained in start time and in end time.', 'zh_CN':'时间，
        # 查询的数据粒度为5m，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Bandwidth value. Unit is Mbps and 2 digits of decimals are allowed.', 'zh_CN':'带宽，单位Mbps。保留2位小数'}
        self.bandwidth = bandwidth
        # {'en':'Flow value. Unit is MB and 2 digits of decimals are allowed.', 'zh_CN':'流量，单位MB。保留2位小数'}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class ReportDirBandwidthInfoServiceResponseResultDetails(TeaModel):
    def __init__(
        self,
        dir: str = None,
        dir_total_flow: str = None,
        details: List[ReportDirBandwidthInfoServiceResponseResultDetailsDetails] = None,
    ):
        # {'en':'The directory.l', 'zh_CN':'具体目录'}
        self.dir = dir
        # {'en':'Total flow under the directory.', 'zh_CN':'目录下的总流量'}
        self.dir_total_flow = dir_total_flow
        # {'en':'Time segment details under specific directory.', 'zh_CN':'具体目录下的时间片段明细'}
        self.details = details

    def validate(self):
        self.validate_required(self.dir, 'dir')
        self.validate_required(self.dir_total_flow, 'dir_total_flow')
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
        if self.dir_total_flow is not None:
            result['dirTotalFlow'] = self.dir_total_flow
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('dirTotalFlow') is not None:
            self.dir_total_flow = m.get('dirTotalFlow')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportDirBandwidthInfoServiceResponseResultDetailsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportDirBandwidthInfoServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_total_flow: str = None,
        details: List[ReportDirBandwidthInfoServiceResponseResultDetails] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'The total flow under the domain name, in MB, with 2 decimal places retained.', 'zh_CN':'域名下的总流量,单位MB,保留2位小数'}
        self.domain_total_flow = domain_total_flow
        # {'en':'Directory details under the domain.', 'zh_CN':'域名下的目录详情'}
        self.details = details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.domain_total_flow, 'domain_total_flow')
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
        if self.domain_total_flow is not None:
            result['domainTotalFlow'] = self.domain_total_flow
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainTotalFlow') is not None:
            self.domain_total_flow = m.get('domainTotalFlow')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportDirBandwidthInfoServiceResponseResultDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportDirBandwidthInfoServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportDirBandwidthInfoServiceResponseResult] = None,
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
                temp_model = ReportDirBandwidthInfoServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportDirBandwidthInfoServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDirBandwidthInfoServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDirBandwidthInfoServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDirBandwidthInfoServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthChannelProtocolRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
        datatype: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
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
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
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
        # {"en":"Display statistic result in merged or separate way:
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"data type:
        # 1.If specified 1,get the bandwidth data of both http and https protocals.
        # 2.If specified 2,get the bandwidth data of http protocal.
        # 3.If specified 3,get the bandwidth data of https protocal.", "zh_CN":"查询的数据类型。填写1时：输出http+https的带宽数据；填写2时：输出http的带宽数据；填写3时：输出https的带宽数据。多个值请用英文分号';'.不选或者为空时默认为'1'。"}
        self.datatype = datatype

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
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.datatype is not None:
            result['datatype'] = self.datatype
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
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        return self


class BandwidthChannelProtocolResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        total: str = None,
        http: str = None,
        https: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'total bandwidth of http and https,unit Mbps.This value only displays When parameter 'datatype' is not specified or includes '1'.', 'zh_CN':'带宽'}
        self.total = total
        # {'en':'http bandwidth,unit Mbps.This value only displays when parameter 'datatype' includes '2'.', 'zh_CN':'http类型的带宽，单位：Mbps(当入参datatype包含2时有值)'}
        self.http = http
        # {'en':'http2 bandwidth,unit Mbps.This value only displays when parameter 'datatype' includes '3'.', 'zh_CN':'https类型的带宽，单位：Mbps(当入参datatype包含3时有值)'}
        self.https = https

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.total, 'total')
        self.validate_required(self.http, 'http')
        self.validate_required(self.https, 'https')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.total is not None:
            result['total'] = self.total
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class BandwidthChannelProtocolResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[BandwidthChannelProtocolResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'频道带宽区分协议带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthChannelProtocolResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthChannelProtocolResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthChannelProtocolResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = BandwidthChannelProtocolResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class BandwidthChannelProtocolResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: BandwidthChannelProtocolResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'频道带宽区分协议带宽数据'}
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
            temp_model = BandwidthChannelProtocolResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthChannelProtocolResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthChannelProtocolResponseProvider = None,
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
            temp_model = BandwidthChannelProtocolResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthChannelProtocolPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelProtocolParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelProtocolRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelProtocolResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportP2pBandwidthDomainServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH:mm:SS+08:00, for example, 2021-05-19T10:00:00+08:00 (10:00:00 Beijing time on May 19, 2021);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2021-05-19T10:00:00+08:00(为北京时间2021年5月19日10点0分0秒)
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 1 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days. ", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support).", "zh_CN":"1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.如未填,则默认查询此账号下所有S-P2P的加速域名"}
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


class ReportP2pBandwidthDomainServiceResponseDataDomainListBandwidthList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        cdn_value: str = None,
        p_2p_value: str = None,
        p_2p_ipv_6value: str = None,
    ):
        # {"en":"Timestamp, returns the time slice containing the start time and end time. Time format: yyyy-MM-dd HH:mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。时间格式:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"The bandwidth value of the CDN requested by the SDK, in Mbps, with 2 decimal places", "zh_CN":"SDK请求CDN的带宽值,单位Mbps,保留2位小数。"}
        self.cdn_value = cdn_value
        # {"en":"P2P bandwidth value, unit Mbps, keep 2 decimal places", "zh_CN":"P2P带宽值,单位Mbps,保留2位小数。"}
        self.p_2p_value = p_2p_value
        # {"en":"IPv6 bandwidth in P2P bandwidth, unit Mbps, keep 2 decimal places", "zh_CN":"P2P带宽中的IPv6带宽,单位Mbps,保留2位小数。"}
        self.p_2p_ipv_6value = p_2p_ipv_6value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.cdn_value, 'cdn_value')
        self.validate_required(self.p_2p_value, 'p_2p_value')
        self.validate_required(self.p_2p_ipv_6value, 'p_2p_ipv_6value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.cdn_value is not None:
            result['cdnValue'] = self.cdn_value
        if self.p_2p_value is not None:
            result['p2pValue'] = self.p_2p_value
        if self.p_2p_ipv_6value is not None:
            result['p2pIpv6Value'] = self.p_2p_ipv_6value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('cdnValue') is not None:
            self.cdn_value = m.get('cdnValue')
        if m.get('p2pValue') is not None:
            self.p_2p_value = m.get('p2pValue')
        if m.get('p2pIpv6Value') is not None:
            self.p_2p_ipv_6value = m.get('p2pIpv6Value')
        return self


class ReportP2pBandwidthDomainServiceResponseDataDomainList(TeaModel):
    def __init__(
        self,
        v_domain: str = None,
        bandwidth_list: List[ReportP2pBandwidthDomainServiceResponseDataDomainListBandwidthList] = None,
    ):
        # {"en":"1. If the accelerated domain name is a generic domain name, this field is the detailed domain name of the generic domain name (a generic domain name may have many detailed domain names, and detailed data of each detailed domain name will be returned).
        # 						  2. If the accelerated domain name queried is not a generic domain name but a precise domain name, then this field displays the same domain name as the accelerated domain name.", "zh_CN":"1.如果加速域名是泛域名,则此字段为泛域名的明细域名(一个泛域名可能会有很多个明细域名,则会返回每个明细域名的详细数据)。
        # 						  2.如果查询的加速域名非泛域名,而是精确域名,则此字段展示同加速域名。"}
        self.v_domain = v_domain
        self.bandwidth_list = bandwidth_list

    def validate(self):
        self.validate_required(self.v_domain, 'v_domain')
        self.validate_required(self.bandwidth_list, 'bandwidth_list')
        if self.bandwidth_list:
            for k in self.bandwidth_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_domain is not None:
            result['vDomain'] = self.v_domain
        if self.bandwidth_list is not None:
            result['bandwidthList'] = []
            for k in self.bandwidth_list:
                result['bandwidthList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vDomain') is not None:
            self.v_domain = m.get('vDomain')
        if m.get('bandwidthList') is not None:
            self.bandwidth_list = []
            for k in m.get('bandwidthList'):
                temp_model = ReportP2pBandwidthDomainServiceResponseDataDomainListBandwidthList()
                self.bandwidth_list.append(temp_model.from_map(k))
        return self


class ReportP2pBandwidthDomainServiceResponseData(TeaModel):
    def __init__(
        self,
        domain_list: List[ReportP2pBandwidthDomainServiceResponseDataDomainList] = None,
    ):
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = []
            for k in self.domain_list:
                result['domainList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = []
            for k in m.get('domainList'):
                temp_model = ReportP2pBandwidthDomainServiceResponseDataDomainList()
                self.domain_list.append(temp_model.from_map(k))
        return self


class ReportP2pBandwidthDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportP2pBandwidthDomainServiceResponseData] = None,
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
                temp_model = ReportP2pBandwidthDomainServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportP2pBandwidthDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2pBandwidthDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2pBandwidthDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2pBandwidthDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBandwidthofOriginminutelyRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        region: str = None,
        group_by: str = None,
    ):
        # {"en":"Start Time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing time on January 1, 2019 at 10:00 am to 0 seconds);
        # 2. No more than the current time;
        # 3. Up to 6 months (183 days) of data are available.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年1月1日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. Time Format 2019-01-02T10:00:00+08:00;
        # 2. the end time should be greater than the start time. if the end time is greater than the current time, take the current time;
        # 3. dateFrom, dateTo, both are not sent, default query past 24 hours; If only one is not sent, throw exception;
        # 4. Allow maximum query interval: 7 days, i.e., 7 days between Dategroup and dateTo. Do not exceed 7 days.", "zh_CN":"结束时间：
        # 1.时间格式2019-01-02T10:00:00+08:00；
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间；
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 4.允许查询最大时间间隔：7天，即dateFrom和dateTo相差不能超过7天，不支持调整"}
        self.date_to = date_to
        # {"en":"Data granularity:
        # 1. Support for 1m (1 minute), 5m (5 minutes), 1h (1 hour);
        # 2. do not pass default 5m.
        # Data granularity, default to 5m", "zh_CN":"数据粒度：
        # 1.支持1m（1分钟）、5m（5分钟）、1h（1小时）；
        # 2.不传默认5m。
        # 
        # 数据粒度，默认为5m"}
        self.data_interval = data_interval
        # {"en":"Domain name:
        # 1. the maximum number of transitive domain names is 50 by default;
        # 2. Automatically filter out illegal domain names (e.g. passing illegal domain names will be filtered out, and the search results will only return the legal domain name data)
        # 3. If left blank, all domain names will be obtained. If the total number of domain names exceeds the upper limit, an error will be reported.", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为50（可联系技术支持调整）；
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。
        # 3. 若未填写默认查询全部域名，全部域名超出域名上限报错"}
        self.domain = domain
        # {"en":"Acceleration zone:
        # 1. do not pass the default query to all areas;
        # 2. currently only the leaflet area is supported externally;
        # 3. optional values: cn, apac, am, emea.", "zh_CN":"加速区域：
        # 1.不传默认查询全部区域；
        # 2.目前对外只支持传单区域；
        # 3.可选值：cn、apac、am、emea。"}
        self.region = region
        # {"en":"grouped dimension:
        # 1. the optional value is domain;
        # 2. If incoming data is shown in accordance with the dimension.", "zh_CN":"分组维度：
        # 1.可选值为domain；
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
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.domain is not None:
            result['domain'] = self.domain
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryBandwidthofOriginminutelyResponseDataOriginBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"The granularity of data is 1 minute, and the format is yyyy-MM-dd HH:MM.", "zh_CN":"数据粒度为1分钟，格式为yyyy-MM-dd HH:mm。"}
        self.timestamp = timestamp
        # {"en":"Return the source bandwidth value, in Mbps, 2 decimal places reserved.", "zh_CN":"回源带宽值，单位Mbps，保留2位小数。"}
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


class QueryBandwidthofOriginminutelyResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_value: str = None,
        peak_time: str = None,
        total: str = None,
        origin_bandwidth_data: List[QueryBandwidthofOriginminutelyResponseDataOriginBandwidthData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名信息"}
        self.domain = domain
        # {"en":"Peak bandwidth Mbps, example (931556.21 Mbps)", "zh_CN":"峰值带宽 Mbps，示例 （931556.21 Mbps）"}
        self.peak_value = peak_value
        # {"en":"Peak Time, Example (2019-02-13 18:01)", "zh_CN":"峰值时间，示例(2019-02-13 18:01)"}
        self.peak_time = peak_time
        # {"en":"Total return flow, example ( 74099.92 MB )", "zh_CN":"回源总流量，示例 ( 74099.92 MB )"}
        self.total = total
        self.origin_bandwidth_data = origin_bandwidth_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.total, 'total')
        self.validate_required(self.origin_bandwidth_data, 'origin_bandwidth_data')
        if self.origin_bandwidth_data:
            for k in self.origin_bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.total is not None:
            result['total'] = self.total
        if self.origin_bandwidth_data is not None:
            result['originBandwidthData'] = []
            for k in self.origin_bandwidth_data:
                result['originBandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('originBandwidthData') is not None:
            self.origin_bandwidth_data = []
            for k in m.get('originBandwidthData'):
                temp_model = QueryBandwidthofOriginminutelyResponseDataOriginBandwidthData()
                self.origin_bandwidth_data.append(temp_model.from_map(k))
        return self


class QueryBandwidthofOriginminutelyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryBandwidthofOriginminutelyResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on request results", "zh_CN":"请求结果的详细数据"}
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
                temp_model = QueryBandwidthofOriginminutelyResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryBandwidthofOriginminutelyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthofOriginminutelyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthofOriginminutelyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthofOriginminutelyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthChannelRequest(TeaModel):
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
        need_flow: str = None,
        optional_fields: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
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
        # {"en":"acceleration type.
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
        # 3. If not specified,means all the isp.", "zh_CN":"&nbsp;要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp = isp
        # {"en":"Display statistic result in merged or separate way.
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"If return the flow details:
        # choose 1: Return 
        # choose 0: Not return 
        # the default is 0", "zh_CN":"needFlow 是否需要返回流量明细，1：需要；0：不需要。默认为0."}
        self.need_flow = need_flow
        # {"en":"flowInfo:displays bandwidth peak, peak time, and total flow information;", "zh_CN":"flowInfo ：展示带宽峰值、峰值时间、总流量信息；"}
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
        if self.need_flow is not None:
            result['needFlow'] = self.need_flow
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
        if m.get('needFlow') is not None:
            self.need_flow = m.get('needFlow')
        if m.get('optionalFields') is not None:
            self.optional_fields = m.get('optionalFields')
        return self


class BandwidthChannelResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽，单位Mbps'}
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


class BandwidthChannelResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[BandwidthChannelResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthChannelResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthChannelResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthChannelResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = BandwidthChannelResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class BandwidthChannelResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: BandwidthChannelResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'频道带宽数据'}
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
            temp_model = BandwidthChannelResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthChannelResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthChannelResponseProvider = None,
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
            temp_model = BandwidthChannelResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BillingOrderRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        contract_code: str = None,
        show_detail: str = None,
        dataformat: str = None,
        pay_date_filter: str = None,
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
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号“;”，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号“;”分隔开，如查询大陆及亚太区域，参数填写为：“region=cn;apac”。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"Contract Code. If there are multiple inputs,use ';' as separator.", "zh_CN":"合同号，如contracCode=SR190001，多个请用英文分号";"分隔开"}
        self.contract_code = contract_code
        # {"en":"Show the details of order or not. Optional valuse: true, false.
        # 'false' as defaullt.", "zh_CN":"showDetail=true 显示订单详情，showDetail=false不显示订单详情，默认值是false。"}
        self.show_detail = show_detail
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Filter the billing start and end time of formal orders", "zh_CN":"是否对正式订单的计费起止时间进行过滤。payDateFilter=true表示要过滤，即正式订单只返回计费起止时间与查询时间有交集的结果；payDateFilter=false表示不过滤，默认false；测试订单不受此参数影响"}
        self.pay_date_filter = pay_date_filter

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
        if self.contract_code is not None:
            result['contractCode'] = self.contract_code
        if self.show_detail is not None:
            result['showDetail'] = self.show_detail
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.pay_date_filter is not None:
            result['payDateFilter'] = self.pay_date_filter
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
        if m.get('contractCode') is not None:
            self.contract_code = m.get('contractCode')
        if m.get('showDetail') is not None:
            self.show_detail = m.get('showDetail')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('payDateFilter') is not None:
            self.pay_date_filter = m.get('payDateFilter')
        return self


class BillingOrderResponseProviderDateOrderTypeDetail(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
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


class BillingOrderResponseProviderDateOrderType(TeaModel):
    def __init__(
        self,
        name: str = None,
        detail: List[BillingOrderResponseProviderDateOrderTypeDetail] = None,
    ):
        # {'en':'name', 'zh_CN':'流量'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.detail = detail

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.detail is not None:
            result['detail'] = []
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('detail') is not None:
            self.detail = []
            for k in m.get('detail'):
                temp_model = BillingOrderResponseProviderDateOrderTypeDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class BillingOrderResponseProviderDateOrder(TeaModel):
    def __init__(
        self,
        id: str = None,
        order_info: str = None,
        charge_method: str = None,
        charge_explanation: str = None,
        region_and_isp: str = None,
        acce_type: str = None,
        charge_value: str = None,
        charge_category: str = None,
        detail_info: str = None,
        channel: str = None,
        type: BillingOrderResponseProviderDateOrderType = None,
    ):
        # {'en':'id', 'zh_CN':'订单ID'}
        self.id = id
        # {'en':'orderInfo', 'zh_CN':'订单信息'}
        self.order_info = order_info
        # {'en':'chargeMethod', 'zh_CN':'计费方式'}
        self.charge_method = charge_method
        # {'en':'chargeExplanation', 'zh_CN':'计费说明'}
        self.charge_explanation = charge_explanation
        # {'en':'regionAndIsp', 'zh_CN':'区域和ISP'}
        self.region_and_isp = region_and_isp
        # {'en':'acceType', 'zh_CN':'加速类型'}
        self.acce_type = acce_type
        # {'en':'chargeValue', 'zh_CN':'计费值'}
        self.charge_value = charge_value
        # {'en':'chargeCategory', 'zh_CN':'费用类别'}
        self.charge_category = charge_category
        # {'en':'detailInfo', 'zh_CN':'计费单位'}
        self.detail_info = detail_info
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.type = type

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.order_info, 'order_info')
        self.validate_required(self.charge_method, 'charge_method')
        self.validate_required(self.charge_explanation, 'charge_explanation')
        self.validate_required(self.region_and_isp, 'region_and_isp')
        self.validate_required(self.acce_type, 'acce_type')
        self.validate_required(self.charge_value, 'charge_value')
        self.validate_required(self.charge_category, 'charge_category')
        self.validate_required(self.detail_info, 'detail_info')
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.type, 'type')
        if self.type:
            self.type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.order_info is not None:
            result['orderInfo'] = self.order_info
        if self.charge_method is not None:
            result['chargeMethod'] = self.charge_method
        if self.charge_explanation is not None:
            result['chargeExplanation'] = self.charge_explanation
        if self.region_and_isp is not None:
            result['regionAndIsp'] = self.region_and_isp
        if self.acce_type is not None:
            result['acceType'] = self.acce_type
        if self.charge_value is not None:
            result['chargeValue'] = self.charge_value
        if self.charge_category is not None:
            result['chargeCategory'] = self.charge_category
        if self.detail_info is not None:
            result['detailInfo'] = self.detail_info
        if self.channel is not None:
            result['channel'] = self.channel
        if self.type is not None:
            result['type'] = self.type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('orderInfo') is not None:
            self.order_info = m.get('orderInfo')
        if m.get('chargeMethod') is not None:
            self.charge_method = m.get('chargeMethod')
        if m.get('chargeExplanation') is not None:
            self.charge_explanation = m.get('chargeExplanation')
        if m.get('regionAndIsp') is not None:
            self.region_and_isp = m.get('regionAndIsp')
        if m.get('acceType') is not None:
            self.acce_type = m.get('acceType')
        if m.get('chargeValue') is not None:
            self.charge_value = m.get('chargeValue')
        if m.get('chargeCategory') is not None:
            self.charge_category = m.get('chargeCategory')
        if m.get('detailInfo') is not None:
            self.detail_info = m.get('detailInfo')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('type') is not None:
            temp_model = BillingOrderResponseProviderDateOrderType()
            self.type = temp_model.from_map(m['type'])
        return self


class BillingOrderResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        order: List[BillingOrderResponseProviderDateOrder] = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'订单计费值'}
        self.order = order

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.order, 'order')
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.order is not None:
            result['order'] = []
            for k in self.order:
                result['order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('order') is not None:
            self.order = []
            for k in m.get('order'):
                temp_model = BillingOrderResponseProviderDateOrder()
                self.order.append(temp_model.from_map(k))
        return self


class BillingOrderResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BillingOrderResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'订单计费值'}
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
            temp_model = BillingOrderResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BillingOrderResponse(TeaModel):
    def __init__(
        self,
        provider: BillingOrderResponseProvider = None,
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
            temp_model = BillingOrderResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BillingOrderPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BillingOrderParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BillingOrderRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BillingOrderResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetBandwidthLogRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
        flow_unit: str = None,
        time_from_zero: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM若没有输入时、分，则时分默认为00:01；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM,若没有输入时、分，则时分默认为24:00；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way.
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"The unit of the flow value in the details, the default is Mbps. Optional byte (byte) or bps", "zh_CN":"明细中的流量值单位，默认为Mbps。可选 byte (字节)或者bps"}
        self.flow_unit = flow_unit
        # {"en":"If specified 0,the time return as 00:05--24:00,If specified 1,the time return as 00:00--23:55,If not specified, the default value is 0", "zh_CN":"当值为0:返回00:05--24:00；当值为1:返回00:00--23:55。不传默认为:0"}
        self.time_from_zero = time_from_zero

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
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.flow_unit is not None:
            result['flowUnit'] = self.flow_unit
        if self.time_from_zero is not None:
            result['timeFromZero'] = self.time_from_zero
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
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('flowUnit') is not None:
            self.flow_unit = m.get('flowUnit')
        if m.get('timeFromZero') is not None:
            self.time_from_zero = m.get('timeFromZero')
        return self


class GetBandwidthLogResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
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


class GetBandwidthLogResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[GetBandwidthLogResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = GetBandwidthLogResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class GetBandwidthLogResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: GetBandwidthLogResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = GetBandwidthLogResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class GetBandwidthLogResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: GetBandwidthLogResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'频道带宽数据'}
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
            temp_model = GetBandwidthLogResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class GetBandwidthLogResponse(TeaModel):
    def __init__(
        self,
        provider: GetBandwidthLogResponseProvider = None,
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
            temp_model = GetBandwidthLogResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class GetBandwidthLogPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetBandwidthLogParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetBandwidthLogRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetBandwidthLogResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRealTimeBandwidthForMultiDomainRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        group_by: str = None,
    ):
        # {'en':'Start time: 
        #     1.Start time: time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (December 2rd, 2016, 10:00 a.m., Beijing Time); 
        #     2.Not greater than the current time;
        #     3.The most recent half-year (183 days) data can be obtained
        # ', 'zh_CN':'开始时间：
        # 
        # 时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年1月1日10点0分0秒）；
        # 不能大于当前时间
        # 最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time: 
        #     1.The time format is 2016-12-02T10:00:00+08:00 
        #     2.End time should be greater than start time. If the end time is greater than current time, current time will be used. 
        #     3.If both fields of dataFrom and dateTo are left empty, then data in the last 1 hours will be queried by default; if one field is filled and one is left empty, then exception will occur. 
        #     4.Maximum time range allowable for query: The default value is 1 hour, that is, the difference between dateFrom and dateTo cannot exceed 1 hour (you can contact technical support to adjust it, the maximum is 31 days)
        # ', 'zh_CN':'结束时间：
        # 
        # 时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        # 结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # dateFrom，dateTo二者都未传，默认查询过去的1小时；如仅有一个未传，抛异常
        # 允许查询最大时间间隔：默认1小时，即dateFrom和dateTo相差不能超过1小时（可联系技术支持调整，最长31天）。'}
        self.date_to = date_to
        # {'en':'Data granularity: 
        #     1. Support 1m (1 minute granularity),5m (5 minutes granularity) 
        #     2. The default value is 1m
        # ', 'zh_CN':'数据粒度：不传默认1m
        # 
        # 支持1m（1分钟）、5m（5分钟）'}
        self.data_interval = data_interval
        # {'en':'Domain: 
        #     1.The default upper limit of domains that can be entered is 20 (if you want to adjust, please, contact technical support); 
        #     2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)
        # ', 'zh_CN':'域名：
        # 
        # 可传递域名数量上限默认为20（可联系技术支持调整）；
        # 自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）'}
        self.domain = domain
        # {'en':'The optional value of the grouping dimension is domain; if it is passed in, detailed data will be displayed according to this dimension;', 'zh_CN':'分组维度
        # 
        # 可选值为domain；
        # 有传入则按照该维度展示明细数据；'}
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
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryRealTimeBandwidthForMultiDomainResponseDataBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'Time: 1. When the data query granularity is 1m, then the format is yyyy-MM-dd HH:mm; 
        #     Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00; 
        #     2. Return the time slices that contained in start time and in end time.
        # ', 'zh_CN':'格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。
        # 
        # 一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是第二天（yyyy-MM-dd） 00:00。
        # 
        # 返回开始时间和结束时间包含的时间片'}
        self.timestamp = timestamp
        # {'en':'Edge bandwidth,the unit is Mbps,keep 2 decimal places', 'zh_CN':'带宽值，单位Mbps，保留2位小数。'}
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


class QueryRealTimeBandwidthForMultiDomainResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_value: str = None,
        peak_time: str = None,
        total: str = None,
        bandwidth_data: List[QueryRealTimeBandwidthForMultiDomainResponseDataBandwidthData] = None,
    ):
        # {'en':' Domain name. If you do not select domain name group Dimension, this field is a semicolon-separated string of all domain names.', 'zh_CN':'域名，如果不选择域名分组维度，该字段为所有域名以分号分隔的字符串'}
        self.domain = domain
        # {'en':'Peak Bandwidth,unit is Mbps,example(9811.21Mbps)', 'zh_CN':'峰值带宽，单位Mbps，示例 （9811.21Mbps)'}
        self.peak_value = peak_value
        # {'en':'Time of peak bandwidth,example(2019-02-13 18:01)', 'zh_CN':'峰值时间，示例（2019-02-13 18:01）'}
        self.peak_time = peak_time
        # {'en':'Edge total traffic,example(74099.91MB)', 'zh_CN':'边缘总流量，单位MB，示例 ( 74099.91MB)'}
        self.total = total
        self.bandwidth_data = bandwidth_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.total, 'total')
        self.validate_required(self.bandwidth_data, 'bandwidth_data')
        if self.bandwidth_data:
            for k in self.bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.total is not None:
            result['total'] = self.total
        if self.bandwidth_data is not None:
            result['bandwidthData'] = []
            for k in self.bandwidth_data:
                result['bandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('bandwidthData') is not None:
            self.bandwidth_data = []
            for k in m.get('bandwidthData'):
                temp_model = QueryRealTimeBandwidthForMultiDomainResponseDataBandwidthData()
                self.bandwidth_data.append(temp_model.from_map(k))
        return self


class QueryRealTimeBandwidthForMultiDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryRealTimeBandwidthForMultiDomainResponseData] = None,
    ):
        # {'en':'request result status code', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'request result information', 'zh_CN':'请求结果信息'}
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
                temp_model = QueryRealTimeBandwidthForMultiDomainResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryRealTimeBandwidthForMultiDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeBandwidthForMultiDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeBandwidthForMultiDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeBandwidthForMultiDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCPSBandwidthRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        start_date: str = None,
        end_date: str = None,
        channel: str = None,
        timezone: str = None,
        optional_fields: str = None,
        line_type: str = None,
    ):
        # {"en":"cust_en_name.If there are multiple inputs,use ';' as separator", "zh_CN":"客户的英文名，多个';'隔开"}
        self.cust = cust
        # {"en":"1.Must work with 'enddate' and they specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；
        # 
        # 此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.start_date = start_date
        # {"en":"1.Must work with 'startdate' and they specify the query date scope.
        # 
        # 2.With format yyyy-mm-dd 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；
        # 
        # 此参数需与startdate参数配合,若存在date参数,则该参数无效"}
        self.end_date = end_date
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，
        # 
        # 返回多个频道的汇总值，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，
        # 
        # GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"Input 'flowInfo', which will show the bandwidth peak, peak time, total flow. not selected or null&nbsp;will not be showed", "zh_CN":"入参flowInfo，将展示带宽峰值、峰值时间、总流量,不选或者为空默认不展示"}
        self.optional_fields = optional_fields
        # {"en":"This parameter represents the type of the dedicated line. It can have multiple values. Use the semicolon as a separator if there are multiple values. hk: represents China Premium Service; jp: represents China Premium Service-Basic. eu: not applicable to CDNW. all: not applicable to CDNW.", "zh_CN":"专线类型:hk;jp，支持多个，用分号隔开。hk:中港；jp:中日；eu:中欧；all:所有，默认为：hk"}
        self.line_type = line_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.channel is not None:
            result['channel'] = self.channel
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.optional_fields is not None:
            result['optionalFields'] = self.optional_fields
        if self.line_type is not None:
            result['lineType'] = self.line_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('optionalFields') is not None:
            self.optional_fields = m.get('optionalFields')
        if m.get('lineType') is not None:
            self.line_type = m.get('lineType')
        return self


class QueryCPSBandwidthResponseDataDetail(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
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


class QueryCPSBandwidthResponseData(TeaModel):
    def __init__(
        self,
        total_flow: str = None,
        peak_time: str = None,
        peak_value: str = None,
        detail: QueryCPSBandwidthResponseDataDetail = None,
    ):
        # {'en':'totalFlow', 'zh_CN':'总流量，单位GB'}
        self.total_flow = total_flow
        # {'en':'peakTime', 'zh_CN':'峰值时间'}
        self.peak_time = peak_time
        # {'en':'peakvalue', 'zh_CN':'带宽峰值，单位Mbps'}
        self.peak_value = peak_value
        # {'en':'detail', 'zh_CN':'时点带宽数据'}
        self.detail = detail

    def validate(self):
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('detail') is not None:
            temp_model = QueryCPSBandwidthResponseDataDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class QueryCPSBandwidthResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryCPSBandwidthResponseData = None,
    ):
        # {'en':'code', 'zh_CN':'返回编码'}
        self.code = code
        # {'en':'message', 'zh_CN':'返回消息'}
        self.message = message
        # {'en':'data', 'zh_CN':'频道带宽数据'}
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
            temp_model = QueryCPSBandwidthResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCPSBandwidthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCPSBandwidthParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCPSBandwidthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCPSBandwidthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryP2PBandwidthRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        accetype: str = None,
        dataformat: str = None,
        is_exact_match: str = None,
        is_log: str = None,
        box: str = None,
        flow: str = None,
        region: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date: 1.With format yyyy-mm-dd. 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they specify the query date scope. 2.With format yyyy-mm-dd. 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they specify the query date scope.
        # 2.With format yyyy-mm-dd
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Whether the channel is completely matched. When it is true, the complete domain name must be filled in (invalid or duplicate channels entered by the user will be filtered at this time, and 403 will be returned if all input channels are invalid. If it is not true, the display will end with the channel entered by the user All channels. Defaults to true", "zh_CN":"频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"A value of 1 means log bandwidth is returned, 0 means cdn bandwidth is returned, and the default value is 0", "zh_CN":"值为1，表示返回的是log带宽，0表示返回的是cdn带宽，默认值为0"}
        self.is_log = is_log
        # {"en":"Control whether to return box bandwidth, the default is 0, when box=1, return cdn(log) bandwidth+p2p bandwidth+box bandwidth; when box=0, return cdn(log) bandwidth+p2p bandwidth", "zh_CN":"控制是否返回盒子带宽,默认为0,box=1时，返回cdn(log)带宽+p2p带宽+box带宽;box=0时，返回cdn(log)带宽+p2p带宽"}
        self.box = box
        # {"en":"Control whether to return flow details, the default is 0 and no return, return flow details when passing 1", "zh_CN":"控制是否返回流量明细，默认为0不返回，传1时返回流量明细"}
        self.flow = flow
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region

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
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.is_log is not None:
            result['isLog'] = self.is_log
        if self.box is not None:
            result['box'] = self.box
        if self.flow is not None:
            result['flow'] = self.flow
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('isLog') is not None:
            self.is_log = m.get('isLog')
        if m.get('box') is not None:
            self.box = m.get('box')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class QueryP2PBandwidthResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        p_2p: str = None,
        cdn: str = None,
        box: str = None,
        total: str = None,
    ):
        # {'en':'time', 'zh_CN':'时间点，格式 yyyy-MM-dd hh:mm:ss'}
        self.time = time
        # {'en':'p2pBandWidth', 'zh_CN':'cdn带宽，单位 Mbps'}
        self.p_2p = p_2p
        # {'en':'cdnBandWidth', 'zh_CN':'cdn带宽，单位 Mbps'}
        self.cdn = cdn
        # {'en':'boxBandWidth', 'zh_CN':'p2sp带宽，单位 Mbps'}
        self.box = box
        # {'en':'totalBandWidth', 'zh_CN':'总带宽，单位 Mbps'}
        self.total = total

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.p_2p, 'p_2p')
        self.validate_required(self.cdn, 'cdn')
        self.validate_required(self.box, 'box')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.p_2p is not None:
            result['p2p'] = self.p_2p
        if self.cdn is not None:
            result['cdn'] = self.cdn
        if self.box is not None:
            result['box'] = self.box
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('p2p') is not None:
            self.p_2p = m.get('p2p')
        if m.get('cdn') is not None:
            self.cdn = m.get('cdn')
        if m.get('box') is not None:
            self.box = m.get('box')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryP2PBandwidthResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[QueryP2PBandwidthResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'p2p带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = QueryP2PBandwidthResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class QueryP2PBandwidthResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: QueryP2PBandwidthResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = QueryP2PBandwidthResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class QueryP2PBandwidthResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: QueryP2PBandwidthResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'p2p带宽数据'}
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
            temp_model = QueryP2PBandwidthResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class QueryP2PBandwidthResponse(TeaModel):
    def __init__(
        self,
        provider: QueryP2PBandwidthResponseProvider = None,
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
            temp_model = QueryP2PBandwidthResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class QueryP2PBandwidthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryP2PBandwidthParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryP2PBandwidthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryP2PBandwidthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthTotalRequest(TeaModel):
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
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
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
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1)If there isp multiple inputs,use ';' as demimeter.
        # 2)optional values of isp: refers to the ISP-section of appendix.
        # 3) If not specified,means all the isp.", "zh_CN":"&nbsp;要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp = isp

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
        return self


class BandwidthTotalResponseProviderDateChannelTotalFlow(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        # {'en':'the total flow(GB)', 'zh_CN':'总流量（单位GB）'}
        self.text = text

    def validate(self):
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class BandwidthTotalResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        total_flow: List[BandwidthTotalResponseProviderDateChannelTotalFlow] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'totalFlow', 'zh_CN':'总流量'}
        self.total_flow = total_flow

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.total_flow, 'total_flow')
        if self.total_flow:
            for k in self.total_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.total_flow is not None:
            result['totalFlow'] = []
            for k in self.total_flow:
                result['totalFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalFlow') is not None:
            self.total_flow = []
            for k in m.get('totalFlow'):
                temp_model = BandwidthTotalResponseProviderDateChannelTotalFlow()
                self.total_flow.append(temp_model.from_map(k))
        return self


class BandwidthTotalResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthTotalResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = BandwidthTotalResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class BandwidthTotalResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: BandwidthTotalResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'时点数据'}
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
            temp_model = BandwidthTotalResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthTotalResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthTotalResponseProvider = None,
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
            temp_model = BandwidthTotalResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthTotalPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthTotalParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthTotalRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthTotalResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainOriginResponseTimeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {'en':'Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2024-01-23T10:00 + 08:00 (10:00:00 Beijing time on January 23, 2024);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.', 'zh_CN':'开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2024-01-23T10:00:00+08:00（为北京时间2024年01月23日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days. ', 'zh_CN':'结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天。'}
        self.date_to = date_to
        # {'en':'Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment);
        # 
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).', 'zh_CN':'域名：
        # 
        # 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)；
        # 
        # 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。'}
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


class ReportDomainOriginResponseTimeServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'Time:
        # 
        # 1. When the data query granularity is 1m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        # 2. Return the time slices that contained in start time and in end time.', 'zh_CN':'时间，
        # 查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Return to origin response time. Unit is ms and 2 digits of decimals are allowed.
        # ', 'zh_CN':'回源响应时间，单位ms。保留2位小数'}
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


class ReportDomainOriginResponseTimeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportDomainOriginResponseTimeServiceResponseDataDetailList] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'details', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportDomainOriginResponseTimeServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportDomainOriginResponseTimeServiceResponse(TeaModel):
    def __init__(
        self,
        data: List[ReportDomainOriginResponseTimeServiceResponseData] = None,
    ):
        # {'en':'data', 'zh_CN':'请求结果'}
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
                temp_model = ReportDomainOriginResponseTimeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainOriginResponseTimeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainOriginResponseTimeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainOriginResponseTimeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainOriginResponseTimeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportCountryServerBandwidthServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        country_code: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days.  ", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error,you can contact technical support for adjustment);
        # 
        # 2.Domain is uploaded: Up to 20 domains are supported(you can contact technical support for adjustment).", "zh_CN":"域名:
        # 
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)。"}
        self.domain = domain
        # {"en":"Country area:
        # 
        # 1. countryCode is not uploaded: Query all country areas by default;
        # 
        # 2. countryCode is uploaded: Multiple can be uploaded, such as cn, in.  Please refer to the appendix description section of the overview page.", "zh_CN":"国家区域(含中国台湾、中国澳门、中国香港、中国大陆):
        # 
        # 1.未传递countryCode时:查询全部国家区域;
        # 
        # 2.有传递countryCode时:可传多个,如cn,in。可传递的值详见概览页附录说明章节"}
        self.country_code = country_code
        # {"en":"Data granularity:
        # 
        # 5m: 5 minute granularity; Default value is 5m.
        # 
        # 1h: 1 hour granularity.", "zh_CN":"数据粒度:
        # 
        # 5m:5分钟粒度。不传默认5分钟粒度
        # 
        # 1h:1小时粒度;"}
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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.country_code is not None:
            result['countryCode'] = self.country_code
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
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        return self


class ReportCountryServerBandwidthServiceResponseCountryDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        flow: str = None,
    ):
        # {"en":"Time:
        # 
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; ach time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        # 2. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00;
        # 
        # 3. Return the time slices that contained in start time and in end time.", "zh_CN":"时间,
        # 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00;
        # 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Bandwidth value, unit Mbps", "zh_CN":"时间点对应的边缘带宽数据,单位Mbps"}
        self.value = value
        # {"en":"Flow, unit MB", "zh_CN":"时间点对应的边缘流量,单位MB"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class ReportCountryServerBandwidthServiceResponseCountryData(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        detail_list: List[ReportCountryServerBandwidthServiceResponseCountryDataDetailList] = None,
    ):
        # {"en":"Country area", "zh_CN":"国家地区"}
        self.country_code = country_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.country_code, 'country_code')
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
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportCountryServerBandwidthServiceResponseCountryDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportCountryServerBandwidthServiceResponse(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[ReportCountryServerBandwidthServiceResponseCountryData] = None,
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
                temp_model = ReportCountryServerBandwidthServiceResponseCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class ReportCountryServerBandwidthServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportCountryServerBandwidthServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportCountryServerBandwidthServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportCountryServerBandwidthServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportBandwidthRequestByIPIspProvinceRequest(TeaModel):
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
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2024-12-23T10:00 + 08:00 (10:00:00 Beijing time on December 23, 2024);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2024-12-23T10:00:00+08:00（为北京时间2024年12月23日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days.  ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to
        # {"en":"Domains: 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment); 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).", "zh_CN":"域名： 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)； 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。"}
        self.domain = domain
        # {"en":"Data granularity: 1m:1 mintues5m: 5 minute granularity; Default value is 5m. ", "zh_CN":"数据粒度：1m：1分钟粒度 5m：5分钟粒度。不传默认5分钟粒度 "}
        self.data_interval = data_interval
        # {"en":"Province: 1. Province is empty: Query all provinces and aggregate the returned data according to all provinces; 2. Province : please send province code. ", "zh_CN":"省份： 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。 2.有传递province时：传递省份code，可传多个"}
        self.province = province
        # {"en":"ISP: 1. ISP  is empty: Query all ISPs and aggregate the returned data according to all ISPs; 2. ISP: please send ISP code.", "zh_CN":"运营商： 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 2.有传递isp时：传递运营商code，可传多个"}
        self.isp = isp
        # {"en":"Group dimension 1.Options are domain, province, isp, and more than one value can be entered; 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度 可选值为domain、province、isp，可传入多个值； 有传入则按照该维度展示明细数据； 没传默认全部聚合。"}
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


class ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        v_4request: str = None,
        v_4bandwidth: str = None,
        v_6request: str = None,
        v_6bandwidth: str = None,
    ):
        # {"en":"Time: 1.the format is yyyy-MM-dd HH:mm;   ach time slice value represents the value within the previous time granularity range. When the data query granularity is 5m,The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00; 2. When the data query granularity is 1m, The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00.", "zh_CN":"时间， 格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。查询的数据粒度为5m时，一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00； 查询的数据粒度为1m时，一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；"}
        self.timestamp = timestamp
        # {"en":"Number of IPv4 requests.", "zh_CN":"IPv4请求数"}
        self.v_4request = v_4request
        # {"en":"Bandwidth of IPv4", "zh_CN":"IPv4带宽 单位Mbps。保留2位小数"}
        self.v_4bandwidth = v_4bandwidth
        # {"en":"Number of IPv6 requests.", "zh_CN":"IPv6请求数"}
        self.v_6request = v_6request
        # {"en":"Bandwidth of IPv6", "zh_CN":"IPv6带宽 单位Mbps。保留2位小数"}
        self.v_6bandwidth = v_6bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.v_4request, 'v_4request')
        self.validate_required(self.v_4bandwidth, 'v_4bandwidth')
        self.validate_required(self.v_6request, 'v_6request')
        self.validate_required(self.v_6bandwidth, 'v_6bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.v_4request is not None:
            result['v4Request'] = self.v_4request
        if self.v_4bandwidth is not None:
            result['v4Bandwidth'] = self.v_4bandwidth
        if self.v_6request is not None:
            result['v6Request'] = self.v_6request
        if self.v_6bandwidth is not None:
            result['v6Bandwidth'] = self.v_6bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('v4Request') is not None:
            self.v_4request = m.get('v4Request')
        if m.get('v4Bandwidth') is not None:
            self.v_4bandwidth = m.get('v4Bandwidth')
        if m.get('v6Request') is not None:
            self.v_6request = m.get('v6Request')
        if m.get('v6Bandwidth') is not None:
            self.v_6bandwidth = m.get('v6Bandwidth')
        return self


class ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceData(TeaModel):
    def __init__(
        self,
        detail_list: List[ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceDataDetailList] = None,
    ):
        # {"en":"", "zh_CN":""}
        self.detail_list = detail_list

    def validate(self):
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
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportBandwidthRequestByIPIspProvinceResponseDataIspData(TeaModel):
    def __init__(
        self,
        province_data: List[ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceData] = None,
    ):
        # {"en":"Province code", "zh_CN":"省份code"}
        self.province_data = province_data

    def validate(self):
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
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportBandwidthRequestByIPIspProvinceResponseDataIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportBandwidthRequestByIPIspProvinceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportBandwidthRequestByIPIspProvinceResponseDataIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"ISP code", "zh_CN":"运营商code"}
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
                temp_model = ReportBandwidthRequestByIPIspProvinceResponseDataIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportBandwidthRequestByIPIspProvinceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportBandwidthRequestByIPIspProvinceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"result", "zh_CN":"结果"}
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
                temp_model = ReportBandwidthRequestByIPIspProvinceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportBandwidthRequestByIPIspProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRequestByIPIspProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRequestByIPIspProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRequestByIPIspProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBandwidthMinutelyRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        region: str = None,
        group_by: str = None,
    ):
        # {"en":"Start Time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, December 2, 2016 10:00-02T10:00:00+08:00 (Beijing time on December 2, 2016 10:00 am 0 seconds);
        # 2. No more than the current time
        # 3. Only available for the last 30 minutes.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.只能查询最近30分钟。"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. Time Format 2016-12-02T10:00:00+08:00
        # 2. the end time should be greater than the start time. if the end time is greater than the current time, take the current time.
        # 3. dateFrom, dateTo both not upload, default query past 30 minutes; If only one is not sent, throw exception
        # 4. Allow maximum query interval: 30 minutes, i.e. the difference between dateFrom and dateTo should not exceed 30 minutes.", "zh_CN":"结束时间：
        # 
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的30分钟；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：30分钟，即dateFrom和dateTo相差不能超过30分钟。"}
        self.date_to = date_to
        # {"en":"Multiple domain names:
        # 1. The maximum number of incoming domain names is 50 (contact technical support for adjustment).
        # 2. filter out invalid domain name; A domain name that is not in the historical domain name table.", "zh_CN":"多域名：
        # 1.单次传入域名数量最多50个（可联系技术支持调整）。
        # 2.过滤掉无效域名；即不在历史域名表中的域名。"}
        self.domain = domain
        # {"en":"Acceleration zone:
        # 1. do not pass the default query to all areas.
        # 2. currently only the leaflet area is supported externally.
        # 3. optional values: cn, apac, am, emea.", "zh_CN":"加速区域：
        # 1.不传默认查询全部区域。
        # 2.目前对外只支持传单区域。
        # 3.可选值：cn、apac、am、emea；"}
        self.region = region
        # {"en":"grouped dimension:
        # 1. the optional value is domain.
        # 2. If incoming data is shown in accordance with the dimension;", "zh_CN":"分组维度:
        # 1.可选值为domain；
        # 2.有传入则按照该维度展示明细数据；"}
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
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryBandwidthMinutelyResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_time: str = None,
        peak_value: str = None,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Peak Time", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"Peak Bandwidth", "zh_CN":"带宽峰值"}
        self.peak_value = peak_value
        # {"en":"The granularity of data is 1 minute, and the format is yyyy-MM-dd HH:MM. Each time slice data value represents the data value in the previous time granularity range. Returns the time slice included with the start and end times.", "zh_CN":"数据粒度为1分钟，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。
        #                 一天开始的时间片是yyyy-MM-dd 00:01:00，最后一个时间片是（yyyy-MM-dd） 24:00:00。
        #                 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Bandwidth value in Mbps, with 2 decimal places reserved.", "zh_CN":"带宽值，单位Mbps，保留2位小数。"}
        self.value = value

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryBandwidthMinutelyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryBandwidthMinutelyResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
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
                temp_model = QueryBandwidthMinutelyResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryBandwidthMinutelyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthMinutelyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthMinutelyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthMinutelyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportLogBandwidthMultiDomainEcdnEdgeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        region: List[str] = None,
        group_by: str = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 90 days, that is, the difference between dateFrom and dateTo can not exceed 90 days.", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：31天，即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The default upper limit of domains that can be entered is 20 (if you want to adjust, please, contact technical support);
        # 2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        # 3.域名超过上限，报错"}
        self.domain = domain
        # {"en":"region:
        # 1. All areas are queried by default if the system does not transmit data.
        # 2. Multiple regions can be passed. The value can be cn, hk, ov, apac, am, emea, or fg.", "zh_CN":"区域：
        # 1.不传默认查询全部区域。
        # 2.支持传递多个区域，可选值为：cn、hk、ov、apac、am、emea、fg。"}
        self.region = region
        # {"en":"Grouping dimension:
        # 1. By default, it is not transmitted and displayed in aggregation mode;
        # 2. The optional value supports only domain, and displays detailed data by domain.", "zh_CN":"分组维度
        # 1.默认不传，聚合展示；
        # 2.可选值仅支持domain，传入时按域名展示明细数据。"}
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
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseDataBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"The data granularity is 1 minute,the format is yyyy-MM-dd HH:mm", "zh_CN":"数据粒度为5分钟，格式为yyyy-MM-dd HH:mm；"}
        self.timestamp = timestamp
        # {"en":"Edge bandwidth,the unit is Mbps,keep 2 decimal places", "zh_CN":"边缘带宽值，单位Mbps，保留2位小数。"}
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


class ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_value: str = None,
        peak_time: str = None,
        total: str = None,
        bandwidth_data: List[ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseDataBandwidthData] = None,
    ):
        # {"en":"Domain name. If you do not select domain name group Dimension, this field is a semicolon-separated string of all domain names.", "zh_CN":"域名，如果不选择域名分组维度，该字段为所有域名以分号分隔的字符串。"}
        self.domain = domain
        # {"en":"Peak Bandwidth,unit is Mbps,example(9811.21Mbps)", "zh_CN":"峰值带宽 Mbps，示例 （931556.21 Mbps）"}
        self.peak_value = peak_value
        # {"en":"Time of peak bandwidth,example(2019-02-13 18:01)", "zh_CN":"峰值时间，示例（2019-02-13 18:01）;"}
        self.peak_time = peak_time
        # {"en":"Edge total traffic,example(74099.91MB)", "zh_CN":"边缘总流量，示例 ( 74099.92 MB )"}
        self.total = total
        self.bandwidth_data = bandwidth_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.total, 'total')
        self.validate_required(self.bandwidth_data, 'bandwidth_data')
        if self.bandwidth_data:
            for k in self.bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.total is not None:
            result['total'] = self.total
        if self.bandwidth_data is not None:
            result['bandwidthData'] = []
            for k in self.bandwidth_data:
                result['bandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('bandwidthData') is not None:
            self.bandwidth_data = []
            for k in m.get('bandwidthData'):
                temp_model = ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseDataBandwidthData()
                self.bandwidth_data.append(temp_model.from_map(k))
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
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
                temp_model = ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogBandwidthMultiDomainEcdnEdgeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportP2SPOriginBandwidthWildcardDomainServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        wildcard_domain: List[str] = None,
        group_by: str = None,
    ):
        # {'en':'Start time:
        # 1. The format is yyyy-MM-ddTHH:mm:SS+08:00, for example, 2016-12-02T10:00 + 08:00 (10:00:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.', 'zh_CN':'开始时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2021-05-19T10:00:00+08:00(为北京时间2021年5月19日10点0分0秒);
        #         2.不能大于当前时间;
        #         3.最多可获取最近半年(183天)的数据'}
        self.date_from = date_from
        # {'en':'End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time;
        # 3. If the end time is greater than the current time, the current time is taken;
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours, if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 31 days, that is the difference between dateFrom and dateTo can not exceed 31 days. ', 'zh_CN':'结束时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间;
        #         3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        #         4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天.'}
        self.date_to = date_to
        # {'en':'Wildcard Domain:
        # 1. The upper limit of the number of Wildcard Domain names that can be passed is 20 by default (contact technical support for adjustment);
        # 2. Automatically filter out invalid domain names (if a non-common domain name is passed in, it will be filtered out);
        # 3. If it is not filled, all pan domain names under the account will be queried by default.', 'zh_CN':'泛域名:
        #         1.可传递泛域名数量上限默认为20个(可联系技术支持调整);
        #         2.自动过滤掉无效域名(如传递非泛域名,会被过滤掉);
        #         3.如未填,则默认查询此账号下所有泛域名.'}
        self.wildcard_domain = wildcard_domain
        # {'en':'Grouped dimension:
        # 1.When the "groupBy" parameter has a value, the value can only be "domain". It will group and return the detailed back-to-origin bandwidth based on wildcard domains and exact domains.
        # 2.When groupBy does not have a value, return the total origin bandwidth details for the wildcard domain. ', 'zh_CN':'	
        # 分组维度:
        # 1.有传值时,只能选domain,按照泛域名及精确域名分组返回回源带宽明细;
        # 2.不传时:返回查询泛域名下的总回源带宽明细.'}
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
        if self.wildcard_domain is not None:
            result['wildcardDomain'] = self.wildcard_domain
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('wildcardDomain') is not None:
            self.wildcard_domain = m.get('wildcardDomain')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainListOriginBandwidthList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'Time:
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 2. Return the time slices that contained in start time and in end time.', 'zh_CN':'时间,
        # 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值.一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 返回开始时间和结束时间包含的时间片.'}
        self.timestamp = timestamp
        # {'en':'Origin bandwidth value. Unit is Mbps and 2 digits of decimals are allowed', 'zh_CN':'回源带宽数据,单位Mbps,保留2位小数.'}
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


class ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        origin_bandwidth_list: List[ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainListOriginBandwidthList] = None,
    ):
        # {'en':'Domain', 'zh_CN':'明细域名'}
        self.domain = domain
        self.origin_bandwidth_list = origin_bandwidth_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.origin_bandwidth_list, 'origin_bandwidth_list')
        if self.origin_bandwidth_list:
            for k in self.origin_bandwidth_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.origin_bandwidth_list is not None:
            result['originBandwidthList'] = []
            for k in self.origin_bandwidth_list:
                result['originBandwidthList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('originBandwidthList') is not None:
            self.origin_bandwidth_list = []
            for k in m.get('originBandwidthList'):
                temp_model = ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainListOriginBandwidthList()
                self.origin_bandwidth_list.append(temp_model.from_map(k))
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceResponseData(TeaModel):
    def __init__(
        self,
        wildcard_domain: str = None,
        domain_list: List[ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainList] = None,
    ):
        # {'en':'Wildcard domain', 'zh_CN':'泛域名'}
        self.wildcard_domain = wildcard_domain
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.wildcard_domain, 'wildcard_domain')
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wildcard_domain is not None:
            result['wildcardDomain'] = self.wildcard_domain
        if self.domain_list is not None:
            result['domainList'] = []
            for k in self.domain_list:
                result['domainList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wildcardDomain') is not None:
            self.wildcard_domain = m.get('wildcardDomain')
        if m.get('domainList') is not None:
            self.domain_list = []
            for k in m.get('domainList'):
                temp_model = ReportP2SPOriginBandwidthWildcardDomainServiceResponseDataDomainList()
                self.domain_list.append(temp_model.from_map(k))
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportP2SPOriginBandwidthWildcardDomainServiceResponseData] = None,
    ):
        # {'en':'Request result status code', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'Request result information', 'zh_CN':'请求结果信息'}
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
                temp_model = ReportP2SPOriginBandwidthWildcardDomainServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportP2SPOriginBandwidthWildcardDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportP2SPOriginBandwidthWildcardDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportIPV6BandwidthServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据."}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days. ", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天."}
        self.date_to = date_to
        # {"en":"Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error,you can contact technical support for adjustment) ;
        # 
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).", "zh_CN":"域名:
        # 
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)."}
        self.domain = domain
        # {"en":"Data granularity:
        # 
        # 5m: 5 minute granularity; Default value is 5m.
        # 
        # 1h: 1 hour granularity.", "zh_CN":"数据粒度:
        # 
        # 5m:5分钟粒度.不传默认5分钟粒度
        # 
        # 1h:1小时粒度;"}
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


class ReportIPV6BandwidthServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        flow: str = None,
    ):
        # {"en":"Time:
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; ach time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;", "zh_CN":"时间,
        # 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值.一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值.一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00;
        # 返回开始时间和结束时间包含的时间片."}
        self.timestamp = timestamp
        # {"en":"IPV6 bandwidth data, unit Mbps. Keep 2 decimal places", "zh_CN":"IPV6带宽数据,单位Mbps.保留2位小数"}
        self.value = value
        # {"en":"IPV6 traffic, unit MB. Keep 2 decimal places", "zh_CN":"IPV6流量,单位MB.保留2位小数"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class ReportIPV6BandwidthServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportIPV6BandwidthServiceResponseDataDetailList] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
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
                temp_model = ReportIPV6BandwidthServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportIPV6BandwidthServiceResponse(TeaModel):
    def __init__(
        self,
        data: List[ReportIPV6BandwidthServiceResponseData] = None,
    ):
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
                temp_model = ReportIPV6BandwidthServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportIPV6BandwidthServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIPV6BandwidthServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIPV6BandwidthServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIPV6BandwidthServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelValueSumRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        is_exact_match: str = None,
        accetype: str = None,
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
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
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
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.accetype is not None:
            result['accetype'] = self.accetype
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
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class ChannelValueSumResponseProviderDateInformationBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        charge_method: str = None,
        value: str = None,
        unit: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'charge method', 'zh_CN':'计费方式'}
        self.charge_method = charge_method
        # {'en':'charge value', 'zh_CN':'计费值'}
        self.value = value
        # {'en':'charge unit', 'zh_CN':'计费单位'}
        self.unit = unit

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.charge_method, 'charge_method')
        self.validate_required(self.value, 'value')
        self.validate_required(self.unit, 'unit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.charge_method is not None:
            result['charge-method'] = self.charge_method
        if self.value is not None:
            result['value'] = self.value
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('charge-method') is not None:
            self.charge_method = m.get('charge-method')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class ChannelValueSumResponseProviderDateInformation(TeaModel):
    def __init__(
        self,
        channel: str = None,
        bandwidth: List[ChannelValueSumResponseProviderDateInformationBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = ChannelValueSumResponseProviderDateInformationBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class ChannelValueSumResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        information: List[ChannelValueSumResponseProviderDateInformation] = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'information', 'zh_CN':'频道计费数据'}
        self.information = information

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.information, 'information')
        if self.information:
            for k in self.information:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.information is not None:
            result['information'] = []
            for k in self.information:
                result['information'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('information') is not None:
            self.information = []
            for k in m.get('information'):
                temp_model = ChannelValueSumResponseProviderDateInformation()
                self.information.append(temp_model.from_map(k))
        return self


class ChannelValueSumResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: ChannelValueSumResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'多域名总计费带宽数据'}
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
            temp_model = ChannelValueSumResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class ChannelValueSumResponse(TeaModel):
    def __init__(
        self,
        provider: ChannelValueSumResponseProvider = None,
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
            temp_model = ChannelValueSumResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class ChannelValueSumPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueSumParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueSumRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueSumResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportLowDelayCountryBandwidthServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        area_code: List[str] = None,
        country_code: List[str] = None,
    ):
        # {"en":"Start time:
        # 	1.The format is yyyy-MM-ddTHH:mm:ss+08:00; 
        # 	2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo; 
        # 	3.Period between dataFrom and dateTo cannot be longer than 7 days; 
        # 	4.dateFrom and dateTo can be either both are specified or neither is specifies; 
        # 	5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天;(可联系技术支持调整)
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time: 
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00.
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 250 (can be adjusted by contacting technical support).
        # 	2.Domain is not uploaded: Query all domain names of the account", "zh_CN":"域名:可传递域名数量上限默认为250个(可联系技术支持调整),未传递该入参时查询账号下所有域名,但当账号下域名数量超过限制时不可查询(报错)"}
        self.domain = domain
        # {"en":"Acceleration zone:
        # 1. If not passed or empty, it defaults to all regions.
        # 2. Multiple areas are separated by English semicolons;
        # 3. The optional values are: cn, apac, etc., see the overview page [Appendix 1] for details", "zh_CN":"加速区域:
        # 1.不选或者为空时默认为全部区域。
        # 2.多个区域使用英文分号分隔;
        # 3.可选值为:cn、apac…等,详见概览页【附表1】说明"}
        self.area_code = area_code
        # {"en":"Country code:
        # 1.If no value is passed, all countries and regions will be queried by default;
        # 2.For the values that can be passed, see the overview page [Appendix 1] for details.", "zh_CN":"国家地区代号:
        # 1.不传默认查询全部国家地区;
        # 2.可传递的值详见概览页【附表1】说明。"}
        self.country_code = country_code

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
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        return self


class ReportLowDelayCountryBandwidthServiceResponseDataCountryDataBandwidthList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time:
        # 																	1.When the query data granularity is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value within the previous time granularity range. 
        # 																	2.The time slice at the beginning of a day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00; return the time slice included in the start time and end time.", "zh_CN":"时间:
        # 																	1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。
        # 																	2.一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"The bandwidth value corresponding to the time point, in Mbps", "zh_CN":"时间点对应的带宽值,单位Mbps"}
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


class ReportLowDelayCountryBandwidthServiceResponseDataCountryData(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        bandwidth_list: List[ReportLowDelayCountryBandwidthServiceResponseDataCountryDataBandwidthList] = None,
    ):
        # {"en":"CountryCode", "zh_CN":"国家地区"}
        self.country_code = country_code
        self.bandwidth_list = bandwidth_list

    def validate(self):
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.bandwidth_list, 'bandwidth_list')
        if self.bandwidth_list:
            for k in self.bandwidth_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.bandwidth_list is not None:
            result['bandwidthList'] = []
            for k in self.bandwidth_list:
                result['bandwidthList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('bandwidthList') is not None:
            self.bandwidth_list = []
            for k in m.get('bandwidthList'):
                temp_model = ReportLowDelayCountryBandwidthServiceResponseDataCountryDataBandwidthList()
                self.bandwidth_list.append(temp_model.from_map(k))
        return self


class ReportLowDelayCountryBandwidthServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[ReportLowDelayCountryBandwidthServiceResponseDataCountryData] = None,
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
                temp_model = ReportLowDelayCountryBandwidthServiceResponseDataCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class ReportLowDelayCountryBandwidthServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportLowDelayCountryBandwidthServiceResponseData] = None,
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
                temp_model = ReportLowDelayCountryBandwidthServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportLowDelayCountryBandwidthServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLowDelayCountryBandwidthServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLowDelayCountryBandwidthServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLowDelayCountryBandwidthServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportLogFlowIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time 
        # 	1.The format is yyyy-MM-ddTHH:mm:ss+08:00; 
        # 	2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo; 
        # 	3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust); 
        # 	4.dateFrom and dateTo can be either both are specified or neither is specifies; 
        # 	5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天;(可联系技术支持调整)
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据;"}
        self.date_from = date_from
        # {"en":"End time 
        # 	1.The format is yyyy-MM-ddTHH:mm:ss+08:00; 
        # 	2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Data granularity, 5m: 5-minute granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度。默认5分钟粒度"}
        self.data_interval = data_interval
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个(可联系技术支持调整)"}
        self.domain = domain
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
        # 	1.Options are domain, province, isp, and more than one value can be entered; 
        # 	2.The data is displayed according to the specified dimension", "zh_CN":"分组维度
        #     1.可选值为domain、province、isp,可传入多个值;
        #     2.有传入则按照该维度展示明细数据;"}
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
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        flow: str = None,
        bandwidth: str = None,
    ):
        # {"en":"Time:
        # 				1.When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 				2.When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        # 				3.Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间:
        # 
        # 1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00。
        # 2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00。
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Traffic unit is MB and 2 digits of decimals allowed", "zh_CN":"流量值,单位为MB,保留两位小数"}
        self.flow = flow
        # {"en":"Bandwidth value. Unit is Mbps and 2 digits of decimals allowed", "zh_CN":"带宽值,单位为Mbps,保留两位小数"}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.flow, 'flow')
        self.validate_required(self.bandwidth, 'bandwidth')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self


class ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        details: List[ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceDataDetails] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
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
                temp_model = ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportLogFlowIspProvinceServiceResponseDataIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceData] = None,
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
                temp_model = ReportLogFlowIspProvinceServiceResponseDataIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportLogFlowIspProvinceServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportLogFlowIspProvinceServiceResponseDataIspData] = None,
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
                temp_model = ReportLogFlowIspProvinceServiceResponseDataIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportLogFlowIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportLogFlowIspProvinceServiceResponseData] = None,
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
                temp_model = ReportLogFlowIspProvinceServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportLogFlowIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogFlowIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogFlowIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportLogFlowIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthVmRequest(TeaModel):
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
        isp_id: str = None,
        ip_protocol: str = None,
        bandwidth_type: str = None,
        node: str = None,
        optional_fields: str = None,
        group_by: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到天,日期格式为yyyy-mm-dd 此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到天,日期格式为yyyy-mm-dd 此参数需与startdate参数配合,若存在date参数,则该参数无效"}
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
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1.If there isp multiple inputs,use ';' as demimeter.
        # 2.optional values of isp: refers to the ISP-section of appendix.
        # 3. If not specified,means all the isp.", "zh_CN":"要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp_id = isp_id
        # {"en":"choose the ipv4 or ipv6.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"ipv4、ipv6，不填默认查全部"}
        self.ip_protocol = ip_protocol
        # {"en":"the type of bandwidth:
        # 1. in : the in's bandwidth.
        # 2. out: the out's bandwidth.
        # 3. ein: the exin's bandwidth.
        # 4. eout: the exout's bandwidth.", "zh_CN":"带宽类型：in:流入带宽,out:流出带宽;ein:外网流入带宽,eout:外网流出带宽。不传或者空时默认为：in:流入带宽,out:流出带宽;ein:外网流入带宽,eout:外网流出带宽"}
        self.bandwidth_type = bandwidth_type
        # {"en":"The name of the node", "zh_CN":"节点名称"}
        self.node = node
        # {"en":"chargeInfo:show the charge method,charge value,the 95 of charge value", "zh_CN":"chargeInfo：计费时间计费方式、计费值、95值"}
        self.optional_fields = optional_fields
        # {"en":"method of data aggregation, can be left blank or filled with 'isp'", "zh_CN":"groupBy：数据聚合方式，可不填或填'isp'"}
        self.group_by = group_by

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
        if self.isp_id is not None:
            result['ispId'] = self.isp_id
        if self.ip_protocol is not None:
            result['ipProtocol'] = self.ip_protocol
        if self.bandwidth_type is not None:
            result['bandwidthType'] = self.bandwidth_type
        if self.node is not None:
            result['node'] = self.node
        if self.optional_fields is not None:
            result['optionalFields'] = self.optional_fields
        if self.group_by is not None:
            result['groupBy'] = self.group_by
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
        if m.get('ispId') is not None:
            self.isp_id = m.get('ispId')
        if m.get('ipProtocol') is not None:
            self.ip_protocol = m.get('ipProtocol')
        if m.get('bandwidthType') is not None:
            self.bandwidth_type = m.get('bandwidthType')
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('optionalFields') is not None:
            self.optional_fields = m.get('optionalFields')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class BandwidthVmResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
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


class BandwidthVmResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[BandwidthVmResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthVmResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthVmResponseProviderDateIsp(TeaModel):
    def __init__(
        self,
        ispid: str = None,
        node: str = None,
        peak_time: str = None,
        peak_value: str = None,
    ):
        # {'en':'isp id', 'zh_CN':'isp id'}
        self.ispid = ispid
        # {'en':'node', 'zh_CN':'节点名称'}
        self.node = node
        # {'en':'peakTime', 'zh_CN':'带宽峰值时间'}
        self.peak_time = peak_time
        # {'en':'peakValue', 'zh_CN':'带宽峰值'}
        self.peak_value = peak_value

    def validate(self):
        self.validate_required(self.ispid, 'ispid')
        self.validate_required(self.node, 'node')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ispid is not None:
            result['ispid'] = self.ispid
        if self.node is not None:
            result['node'] = self.node
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ispid') is not None:
            self.ispid = m.get('ispid')
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        return self


class BandwidthVmResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthVmResponseProviderDateChannel = None,
        isp: BandwidthVmResponseProviderDateIsp = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel
        # {'en':'isp', 'zh_CN':'运营商'}
        self.isp = isp

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()
        self.validate_required(self.isp, 'isp')
        if self.isp:
            self.isp.validate()

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
        if self.isp is not None:
            result['isp'] = self.isp.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = BandwidthVmResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        if m.get('isp') is not None:
            temp_model = BandwidthVmResponseProviderDateIsp()
            self.isp = temp_model.from_map(m['isp'])
        return self


class BandwidthVmResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthVmResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'频道带宽数据'}
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
            temp_model = BandwidthVmResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthVmResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthVmResponseProvider = None,
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
            temp_model = BandwidthVmResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthVmPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthVmParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthVmRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthVmResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBandwidthbyISPProvinceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        area_code: List[str] = None,
        domain: List[str] = None,
        province: List[str] = None,
        isp: List[str] = None,
    ):
        # {'en':'Start time', 'zh_CN':'开始时间：
        # &nbsp; 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # &nbsp; 2.不能大于当前时间；
        # &nbsp; 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # The 1. format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. the end time is larger than the start time.
        # 
        # 3. if the end time is greater than the current time, take the current time.
        # 
        # 4. DateFrom and dateTo are not uploaded, default query for the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days (technical support can be contacted to adjust).', 'zh_CN':'结束时间：
        # &nbsp; 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # &nbsp; 2.结束时间需大于开始时间；
        # &nbsp; 3.结束时间如果大于当前时间，取当前时间；
        # &nbsp; 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # &nbsp; 5.允许查询最大间隔：31天，即dateFrom和dateTo相差不能超过31天（可联系技术支持调整）。'}
        self.date_to = date_to
        # {'en':'Data granularity
        # 
        # 1.        fiveminutes:   five minutes, hourly: one hour, daily: one day;
        # 
        # 2.        If   not specified, daily is set as the default value;
        # 
        # 3.        If   fiveminutes is specified as the value, then data is returned in actual   configured granularity when there is specific configuration to data collecting   granularity for the customer.', 'zh_CN':'数据粒度：
        # 1.支持5m（5分钟）
        # 2.不传默认5m。'}
        self.data_interval = data_interval
        # {'en':'area:
        # 
        # 1. Do not pass the default query all areas.
        # 
        # 2. Support to pass multiple regions, the optional values are: cn, hk, ov, apac, am, emea, fg.', 'zh_CN':'区域：
        # 1.不传默认查询全部区域。
        # 2.支持传递多个区域，可选值为：cn、hk、ov、apac、am、emea、fg。'}
        self.area_code = area_code
        # {'en':'domain:
        # 
        # 1. The maximum number of passable domain names is 20 by default (you can contact technical support adjustment).
        # 
        # 2. Query all the domain names under the account when the entry is not passed, but you cannot query (error) when the number of domain names under the account exceeds the limit.', 'zh_CN':'域名：
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整），
        # 2.未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询（报错）。'}
        self.domain = domain
        # {'en':'By default, all provinces are queried, and the provinces are transferred. The province information code table is detailed in the appendix of the overview page.', 'zh_CN':'默认查询全部省份，传递省份，省份信息码表详见概览页附录说明章节'}
        self.province = province
        # {'en':'The default query is for all operators, the operators and operator information codes are detailed in the appendix of the overview page.', 'zh_CN':'默认查询全部运营商，传递运营商，运营商信息码表详见概览页附录说明章节'}
        self.isp = isp

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
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        if self.domain is not None:
            result['domain'] = self.domain
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class QueryBandwidthbyISPProvinceResponseResultBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'Date
        # 
        # 1.        When   the data query granularity is fiveminutes, the format is yyyy-MM-dd HH:mm;   the data value of every time slice represents the data value within the   previous time granularity range. 
        # 2.        Return   the time slice contained in start time and the time slice contained in end   time.', 'zh_CN':'时间
        # 1.查询的数据粒度为5m时，格式为yyyy-MM-dd &nbsp; HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值，比如yyyy-MM-dd 00:05，代表00:00到00:05范围内的数据。
        # 2.返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'The bandwidth value, the corresponding value value of each time slice, shows the cumulative data value represented by this time slice.
        # 
        # 
        # 
        # Unit Mbps, keep 2 decimal digits.', 'zh_CN':'带宽值，每个时间片的对应value值都展示这个时间片代表的完整数据累计值。
        # 单位Mbps，保留2位小数。'}
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


class QueryBandwidthbyISPProvinceResponseResult(TeaModel):
    def __init__(
        self,
        bandwidth_data: List[QueryBandwidthbyISPProvinceResponseResultBandwidthData] = None,
    ):
        self.bandwidth_data = bandwidth_data

    def validate(self):
        self.validate_required(self.bandwidth_data, 'bandwidth_data')
        if self.bandwidth_data:
            for k in self.bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_data is not None:
            result['bandwidthData'] = []
            for k in self.bandwidth_data:
                result['bandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidthData') is not None:
            self.bandwidth_data = []
            for k in m.get('bandwidthData'):
                temp_model = QueryBandwidthbyISPProvinceResponseResultBandwidthData()
                self.bandwidth_data.append(temp_model.from_map(k))
        return self


class QueryBandwidthbyISPProvinceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryBandwidthbyISPProvinceResponseResult] = None,
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
                temp_model = QueryBandwidthbyISPProvinceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryBandwidthbyISPProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthbyISPProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthbyISPProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthbyISPProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthPeakRankingRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        isp: str = None,
        accetype: str = None,
        dataformat: str = None,
        is_exact_match: str = None,
        datatype: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期，日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"1.If there area multiple inputs,use ';' as demimeter.
        # 2.optional values of isp: refers to the ISP-section of appendix.
        # 3. If not specified,means all the isp.", "zh_CN":"&nbsp;要查询的运营商的缩写，多个isp请用英文分号';'分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了'cn'时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp = isp
        # {"en":"acceleration type.
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
        # {"en":"Different data types.
        # 1.optional values:1,2,3.
        # 2.'2' means bandwidth of http.'3' means bandwidth of https.'1' mean the total bandwidth.
        # 3.ISP parameter not supported.", "zh_CN":"datatype=1时，输出总带宽；datatype=2时输出http的带宽；datatype=3时，输出https的带宽。默认datatype=1。当datatype=2或者3时，不支持isp入参。"}
        self.datatype = datatype

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
        if self.isp is not None:
            result['isp'] = self.isp
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.datatype is not None:
            result['datatype'] = self.datatype
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
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        return self


class BandwidthPeakRankingResponseProviderDateChannelPeak(TeaModel):
    def __init__(
        self,
        channel: str = None,
        peak_time: str = None,
        peak_value: str = None,
        total_flow: str = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel
        # {'en':'peakTime', 'zh_CN':'峰值时间'}
        self.peak_time = peak_time
        # {'en':'peakvalue（Mbps）', 'zh_CN':'带宽峰值，单位Mbps'}
        self.peak_value = peak_value
        # {'en':'total traffic,unit GB', 'zh_CN':'总流量，单位GB'}
        self.total_flow = total_flow

    def validate(self):
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.total_flow, 'total_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        return self


class BandwidthPeakRankingResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel_peak: BandwidthPeakRankingResponseProviderDateChannelPeak = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始日期'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束日期'}
        self.enddate = enddate
        # {'en':'channelPeak', 'zh_CN':'频道峰值数据'}
        self.channel_peak = channel_peak

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel_peak, 'channel_peak')
        if self.channel_peak:
            self.channel_peak.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel_peak is not None:
            result['channelPeak'] = self.channel_peak.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channelPeak') is not None:
            temp_model = BandwidthPeakRankingResponseProviderDateChannelPeak()
            self.channel_peak = temp_model.from_map(m['channelPeak'])
        return self


class BandwidthPeakRankingResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthPeakRankingResponseProviderDate = None,
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
            temp_model = BandwidthPeakRankingResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthPeakRankingResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthPeakRankingResponseProvider = None,
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
            temp_model = BandwidthPeakRankingResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthPeakRankingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthPeakRankingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthPeakRankingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthPeakRankingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthEcdnRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        timezone: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        datasource: str = None,
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
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"The option without specifying a value will return all types of data:
        # 1)ecdnBandwidth: will only return ECDN data.
        # 2)cdnBandwidth: will only return CDN details data.
        # 3)cdnPlusEcdnBandwidth: will only return ECDN+CDN details dat.", "zh_CN":"不传返回所有类型数据。ecdnBandwidth：只返回ECDN数据；cdnBandwidth：只返回CDN明细数据；cdnPlusEcdnBandwidth：只返回ECDN+cdn明细数据"}
        self.datasource = datasource

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
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.datasource is not None:
            result['datasource'] = self.datasource
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
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('datasource') is not None:
            self.datasource = m.get('datasource')
        return self


class BandwidthEcdnResponseProviderDateChartDataListData(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'time of every 5 duration,with format yyyy-mmm-dd hh:MM:ss', 'zh_CN':'ecdn带宽5分钟粒度时间，格式yyyy-mm-dd hh:MM:ss'}
        self.time = time
        # {'en':'displaying the Bandwidth(Mbps)', 'zh_CN':'ecdn带宽(Mbps)'}
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


class BandwidthEcdnResponseProviderDateChartDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        data: List[BandwidthEcdnResponseProviderDateChartDataListData] = None,
    ):
        # {'en':'ecdnBandwidth', 'zh_CN':'支持：[ecdnBandwidth],[cdnBandwidth],[cdnPlusEcdnBandwidth] 3种类型带宽数据'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽明细'}
        self.data = data

    def validate(self):
        self.validate_required(self.name, 'name')
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
        if self.name is not None:
            result['name'] = self.name
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = BandwidthEcdnResponseProviderDateChartDataListData()
                self.data.append(temp_model.from_map(k))
        return self


class BandwidthEcdnResponseProviderDate(TeaModel):
    def __init__(
        self,
        chart_data_list: List[BandwidthEcdnResponseProviderDateChartDataList] = None,
    ):
        # {'en':'chartDataList', 'zh_CN':'带宽明细'}
        self.chart_data_list = chart_data_list

    def validate(self):
        self.validate_required(self.chart_data_list, 'chart_data_list')
        if self.chart_data_list:
            for k in self.chart_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_data_list is not None:
            result['chartDataList'] = []
            for k in self.chart_data_list:
                result['chartDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chartDataList') is not None:
            self.chart_data_list = []
            for k in m.get('chartDataList'):
                temp_model = BandwidthEcdnResponseProviderDateChartDataList()
                self.chart_data_list.append(temp_model.from_map(k))
        return self


class BandwidthEcdnResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthEcdnResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'ecdn数据'}
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
            temp_model = BandwidthEcdnResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthEcdnResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthEcdnResponseProvider = None,
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
            temp_model = BandwidthEcdnResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthEcdnPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthEcdnParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthEcdnRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthEcdnResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthLogEcdnRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        timezone: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        datasource: str = None,
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
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"The option without specifying a value will return all types of data:
        # 1)ecdnBandwidth: will only return ECDN data.
        # 2)cdnBandwidth: will only return CDN details data.
        # 3)cdnPlusEcdnBandwidth: will only return ECDN+CDN details dat.", "zh_CN":"不传返回所有类型数据。ecdnBandwidth：只返回ECDN数据；cdnBandwidth：只返回CDN明细数据；cdnPlusEcdnBandwidth：只返回ECDN+cdn明细数据"}
        self.datasource = datasource

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
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.datasource is not None:
            result['datasource'] = self.datasource
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
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('datasource') is not None:
            self.datasource = m.get('datasource')
        return self


class BandwidthLogEcdnResponseProviderDateChartDataListData(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'time of every 5 duration,with format yyyy-mmm-dd hh:MM:ss', 'zh_CN':'ecdn带宽5分钟粒度时间，格式yyyy-mm-dd hh:MM:ss'}
        self.time = time
        # {'en':'displaying the Bandwidth(Mbps)', 'zh_CN':'ecdn带宽(Mbps)'}
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


class BandwidthLogEcdnResponseProviderDateChartDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        data: List[BandwidthLogEcdnResponseProviderDateChartDataListData] = None,
    ):
        # {'en':'ecdnBandwidth', 'zh_CN':'支持：[ecdnBandwidth],[cdnBandwidth],[cdnPlusEcdnBandwidth] 3种类型带宽数据'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽明细'}
        self.data = data

    def validate(self):
        self.validate_required(self.name, 'name')
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
        if self.name is not None:
            result['name'] = self.name
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = BandwidthLogEcdnResponseProviderDateChartDataListData()
                self.data.append(temp_model.from_map(k))
        return self


class BandwidthLogEcdnResponseProviderDate(TeaModel):
    def __init__(
        self,
        chart_data_list: List[BandwidthLogEcdnResponseProviderDateChartDataList] = None,
    ):
        # {'en':'chartDataList', 'zh_CN':'带宽明细'}
        self.chart_data_list = chart_data_list

    def validate(self):
        self.validate_required(self.chart_data_list, 'chart_data_list')
        if self.chart_data_list:
            for k in self.chart_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_data_list is not None:
            result['chartDataList'] = []
            for k in self.chart_data_list:
                result['chartDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chartDataList') is not None:
            self.chart_data_list = []
            for k in m.get('chartDataList'):
                temp_model = BandwidthLogEcdnResponseProviderDateChartDataList()
                self.chart_data_list.append(temp_model.from_map(k))
        return self


class BandwidthLogEcdnResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthLogEcdnResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'ecdn数据'}
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
            temp_model = BandwidthLogEcdnResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthLogEcdnResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthLogEcdnResponseProvider = None,
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
            temp_model = BandwidthLogEcdnResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthLogEcdnPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthLogEcdnParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthLogEcdnRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthLogEcdnResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryIPV6BandwidthOfeachISPandProvinceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        iptype: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 
        # 1.The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00);
        # 2.Cannot be greater than the current time
        # 3.Get up to the last six months (183 days) of data.", "zh_CN":"开始时间:
        # 
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 
        # 2.不能大于当前时间
        # 
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;
        # 3.If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default;
        # 4.Allowable maximum time range for query: 1 day, means the period between dateFrom to dateTo should not exceed 1 day (can be adjusted by contacting technical support up to 31 days)", "zh_CN":"结束时间:
        # 
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常
        # 
        # 4.允许查询最大时间间隔:1天,即dateFrom和dateTo相差不能超过1天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The default upper limit to domains that can be entered is 200 (Contact technical support to adjust);
        # 2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)", "zh_CN":"域名:
        # 
        # 1.可传递域名数量上限默认为200个(可联系技术支持调整);
        # 
        # 2.自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. Support 5m (5 minutes granularity),1h (1 hour granularity)
        # 2. The default value is 5m", "zh_CN":"数据粒度:
        # 
        # 1.支持5m(5分钟)、1h(1小时)
        # 
        # 2.不传默认5m。"}
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
        # {"en":"IP type
        # 1.Optional values:IPV6,IPV4
        # 2.Query all IP type by default.", "zh_CN":"IP类型:
        # 
        # 1.可选值为 IPV6.IPV4
        # 2.不传默认查询全部"}
        self.iptype = iptype
        # {"en":"Group dimension:
        # 1.Default response aggregation data without group
        # 2.Optional values:domain,province,isp,you can pass in single or multiple values
        # 3.The detailed data will be displayed according to the dimension.For example,if the dimension is isp,the detail data will be group by each isp.", "zh_CN":"分组关键词:
        # 1.默认聚合展示;
        # 2.可选值为domain.province.isp,可传入多个值;
        # 3.传入关键词则代表需要按照关键词对应的值展示明细; 例如groupBy传入isp,则isp维度需要明细展示;当没有传递isp,则代表isp聚合展示,同时isp节点则不返回。其他province和domain相同逻辑。 例如:传递'groupBy':   ['domain','province'],则ispData下的isp节点无需返回。 { 'domain': 'www.aaaa.com', 'ispData': [ { 'isp':   '中国电信', 'provinceData': [....] }]}"}
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
        if self.iptype is not None:
            result['IPType'] = self.iptype
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
        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceDataBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time
        # 1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value in the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00.
        # 3. Returns the time slice contained in the start time and end time.", "zh_CN":"时间,
        # 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00;
        # 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Bandwidth,unit is Mbps,Keep 2 decimal places", "zh_CN":"带宽值,单位Mbps,保留2位小数。"}
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


class QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        bandwidth_data: List[QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceDataBandwidthData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.bandwidth_data = bandwidth_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.bandwidth_data, 'bandwidth_data')
        if self.bandwidth_data:
            for k in self.bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.bandwidth_data is not None:
            result['bandwidthData'] = []
            for k in self.bandwidth_data:
                result['bandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('bandwidthData') is not None:
            self.bandwidth_data = []
            for k in m.get('bandwidthData'):
                temp_model = QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceDataBandwidthData()
                self.bandwidth_data.append(temp_model.from_map(k))
        return self


class QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceData] = None,
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
                temp_model = QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class QueryIPV6BandwidthOfeachISPandProvinceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspData] = None,
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
                temp_model = QueryIPV6BandwidthOfeachISPandProvinceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class QueryIPV6BandwidthOfeachISPandProvinceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryIPV6BandwidthOfeachISPandProvinceResponseResult] = None,
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
                temp_model = QueryIPV6BandwidthOfeachISPandProvinceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryIPV6BandwidthOfeachISPandProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6BandwidthOfeachISPandProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6BandwidthOfeachISPandProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6BandwidthOfeachISPandProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportBandwidthRealTimeEdgeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"Start time:
        # 1.Start time: time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (December 2rd, 2016, 10:00 a.m., Beijing Time);
        # 2.Not greater than the current time
        # 3.The most recent half-year (183 days) data can be obtained", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The time format is 2016-12-02T10:00:00+08:00
        # 2.End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3.If both fields of dataFrom and dateTo are left empty, then data in the last 1 hours will be queried by default; if one field is filled and one is left empty, then exception will occur.
        # 4.Maximum time range allowable for query: The default value is 1 hour, that is, the difference between dateFrom and dateTo cannot exceed 1 hour (you can contact technical support to adjust it, the maximum is 31 days).", "zh_CN":"结束时间:
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:默认1小时，即dateFrom和dateTo相差不能超过1小时（可联系技术支持调整，最长31天）。"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The default upper limit of domains that can be entered is 20 (if you want to adjust, please, contact technical support);
        # 2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 3.域名超过上限,报错"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. Support 1m (1 minute granularity),5m (5 minutes granularity)
        # 2. The default value is 1m", "zh_CN":"数据粒度:不传默认1m
        # 1.支持1m(1分钟)、5m(5分钟)"}
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


class ReportBandwidthRealTimeEdgeServiceResponseResultBandwidthData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"The data granularity is 1 minute,the format is yyyy-MM-dd HH:mm", "zh_CN":"数据粒度为1分钟,格式为yyyy-MM-dd HH:mm;"}
        self.timestamp = timestamp
        # {"en":"Edge bandwidth,the unit is Mbps,keep 2 decimal places", "zh_CN":"边缘带宽值,单位Mbps,保留2位小数。"}
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


class ReportBandwidthRealTimeEdgeServiceResponseResult(TeaModel):
    def __init__(
        self,
        peak_value: str = None,
        peak_time: str = None,
        total: str = None,
        bandwidth_data: List[ReportBandwidthRealTimeEdgeServiceResponseResultBandwidthData] = None,
    ):
        # {"en":"Peak Bandwidth,unit is Mbps,example(9811.21Mbps)", "zh_CN":"峰值带宽 Mbps,示例 (931556.21 Mbps)"}
        self.peak_value = peak_value
        # {"en":"Time of peak bandwidth,example(2019-02-13 18:01)", "zh_CN":"峰值时间,示例(2019-02-13 18:01);"}
        self.peak_time = peak_time
        # {"en":"Edge total traffic,example(74099.91MB)", "zh_CN":"边缘总流量,示例 ( 74099.92 MB )"}
        self.total = total
        self.bandwidth_data = bandwidth_data

    def validate(self):
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.total, 'total')
        self.validate_required(self.bandwidth_data, 'bandwidth_data')
        if self.bandwidth_data:
            for k in self.bandwidth_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.total is not None:
            result['total'] = self.total
        if self.bandwidth_data is not None:
            result['bandwidthData'] = []
            for k in self.bandwidth_data:
                result['bandwidthData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('bandwidthData') is not None:
            self.bandwidth_data = []
            for k in m.get('bandwidthData'):
                temp_model = ReportBandwidthRealTimeEdgeServiceResponseResultBandwidthData()
                self.bandwidth_data.append(temp_model.from_map(k))
        return self


class ReportBandwidthRealTimeEdgeServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportBandwidthRealTimeEdgeServiceResponseResult] = None,
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
                temp_model = ReportBandwidthRealTimeEdgeServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportBandwidthRealTimeEdgeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRealTimeEdgeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRealTimeEdgeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthRealTimeEdgeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthMiddleRequest(TeaModel):
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
        result_type: str = None,
        type: str = None,
        father_type: str = None,
        need_flow: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期，日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号“;”，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号“;”分隔开，如查询大陆及亚太区域，参数填写为：“region=cn;apac”。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type:
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号“;”分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":" 频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"Display statistic result in merged or separate way:
        # 1.If specified 1, get the merged result.
        # 2.If  specified 2,get the separate result.
        # 3.If specifed 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":" 结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为“1”。"}
        self.result_type = result_type
        # {"en":"Different data types:
        # 1.optional values: hit,miss.
        # 2.If  there are multiple inputs,use ';' as separator.
        # 3.If not specified,it means the merged value of all types.", "zh_CN":"可选值：hit（hit带宽），miss（miss带宽）。多个以英文分号分隔，不选或为空默认展示合计值。"}
        self.type = type
        # {"en":"Different father types:
        # 1.optional values: stafu,dynfu,all
        # 2.If there are multiple inputs,use ';' as separator.
        # 3.If not specified,it means 'all'.", "zh_CN":"可选值：stafu（静态父），dynfu（动态父），all(全选)；默认all（全选）。"}
        self.father_type = father_type
        # {"en":"Return traffic details, 1: mandatory; 0: optional. The default value is 0.", "zh_CN":"返回流量明细，1：需要；0：不需要。默认为0."}
        self.need_flow = need_flow

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
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.type is not None:
            result['type'] = self.type
        if self.father_type is not None:
            result['fatherType'] = self.father_type
        if self.need_flow is not None:
            result['needFlow'] = self.need_flow
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
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('fatherType') is not None:
            self.father_type = m.get('fatherType')
        if m.get('needFlow') is not None:
            self.need_flow = m.get('needFlow')
        return self


class BandwidthMiddleResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        summary: str = None,
        stafu_hit: str = None,
        dynfu_hit: str = None,
        stafu_miss: str = None,
        dynfu_miss: str = None,
        third_ws: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'summary', 'zh_CN':'带宽合计'}
        self.summary = summary
        # {'en':'stafuHit', 'zh_CN':'静态Hit带宽'}
        self.stafu_hit = stafu_hit
        # {'en':'dynfuHit', 'zh_CN':'动态Hit带宽'}
        self.dynfu_hit = dynfu_hit
        # {'en':'stafuMiss', 'zh_CN':'静态Miss带宽'}
        self.stafu_miss = stafu_miss
        # {'en':'dynfuMiss', 'zh_CN':'动态Miss带宽'}
        self.dynfu_miss = dynfu_miss
        # {'en':'thirdWs', 'zh_CN':'带宽'}
        self.third_ws = third_ws

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.summary, 'summary')
        self.validate_required(self.stafu_hit, 'stafu_hit')
        self.validate_required(self.dynfu_hit, 'dynfu_hit')
        self.validate_required(self.stafu_miss, 'stafu_miss')
        self.validate_required(self.dynfu_miss, 'dynfu_miss')
        self.validate_required(self.third_ws, 'third_ws')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.summary is not None:
            result['summary'] = self.summary
        if self.stafu_hit is not None:
            result['stafuHit'] = self.stafu_hit
        if self.dynfu_hit is not None:
            result['dynfuHit'] = self.dynfu_hit
        if self.stafu_miss is not None:
            result['stafuMiss'] = self.stafu_miss
        if self.dynfu_miss is not None:
            result['dynfuMiss'] = self.dynfu_miss
        if self.third_ws is not None:
            result['thirdWs'] = self.third_ws
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('stafuHit') is not None:
            self.stafu_hit = m.get('stafuHit')
        if m.get('dynfuHit') is not None:
            self.dynfu_hit = m.get('dynfuHit')
        if m.get('stafuMiss') is not None:
            self.stafu_miss = m.get('stafuMiss')
        if m.get('dynfuMiss') is not None:
            self.dynfu_miss = m.get('dynfuMiss')
        if m.get('thirdWs') is not None:
            self.third_ws = m.get('thirdWs')
        return self


class BandwidthMiddleResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[BandwidthMiddleResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'中间缓存带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthMiddleResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthMiddleResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthMiddleResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
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
            temp_model = BandwidthMiddleResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class BandwidthMiddleResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: BandwidthMiddleResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'中间缓存带宽数据'}
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
            temp_model = BandwidthMiddleResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthMiddleResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthMiddleResponseProvider = None,
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
            temp_model = BandwidthMiddleResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthMiddlePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthMiddleParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthMiddleRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthMiddleResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class WsiInfoRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        relateaccount: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        timezone: str = None,
        dataformat: str = None,
        datatype: str = None,
    ):
        # {"en":"cust_en_name of sub-client. When a merged-account wants to view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"rbi mapping account. If there is a pass, use this account to query; if it is empty or not, use w+authentication account to query.", "zh_CN":"rbi映射账号。有传就使用此账号查询；为空或者没传，则使用w+鉴权账号查询。"}
        self.relateaccount = relateaccount
        # {"en":"Specifies the query date: 1.With format yyyy-mm-dd. 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they specify the query date scope. 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'. 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM若没有输入时、分，则时分默认为00:01；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they specify the query date scope. 2.With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'. 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM,若没有输入时、分，则时分默认为24:00；此参数需与startdate参数配合,若存在date参数,则该参数无效"}
        self.enddate = enddate
        # {"en":"domains that been queried: 1.If there are multiple inputs,use ';' as separator. 2.If not specified, it means all the domains of the account .When datatype=0, when querying the average number of domain names, this parameter is invalid.", "zh_CN":"查询的频道，多个频道值请用英文分号“;”，不选或者为空时默认为所查询客户的所有频道。当datatype=0，查询域名数均值的时候，此参数无效。"}
        self.channel = channel
        # {"en":"Greenwich Mean Time Zone, the parameter format GMT+09:00 means East 9th District, GMT-09:00 means West 9th District, if not passed, it defaults to the local time zone (East 8th District). When datatype=0, when querying the average number of domain names, this parameter is invalid.", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）。当datatype=0，查询域名数均值的时候，此参数无效。"}
        self.timezone = timezone
        # {"en":"The response format: 1.optional values:xml, json. 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"3 types. 0: The average number of query domain names; 1: Query bandwidth; 2: The number of query requests. Default query: 0.", "zh_CN":"3种类型。0：查询域名数均值；1：查询带宽；2：查询请求数。默认查询：0。"}
        self.datatype = datatype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.relateaccount is not None:
            result['relateaccount'] = self.relateaccount
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.datatype is not None:
            result['datatype'] = self.datatype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('relateaccount') is not None:
            self.relateaccount = m.get('relateaccount')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        return self


class WsiInfoResponseChannelDetail(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {"en":"time", "zh_CN":"时间点"}
        self.time = time
        # {"en":"The bandwidth value corresponding to the time point, the default unit is Mbps,
        # Return the value of the corresponding unit according to flowUnit", "zh_CN":"时间点对应的带宽值，默认单位Mbps，根据flowUnit返回对应单位的数值"}
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


class WsiInfoResponseChannel(TeaModel):
    def __init__(
        self,
        detail: List[WsiInfoResponseChannelDetail] = None,
    ):
        # {'en':'detail', 'zh_CN':'detail'}
        self.detail = detail

    def validate(self):
        self.validate_required(self.detail, 'detail')
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = []
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = []
            for k in m.get('detail'):
                temp_model = WsiInfoResponseChannelDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class WsiInfoResponse(TeaModel):
    def __init__(
        self,
        peak_time: str = None,
        peak_value: str = None,
        charge_method: str = None,
        charge_value: str = None,
        total_flow: str = None,
        total_hit: str = None,
        channel_avg: str = None,
        channel: WsiInfoResponseChannel = None,
    ):
        # {"en":"peakTime", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"peakvalue(Mbps)", "zh_CN":"带宽峰值（单位Mbps）"}
        self.peak_value = peak_value
        # {"en":"chargeMethod", "zh_CN":"计费方式"}
        self.charge_method = charge_method
        # {"en":"chargeValue", "zh_CN":"计费值"}
        self.charge_value = charge_value
        # {"en":"the total flow(GB)", "zh_CN":"总流量（单位GB）"}
        self.total_flow = total_flow
        # {"en":"the total hits", "zh_CN":"总请求数"}
        self.total_hit = total_hit
        # {"en":"Average number of domain names", "zh_CN":"域名数均值"}
        self.channel_avg = channel_avg
        # {'en':'channel', 'zh_CN':'channel'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.charge_method, 'charge_method')
        self.validate_required(self.charge_value, 'charge_value')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_hit, 'total_hit')
        self.validate_required(self.channel_avg, 'channel_avg')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.charge_method is not None:
            result['chargeMethod'] = self.charge_method
        if self.charge_value is not None:
            result['chargeValue'] = self.charge_value
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_hit is not None:
            result['totalHit'] = self.total_hit
        if self.channel_avg is not None:
            result['channelAvg'] = self.channel_avg
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('chargeMethod') is not None:
            self.charge_method = m.get('chargeMethod')
        if m.get('chargeValue') is not None:
            self.charge_value = m.get('chargeValue')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalHit') is not None:
            self.total_hit = m.get('totalHit')
        if m.get('channelAvg') is not None:
            self.channel_avg = m.get('channelAvg')
        if m.get('channel') is not None:
            temp_model = WsiInfoResponseChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class WsiInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsiInfoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsiInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsiInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportBandwidthWildcardDomainServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        wildcard_domain: List[str] = None,
    ):
        # {"en":"Start time: 
        # 		1. The format is yyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00:00+08:00 (10:00:00 Beijing time on December 2, 2016); 
        # 		2. Can not exceed the current time; 
        # 		3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月02日10点0分0秒)
        #         2.不能大于当前时间
        #         3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time: 
        # 		1. The format is yyyy-MM-ddTHH:mm:ss+08:00; 
        # 		2. The end time is greater than the start time. If the end time is greater than the current time, the current time is taken. 
        # 		3. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception; 
        # 		4. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days.", "zh_CN":"结束时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        #         2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        #         3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        #         4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Wildcard Domain:
        #         1. The upper limit of the number of Wildcard Domain names that can be passed is 20 by default (contact technical support for adjustment);
        #         2. Automatically filter out invalid domain names (if a non-common domain name is passed in, it will be filtered out).
        #         3. If it is not filled, all pan domain names under the account will be queried by default", "zh_CN":"泛域名:
        #         1. 可传递泛域名数量上限默认为20个(可联系技术支持调整);
        #         2. 自动过滤掉无效域名(如传递非泛域名,会被过滤掉)。
        #         3. 如未填,则默认查询此账号下所有泛域名"}
        self.wildcard_domain = wildcard_domain

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
        if self.wildcard_domain is not None:
            result['wildcardDomain'] = self.wildcard_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('wildcardDomain') is not None:
            self.wildcard_domain = m.get('wildcardDomain')
        return self


class ReportBandwidthWildcardDomainServiceResponseDataDomainListBandwidthList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time slice, returns the time slice containing the start time and end time. Time format: yyyy-MM-dd HH:mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。时间格式:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Bandwidth value, unit Mbps, keep 2 decimal places", "zh_CN":"带宽值,单位Mbps,保留2位小数。"}
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


class ReportBandwidthWildcardDomainServiceResponseDataDomainList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        bandwidth_list: List[ReportBandwidthWildcardDomainServiceResponseDataDomainListBandwidthList] = None,
    ):
        # {"en":"domain", "zh_CN":"明细域名"}
        self.domain = domain
        self.bandwidth_list = bandwidth_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.bandwidth_list, 'bandwidth_list')
        if self.bandwidth_list:
            for k in self.bandwidth_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.bandwidth_list is not None:
            result['bandwidthList'] = []
            for k in self.bandwidth_list:
                result['bandwidthList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('bandwidthList') is not None:
            self.bandwidth_list = []
            for k in m.get('bandwidthList'):
                temp_model = ReportBandwidthWildcardDomainServiceResponseDataDomainListBandwidthList()
                self.bandwidth_list.append(temp_model.from_map(k))
        return self


class ReportBandwidthWildcardDomainServiceResponseData(TeaModel):
    def __init__(
        self,
        wildcard_domain: str = None,
        domain_list: List[ReportBandwidthWildcardDomainServiceResponseDataDomainList] = None,
    ):
        # {"en":"wildcard Domain", "zh_CN":"泛域名"}
        self.wildcard_domain = wildcard_domain
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.wildcard_domain, 'wildcard_domain')
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.wildcard_domain is not None:
            result['wildcardDomain'] = self.wildcard_domain
        if self.domain_list is not None:
            result['domainList'] = []
            for k in self.domain_list:
                result['domainList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wildcardDomain') is not None:
            self.wildcard_domain = m.get('wildcardDomain')
        if m.get('domainList') is not None:
            self.domain_list = []
            for k in m.get('domainList'):
                temp_model = ReportBandwidthWildcardDomainServiceResponseDataDomainList()
                self.domain_list.append(temp_model.from_map(k))
        return self


class ReportBandwidthWildcardDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportBandwidthWildcardDomainServiceResponseData] = None,
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
                temp_model = ReportBandwidthWildcardDomainServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportBandwidthWildcardDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthWildcardDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthWildcardDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthWildcardDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainBandwidthDomainList(TeaModel):
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


class QueryDomainBandwidthRequest(TeaModel):
    def __init__(
        self,
        domain_list: QueryDomainBandwidthDomainList = None,
    ):
        # {"en":"Domain list.
        # Domain number limits can be adjusted depending on different accounts. The default value is 20(if you want to adjust,please, contact technical support)", "zh_CN":"域名列表
        # 1.域名个数限制根据账号可调,默认为20个（可联系技术支持下单调整）;"}
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
            temp_model = QueryDomainBandwidthDomainList()
            self.domain_list = temp_model.from_map(m['domain-list'])
        return self


class QueryDomainBandwidthResponseBandwidthReport(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        bandwidth: int = None,
    ):
        # {"en":"Date
        # When the querying data granularity is fiveminutes, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05 AM, and the last one is yyyy-MM-dd 24:00;When the querying data granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is yyyy-MM-dd 24;When the querying data granularity is daily, the format is yyyy-MM-dd; the data value of every time slice represents the value of the daily data;Return the time slice contained in start time and in end time", "zh_CN":"时间
        # 1.查询的数据粒度为fiveminutes时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是yyyy-MM-dd 24:00。
        # 2.查询的数据粒度为hourly时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是yyyy-MM-dd 24。
        # 3.查询的数据粒度为daily时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值;
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Bandwidth, keep the number to four decimal places. Unit: Mbps", "zh_CN":"带宽,保留4位小数,单位为Mbps"}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self


class QueryDomainBandwidthResponse(TeaModel):
    def __init__(
        self,
        bandwidth_report: List[QueryDomainBandwidthResponseBandwidthReport] = None,
    ):
        self.bandwidth_report = bandwidth_report

    def validate(self):
        self.validate_required(self.bandwidth_report, 'bandwidth_report')
        if self.bandwidth_report:
            for k in self.bandwidth_report:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_report is not None:
            result['bandwidthReport'] = []
            for k in self.bandwidth_report:
                result['bandwidthReport'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidthReport') is not None:
            self.bandwidth_report = []
            for k in m.get('bandwidthReport'):
                temp_model = QueryDomainBandwidthResponseBandwidthReport()
                self.bandwidth_report.append(temp_model.from_map(k))
        return self


class QueryDomainBandwidthPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainBandwidthParameters(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        type: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.And smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 31 days", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过31天（可联系技术支持调整）;4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time will be assigned as the value", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Data granularity
        # fiveminutes: five minutes, hourly: one hour, daily: one day;If not specified, daily is set as the default value", "zh_CN":"数据粒度
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


class QueryDomainBandwidthRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainBandwidthResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




