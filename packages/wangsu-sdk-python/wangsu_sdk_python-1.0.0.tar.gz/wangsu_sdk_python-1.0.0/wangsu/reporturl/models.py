# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReportUrlOriginServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
    ):
        # {'en':'Start date:
        # The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # Cannot be greater than the current time
        # The most recent six-month (183 days) data are available.', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年1月1日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2019-01-01T10:00:00+08:00 (Beijing Time, 1 January 2019: 0 minutes 0 seconds);
        # The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # Date from, dateTo, neither passed, default query past 24 hours; If there is only one unsent, throw an exception
        # Maximum allowed query time interval: 31 days, i.e., the difference between Date from and dateTo cannot exceed 31 days (adjusted by contact technology support).', 'zh_CN':'结束时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年1月1日10点0分0秒）；
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天（可联系技术支持调整）。'}
        self.date_to = date_to
        # {'en':'Domain name:
        # 
        # The maximum number of TLDs that can be delivered is 20 by default (Technical Support Adjustments can be contacted).
        # Auto-filter illegal domain name (pass illegal domain name, will be filtered, query result only returns the data of legal domain name)
        # All domain names are queried by default when this entry is not delivered, but an error occurs when the number of domain names in the account exceeds the upper limit', 'zh_CN':'域名：
        # 
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）。
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        # 3.未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误'}
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


class ReportUrlOriginServiceResponseDataUrlDatas(TeaModel):
    def __init__(
        self,
        url: str = None,
        value: str = None,
    ):
        # {'en':'URL', 'zh_CN':'URL'}
        self.url = url
        # {'en':'Number of requests', 'zh_CN':'请求数'}
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


class ReportUrlOriginServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        url_datas: List[ReportUrlOriginServiceResponseDataUrlDatas] = None,
    ):
        # {'en':'Domain name', 'zh_CN':'域名'}
        self.domain = domain
        self.url_datas = url_datas

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.url_datas, 'url_datas')
        if self.url_datas:
            for k in self.url_datas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.url_datas is not None:
            result['urlDatas'] = []
            for k in self.url_datas:
                result['urlDatas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('urlDatas') is not None:
            self.url_datas = []
            for k in m.get('urlDatas'):
                temp_model = ReportUrlOriginServiceResponseDataUrlDatas()
                self.url_datas.append(temp_model.from_map(k))
        return self


class ReportUrlOriginServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportUrlOriginServiceResponseData] = None,
    ):
        # {'en':'Request result status code', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'Request Result Information', 'zh_CN':'请求结果信息'}
        self.message = message
        # {'en':'Detailed data on results of requests', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportUrlOriginServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportUrlOriginServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlOriginServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlOriginServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlOriginServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainRefererUrlServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        area_code: List[str] = None,
        order_by: str = None,
        top: int = None,
    ):
        # {"en":"Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.允许查询最大间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account and aggregate the returned data according to all domain names.
        # 2.Domain is uploaded: Up to 20 domains are supported.", "zh_CN":"域名:
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整)。
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整);
        # 3.自动过滤掉无效域名,(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"Acceleration areaCode is not uploaded: Query all acceleration areas by default.", "zh_CN":"加速区域:
        # 
        # 未传递areaCode时,默认查询所有加速区域。"}
        self.area_code = area_code
        # {"en":"Order by: 
        # 	1.The optional values are flow and request; 
        # 	2.If not passed, the default is request; 
        # 	3.When the value is flow, the query results are sorted in descending order of traffic, and when the value is request, they are sorted in descending order of the number of requests.
        # ", "zh_CN":"排序:
        # 
        # 1.request或flow;
        # 2.不传默认request;
        # 3.值为request时查询结果按照请求数降序排列;值为flow时查询结果按照流量值降序排列。"}
        self.order_by = order_by
        # {"en":"Top quantity:
        # If no parameter is passed, the default is TOP 10, and the maximum is TOP 200", "zh_CN":"排行:
        # 不传默认top10,有传最大top200。"}
        self.top = top

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
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.top is not None:
            result['top'] = self.top
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
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('top') is not None:
            self.top = m.get('top')
        return self


