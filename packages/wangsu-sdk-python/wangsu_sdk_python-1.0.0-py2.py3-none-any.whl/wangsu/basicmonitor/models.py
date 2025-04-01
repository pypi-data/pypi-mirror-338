# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportFlowDomainIspProvinceIaasServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        type: List[str] = None,
        group_by: List[str] = None,
    ):
        # {'en':'Starting time:
        # 
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00) );
        # 
        # 2. Cannot be greater than the current time
        # 
        # 3. Get up to the last six months (183 days) of data.', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {"en":"End Time:
        # 
        # 1. Time format 2016-12-02T10:00:00+08:00
        # 
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 
        # 3. dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one untransmitted, throw an exception
        # 
        # 4. Allow query maximum time interval: 7 days, that is, the difference between dateFrom and dateTo can't exceed 7 days (can contact technical support adjustment).", "zh_CN":"结束时间：
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：7天，即dateFrom和dateTo相差不能超过7天（可联系技术支持调整）。"}
        self.date_to = date_to
        # {'en':'domain:
        # 
        # 1. The maximum number of passable domain names is 20 by default (you can contact technical support adjustment). All domain names under the account are not queried when the entry is not passed, but cannot be queried (error) when the number of domain names under the account exceeds the limit.
        # 
        # 2. Automatically filter out illegal domain names (such as passing illegal domain names, they will be filtered out, and the query results only return data of legitimate domain names).', 'zh_CN':'域名：
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）。未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询（报错）。
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。'}
        self.domain = domain
        # {'en':'Data granularity, the default is 5m (5 minutes, currently only supports 5m)', 'zh_CN':'数据粒度，默认为5m（5分钟，当前只支持5m）'}
        self.data_interval = data_interval
        # {'en':'Province
        # 
        # 1.Province is not upload: Query all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.', 'zh_CN':'省份
        # 
        # 1.未传递province时：查询所有省份
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。'}
        self.province = province
        # {'en':'ISP:
        # 1.ISP is not upload: Query all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.', 'zh_CN':'运营商：
        # 1.未传递isp时：查询所有isp；
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节'}
        self.isp = isp
        # {'en':'Traffic type:
        # 
        # 1. Passable value range: trafficOut (outflow), trafficIn (inflow)
        # 
        # 2. Multiple deliverables, no default outgoing, and merged traffic when multiple passes.', 'zh_CN':'流量类型：
        # 1.可传递值范围：trafficOut（流出）、trafficIn（流入）
        # 2.可传递多个，不传默认流出，传递多个时返回合并流量。'}
        self.type = type
        # {"en":"Grouping dimensions:
        # 
        # 1. The optional values are domain,province, and isp, which can pass in single or multiple values.
        # 
        # 2. If there is an incoming, the detailed data will be displayed according to the dimension;
        # 
        # 3. The result hierarchy is fixed in order, and the order of the parameters does not affect the order of the returned results. For example: 'groupBy': ['domain','province'] is the same as 'groupBy': ['province', 'domain'].
        # 
        # For example: pass 'groupBy': ['domain', 'province'], then the isp node under ispData does not need to return.", "zh_CN":"分组维度：
        # 1.可选值为domain、province、isp，可传入单个或多个值；
        # 2.有传入则按照该维度展示明细数据；
        # 3.返回结果层级顺序固定，入参顺序不影响返回结果顺序。例如：'groupBy': ['domain','province']与'groupBy': ['province','domain']返回结果一样。
        # 例如：传递'groupBy': ['domain','province']，则ispData下的isp节点无需返回。"}
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
        if self.type is not None:
            result['type'] = self.type
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
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceDataFlowData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'time
        # 1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value in the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00.
        # 2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00.
        # 3. Returns the time slice contained in the start time and end time.', 'zh_CN':'时间
        # 1.查询的数据粒度为5m时，格式为yyyy-MM-dd &nbsp; HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd &nbsp; 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00。
        # 2.查询的数据粒度为1h时，格式为yyyy-MM-dd &nbsp; HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） &nbsp; 00。
        # 3.返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'The value of the flow, the unit is MB, and the two decimal digits are retained', 'zh_CN':'流量值，单位为MB，保留两位小数'}
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


class ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        flow_data: List[ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceDataFlowData] = None,
    ):
        # {'en':'Chinese name of the province', 'zh_CN':'省份中文名称'}
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
                temp_model = ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceDataFlowData()
                self.flow_data.append(temp_model.from_map(k))
        return self


class ReportFlowDomainIspProvinceIaasServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceData] = None,
    ):
        # {'en':'Service provider&rsquo;s Chinese name', 'zh_CN':'运营商中文名称'}
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
                temp_model = ReportFlowDomainIspProvinceIaasServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportFlowDomainIspProvinceIaasServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportFlowDomainIspProvinceIaasServiceResponseResultIspData] = None,
    ):
        # {'en':'domain', 'zh_CN':'域名'}
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
                temp_model = ReportFlowDomainIspProvinceIaasServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportFlowDomainIspProvinceIaasServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportFlowDomainIspProvinceIaasServiceResponseResult] = None,
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
                temp_model = ReportFlowDomainIspProvinceIaasServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportFlowDomainIspProvinceIaasServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainIspProvinceIaasServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainIspProvinceIaasServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowDomainIspProvinceIaasServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQueryServerMetricRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryServerMetricBandwidth(TeaModel):
    def __init__(
        self,
        stat_time: str = None,
        out: str = None,
        in_: str = None,
        ext_in: str = None,
        ext_out: str = None,
    ):
        # {"en":"The bandwidth collection time, formatted as YYYYMMDDHHMM, is 5 minutes granularity", "zh_CN":"带宽采集时间，格式yyyyMMddHHmm，为5分钟粒度"}
        self.stat_time = stat_time
        # {"en":"Total outflow bandwidth (including intra-node flow) in Mbps", "zh_CN":"总流出带宽（含节点内流量），单位Mbps"}
        self.out = out
        # {"en":"Total inflow bandwidth (including intra-node traffic) in Mbps", "zh_CN":"总流入带宽（含节点内流量），单位Mbps"}
        self.in_ = in_
        # {"en":"Inflow bandwidth of external network (not including intra-node traffic), unit of Mbps", "zh_CN":"外网流入带宽（不含节点内流量），单位Mbps"}
        self.ext_in = ext_in
        # {"en":"Outflow bandwidth of the external network (excluding intra-node traffic), unit of Mbps", "zh_CN":"外网流出带宽（不含节点内流量），单位Mbps"}
        self.ext_out = ext_out

    def validate(self):
        self.validate_required(self.stat_time, 'stat_time')
        self.validate_required(self.out, 'out')
        self.validate_required(self.in_, 'in_')
        self.validate_required(self.ext_in, 'ext_in')
        self.validate_required(self.ext_out, 'ext_out')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.out is not None:
            result['out'] = self.out
        if self.in_ is not None:
            result['in'] = self.in_
        if self.ext_in is not None:
            result['extIn'] = self.ext_in
        if self.ext_out is not None:
            result['extOut'] = self.ext_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('out') is not None:
            self.out = m.get('out')
        if m.get('in') is not None:
            self.in_ = m.get('in')
        if m.get('extIn') is not None:
            self.ext_in = m.get('extIn')
        if m.get('extOut') is not None:
            self.ext_out = m.get('extOut')
        return self


