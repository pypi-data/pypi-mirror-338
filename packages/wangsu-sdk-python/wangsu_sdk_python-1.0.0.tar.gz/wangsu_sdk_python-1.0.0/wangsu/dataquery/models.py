# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AllSiteSumFlowRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AllSiteSumFlowResponseContent(TeaModel):
    def __init__(
        self,
        sum_site_out_flow: str = None,
        sum_site_in_flow: str = None,
    ):
        # {'en':'Total outgoing traffic of the enterprise site', 'zh_CN':'企业站点流出流量总和'}
        self.sum_site_out_flow = sum_site_out_flow
        # {'en':'The sum of the inbound traffic of the enterprise site', 'zh_CN':'企业站点流入流量总和'}
        self.sum_site_in_flow = sum_site_in_flow

    def validate(self):
        self.validate_required(self.sum_site_out_flow, 'sum_site_out_flow')
        self.validate_required(self.sum_site_in_flow, 'sum_site_in_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sum_site_out_flow is not None:
            result['sumSiteOutFlow'] = self.sum_site_out_flow
        if self.sum_site_in_flow is not None:
            result['sumSiteInFlow'] = self.sum_site_in_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sumSiteOutFlow') is not None:
            self.sum_site_out_flow = m.get('sumSiteOutFlow')
        if m.get('sumSiteInFlow') is not None:
            self.sum_site_in_flow = m.get('sumSiteInFlow')
        return self


class AllSiteSumFlowResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: AllSiteSumFlowResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = AllSiteSumFlowResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class AllSiteSumFlowPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AllSiteSumFlowParameters(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"start time", "zh_CN":"1、查询的开始时间，格式：yyyy-mm-dd
        # 2、必须小于当前时间和endtime；
        # 3、startTime和endTime相差不能超过31天；（可联系技术支持调整）
        # 4、只能查询最近半年内数据。"}
        self.start_time = start_time
        # {"en":"end time", "zh_CN":"1、查询的结束时间，格式：yyyy-mm-dd
        # 2、必须小于当前时间，大于或等于starttime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）；
        # 4、如果起始时间、结束时间是当天，且不满一天，那就查询从00:00到查询时刻的站点累计流量。
        # 4、只能查询最近半年内数据。"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class AllSiteSumFlowRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AllSiteSumFlowResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SiteMsDeviceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteMsDeviceResponseContentDetails(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        site_id: int = None,
        device_num: int = None,
        master: str = None,
        slave: str = None,
    ):
        # {'en':'site name', 'zh_CN':'站点名称'}
        self.site_name = site_name
        # {'en':'site Id', 'zh_CN':'站点 ID'}
        self.site_id = site_id
        # {'en':'deviceNum num', 'zh_CN':'设备数量'}
        self.device_num = device_num
        # {'en':'master site name', 'zh_CN':'主用设备名称'}
        self.master = master
        # {'en':'slave site name', 'zh_CN':'备用设备名称'}
        self.slave = slave

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_id, 'site_id')
        self.validate_required(self.device_num, 'device_num')
        self.validate_required(self.master, 'master')
        self.validate_required(self.slave, 'slave')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.site_id is not None:
            result['siteId'] = self.site_id
        if self.device_num is not None:
            result['deviceNum'] = self.device_num
        if self.master is not None:
            result['master'] = self.master
        if self.slave is not None:
            result['slave'] = self.slave
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('siteId') is not None:
            self.site_id = m.get('siteId')
        if m.get('deviceNum') is not None:
            self.device_num = m.get('deviceNum')
        if m.get('master') is not None:
            self.master = m.get('master')
        if m.get('slave') is not None:
            self.slave = m.get('slave')
        return self


