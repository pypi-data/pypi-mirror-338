# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportVisitorCustomTopDailyServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        top: str = None,
        order_by: str = None,
    ):
        # {"en":"Start time:
        # The time format is yyyy-MM-dd, for example, 2021-10-10;
        # It cannot be greater than the current time
        # You can get data for the last three months (90 days) at most.", "zh_CN":"开始时间：
        # 时间格式为yyyy-MM-dd，例如，2021-10-10；
        # 不能大于当前时间
        # 最多可获取最近三个月（90天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-dd, the end time must be greater than the start time. If the end time is greater than the current time, the current time is used.
        # 2. If both dateFrom and dateTo are not transmitted, the default query is the past 7 days. If only one is not transmitted, an exception is thrown;
        # 3. The maximum query time interval allowed is 31 days, that is, the difference between dateFrom and dateTo cannot exceed 31 days (you can contact technical support to adjust)", "zh_CN":"结束时间：
        # 时间格式为yyyy-MM-dd
        # 结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # dateFrom，dateTo二者都未传，默认查询过去的7天；如仅有一个未传，抛异常
        # 允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天（可联系技术支持调整）。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The upper limit of the number of domain names that can be passed is 100 by default (you can contact technical support to adjust it);
        # 2. Automatically filter out illegal domain names (if an illegal domain name is passed, it will be filtered out, and the query result will only return data for legal domain names);
        # 3. When this parameter is not passed, all domain names under the account will be queried by default, but an error will be prompted when the number of domain names under the account exceeds the upper limit.", "zh_CN":"域名：
        # 可传递域名数量上限默认为100个（可联系技术支持调整）。
        # 自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        # 未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"Number of TOPs:
        # 1. If not specified, the default is TOP 10;
        # 2. The maximum number of TOPs is 100.", "zh_CN":"TOP个数：
        # 不传默认TOP 10
        # 最大TOP 100"}
        self.top = top
        # {"en":"Sorting:
        # 1. Optional values: request, flow
        # 2. Do not pass the default request", "zh_CN":"排序：
        # 1、可选值为：request, flow
        # 2、不传默认request"}
        self.order_by = order_by

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
        if self.top is not None:
            result['top'] = self.top
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self


class ReportVisitorCustomTopDailyServiceData(TeaModel):
    def __init__(
        self,
        top: str = None,
        ip: str = None,
        total_flow: str = None,
        total_request: str = None,
    ):
        # {"en":"Top", "zh_CN":"top排名"}
        self.top = top
        # {"en":"IP", "zh_CN":"ip"}
        self.ip = ip
        # {"en":"Total traffic: The unit of measurement is MB, with 2 decimal places.", "zh_CN":"总流量：计量单位MB，保留2位小数"}
        self.total_flow = total_flow
        # {"en":"Total requests", "zh_CN":"总请求数"}
        self.total_request = total_request

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_request, 'total_request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.ip is not None:
            result['ip'] = self.ip
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        return self


class ReportVisitorCustomTopDailyServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportVisitorCustomTopDailyServiceData] = None,
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
                temp_model = ReportVisitorCustomTopDailyServiceData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportVisitorCustomTopDailyServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportVisitorCustomTopDailyServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportVisitorCustomTopDailyServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportVisitorCustomTopDailyServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUvIspProvinceServiceRequest(TeaModel):
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
        #         1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        #         2. Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        #         3. Period between dataFrom and dateTo cannot be longer than 183 days;", "zh_CN":"开始时间:
        #         1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        #         2.不能大于当前时间;
        #         3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        #         1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        #         2. the end time is larger than the start time.
        #         3. if the end time is greater than the current time, take the current time.
        #         4. DateFrom and dateTo are not uploaded, default query for the past 24 hours; if only one is not uploaded, throw an exception;
        #         5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (technical support can be contacted to adjust). ", "zh_CN":"结束时间:
        #         1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        #         2.结束时间需大于开始时间;
        #         3.结束时间如果大于当前时间,取当前时间;
        #         4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        #         5.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名:可传递域名数量上限默认为20个(可联系技术支持调整),未传递该入参时查询账号下所有域名,但当账号下域名数量超过限制时不可查询(报错)。"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5-minute granularity", "zh_CN":"数据粒度,5m:5分钟粒度"}
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
        #         1. Options are domain, province, isp, and more than one value can be entered;
        #         2. The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        #         1.可选值为domain、province、isp,可传入多个值;
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


