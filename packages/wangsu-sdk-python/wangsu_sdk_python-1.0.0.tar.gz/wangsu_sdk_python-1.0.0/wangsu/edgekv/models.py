# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetShortUrlRequest(TeaModel):
    def __init__(
        self,
        short_url: str = None,
    ):
        # {'en':'ShortUrl', 'zh_CN':'短网址'}
        self.short_url = short_url

    def validate(self):
        self.validate_required(self.short_url, 'short_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class GetShortUrlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        long_url: str = None,
    ):
        # {'en':'Code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'Msg', 'zh_CN':'返回信息'}
        self.msg = msg
        # {'en':'LongUrl', 'zh_CN':'长网址'}
        self.long_url = long_url

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.long_url, 'long_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.long_url is not None:
            result['LongUrl'] = self.long_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('LongUrl') is not None:
            self.long_url = m.get('LongUrl')
        return self


class GetShortUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetShortUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetShortUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetShortUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetKeyValueKeyValue(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        exp: int = None,
    ):
        # {'en':'key', 'zh_CN':'key'}
        self.key = key
        # {'en':'value,base64 encoded', 'zh_CN':'base64 encode过的value'}
        self.value = value
        # {'en':'expiration', 'zh_CN':'过期时间，unix 时间戳'}
        self.exp = exp

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')
        self.validate_required(self.exp, 'exp')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.exp is not None:
            result['exp'] = self.exp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('exp') is not None:
            self.exp = m.get('exp')
        return self


class GetKeyValueRequest(TeaModel):
    def __init__(
        self,
        space_name: str = None,
        key: str = None,
    ):
        # {'en':'spaceName', 'zh_CN':'空间名称'}
        self.space_name = space_name
        # {'en':'key to query', 'zh_CN':'要查询的key'}
        self.key = key

    def validate(self):
        self.validate_required(self.space_name, 'space_name')
        self.validate_required(self.key, 'key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class GetKeyValueResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        result: GetKeyValueKeyValue = None,
    ):
        # {'en':'code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'返回信息'}
        self.msg = msg
        # {'en':'result', 'zh_CN':'结果'}
        self.result = result

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.result, 'result')
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('result') is not None:
            temp_model = GetKeyValueKeyValue()
            self.result = temp_model.from_map(m['result'])
        return self


class GetKeyValuePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetKeyValueParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetKeyValueRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetKeyValueResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteKeyValueRequest(TeaModel):
    def __init__(
        self,
        space_name: str = None,
        keys: List[str] = None,
    ):
        # {'en':'spaceName', 'zh_CN':'空间名称'}
        self.space_name = space_name
        # {'en':'keys to delete', 'zh_CN':'要删除的key'}
        self.keys = keys

    def validate(self):
        self.validate_required(self.space_name, 'space_name')
        self.validate_required(self.keys, 'keys')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.keys is not None:
            result['keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        return self


class DeleteKeyValueResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
    ):
        # {'en':'code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'返回信息'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteKeyValuePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteKeyValueParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteKeyValueRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteKeyValueResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SharkletVisitRequest(TeaModel):
    def __init__(
        self,
        u: str = None,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        timezone: str = None,
        return_type: str = None,
        datasource: str = None,
    ):
        # {"en":"login name.", "zh_CN":"主账号登录名"}
        self.u = u
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
        # {"en":"Greenwich TimeZone. The parameter format is GMT+09:00 for East 9th District, GMT-09:00 for West 9th District. If not specified, the default is the local time zone (East 8th District).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"Whether to aggregate in a specific way, format: number_day|hour. For example, 3_hour means aggregation in 3 hours; 2_day means aggregation in 2 days", "zh_CN":"是否按照特定方式聚合,格式 :  数字_day|hour .例如 3_hour表示按照3小时聚合; 2_day表示按照2天聚合"}
        self.return_type = return_type
        # {"en":"Data source 0: Get sharklet request count information; 1: Get serverless request count information. If not filled in, the default value is 0. When datasource=1, the Input SharkletVisitParameters channel is invalid", "zh_CN":"数据源 0:获取sharklet请求数信息; 1:获取serverless请求数信息. 不填默认为:0。当datasource=1的时候，入参channel无效"}
        self.datasource = datasource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.u is not None:
            result['u'] = self.u
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
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.return_type is not None:
            result['returnType'] = self.return_type
        if self.datasource is not None:
            result['datasource'] = self.datasource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('u') is not None:
            self.u = m.get('u')
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
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('returnType') is not None:
            self.return_type = m.get('returnType')
        if m.get('datasource') is not None:
            self.datasource = m.get('datasource')
        return self