class VMPQueryServerMetricMem(TeaModel):
    def __init__(
        self,
        stat_time: str = None,
        used: str = None,
        total: str = None,
    ):
        # {"en":"The memory data collection time, in the format YYYYMMDDHHMM, is 5 minutes granularity", "zh_CN":"内存数据采集时间，格式yyyyMMddHHmm，为5分钟粒度"}
        self.stat_time = stat_time
        # {"en":"Memory usage in MB", "zh_CN":"内存使用量，单位为MB"}
        self.used = used
        # {"en":"Total memory, in MB", "zh_CN":"总内存量，单位为MB"}
        self.total = total

    def validate(self):
        self.validate_required(self.stat_time, 'stat_time')
        self.validate_required(self.used, 'used')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.used is not None:
            result['used'] = self.used
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('used') is not None:
            self.used = m.get('used')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class VMPQueryServerMetricCpu(TeaModel):
    def __init__(
        self,
        stat_time: str = None,
        usage: str = None,
    ):
        # {"en":"CPU usage collection time in the format YYYYMMDDHHMM, with a granularity of 5 minutes", "zh_CN":"cpu使用率采集时间，格式yyyyMMddHHmm，为5分钟粒度"}
        self.stat_time = stat_time
        # {"en":"CPU utilization, with a value of 0-1, such as 0.25, represents 25% utilization", "zh_CN":"cpu使用率，取值0-1，如0.25，该值则表示使用率为25%"}
        self.usage = usage

    def validate(self):
        self.validate_required(self.stat_time, 'stat_time')
        self.validate_required(self.usage, 'usage')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.usage is not None:
            result['usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        return self


class VMPQueryServerMetricServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_ip: str = None,
        bandwidths: List[VMPQueryServerMetricBandwidth] = None,
        mems: List[VMPQueryServerMetricMem] = None,
        cpus: List[VMPQueryServerMetricCpu] = None,
    ):
        # {"en":"instance id", "zh_CN":"实例唯一标识"}
        self.id = id
        # {"en":"instance ip", "zh_CN":"实例公网IP"}
        self.instance_ip = instance_ip
        # {"en":"VMPQueryServerMetricBandwidth information", "zh_CN":"带宽信息"}
        self.bandwidths = bandwidths
        # {"en":"Memory information", "zh_CN":"内存信息"}
        self.mems = mems
        # {"en":"CPU information", "zh_CN":"CPU信息"}
        self.cpus = cpus

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.instance_ip, 'instance_ip')
        self.validate_required(self.bandwidths, 'bandwidths')
        if self.bandwidths:
            for k in self.bandwidths:
                if k:
                    k.validate()
        self.validate_required(self.mems, 'mems')
        if self.mems:
            for k in self.mems:
                if k:
                    k.validate()
        self.validate_required(self.cpus, 'cpus')
        if self.cpus:
            for k in self.cpus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.instance_ip is not None:
            result['instanceIp'] = self.instance_ip
        if self.bandwidths is not None:
            result['bandwidths'] = []
            for k in self.bandwidths:
                result['bandwidths'].append(k.to_map() if k else None)
        if self.mems is not None:
            result['mems'] = []
            for k in self.mems:
                result['mems'].append(k.to_map() if k else None)
        if self.cpus is not None:
            result['cpus'] = []
            for k in self.cpus:
                result['cpus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceIp') is not None:
            self.instance_ip = m.get('instanceIp')
        if m.get('bandwidths') is not None:
            self.bandwidths = []
            for k in m.get('bandwidths'):
                temp_model = VMPQueryServerMetricBandwidth()
                self.bandwidths.append(temp_model.from_map(k))
        if m.get('mems') is not None:
            self.mems = []
            for k in m.get('mems'):
                temp_model = VMPQueryServerMetricMem()
                self.mems.append(temp_model.from_map(k))
        if m.get('cpus') is not None:
            self.cpus = []
            for k in m.get('cpus'):
                temp_model = VMPQueryServerMetricCpu()
                self.cpus.append(temp_model.from_map(k))
        return self


class VMPQueryServerMetricResponse(TeaModel):
    def __init__(
        self,
        servers: List[VMPQueryServerMetricServer] = None,
    ):
        # {"en":"Instance information array", "zh_CN":"实例信息数组"}
        self.servers = servers

    def validate(self):
        self.validate_required(self.servers, 'servers')
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servers is not None:
            result['servers'] = []
            for k in self.servers:
                result['servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = []
            for k in m.get('servers'):
                temp_model = VMPQueryServerMetricServer()
                self.servers.append(temp_model.from_map(k))
        return self


class VMPQueryServerMetricPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryServerMetricParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        type: str = None,
        stat_time: str = None,
        carrier: str = None,
    ):
        # {"en":"The ID of the virtual machine to query. At most 30 queries can be made at a time, ids 
        #  are separated by character  ','", "zh_CN":"云主机ID。单次最多查询 20 条 ID，ID 之间用半角逗号字符','隔开。"}
        self.ids = ids
        # {"en":"Monitoring data type of query, value:
        # CPU: CPU utilization
        # VMPQueryServerMetricMem: memory
        # VMPQueryServerMetricBandwidth: Traffic data", "zh_CN":"查询的监控数据类型，取值：
        # cpu： cpu使用率
        # mem：内存
        # bandwidth：流量数据"}
        self.type = type
        # {"en":"Query time range in format: yyyymmddhhmm-yyyymmddhhmm
        # Query data for nearly 90 days, a single query no more than 3 days.
        # For example: 202001201730-202001201930 means to query 2020-01-20 17:30 to 19:30 monitoring data.", "zh_CN":"查询时间范围，格式：yyyyMMddHHmm- yyyyMMddHHmm
        # 查询近90天的数据，单次查询不超过10天。
        # 例如：202001201730-202001201930表示查询2020-01-20 17:30到19:30的监控数据。"}
        self.stat_time = stat_time
        # {"en":"The ISP code  ", "zh_CN":"当查询流量数据时可填。实例所属运营商：dx-电信；wt-网通；yd-移动。一次仅允许传入一个运营商参数"}
        self.carrier = carrier

    def validate(self):
        self.validate_required(self.ids, 'ids')
        self.validate_required(self.type, 'type')
        self.validate_required(self.stat_time, 'stat_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.type is not None:
            result['type'] = self.type
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.carrier is not None:
            result['carrier'] = self.carrier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        return self


class VMPQueryServerMetricRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryServerMetricResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