class ReportUvIspProvinceServiceResponseResultIspDataProvinceDataUvData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Date
        #         1. When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        #         2. When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        #         3. Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间
        #         1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        #         2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00;
        #         3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests from unique IP addresses", "zh_CN":"独立IP数"}
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


class ReportUvIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        uv_data: List[ReportUvIspProvinceServiceResponseResultIspDataProvinceDataUvData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"Number of requests from unique IP addresses", "zh_CN":"独立IP数"}
        self.uv_data = uv_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.uv_data, 'uv_data')
        if self.uv_data:
            for k in self.uv_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.uv_data is not None:
            result['uvData'] = []
            for k in self.uv_data:
                result['uvData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('uvData') is not None:
            self.uv_data = []
            for k in m.get('uvData'):
                temp_model = ReportUvIspProvinceServiceResponseResultIspDataProvinceDataUvData()
                self.uv_data.append(temp_model.from_map(k))
        return self


class ReportUvIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportUvIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"Internet service providers", "zh_CN":"运营商"}
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
                temp_model = ReportUvIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportUvIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportUvIspProvinceServiceResponseResultIspData] = None,
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
                temp_model = ReportUvIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportUvIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportUvIspProvinceServiceResponseResult] = None,
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
                temp_model = ReportUvIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportUvIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUvIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUvIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUvIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportIpTopDetailsServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        order_by: str = None,
    ):
        # {"en":"Start date:
        #         1.The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        #         2.Cannot be greater than the current time
        #         3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间：
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒);
        #         2.不能大于当前时间
        #         3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        #         1.The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        #         2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        #         3.Date from, dateTo, neither passed, default query past 24 hours; If there is only one unsent, throw an exception
        #         4.The default query interval is 7 days, maximum allowed query time interval: 31 days, i.e., the difference between Date from and dateTo cannot exceed 31 days (adjusted by contact technology support).", "zh_CN":"结束时间：
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒);
        #         2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        #         3.dateFrom，dateTo二者都未传，默认查询过去的24小时;如仅有一个未传，抛异常
        #         4.默认查询时间间隔7天，允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain name:
        #         1.The maximum number of TLDs that can be delivered is 20 by default (Technical Support Adjustments can be contacted).
        #         2.Auto-filter illegal domain name (pass illegal domain name, will be filtered, query result only returns the data of legal domain name)
        #         3.All domain names are queried by default when this entry is not delivered, but an error occurs when the number of domain names in the account exceeds the upper limit", "zh_CN":"域名：
        #         1.可传递域名数量上限默认为20个(可联系技术支持调整)。
        #         2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        #         3.未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"Ordering:
        #         1.Optional values are: bandwidth, request, flow
        #         2.No default bandwidth", "zh_CN":"排序：
        #         1.可选值为：bandwidth 、request、flow
        #         2.不传默认 bandwidth"}
        self.order_by = order_by

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
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self


class ReportIpTopDetailsServiceResponseDataDomainDataIpData(TeaModel):
    def __init__(
        self,
        ip: str = None,
        value: str = None,
    ):
        # {"en":"Ip, default TOP 100", "zh_CN":"ip，默认 TOP 100"}
        self.ip = ip
        # {"en":"
        # 		1.Flow: Unit of measure MB, keeping 2 decimal places
        #         2.Bandwidth: Unit of measure Mbps, keeping 2 decimal places
        #         3.Request", "zh_CN":"
        # 		1.流量：计量单位MB，保留2位小数
        #         2.带宽：计量单位Mbps，保留2位小数
        #         3.请求数"}
        self.value = value

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportIpTopDetailsServiceResponseDataDomainData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ip_data: List[ReportIpTopDetailsServiceResponseDataDomainDataIpData] = None,
    ):
        # {"en":"Domain name", "zh_CN":"域名"}
        self.domain = domain
        self.ip_data = ip_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.ip_data, 'ip_data')
        if self.ip_data:
            for k in self.ip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.ip_data is not None:
            result['ipData'] = []
            for k in self.ip_data:
                result['ipData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ipData') is not None:
            self.ip_data = []
            for k in m.get('ipData'):
                temp_model = ReportIpTopDetailsServiceResponseDataDomainDataIpData()
                self.ip_data.append(temp_model.from_map(k))
        return self


class ReportIpTopDetailsServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        domain_data: List[ReportIpTopDetailsServiceResponseDataDomainData] = None,
    ):
        # {"en":"timestamp:
        #         The format is yyyy-MM-dd HH:MM:ss; Each time slice data value represents the data value in the previous time-granularity range, such as yyyy-MM-dd 00:05, Data in the range 00:00:00 to 00:05.", "zh_CN":"timestamp"}
        self.timestamp = timestamp
        # {"en":"domainData", "zh_CN":"域名数据"}
        self.domain_data = domain_data

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.domain_data, 'domain_data')
        if self.domain_data:
            for k in self.domain_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.domain_data is not None:
            result['domainData'] = []
            for k in self.domain_data:
                result['domainData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('domainData') is not None:
            self.domain_data = []
            for k in m.get('domainData'):
                temp_model = ReportIpTopDetailsServiceResponseDataDomainData()
                self.domain_data.append(temp_model.from_map(k))
        return self


class ReportIpTopDetailsServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportIpTopDetailsServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request Result Information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the requests", "zh_CN":"请求结果的详细数据"}
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
                temp_model = ReportIpTopDetailsServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportIpTopDetailsServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIpTopDetailsServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIpTopDetailsServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportIpTopDetailsServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportReferrerTopDetailsServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        order_by: str = None,
    ):
        # {"en":"Start date:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # 2.Cannot be greater than the current time
        # 3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒)；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3.Date from, dateTo, neither passed, default query past 24 hours; If there is only one unsent, throw an exception
        # 4.Maximum allowed query time interval: 31 days, i.e., the difference between Date from and dateTo cannot exceed 31 days (adjusted by contact technology support).", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒)；
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔:31天，即dateFrom和dateTo相差不能超过31天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1.The maximum number of TLDs that can be delivered is 20 by default (Technical Support Adjustments can be contacted).
        # 2.Auto-filter illegal domain name (pass illegal domain name, will be filtered, query result only returns the data of legal domain name)
        # 3.All domain names are queried by default when this entry is not delivered, but an error occurs when the number of domain names in the account exceeds the upper limit", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)。
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        # 3.未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"Ordering:
        # 1.Optional values are: bandwidth, request, flow
        # 2.No default bandwidth", "zh_CN":"排序:
        # 1.可选值为:bandwidth 、request、flow
        # 2.不传默认 bandwidth"}
        self.order_by = order_by

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
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self


