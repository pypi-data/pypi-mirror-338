# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryDomainLogDownloadAddressDomainList(TeaModel):
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


class QueryDomainLogDownloadAddressRequest(TeaModel):
    def __init__(
        self,
        domain_list: QueryDomainLogDownloadAddressDomainList = None,
        datefrom: str = None,
        dateto: str = None,
        log_type: str = None,
        area_code: str = None,
    ):
        # {"en":"Domain list:
        #     1.All domains will be queried if this field is not specified;
        #     2.The default upper limit of the number of domain names is 20 (you can contact technical support for adjustment), The maximum recommended cap is 500 .", "zh_CN":"域名列表:
        #     1.不传递则查询全部域名;
        #     2.域名数量默认上限为20个(可联系技术支持调整), 最大上限为500."}
        self.domain_list = domain_list
        # {"en":"Start time:
        #     1.The format is yyyy-MM-ddTHH:mm:ss+08:00 ;
        #     2.Must be smaller than the current time and dateTo ;
        #     3.Period between dataFrom and dateTo cannot be longer than 31 days .", "zh_CN":"开始时间:
        #     1.格式为yyyy-MM-ddTHH:mm:ss+08:00 ;
        #     2.必须小于当前时间和dateTo ;
        #     3.dateFrom和dateTo相差不能超过31天(可联系技术支持调整) ;
        #     4.只能查询最近2年内数据.(实际可查询的日志范围,取决于域名配置的日志保留天数) ."}
        self.datefrom = datefrom
        # {"en":"End time, format is yyyy-MM-ddTHH:mm:ss+08:00(The actual range of logs that can be queried depends on the number of days of log retention configured by the domain name).", "zh_CN":"结束时间,格式为yyyy-MM-ddTHH:mm:ss+08:00(实际可查询的日志范围,取决于域名配置的日志保留天数)."}
        self.dateto = dateto
        # {"en":"Log type, optional values:cdn,bot,ddos;Multiple are separated by English commas. If they are not transmitted, the data will be queried by logtype = cdn,bot by default.", "zh_CN":"日志类型,可选值: cdn,bot,ddos ;
        # 多个通过英文逗号分隔,若未传则默认按logtype=cdn,bot查询数据"}
        self.log_type = log_type
        # {"en":"areaCode", "zh_CN":"加速区域"}
        self.area_code = area_code

    def validate(self):
        if self.domain_list:
            self.domain_list.validate()
        self.validate_required(self.datefrom, 'datefrom')
        self.validate_required(self.dateto, 'dateto')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domain-list'] = self.domain_list.to_map()
        if self.datefrom is not None:
            result['datefrom'] = self.datefrom
        if self.dateto is not None:
            result['dateto'] = self.dateto
        if self.log_type is not None:
            result['logType'] = self.log_type
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-list') is not None:
            temp_model = QueryDomainLogDownloadAddressDomainList()
            self.domain_list = temp_model.from_map(m['domain-list'])
        if m.get('datefrom') is not None:
            self.datefrom = m.get('datefrom')
        if m.get('dateto') is not None:
            self.dateto = m.get('dateto')
        if m.get('logType') is not None:
            self.log_type = m.get('logType')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        return self


class QueryDomainLogDownloadAddressResponseLogsFiles(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        log_url: str = None,
        file_size: int = None,
    ):
        # {"en":"The start time of log file, format is yyyy-MM-dd-HHmm", "zh_CN":"日志文件的开始时间,格式为yyyy-MM-dd-HHmm"}
        self.date_from = date_from
        # {"en":"The end time of log file, format is yyyy-MM-dd-HHmm", "zh_CN":"日志文件的结束时间,格式为yyyy-MM-dd-HHmm"}
        self.date_to = date_to
        # {"en":"Download address of log file", "zh_CN":"日志文件下载地址"}
        self.log_url = log_url
        # {"en":"Size of log file", "zh_CN":"日志文件大小"}
        self.file_size = file_size

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.log_url, 'log_url')
        self.validate_required(self.file_size, 'file_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class QueryDomainLogDownloadAddressResponseLogs(TeaModel):
    def __init__(
        self,
        domain: str = None,
        area_code: str = None,
        files: List[QueryDomainLogDownloadAddressResponseLogsFiles] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"areaCode", "zh_CN":"加速区域"}
        self.area_code = area_code
        self.files = files

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.area_code, 'area_code')
        self.validate_required(self.files, 'files')
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        if self.files is not None:
            result['files'] = []
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('files') is not None:
            self.files = []
            for k in m.get('files'):
                temp_model = QueryDomainLogDownloadAddressResponseLogsFiles()
                self.files.append(temp_model.from_map(k))
        return self


