# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryCloudVODStorageVolumeRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        is_details: int = None,
    ):
        # {"en":"Start Time:
        # 1. The format is yyyy-MM-dd, for example, 2024-01-23 (which is January 23, 2024, Beijing Time);
        # 2. Cannot be greater than the current time;", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-dd，例如，2024-01-23（为北京时间2024年01月23日）；
        # 2.不能大于当前时间；"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. The format is yyyy-MM-dd;
        # 2. The end time must be greater than the start time;
        # 3. If the end time is greater than the current time, use the current time;
        # 4. If both dateFrom and dateTo are not passed, today data will be queried by default; if only one is not passed, an exception will be thrown;
        # 5. The maximum query interval allowed is 61 days, that is, the difference between dateFrom and dateTo cannot exceed 61 days.", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-dd；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询今天数据；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：61天，即dateFrom和dateTo相差不能超过61天。"}
        self.date_to = date_to
        # {"en":"Whether to return details. Default: 0
        # 0: Do not return the peak storage peak value details at the daily granularity
        # 1: Returns the peak storage peak value details at the daily granularity", "zh_CN":"是否返回明细。默认：0
        # 0:不返回天粒度存储量峰值明细
        # 1:返回天粒度存储量峰值明细"}
        self.is_details = is_details

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
        if self.is_details is not None:
            result['isDetails'] = self.is_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('isDetails') is not None:
            self.is_details = m.get('isDetails')
        return self


class QueryCloudVODStorageVolumeResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[str] = None,
        peak_value: float = None,
        details: List[str] = None,
        date: str = None,
        storage_volume: float = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data
        # {"en":"Peak value of storage, unit GB", "zh_CN":"存储量峰值，单位GB"}
        self.peak_value = peak_value
        # {"en":"Storage Volume Detail List", "zh_CN":"存储量明细列表"}
        self.details = details
        # {"en":"Date", "zh_CN":"日期"}
        self.date = date
        # {"en":"Storage volume, unit: MB", "zh_CN":"每日存储量峰值，单位MB"}
        self.storage_volume = storage_volume

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.details, 'details')
        self.validate_required(self.date, 'date')
        self.validate_required(self.storage_volume, 'storage_volume')

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
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.details is not None:
            result['details'] = self.details
        if self.date is not None:
            result['date'] = self.date
        if self.storage_volume is not None:
            result['storageVolume'] = self.storage_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('details') is not None:
            self.details = m.get('details')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('storageVolume') is not None:
            self.storage_volume = m.get('storageVolume')
        return self


class QueryCloudVODStorageVolumePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCloudVODStorageVolumeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCloudVODStorageVolumeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCloudVODStorageVolumeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetRealTimeChannelOnlineNumberRequest(TeaModel):
    def __init__(
        self,
        pull_ids: str = None,
    ):
        # {"en":"Pull id, multiple values separated by \",\"", "zh_CN":"拉流 id，多个值通过\",\"隔开"}
        self.pull_ids = pull_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_ids is not None:
            result['pullIds'] = self.pull_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullIds') is not None:
            self.pull_ids = m.get('pullIds')
        return self


class GetRealTimeChannelOnlineNumberOnlineNumberItem(TeaModel):
    def __init__(
        self,
        online_number: int = None,
        pull_id: str = None,
    ):
        # {"en":"Online population", "zh_CN":"在线人数"}
        self.online_number = online_number
        # {"en":"pullId", "zh_CN":"拉流 id"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.online_number, 'online_number')
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_number is not None:
            result['onlineNumber'] = self.online_number
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onlineNumber') is not None:
            self.online_number = m.get('onlineNumber')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetRealTimeChannelOnlineNumberData(TeaModel):
    def __init__(
        self,
        online_number_list: List[GetRealTimeChannelOnlineNumberOnlineNumberItem] = None,
    ):
        # {"en":"Online list of people", "zh_CN":"在线人数列表"}
        self.online_number_list = online_number_list

    def validate(self):
        self.validate_required(self.online_number_list, 'online_number_list')
        if self.online_number_list:
            for k in self.online_number_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_number_list is not None:
            result['onlineNumberList'] = []
            for k in self.online_number_list:
                result['onlineNumberList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onlineNumberList') is not None:
            self.online_number_list = []
            for k in m.get('onlineNumberList'):
                temp_model = GetRealTimeChannelOnlineNumberOnlineNumberItem()
                self.online_number_list.append(temp_model.from_map(k))
        return self


class GetRealTimeChannelOnlineNumberResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[GetRealTimeChannelOnlineNumberData] = None,
    ):
        # {"en":"200 success", "zh_CN":"200，操作成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
                temp_model = GetRealTimeChannelOnlineNumberData()
                self.data.append(temp_model.from_map(k))
        return self


class GetRealTimeChannelOnlineNumberPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRealTimeChannelOnlineNumberParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRealTimeChannelOnlineNumberRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRealTimeChannelOnlineNumberResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