class ReportDomainRefererUrlServiceResponseData(TeaModel):
    def __init__(
        self,
        url: str = None,
        request: str = None,
        flow: str = None,
    ):
        # {"en":"URL", "zh_CN":"URL"}
        self.url = url
        # {"en":"Request", "zh_CN":"请求数"}
        self.request = request
        # {"en":"Flow", "zh_CN":"流量值,单位MB,保留2位小数"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.request, 'request')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.request is not None:
            result['request'] = self.request
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class ReportDomainRefererUrlServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportDomainRefererUrlServiceResponseData] = None,
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
                temp_model = ReportDomainRefererUrlServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainRefererUrlServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererUrlServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererUrlServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererUrlServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTopRankingUrlRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        order_by: str = None,
    ):
        # {"en":"Start date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (Beijing Time 2 December 2016 10:0 min 0 seconds);
        # 2. Not Greater Than The Current Time;
        # 3. Data for the last six months (183 days) are available at most.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. Time format yyyy-MM-ddTHH:MM:ss+08:00
        # 2. The end time must be greater than the start time. if the end time is greater than the current time, take the current time.
        # 3. Date from, dateTo, neither passed, default query day; If there is only one unsent, throw an exception
        # 4. Maximum time interval allowed for queries: 31 days, i.e. the difference between Date from and dateTo cannot exceed 31 days. (Could contact technical support adjustment)", "zh_CN":"结束时间：
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询当天；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天。（可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The default number of domain names is 100, which can be adjusted by contacting technical support. The maximum limit is 500;
        # 2. Automatic filtering invalid domain name (if pass illegal domain name, can be filtered, query result only returns the data of valid domain name).
        # 3. Did not deliver this entry, the default query account under all domain names, but when the number of domain names under the account number exceeds the upper limit, prompt an error", "zh_CN":"域名：
        # 1.可传递域名数量默认为100个，可联系技术支持调整，最大上限500；
        # 2.自动过滤掉无效域名（如传递非法域名，会被过滤，查询结果只返回有效域名的数据）。
        # 3.未传递该入参时，默认查询账号下所有域名，但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"Ordering:
        # 1. The optional values are: totalRequest, totalFlow
        # 2. No default totalRequest", "zh_CN":"排序：
        # 1.可选值为：totalRequest、totalFlow
        # 2.不传则默认取值 totalRequest"}
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


class QueryTopRankingUrlResponse(TeaModel):
    def __init__(
        self,
        top: str = None,
        url: str = None,
        total_flow: str = None,
        total_request: str = None,
        hit_request: str = None,
        miss_request: str = None,
        sc_200: str = None,
        sc_206: str = None,
        sc_302: str = None,
        sc_304: str = None,
        sc_404: str = None,
    ):
        # {"en":"Top ranking", "zh_CN":"top排名"}
        self.top = top
        # {"en":"url", "zh_CN":"url"}
        self.url = url
        # {"en":"Total flow: unit of measure MB, keeping 2 decimal places", "zh_CN":"总流量：计量单位MB，保留2位小数"}
        self.total_flow = total_flow
        # {"en":"Total request", "zh_CN":"总请求数"}
        self.total_request = total_request
        # {"en":"Total hit request", "zh_CN":"请求数hit值"}
        self.hit_request = hit_request
        # {"en":"Total miss request", "zh_CN":"请求数miss值"}
        self.miss_request = miss_request
        # {"en":"Number of requests for status code 200", "zh_CN":"状态码200的请求数"}
        self.sc_200 = sc_200
        # {"en":"Number of requests for status code 206", "zh_CN":"状态码206的请求数"}
        self.sc_206 = sc_206
        # {"en":"Number of requests for status code 302", "zh_CN":"状态码302的请求数"}
        self.sc_302 = sc_302
        # {"en":"Number of requests for status code 304", "zh_CN":"状态码304的请求数"}
        self.sc_304 = sc_304
        # {"en":"Number of requests for status code 404", "zh_CN":"状态码404的请求数"}
        self.sc_404 = sc_404

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.url, 'url')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.hit_request, 'hit_request')
        self.validate_required(self.miss_request, 'miss_request')
        self.validate_required(self.sc_200, 'sc_200')
        self.validate_required(self.sc_206, 'sc_206')
        self.validate_required(self.sc_302, 'sc_302')
        self.validate_required(self.sc_304, 'sc_304')
        self.validate_required(self.sc_404, 'sc_404')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.url is not None:
            result['url'] = self.url
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.hit_request is not None:
            result['hitRequest'] = self.hit_request
        if self.miss_request is not None:
            result['missRequest'] = self.miss_request
        if self.sc_200 is not None:
            result['sc200'] = self.sc_200
        if self.sc_206 is not None:
            result['sc206'] = self.sc_206
        if self.sc_302 is not None:
            result['sc302'] = self.sc_302
        if self.sc_304 is not None:
            result['sc304'] = self.sc_304
        if self.sc_404 is not None:
            result['sc404'] = self.sc_404
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('hitRequest') is not None:
            self.hit_request = m.get('hitRequest')
        if m.get('missRequest') is not None:
            self.miss_request = m.get('missRequest')
        if m.get('sc200') is not None:
            self.sc_200 = m.get('sc200')
        if m.get('sc206') is not None:
            self.sc_206 = m.get('sc206')
        if m.get('sc302') is not None:
            self.sc_302 = m.get('sc302')
        if m.get('sc304') is not None:
            self.sc_304 = m.get('sc304')
        if m.get('sc404') is not None:
            self.sc_404 = m.get('sc404')
        return self


class QueryTopRankingUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTopRankingUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTopRankingUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTopRankingUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainRefererWebsiteServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        order_by: str = None,
        top: int = None,
    ):
        # {"en":"Start time:
        # 
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2024-01-23T10:00 + 08:00 (10:00:00 Beijing time on January 23, 2024);
        # 
        # 2. Can not exceed the current time;
        # 
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2024-01-23T10:00:00+08:00（为北京时间2024年01月23日10点0分0秒）；
        # 2.不能大于当前时间；
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. The end time is greater than the start time.
        # 
        # 3. If the end time is greater than the current time, the current time is taken.
        # 
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days. ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：31天，即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domain: 1.The maximum number of deliverable domain names is 200 by default 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names) 3.The default query accounts for all domains if the number of domain names exceeds the upper limit when the entry is not delivered. If the number of domain names in the account exceeds the limit, an error is raised.", "zh_CN":"域名:
        # 
        # 1.可传递域名数量上限默认为200个
        # 
        # 2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 
        # 3.未传递该入参时,默认查询账号下所有域名,但当账号下域名数量超过上限时提示错误。"}
        self.domain = domain
        # {"en":"Order by: 1.The optional values are flow and request; 2.the default value is request; 3.When the value is flow, the query results are sorted in descending order of traffic, and when the value is request, they are sorted in descending order of the number of requests.", "zh_CN":"排序： 1.可选值为：request、flow 2.不传则默认取值 request
        # 
        # 3.值为request时查询结果按照请求数降序排列;值为flow时查询结果按照流量值降序排列。"}
        self.order_by = order_by
        # {"en":"op quantity: the default is TOP 10, and the maximum is TOP 500
        # 
        # ", "zh_CN":"排行: 不传默认top10,有传最大top500。"}
        self.top = top

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
        if self.top is not None:
            result['top'] = self.top
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
        if m.get('top') is not None:
            self.top = m.get('top')
        return self


class ReportDomainRefererWebsiteServiceResponseData(TeaModel):
    def __init__(
        self,
        website: str = None,
        request: str = None,
        flow: str = None,
    ):
        # {"en":"Website", "zh_CN":"网站"}
        self.website = website
        # {"en":"Requests", "zh_CN":"对应请求数"}
        self.request = request
        # {"en":"Traffic data, in MB, rounded to two decimal places", "zh_CN":"对应流量数据，单位：MB,保留两位小数"}
        self.flow = flow

    def validate(self):
        self.validate_required(self.website, 'website')
        self.validate_required(self.request, 'request')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.website is not None:
            result['website'] = self.website
        if self.request is not None:
            result['request'] = self.request
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('website') is not None:
            self.website = m.get('website')
        if m.get('request') is not None:
            self.request = m.get('request')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class ReportDomainRefererWebsiteServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportDomainRefererWebsiteServiceResponseData] = None,
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
                temp_model = ReportDomainRefererWebsiteServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainRefererWebsiteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererWebsiteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererWebsiteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainRefererWebsiteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUrlCustomTopDailyServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        top: str = None,
        order_by: str = None,
    ):
        # {"en":"Start time:
        # 1. Time format is yyyy-MM-ddTHH:mm:ss+08:00,
        # 2. No bigger than the current time.
        # 3. Data in the last 183 days at most can be queried.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 7 days will be queried by default; if only one field is filled in and one is left empty, then exception will be occur.
        # 4. Allowable maximum time range for query: 31days, means the period between dateFrom to dateTo should not exceed 31days.", "zh_CN":"结束时间:
        # 1.时间格式2019-01-02T10:00:00+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的7天;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1. The maximum number of domain is 100 by default (the upper limit is 500 according to technical support adjustment);
        # 2. Automatically filter out invalid domain (an illegal domain will be filtered, and the query result will only return the data of valid domains).
        # 3. If the input parameter is not inputed, all domains under the account will be queried by default, but an error will be prompted when the number of domains under the account exceeds the upper limit", "zh_CN":"域名:
        # 可传递域名数量上限默认为100个(可联系技术支持调整)。
        # 自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 未传递该入参时,默认查询账号下所有域名,但当账号下域名数量超过上限时提示错误"}
        self.domain = domain
        # {"en":"highest number:
        # Default TOP 100;
        # Maximum TOP 500.", "zh_CN":"TOP个数:
        # 不传默认TOP 100
        # 最大TOP 500"}
        self.top = top
        # {"en":"sort by:
        # 1. Optional values are: request, flow
        # 2. Default value request", "zh_CN":"排序:
        # 1. 可选值为:request, flow
        # 2. 不传默认request"}
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


class ReportUrlCustomTopDailyServiceResponseData(TeaModel):
    def __init__(
        self,
        top: str = None,
        url: str = None,
        total_flow: str = None,
        total_request: str = None,
    ):
        # {"en":"top", "zh_CN":"top排名"}
        self.top = top
        # {"en":"url", "zh_CN":"url"}
        self.url = url
        # {"en":"Total traffic: unit MB, with 2 decimal places", "zh_CN":"总流量:计量单位MB,保留2位小数"}
        self.total_flow = total_flow
        # {"en":"Total requests", "zh_CN":"总请求数"}
        self.total_request = total_request

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.url, 'url')
        self.validate_required(self.total_flow, 'total_flow')
        self.validate_required(self.total_request, 'total_request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['top'] = self.top
        if self.url is not None:
            result['url'] = self.url
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        return self


class ReportUrlCustomTopDailyServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportUrlCustomTopDailyServiceResponseData] = None,
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
                temp_model = ReportUrlCustomTopDailyServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportUrlCustomTopDailyServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlCustomTopDailyServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlCustomTopDailyServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlCustomTopDailyServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