class SiteMsDeviceResponseContent(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        details: SiteMsDeviceResponseContentDetails = None,
    ):
        # {'en':'query time', 'zh_CN':'查询时间'}
        self.time_stamp = time_stamp
        # {'en':'Use of site equipment', 'zh_CN':'站点设备的使用情况'}
        self.details = details

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.details, 'details')
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['timeStamp'] = self.time_stamp
        if self.details is not None:
            result['details'] = self.details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeStamp') is not None:
            self.time_stamp = m.get('timeStamp')
        if m.get('details') is not None:
            temp_model = SiteMsDeviceResponseContentDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class SiteMsDeviceResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: List[SiteMsDeviceResponseContent] = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = SiteMsDeviceResponseContent()
                self.content.append(temp_model.from_map(k))
        return self


class SiteMsDevicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteMsDeviceParameters(TeaModel):
    def __init__(
        self,
        site_name: str = None,
    ):
        # {'en':'Site name(Only support querying CPE sites)
        # This parameter can be unspecified; if not specified, it queries all CPE sites of the enterprise for their primary and backup equipment', 'zh_CN':'站点名称(只支持查询CPE站点)
        # 该参数可不指定，不指定时，查询企业的所有CPE站点的主用、备用设备情况'}
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        return self


class SiteMsDeviceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteMsDeviceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SiteSessionInfoRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteSessionInfoResponseContentContent(TeaModel):
    def __init__(
        self,
        src_ip: str = None,
        src_port: int = None,
        dest_ip: str = None,
        dest_port: int = None,
        protocol: str = None,
        flow: int = None,
    ):
        # {'en':'Original IP', 'zh_CN':'原始IP'}
        self.src_ip = src_ip
        # {'en':'Original Port', 'zh_CN':'原始端口'}
        self.src_port = src_port
        # {'en':'Destination IP', 'zh_CN':'目的IP'}
        self.dest_ip = dest_ip
        # {'en':'Destination Port', 'zh_CN':'目的端口'}
        self.dest_port = dest_port
        # {'en':'protocol', 'zh_CN':'协议'}
        self.protocol = protocol
        # {'en':'Flow size in byte', 'zh_CN':'流量大小，单位byte'}
        self.flow = flow

    def validate(self):
        self.validate_required(self.src_ip, 'src_ip')
        self.validate_required(self.src_port, 'src_port')
        self.validate_required(self.dest_ip, 'dest_ip')
        self.validate_required(self.dest_port, 'dest_port')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.flow, 'flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_ip is not None:
            result['srcIp'] = self.src_ip
        if self.src_port is not None:
            result['srcPort'] = self.src_port
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.flow is not None:
            result['flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcIp') is not None:
            self.src_ip = m.get('srcIp')
        if m.get('srcPort') is not None:
            self.src_port = m.get('srcPort')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        return self


class SiteSessionInfoResponseContent(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        site_id: int = None,
        content: List[SiteSessionInfoResponseContentContent] = None,
    ):
        # {'en':'site name', 'zh_CN':'站点名称'}
        self.site_name = site_name
        # {'en':'site Id', 'zh_CN':'站点 ID'}
        self.site_id = site_id
        # {'en':'Session data', 'zh_CN':'会话数据'}
        self.content = content

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_id, 'site_id')
        self.validate_required(self.content, 'content')
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.site_id is not None:
            result['siteId'] = self.site_id
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('siteId') is not None:
            self.site_id = m.get('siteId')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = SiteSessionInfoResponseContentContent()
                self.content.append(temp_model.from_map(k))
        return self


class SiteSessionInfoResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: SiteSessionInfoResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = SiteSessionInfoResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SiteSessionInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteSessionInfoParameters(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {'en':'Site name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_name = site_name
        # {'en':'1.the start time of the query, in the format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time and endtime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的开始时间，格式：yyyy-mm-ddThh:mm:ss 或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间和endtime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.start_time = start_time
        # {'en':'1.the end time of the query, format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time, more than starttime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的结束时间，格式：yyyy-mm-ddThh:mm:ss或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间，大于starttime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class SiteSessionInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteSessionInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SiteTotalFlowChartRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteTotalFlowChartResponseContentBandwidths(TeaModel):
    def __init__(
        self,
        time_stamp: List[int] = None,
        time_data: List[str] = None,
        up_stream_bandwidth: List[int] = None,
        down_stream_bandwidth: List[int] = None,
    ):
        # {'en':'timeStamp', 'zh_CN':'时间戳'}
        self.time_stamp = time_stamp
        # {'en':'Time slice', 'zh_CN':'时间分片'}
        self.time_data = time_data
        # {'en':'1min granularity, showing direct uplink bandwidth, 5min granularity, showing average uplink bandwidth over 5min, unit is byte', 'zh_CN':'单位为byte，1min粒度，直接显示上行流量，5min粒度，显示5min内的平均上行流量，带宽(Mbps)=流量/1000/1000/60'}
        self.up_stream_bandwidth = up_stream_bandwidth
        # {'en':'1min granularity, showing direct downlink bandwidth, 5min granularity, showing average downlink bandwidth over 5min, unit is byte', 'zh_CN':'单位为byte，1min粒度，直接显示下行流量，5min粒度，显示5min内的平均下行流量，带宽（Mbps）=流量/1000/1000/60'}
        self.down_stream_bandwidth = down_stream_bandwidth

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.time_data, 'time_data')
        self.validate_required(self.up_stream_bandwidth, 'up_stream_bandwidth')
        self.validate_required(self.down_stream_bandwidth, 'down_stream_bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['timeStamp'] = self.time_stamp
        if self.time_data is not None:
            result['timeData'] = self.time_data
        if self.up_stream_bandwidth is not None:
            result['upStreamBandwidth'] = self.up_stream_bandwidth
        if self.down_stream_bandwidth is not None:
            result['downStreamBandwidth'] = self.down_stream_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeStamp') is not None:
            self.time_stamp = m.get('timeStamp')
        if m.get('timeData') is not None:
            self.time_data = m.get('timeData')
        if m.get('upStreamBandwidth') is not None:
            self.up_stream_bandwidth = m.get('upStreamBandwidth')
        if m.get('downStreamBandwidth') is not None:
            self.down_stream_bandwidth = m.get('downStreamBandwidth')
        return self


class SiteTotalFlowChartResponseContent(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        site_id: int = None,
        allocate_bandwidth: int = None,
        bandwidths: SiteTotalFlowChartResponseContentBandwidths = None,
    ):
        # {'en':'site name', 'zh_CN':'站点名称'}
        self.site_name = site_name
        # {'en':'site Id', 'zh_CN':'站点 ID'}
        self.site_id = site_id
        # {'en':'Allocated bandwidth in Mbps', 'zh_CN':'分配带宽，单位：Mbps'}
        self.allocate_bandwidth = allocate_bandwidth
        # {'en':'Bandwidth trend data', 'zh_CN':'带宽趋势数据'}
        self.bandwidths = bandwidths

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_id, 'site_id')
        self.validate_required(self.allocate_bandwidth, 'allocate_bandwidth')
        self.validate_required(self.bandwidths, 'bandwidths')
        if self.bandwidths:
            self.bandwidths.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.site_id is not None:
            result['siteId'] = self.site_id
        if self.allocate_bandwidth is not None:
            result['allocateBandwidth'] = self.allocate_bandwidth
        if self.bandwidths is not None:
            result['bandwidths'] = self.bandwidths.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('siteId') is not None:
            self.site_id = m.get('siteId')
        if m.get('allocateBandwidth') is not None:
            self.allocate_bandwidth = m.get('allocateBandwidth')
        if m.get('bandwidths') is not None:
            temp_model = SiteTotalFlowChartResponseContentBandwidths()
            self.bandwidths = temp_model.from_map(m['bandwidths'])
        return self


class SiteTotalFlowChartResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: SiteTotalFlowChartResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = SiteTotalFlowChartResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SiteTotalFlowChartPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteTotalFlowChartParameters(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        start_time: str = None,
        end_time: str = None,
        chart_accuracy: int = None,
    ):
        # {'en':'Site name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_name = site_name
        # {'en':'1.the start time of the query, in the format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time and endtime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的开始时间，格式：yyyy-mm-ddThh:mm:ss 或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间和endtime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.start_time = start_time
        # {'en':'1.the end time of the query, format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time, more than starttime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的结束时间，格式：yyyy-mm-ddThh:mm:ss或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间，大于starttime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.end_time = end_time
        # {'en':'Time interval, enumerated
        # 1 = 1 minute
        # 2 = 5 minutes
        # No pass default 5 minutes', 'zh_CN':'时间间隔，枚举
        # 1 = 1分钟
        # 2 = 5分钟
        # 不传默认5分钟'}
        self.chart_accuracy = chart_accuracy

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.chart_accuracy is not None:
            result['chartAccuracy'] = self.chart_accuracy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('chartAccuracy') is not None:
            self.chart_accuracy = m.get('chartAccuracy')
        return self


class SiteTotalFlowChartRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteTotalFlowChartResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SaasSessionRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaasSessionResponseContentContent(TeaModel):
    def __init__(
        self,
        src_ip: str = None,
        src_port: int = None,
        dest_ip: str = None,
        dest_port: int = None,
        protocol: str = None,
        rx: int = None,
        tx: int = None,
        sumflow: int = None,
    ):
        # {'en':'Original IP', 'zh_CN':'原始IP'}
        self.src_ip = src_ip
        # {'en':'Original Port', 'zh_CN':'原始端口'}
        self.src_port = src_port
        # {'en':'Destination IP', 'zh_CN':'目的IP'}
        self.dest_ip = dest_ip
        # {'en':'Destination Port', 'zh_CN':'目的端口'}
        self.dest_port = dest_port
        # {'en':'protocol', 'zh_CN':'协议'}
        self.protocol = protocol
        # {'en':'inFlow size in byte', 'zh_CN':'流入流量大小，单位byte'}
        self.rx = rx
        # {'en':'outFlow size in byte', 'zh_CN':'流出流量大小，单位byte'}
        self.tx = tx
        # {'en':'sumFlow size in byte', 'zh_CN':'流入流出流量大小，单位byte'}
        self.sumflow = sumflow

    def validate(self):
        self.validate_required(self.src_ip, 'src_ip')
        self.validate_required(self.src_port, 'src_port')
        self.validate_required(self.dest_ip, 'dest_ip')
        self.validate_required(self.dest_port, 'dest_port')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.rx, 'rx')
        self.validate_required(self.tx, 'tx')
        self.validate_required(self.sumflow, 'sumflow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_ip is not None:
            result['srcIp'] = self.src_ip
        if self.src_port is not None:
            result['srcPort'] = self.src_port
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.rx is not None:
            result['rx'] = self.rx
        if self.tx is not None:
            result['tx'] = self.tx
        if self.sumflow is not None:
            result['sumflow'] = self.sumflow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('srcIp') is not None:
            self.src_ip = m.get('srcIp')
        if m.get('srcPort') is not None:
            self.src_port = m.get('srcPort')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('rx') is not None:
            self.rx = m.get('rx')
        if m.get('tx') is not None:
            self.tx = m.get('tx')
        if m.get('sumflow') is not None:
            self.sumflow = m.get('sumflow')
        return self


class SaasSessionResponseContent(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        site_id: int = None,
        content: List[SaasSessionResponseContentContent] = None,
    ):
        # {'en':'site name', 'zh_CN':'站点名称'}
        self.site_name = site_name
        # {'en':'site Id', 'zh_CN':'站点 ID'}
        self.site_id = site_id
        # {'en':'Session data', 'zh_CN':'会话数据'}
        self.content = content

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_id, 'site_id')
        self.validate_required(self.content, 'content')
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.site_id is not None:
            result['siteId'] = self.site_id
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('siteId') is not None:
            self.site_id = m.get('siteId')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = SaasSessionResponseContentContent()
                self.content.append(temp_model.from_map(k))
        return self


class SaasSessionResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: SaasSessionResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = SaasSessionResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SaasSessionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaasSessionParameters(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        start_time: str = None,
        end_time: str = None,
        ip: str = None,
        port: int = None,
    ):
        # {'en':'Site name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_name = site_name
        # {'en':'1.the start time of the query, in the format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time and endtime
        # 3.the difference between startTime and endTime cannot exceed 6 hours (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的开始时间，格式：yyyy-mm-ddThh:mm:ss 或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间和endtime
        # 3、startTime和endTime相差不能超过6小时（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.start_time = start_time
        # {'en':'1.the end time of the query, format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time, more than starttime
        # 3.the difference between startTime and endTime cannot exceed 6 hours (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的结束时间，格式：yyyy-mm-ddThh:mm:ss或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间，大于starttime
        # 3、startTime和endTime相差不能超过6小时（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.end_time = end_time
        # {'zh_CN':'查询IP地址（不区分源IP、目的IP）','en':'Source IP And Destination IP'}
        self.ip = ip
        # {'zh_CN':'查询端口（不区分源端口、目的端口）','en':'Source Port And Destination Port'}
        self.port = port

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ip is not None:
            result['ip'] = self.ip
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class SaasSessionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SaasSessionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SiteLogicChartRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteLogicChartResponseContentQuality(TeaModel):
    def __init__(
        self,
        time_stamp: List[int] = None,
        time_data: List[str] = None,
        rtt: List[int] = None,
        loss: List[int] = None,
        mdev: List[int] = None,
    ):
        # {'en':'timeStamp', 'zh_CN':'时间戳'}
        self.time_stamp = time_stamp
        # {'en':'Time slice', 'zh_CN':'时间分片'}
        self.time_data = time_data
        # {'en':'Time delay', 'zh_CN':'时延'}
        self.rtt = rtt
        # {'en':'Packet loss rate', 'zh_CN':'丢包率'}
        self.loss = loss
        # {'en':'jitter', 'zh_CN':'抖动'}
        self.mdev = mdev

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.time_data, 'time_data')
        self.validate_required(self.rtt, 'rtt')
        self.validate_required(self.loss, 'loss')
        self.validate_required(self.mdev, 'mdev')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['timeStamp'] = self.time_stamp
        if self.time_data is not None:
            result['timeData'] = self.time_data
        if self.rtt is not None:
            result['rtt'] = self.rtt
        if self.loss is not None:
            result['loss'] = self.loss
        if self.mdev is not None:
            result['mdev'] = self.mdev
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeStamp') is not None:
            self.time_stamp = m.get('timeStamp')
        if m.get('timeData') is not None:
            self.time_data = m.get('timeData')
        if m.get('rtt') is not None:
            self.rtt = m.get('rtt')
        if m.get('loss') is not None:
            self.loss = m.get('loss')
        if m.get('mdev') is not None:
            self.mdev = m.get('mdev')
        return self