class ReportReferrerTopDetailsServiceResponseDataDomainDataReferData(TeaModel):
    def __init__(
        self,
        refer: str = None,
        value: str = None,
    ):
        # {"en":"Refer, default TOP 100", "zh_CN":"refer，默认 TOP 100"}
        self.refer = refer
        # {"en":"
        # 									  1.Flow: Unit of measure MB, keeping 2 decimal places
        #                                       2.Bandwidth: Unit of measure Mbps, keeping 2 decimal places
        #                                       3.Request", "zh_CN":"
        # 									  1.流量:计量单位MB，保留2位小数
        #                                       2.带宽:计量单位Mbps，保留2位小数
        #                                       3.请求数"}
        self.value = value

    def validate(self):
        self.validate_required(self.refer, 'refer')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refer is not None:
            result['refer'] = self.refer
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('refer') is not None:
            self.refer = m.get('refer')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportReferrerTopDetailsServiceResponseDataDomainData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        refer_data: List[ReportReferrerTopDetailsServiceResponseDataDomainDataReferData] = None,
    ):
        # {"en":"Domain name", "zh_CN":"域名"}
        self.domain = domain
        self.refer_data = refer_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.refer_data, 'refer_data')
        if self.refer_data:
            for k in self.refer_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.refer_data is not None:
            result['referData'] = []
            for k in self.refer_data:
                result['referData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('referData') is not None:
            self.refer_data = []
            for k in m.get('referData'):
                temp_model = ReportReferrerTopDetailsServiceResponseDataDomainDataReferData()
                self.refer_data.append(temp_model.from_map(k))
        return self


class ReportReferrerTopDetailsServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        domain_data: List[ReportReferrerTopDetailsServiceResponseDataDomainData] = None,
    ):
        # {"en":"timestamp:
        # The format is yyyy-MM-dd HH:MM:ss; Each time slice data value represents the data value in the previous time-granularity range, such as yyyy-MM-dd 00:05, Data in the range 00:00:00 to 00:05.", "zh_CN":"timestamp"}
        self.timestamp = timestamp
        self.domain_data = domain_data

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.domain_data, 'domain_data')
        if self.domain_data:
            for k in self.domain_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.domain_data is not None:
            result['domainData'] = []
            for k in self.domain_data:
                result['domainData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('domainData') is not None:
            self.domain_data = []
            for k in m.get('domainData'):
                temp_model = ReportReferrerTopDetailsServiceResponseDataDomainData()
                self.domain_data.append(temp_model.from_map(k))
        return self


class ReportReferrerTopDetailsServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportReferrerTopDetailsServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request Result Information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on results of requests", "zh_CN":"请求结果的详细数据"}
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
                temp_model = ReportReferrerTopDetailsServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportReferrerTopDetailsServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportReferrerTopDetailsServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportReferrerTopDetailsServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportReferrerTopDetailsServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUrlTopDetailsServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        order_by: str = None,
    ):
        # {"en":"Start date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # 2. Cannot be greater than the current time
        # 3. The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒)；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3. Date from, dateTo, neither passed, default query past 24 hours; If there is only one unsent, throw an exception
        # 4. Maximum allowed query time interval: 7 days, i.e., the difference between Date from and dateTo cannot exceed 7 days (adjusted by contact technology support, the maximum interval is 31 days).", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年1月1日10点0分0秒)；
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时；如仅有一个未传,抛异常
        # 4.默认最大查询时间间隔:7天，即dateFrom和dateTo相差不能超过7天(可联系技术支持调整，最大间隔31天)。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The maximum number of TLDs that can be delivered is 20 by default (Technical Support Adjustments can be contacted).
        # 2. Auto-filter illegal domain name (pass illegal domain name, will be filtered, query result only returns the data of legal domain name)
        # 3. All domain names are queried by default when this entry is not delivered, but an error occurs when the number of domain names in the account exceeds the upper limit", "zh_CN":"域名:
        # 
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)。
        # 2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 3.未传递该入参时,默认查询账号下所有域名,但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"Ordering:
        # 1. Optional values are: bandwidth, request, flow
        # 2. No default bandwidth", "zh_CN":"排序:
        # 1.可选值为:bandwidth 、request、flow
        # 2.不传默认 bandwidth"}
        self.order_by = order_by

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
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self


