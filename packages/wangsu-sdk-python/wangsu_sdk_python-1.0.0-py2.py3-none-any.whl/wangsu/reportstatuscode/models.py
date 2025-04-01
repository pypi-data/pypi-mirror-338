# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryIPV6StatusOfeachISPandProvinceRequest(TeaModel):
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
        # 	1. Time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (10:00 on 2nd of December 2016, Beijing Time); 
        #     2. No bigger than the current time. 
        #     3. Data in the last 183 days at most can be queried.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2016-12-02T10:00:00+08:00（为北京时间2016年12月2日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。"}
        self.date_from = date_from
        # {"en":"End time: 
        # 	1. the time format is 2016-12-02T10:00:00+08:00 
        #     2. End time should be greater than start time. If the end time is greater than current time, current time will be used. 
        #     3. If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default; if only one field is filled in and one is left empty, then exception will be occur. 
        #     4. Allowable maximum time range for query: 1 day, means the period between dateFrom to dateTo should not exceed 1 day (can be adjusted by contacting technical support).", "zh_CN":"结束时间：
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：1天，即dateFrom和dateTo相差不能超过1天。（可联系技术支持调整）"}
        self.date_to = date_to
        # {"en":"Domain name: 
        # 	1. The maximum number of domains is 200 by default (Technical Support Adjustment can be contacted); 
        #     2. Automatic filtering invalid domain name (if pass illegal domain name, can be filtered, query result only returns the data of valid domain name).", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为200个（可联系技术支持调整）；
        # 2.自动过滤掉无效域名（如传递非法域名，会被过滤掉，查询结果只返回有效域名的数据）。"}
        self.domain = domain
        # {"en":"Data granularity:
        #     1. Support 5m (5 minute granularity), 1h (1 hour granularity); 
        # 	2. The default is 5m", "zh_CN":"数据粒度：
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
        # 	1.The optional values are IPv6 and IPv4 
        # 	2.If let this parameter empty,it will query all IP type", "zh_CN":"IP类型：
        # 1.可选值为 IPV6、IPV4
        # 2.不传默认查询全部"}
        self.iptype = iptype
        # {"en":"Grouped dimension: 
        #     1.Aggregation date by default. 
        #     2.the optional value is domain,province,isp,allow to send multi option 
        #     3.send the Grouped dimension represent the need to display details by their corresponding values.For example, when groupBy is isp, the ISP dimension needs to be displayed in detail. When an ISP is not passed, it represents an aggregate date and would not return the ISP node. Provinces and domains have the same logic. For example, by passing 'groupBy': ['domain', 'province'], the ISP node under ispData does not need to return. {domain:'www.aaaa.com','ispData': [{'isp','China Telecom','provinceData': [...]}]}", "zh_CN":"分组关键词：
        # 1.默认聚合展示；
        # 2.可选值为domain.province.isp，可传入多个值；
        # 3.传入关键词则代表需要按照关键词对应的值展示明细； 例如groupBy传入isp，则isp维度需要明细展示；当没有传递isp，则代表isp聚合展示，同时isp节点则不返回。其他province和domain相同逻辑。 例如：传递'groupBy':   ['domain','province']，则ispData下的isp节点无需返回。 { 'domain': 'www.aaaa.com', 'ispData': [ { 'isp':   '中国电信', 'provinceData': [....] }]}"}
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


class QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time granularity is 5m, the format is yyyy-MM-dd HH:mm", "zh_CN":"数据粒度为5分钟，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Requests of status code", "zh_CN":"状态码请求数"}
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


class QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData] = None,
    ):
        # {"en":"Status Code", "zh_CN":"状态码类型"}
        self.status_code = status_code
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        status_code_data: List[QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class QueryIPV6StatusOfeachISPandProvinceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceData] = None,
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
                temp_model = QueryIPV6StatusOfeachISPandProvinceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class QueryIPV6StatusOfeachISPandProvinceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[QueryIPV6StatusOfeachISPandProvinceResponseResultIspData] = None,
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
                temp_model = QueryIPV6StatusOfeachISPandProvinceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class QueryIPV6StatusOfeachISPandProvinceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryIPV6StatusOfeachISPandProvinceResponseResult] = None,
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
                temp_model = QueryIPV6StatusOfeachISPandProvinceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryIPV6StatusOfeachISPandProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6StatusOfeachISPandProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6StatusOfeachISPandProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryIPV6StatusOfeachISPandProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowIpVersionStatusCodeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Starting time:
        # 	1. The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00); 
        # 	2. Cannot be greater than the current time 
        # 	3. Get up to the last six months (183 days) of data.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2021-05-19T10:00:00+08:00(为北京时间2021年5月19日10点0分0秒)
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End Time: 
        # 	1. Time format 2016-12-02T10:00:00+08:00 
        # 	2. The end time needs to be greater than the start time. If the end time is greater than the current time, the current time is taken. 
        # 	3. dateFrom, dateTo are not passed, the default query for the past 24 hours; if there is only one untransmitted, throw an exception 
        # 	4. Allow query maximum time interval: 1 days, that is, the difference between dateFrom and dateTo can't exceed 1 days (can contact technical support adjustment).", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:1天,即dateFrom和dateTo相差不能超过1天。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"domain name: 
        # 	1. The maximum number of deliverable domain names is 20 by default (can be contacted by technical support); 
        # 	2. Automatically filter out illegal domain names (such as passing illegal domain names, they will be filtered out, and the query results only return data of legitimate domain names).", "zh_CN":"域名:
        # 1、可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2、自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
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


class ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        v_4value: str = None,
        v_6value: str = None,
    ):
        # {"en":"timestamp,Returns the timestamp between the start time and end time. Time format: Hours: yyyy MM DD hh:00:00", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。
        # 时间格式:5分钟:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"IPv4 data", "zh_CN":"IPv4数据"}
        self.v_4value = v_4value
        # {"en":"IPv6 data", "zh_CN":"IPv6数据"}
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


class ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataListDetailList] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowIpVersionStatusCodeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data_list: List[ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataList] = None,
    ):
        # {"en":"Domain. If merge date of all domains will not return domain", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
        self.domain = domain
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data_list is not None:
            result['statusCodeDataList'] = []
            for k in self.status_code_data_list:
                result['statusCodeDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeDataList') is not None:
            self.status_code_data_list = []
            for k in m.get('statusCodeDataList'):
                temp_model = ReportFlowIpVersionStatusCodeServiceResponseDataStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class ReportFlowIpVersionStatusCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowIpVersionStatusCodeServiceResponseData] = None,
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
                temp_model = ReportFlowIpVersionStatusCodeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowIpVersionStatusCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIpVersionStatusCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIpVersionStatusCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowIpVersionStatusCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeNodeOriginServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 
        # 1.The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00);
        # 2.Cannot be greater than the current time
        # 3.Get up to the last six months (183 days) of data.", "zh_CN":"开始时间
        # 
        #         格式为yyyy-MM-ddTHH:mm:ss+08:00；
        #         必须大于当前时间-183 天，并且小于当前时间和dateTo；
        #         dateFrom和dateTo相差不能超过7天；
        #         dateFrom和dateTo要么都传递，要么都不传递；
        #         dateFrom和dateTo都未传递，则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;
        # 3.If both fields of dataFrom and dateTo are left empty, then data in the last 24 hours will be queried by default;
        # 4.Allowable maximum time range for query: 7 day, means the period between dateFrom to dateTo should not exceed 7 day", "zh_CN":"结束时间
        #         格式为yyyy-MM-ddTHH:mm:ss+08:00；
        #         必须大于dateFrom；如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The default upper limit to domains that can be entered is 20 (Contact technical support to adjust);", "zh_CN":"域名，域名个数限制根据账号可调，默认为20个"}
        self.domain = domain
        # {"en":"Data granularity:5m (5 minutes granularity)", "zh_CN":"数据粒度，5m：5分钟粒度"}
        self.data_interval = data_interval
        # {"en":"Group dimension:
        # Optional values:domain.The detailed data will be displayed according to the dimension", "zh_CN":"分组维度
        #         可选值为domain；
        #         有传入则按照该维度展示明细数据；"}
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


class ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"The format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range.The first time of the day was yyyy-MM-dd 00:05, and the last time was yyyy-MM-dd 24:00", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05，最后一个时间片是yyyy-MM-dd 24:00。"}
        self.timestamp = timestamp
        # {"en":"Requests of status code", "zh_CN":"状态码对应的请求数"}
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


class ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginDataRequestData] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        # {"en":"Request data", "zh_CN":"请求数据"}
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeNodeOriginServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_origin_data: List[ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Status code data", "zh_CN":"状态码数据"}
        self.status_code_origin_data = status_code_origin_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_origin_data, 'status_code_origin_data')
        if self.status_code_origin_data:
            for k in self.status_code_origin_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_origin_data is not None:
            result['statusCodeOriginData'] = []
            for k in self.status_code_origin_data:
                result['statusCodeOriginData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeOriginData') is not None:
            self.status_code_origin_data = []
            for k in m.get('statusCodeOriginData'):
                temp_model = ReportStatusCodeNodeOriginServiceResponseResultStatusCodeOriginData()
                self.status_code_origin_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeNodeOriginServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportStatusCodeNodeOriginServiceResponseResult] = None,
    ):
        # {"en":"Result", "zh_CN":"结果"}
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
                temp_model = ReportStatusCodeNodeOriginServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportStatusCodeNodeOriginServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeNodeOriginServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeNodeOriginServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeNodeOriginServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeOriginFailRateServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"Start date:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2.Cannot exceed current time
        # 3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒)；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3.Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        # 4.Maximum allowed query time interval: 24 hours (with technical support adjustments), meaning that the difference between Date from and dateTo cannot exceed 24 hours.", "zh_CN":"结束时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒)
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：24小时(可联系技术支持调整)，即dateFrom和dateTo相差不能超过24小时。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1.The maximum number of TLDs that can be delivered is 20 by default (contact technical support adjustment);
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3.Domain name exceeding limit, misstatement", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)；
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        # 3.域名超过上限，报错"}
        self.domain = domain
        # {"en":"Data granularity:  
        # 1.The default is 1m;
        # 2.Support 1m (1 minute), 5m (5 minutes)", "zh_CN":"数据粒度：
        # 1.不传默认1m
        # 2.支持1m(1分钟)、5m(5分钟)"}
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


class ReportStatusCodeOriginFailRateServiceResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        total_request: str = None,
        fail_request: str = None,
        fail_rate: str = None,
    ):
        # {"en":"Time, in yyyy-MM-dd HH:MM", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Total number of return requests", "zh_CN":"回源总请求数"}
        self.total_request = total_request
        # {"en":"Number of source failure requests (non-2XX status codes)", "zh_CN":"回源失败请求数(非2XX状态码)"}
        self.fail_request = fail_request
        # {"en":"Return source failure rate, reserved 4 decimal places", "zh_CN":"回源失败率，保留4位小数"}
        self.fail_rate = fail_rate

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.fail_request, 'fail_request')
        self.validate_required(self.fail_rate, 'fail_rate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.fail_request is not None:
            result['failRequest'] = self.fail_request
        if self.fail_rate is not None:
            result['failRate'] = self.fail_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('failRequest') is not None:
            self.fail_request = m.get('failRequest')
        if m.get('failRate') is not None:
            self.fail_rate = m.get('failRate')
        return self


class ReportStatusCodeOriginFailRateServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportStatusCodeOriginFailRateServiceResponseData] = None,
    ):
        # {"en":"Request result status code", "zh_CN":"请求结果状态码"}
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
                temp_model = ReportStatusCodeOriginFailRateServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeOriginFailRateServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeOriginFailRateServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeOriginFailRateServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeOriginFailRateServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryStatusCodeDistributioninCountriesRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        country_code: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time
        # 
        # 1. The format is yyyyy-MM-ddTHH:mm:SS+08:00, for example, 2016-12-02T10:00+08:00 (10:00:00 Beijing time on December 2, 2016);
        # 2. can not exceed the current time;
        # 3. the latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 4. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (technical support can be contacted to adjust). ", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间;
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 4.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名:可传递域名数量上限默认为20个(可联系技术支持调整),未传递报错"}
        self.domain = domain
        # {"en":"Data granularity, 1m: 1-minute  5m: 5-minute  granularity, 1h: 1-hour granularity, 1d: 1-day granularity", "zh_CN":"数据粒度,1m: 1分钟粒度, 5m:5分钟粒度,1h:1小时粒度,1d:1天粒度"}
        self.data_interval = data_interval
        # {"en":"Country code 1) By default, all countries  are queried; 2) For specific country and region names, please refer to the appendix chapter on the overview page).","zh_CN":"国家代号: 1) 没传返回所有国家; 2)具体国家和地区名称请参考概览页面的附录章节."}
        self.country_code = country_code
        # {"en":"Group dimension
        # 
        # 1.        Options   are domain, province, isp, and more than one value can be entered;
        # 
        # 2.        The   data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、country,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
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


class QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time,
        # 1.        When   the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data   value of every time slice represents the data value within the previous time   granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM,   and the last one is (yyyy-MM-dd+1) 00:00;
        # 2.        When   the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value   of every time slice represents the data value within the previous time   granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and   the last one is (yyyy-MM-dd+1) 00;
        # 3.        Return   the time slice contained in start time and the time slice contained in end   time.", "zh_CN":"时间,
        # 1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)&nbsp;00;
        # 3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests of the status   code", "zh_CN":"状态码对应的请求数"}
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


class QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeDataRequestData] = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.status_code = status_code
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributioninCountriesResponseDataCountryData(TeaModel):
    def __init__(
        self,
        country_code: str = None,
        country_name: str = None,
        status_code_data: List[QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeData] = None,
    ):
        # {"en":"country code", "zh_CN":"国家代码"}
        self.country_code = country_code
        # {"en":"country name", "zh_CN":"国家名称"}
        self.country_name = country_name
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.country_code, 'country_code')
        self.validate_required(self.country_name, 'country_name')
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
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
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        if m.get('countryName') is not None:
            self.country_name = m.get('countryName')
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = QueryStatusCodeDistributioninCountriesResponseDataCountryDataStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributioninCountriesResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[QueryStatusCodeDistributioninCountriesResponseDataCountryData] = None,
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
                temp_model = QueryStatusCodeDistributioninCountriesResponseDataCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributioninCountriesResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryStatusCodeDistributioninCountriesResponseData] = None,
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
                temp_model = QueryStatusCodeDistributioninCountriesResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributioninCountriesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributioninCountriesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributioninCountriesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributioninCountriesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryOriginStatusCodeDistributionRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
        backsrc_only: int = None,
        query_by: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days;
        # 4dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过7天;
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
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is  20", "zh_CN":"域名,域名个数限制根据账号可调,默认为20个"}
        self.domain = domain
        # {"en":"Data granularity, 5m: granularity of 5 minutes", "zh_CN":"数据粒度,5m:5分钟粒度"}
        self.data_interval = data_interval
        # {"en":"Group dimension
        # 
        # 1.The value can be selected is domain;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by
        # {"en":"Optional values 0, 1. Default is 0
        # Input parameter 1 returns the total number of requests to the source, and 0 only returns the number of requests to the source station", "zh_CN":"可选值 0, 1 。默认为 0
        # 入参 1 则返回全部回源请求数,入参 0 则只返回回源站请求数"}
        self.backsrc_only = backsrc_only
        # {"en":"Query dimension. Optional values: statusCode , statusCodeType. Default value is statuscode.
        # 1.statusCode: returns the status code details;
        # 2.statusCodeType: returns the requests of each status code type (such as the number of requests corresponding to success, redirect, not modified, permission, not found, server error, and other)", "zh_CN":"查询维度,可选值:statusCode, statusCodeType;不传默认statusCode
        # 1.statusCode :返回状态码明细;
        # 2.statusCodeType:返回状态码类型对应明细(如Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other对应的请求数)"}
        self.query_by = query_by

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
        if self.backsrc_only is not None:
            result['backsrcOnly'] = self.backsrc_only
        if self.query_by is not None:
            result['queryBy'] = self.query_by
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
        if m.get('backsrcOnly') is not None:
            self.backsrc_only = m.get('backsrcOnly')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        return self


class QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range.", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。每一个时间片数据值代表的是前一个时间粒度范围内的数据值,比如yyyy-MM-dd 00:05,代表00:00到00:05范围内的数据。"}
        self.timestamp = timestamp
        # {"en":"Number of requests of the status  code", "zh_CN":"状态码对应的请求数"}
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


class QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginDataRequestData] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        # {"en":"requestData", "zh_CN":"数据"}
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryOriginStatusCodeDistributionResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_type: str = None,
        status_code_origin_data: List[QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other", "zh_CN":"Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other"}
        self.status_code_type = status_code_type
        # {"en":"statusCodeOriginData", "zh_CN":"回源状态码数据"}
        self.status_code_origin_data = status_code_origin_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_type, 'status_code_type')
        self.validate_required(self.status_code_origin_data, 'status_code_origin_data')
        if self.status_code_origin_data:
            for k in self.status_code_origin_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_type is not None:
            result['statusCodeType'] = self.status_code_type
        if self.status_code_origin_data is not None:
            result['statusCodeOriginData'] = []
            for k in self.status_code_origin_data:
                result['statusCodeOriginData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeType') is not None:
            self.status_code_type = m.get('statusCodeType')
        if m.get('statusCodeOriginData') is not None:
            self.status_code_origin_data = []
            for k in m.get('statusCodeOriginData'):
                temp_model = QueryOriginStatusCodeDistributionResponseResultStatusCodeOriginData()
                self.status_code_origin_data.append(temp_model.from_map(k))
        return self


class QueryOriginStatusCodeDistributionResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryOriginStatusCodeDistributionResponseResult] = None,
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
                temp_model = QueryOriginStatusCodeDistributionResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryOriginStatusCodeDistributionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOriginStatusCodeDistributionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOriginStatusCodeDistributionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOriginStatusCodeDistributionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlvStatusCodeRealTimeOriginTotalServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        query_by: str = None,
    ):
        # {"en":"Start time: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.Cannot exceed current time 
        # 	3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time: 
        # 	1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 	2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time. 
        # 	3.If both fields of dataFrom and dateTo are left empty, the default query past 24 hours; If there is only one unsent, throw an exception 
        # 	4.Maximum allowed query time interval: 24 hours, Date from and dateTo, not more than 24 hours", "zh_CN":"结束时间:
        # 时间格式2016-12-02T10:00:00+08:00
        # 结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常
        # 允许查询最大时间间隔:24小时(可联系技术支持调整),即dateFrom和dateTo相差不能超过24小时。"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support). 
        # 	2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)", "zh_CN":"域名:
        # 可传递域名数量上限默认为20个(可联系技术支持调整);
        # 自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 域名超过上限,报错"}
        self.domain = domain
        # {"en":"Data granularity: 1. Default 1m 2. 1m (1 minute), 5m (5 minutes)
        # ", "zh_CN":"数据粒度:不传默认1m
        # 支持1m(1分钟)、5m(5分钟)"}
        self.data_interval = data_interval
        # {"en":"Query dimension:
        # Optional values: statusCode, 2XX, 3XX, 4XX, 5XX;
        # Default value is statusCode if not passed;
        # statusCode: Returns the detailed origin status code;
        # 2XX: Returns the detailed data of origin status codes starting with 2;
        # 3XX: Returns the detailed data of origin status codes starting with 3;
        # 4XX: Returns the detailed data of origin status codes starting with 4;
        # 5XX: Returns the detailed data of origin status codes starting with 5.", "zh_CN":"查询维度:
        # 可选值 statusCode, 2XX, 3XX, 4XX, 5XX;
        # 不传默认 statusCode;
        # statusCode :返回回源状态码明细;
        # 2XX : 返回各 2 开头回源状态码明细数据;
        # 3XX : 返回各 3 开头回源状态码明细数据;
        # 4XX : 返回各 4 开头回源状态码明细数据;
        # 5XX : 返回各 5 开头回源状态码明细数据;"}
        self.query_by = query_by

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
        if self.query_by is not None:
            result['queryBy'] = self.query_by
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
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":" Time format: yyyy-MM-dd HH:mm", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"The total number of back-to-source requests", "zh_CN":"回源总请求数"}
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