class SharkletVisitResponseProviderDateChartDataListData(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'请求数'}
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


class SharkletVisitResponseProviderDateChartDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        data: List[SharkletVisitResponseProviderDateChartDataListData] = None,
    ):
        # {'en':'channel', 'zh_CN':'请求数'}
        self.name = name
        # {'en':'data', 'zh_CN':'请求数明细'}
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
                temp_model = SharkletVisitResponseProviderDateChartDataListData()
                self.data.append(temp_model.from_map(k))
        return self


class SharkletVisitResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        total_hit_total: str = None,
        base_app_hit_total: str = None,
        normal_app_hit_total: str = None,
        special_app_hit_total: str = None,
        chart_data_list: List[SharkletVisitResponseProviderDateChartDataList] = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'totalHitTotal', 'zh_CN':'总请求数'}
        self.total_hit_total = total_hit_total
        # {'en':'baseAppHitTotal', 'zh_CN':'基础应用请求数'}
        self.base_app_hit_total = base_app_hit_total
        # {'en':'normalAppHitTotal', 'zh_CN':'中型应用请求数'}
        self.normal_app_hit_total = normal_app_hit_total
        # {'en':'specialAppHitTotal', 'zh_CN':'特殊应用请求数	'}
        self.special_app_hit_total = special_app_hit_total
        # {'en':'chartDataList', 'zh_CN':'请求数分类'}
        self.chart_data_list = chart_data_list

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.total_hit_total, 'total_hit_total')
        self.validate_required(self.base_app_hit_total, 'base_app_hit_total')
        self.validate_required(self.normal_app_hit_total, 'normal_app_hit_total')
        self.validate_required(self.special_app_hit_total, 'special_app_hit_total')
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
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.total_hit_total is not None:
            result['totalHitTotal'] = self.total_hit_total
        if self.base_app_hit_total is not None:
            result['baseAppHitTotal'] = self.base_app_hit_total
        if self.normal_app_hit_total is not None:
            result['normalAppHitTotal'] = self.normal_app_hit_total
        if self.special_app_hit_total is not None:
            result['specialAppHitTotal'] = self.special_app_hit_total
        if self.chart_data_list is not None:
            result['chartDataList'] = []
            for k in self.chart_data_list:
                result['chartDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('totalHitTotal') is not None:
            self.total_hit_total = m.get('totalHitTotal')
        if m.get('baseAppHitTotal') is not None:
            self.base_app_hit_total = m.get('baseAppHitTotal')
        if m.get('normalAppHitTotal') is not None:
            self.normal_app_hit_total = m.get('normalAppHitTotal')
        if m.get('specialAppHitTotal') is not None:
            self.special_app_hit_total = m.get('specialAppHitTotal')
        if m.get('chartDataList') is not None:
            self.chart_data_list = []
            for k in m.get('chartDataList'):
                temp_model = SharkletVisitResponseProviderDateChartDataList()
                self.chart_data_list.append(temp_model.from_map(k))
        return self


class SharkletVisitResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: SharkletVisitResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'date', 'zh_CN':'边缘应用请求数'}
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
            temp_model = SharkletVisitResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class SharkletVisitResponse(TeaModel):
    def __init__(
        self,
        provider: SharkletVisitResponseProvider = None,
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
            temp_model = SharkletVisitResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class SharkletVisitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SharkletVisitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SharkletVisitRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SharkletVisitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EcaKvInfoRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        region: str = None,
        space: str = None,
        timezone: str = None,
        dataformat: str = None,
        datatype: str = None,
        return_type: str = None,
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
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"Space names, multiple names should be separated by a semicolon ';'.", "zh_CN":"空间名称，多个请用英文分号“;”分隔开。"}
        self.space = space
        # {"en":"Greenwich Mean Time (GMT) zone, the parameter format is GMT+09:00 to indicate East 9th Zone, and GMT-09:00 to indicate West 9th Zone. If not provided, the default is the local time zone (East 8th Zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"Return result format, supported formats are XML and JSON, default is XML.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"4 types. 0: Storage capacity; 1: Read request count; 2: Write request count; 3: Delete request count. Default is: 0.", "zh_CN":"4种类型。0：存储量；1：读请求数；2：写请求数；3：删请求数。默认取：0"}
        self.datatype = datatype
        # {"en":"Whether to aggregate in a specific manner, format: number_day|hour. For example, 3_hour means to aggregate by 3 hours; 2_day means to aggregate by 2 days.", "zh_CN":"是否按照特定方式聚合,格式 :  数字_day|hour .例如 3_hour表示按照3小时聚合; 2_day表示按照2天聚合"}
        self.return_type = return_type

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
        if self.region is not None:
            result['region'] = self.region
        if self.space is not None:
            result['space'] = self.space
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.datatype is not None:
            result['datatype'] = self.datatype
        if self.return_type is not None:
            result['returnType'] = self.return_type
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
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('space') is not None:
            self.space = m.get('space')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('datatype') is not None:
            self.datatype = m.get('datatype')
        if m.get('returnType') is not None:
            self.return_type = m.get('returnType')
        return self


