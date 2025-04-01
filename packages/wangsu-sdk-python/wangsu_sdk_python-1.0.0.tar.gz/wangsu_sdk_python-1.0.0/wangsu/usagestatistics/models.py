# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class WcsQpsRequest(TeaModel):
    def __init__(
        self,
        bucket_list: List[str] = None,
        region_name_list: List[str] = None,
        date_from: str = None,
        date_to: str = None,
        type: str = None,
        timezone: str = None,
    ):
        # {"en":"bucket", "zh_CN":"空间名"}
        self.bucket_list = bucket_list
        # {"en":"regionname", "zh_CN":"节点名称"}
        self.region_name_list = region_name_list
        # {"en":"dateFrom", "zh_CN":"查询开始时间，例如：2024-12-12T10:00+08:00，包含开始时间"}
        self.date_from = date_from
        # {"en":"dateTo", "zh_CN":"查询j结束时间，例如：2024-12-12T10:01+08:00，包含结束时间"}
        self.date_to = date_to
        # {"en":"type", "zh_CN":"write：写, read：读, 不传则查读和写"}
        self.type = type
        # {"en":"timezone", "zh_CN":"返回数据的时区。 格式：+0N:00，-12<= n <= 12。如:+08:00。  默认+08:00"}
        self.timezone = timezone

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_list is not None:
            result['bucketList'] = self.bucket_list
        if self.region_name_list is not None:
            result['regionNameList'] = self.region_name_list
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.type is not None:
            result['type'] = self.type
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketList') is not None:
            self.bucket_list = m.get('bucketList')
        if m.get('regionNameList') is not None:
            self.region_name_list = m.get('regionNameList')
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class WcsQpsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[str] = None,
        bucket: str = None,
        region_name: str = None,
        detail: List[str] = None,
        time: str = None,
        read_value: float = None,
        write_value: float = None,
    ):
        # {"en":"code", "zh_CN":"错误码"}
        self.code = code
        # {"en":"string", "zh_CN":"错误信息"}
        self.message = message
        # {"en":"", "zh_CN":""}
        self.data = data
        # {"en":"bucket", "zh_CN":"空间名"}
        self.bucket = bucket
        # {"en":"regionname", "zh_CN":"节点名称"}
        self.region_name = region_name
        # {"en":"writeDetail", "zh_CN":"写"}
        self.detail = detail
        # {"en":"time", "zh_CN":"时间"}
        self.time = time
        # {"en":"value", "zh_CN":"每分钟的读qps。保留两位小数，每分钟的qps=请求数/60"}
        self.read_value = read_value
        # {"en":"value", "zh_CN":"每分钟的写qps。保留两位小数，每分钟的qps=请求数/60"}
        self.write_value = write_value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.detail, 'detail')
        self.validate_required(self.time, 'time')
        self.validate_required(self.read_value, 'read_value')
        self.validate_required(self.write_value, 'write_value')

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
            result['data'] = self.data
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.detail is not None:
            result['detail'] = self.detail
        if self.time is not None:
            result['time'] = self.time
        if self.read_value is not None:
            result['readValue'] = self.read_value
        if self.write_value is not None:
            result['writeValue'] = self.write_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('readValue') is not None:
            self.read_value = m.get('readValue')
        if m.get('writeValue') is not None:
            self.write_value = m.get('writeValue')
        return self


class WcsQpsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WcsQpsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WcsQpsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WcsQpsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




