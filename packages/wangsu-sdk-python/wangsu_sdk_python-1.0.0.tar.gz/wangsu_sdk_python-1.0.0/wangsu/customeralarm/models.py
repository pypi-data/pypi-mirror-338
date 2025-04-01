# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryInstanceDowntimeNotificationRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryInstanceDowntimeNotificationServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # {"en":"instance id", "zh_CN":"云主机id"}
        self.id = id
        # {"en":"instance name", "zh_CN":"云主机名称"}
        self.name = name
        # {"en":"ipv4 array", "zh_CN":"ipv4 集合"}
        self.ipv_4 = ipv_4
        # {"en":"ipv6 array", "zh_CN":"ipv6 集合"}
        self.ipv_6 = ipv_6

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ipv_4, 'ipv_4')
        self.validate_required(self.ipv_6, 'ipv_6')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.ipv_4 is not None:
            result['ipv4'] = self.ipv_4
        if self.ipv_6 is not None:
            result['ipv6'] = self.ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        return self


class QueryInstanceDowntimeNotificationEvent(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        event: str = None,
        time: str = None,
        servers: List[QueryInstanceDowntimeNotificationServer] = None,
    ):
        # {"en":"node name", "zh_CN":"节点英文名称"}
        self.node_name = node_name
        # {"en":"event name", "zh_CN":"事件名称"}
        self.event = event
        # {"en":"instnace fault time", "zh_CN":"宕机时间"}
        self.time = time
        self.servers = servers

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.event, 'event')
        self.validate_required(self.time, 'time')
        self.validate_required(self.servers, 'servers')
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.event is not None:
            result['event'] = self.event
        if self.time is not None:
            result['time'] = self.time
        if self.servers is not None:
            result['servers'] = []
            for k in self.servers:
                result['servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('servers') is not None:
            self.servers = []
            for k in m.get('servers'):
                temp_model = QueryInstanceDowntimeNotificationServer()
                self.servers.append(temp_model.from_map(k))
        return self


class QueryInstanceDowntimeNotificationResponse(TeaModel):
    def __init__(
        self,
        events: List[QueryInstanceDowntimeNotificationEvent] = None,
    ):
        self.events = events

    def validate(self):
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['events'] = []
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('events') is not None:
            self.events = []
            for k in m.get('events'):
                temp_model = QueryInstanceDowntimeNotificationEvent()
                self.events.append(temp_model.from_map(k))
        return self


class QueryInstanceDowntimeNotificationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryInstanceDowntimeNotificationParameters(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # {"en":"node name", "zh_CN":"节点英文名称，多个逗号隔开"}
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class QueryInstanceDowntimeNotificationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryInstanceDowntimeNotificationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryPoPsMaintenanceNotificationRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPoPsMaintenanceNotificationServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
        private_ip: List[str] = None,
    ):
        # {"en":"Instance ID", "zh_CN":"实例id"}
        self.id = id
        # {"en":"Instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Instance IPv4", "zh_CN":"实例IPv4"}
        self.ipv_4 = ipv_4
        # {"en":"Instance IPv6", "zh_CN":"实例IPv6"}
        self.ipv_6 = ipv_6
        # {"en":"Instance intranet IP", "zh_CN":"实例内网IP"}
        self.private_ip = private_ip

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ipv_4, 'ipv_4')
        self.validate_required(self.ipv_6, 'ipv_6')
        self.validate_required(self.private_ip, 'private_ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.ipv_4 is not None:
            result['ipv4'] = self.ipv_4
        if self.ipv_6 is not None:
            result['ipv6'] = self.ipv_6
        if self.private_ip is not None:
            result['privateIp'] = self.private_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')
        return self


class QueryPoPsMaintenanceNotificationResponse(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        event: str = None,
        status: str = None,
        start_time: str = None,
        end_time: str = None,
        servers: List[QueryPoPsMaintenanceNotificationServer] = None,
    ):
        # {"en":"Node name", "zh_CN":"节点英文名称"}
        self.node_name = node_name
        # {"en":"Event:
        # CUTOVER
        # WITHDRAWAL
        # ", "zh_CN":"事件
        # CUTOVER     节点割接
        # WITHDRAWAL  节点退用"}
        self.event = event
        # {"en":"Event status:
        # Scheduled
        # Executing
        # Executed
        # Canceled
        # ", "zh_CN":"事件状态
        # Scheduled    计划
        # Executing     执行中
        # Executed     执行完毕
        # Canceled     取消"}
        self.status = status
        # {"en":"Cutover start time in yyyy-MM-dd HH:mm:ss.
        #     If it is a node retirement, then it is the retirement date.
        #     ", "zh_CN":"割接开始时间，格式 yyyy-MM-dd HH:mm:ss ，如果是节点退用，则是退用日期."}
        self.start_time = start_time
        # {"en":"Cutover end time in yyyy-MM-dd HH:mm:ss.
        # If it is a node retirement, then the value is empty.", "zh_CN":"割接结束时间，格式yyyy-MM-dd HH:mm:ss
        # 如果是节点退用，则该值为空."}
        self.end_time = end_time
        # {"en":"Instance information array", "zh_CN":"实例信息数组"}
        self.servers = servers

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.event, 'event')
        self.validate_required(self.status, 'status')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.servers, 'servers')
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.event is not None:
            result['event'] = self.event
        if self.status is not None:
            result['status'] = self.status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.servers is not None:
            result['servers'] = []
            for k in self.servers:
                result['servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('servers') is not None:
            self.servers = []
            for k in m.get('servers'):
                temp_model = QueryPoPsMaintenanceNotificationServer()
                self.servers.append(temp_model.from_map(k))
        return self


class QueryPoPsMaintenanceNotificationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPoPsMaintenanceNotificationParameters(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # {"en":"Node name, optional;
        # If it is multiple, it needs to be separated by a semicolon;
        # If not specified, query all nodes.
        # If the specified node customer is not in use or there is no cutover and dropout event, the node will not be returned in the response message.
        # ", "zh_CN":"节点英文名称，可选；
        # 如果是多个，需要用半角逗号隔开;
        # 如果未指定，则查询所有的节点。
        # 如果指定的节点客户未使用，或者没有割接退用事件，则在响应消息中不返回该节点。"}
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class QueryPoPsMaintenanceNotificationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPoPsMaintenanceNotificationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