class EcaKvInfoResponse(TeaModel):
    def __init__(
        self,
        provider: str = None,
        peak_time: str = None,
        peak_value: str = None,
        peak_avg_value: str = None,
        total_hit: str = None,
        time: str = None,
        text: str = None,
    ):
        # {"en":"provider", "zh_CN":"结果"}
        self.provider = provider
        # {"en":"Peak time", "zh_CN":"峰值时间"}
        self.peak_time = peak_time
        # {"en":"Peak, unit GB", "zh_CN":"峰值，单位GB"}
        self.peak_value = peak_value
        # {"en":"Peak average, unit GB", "zh_CN":"峰值平均，单位GB"}
        self.peak_avg_value = peak_avg_value
        # {"en":"total hits", "zh_CN":"总请求数"}
        self.total_hit = total_hit
        # {"en":"Time point, format yyyy-mm-dd hh:MM:ss", "zh_CN":"时间点，格式yyyy-mm-dd hh:MM:ss"}
        self.time = time
        # {"en":"Value corresponding to the time point", "zh_CN":"时间点对应的值"}
        self.text = text

    def validate(self):
        self.validate_required(self.provider, 'provider')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_avg_value, 'peak_avg_value')
        self.validate_required(self.total_hit, 'total_hit')
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['provider'] = self.provider
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_avg_value is not None:
            result['peakAvgValue'] = self.peak_avg_value
        if self.total_hit is not None:
            result['totalHit'] = self.total_hit
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakAvgValue') is not None:
            self.peak_avg_value = m.get('peakAvgValue')
        if m.get('totalHit') is not None:
            self.total_hit = m.get('totalHit')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class EcaKvInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EcaKvInfoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EcaKvInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EcaKvInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateShortUrlShortUrl(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        short_url: str = None,
        long_url: str = None,
    ):
        # {'en':'Code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'Msg', 'zh_CN':'返回信息'}
        self.msg = msg
        # {'en':'CreateShortUrlShortUrl', 'zh_CN':'短网址'}
        self.short_url = short_url
        # {'en':'LongUrl', 'zh_CN':'长网址（原网址）'}
        self.long_url = long_url

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.short_url, 'short_url')
        self.validate_required(self.long_url, 'long_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.short_url is not None:
            result['CreateShortUrlShortUrl'] = self.short_url
        if self.long_url is not None:
            result['LongUrl'] = self.long_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('CreateShortUrlShortUrl') is not None:
            self.short_url = m.get('CreateShortUrlShortUrl')
        if m.get('LongUrl') is not None:
            self.long_url = m.get('LongUrl')
        return self


class CreateShortUrlRequest(TeaModel):
    def __init__(
        self,
        long_urls: List[str] = None,
        ttl: int = None,
    ):
        # {'en':'LongUrls', 'zh_CN':'长网址（原网址）'}
        self.long_urls = long_urls
        # {'en':'Ttl', 'zh_CN':'短网址有效时长(单位秒)'}
        self.ttl = ttl

    def validate(self):
        self.validate_required(self.long_urls, 'long_urls')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.long_urls is not None:
            result['LongUrls'] = self.long_urls
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LongUrls') is not None:
            self.long_urls = m.get('LongUrls')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class CreateShortUrlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        short_urls: List[CreateShortUrlShortUrl] = None,
    ):
        # {'en':'Code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'Msg', 'zh_CN':'返回信息'}
        self.msg = msg
        # {'en':'ShortUrls', 'zh_CN':'短网址'}
        self.short_urls = short_urls

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.short_urls, 'short_urls')
        if self.short_urls:
            for k in self.short_urls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.short_urls is not None:
            result['ShortUrls'] = []
            for k in self.short_urls:
                result['ShortUrls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('ShortUrls') is not None:
            self.short_urls = []
            for k in m.get('ShortUrls'):
                temp_model = CreateShortUrlShortUrl()
                self.short_urls.append(temp_model.from_map(k))
        return self


class CreateShortUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateShortUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateShortUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateShortUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DelShortUrlRequest(TeaModel):
    def __init__(
        self,
        short_url: str = None,
    ):
        # {'en':'ShortUrl', 'zh_CN':'短网址'}
        self.short_url = short_url

    def validate(self):
        self.validate_required(self.short_url, 'short_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class DelShortUrlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
    ):
        # {'en':'Code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'Msg', 'zh_CN':'返回信息'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        return self


class DelShortUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelShortUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelShortUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelShortUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SetKeyValueKeyValue(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        base_64: bool = None,
        exp: int = None,
    ):
        # {'en':'key', 'zh_CN':'key'}
        self.key = key
        # {'en':'value', 'zh_CN':'value,如果是图片等可以先进行bease64 encode。'}
        self.value = value
        # {'en':'Whether or not the server should base64 decode the value before storing it.', 'zh_CN':'是否需要对value进行base64 decode后再存储'}
        self.base_64 = base_64
        # {'en':'The time, measured in number of seconds since the UNIX epoch, at which the key should expire.', 'zh_CN':'过期时间戳，unix时间戳格式'}
        self.exp = exp

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.base_64 is not None:
            result['base64'] = self.base_64
        if self.exp is not None:
            result['exp'] = self.exp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('base64') is not None:
            self.base_64 = m.get('base64')
        if m.get('exp') is not None:
            self.exp = m.get('exp')
        return self


class SetKeyValueRequest(TeaModel):
    def __init__(
        self,
        space_name: str = None,
        data: List[SetKeyValueKeyValue] = None,
    ):
        # {'en':'spaceName', 'zh_CN':'空间名称'}
        self.space_name = space_name
        # {'en':'key value pairs', 'zh_CN':'key value 数据'}
        self.data = data

    def validate(self):
        self.validate_required(self.space_name, 'space_name')
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
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = SetKeyValueKeyValue()
                self.data.append(temp_model.from_map(k))
        return self


class SetKeyValueResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
    ):
        # {'en':'code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'返回信息'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SetKeyValuePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetKeyValueParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetKeyValueRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetKeyValueResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




