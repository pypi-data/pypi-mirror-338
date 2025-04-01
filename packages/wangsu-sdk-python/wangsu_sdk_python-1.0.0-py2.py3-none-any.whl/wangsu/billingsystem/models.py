# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryUsedNodesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryUsedNodesResponse(TeaModel):
    def __init__(
        self,
        nodes: List[str] = None,
    ):
        # {"en":"the nodes that have been used", "zh_CN":"使用过的节点列表"}
        self.nodes = nodes

    def validate(self):
        self.validate_required(self.nodes, 'nodes')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        return self


class QueryUsedNodesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryUsedNodesParameters(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"startTime", "zh_CN":"起始时间，格式为：yyyy-MM-dd"}
        self.start_time = start_time
        # {"en":"endTime", "zh_CN":"截止时间，格式为：yyyy-MM-dd"}
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


class QueryUsedNodesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryUsedNodesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBillingDetailsOfComputingServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBillingDetailsOfComputingServiceServerBill(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
        is_bm: int = None,
        state: str = None,
        node_name: str = None,
        node_name_cn: str = None,
        charge_region: str = None,
        instance_type: str = None,
        server_feature: str = None,
        period_start_time: str = None,
        period_end_time: str = None,
        period_days: int = None,
        period_count: float = None,
    ):
        # {"en":"Instance id", "zh_CN":"实例id"}
        self.id = id
        # {"en":"Instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Instance IPv4", "zh_CN":"实例IPv4"}
        self.ipv_4 = ipv_4
        # {"en":"Instance IPv6", "zh_CN":"实例IPv6"}
        self.ipv_6 = ipv_6
        # {"en":"Instance type:1---Bare metal instance;-1:Virtual machine instance", "zh_CN":"实例类型
        # 1：裸机实例,-1：虚拟机实例"}
        self.is_bm = is_bm
        # {"en":"Instance Status:
        # RUNNING
        # STOPPED
        # ERROR
        # DELETED
        # RESTARTING
        # STARTING
        # STOPPING
        # SNAPSHOTTING
        # REBUILDING
        # MIGRATING
        # ", "zh_CN":"实例状态
        # RUNNING	运行状态
        # STOPPED	停机
        # ERROR	错误
        # DELETED	已销毁
        # RESTARTING  重启中
        # STARTING  启动中
        # STOPPING  停止中
        # SNAPSHOTTING  制作快照镜像中
        # REBUILDING 重建中
        # MIGRATING 迁移中"}
        self.state = state
        # {"en":"Node name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"Node Chinese Name", "zh_CN":"节点中文名称"}
        self.node_name_cn = node_name_cn
        # {"en":"Charge region", "zh_CN":"计费区域，14个取值：
        # 中国大陆
        # 亚太
        # 香港
        # 台湾
        # 美洲
        # 欧洲
        # 中东
        # 非洲
        # 台湾 
        # 香港
        # 非洲
        # 南美
        # 澳大利亚
        # 印度"}
        self.charge_region = charge_region
        # {"en":"Instance spec", "zh_CN":"实例规格"}
        self.instance_type = instance_type
        # {"en":"Instance configuration, including CPU, memory, and disk specifications information of the virtual machine", "zh_CN":"实例配置，包含虚拟机的CPU、内存、磁盘规格信息"}
        self.server_feature = server_feature
        # {"en":"Starting time of use within the accounting period", "zh_CN":"账期内开始使用时间，格式yyyy-MM-dd"}
        self.period_start_time = period_start_time
        # {"en":"End of usage time within the accounting period", "zh_CN":"账期内结束时间，格式yyyy-MM-dd"}
        self.period_end_time = period_end_time
        # {"en":"Usage days within the accounting period", "zh_CN":"账期内使用天数"}
        self.period_days = period_days
        # {"en":"Instance usage during the accounting period", "zh_CN":"账期内实例用量"}
        self.period_count = period_count

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ipv_4, 'ipv_4')
        self.validate_required(self.ipv_6, 'ipv_6')
        self.validate_required(self.is_bm, 'is_bm')
        self.validate_required(self.state, 'state')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.node_name_cn, 'node_name_cn')
        self.validate_required(self.charge_region, 'charge_region')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.server_feature, 'server_feature')
        self.validate_required(self.period_start_time, 'period_start_time')
        self.validate_required(self.period_end_time, 'period_end_time')
        self.validate_required(self.period_days, 'period_days')
        self.validate_required(self.period_count, 'period_count')

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
        if self.is_bm is not None:
            result['isBm'] = self.is_bm
        if self.state is not None:
            result['state'] = self.state
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.node_name_cn is not None:
            result['nodeNameCn'] = self.node_name_cn
        if self.charge_region is not None:
            result['chargeRegion'] = self.charge_region
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.server_feature is not None:
            result['serverFeature'] = self.server_feature
        if self.period_start_time is not None:
            result['periodStartTime'] = self.period_start_time
        if self.period_end_time is not None:
            result['periodEndTime'] = self.period_end_time
        if self.period_days is not None:
            result['periodDays'] = self.period_days
        if self.period_count is not None:
            result['periodCount'] = self.period_count
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
        if m.get('isBm') is not None:
            self.is_bm = m.get('isBm')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('nodeNameCn') is not None:
            self.node_name_cn = m.get('nodeNameCn')
        if m.get('chargeRegion') is not None:
            self.charge_region = m.get('chargeRegion')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('serverFeature') is not None:
            self.server_feature = m.get('serverFeature')
        if m.get('periodStartTime') is not None:
            self.period_start_time = m.get('periodStartTime')
        if m.get('periodEndTime') is not None:
            self.period_end_time = m.get('periodEndTime')
        if m.get('periodDays') is not None:
            self.period_days = m.get('periodDays')
        if m.get('periodCount') is not None:
            self.period_count = m.get('periodCount')
        return self