class ReportUrlTopDetailsServiceResponseDataDomainDataUrlData(TeaModel):
    def __init__(
        self,
        url: str = None,
        value: str = None,
    ):
        # {"en":"URL, default TOP 100", "zh_CN":"url,默认 TOP 100"}
        self.url = url
        # {"en":"1. Flow: Unit of measure MB, keeping 2 decimal places;
        # 									2. Bandwidth: Unit of measure Mbps, keeping 2 decimal places;
        # 									3. Request", "zh_CN":"1.流量:计量单位MB,保留2位小数; 
        # 									2.带宽:计量单位Mbps,保留2位小数
        # 									3.请求数"}
        self.value = value

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportUrlTopDetailsServiceResponseDataDomainData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        url_data: List[ReportUrlTopDetailsServiceResponseDataDomainDataUrlData] = None,
    ):
        # {"en":"Domain name", "zh_CN":"域名"}
        self.domain = domain
        self.url_data = url_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.url_data, 'url_data')
        if self.url_data:
            for k in self.url_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.url_data is not None:
            result['urlData'] = []
            for k in self.url_data:
                result['urlData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('urlData') is not None:
            self.url_data = []
            for k in m.get('urlData'):
                temp_model = ReportUrlTopDetailsServiceResponseDataDomainDataUrlData()
                self.url_data.append(temp_model.from_map(k))
        return self


class ReportUrlTopDetailsServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        domain_data: List[ReportUrlTopDetailsServiceResponseDataDomainData] = None,
    ):
        # {"en":"timestamp
        # 1. the format is yyyy-MM-dd HH:MM:ss; Each time slice data value represents the data value in the previous time-granularity range, such as yyyy-MM-dd 00:05, Data in the range 00:00:00 to 00:05.", "zh_CN":"timestamp"}
        self.timestamp = timestamp
        self.domain_data = domain_data

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.domain_data, 'domain_data')
        if self.domain_data:
            for k in self.domain_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.domain_data is not None:
            result['domainData'] = []
            for k in self.domain_data:
                result['domainData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('domainData') is not None:
            self.domain_data = []
            for k in m.get('domainData'):
                temp_model = ReportUrlTopDetailsServiceResponseDataDomainData()
                self.domain_data.append(temp_model.from_map(k))
        return self


class ReportUrlTopDetailsServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportUrlTopDetailsServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request Result Information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on results of requests", "zh_CN":"请求结果的详细数据"}
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
                temp_model = ReportUrlTopDetailsServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportUrlTopDetailsServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlTopDetailsServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlTopDetailsServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlTopDetailsServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTotalNumberofUniqueIPUnderSingleDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream: str = None,
    ):
        # {"en":"Domain, maximum number is 1", "zh_CN":"域名，数量上限1个"}
        self.domain = domain
        # {"en":"Stream name:
        # 1. Limit to the number of streams can be adjusted depending on different accounts. The default value is 20;
        # 2. All streams are queried by default is this field is left empty and at the same time, the upper limit of the number of streams can be set.", "zh_CN":"流名：
        # 1.流名个数限制根据账号可调，默认为20个；
        # 2.不传时默认查询域名下所有流名，同时受流名数量上限限制；"}
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


class QueryTotalNumberofUniqueIPUnderSingleDomainResponseResultDetails(TeaModel):
    def __init__(
        self,
        stream: str = None,
        timestamp: str = None,
        total: int = None,
    ):
        # {"en":"Stream name", "zh_CN":"流名"}
        self.stream = stream
        # {"en":"Time, format is yyyy-MM-dd", "zh_CN":"时间，格式为yyyy-MM-dd"}
        self.timestamp = timestamp
        # {"en":"Number of unique IP addresses", "zh_CN":"独立IP数"}
        self.total = total

    def validate(self):
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[QueryTotalNumberofUniqueIPUnderSingleDomainResponseResultDetails] = None,
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
                temp_model = QueryTotalNumberofUniqueIPUnderSingleDomainResponseResultDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryTotalNumberofUniqueIPUnderSingleDomainResponseResult] = None,
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
                temp_model = QueryTotalNumberofUniqueIPUnderSingleDomainResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainParameters(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
    ):
        # {"en":"Start time
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. Must be smaller than the current time and dateTo;
        # 3. Period between dataFrom and dateTo cannot be longer than 3 days(technical support can be contacted to adjust);
        # 4. You can only query data for the last 2 years.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过3天（可联系技术支持调整）；
        # 4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. Must be greater than dateFrom;
        # 3. The query range must include 00:00:00 of a certain day to query the data of that day. For example, if the query range includes 2017-11-07 00:00:00, the data of 2017-11-07 can be queried.", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；
        # 3.查询范围必须包含某一天的00:00:00，才能查询到当天数据，例如查询范围包含 2017-11-07 00:00:00 可以查询到2017-11-07当天数据。"}
        self.date_to = date_to

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTotalNumberofUniqueIPUnderSingleDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