class SiteLogicChartResponseContent(TeaModel):
    def __init__(
        self,
        site_aname: str = None,
        site_bname: str = None,
        site_aid: int = None,
        site_bid: int = None,
        status: int = None,
        quality: SiteLogicChartResponseContentQuality = None,
    ):
        # {'en':'site A name', 'zh_CN':'站点A名称'}
        self.site_aname = site_aname
        # {'en':'site B name', 'zh_CN':'站点B名称'}
        self.site_bname = site_bname
        # {'en':'site A Id', 'zh_CN':'站点A ID'}
        self.site_aid = site_aid
        # {'en':'site B Id', 'zh_CN':'站点B ID'}
        self.site_bid = site_bid
        # {'en':'tunnel status 0-unknown, 1-online, 2-offline, 3-not reported, 4-suspend', 'zh_CN':'链路状态0–未知，1–在线，2-离线，3-未上报，4-挂起'}
        self.status = status
        # {'en':'Quality trend data', 'zh_CN':'质量趋势数据'}
        self.quality = quality

    def validate(self):
        self.validate_required(self.site_aname, 'site_aname')
        self.validate_required(self.site_bname, 'site_bname')
        self.validate_required(self.site_aid, 'site_aid')
        self.validate_required(self.site_bid, 'site_bid')
        self.validate_required(self.status, 'status')
        self.validate_required(self.quality, 'quality')
        if self.quality:
            self.quality.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_aname is not None:
            result['siteAName'] = self.site_aname
        if self.site_bname is not None:
            result['siteBName'] = self.site_bname
        if self.site_aid is not None:
            result['siteAId'] = self.site_aid
        if self.site_bid is not None:
            result['siteBId'] = self.site_bid
        if self.status is not None:
            result['status'] = self.status
        if self.quality is not None:
            result['quality'] = self.quality.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteAName') is not None:
            self.site_aname = m.get('siteAName')
        if m.get('siteBName') is not None:
            self.site_bname = m.get('siteBName')
        if m.get('siteAId') is not None:
            self.site_aid = m.get('siteAId')
        if m.get('siteBId') is not None:
            self.site_bid = m.get('siteBId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('quality') is not None:
            temp_model = SiteLogicChartResponseContentQuality()
            self.quality = temp_model.from_map(m['quality'])
        return self


class SiteLogicChartResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: SiteLogicChartResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = SiteLogicChartResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SiteLogicChartPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteLogicChartParameters(TeaModel):
    def __init__(
        self,
        site_aname: str = None,
        site_bname: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {'en':'Site A name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点A名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_aname = site_aname
        # {'en':'Site B name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点B名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_bname = site_bname
        # {'en':'1.the start time of the query, in the format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time and endtime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的开始时间，格式：yyyy-mm-ddThh:mm:ss 或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间和endtime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.start_time = start_time
        # {'en':'1.the end time of the query, format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time, more than starttime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的结束时间，格式：yyyy-mm-ddThh:mm:ss或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间，大于starttime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.site_aname, 'site_aname')
        self.validate_required(self.site_bname, 'site_bname')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_aname is not None:
            result['siteAName'] = self.site_aname
        if self.site_bname is not None:
            result['siteBName'] = self.site_bname
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteAName') is not None:
            self.site_aname = m.get('siteAName')
        if m.get('siteBName') is not None:
            self.site_bname = m.get('siteBName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class SiteLogicChartRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteLogicChartResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SiteQualityChartRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteQualityChartResponseContentTunnel(TeaModel):
    def __init__(
        self,
        tunnel_name: str = None,
        tunnel_id: int = None,
        status: int = None,
        time_stamp: List[int] = None,
        time_data: List[str] = None,
        rtt: List[int] = None,
        loss: List[int] = None,
        mdev: List[int] = None,
    ):
        # {'en':'tunnel name', 'zh_CN':'链路名称'}
        self.tunnel_name = tunnel_name
        # {'en':'tunnel Id', 'zh_CN':'链路 ID'}
        self.tunnel_id = tunnel_id
        # {'en':'tunnel status 0-unknown, 1-online, 2-offline, 3-not reported, 4-suspend', 'zh_CN':'链路状态0–未知，1–在线，2-离线，3-未上报，4-挂起'}
        self.status = status
        # {'en':'timeStamp', 'zh_CN':'时间戳'}
        self.time_stamp = time_stamp
        # {'en':'Time slice', 'zh_CN':'时间分片'}
        self.time_data = time_data
        # {'en':'Time delay', 'zh_CN':'时延'}
        self.rtt = rtt
        # {'en':'Packet loss rate', 'zh_CN':'丢包率'}
        self.loss = loss
        # {'en':'jitter', 'zh_CN':'抖动'}
        self.mdev = mdev

    def validate(self):
        self.validate_required(self.tunnel_name, 'tunnel_name')
        self.validate_required(self.tunnel_id, 'tunnel_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.time_data, 'time_data')
        self.validate_required(self.rtt, 'rtt')
        self.validate_required(self.loss, 'loss')
        self.validate_required(self.mdev, 'mdev')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_name is not None:
            result['tunnelName'] = self.tunnel_name
        if self.tunnel_id is not None:
            result['tunnelId'] = self.tunnel_id
        if self.status is not None:
            result['status'] = self.status
        if self.time_stamp is not None:
            result['timeStamp'] = self.time_stamp
        if self.time_data is not None:
            result['timeData'] = self.time_data
        if self.rtt is not None:
            result['rtt'] = self.rtt
        if self.loss is not None:
            result['loss'] = self.loss
        if self.mdev is not None:
            result['mdev'] = self.mdev
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tunnelName') is not None:
            self.tunnel_name = m.get('tunnelName')
        if m.get('tunnelId') is not None:
            self.tunnel_id = m.get('tunnelId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timeStamp') is not None:
            self.time_stamp = m.get('timeStamp')
        if m.get('timeData') is not None:
            self.time_data = m.get('timeData')
        if m.get('rtt') is not None:
            self.rtt = m.get('rtt')
        if m.get('loss') is not None:
            self.loss = m.get('loss')
        if m.get('mdev') is not None:
            self.mdev = m.get('mdev')
        return self


class SiteQualityChartResponseContent(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        site_id: int = None,
        tunnel: List[SiteQualityChartResponseContentTunnel] = None,
    ):
        # {'en':'site name', 'zh_CN':'站点名称'}
        self.site_name = site_name
        # {'en':'site Id', 'zh_CN':'站点 ID'}
        self.site_id = site_id
        # {'en':'Tunnel quality data under site', 'zh_CN':'站点下的隧道质量数据'}
        self.tunnel = tunnel

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_id, 'site_id')
        self.validate_required(self.tunnel, 'tunnel')
        if self.tunnel:
            for k in self.tunnel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.site_id is not None:
            result['siteId'] = self.site_id
        if self.tunnel is not None:
            result['tunnel'] = []
            for k in self.tunnel:
                result['tunnel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('siteId') is not None:
            self.site_id = m.get('siteId')
        if m.get('tunnel') is not None:
            self.tunnel = []
            for k in m.get('tunnel'):
                temp_model = SiteQualityChartResponseContentTunnel()
                self.tunnel.append(temp_model.from_map(k))
        return self


class SiteQualityChartResponse(TeaModel):
    def __init__(
        self,
        return_code: int = None,
        return_msg: str = None,
        content: SiteQualityChartResponseContent = None,
    ):
        # {'en':'Interface status codes', 'zh_CN':'接口状态码'}
        self.return_code = return_code
        # {'en':'Interface information', 'zh_CN':'接口信息'}
        self.return_msg = return_msg
        # {'en':'response content', 'zh_CN':'响应内容'}
        self.content = content

    def validate(self):
        self.validate_required(self.return_code, 'return_code')
        self.validate_required(self.return_msg, 'return_msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['returnCode'] = self.return_code
        if self.return_msg is not None:
            result['returnMsg'] = self.return_msg
        if self.content is not None:
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnCode') is not None:
            self.return_code = m.get('returnCode')
        if m.get('returnMsg') is not None:
            self.return_msg = m.get('returnMsg')
        if m.get('content') is not None:
            temp_model = SiteQualityChartResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class SiteQualityChartPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteQualityChartParameters(TeaModel):
    def __init__(
        self,
        site_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {'en':'Site name
        # When this parameter must be specified, query the specified site data', 'zh_CN':'站点名称
        # 该参数必须指定时，查询指定的站点数据'}
        self.site_name = site_name
        # {'en':'1.the start time of the query, in the format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time and endtime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的开始时间，格式：yyyy-mm-ddThh:mm:ss 或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间和endtime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.start_time = start_time
        # {'en':'1.the end time of the query, format: yyyy-mm-ddThh:mm:ss or yyyy-mm-ddThh:mm
        # 2.must be less than the current time, more than starttime
        # 3.the difference between startTime and endTime cannot exceed 31 days (can be adjusted by contacting technical support)
        # 4.can only query the last six months of data', 'zh_CN':'1、查询的结束时间，格式：yyyy-mm-ddThh:mm:ss或 yyyy-mm-ddThh:mm
        # 2、必须小于当前时间，大于starttime
        # 3、startTime和endTime相差不能超过31天（可联系技术支持调整）
        # 4、只能查询最近半年内数据'}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_name is not None:
            result['siteName'] = self.site_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('siteName') is not None:
            self.site_name = m.get('siteName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class SiteQualityChartRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SiteQualityChartResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




