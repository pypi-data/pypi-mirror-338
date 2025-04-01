# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportRequestQuicServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The time format is yyyy-MM-dd, for example, 2021-10-10;
        # 2. It cannot be greater than the current time
        # 3. Data for the most recent six months (183 days) can be obtained.", "zh_CN":"开始时间：
        #             时间格式为yyyy-MM-dd，例如，2021-10-10；
        #             不能大于当前时间
        #             最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-dd
        # 2. The end time must be greater than the start time. If the end time is greater than the current time, the current time is used.
        # 3. If both dateFrom and dateTo are not passed, the default query is the past day; if only one is not passed, an exception is thrown
        # 4. The maximum query time interval allowed is 7 days, that is, the difference between dateFrom and dateTo cannot exceed 7 days (you can contact technical support to adjust)", "zh_CN":"结束时间：
        #             时间格式为yyyy-MM-dd
        #             结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        #             dateFrom，dateTo二者都未传，默认查询过去的1天；如仅有一个未传，抛异常
        #             允许查询最大时间间隔：7天，即dateFrom和dateTo相差不能超过7天（可联系技术支持调整）。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The upper limit of the number of domain names that can be passed is 20 by default (you can contact technical support to adjust it).
        # 2. Automatically filter out illegal domain names (if an illegal domain name is passed, it will be filtered out, and the query result will only return data for legal domain names).
        # 3. When this parameter is not passed, all domain names under the account are queried by default, but an error message will be prompted when the number of domain names under the account exceeds the upper limit.", "zh_CN":"域名：
        #             可传递域名数量上限默认为20个（可联系技术支持调整）。
        #             自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        #             未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误"}
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


class ReportRequestQuicServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        total_request: str = None,
        quic_request: str = None,
    ):
        # {"en":"Time, in the format of yyyy-MM-dd HH:mm:ss", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm:ss"}
        self.timestamp = timestamp
        # {"en":"Number of requests, in units", "zh_CN":"请求个数，单位 个"}
        self.total_request = total_request
        # {"en":"Number of requests, in units", "zh_CN":"请求个数，单位 个"}
        self.quic_request = quic_request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.quic_request, 'quic_request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.quic_request is not None:
            result['quicRequest'] = self.quic_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('quicRequest') is not None:
            self.quic_request = m.get('quicRequest')
        return self


class ReportRequestQuicServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportRequestQuicServiceResponseData] = None,
    ):
        # {"en":"code", "zh_CN":"code"}
        self.code = code
        # {"en":"message", "zh_CN":"message"}
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
                temp_model = ReportRequestQuicServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportRequestQuicServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestQuicServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestQuicServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestQuicServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportHitServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportHitServiceResponseHitData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        hit: str = None,
    ):
        # {"en":"Date
        # When the data query granularity is fiveminutes, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05 AM, and the last one is yyyy-MM-dd 24:00;When the data query granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is yyyy-MM-dd 24;When the data query granularity is daily, the format is yyyy-MM-dd; the data value of every time slice represents the value of the daily data;Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间
        # 1.查询的数据粒度为fiveminutes时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是yyyy-MM-dd 24:00。
        # 2.查询的数据粒度为hourly时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是yyyy-MM-dd 24。
        # 3.查询的数据粒度为daily时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值；
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Total number of requests", "zh_CN":"请求数"}
        self.hit = hit

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.hit, 'hit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.hit is not None:
            result['hit'] = self.hit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        return self


class ReportHitServiceResponse(TeaModel):
    def __init__(
        self,
        hit_summary: str = None,
        hit_data: List[ReportHitServiceResponseHitData] = None,
    ):
        # {"en":"Total requests", "zh_CN":"总请求数"}
        self.hit_summary = hit_summary
        # {'en':'hitData', 'zh_CN':'请求数数据'}
        self.hit_data = hit_data

    def validate(self):
        self.validate_required(self.hit_summary, 'hit_summary')
        self.validate_required(self.hit_data, 'hit_data')
        if self.hit_data:
            for k in self.hit_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_summary is not None:
            result['hit-summary'] = self.hit_summary
        if self.hit_data is not None:
            result['hit-data'] = []
            for k in self.hit_data:
                result['hit-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hit-summary') is not None:
            self.hit_summary = m.get('hit-summary')
        if m.get('hit-data') is not None:
            self.hit_data = []
            for k in m.get('hit-data'):
                temp_model = ReportHitServiceResponseHitData()
                self.hit_data.append(temp_model.from_map(k))
        return self


class ReportHitServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportHitServiceParameters(TeaModel):
    def __init__(
        self,
        datefrom: str = None,
        dateto: str = None,
        type: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00
        # ;2.And smaller than the current time and ‘dateTo’;
        # 3.Period between ‘dataFrom’ and ‘dateTo’ cannot be longer than 31 days", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过31天（可联系技术支持调整）；
        # 4.只能查询最近2年内数据。"}
        self.datefrom = datefrom
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than ‘dateFrom’;
        # 3.If it’s greater than the current time, then the current time is assigned as the value", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；
        # 3.如果大于当前时间，则重新赋值为当前时间；"}
        self.dateto = dateto
        # {"en":"Data granularity
        # 1.fiveminutes: five minutes, hourly: one hour, daily: one day;
        # 2.If not specified, daily is set as the default value;
        # 3.If fiveminutes is specified as the value, then data is returned in actual configured granularity when there is specific configuration to data collecting granularity for the customer", "zh_CN":"数据粒度
        # 1.fiveminutes：5分钟，hourly：1小时，daily：1天；
        # 2.不传递，默认为daily；
        # 3.传递fiveminutes时，若客户数据采集粒度有特殊配置将按实际配置粒度返回。"}
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


class ReportHitServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportHitServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUserRequestCountryServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        area_code: List[str] = None,
        data_interval: str = None,
        country_code: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time;
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. The default query interval is 7 days, Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.默认查询间隔7天,允许查询最大间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 1. Domain is not uploaded: Query all domain names of the account (More than 20 domains will error,you can contact technical support for adjustment);
        # 2. Domain is uploaded: Up to 20 domains are supported(you can contact technical support for adjustment).", "zh_CN":"域名:
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)。"}
        self.domain = domain
        # {"en":"Acceleration area:
        # 1. Acceleration areaCode is not uploaded: Query all acceleration areas by default.", "zh_CN":"加速区域:
        # 未传递areaCode时,默认查询所有加速区域。"}
        self.area_code = area_code
        # {"en":"Data granularity:
        # 5m: 5 minute granularity;
        # 1h: 1 hour granularity;
        # 1d: 1 day granularity; Default value is 1d.", "zh_CN":"数据粒度:
        # 5m:5分钟粒度;
        # 1h:1小时粒度;
        # 1d:1天粒度。不传默认1天粒度"}
        self.data_interval = data_interval
        # {"en":"Country area:
        # 1. countryCode is not uploaded: Query all country areas by default;
        # 2. countryCode is uploaded: Multiple can be uploaded, such as cn, in.  Please refer to the appendix description section of the overview page.", "zh_CN":"国家区域(含中国台湾、中国澳门、中国香港、中国大陆):
        # 1.未传递countryCode时:查询全部国家区域;
        # 2.有传递countryCode时:可传多个,如cn,in。可传递的值详见概览页附录说明章节"}
        self.country_code = country_code
        # {"en":"Grouped dimension:
        # 1. The optional values are domain, countryCode;Multiple values can be uploaded;
        # 2. If no value is uploaded: Aggregate all data by default.", "zh_CN":"分组维度
        # 可选值为domain、countryCode,可传入多个值;
        # 有传入则按照该维度展示明细数据;
        # 没传默认全部聚合。"}
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
        if self.area_code is not None:
            result['areaCode'] = self.area_code
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
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportUserRequestCountryServiceResponseResultCountryDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        request: str = None,
    ):
        # {"en":"Time:
        # 
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; ach time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 2. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00;
        # 3. When the data query granularity is 1d, the format is yyyy-MM-dd; Each time slice value represents the value of the day;
        # 4. Return the time slices that contained in start time and in end time.", "zh_CN":"时间,
        # 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00;
        # 查询的数据粒度为1d时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值;
        # 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests.", "zh_CN":"请求数"}
        self.request = request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class ReportUserRequestCountryServiceResponseResultCountryData(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        total_request: str = None,
        request_data: List[ReportUserRequestCountryServiceResponseResultCountryDataRequestData] = None,
    ):
        # {"en":"Country area", "zh_CN":"国家区域"}
        self.country_code = country_code
        # {"en":"Total number of requests.", "zh_CN":"国家的请求总数"}
        self.total_request = total_request
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.request_data, 'request_data')
        if self.request_data:
            for k in self.request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportUserRequestCountryServiceResponseResultCountryDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportUserRequestCountryServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[ReportUserRequestCountryServiceResponseResultCountryData] = None,
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
                temp_model = ReportUserRequestCountryServiceResponseResultCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class ReportUserRequestCountryServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportUserRequestCountryServiceResponseResult] = None,
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
                temp_model = ReportUserRequestCountryServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportUserRequestCountryServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestCountryServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestCountryServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestCountryServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportRequestHttpHttpsServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH:mm:SS +08:00, for example, 2021-05-19T10:00:00+08:00 (10:00:00 Beijing time on May 19, 2021);
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
        # 4. Maximum query interval allowed: 1 day, that is, the difference between dateFrom and dateTo can not exceed 1 day.", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:1天,即dateFrom和dateTo相差不能超过1天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support).
        # 	2.Domain is not uploaded: Query all domain names of the account", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)"}
        self.domain = domain
        # {"en":"1. Optional value: domain
        # 	2. No value is passed, and all domain name data is aggregated by default", "zh_CN":"1.可选值:domain
        # 2.不传默认聚合所有频道数据"}
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


class ReportRequestHttpHttpsServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        https_value: str = None,
        http_value: str = None,
    ):
        # {"en":"TimeStamp, returns the time slice containing the start time and end time. Time format: 1 minute: yyyy-MM-dd HH: mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。时间格式:1分钟:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"HTTPS requests", "zh_CN":"https请求数"}
        self.https_value = https_value
        # {"en":"HTTP requests", "zh_CN":"http请求数"}
        self.http_value = http_value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.https_value, 'https_value')
        self.validate_required(self.http_value, 'http_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.https_value is not None:
            result['httpsValue'] = self.https_value
        if self.http_value is not None:
            result['httpValue'] = self.http_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('httpsValue') is not None:
            self.https_value = m.get('httpsValue')
        if m.get('httpValue') is not None:
            self.http_value = m.get('httpValue')
        return self


class ReportRequestHttpHttpsServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportRequestHttpHttpsServiceResponseDataDetailList] = None,
    ):
        # {"en":"Domain name, this field is not returned when summarizing all domain name data", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
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
                temp_model = ReportRequestHttpHttpsServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportRequestHttpHttpsServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportRequestHttpHttpsServiceResponseData] = None,
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
                temp_model = ReportRequestHttpHttpsServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportRequestHttpHttpsServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHttpHttpsServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHttpHttpsServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHttpHttpsServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUserRequestIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        area_code: List[str] = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. The default query interval upper limit is 7 days (can be adjusted by contacting technical support), the maximum allowable query interval: 31 days, that is, the difference between dateFrom and dateTo cannot exceed 31 days.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.默认查询间隔上限为7天(可联系技术支持调整),允许查询最大间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 1.Domain is not uploaded: Query all domain names of the account(More than 20 domains will error,you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 20 domains are supported(you can contact technical support for adjustment).", "zh_CN":"域名:
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)。"}
        self.domain = domain
        # {"en":"Acceleration area:
        # Acceleration areaCode is not uploaded: Query all acceleration areas by default.", "zh_CN":"加速区域:
        # 未传递areaCode时,默认查询所有加速区域。"}
        self.area_code = area_code
        # {"en":"By default, all provinces are queried, and the Chinese name of the province is passed. The province information code table is detailed in the appendix of the overview page.", "zh_CN":"默认查询全部省份,传递省份中文名称,省份信息码表详见概览页附录说明章节"}
        self.province = province
        # {"en":"By default, all operators are queried, and the operator's Chinese name is transmitted. The operator information code table is detailed in the appendix of the overview page.", "zh_CN":"默认查询全部运营商,传递运营商中文名称,运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Grouped dimension:
        # 1. The optional values are domain, province, isp; Multiple values can be uploaded;
        # 2. If no value is uploaded: Aggregate all data by default.", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据,,没传默认全部聚合。"}
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
        if self.area_code is not None:
            result['areaCode'] = self.area_code
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
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        request: str = None,
    ):
        # {"en":"Time:
        # 1. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; ach time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 2. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00;
        # 3. When the data query granularity is 1d, the format is yyyy-MM-dd; Each time slice value represents the value of the day;
        # 4. Return the time slices that contained in start time and in end time.", "zh_CN":"时间:
        # 1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00;
        # 2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1) 00;
        # 3.查询的数据粒度为1d时,格式为yyyy-MM-dd;每一个时间片数据值代表的该天内的数据值;
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests.", "zh_CN":"请求数"}
        self.request = request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        total_request: str = None,
        request_data: List[ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"Total number of requests.", "zh_CN":"省份运营商的请求总数"}
        self.total_request = total_request
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.request_data, 'request_data')
        if self.request_data:
            for k in self.request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportUserRequestIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceData] = None,
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
                temp_model = ReportUserRequestIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportUserRequestIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportUserRequestIspProvinceServiceResponseResultIspData] = None,
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
                temp_model = ReportUserRequestIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportUserRequestIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportUserRequestIspProvinceServiceResponseResult] = None,
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
                temp_model = ReportUserRequestIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportUserRequestIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUserRequestIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportProtocolOriginRequestServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: str = None,
    ):
        # {'en':'Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.', 'zh_CN':'开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (you can contact technical support for adjustment).. ', 'zh_CN':'结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.默认允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天（可联系技术支持调整）。'}
        self.date_to = date_to
        # {'en':'Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).', 'zh_CN':'域名：
        # 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)；
        # 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。'}
        self.domain = domain
        # {'en':'Data granularity:
        # 
        # 1m: 1 minute granularity; 
        # 5m: 5 minute granularity; Default value is 5m.
        # 1h: 1 hour granularity;
        # 1d: 1 day granularity.', 'zh_CN':'数据粒度：
        # 1m：1分钟粒度。
        # 5m：5分钟粒度。不传默认5分钟粒度
        # 1h：1小时粒度;
        # 1d：1天粒度'}
        self.data_interval = data_interval
        # {'en':'Grouped dimension:
        # 1.When the "groupBy" parameter has a value, the value can only be "domain". It will group and return the detailed based on domain;
        # 2.When groupBy does not have a value, aggregate all domain by default.', 'zh_CN':'分组维度
        # 1.有传，只能传domain。按照domain分组展示明细数据;
        # 2.不传，则默认所有域名聚合。'}
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


class ReportProtocolOriginRequestServiceResponseDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        all_requests: str = None,
        http_requests: str = None,
        https_requests: str = None,
    ):
        # {'en':'Time:
        # 
        # 1.When the data query granularity is 1m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00.
        # 2.When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00.
        # 3. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00.
        # 4. When the data query granularity is 1d, the format is yyyy-MM-dd; Each time slice value represents the value within the previous time granularity range.
        # 5. Return the time slices that contained in start time and in end time.', 'zh_CN':'时间，
        # 查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        # 查询的数据粒度为1d时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值；
        # 返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Number of all back-to-source requests.', 'zh_CN':'全部回源请求数'}
        self.all_requests = all_requests
        # {'en':'Number of http back-to-source requests.', 'zh_CN':'http回源请求数'}
        self.http_requests = http_requests
        # {'en':'Number of https back-to-source requests.', 'zh_CN':'https回源请求数'}
        self.https_requests = https_requests

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.all_requests, 'all_requests')
        self.validate_required(self.http_requests, 'http_requests')
        self.validate_required(self.https_requests, 'https_requests')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.all_requests is not None:
            result['allRequests'] = self.all_requests
        if self.http_requests is not None:
            result['httpRequests'] = self.http_requests
        if self.https_requests is not None:
            result['httpsRequests'] = self.https_requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('allRequests') is not None:
            self.all_requests = m.get('allRequests')
        if m.get('httpRequests') is not None:
            self.http_requests = m.get('httpRequests')
        if m.get('httpsRequests') is not None:
            self.https_requests = m.get('httpsRequests')
        return self


class ReportProtocolOriginRequestServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[ReportProtocolOriginRequestServiceResponseDataDetails] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'details', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportProtocolOriginRequestServiceResponseDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportProtocolOriginRequestServiceResponse(TeaModel):
    def __init__(
        self,
        data: List[ReportProtocolOriginRequestServiceResponseData] = None,
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
                temp_model = ReportProtocolOriginRequestServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportProtocolOriginRequestServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolOriginRequestServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolOriginRequestServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolOriginRequestServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportProtocolRequestServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: str = None,
    ):
        # {'en':'Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.', 'zh_CN':'开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (you can contact technical support for adjustment).;
        # 6.When querying daily granularity data, 00:00:00 on the following day represents the data of the current day, so the time range needs to include 00:00:00 on the following day.', 'zh_CN':'结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.默认允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天（可联系技术支持调整）。
        # 6.查询天粒度数据时，次日的00:00:00表示当天的数据，所以时间范围需包含次日的00:00:00。'}
        self.date_to = date_to
        # {'en':'Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).', 'zh_CN':'域名：
        # 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)；
        # 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。'}
        self.domain = domain
        # {'en':'Data granularity:
        # 
        # 1m: 1 minute granularity; 
        # 5m: 5 minute granularity; Default value is 5m.
        # 1h: 1 hour granularity;
        # 1d: 1 day granularity.', 'zh_CN':'数据粒度：
        # 1m：1分钟粒度。
        # 5m：5分钟粒度。不传默认5分钟粒度
        # 1h：1小时粒度;
        # 1d：1天粒度'}
        self.data_interval = data_interval
        # {'en':'Grouped dimension:
        # 
        # 1.When the "groupBy" parameter has a value, the value can only be "domain". It will group and return the detailed based on domain;
        # 2.When groupBy does not have a value, aggregate all domain by default.', 'zh_CN':'分组维度
        # 1.有传，只能传domain。按照domain分组展示明细数据;
        # 2.不传，则默认所有域名聚合。'}
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


class ReportProtocolRequestServiceResponseDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        all_requests: str = None,
        http_requests: str = None,
        https_requests: str = None,
    ):
        # {'en':'Time:
        # 
        # 1.When the data query granularity is 1m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00.
        # 2.When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00.
        # 3. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00.
        # 4. When the data query granularity is 1d, the format is yyyy-MM-dd; Each time slice value represents the value within the previous time granularity range.
        # 5. Return the time slices that contained in start time and in end time.', 'zh_CN':'时间，
        # 查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        # 查询的数据粒度为1d时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值；
        # 返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        # {'en':'Number of all requests.', 'zh_CN':'全部请求数'}
        self.all_requests = all_requests
        # {'en':'Number of httpe requests.', 'zh_CN':'http请求数'}
        self.http_requests = http_requests
        # {'en':'Number of https requests.', 'zh_CN':'https请求数'}
        self.https_requests = https_requests

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.all_requests, 'all_requests')
        self.validate_required(self.http_requests, 'http_requests')
        self.validate_required(self.https_requests, 'https_requests')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.all_requests is not None:
            result['allRequests'] = self.all_requests
        if self.http_requests is not None:
            result['httpRequests'] = self.http_requests
        if self.https_requests is not None:
            result['httpsRequests'] = self.https_requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('allRequests') is not None:
            self.all_requests = m.get('allRequests')
        if m.get('httpRequests') is not None:
            self.http_requests = m.get('httpRequests')
        if m.get('httpsRequests') is not None:
            self.https_requests = m.get('httpsRequests')
        return self


class ReportProtocolRequestServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        details: List[ReportProtocolRequestServiceResponseDataDetails] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'details', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportProtocolRequestServiceResponseDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportProtocolRequestServiceResponse(TeaModel):
    def __init__(
        self,
        data: List[ReportProtocolRequestServiceResponseData] = None,
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
                temp_model = ReportProtocolRequestServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportProtocolRequestServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolRequestServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolRequestServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportProtocolRequestServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStreamTaskNumberServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {'en':'Start Time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing time on December 2, 2018 at 10:00 am to 0 seconds);
        # 2. No more than the current time
        # 3. Up to 30 days of data available.', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2018年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近 30 天的数据。'}
        self.date_from = date_from
        # {'en':'End Time:
        # Time Format 2019-01-02T10:00:00+08:00
        # The end time should be greater than the start time. If the end time is greater than the current time, take the current time.
        # DateFrom, dateTo both not passed, the default query past 30 minutes; If only one is not sent, throw exception
        # Maximum time interval allowed for queries: 30 minutes', 'zh_CN':'结束时间：
        # 1.时间格式2019-01-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的 30 分钟；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：30分钟'}
        self.date_to = date_to
        # {'en':'Domain name:
        # The maximum number of transitive domain names by default is 200
        # Automatically filter out illegal domain names (such as passing illegal domain names, will be filtered out, the query results only return the data of the legal domain name).', 'zh_CN':'域名：
        # 1.可传递域名数量上限默认为200个
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。'}
        self.domain = domain

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


class ReportStreamTaskNumberServiceResponseDataDataDetail(TeaModel):
    def __init__(
        self,
        domain: str = None,
        h_265: str = None,
        transcode_num: str = None,
        duration: str = None,
    ):
        # {'en':'domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'h265', 'zh_CN':'1 or 0 , 1 代表 H265 转码，0 代表 H264 转码。'}
        self.h_265 = h_265
        # {'en':'transcodeNum', 'zh_CN':'转码数量'}
        self.transcode_num = transcode_num
        # {'en':'duration', 'zh_CN':'转码时长'}
        self.duration = duration

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.h_265, 'h_265')
        self.validate_required(self.transcode_num, 'transcode_num')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.h_265 is not None:
            result['h265'] = self.h_265
        if self.transcode_num is not None:
            result['transcodeNum'] = self.transcode_num
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('h265') is not None:
            self.h_265 = m.get('h265')
        if m.get('transcodeNum') is not None:
            self.transcode_num = m.get('transcodeNum')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class ReportStreamTaskNumberServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        data_detail: List[ReportStreamTaskNumberServiceResponseDataDataDetail] = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间片
        # 每一个时间片数据值代表的是前一个时间粒度范围内的数据值，比如yyyy-MM-dd 00:01，代表00:00到00:51范围内的数据。
        # 返回开始时间和结束时间包含的时间片。'}
        self.timestamp = timestamp
        self.data_detail = data_detail

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.data_detail, 'data_detail')
        if self.data_detail:
            for k in self.data_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.data_detail is not None:
            result['dataDetail'] = []
            for k in self.data_detail:
                result['dataDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('dataDetail') is not None:
            self.data_detail = []
            for k in m.get('dataDetail'):
                temp_model = ReportStreamTaskNumberServiceResponseDataDataDetail()
                self.data_detail.append(temp_model.from_map(k))
        return self


class ReportStreamTaskNumberServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportStreamTaskNumberServiceResponseData] = None,
    ):
        # {'en':'code', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'请求结果信息'}
        self.message = message
        # {'en':'data', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportStreamTaskNumberServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportStreamTaskNumberServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamTaskNumberServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamTaskNumberServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamTaskNumberServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainTotalRequestDomainList(TeaModel):
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


class QueryDomainTotalRequestRequest(TeaModel):
    def __init__(
        self,
        domain_list: QueryDomainTotalRequestDomainList = None,
    ):
        # {"en":"Domain list
        # Domain number limits can be adjusted depending on different accounts. The default value is 20(if you want to adjust,please, contact technical support)", "zh_CN":"域名列表
        # 1.域名个数限制根据账号可调，默认为20个（可联系技术支持下单调整）；"}
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
            temp_model = QueryDomainTotalRequestDomainList()
            self.domain_list = temp_model.from_map(m['domain-list'])
        return self


class QueryDomainTotalRequestResponseHitData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        hit: int = None,
    ):
        # {"en":"Date
        # When the querying data granularity is fiveminutes, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05 AM, and the last one is yyyy-MM-dd 24:00;When the data query granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is yyyy-MM-dd 24;When the querying data granularity is daily, the format is yyyy-MM-dd; the data value of every time slice represents the value of the data;Return the time slices contained in start time and in end time", "zh_CN":"时间
        # 1.查询的数据粒度为fiveminutes时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是yyyy-MM-dd 24:00。
        # 2.查询的数据粒度为hourly时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是yyyy-MM-dd 24
        # 3.查询的数据粒度为daily时，格式为yyyy-MM-dd；每一个时间片数据值代表的该天内的数据值；
        # 4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Total number of requests, More than 6 digits are displayed in scientific notation,e.g.:1642565=1.642565E6", "zh_CN":"请求数,超过6位数的以科学计数展示，例：1642565=1.642565E6"}
        self.hit = hit

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.hit, 'hit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.hit is not None:
            result['hit'] = self.hit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        return self


class QueryDomainTotalRequestResponse(TeaModel):
    def __init__(
        self,
        hit_summary: int = None,
        hit_data: List[QueryDomainTotalRequestResponseHitData] = None,
    ):
        # {"en":"Total requests", "zh_CN":"总请求数"}
        self.hit_summary = hit_summary
        # {'en':'hitData', 'zh_CN':'请求数据'}
        self.hit_data = hit_data

    def validate(self):
        self.validate_required(self.hit_summary, 'hit_summary')
        self.validate_required(self.hit_data, 'hit_data')
        if self.hit_data:
            for k in self.hit_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_summary is not None:
            result['hit-summary'] = self.hit_summary
        if self.hit_data is not None:
            result['hit-data'] = []
            for k in self.hit_data:
                result['hit-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hit-summary') is not None:
            self.hit_summary = m.get('hit-summary')
        if m.get('hit-data') is not None:
            self.hit_data = []
            for k in m.get('hit-data'):
                temp_model = QueryDomainTotalRequestResponseHitData()
                self.hit_data.append(temp_model.from_map(k))
        return self


class QueryDomainTotalRequestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTotalRequestParameters(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        type: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.And smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo should not be longer than 31 days;", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过31天；
        # 4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00
        # 2.Must be greater than dateFrom;
        # 3.If it is greater than the current time, then the current time will be assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；
        # 3.如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Data granularity
        # 1.fiveminutes: five minutes, hourly: one hour, daily: one day;
        # 2.If not specified, daily is set as the default value;
        # 3.If fiveminutes is specified as the value, then data is returned in the granularity of actual configuration when there is specific configuration of the data collecting granularity for the customer", "zh_CN":"数据粒度
        # 1.fiveminutes：5分钟，hourly：1小时，daily：1天；
        # 2.不传递，默认为daily；
        # 3.传递fiveminutes时，若客户数据采集粒度有特殊配置将按实际配置粒度返回。"}
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


class QueryDomainTotalRequestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainTotalRequestResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class HitRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
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
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"This parameter specifies if the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
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
        # {"en":"Display statistic result in merged or separate way
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type

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
        return self


class HitResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'请求数'}
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


class HitResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[HitResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'请求数数据'}
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
                temp_model = HitResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class HitResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: HitResponseProviderDateChannel = None,
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
            temp_model = HitResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class HitResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: HitResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'请求数数据'}
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
            temp_model = HitResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class HitResponse(TeaModel):
    def __init__(
        self,
        provider: HitResponseProvider = None,
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
            temp_model = HitResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class HitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HitRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportMinuteUserRequestIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        province: List[str] = None,
        isp: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:00:00 Beijing time on December 2, 2016);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
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
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days. ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error, you can contact technical support for adjustment)
        # 
        # 2.Domain is uploaded: Up to 20 domains are supported (you can contact technical support for adjustment).", "zh_CN":"域名：
        # 
        # 1.未传递domain时：查询账号下所有全部域名(域名超过20个则报错，可联系技术支持调整)；
        # 
        # 2.有传递domain时：域名最多支持传20个（可联系技术支持调整）。"}
        self.domain = domain
        # {"en":"Province:
        # 
        # 1. Province is not upload: Query all provinces and aggregate the returned data according to all provinces;
        # 
        # 2. Province is upload: Support upload multiple provinces. Upload the Chinese name of the province, such as: beijing, shanghai. Please refer to the appendix description section of the overview page for the provincial information code table.", "zh_CN":"省份：
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：支持传多个。传递省份code，如：beijing、shanghai。省份信息码表详见概览页附录说明章节"}
        self.province = province
        # {"en":"ISP:
        # 
        # 1. ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs;
        # 
        # 2. ISPs is upload: Support upload multiple ISPs. Upload the Chinese name of the ISPs, such as: dx, tt. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。
        # 
        # 2.有传递isp时：支持传多个。传递运营商code，如：dx、tt。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Data granularity:
        # 
        # 1m: 1 minute granularity.
        # 
        # 5m: 5 minute granularity; Default value is 5m.
        # 
        # 1h: 1 hour granularity.", "zh_CN":"数据粒度：
        # 
        # 1m：1分钟粒度。
        # 
        # 5m：5分钟粒度。不传默认5分钟粒度
        # 
        # 1h：1小时粒度;"}
        self.data_interval = data_interval
        # {"en":"Grouped dimension:
        # 
        # 1. The optional values are province, isp,domain;Multiple values can be uploaded;
        # 
        # 2. If no value is uploaded: Aggregate all data by default.", "zh_CN":"分组维度
        # 可选值为province、isp、domain，可传入多个值；
        # 有传入则按照该维度展示明细数据；
        # 没传默认全部聚合。"}
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
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
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
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        request: str = None,
    ):
        # {"en":"ime:
        # 
        # 1. When the data query granularity is 1m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        # 2. When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:05, and the last one is (yyyy-MM-dd+1) 00:00;
        # 
        # 3. When the data query granularity is 1h, the format is yyyy-MM-dd HH; Each time slice value represents the value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 01, and the last one is (yyyy-MM-dd+1) 00;
        # 
        # 4. Return the time slices that contained in start time and in end time.", "zh_CN":"时间，
        # 查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        # 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests.", "zh_CN":"请求数"}
        self.request = request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        total_request: str = None,
        details: List[ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceDataDetails] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"Total number of requests.", "zh_CN":"省份运营商的请求总数"}
        self.total_request = total_request
        self.details = details

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.total_request, 'total_request')
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
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportMinuteUserRequestIspProvinceServiceResponseDataIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceData] = None,
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
                temp_model = ReportMinuteUserRequestIspProvinceServiceResponseDataIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportMinuteUserRequestIspProvinceServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportMinuteUserRequestIspProvinceServiceResponseDataIspData] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
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
                temp_model = ReportMinuteUserRequestIspProvinceServiceResponseDataIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportMinuteUserRequestIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        data: List[ReportMinuteUserRequestIspProvinceServiceResponseData] = None,
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
                temp_model = ReportMinuteUserRequestIspProvinceServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportMinuteUserRequestIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportMinuteUserRequestIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportMinuteUserRequestIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportMinuteUserRequestIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRequestHitRatioRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"From date:
        #         1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example: 2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8)
        #         2.Cannot exceed current time
        #         3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2018年12月2日10点0分0秒)；
        #         2.不能大于当前时间
        #         3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"To time:
        #         1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example: 2019-01-01T10:00:00+08:00 (10:00 on December 2, 2018 10:00:00:00 UTC+8)
        #         2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        #         3.Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        #         4.Maximum allowed query time interval: 31 days, Date from and dateTo, not more than 31 days", "zh_CN":"结束时间:
        #         1.时间格式2019-01-02T10:00:00+08:00
        #         2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        #         3.dateFrom,dateTo二者都未传,默认查询过去的24小时；如仅有一个未传,抛异常
        #         4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天"}
        self.date_to = date_to
        # {"en":"Domain:
        #         1.The maximum number of deliverable domain names is 200 by default
        # 		2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        #         3.The default query accounts for all domains if the number of domain names exceeds the upper limit when the entry is not delivered. If the number of domain names in the account exceeds the limit, an error is raised.", "zh_CN":"域名:
        #         1.可传递域名数量上限默认为200个
        #         2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        #         3.未传递该入参时,默认查询账号下所有域名,但当账号下域名数量超过上限时提示错误。"}
        self.domain = domain
        # {"en":"Data granularity:
        # 
        # 1m: 1 minute granularity.
        # 
        # 5m: 5 minute granularity.
        # 
        # 1h: 1 hour granularity.
        # 
        # 1d: 1 day granularity. Default value is 1d.", "zh_CN":"数据粒度：
        # 
        # 支持1m（1分钟）、5m（5分钟）、1h（1小时）、1d（天）
        # 不传默认1d。"}
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