class QueryDomainLogDownloadAddressResponse(TeaModel):
    def __init__(
        self,
        logs: List[QueryDomainLogDownloadAddressResponseLogs] = None,
    ):
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
                temp_model = QueryDomainLogDownloadAddressResponseLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class QueryDomainLogDownloadAddressPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainLogDownloadAddressParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainLogDownloadAddressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainLogDownloadAddressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTranscodingDurationLogDownloadAddressRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
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
        # 5. Maximum query interval allowed: 7 days, that is, the difference between dateFrom and dateTo can not exceed 7 days. ", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.允许查询最大间隔:7天,即dateFrom和dateTo相差不能超过7天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 
        # 1.Domain is not uploaded: Query all domain names of the account (More than 100 domains will error,you can contact technical support for adjustment);
        # 
        # 2.Domain is uploaded: Up to 100 domains are supported(you can contact technical support for adjustment).", "zh_CN":"域名:
        # 
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)。"}
        self.domain = domain

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


class QueryTranscodingDurationLogDownloadAddressResponseResultFileData(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        log_url: str = None,
        url_expire_time: str = None,
        file_name: str = None,
        file_size: int = None,
    ):
        # {"en":"The start time of log file, format is yyyy-MM-dd-HHmm", "zh_CN":"日志文件的开始时间,格式为yyyy-MM-dd-HHmm"}
        self.date_from = date_from
        # {"en":"The end time of log file, format is yyyy-MM-dd-HHmm", "zh_CN":"日志文件的结束时间,格式为yyyy-MM-dd-HHmm"}
        self.date_to = date_to
        # {"en":"Download address of log file", "zh_CN":"日志文件下载地址"}
        self.log_url = log_url
        # {"en":"Expire time", "zh_CN":"日志文件下载地址过期时间"}
        self.url_expire_time = url_expire_time
        # {"en":"File name", "zh_CN":"文件名"}
        self.file_name = file_name
        # {"en":"Size of log file", "zh_CN":"日志文件大小,单位:Byte"}
        self.file_size = file_size

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.log_url, 'log_url')
        self.validate_required(self.url_expire_time, 'url_expire_time')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_size, 'file_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.url_expire_time is not None:
            result['urlExpireTime'] = self.url_expire_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('urlExpireTime') is not None:
            self.url_expire_time = m.get('urlExpireTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class QueryTranscodingDurationLogDownloadAddressResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        file_data: List[QueryTranscodingDurationLogDownloadAddressResponseResultFileData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        self.file_data = file_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.file_data, 'file_data')
        if self.file_data:
            for k in self.file_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.file_data is not None:
            result['fileData'] = []
            for k in self.file_data:
                result['fileData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('fileData') is not None:
            self.file_data = []
            for k in m.get('fileData'):
                temp_model = QueryTranscodingDurationLogDownloadAddressResponseResultFileData()
                self.file_data.append(temp_model.from_map(k))
        return self


class QueryTranscodingDurationLogDownloadAddressResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryTranscodingDurationLogDownloadAddressResponseResult] = None,
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
                temp_model = QueryTranscodingDurationLogDownloadAddressResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryTranscodingDurationLogDownloadAddressPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTranscodingDurationLogDownloadAddressParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTranscodingDurationLogDownloadAddressRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTranscodingDurationLogDownloadAddressResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




