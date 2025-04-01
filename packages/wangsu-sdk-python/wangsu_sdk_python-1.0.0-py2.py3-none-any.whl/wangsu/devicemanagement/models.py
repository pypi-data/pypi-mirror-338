# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class InvitePushRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
        notice_url: str = None,
        trans_no: str = None,
    ):
        # {"en":"The national standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"channelId", "zh_CN":"通道Id"}
        self.channel_id = channel_id
        # {"en":"Callback notification URL", "zh_CN":"回调通知URL"}
        self.notice_url = notice_url
        # {"en":"Custom request id, customers need to ensure uniqueness", "zh_CN":"自定义请求id, 客户需要保证唯一性"}
        self.trans_no = trans_no

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.trans_no, 'trans_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.notice_url is not None:
            result['noticeUrl'] = self.notice_url
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('noticeUrl') is not None:
            self.notice_url = m.get('noticeUrl')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        return self


class InvitePushResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class InvitePushPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class InvitePushParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class InvitePushRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class InvitePushResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class StopPushRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
        notice_url: str = None,
        trans_no: str = None,
    ):
        # {"en":"The national standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"channelId", "zh_CN":"通道Id"}
        self.channel_id = channel_id
        # {"en":"Callback notification URL", "zh_CN":"回调通知URL"}
        self.notice_url = notice_url
        # {"en":"Custom request id, customers need to ensure uniqueness", "zh_CN":"自定义请求id, 客户需要保证唯一性"}
        self.trans_no = trans_no

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.trans_no, 'trans_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.notice_url is not None:
            result['noticeUrl'] = self.notice_url
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('noticeUrl') is not None:
            self.notice_url = m.get('noticeUrl')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        return self


class StopPushResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class StopPushPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopPushParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopPushRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopPushResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetDevicesListRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: str = None,
        space_name: str = None,
        status: int = None,
        type: int = None,
        name: str = None,
        device_id: str = None,
        page_size: int = None,
        page_index: int = None,
    ):
        # {"en":"Relay node ID", "zh_CN":"父节点ID"}
        self.parent_node_id = parent_node_id
        # {"en":"Space name. Fuzzy search is not supported.", "zh_CN":"空间名称。不支持模糊搜索"}
        self.space_name = space_name
        # {"en":"GetDevicesListDevice status: 0: Offline 1: Online", "zh_CN":"设备状态： 0:离线    1：在线"}
        self.status = status
        # {"en":"GetDevicesListDevice type: 1: IPC 2: NVR", "zh_CN":"设备类型：1：IPC   2：NVR"}
        self.type = type
        # {"en":"GetDevicesListDevice name. Supports fuzzy search", "zh_CN":"设备名称。支持模糊搜索"}
        self.name = name
        # {"en":"The national standard id of the device. Fuzzy search is not supported.", "zh_CN":"设备国标id。不支持模糊搜索。"}
        self.device_id = device_id
        # {"en":"Specify the paging size. The default value is 10, and the maximum value is 50.", "zh_CN":"分页大小。默认10，最大50"}
        self.page_size = page_size
        # {"en":"Page number, default is first page", "zh_CN":"第几页，默认第一页"}
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        return self


