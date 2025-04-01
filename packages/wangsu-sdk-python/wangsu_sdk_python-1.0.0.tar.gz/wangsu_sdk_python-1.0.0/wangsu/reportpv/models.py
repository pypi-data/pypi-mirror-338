# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportDomainPvServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. Time format is yyyy-MM-dd,
        # 2. No bigger than the current time.
        # 3. Data in the last 2 years at most can be queried.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-dd
        # 2.不能大于当前时间
        # 3.最多可获取最近2年内数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-dd
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 1day will be queried by default; if only one field is filled in and one is left empty, then exception will be occur.
        # 4. Allowable maximum time range for query: 31days, means the period between dateFrom to dateTo should not exceed 31days (can be adjusted by contacting technical support).", "zh_CN":"结束时间:
        # 
        # 1.时间格式yyyy-MM-dd
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1天;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔31天:,即dateFrom和dateTo相差不能超过31天。（可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1. The maximum number of domain is 20 by default (you can contact technical support for adjustment);
        # 2. Automatically filter out invalid domain (an illegal domain will be filtered, and the query result will only return the data of valid domains).", "zh_CN":"域名:
        # 
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）;
        # 2.自动过滤掉无效域名（如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据）。"}
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


class ReportDomainPvServiceResponseDateDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"timestamp, format is  yyyy-MM-dd HH:mm:ss, the first point of one day is yyyy-MM-dd 01:00:00, the last point of one day is yyyy-MM-dd 24:00:00,", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm:ss,每一个时间片数据值代表的是前一个时间粒度范围内的数据值,一天开始的时间片是yyyy-MM-dd 01:00:00,最后一个时间片是yyyy-MM-dd 24:00:00。"}
        self.timestamp = timestamp
        # {"en":"PV count", "zh_CN":"PV数"}
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


class ReportDomainPvServiceResponseDate(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportDomainPvServiceResponseDateDetailList] = None,
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
                temp_model = ReportDomainPvServiceResponseDateDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportDomainPvServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        date: List[ReportDomainPvServiceResponseDate] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        self.date = date

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.date, 'date')
        if self.date:
            for k in self.date:
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
        if self.date is not None:
            result['date'] = []
            for k in self.date:
                result['date'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('date') is not None:
            self.date = []
            for k in m.get('date'):
                temp_model = ReportDomainPvServiceResponseDate()
                self.date.append(temp_model.from_map(k))
        return self


class ReportDomainPvServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainPvServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainPvServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainPvServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainUVRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        data_interval: str = None,
        domain: List[str] = None,
    ):
        # {"en":"Start date:
        #         1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (Beijing Time 2 December 2016 10:0 min 0 seconds);
        #         2. Not Greater Than The Current Time
        #         3. Data for the last six months (183 days) are available at most.", "zh_CN":"开始时间：
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        #         2.不能大于当前时间
        #         3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        #         1. Time format yyyy-MM-ddTHH:MM:ss+08:00
        #         2. The end time must be greater than the start time. if the end time is greater than the current time, take the current time.
        #         3. Date from, dateTo, neither passed, default query past 24 hours; If there is only one unsent, throw an exception
        #         4. Maximum time interval allowed for queries: 31 days, i.e. the difference between Date from and dateTo cannot exceed 31 days. (Could contact technical support adjustment)", "zh_CN":"结束时间：
        #         1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        #         2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        #         3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        #         4.允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天。（可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"Data granularity
        #         1. Support 1h (1 hour granularity), 1d (1 day granularity);
        #         2. The default is 1h;", "zh_CN":"数据粒度
        #         1.支持1h（1小时粒度）、1d（1天粒度）；
        #         2.不传默认为1h；"}
        self.data_interval = data_interval
        # {"en":"Domain name:
        #         1. The maximum number of TLDs is 20 by default (Technical Support Adjustment can be contacted);
        #         2. Automatic filtering invalid domain name (if pass illegal domain name, can be filtered, query result only returns the data of valid domain name).
        #         3. No default lookup of all domain names", "zh_CN":"域名：
        #         1.可传递域名数量上限默认为20个（可联系技术支持调整）；
        #         2.自动过滤掉无效域名（如传递非法域名，会被过滤，查询结果只返回有效域名的数据）。
        #         3.不传默认查全部域名"}
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
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.domain is not None:
            result['domain'] = self.domain
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
        return self


class QueryDomainUVResponseResultUvData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time
        #         1. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; Each time slice data value represents the data value in the previous time granularity range. The time slice at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00;
        #         2. When the data granularity of the query is 1d, the format is yyyy-MM-dd; Each time slice data value represents the value of the data for that date.
        #         3. Return the time slice contained in the start and end times.", "zh_CN":"时间
        #         1.查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        #         2.查询的数据粒度为1d时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值。
        #         3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"UV", "zh_CN":"UV数"}
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


class QueryDomainUVResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_time: str = None,
        peak_uv: str = None,
        total_uv: str = None,
        uv_data: List[QueryDomainUVResponseResultUvData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Peak Time", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"Peak value of UV", "zh_CN":"UV峰值"}
        self.peak_uv = peak_uv
        # {"en":"Total UV", "zh_CN":"UV总数"}
        self.total_uv = total_uv
        # {"en":"uvData", "zh_CN":"UV数"}
        self.uv_data = uv_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_uv, 'peak_uv')
        self.validate_required(self.total_uv, 'total_uv')
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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_uv is not None:
            result['peakUV'] = self.peak_uv
        if self.total_uv is not None:
            result['totalUV'] = self.total_uv
        if self.uv_data is not None:
            result['uvData'] = []
            for k in self.uv_data:
                result['uvData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakUV') is not None:
            self.peak_uv = m.get('peakUV')
        if m.get('totalUV') is not None:
            self.total_uv = m.get('totalUV')
        if m.get('uvData') is not None:
            self.uv_data = []
            for k in m.get('uvData'):
                temp_model = QueryDomainUVResponseResultUvData()
                self.uv_data.append(temp_model.from_map(k))
        return self


class QueryDomainUVResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryDomainUVResponseResult] = None,
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
                temp_model = QueryDomainUVResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryDomainUVPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainUVParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainUVRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainUVResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