class QueryRequestHitRatioResponseDataHitRatioDatas(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        hit_ratio: str = None,
    ):
        # {"en":"timetamp
        # 1. When the data granularity of the query is fiveminutes, the format is yyyy-MM-dd HH:MM; Each time slice data value represents the data value in the previous time granularity range, For example yyyy-MM-dd 00:05 represents data in the range from 00:00 to 00:05.
        # 2.The data granularity of query is hourly, the format is yyyy-MM-dd HH. Each time slice data value represents data values in the previous time granularity range such as yyyy-MM-dd 01 that represent data from 00 to 01.
        # 3. the data granularity of the query is daily, the format is yyyy-MM-dd; Each time slice data value represents the data value for that day.
        # 4.Returns the timetamp contained in start time and end time.", "zh_CN":"时间，
        # 
        # 查询的数据粒度为1m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        # 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Cache hit ratio,keep 4 decimal places", "zh_CN":"缓存命中率,保留4位小数"}
        self.hit_ratio = hit_ratio

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.hit_ratio, 'hit_ratio')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.hit_ratio is not None:
            result['hitRatio'] = self.hit_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('hitRatio') is not None:
            self.hit_ratio = m.get('hitRatio')
        return self


class QueryRequestHitRatioResponseData(TeaModel):
    def __init__(
        self,
        real_date: str = None,
        total_avg: float = None,
        hit_ratio_datas: List[QueryRequestHitRatioResponseDataHitRatioDatas] = None,
    ):
        # {"en":"Actually processed time. yyyy-MM-dd HH:mm format", "zh_CN":"实际查询时间,格式 yyyy-MM-dd HH:mm"}
        self.real_date = real_date
        # {"en":"Average of total hit ratio.", "zh_CN":"总命中率的平均值"}
        self.total_avg = total_avg
        # {"en":"hitRatioDatas", "zh_CN":"缓存命中率数据"}
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
                temp_model = QueryRequestHitRatioResponseDataHitRatioDatas()
                self.hit_ratio_datas.append(temp_model.from_map(k))
        return self


class QueryRequestHitRatioResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryRequestHitRatioResponseData] = None,
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
                temp_model = QueryRequestHitRatioResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryRequestHitRatioPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestHitRatioParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestHitRatioRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestHitRatioResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRequestBySpecificProtocolRequest(TeaModel):
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
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于当前时间-183天，并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过7天（可联系技术支持调整）；
        # 4.dateFrom和dateTo要么都传递，要么都不传递；
        # 5.dateFrom和dateTo都未传递，则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；
        # 3.如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名，域名个数限制根据账号可调，默认为20个"}
        self.domain = domain
        # {"en":"Data granularity: 1m , 5m, support 5m", "zh_CN":"数据粒度 : 1m  , 5m ，默认5m"}
        self.data_interval = data_interval
        # {"en":"Transmission protocol
        # 
        # 1.Options: http, https;
        # 2.https is used as the default value is no value specified;
        # 3.httpRequestData is displayed if http is queried, and httpsRequestData is displayed if https is queried;", "zh_CN":"传输协议
        # 1.可选值为http、https；
        # 2.不传默认查询https；
        # 3.查询http时出参展示httpRequestData，查询https时出参展示httpsRequestData；"}
        self.protocol_type = protocol_type
        # {"en":"Group dimension
        # 
        # 1.The value can be selected is domain;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
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


class QueryRequestBySpecificProtocolResponseResultHttpsRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime, the format is  yyyy-MM-dd HH:mm; the data value of every time slice represents the data  value within the previous time granularity range.", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。比如yyyy-MM-dd 00:05，代表00:00到00:05范围内的数据。"}
        self.timestamp = timestamp
        # {"en":"Total number of requests", "zh_CN":"请求数"}
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


class QueryRequestBySpecificProtocolResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        https_request_data: List[QueryRequestBySpecificProtocolResponseResultHttpsRequestData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.https_request_data = https_request_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.https_request_data, 'https_request_data')
        if self.https_request_data:
            for k in self.https_request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.https_request_data is not None:
            result['httpsRequestData'] = []
            for k in self.https_request_data:
                result['httpsRequestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('httpsRequestData') is not None:
            self.https_request_data = []
            for k in m.get('httpsRequestData'):
                temp_model = QueryRequestBySpecificProtocolResponseResultHttpsRequestData()
                self.https_request_data.append(temp_model.from_map(k))
        return self


class QueryRequestBySpecificProtocolResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryRequestBySpecificProtocolResponseResult] = None,
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
                temp_model = QueryRequestBySpecificProtocolResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryRequestBySpecificProtocolPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestBySpecificProtocolParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestBySpecificProtocolRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestBySpecificProtocolResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryIPV6RequestOfeachISPandProvinceRequest(TeaModel):
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
        # {"en":"Start time: 
        #     1. Time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (10:00 on 2nd of December 2016, Beijing Time); 
        #     2. No bigger than the current time;
        #     3. Data in the last 183 days at most can be queried.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）;
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time: 1. the time format is 2016-12-02T10:00:00+08:00;
        #     2.End time should be greater than start time. If the end time is greater than current time, current time will be used;
        #     3.If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default; if only one field is filled in and one is left empty, then exception will be occur;
        #     4.Allowable maximum time range for query: 1 day, means the period between dateFrom to dateTo should not exceed 1 day (can be adjusted by contacting technical support).", "zh_CN":"结束时间：
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间;
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时，如仅有一个未传，抛异常;
        # 4.允许查询最大时间间隔：1天，即dateFrom和dateTo相差不能超过1天。（可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"Domain name: 1. The maximum number of TLDs is 20 by default (Technical Support Adjustment can be contacted); 
        #     2. automatic filtering invalid domain name (if pass illegal domain name, can be filtered, query result only returns the data of valid domain name).", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为200个（可联系技术支持调整）;
        # 2.自动过滤掉无效域名（如传递非法域名，会被过滤掉，查询结果只返回有效域名的数据）。"}
        self.domain = domain
        # {"en":"Data granularity 1. Support 5m (5 minute granularity), 1h (1 hour granularity); 2. The default is 5m;", "zh_CN":"数据粒度：
        # 1.支持5m（5分钟）、1h（1小时）
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
        # {"en":"IP type:
        # 	1.The optional values are IPv6 and IPv4;
        # 	2.If let this parameter empty,it will query all IP type.", "zh_CN":"IP类型：
        # 1.可选值为 IPV6、IPV4;
        # 2.不传默认查询全部"}
        self.iptype = iptype
        # {"en":"Grouped dimension:
        #     1.Aggregation date by default;
        #     2.the optional value is domain,province,isp,allow to send multi option ;
        #     3.send the Grouped dimension represent the need to display details by their corresponding values.For example, when groupBy is isp, the ISP dimension needs to be displayed in detail. When an ISP is not passed, it represents an aggregate date and would not return the ISP node.Provinces and domains have the same logic. For example, by passing 'groupBy': ['domain', 'province'], the ISP node under ispData does not need to return. {domain:'www.aaaa.com','ispData': [{'isp','China Telecom','provinceData': [...]}}",
        #     "zh_CN":"分组关键词：
        # 1.默认聚合展示;
        # 2.可选值为domain.province.isp，可传入多个值;
        # 3.传入关键词则代表需要按照关键词对应的值展示明细; 例如groupBy传入isp，则isp维度需要明细展示;当没有传递isp，则代表isp聚合展示，同时isp节点则不返回。其他province和domain相同逻辑。 例如：传递'groupBy':   ['domain','province']，则ispData下的isp节点无需返回。 { 'domain': 'www.aaaa.com', 'ispData': [ { 'isp':   '中国电信', 'provinceData': [....] }]}"}
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


class QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"1.When the data query granularity is 5m, then the format is yyyy-MM-dd HH:mm (the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00 ); 
        #                     2.When the data query granularity is hourly, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is yyyy-MM-dd 24;
        #                     3.Return the time slices that contained in start time and in end time.", "zh_CN":"时间，
        # 1.查询的数据粒度为5m时，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是（yyyy-MM-dd+1） 00:00；
        # 2.查询的数据粒度为1h时，格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01，最后一个时间片是（yyyy-MM-dd+1） 00；
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Requests", "zh_CN":"请求数"}
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


class QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        request_data: List[QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceDataRequestData] = None,
    ):
        # {"en":"province", "zh_CN":"省份"}
        self.province = province
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.request_data, 'request_data')
        if self.request_data:
            for k in self.request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryIPV6RequestOfeachISPandProvinceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"isp", "zh_CN":"运营商"}
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
                temp_model = QueryIPV6RequestOfeachISPandProvinceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class QueryIPV6RequestOfeachISPandProvinceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[QueryIPV6RequestOfeachISPandProvinceResponseResultIspData] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
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
                temp_model = QueryIPV6RequestOfeachISPandProvinceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class QueryIPV6RequestOfeachISPandProvinceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryIPV6RequestOfeachISPandProvinceResponseResult] = None,
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
                temp_model = QueryIPV6RequestOfeachISPandProvinceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryIPV6RequestOfeachISPandProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6RequestOfeachISPandProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6RequestOfeachISPandProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6RequestOfeachISPandProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRequestNumbersUnderShieldPoPRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, support 5m (granularity of 5 minutes)", "zh_CN":"数据粒度,支持5m: 5分钟粒度"}
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


class QueryRequestNumbersUnderShieldPoPResponseResultRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data  value within the previous time granularity range.", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。比如yyyy-MM-dd 00:05,代表00:00到00:05范围内的数据。"}
        self.timestamp = timestamp
        # {"en":"Total number of requests", "zh_CN":"请求数"}
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


class QueryRequestNumbersUnderShieldPoPResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        peak_time: str = None,
        peak_value: str = None,
        total_request: str = None,
        request_data: List[QueryRequestNumbersUnderShieldPoPResponseResultRequestData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Peak Time", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"Peak Request", "zh_CN":"请求数峰值"}
        self.peak_value = peak_value
        # {"en":"Total Request", "zh_CN":"总请求数"}
        self.total_request = total_request
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.request_data, 'request_data')
        if self.request_data:
            for k in self.request_data:
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
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryRequestNumbersUnderShieldPoPResponseResultRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryRequestNumbersUnderShieldPoPResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryRequestNumbersUnderShieldPoPResponseResult] = None,
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
                temp_model = QueryRequestNumbersUnderShieldPoPResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryRequestNumbersUnderShieldPoPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestNumbersUnderShieldPoPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestNumbersUnderShieldPoPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRequestNumbersUnderShieldPoPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportRequestIspProvinceServiceRequest(TeaModel):
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
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. can not exceed the current time;
        # 3. the latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒)；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. the end time is greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 4. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (technical support can be contacted to adjust).", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间；
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时；如仅有一个未传,抛异常；
        # 4.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名:可传递域名数量上限默认为20个(可联系技术支持调整),未传递该入参时查询账号下所有域名,但当账号下域名数量超过限制时不可查询(报错)。"}
        self.domain = domain
        # {"en":"Data granularity, 5m: 5-minute; granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,5m:5分钟粒度,1h:1小时粒度"}
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
        # 1. Options are domain, province, isp, and more than one value can be entered;
        # 2. The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值；
        # 2.有传入则按照该维度展示明细数据；"}
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


class ReportRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        qps: str = None,
    ):
        # {"en":"Time,", "zh_CN":"时间,
        #                1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00；
        #                2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1);00；
        #                3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Total number of requests", "zh_CN":"请求数"}
        self.value = value
        # {"en":"Number of requests within unit ; time. Keep two digits of decimals.", "zh_CN":"单位时间内的请求数,保留2位小数"}
        self.qps = qps

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.qps, 'qps')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.qps is not None:
            result['qps'] = self.qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        return self


class ReportRequestIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        request_data: List[ReportRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"qps", "zh_CN":"qps数据"}
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.request_data, 'request_data')
        if self.request_data:
            for k in self.request_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportRequestIspProvinceServiceResponseResultIspDataProvinceDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportRequestIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportRequestIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
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
                temp_model = ReportRequestIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportRequestIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportRequestIspProvinceServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"ispData", "zh_CN":"isp数据"}
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
                temp_model = ReportRequestIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportRequestIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportRequestIspProvinceServiceResponseResult] = None,
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
                temp_model = ReportRequestIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportRequestIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PolicyDetailReportRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        policy_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"domain id", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"policy Id", "zh_CN":"策略id"}
        self.policy_id = policy_id
        # {"en":"begin time", "zh_CN":"开始时间"}
        self.start_time = start_time
        # {"en":"end time", "zh_CN":"结束时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class PolicyDetailReportResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"detail", "zh_CN":"详情"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class PolicyDetailReportPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PolicyDetailReportParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PolicyDetailReportRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PolicyDetailReportResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportRequestHitRateIspProvinceServiceRequest(TeaModel):
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
        #         1.The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00) );
        #         2.Cannot be greater than the current time
        #         3.Up to the data for the last six months (183 days) can be obtained.", "zh_CN":"开始时间:
        #         1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        #         2.不能大于当前时间
        #         3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End Time:
        #         1.Time format yyyy-MM-ddTHH:mm:ss+08:00
        #         2.The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken.
        #         3.dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one undelivered, throw an exception
        #         4.Allow query maximum time interval: 7 days, that is, the difference between dateFrom and dateTo cannot exceed 7 days","zh_CN":"结束时间:
        #         1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        #         2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        #         3.dateFrom,dateTo二者都未传,默认查询过去的24小时；如仅有一个未传,抛异常
        #         4.允许查询最大时间间隔:7天,即dateFrom和dateTo相差不能超过7天。
        #         （可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"domain name:
        # 
        #         1.The maximum number of deliverable domain names is 20 by default (can be contacted by technical support);
        #         2.Automatically filter out invalid domain names (such as passing illegal domain names, they will be filtered out, and the query results only return data of valid domain names).", "zh_CN":"域名:
        #         1.可传递域名数量上限默认为20个（可联系技术支持调整）；
        #         2.自动过滤掉无效域名（如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据）。"}
        self.domain = domain
        # {"en":"Data granularity:
        # 
        #         1.support 5m (5 minutes), 1h (1 hour)
        # 
        #         2.do not pass the default 5m.", "zh_CN":"数据粒度:
        #         1.支持5m（5分钟）、1h（1小时）
        #         2.不传默认5m。"}
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
        # {"en":"Group keywords:
        # 
        #         1. the default aggregate display;
        #         2. The optional values are domain, province, and isp, which can pass multiple values.
        #         3. The incoming keyword means that the details need to be displayed according to the value corresponding to the keyword;
        #         For example, when groupBy is passed into isp, the isp dimension needs to be displayed in detail; when it is not passed, it represents the isp aggregation display, and the isp node does not return. Other provinces and domains have the same logic.
        #         For example: pass 'groupBy': ['domain', 'province'], then the isp node under ispData does not need to return.
        #         { 'domain': 'www.aaaa.com', 'ispData': [ { 'isp': 'China Telecom', 'provinceData': [....] }]}", "zh_CN":"分组关键词:
        #         1.默认聚合展示；
        #         2.可选值为domain、province、isp,可传入多个值；
        #         3.传入关键词则代表需要按照关键词对应的值展示明细；
        #         例如groupBy传入isp,则isp维度需要明细展示；当没有传递isp,则代表isp聚合展示,同时isp节点则不返回。其他province和domain相同逻辑。
        #         例如:传递'groupBy':  ['domain','province'],则ispData下的isp节点无需返回。
        #         { 'domain': 'www.aaaa.com', 'ispData': [ {'isp':  '中国电信','provinceData': [....] }]}"}
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


class ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
        hit_request: str = None,
    ):
        # {"en":"time,
        #         1. When the data size of the query is 5m, the format is yyyy-MM-dd HH:mm; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 00:05, and the last time slice is (yyyy-MM-dd+1) 00:00;
        #         2. When the data granularity of the query is 1h, the format is yyyy-MM-dd HH; each time slice data value represents the data value within the previous time granularity range. The time slice starting at the beginning of the day is yyyy-MM-dd 01, and the last time slice is (yyyy-MM-dd+1) 00;
        #         3. Return to the time slice included in the start time and end time.", "zh_CN":"时间,
        #         1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是（yyyy-MM-dd+1）00:00；
        #         2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是（yyyy-MM-dd+1）00；
        #         3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Request number hit rate, retain 4 decimal places", "zh_CN":"请求数命中率,保留4位小数"}
        self.value = value
        # {"en":"Number of hit requests. (This field is not provided by default, if you need this field, you can contact configuration support)", "zh_CN":"命中请求数
        #         (该字段默认不提供,需要该字段可联系配置支持)"}
        self.hit_request = hit_request

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')
        self.validate_required(self.hit_request, 'hit_request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        if self.hit_request is not None:
            result['hitRequest'] = self.hit_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('hitRequest') is not None:
            self.hit_request = m.get('hitRequest')
        return self


class ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        hit_rate_data: List[ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        # {"en":"Request number hit rate, retain 4 decimal places", "zh_CN":"求数命中率数据"}
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
                temp_model = ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceDataHitRateData()
                self.hit_rate_data.append(temp_model.from_map(k))
        return self


class ReportRequestHitRateIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceData] = None,
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
                temp_model = ReportRequestHitRateIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportRequestHitRateIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportRequestHitRateIspProvinceServiceResponseResultIspData] = None,
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
                temp_model = ReportRequestHitRateIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportRequestHitRateIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportRequestHitRateIspProvinceServiceResponseResult] = None,
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
                temp_model = ReportRequestHitRateIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportRequestHitRateIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHitRateIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHitRateIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportRequestHitRateIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DispatchDomainAreaTimeReportRequest(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        view_ids: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"domain id", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"view id", "zh_CN":"线路id 多个用英文逗号,隔开。为空表示查所有。"}
        self.view_ids = view_ids
        # {"en":"begin time", "zh_CN":"开始时间"}
        self.start_time = start_time
        # {"en":"end time", "zh_CN":"结算时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.view_ids is not None:
            result['viewIds'] = self.view_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('viewIds') is not None:
            self.view_ids = m.get('viewIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class DispatchDomainAreaTimeReportResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"detail", "zh_CN":"详情"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DispatchDomainAreaTimeReportPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchDomainAreaTimeReportParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchDomainAreaTimeReportRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchDomainAreaTimeReportResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryEdgeRequestHitRatioServiceRequest(TeaModel):
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


class QueryEdgeRequestHitRatioServiceResponseResultHitRatioDatas(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        edge_hit_ratio: str = None,
    ):
        # {"en":"timestamp", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01，最后一个时间片是（yyyy-MM-dd+1） 00:00；"}
        self.timestamp = timestamp
        # {"en":"edge node hit ratio,keep 4 decimal places", "zh_CN":"边缘节点请求数命中率，保留4位小数"}
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


class QueryEdgeRequestHitRatioServiceResponseResult(TeaModel):
    def __init__(
        self,
        real_date: str = None,
        total_avg: str = None,
        hit_ratio_datas: List[QueryEdgeRequestHitRatioServiceResponseResultHitRatioDatas] = None,
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
                temp_model = QueryEdgeRequestHitRatioServiceResponseResultHitRatioDatas()
                self.hit_ratio_datas.append(temp_model.from_map(k))
        return self


class QueryEdgeRequestHitRatioServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryEdgeRequestHitRatioServiceResponseResult] = None,
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
                temp_model = QueryEdgeRequestHitRatioServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryEdgeRequestHitRatioServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeRequestHitRatioServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeRequestHitRatioServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryEdgeRequestHitRatioServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