class ReportFlvStatusCodeRealTimeOriginTotalServiceResponseData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[ReportFlvStatusCodeRealTimeOriginTotalServiceResponseDataDetailList] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlvStatusCodeRealTimeOriginTotalServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlvStatusCodeRealTimeOriginTotalServiceResponseData] = None,
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
                temp_model = ReportFlvStatusCodeRealTimeOriginTotalServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlvStatusCodeRealTimeOriginTotalServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryISPProvinceStatusCodeRequest(TeaModel):
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
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2.Cannot exceed current time
        # 3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒)；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3.Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        # 4.Maximum allowed query time interval: 24 hours (with technical support adjustments), meaning that the difference between Date from and dateTo cannot exceed 24 hours.", "zh_CN":"结束时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒)
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：24小时(可联系技术支持调整)，即dateFrom和dateTo相差不能超过24小时。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1.The maximum number of TLDs that can be delivered is 20 by default (contact technical support adjustment);
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3.If left blank, all domain names will be obtained. If the total number of domain names exceeds the upper limit, an error will be reported.", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)；
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        # 3.若未填写默认查询全部域名，全部域名超出域名上限报错"}
        self.domain = domain
        # {"en":"Data granularity:  
        # 1.The default is 1m;
        # 2.Support 1m (1 minute), 5m (5 minutes)", "zh_CN":"数据粒度：
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
        # 1.Optional value StatusCode, 2XX, 3XX, 4XX, 5XX, No default statusCode
        # 2.StatusCode: returns the status code details;
        # 3.2XX:Returns the 2XX return status code summary and the 2 start return status code detail data;
        # 4.3XX:Returns the 2XX return status code summary and the 3 start return status code detail data;
        # 5.4XX:Returns the 2XX return status code summary and the 4 start return status code detail data;
        # 6.5XX:Returns the 2XX return status code summary and the 5 start return status code detail data;", "zh_CN":"查询维度:
        # 1.可选值 statusCode 2XX 3XX 4XX 5XX, 不传默认 statusCode
        # 2.statusCode ：返回请求状态码明细；
        # 3.2XX:返回 2XX 状态码汇总及各 2 开头状态码明细数据；
        # 4.3XX:返回 3XX 状态码汇总及各 2 开头状态码明细数据；
        # 5.4XX:返回 4XX 状态码汇总及各 4 开头状态码明细数据；
        # 6.5XX:返回 5XX 状态码汇总及各 5 开头状态码明细数据；"}
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


class QueryISPProvinceStatusCodeResponseDataStatusCodeDataListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time, in yyyy-MM-dd HH:MM", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Total number of  requests", "zh_CN":"总请求数"}
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


class QueryISPProvinceStatusCodeResponseDataStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[QueryISPProvinceStatusCodeResponseDataStatusCodeDataListDetailList] = None,
    ):
        # {"en":"StatusCode", "zh_CN":"状态码"}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = QueryISPProvinceStatusCodeResponseDataStatusCodeDataListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class QueryISPProvinceStatusCodeResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data_list: List[QueryISPProvinceStatusCodeResponseDataStatusCodeDataList] = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data_list is not None:
            result['statusCodeDataList'] = []
            for k in self.status_code_data_list:
                result['statusCodeDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeDataList') is not None:
            self.status_code_data_list = []
            for k in m.get('statusCodeDataList'):
                temp_model = QueryISPProvinceStatusCodeResponseDataStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class QueryISPProvinceStatusCodeResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryISPProvinceStatusCodeResponseData] = None,
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
                temp_model = QueryISPProvinceStatusCodeResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryISPProvinceStatusCodePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceStatusCodeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceStatusCodeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryISPProvinceStatusCodeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeRealTimeEdgeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {'en':'Start time:
        # 1. Start time: time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (December 2rd, 2016, 10:00 a.m., Beijing Time);
        # 2. Not greater than the current time
        # 3. The most recent half-year (183 days) data can be obtained', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00（为北京时间2019年01月01日10点0分0秒）；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据。'}
        self.date_from = date_from
        # {'en':'End time:
        # 1. The time format is 2016-12-02T10:00:00+08:00
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 1 hours will be queried by default; if one field is filled and one is left empty, then exception will occur.
        # 4. Maximum time range allowable for query: 1 hour, means the period between dateFrom to dateTo should not exceed 1 hour', 'zh_CN':'结束时间：
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的1小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：1小时（可联系技术支持调整），即dateFrom和dateTo相差不能超过1小时。'}
        self.date_to = date_to
        # {'en':'Domain:
        # 1. The default upper limit of domains that can be entered is 20 (if you want to adjust, please, contact technical support);
        # 2. Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3. Domain name exceeding limit, misstatement', 'zh_CN':'域名：
        # 1.可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）
        # 3.域名超过上限，报错'}
        self.domain = domain
        # {'en':'Data granularity:
        # 1. default 1m
        # 2. 1m (1 minute), 5m (5 minutes)', 'zh_CN':'数据粒度：不传默认1m
        # 1.支持1m（1分钟）、5m（5分钟）'}
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


class ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'DateTime, the format is   yyyy-MM-dd HH:mm; the data value of every time slice represents the data   value within the previous time granularity range.', 'zh_CN':'时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。比如yyyy-MM-dd 00:05，代表00:00到00:05范围内的数据。'}
        self.timestamp = timestamp
        # {'en':'Number of requests for status codes', 'zh_CN':'状态码对应的请求数'}
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


class ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeDataRequestData] = None,
    ):
        # {'en':'Status code', 'zh_CN':'状态码'}
        self.status_code = status_code
        # {'en':'requestData', 'zh_CN':'请求数数据'}
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeEdgeServiceResponseResult(TeaModel):
    def __init__(
        self,
        status_code_data: List[ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeData] = None,
    ):
        # {'en':'statusCodeData', 'zh_CN':'状态码数据'}
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = ReportStatusCodeRealTimeEdgeServiceResponseResultStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeEdgeServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportStatusCodeRealTimeEdgeServiceResponseResult] = None,
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
                temp_model = ReportStatusCodeRealTimeEdgeServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeEdgeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeEdgeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeEdgeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeEdgeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowProtocolStatusCodeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
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


class ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        https_value: str = None,
        http_value: str = None,
    ):
        # {"en":"timestamp,Returns the timestamp between the start time and end time. Time format: yyyy-MM-dd HH:mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。
        # 时间格式:
        # 5分钟:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"https", "zh_CN":"https数据"}
        self.https_value = https_value
        # {"en":"http", "zh_CN":"http数据"}
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


class ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataListDetailList] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolStatusCodeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data_list: List[ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataList] = None,
    ):
        # {"en":"Domain. If merge date of all domains will not return domain", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
        self.domain = domain
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data_list is not None:
            result['statusCodeDataList'] = []
            for k in self.status_code_data_list:
                result['statusCodeDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeDataList') is not None:
            self.status_code_data_list = []
            for k in m.get('statusCodeDataList'):
                temp_model = ReportFlowProtocolStatusCodeServiceResponseDataStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolStatusCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowProtocolStatusCodeServiceResponseData] = None,
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
                temp_model = ReportFlowProtocolStatusCodeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolStatusCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolStatusCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolStatusCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolStatusCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryStatusCodeDistributionOfeachISPandProvinceRequest(TeaModel):
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
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. can not exceed the current time;
        # 3. the latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. the end time is greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 4. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (technical support can be contacted to adjust). ", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间;
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 4.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain: when domain is not passed: default is all domain names, maximum supported domain names are 20 (can be adjusted by contacting technical support)", "zh_CN":"域名：当domain没有传时:默认为全部域名,最大域名支持20个(可联系技术支持调整)	"}
        self.domain = domain
        # {"en":"Data granularity, 1m: 1-minute 5m: 5-minute granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,1m: 1分钟粒度, 5m:5分钟粒度,1h:1小时粒度"}
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
        # {"en":"Group dimension
        # 
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
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


class QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time,
        #                                                                     1.When the data query granularity is 1m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 																	2.When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 																	3.When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        # 																	4.Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间,
        #                                                                     1.查询的数据粒度为1m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:01,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 																	2.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 																	3.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)00;
        # 																	4.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests of the status code", "zh_CN":"状态码对应的请求数"}
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


class QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData] = None,
    ):
        # {"en":"Return specific status code details such as 200, 201, 500, as well as aggregated 1XX, 2XX, 3XX, 4XX, 5XX, all, OTHERS. Return when values are available.", "zh_CN":"返回具体状态码明细如200,201,500，及聚合的1XX，2XX，3XX，4XX，5XX，all，OTHERS。有值时返回"}
        self.status_code = status_code
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        status_code_data: List[QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceDataStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceData] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspData] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryStatusCodeDistributionOfeachISPandProvinceResponseResult] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvincePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeLogServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
    ):
        # {'en':'From date:
        # 
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00.
        # 
        #  2.Cannot exceed current time
        # 
        # 3.The most recent six-month (183 days) data are available.', 'zh_CN':'开始时间：
        # 
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        # 
        # 2.不能大于当前时间
        # 
        # 3.最多可获取最近半年（183天）的数据'}
        self.date_from = date_from
        # {'en':'End time:
        # 
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. 
        # 
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 
        # 3.If both fields of dataFrom and dateTo are left empty,  the default query past 1 day; If there is only one unsent, throw an exception
        # 
        # 4.Maximum allowed query time interval: 30 days, Date from and dateTo, not more than 30 days', 'zh_CN':'结束时间：
        # 
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间
        # 
        # 3.dateFrom，dateTo二者都未传，默认查询过去的1天；如仅有一个未传，抛异常
        # 
        # 4.允许查询最大时间间隔：31天，即dateFrom和dateTo相差不能超过31天。（可联系技术支持调整）'}
        self.date_to = date_to
        # {'en':'Domain:
        # 
        # 1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support).
        # 
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)', 'zh_CN':'域名：
        # 
        # 1、可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 
        # 2、自动过滤掉无效域名（如传递非法域名，会被过滤掉，查询结果只返回有效域名的数据）。'}
        self.domain = domain
        # {'en':'1.Selection:domain
        # 2.If groupBy left empty, merge date of all domains', 'zh_CN':'1. 可选值：domain
        # 2. 不传默认聚合所有频道数据'}
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


class ReportStatusCodeLogServiceResponseDataStatusCodeDataListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'timestamp,Returns the timestamp between the start time and end time.Time format:
        #                                                                                  Hours: yyyy MM DD hh:00:00', 
        #                                                                                  'zh_CN':'时间片,返回开始时间和结束时间包含的时间片。
        #                                                                                  时间格式:
        #                                                                                  小时：yyyy-MM-dd HH:00:00'}
        self.timestamp = timestamp
        # {'en':'Status code times', 'zh_CN':'状态码次数'}
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


class ReportStatusCodeLogServiceResponseDataStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[ReportStatusCodeLogServiceResponseDataStatusCodeDataListDetailList] = None,
    ):
        # {'en':'Status code', 'zh_CN':'状态码'}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportStatusCodeLogServiceResponseDataStatusCodeDataListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportStatusCodeLogServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data_list: List[ReportStatusCodeLogServiceResponseDataStatusCodeDataList] = None,
    ):
        # {'en':'Domain. If merge date of all domains will not return domain', 'zh_CN':'域名，聚合全部域名数据不返回该字段'}
        self.domain = domain
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data_list is not None:
            result['statusCodeDataList'] = []
            for k in self.status_code_data_list:
                result['statusCodeDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeDataList') is not None:
            self.status_code_data_list = []
            for k in m.get('statusCodeDataList'):
                temp_model = ReportStatusCodeLogServiceResponseDataStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class ReportStatusCodeLogServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportStatusCodeLogServiceResponseData] = None,
    ):
        self.code = code
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
                temp_model = ReportStatusCodeLogServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeLogServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeLogServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeLogServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeLogServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
        is_status_merge: str = None,
    ):
        # {"en":"Start time
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. can not exceed the current time;
        # 3. the latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. the end time is greater than the start time. If the end time is greater than the current time, the current time is taken.
        # 3. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 4. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days (technical support can be contacted to adjust). ", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间;
        # 3.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 4.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain names, domain number limits can be adjusted depending on different accounts. The default value is 20", "zh_CN":"域名:可传递域名数量上限默认为20个(可联系技术支持调整),未传递视为全部域名，全部域名超出域名数量上限将报错"}
        self.domain = domain
        # {"en":"Data granularity, 1m: 1-minute 5m: 5-minute granularity, 1h: 1-hour granularity", "zh_CN":"数据粒度,1m: 1分钟粒度, 5m:5分钟粒度,1h:1小时粒度"}
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
        # 
        # 1.Options are domain, province, isp, and more than one value can be entered;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain、province、isp,可传入多个值;
        # 2.有传入则按照该维度展示明细数据;"}
        self.group_by = group_by
        # {"en":"Dimension of status code query:
        # 1. true: Status code aggregation return, return values are 2XX, 3XX, 4XX, 5XX, ALL, OTHER.
        # 2. false: Return detailed data based on specific status codes. isStatusMerge defaults to false when not passed.", "zh_CN":"状态码查询维度:
        # 1.true：状态码聚合返回，返回2XX,3XX,4XX,5XX,ALL,OTHER
        # 2.false：按具体状态码明细数据返回。不传默认为false"}
        self.is_status_merge = is_status_merge

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
        if self.is_status_merge is not None:
            result['isStatusMerge'] = self.is_status_merge
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
        if m.get('isStatusMerge') is not None:
            self.is_status_merge = m.get('isStatusMerge')
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time,
        # 																	1.When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        # 																	2.When the data query granularity is 1h, the format is yyyy-MM-dd HH; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 00:01, and the last one is (yyyy-MM-dd+1) 00;
        # 																	3.Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间,
        # 																	1.查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1)00:00;
        # 																	2.查询的数据粒度为1h时,格式为yyyy-MM-dd HH;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 01,最后一个时间片是(yyyy-MM-dd+1)00;
        # 																	3.返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Number of requests of the status code", "zh_CN":"状态码对应的请求数"}
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


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeDataRequestData] = None,
    ):
        # {"en":"Status codes, with options of: '200', '500' and 'Others'", "zh_CN":"状态码,取值可能为:'200'、'500'、'其他'等"}
        self.status_code = status_code
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        status_code_data: List[QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeData] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceDataStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceData] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspData] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResult] = None,
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
                temp_model = QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionOfeachISPandProvinceByUserIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryStatusCodeDistributionRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        group_by: List[str] = None,
        data_padding: bool = None,
        query_by: str = None,
    ):
        # {"en":"Start time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 7 days(technical support can be contacted to adjust);
        # 4.dateFrom and dateTo can be either both are specified or neither is specifies;
        # 5.If neither dateFrom nor dateTo is specified, then by default, data in the last 24 hour is queried", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于当前时间-183天，并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过7天(可联系技术支持调整)；
        # 4.dateFrom和dateTo要么都传递，要么都不传递；
        # 5.dateFrom和dateTo都未传递，则默认查询过去24小时的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；如果大于当前时间，则重新赋值为当前时间；"}
        self.date_to = date_to
        # {"en":"Domain names:
        # 1.Domain number limits can be adjusted depending on different accounts. The default value is 20
        # 2.Query all domain names under account when this entry is not passed", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)；
        # 2.未传递该入参时查询账号下所有域名"}
        self.domain = domain
        # {"en":"Data granularity, 5m: granularity of 5 minutes", "zh_CN":"数据粒度，5m：5分钟粒度"}
        self.data_interval = data_interval
        # {"en":"Group dimension
        # 1.The value can be selected is domain;
        # 2.The data is displayed according to the specified dimension;", "zh_CN":"分组维度
        # 1.可选值为domain；
        # 2.有传入则按照该维度展示明细数据；"}
        self.group_by = group_by
        # {"en":"1.If 0 is added, the value is true or false, which is false by default
        # 2.When the value of data adding is true, data is added to time points without data
        # 3.When the dataPadding value is false, no treatment will be done", "zh_CN":"是否补0，取值为true或false，默认为false
        # 当dataPadding取值为true时，对没有数据的时间点填充数据，取值为0
        # 当dataPadding取值为false时，不做处理"}
        self.data_padding = data_padding
        # {"en":"Query dimension. Optional values: statusCode, statusCodeType. Default value is statuscode.
        # 1.statusCode: returns the status code details;
        # 2.statusCodeType: returns the requests of eachstatus code type (such as the number of requests corresponding to success, redirect, not modified, permission, not found, server error, and other)", "zh_CN":"查询维度，可选值：statusCode、statusCodeType；不传默认statusCode
        # 1.statusCode ：返回状态码明细；
        # 2.statusCodeType：返回状态码类型对应明细(如Success、Redirect、Not-Modified、Permission、Not-Found、Server Error、Other对应的请求数)"}
        self.query_by = query_by

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
        if self.data_padding is not None:
            result['dataPadding'] = self.data_padding
        if self.query_by is not None:
            result['queryBy'] = self.query_by
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
        if m.get('dataPadding') is not None:
            self.data_padding = m.get('dataPadding')
        if m.get('queryBy') is not None:
            self.query_by = m.get('queryBy')
        return self


class QueryStatusCodeDistributionResponseResultStatusCodeDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"DateTime, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range.", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm；每一个时间片数据值代表的是前一个时间粒度范围内的数据值。比如yyyy-MM-dd 00:05，代表00:00到00:05范围内的数据。"}
        self.timestamp = timestamp
        # {"en":"Number of requests for status codes", "zh_CN":"状态码对应的请求数"}
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


class QueryStatusCodeDistributionResponseResultStatusCodeData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        total_request: str = None,
        status_code_type: str = None,
        request_data: List[QueryStatusCodeDistributionResponseResultStatusCodeDataRequestData] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        # {"en":"totalRequest", "zh_CN":"总请求数"}
        self.total_request = total_request
        # {"en":"Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other", "zh_CN":"Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other"}
        self.status_code_type = status_code_type
        # {"en":"requestData", "zh_CN":"请求数数据"}
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.total_request, 'total_request')
        self.validate_required(self.status_code_type, 'status_code_type')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.total_request is not None:
            result['totalRequest'] = self.total_request
        if self.status_code_type is not None:
            result['statusCodeType'] = self.status_code_type
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('totalRequest') is not None:
            self.total_request = m.get('totalRequest')
        if m.get('statusCodeType') is not None:
            self.status_code_type = m.get('statusCodeType')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = QueryStatusCodeDistributionResponseResultStatusCodeDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data: List[QueryStatusCodeDistributionResponseResultStatusCodeData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"statusCodeData", "zh_CN":"状态码数据"}
        self.status_code_data = status_code_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data, 'status_code_data')
        if self.status_code_data:
            for k in self.status_code_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data is not None:
            result['statusCodeData'] = []
            for k in self.status_code_data:
                result['statusCodeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeData') is not None:
            self.status_code_data = []
            for k in m.get('statusCodeData'):
                temp_model = QueryStatusCodeDistributionResponseResultStatusCodeData()
                self.status_code_data.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryStatusCodeDistributionResponseResult] = None,
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
                temp_model = QueryStatusCodeDistributionResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryStatusCodeDistributionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryStatusCodeDistributionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusAllServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusAllServiceResponseStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        hit: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        # {"en":"Number of requests of the status   code", "zh_CN":"状态码对应的请求数"}
        self.hit = hit

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.hit, 'hit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['status-code'] = self.status_code
        if self.hit is not None:
            result['hit'] = self.hit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status-code') is not None:
            self.status_code = m.get('status-code')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        return self