class QueryBillingDetailsOfComputingServiceResponse(TeaModel):
    def __init__(
        self,
        servers: List[QueryBillingDetailsOfComputingServiceServerBill] = None,
    ):
        # {"en":"Instance computing power information array", "zh_CN":"实例算力信息数组"}
        self.servers = servers

    def validate(self):
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
        if self.servers is not None:
            result['servers'] = []
            for k in self.servers:
                result['servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = []
            for k in m.get('servers'):
                temp_model = QueryBillingDetailsOfComputingServiceServerBill()
                self.servers.append(temp_model.from_map(k))
        return self


class QueryBillingDetailsOfComputingServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBillingDetailsOfComputingServiceParameters(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Starting time of use within the accounting period,format:yyyy-MM-dd", "zh_CN":"账期开始时间，格式yyyy-MM-dd"}
        self.start_time = start_time
        # {"en":"The end time of the accounting period, in the format yyyy-MM-dd. If not filled in, it will be the current time.", "zh_CN":"账期结束时间，格式yyyy-MM-dd，如果未填写则为当前时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.start_time, 'start_time')

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


class QueryBillingDetailsOfComputingServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBillingDetailsOfComputingServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VmNodeInfoForMaxOutAndInRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        isp_id: str = None,
        ip_protocol: str = None,
        node: str = None,
        spec: str = None,
        line_mode: str = None,
        timezone: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到天,日期格式为yyyy-mm-dd 此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到天,日期格式为yyyy-mm-dd 此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried: 1)If there are multiple inputs,use ';' as separator. 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号“;”，不选或者为空时默认为所查询客户的所有频道。"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号“;”分隔开，如查询大陆及亚太区域，参数填写为：“region=cn;apac”。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type. 1)If there are multiple inputs,use ';' as separator. 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号“;”分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"Return result format, supported formats are XML and JSON, default is XML.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"1)If there area multiple inputs,use ';' as demimeter. 2)optional values of isp: refers to the ISP-section of appendix. 3) If not specified,means all the isp.", "zh_CN":"要查询的运营商的缩写，多个isp请用英文分号“;”分隔开。运营商的缩写格式参考附录：具体运行商（ISP）信息的代号。备注：只有当地区只写了“cn”时，填写isp信息才有效。不选或者为空时默认为所有isp。"}
        self.isp_id = isp_id
        # {"en":"IPv4, IPv6, if not specified, search all by default.", "zh_CN":"ipv4、ipv6，不填默认查全部"}
        self.ip_protocol = ip_protocol
        # {"en":"Node names, please separate multiple values with a semicolon ';'", "zh_CN":"节点名称,多个值请用英文分号;分隔"}
        self.node = node
        # {"en":"Instance specifications. Please separate multiple values with a semicolon ';'. If not selected or left blank, it defaults to querying all.", "zh_CN":"实例规格。多个值请用英文分号“;”，不选或者为空时默认为查询所有。"}
        self.spec = spec
        # {"en":"4 types. 0: Storage capacity; 1: Read request count; 2: Write request count; 3: Delete request count. Default is: 0.", "zh_CN":"4种类型。0：存储量；1：读请求数；2：写请求数；3：删请求数。默认取：0"}
        self.line_mode = line_mode
        # {"en":"Greenwich Mean Time (GMT) zone, the parameter format is GMT+09:00 to indicate East 9th Zone, and GMT-09:00 to indicate West 9th Zone. If not provided, the default is the local time zone (East 8th Zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone

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
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.isp_id is not None:
            result['ispId'] = self.isp_id
        if self.ip_protocol is not None:
            result['ipProtocol'] = self.ip_protocol
        if self.node is not None:
            result['node'] = self.node
        if self.spec is not None:
            result['spec'] = self.spec
        if self.line_mode is not None:
            result['lineMode'] = self.line_mode
        if self.timezone is not None:
            result['timezone'] = self.timezone
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
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('ispId') is not None:
            self.isp_id = m.get('ispId')
        if m.get('ipProtocol') is not None:
            self.ip_protocol = m.get('ipProtocol')
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('lineMode') is not None:
            self.line_mode = m.get('lineMode')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class VmNodeInfoForMaxOutAndInResponseData(TeaModel):
    def __init__(
        self,
        node: str = None,
        charge_95value: str = None,
        charge_95time: str = None,
        data_type_for_95: str = None,
        peak_avg_value: str = None,
        peak_1st_value: str = None,
        peak_1st_time: str = None,
        data_type_for_peak: str = None,
        total_flow: str = None,
    ):
        # {"en":"node", "zh_CN":"节点"}
        self.node = node
        # {"en":"95th billing value, unit: Mbps", "zh_CN":"95计费值, 单位Mbps"}
        self.charge_95value = charge_95value
        # {"en":"95th billing time", "zh_CN":"95计费值时刻"}
        self.charge_95time = charge_95time
        # {"en":"Data types corresponding to the 95th percentile value: ein: external inbound bandwidth, eout: external outbound bandwidth", "zh_CN":"95值对应的数据类型：ein:外网流入带宽,eout:外网流出带宽"}
        self.data_type_for_95 = data_type_for_95
        # {"en":"Peak average billing value, unit: Mbps", "zh_CN":"峰值平均计费值, 单位Mbps"}
        self.peak_avg_value = peak_avg_value
        # {"en":"Peak value, unit: Mbps", "zh_CN":"第一峰值, 单位Mbps"}
        self.peak_1st_value = peak_1st_value
        # {"en":"Peak time", "zh_CN":"第一峰值时刻"}
        self.peak_1st_time = peak_1st_time
        # {"en":"Data types corresponding to the peak value: ein: external inbound bandwidth, eout: external outbound bandwidth", "zh_CN":"峰值对应的数据类型：ein:外网流入带宽,eout:外网流出带宽"}
        self.data_type_for_peak = data_type_for_peak
        # {"en":"Total traffic, unit: GB", "zh_CN":"总流量, 单位GB"}
        self.total_flow = total_flow

    def validate(self):
        self.validate_required(self.node, 'node')
        self.validate_required(self.charge_95value, 'charge_95value')
        self.validate_required(self.charge_95time, 'charge_95time')
        self.validate_required(self.data_type_for_95, 'data_type_for_95')
        self.validate_required(self.peak_avg_value, 'peak_avg_value')
        self.validate_required(self.peak_1st_value, 'peak_1st_value')
        self.validate_required(self.peak_1st_time, 'peak_1st_time')
        self.validate_required(self.data_type_for_peak, 'data_type_for_peak')
        self.validate_required(self.total_flow, 'total_flow')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node is not None:
            result['node'] = self.node
        if self.charge_95value is not None:
            result['charge95Value'] = self.charge_95value
        if self.charge_95time is not None:
            result['charge95Time'] = self.charge_95time
        if self.data_type_for_95 is not None:
            result['dataTypeFor95'] = self.data_type_for_95
        if self.peak_avg_value is not None:
            result['peakAvgValue'] = self.peak_avg_value
        if self.peak_1st_value is not None:
            result['peak1stValue'] = self.peak_1st_value
        if self.peak_1st_time is not None:
            result['peak1stTime'] = self.peak_1st_time
        if self.data_type_for_peak is not None:
            result['dataTypeForPeak'] = self.data_type_for_peak
        if self.total_flow is not None:
            result['totalFlow'] = self.total_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('node') is not None:
            self.node = m.get('node')
        if m.get('charge95Value') is not None:
            self.charge_95value = m.get('charge95Value')
        if m.get('charge95Time') is not None:
            self.charge_95time = m.get('charge95Time')
        if m.get('dataTypeFor95') is not None:
            self.data_type_for_95 = m.get('dataTypeFor95')
        if m.get('peakAvgValue') is not None:
            self.peak_avg_value = m.get('peakAvgValue')
        if m.get('peak1stValue') is not None:
            self.peak_1st_value = m.get('peak1stValue')
        if m.get('peak1stTime') is not None:
            self.peak_1st_time = m.get('peak1stTime')
        if m.get('dataTypeForPeak') is not None:
            self.data_type_for_peak = m.get('dataTypeForPeak')
        if m.get('totalFlow') is not None:
            self.total_flow = m.get('totalFlow')
        return self


class VmNodeInfoForMaxOutAndInResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[VmNodeInfoForMaxOutAndInResponseData] = None,
    ):
        # {'en':'status code', 'zh_CN':'状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'消息'}
        self.message = message
        # {'en':'bandwidth', 'zh_CN':'统计数据'}
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
                temp_model = VmNodeInfoForMaxOutAndInResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class VmNodeInfoForMaxOutAndInPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmNodeInfoForMaxOutAndInParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmNodeInfoForMaxOutAndInRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VmNodeInfoForMaxOutAndInResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