class GetDevicesListDevice(TeaModel):
    def __init__(
        self,
        name: str = None,
        device_id: str = None,
        type: int = None,
        access_protocol: int = None,
        sip_id: str = None,
        sip_server_address: str = None,
        sip_server_port: int = None,
        status: int = None,
        is_auto_push: int = None,
        channel_num: int = None,
        space_name: int = None,
        description: str = None,
        create_time: int = None,
        manufacturer: str = None,
        longitude: float = None,
        latitude: float = None,
        address: str = None,
        parent_node_id: str = None,
        stream_type: str = None,
    ):
        # {"en":"GetDevicesListDevice name", "zh_CN":"设备名称"}
        self.name = name
        # {"en":"National standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"GetDevicesListDevice type: 1: IPC 2: NVR","zh_CN":"设备类型：1：IPC   2：NVR"}
        self.type = type
        # {"en":"Access Agreement 1: GB28181-2016",zh_CN:"接入协议 1：GB28181-2016"}
        self.access_protocol = access_protocol
        # {"en":"SIP server ID","zh_CN":"sip服务器id"}
        self.sip_id = sip_id
        # {"en":"SIP Server Address","zh_CN":"sip服务器地址"}
        self.sip_server_address = sip_server_address
        # {"en":"SIP server port","zh_CN":"sip服务器端口"}
        self.sip_server_port = sip_server_port
        # {"en":"The status of the device.","zh_CN":"设备状态"}
        self.status = status
        # {"en":"Whether to enable automatic invitation streaming. true: Enable automatic invitation streaming, false: Disable automatic invitation streaming","zh_CN":"是否启动自动邀请推流。1:启动自动邀请推流，0:不启动自动邀请推流"}
        self.is_auto_push = is_auto_push
        # {"en":"Number of channels","zh_CN":"通道数量"}
        self.channel_num = channel_num
        # {"en":"Space Name","zh_CN":"所属空间名称"}
        self.space_name = space_name
        # {"en":"GetDevicesListDevice Description","zh_CN":"设备描述"}
        self.description = description
        # {"en":"GetDevicesListDevice creation time (timestamp)","zh_CN":"设备创建时间（时间戳）"}
        self.create_time = create_time
        # {"en":"Equipment Manufacturer","zh_CN":"设备厂商"}
        self.manufacturer = manufacturer
        # {"en":"longitude","zh_CN":"经度"}
        self.longitude = longitude
        # {"en":"latitude","zh_CN":"纬度"}
        self.latitude = latitude
        # {"en":"GetDevicesListDevice Address","zh_CN":"设备地址"}
        self.address = address
        # {"en":"Relay node ID", "zh_CN":"父节点ID"}
        self.parent_node_id = parent_node_id
        # {"en":"Stream Type:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB", "zh_CN":"码流类型:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB"}
        self.stream_type = stream_type

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.access_protocol, 'access_protocol')
        self.validate_required(self.sip_id, 'sip_id')
        self.validate_required(self.sip_server_address, 'sip_server_address')
        self.validate_required(self.sip_server_port, 'sip_server_port')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_auto_push, 'is_auto_push')
        self.validate_required(self.channel_num, 'channel_num')
        self.validate_required(self.space_name, 'space_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.manufacturer, 'manufacturer')
        self.validate_required(self.longitude, 'longitude')
        self.validate_required(self.latitude, 'latitude')
        self.validate_required(self.address, 'address')
        self.validate_required(self.parent_node_id, 'parent_node_id')
        self.validate_required(self.stream_type, 'stream_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.type is not None:
            result['type'] = self.type
        if self.access_protocol is not None:
            result['accessProtocol'] = self.access_protocol
        if self.sip_id is not None:
            result['sipId'] = self.sip_id
        if self.sip_server_address is not None:
            result['sipServerAddress'] = self.sip_server_address
        if self.sip_server_port is not None:
            result['sipServerPort'] = self.sip_server_port
        if self.status is not None:
            result['status'] = self.status
        if self.is_auto_push is not None:
            result['isAutoPush'] = self.is_auto_push
        if self.channel_num is not None:
            result['channelNum'] = self.channel_num
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.description is not None:
            result['description'] = self.description
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.address is not None:
            result['address'] = self.address
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.stream_type is not None:
            result['streamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('accessProtocol') is not None:
            self.access_protocol = m.get('accessProtocol')
        if m.get('sipId') is not None:
            self.sip_id = m.get('sipId')
        if m.get('sipServerAddress') is not None:
            self.sip_server_address = m.get('sipServerAddress')
        if m.get('sipServerPort') is not None:
            self.sip_server_port = m.get('sipServerPort')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('isAutoPush') is not None:
            self.is_auto_push = m.get('isAutoPush')
        if m.get('channelNum') is not None:
            self.channel_num = m.get('channelNum')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('streamType') is not None:
            self.stream_type = m.get('streamType')
        return self


class GetDevicesListData(TeaModel):
    def __init__(
        self,
        rows: List[GetDevicesListDevice] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # {"en":"GetDevicesListDevice List", "zh_CN":"设备列表"}
        self.rows = rows
        # {"en":"Page number,", "zh_CN":"第几页"}
        self.page_index = page_index
        # {"en":"Specify the paging size", "zh_CN":"分页大小"}
        self.page_size = page_size
        # {"en":"Total number of devices", "zh_CN":"总设备数"}
        self.total = total

    def validate(self):
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['rows'] = []
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = GetDevicesListDevice()
                self.rows.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetDevicesListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetDevicesListData = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

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
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = GetDevicesListData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetDevicesListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDevicesListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDevicesListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDevicesListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelControlRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
        disable: bool = None,
    ):
        # {"en":"Device GB28181 Id", "zh_CN":"设备国标ID"}
        self.device_id = device_id
        # {"en":"Channel GB28181 Id", "zh_CN":"通道国标ID"}
        self.channel_id = channel_id
        # {"en":"true: channel is disabled
        # false: channel is enabled", "zh_CN":"true:通道禁用
        # 
        # false：通道启用"}
        self.disable = disable

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.disable, 'disable')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.disable is not None:
            result['disable'] = self.disable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        return self


class ChannelControlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ChannelControlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelControlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelControlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelControlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetStreamUrlRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
    ):
        # {"en":"deviceId", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"channelId", "zh_CN":"通道Id"}
        self.channel_id = channel_id

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        return self


class GetStreamUrlData(TeaModel):
    def __init__(
        self,
        flv: str = None,
        rtmp: str = None,
        hls: str = None,
        webrtc: str = None,
    ):
        # {"en":"flv url", "zh_CN":"flv拉流地址"}
        self.flv = flv
        # {"en":"rtmp url", "zh_CN":"rtmp拉流地址"}
        self.rtmp = rtmp
        # {"en":"hls url", "zh_CN":"hls拉流地址"}
        self.hls = hls
        # {"en":"webrtc url", "zh_CN":"webrtc拉流地址"}
        self.webrtc = webrtc

    def validate(self):
        self.validate_required(self.flv, 'flv')
        self.validate_required(self.rtmp, 'rtmp')
        self.validate_required(self.hls, 'hls')
        self.validate_required(self.webrtc, 'webrtc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flv is not None:
            result['flv'] = self.flv
        if self.rtmp is not None:
            result['rtmp'] = self.rtmp
        if self.hls is not None:
            result['hls'] = self.hls
        if self.webrtc is not None:
            result['webrtc'] = self.webrtc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flv') is not None:
            self.flv = m.get('flv')
        if m.get('rtmp') is not None:
            self.rtmp = m.get('rtmp')
        if m.get('hls') is not None:
            self.hls = m.get('hls')
        if m.get('webrtc') is not None:
            self.webrtc = m.get('webrtc')
        return self


class GetStreamUrlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[GetStreamUrlData] = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
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
                temp_model = GetStreamUrlData()
                self.data.append(temp_model.from_map(k))
        return self


class GetStreamUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStreamUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStreamUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetStreamUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: str = None,
        device_id: str = None,
        name: str = None,
        type: int = None,
        space_name: str = None,
        password: str = None,
        is_auto_push: int = None,
        manufacturer: str = None,
        longitude: float = None,
        latitude: float = None,
        address: str = None,
        description: str = None,
        stream_type: str = None,
    ):
        # {"en":"Organization tree directory node id. If not filled in, it will be added to the root directory by default", "zh_CN":"组织树目录节点id。不填默认新增到根目录下"}
        self.parent_node_id = parent_node_id
        # {"en":"The national standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"Device Name","zh_CN":"设备名称"}
        self.name = name
        # {"en":"Device type: 1: IPC 2: NVR","zh_CN":"设备类型：1：IPC   2：NVR"}
        self.type = type
        # {"en":"Space name","zh_CN":"所属空间名称"}
        self.space_name = space_name
        # {"en":"Device registration password","zh_CN":"设备注册密码"}
        self.password = password
        # {"en":"Whether to enable automatic invitation streaming. true: Enable automatic invitation streaming, false: Disable automatic invitation streaming","zh_CN":"是否启动自动邀请推流。1:启动自动邀请推流，0:不启动自动邀请推流"}
        self.is_auto_push = is_auto_push
        # {"en":"Equipment Manufacturer", "zh_CN":"设备厂商"}
        self.manufacturer = manufacturer
        # {"en":"Longituder", "zh_CN":"经度"}
        self.longitude = longitude
        # {"en":"Latitude", "zh_CN":"纬度"}
        self.latitude = latitude
        # {"en":"Device Description", "zh_CN":"设备地址"}
        self.address = address
        # {"en":"Device Address", "zh_CN":"设备描述"}
        self.description = description
        # {"en":"When not transmitting, the code stream type is default
        # Stream Type:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB", "zh_CN":"不传时码流类型为default
        # 码流类型:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB"}
        self.stream_type = stream_type

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.space_name, 'space_name')
        self.validate_required(self.password, 'password')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.password is not None:
            result['password'] = self.password
        if self.is_auto_push is not None:
            result['isAutoPush'] = self.is_auto_push
        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.address is not None:
            result['address'] = self.address
        if self.description is not None:
            result['description'] = self.description
        if self.stream_type is not None:
            result['streamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('isAutoPush') is not None:
            self.is_auto_push = m.get('isAutoPush')
        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('streamType') is not None:
            self.stream_type = m.get('streamType')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateDevicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDeviceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDeviceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDeviceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        # {"en":"The national standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        return self


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteDevicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDeviceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDeviceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDeviceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PtzControlRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
        cmd: str = None,
        ptz_param: int = None,
    ):
        # {"en":"Device GB28181 Id", "zh_CN":"设备国标ID"}
        self.device_id = device_id
        # {"en":"Channel GB28181 Id", "zh_CN":"通道国标ID"}
        self.channel_id = channel_id
        # {"en":"PTZ control commands
        # ptzUp: The Device turns upward
        # ptzDown: The Device turns down
        # ptzLeft: The Device turns left
        # ptzRight: The Device turns right
        # ptzLeftUp: The Device turns to the upper left
        # ptzRightUp: The Device turns right up
        # ptzLeftDown: The Device turns left and down
        # ptzRightDown: The Device turns right and down
        # ptzZoomIn: Device lens zoom in
        # ptzZoomOut: The Device lens is zoomed out
        # ptzStop: Stop ptz operation
        # fiIrisIn: Device aperture magnification
        # fiIrisOut: The Device aperture is reduced
        # fiFocusIn: Device lens far focus
        # fiFocusOut: The Device lens is in close focus
        # fiStop: Stop", "zh_CN":"云台控制指令
        # 
        # ptzUp：设备向上转
        # 
        # ptzDown：设备向下转
        # 
        # ptzLeft：设备向左转
        # 
        # ptzRight：设备向右转
        # 
        # ptzLeftUp：设备向左上转
        # 
        # ptzRightUp：设备向右上转
        # 
        # ptzLeftDown：设备向左下转
        # 
        # ptzRightDown：设备向右下转
        # 
        # ptzZoomIn：设备镜头放大
        # 
        # ptzZoomOut：设备镜头缩小
        # 
        # ptzStop：停止ptz操作
        # 
        # fiIrisIn：设备光圈放大
        # 
        # fiIrisOut：设备光圈缩小
        # 
        # fiFocusIn：设备镜头远焦
        # 
        # fiFocusOut：设备镜头近焦
        # 
        # fiStop：停止"}
        self.cmd = cmd
        # {"en":"Step Length
        # 1. Set the rotation speed when the control Device rotates up, down, left, and right. The value range is 0-255, and the default is 10
        # 2. Set the value when the control Device lens is zoomed in or out. The value range is 0-15, and the default value is 1
        # 3. When controlling the aperture or focal length of the Device, set the value, the range is 0-255, the default is 10", "zh_CN":"步长
        # 
        # 1、当控制设备向上下左右旋转时设置旋转的速度，取值范围0-255，默认10
        # 
        # 2、当控制设备镜头放大或缩小时设置数值，取值范围0-15，默认1
        # 
        # 3、当控制设备光圈或焦距时设置数值，取值范围0-255，默认10"}
        self.ptz_param = ptz_param

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.cmd, 'cmd')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.ptz_param is not None:
            result['ptzParam'] = self.ptz_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('ptzParam') is not None:
            self.ptz_param = m.get('ptzParam')
        return self


class PtzControlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PtzControlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PtzControlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PtzControlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PtzControlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        name: str = None,
        password: str = None,
        is_auto_push: int = None,
        manufacturer: str = None,
        longitude: float = None,
        latitude: float = None,
        address: str = None,
        description: str = None,
        stream_type: str = None,
    ):
        # {"en":"The national standard id of the device", "zh_CN":"设备国标id"}
        self.device_id = device_id
        # {"en":"Device Name", "zh_CN":"设备名称"}
        self.name = name
        # {"en":"Device registration password", "zh_CN":"设备注册密码"}
        self.password = password
        # {"en":"Whether to enable automatic invitation streaming. true: Enable automatic invitation streaming, false: Disable automatic invitation streaming", "zh_CN":"是否启动自动邀请推流 
        # 1.是，0.否
        # 默认：01:启动自动邀请推流0:不启动自动邀请推流"}
        self.is_auto_push = is_auto_push
        # {"en":"Equipment Manufacturer", "zh_CN":"设备厂商"}
        self.manufacturer = manufacturer
        # {"en":"Longituder", "zh_CN":"经度 仅支持正负数，整数部分最多3位，小数部分最多8位"}
        self.longitude = longitude
        # {"en":"Laitude", "zh_CN":"纬度 仅支持正负数，整数部分最多3位，小数部分最多8位"}
        self.latitude = latitude
        # {"en":"Device Address", "zh_CN":"设备地址"}
        self.address = address
        # {"en":"Device Description", "zh_CN":"设备描述"}
        self.description = description
        # {"en":"Stream Type:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB", "zh_CN":"码流类型:
        # default
        # stream:0
        # stream:1
        # streamnumber:0
        # streamnumber:1
        # streamprofile:0 
        # streamprofile:1
        # streamMode:MAIN
        # streamMode:SUB"}
        self.stream_type = stream_type

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.name is not None:
            result['name'] = self.name
        if self.password is not None:
            result['password'] = self.password
        if self.is_auto_push is not None:
            result['isAutoPush'] = self.is_auto_push
        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.address is not None:
            result['address'] = self.address
        if self.description is not None:
            result['description'] = self.description
        if self.stream_type is not None:
            result['streamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('isAutoPush') is not None:
            self.is_auto_push = m.get('isAutoPush')
        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('streamType') is not None:
            self.stream_type = m.get('streamType')
        return self


class EditDeviceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class EditDevicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDeviceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDeviceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDeviceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditChannelInfoRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        channel_id: str = None,
        channel_name: str = None,
        record_switch: int = None,
        immediate_record: int = None,
        record_template: str = None,
        save_period: int = None,
    ):
        # {"en":"Device GB28181 Id.", "zh_CN":"设备国标id。不支持模糊搜索。"}
        self.device_id = device_id
        # {"en":"Channel GB28181 Id", "zh_CN":"通道国标ID"}
        self.channel_id = channel_id
        # {"en":"Channel name", "zh_CN":"通道名称"}
        self.channel_name = channel_name
        # {"en":"Cloud Recording enabled,0: Disabled (default) 1: Enabled", "zh_CN":"云端录制开关状态，0：未开启（默认）  1：开启"}
        self.record_switch = record_switch
        # {"en":"Immediate record enabled,0: Disabled (default),1: Enabled,If the Device is Push streaming, it is forbidden to turn on or off the push-to-record function. When the push-to-record function is turned on, the Recording template Filed recordTemplate is invalid.", "zh_CN":"即推即录开关状态，0：未开启（默认）  1：开启，如果设备在推流中，禁止开启关闭即推即录。当开启即推即录是录制模板字段“recordTemplate”无效。"}
        self.immediate_record = immediate_record
        # {"en":"The Recording template associated with the channel.", "zh_CN":"通道关联的录制模板名称。当前录制模板名称是唯一"}
        self.record_template = record_template
        # {"en":"Immediate record duration of file retention.Unit: Day
        # 
        # Default: 30 days", "zh_CN":"即推即录文件保存时长。单位：天
        # 
        # 默认30天"}
        self.save_period = save_period

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.record_switch is not None:
            result['recordSwitch'] = self.record_switch
        if self.immediate_record is not None:
            result['immediateRecord'] = self.immediate_record
        if self.record_template is not None:
            result['recordTemplate'] = self.record_template
        if self.save_period is not None:
            result['savePeriod'] = self.save_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('recordSwitch') is not None:
            self.record_switch = m.get('recordSwitch')
        if m.get('immediateRecord') is not None:
            self.immediate_record = m.get('immediateRecord')
        if m.get('recordTemplate') is not None:
            self.record_template = m.get('recordTemplate')
        if m.get('savePeriod') is not None:
            self.save_period = m.get('savePeriod')
        return self


class EditChannelInfoResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class EditChannelInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditChannelInfoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditChannelInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditChannelInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelStatusUpdateRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
    ):
        # {"en":"Channel GB28181 Id", "zh_CN":"通道国标ID"}
        self.device_id = device_id

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        return self


class ChannelStatusUpdateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Results status code, 0 means success", "zh_CN":"结果状态码，0 为成功"}
        self.code = code
        # {"en":"Operate successfully", "zh_CN":"操作成功"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ChannelStatusUpdatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelStatusUpdateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelStatusUpdateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelStatusUpdateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryChannelListRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        page_size: int = None,
        page_index: int = None,
    ):
        # {"en":"The national standard id of the device. Fuzzy search is not supported.", "zh_CN":"设备国标id。不支持模糊搜索。"}
        self.device_id = device_id
        # {"en":"Specify the paging size. The default value is 10, and the maximum value is 50.", "zh_CN":"分页大小。默认10，最大50"}
        self.page_size = page_size
        # {"en":"Page number, default is first page", "zh_CN":"第几页，默认第一页"}
        self.page_index = page_index

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        return self


class QueryChannelListChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        channel_id: str = None,
        status: int = None,
        has_stream: int = None,
        type: int = None,
        record_switch: int = None,
        record_state: str = None,
        immediate_record: int = None,
        save_period: int = None,
        resolution: str = None,
        record_template: str = None,
        is_enabled: int = None,
    ):
        # {"en":"QueryChannelListChannel name", "zh_CN":"通道名称"}
        self.name = name
        # {"en":"QueryChannelListChannel national standard ID", "zh_CN":"通道国标ID"}
        self.channel_id = channel_id
        # {"en":"QueryChannelListChannel status: 0. Offline, 1. Online", "zh_CN":"通道状态：0.离线，1.在线"}
        self.status = status
        # {"en":"Streaming status: 0: no streaming, 1: streaming", "zh_CN":"流状态：0：未推流，1：有推流"}
        self.has_stream = has_stream
        # {"en":"QueryChannelListChannel type: 1. Video channel, 2. Alarm channel", "zh_CN":"通道类型：1.视频通道，2.告警通道"}
        self.type = type
        # {"en":"Cloud Recording enabled,0: Disabled (default) 1: Enabled", "zh_CN":"云端录制开关状态，0：未开启（默认）  1：开启"}
        self.record_switch = record_switch
        # {"en":"Recording Status,NOT_RECORD: Not Recording(default) RECCORDING: Recording", "zh_CN":"录制状态，NOT_RECORD：未录制（默认） RECCORDING：录制中"}
        self.record_state = record_state
        # {"en":"Immediate record enabled,0: Disabled (default) 1: Enabled", "zh_CN":"即推即录开关状态，0：未开启（默认）  1：开启"}
        self.immediate_record = immediate_record
        # {"en":"Immediate record duration of file retention.Unit: Day", "zh_CN":"即推即录文件保存时长。单位：天"}
        self.save_period = save_period
        # {"en":"QueryChannelListChannel resolution,If the Platform fails to obtain the resolution, it is unified to -,Example: 720*1280.", "zh_CN":"通道分辨率，如果平台未能获取到分辨率，统一为“-”，示列：720*1280。"}
        self.resolution = resolution
        # {"en":"Template for recording associated with a specific channel.", "zh_CN":"通道关联的录制模板名称"}
        self.record_template = record_template
        # {"en":"QueryChannelListChannel enable status. 1: Enable. 0: Disable", "zh_CN":"通道启用状态。1：启动。0：禁用"}
        self.is_enabled = is_enabled

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.has_stream, 'has_stream')
        self.validate_required(self.type, 'type')
        self.validate_required(self.record_switch, 'record_switch')
        self.validate_required(self.record_state, 'record_state')
        self.validate_required(self.immediate_record, 'immediate_record')
        self.validate_required(self.save_period, 'save_period')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.record_template, 'record_template')
        self.validate_required(self.is_enabled, 'is_enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.status is not None:
            result['status'] = self.status
        if self.has_stream is not None:
            result['hasStream'] = self.has_stream
        if self.type is not None:
            result['type'] = self.type
        if self.record_switch is not None:
            result['recordSwitch'] = self.record_switch
        if self.record_state is not None:
            result['recordState'] = self.record_state
        if self.immediate_record is not None:
            result['immediateRecord'] = self.immediate_record
        if self.save_period is not None:
            result['savePeriod'] = self.save_period
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.record_template is not None:
            result['recordTemplate'] = self.record_template
        if self.is_enabled is not None:
            result['isEnabled'] = self.is_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('hasStream') is not None:
            self.has_stream = m.get('hasStream')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('recordSwitch') is not None:
            self.record_switch = m.get('recordSwitch')
        if m.get('recordState') is not None:
            self.record_state = m.get('recordState')
        if m.get('immediateRecord') is not None:
            self.immediate_record = m.get('immediateRecord')
        if m.get('savePeriod') is not None:
            self.save_period = m.get('savePeriod')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('recordTemplate') is not None:
            self.record_template = m.get('recordTemplate')
        if m.get('isEnabled') is not None:
            self.is_enabled = m.get('isEnabled')
        return self


class QueryChannelListData(TeaModel):
    def __init__(
        self,
        rows: List[QueryChannelListChannel] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # {"en":"QueryChannelListChannel List", "zh_CN":"通道列表"}
        self.rows = rows
        # {"en":"Page number,", "zh_CN":"第几页"}
        self.page_index = page_index
        # {"en":"Specify the paging size", "zh_CN":"分页大小"}
        self.page_size = page_size
        # {"en":"Total number of devices", "zh_CN":"总设备数"}
        self.total = total

    def validate(self):
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['rows'] = []
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = QueryChannelListChannel()
                self.rows.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryChannelListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: QueryChannelListData = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

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
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryChannelListData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryChannelListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