class ReportStatusAllServiceResponse(TeaModel):
    def __init__(
        self,
        status_code_data_list: List[ReportStatusAllServiceResponseStatusCodeDataList] = None,
    ):
        # {'en':'statusCodeData', 'zh_CN':'状态码汇总'}
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code_data_list is not None:
            result['status-code-data'] = []
            for k in self.status_code_data_list:
                result['status-code-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status-code-data') is not None:
            self.status_code_data_list = []
            for k in m.get('status-code-data'):
                temp_model = ReportStatusAllServiceResponseStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class ReportStatusAllServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusAllServiceParameters(TeaModel):
    def __init__(
        self,
        datefrom: str = None,
        dateto: str = None,
    ):
        # {"en":"start time
        # 
        # The 1. format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2. must be less than the current time and dateto;
        # 
        # The difference between 3.dateFrom and dateTo should not exceed 31 days (with technical support adjustment).
        # 
        # 4. we can only query data in the latest 2 years.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须小于当前时间和dateto；
        # 3.dateFrom和dateTo相差不能超过31天（可联系技术支持调整）；
        # 4.只能查询最近2年内数据。"}
        self.datefrom = datefrom
        # {"en":"End time
        # 
        # 1.        The   format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.        Must   be greater than datefrom; if it’s greater than the current time, then the   current time is assigned as the value;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于datefrom；如果大于当前时间，则重新赋值为当前时间；"}
        self.dateto = dateto

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datefrom') is not None:
            self.datefrom = m.get('datefrom')
        if m.get('dateto') is not None:
            self.dateto = m.get('dateto')
        return self


class ReportStatusAllServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusAllServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeUrlTopServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: str = None,
        status_code: str = None,
        top: int = None,
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
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days.", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：7天，即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to
        # {"en":"Domain
        # 
        # Can only transfer one domain.", "zh_CN":"域名：
        # 
        # 只能传一个域名"}
        self.domain = domain
        # {"en":"Status code
        # 
        # Support transmitting specific status codes, such as 201/202, or summarizing status codes 1XX/2XX/3XX/4XX/5XX", "zh_CN":"状态码
        # 
        # 支持传具体状态码，如201，202、或者是汇总状态码1XX/2XX/3XX/4XX/5XX"}
        self.status_code = status_code
        # {"en":"Default top 200, maximum input 1000", "zh_CN":"不传默认top200，最多输入1000"}
        self.top = top

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code, 'status_code')

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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
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
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('top') is not None:
            self.top = m.get('top')
        return self


class ReportStatusCodeUrlTopServiceResponseData(TeaModel):
    def __init__(
        self,
        url: str = None,
        value: str = None,
    ):
        # {"en":"url", "zh_CN":"URL"}
        self.url = url
        # {"en":"Number of requests", "zh_CN":"请求数"}
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


class ReportStatusCodeUrlTopServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportStatusCodeUrlTopServiceResponseData] = None,
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
                temp_model = ReportStatusCodeUrlTopServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeUrlTopServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeUrlTopServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeUrlTopServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeUrlTopServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportFlowProtocolOneMinStatusCodeServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
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
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"1.Selection:domain 
        # 	2.If groupBy left empty, merge date of all domains", "zh_CN":"1.可选值:domain
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


class ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataListDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        https_value: str = None,
        http_value: str = None,
    ):
        # {"en":"timestamp,Returns the timestamp between the start time and end time. Time format: yyyy-MM-dd HH:mm", "zh_CN":"时间片,返回开始时间和结束时间包含的时间片。时间格式:1分钟:yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"https", "zh_CN":"https数据"}
        self.https_value = https_value
        # {"en":"http", "zh_CN":"http数据"}
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


class ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataList(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        detail_list: List[ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataListDetailList] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.status_code = status_code
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolOneMinStatusCodeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status_code_data_list: List[ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataList] = None,
    ):
        # {"en":"Domain. If merge date of all domains will not return domain", "zh_CN":"域名,聚合全部域名数据不返回该字段"}
        self.domain = domain
        self.status_code_data_list = status_code_data_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.status_code_data_list, 'status_code_data_list')
        if self.status_code_data_list:
            for k in self.status_code_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status_code_data_list is not None:
            result['statusCodeDataList'] = []
            for k in self.status_code_data_list:
                result['statusCodeDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('statusCodeDataList') is not None:
            self.status_code_data_list = []
            for k in m.get('statusCodeDataList'):
                temp_model = ReportFlowProtocolOneMinStatusCodeServiceResponseDataStatusCodeDataList()
                self.status_code_data_list.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolOneMinStatusCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportFlowProtocolOneMinStatusCodeServiceResponseData] = None,
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
                temp_model = ReportFlowProtocolOneMinStatusCodeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportFlowProtocolOneMinStatusCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolOneMinStatusCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolOneMinStatusCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportFlowProtocolOneMinStatusCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRealTimeOriginStatusCodeRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        query_by: str = None,
    ):
        # {"en":"Start date:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2.Cannot exceed current time
        # 3.The most recent six-month (183 days) data are available.", "zh_CN":"开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒)；
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00.For example, 2019-01-01T10:00:00+08:00
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3.Date from, Date to both, the default query past 24 hours; If there is only one unsent, throw an exception
        # 4.The default maximum query time interval is 24 hours (you can contact technical support to adjust it, up to 31 days)", "zh_CN":"结束时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2019-01-01T10:00:00+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间。
        # 3.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常
        # 4.默认允许查询最大时间间隔：24小时(可联系技术支持调整，最大31天)"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1.The maximum number of TLDs that can be delivered is 20 by default (contact technical support adjustment);
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3.Domain name exceeding limit, misstatement", "zh_CN":"域名：
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整)；
        # 2.自动过滤掉非法域名(如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据)
        # 3.域名超过上限，报错"}
        self.domain = domain
        # {"en":"Data granularity:  
        # 1.The default is 1m ;
        # 2.Support 1m (1 minute), 5m (5 minutes)", "zh_CN":"数据粒度：
        # 1.不传默认1m
        # 2.支持1m(1分钟)、5m(5分钟)"}
        self.data_interval = data_interval
        # {"en":"Query dimension:
        # 1.Optional value statusCode, statusCodeType, 2XX, 3XX, 4XX, 5XX. Default value is statusCode;
        # 2.StatusCode: returns the source status code details
        # 3.statusCodeType: returns the requests of eachstatus code type (such as the number of requests corresponding to success, redirect, not modified, permission, not found, server error, and other)
        # 4.2XX:Returns the 2XX return source status code summary and the 2 start return source status code detail data;
        # 5.3XX:Returns the 2XX return source status code summary and the 3 start return source status code detail data;
        # 6.4XX:Returns the 2XX return source status code summary and the 4 start return source status code detail data;
        # 7.5XX:Returns the 2XX return source status code summary and the 5 start return source status code detail data;", "zh_CN":"查询维度:
        # 1.可选值 statusCode，statusCodeType， 2XX ，3XX， 4XX， 5XX，不传默认 statusCode
        # 2.statusCode: 返回回源状态码明细；
        # 3.statusCodeType：返回状态码类型对应明细(如Success、Redirect、Not-Modified、Permission、Not-Found、Server Error、Other对应的请求数)
        # 4.2XX : 返回 2XX 回源状态码汇总及各 2 开头回源状态码明细数据；
        # 5.3XX : 返回 3XX 回源状态码汇总及各 2 开头回源状态码明细数据；
        # 6.4XX : 返回 4XX 回源状态码汇总及各 4 开头回源状态码明细数据；
        # 7.5XX : 返回 5XX回源状态码汇总及各 5 开头回源状态码明细数据；"}
        self.query_by = query_by

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
        if self.query_by is not None:
            result['queryBy'] = self.query_by
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
        return self


class QueryRealTimeOriginStatusCodeResponseData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"time, in yyyy-MM-dd HH:MM", "zh_CN":"时间，格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"Total number of return requests", "zh_CN":"回源总请求数"}
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


class QueryRealTimeOriginStatusCodeResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryRealTimeOriginStatusCodeResponseData] = None,
        status_code: str = None,
        status_code_type: str = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
        self.data = data
        # {"en":"StatusCode", "zh_CN":"状态码"}
        self.status_code = status_code
        # {"en":"Success, Redirect, Not-Modified, Permission, Not-Found, Server Error, Other", "zh_CN":"Success、Redirect、Not-Modified、Permission、Not-Found、Server Error、Other"}
        self.status_code_type = status_code_type

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.status_code_type, 'status_code_type')

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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_code_type is not None:
            result['statusCodeType'] = self.status_code_type
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
                temp_model = QueryRealTimeOriginStatusCodeResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusCodeType') is not None:
            self.status_code_type = m.get('statusCodeType')
        return self


class QueryRealTimeOriginStatusCodePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeOriginStatusCodeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeOriginStatusCodeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRealTimeOriginStatusCodeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStatusCodeRealTimeOriginServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
    ):
        # {"en":"Start time
        # 1.The time format is yyyy-MM-ddTHH:mm:ss+08:00, for example, 2016-12-02T10:00:00+08:00 (for Beijing time, December 2, 2016, 10:00:00);
        # 2.Cannot be greater than the current time
        # 3.Get up to the last six months (183 days) of data.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2019-01-01T10:00:00+08:00(为北京时间2019年01月01日10点0分0秒);
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom; if it's greater than the current time, then the current time is assigned as the value;
        # 3.If both fields of dataFrom and dateTo are left empty, then data in the last 1 hours will be queried by default;
        # 4.Allowable maximum time range for query: 1 hour, means the period between dateFrom to dateTo should not exceed 1 hour (can be adjusted by contacting technical support up to 31 days)", "zh_CN":"结束时间:
        # 1.时间格式2016-12-02T10:00:00+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        # 3.dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:1小时(可联系技术支持调整),即dateFrom和dateTo相差不能超过1小时。"}
        self.date_to = date_to
        # {"en":"Domain:
        # 1.The default upper limit to domains that can be entered is 200 (Contact technical support to adjust);
        # 2.Automatically filter out illegal domains (illegal domains will be filtered out, the query results only return the data of legitimate domains)", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为20个(可联系技术支持调整);
        # 2.自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 3.域名超过上限,报错"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. Support 1m (1 minute granularity),5m (5 minutes granularity)
        # 2. The default value is 1m", "zh_CN":"数据粒度:不传默认1m
        # 1. 支持1m(1分钟)、5m(5分钟)"}
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


class ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginDataRequestData(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"The data granularity is 1 minute, and the format is yyyy MM dd HH: mm", "zh_CN":"数据粒度为1分钟,格式为yyyy-MM-dd HH:mm;"}
        self.timestamp = timestamp
        # {"en":"Requests of back to origin status code", "zh_CN":"回源状态码请求数"}
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


class ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginData(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        request_data: List[ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginDataRequestData] = None,
    ):
        # {"en":"Back to origin status code type", "zh_CN":"回源状态码类型"}
        self.status_code = status_code
        self.request_data = request_data

    def validate(self):
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.request_data is not None:
            result['requestData'] = []
            for k in self.request_data:
                result['requestData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('requestData') is not None:
            self.request_data = []
            for k in m.get('requestData'):
                temp_model = ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginDataRequestData()
                self.request_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeOriginServiceResponseResult(TeaModel):
    def __init__(
        self,
        status_code_origin_data: List[ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginData] = None,
    ):
        self.status_code_origin_data = status_code_origin_data

    def validate(self):
        self.validate_required(self.status_code_origin_data, 'status_code_origin_data')
        if self.status_code_origin_data:
            for k in self.status_code_origin_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code_origin_data is not None:
            result['statusCodeOriginData'] = []
            for k in self.status_code_origin_data:
                result['statusCodeOriginData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCodeOriginData') is not None:
            self.status_code_origin_data = []
            for k in m.get('statusCodeOriginData'):
                temp_model = ReportStatusCodeRealTimeOriginServiceResponseResultStatusCodeOriginData()
                self.status_code_origin_data.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeOriginServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportStatusCodeRealTimeOriginServiceResponseResult] = None,
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
                temp_model = ReportStatusCodeRealTimeOriginServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportStatusCodeRealTimeOriginServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeOriginServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeOriginServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStatusCodeRealTimeOriginServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




