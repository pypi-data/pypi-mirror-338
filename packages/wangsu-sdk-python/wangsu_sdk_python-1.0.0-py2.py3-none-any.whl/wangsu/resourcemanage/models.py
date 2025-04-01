# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VMPQueryFlavorRequest(TeaModel):
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


class VMPQueryFlavorDisk(TeaModel):
    def __init__(
        self,
        type: str = None,
        size: int = None,
        category: str = None,
    ):
        # {"en":"disk type ,system disk or data disk", "zh_CN":"磁盘类型,数据盘或者系统盘"}
        self.type = type
        # {"en":"VMPQueryFlavorDisk space size in GB", "zh_CN":"磁盘空间大小，单位是GB"}
        self.size = size
        # {"en":"VMPQueryFlavorDisk type, value:HDD: ordinary hard disk,SSD: solid state drive,The default is HDD", "zh_CN":"磁盘类型，取值：HDD：普通硬盘,SSD：固态硬盘,默认是HDD"}
        self.category = category

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.size, 'size')
        self.validate_required(self.category, 'category')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.size is not None:
            result['size'] = self.size
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class VMPQueryFlavorResponse(TeaModel):
    def __init__(
        self,
        flavors: List[str] = None,
        id: str = None,
        name: str = None,
        vcpus: int = None,
        ram: int = None,
        disks: List[VMPQueryFlavorDisk] = None,
        bandwidth: int = None,
        is_bm: int = None,
        sys_ssd_limit: int = None,
        sys_hdd_limit: int = None,
        data_ssd_limit: int = None,
        data_hdd_limit: int = None,
        type: str = None,
    ):
        # {"en":"flavors", "zh_CN":"规格"}
        self.flavors = flavors
        # {"en":"Unique identification of virtual machine specification, global unique", "zh_CN":"实例规格唯一标识，全局唯一"}
        self.id = id
        # {"en":"form name", "zh_CN":"规格名称"}
        self.name = name
        # {"en":"Number of CPUs of virtual machine", "zh_CN":"实例的cpu数"}
        self.vcpus = vcpus
        # {"en":"Virtual machine memory in GB", "zh_CN":"实例内存,单位是GB"}
        self.ram = ram
        # {"en":"VMPQueryFlavorDisk information of virtual machine", "zh_CN":"实例的磁盘信息"}
        self.disks = disks
        # {"en":"Bearable bandwidth, Mbps", "zh_CN":"可承载带宽，单位是Mbps"}
        self.bandwidth = bandwidth
        # {"en":"1: Yes, -1: No,1 means the template is bare metal template;,-1 indicates that the template is a cloud host template;", "zh_CN":"1：是，-1：否,1表示该模板是裸机模板；-1表示该模板是云主机模板；"}
        self.is_bm = is_bm
        # {"en":"SSD system disk quota (GB). This parameter has no meaning if it is a bare-metal template or a stand-alone disk template", "zh_CN":"SSD系统盘限额（GB），如果是裸机模板或者是独立盘模板，该参数无意义"}
        self.sys_ssd_limit = sys_ssd_limit
        # {"en":"HDD system disk quota (GB). If it is a bare-metal template or a stand-alone template, this parameter has no meaning", "zh_CN":"HDD系统盘限额（GB），如果是裸机模板或者是独立盘模板，该参数无意义"}
        self.sys_hdd_limit = sys_hdd_limit
        # {"en":"SSD disk quota (GB). This parameter has no meaning if it is a bare-metal template or a stand-alone disk template", "zh_CN":"SSD数据盘限额（GB），如果是裸机模板或者是独立盘模板，该参数无意义"}
        self.data_ssd_limit = data_ssd_limit
        # {"en":"HDD disk quota (GB). This parameter has no meaning if it is a bare-metal template or a stand-alone disk template", "zh_CN":"HDD数据盘限额（GB），如果是裸机模板或者是独立盘模板，该参数无意义"}
        self.data_hdd_limit = data_hdd_limit
        # {"en":"Template type,Values: 201- public template, 202- custom template", "zh_CN":"模板类型,取值：201-公共模板、202-自定义模板"}
        self.type = type

    def validate(self):
        self.validate_required(self.flavors, 'flavors')
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.vcpus, 'vcpus')
        self.validate_required(self.ram, 'ram')
        self.validate_required(self.disks, 'disks')
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.is_bm, 'is_bm')
        self.validate_required(self.sys_ssd_limit, 'sys_ssd_limit')
        self.validate_required(self.sys_hdd_limit, 'sys_hdd_limit')
        self.validate_required(self.data_ssd_limit, 'data_ssd_limit')
        self.validate_required(self.data_hdd_limit, 'data_hdd_limit')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flavors is not None:
            result['flavors'] = self.flavors
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.vcpus is not None:
            result['vcpus'] = self.vcpus
        if self.ram is not None:
            result['ram'] = self.ram
        if self.disks is not None:
            result['disks'] = []
            for k in self.disks:
                result['disks'].append(k.to_map() if k else None)
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.is_bm is not None:
            result['isBm'] = self.is_bm
        if self.sys_ssd_limit is not None:
            result['sysSsdLimit'] = self.sys_ssd_limit
        if self.sys_hdd_limit is not None:
            result['sysHddLimit'] = self.sys_hdd_limit
        if self.data_ssd_limit is not None:
            result['dataSsdLimit'] = self.data_ssd_limit
        if self.data_hdd_limit is not None:
            result['dataHddLimit'] = self.data_hdd_limit
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flavors') is not None:
            self.flavors = m.get('flavors')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vcpus') is not None:
            self.vcpus = m.get('vcpus')
        if m.get('ram') is not None:
            self.ram = m.get('ram')
        if m.get('disks') is not None:
            self.disks = []
            for k in m.get('disks'):
                temp_model = VMPQueryFlavorDisk()
                self.disks.append(temp_model.from_map(k))
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('isBm') is not None:
            self.is_bm = m.get('isBm')
        if m.get('sysSsdLimit') is not None:
            self.sys_ssd_limit = m.get('sysSsdLimit')
        if m.get('sysHddLimit') is not None:
            self.sys_hdd_limit = m.get('sysHddLimit')
        if m.get('dataSsdLimit') is not None:
            self.data_ssd_limit = m.get('dataSsdLimit')
        if m.get('dataHddLimit') is not None:
            self.data_hdd_limit = m.get('dataHddLimit')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class VMPQueryFlavorPaths(TeaModel):
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


class VMPQueryFlavorParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # {"en":"The virtual machine specification is a unique identifier. Multiple values are separated by commas.Can be left blank, and when left blank, all available template specifications will be returned.", "zh_CN":"实例规格唯一标识，多个值用英文逗号分隔。可放空不填，不填时返回所有可用模板规格。"}
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class VMPQueryFlavorRequestHeader(TeaModel):
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


class VMPQueryFlavorResponseHeader(TeaModel):
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






class VMPQueryNodeRequest(TeaModel):
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


class VMPQueryNodeResponse(TeaModel):
    def __init__(
        self,
        nodes: List[str] = None,
        name: str = None,
        region_name: str = None,
        province: str = None,
        carrier: str = None,
        state: str = None,
        line_type: str = None,
        ipv_6supported: str = None,
        bm_supported: str = None,
    ):
        # {"en":"Node information array", "zh_CN":"节点信息数组"}
        self.nodes = nodes
        # {"en":"Node name, unique", "zh_CN":"节点名称，唯一"}
        self.name = name
        # {"en":"Node area", "zh_CN":"节点所在区域"}
        self.region_name = region_name
        # {"en":"Province of node", "zh_CN":"节点所在省份"}
        self.province = province
        # {"en":"If the node is a multi line node, multiple operators will be returned, separated by '/'", "zh_CN":"节点所在运营商，如果是多线节点，则返回多个运营商，以'/'分隔"}
        self.carrier = carrier
        # {"en":"Node status: running - node available; maintenance - node in maintenance, temporarily unavailable", "zh_CN":"节点状态：RUNNING ---节点可用；MAINTENANCE ---节点维护中，暂时不可用"}
        self.state = state
        # {"en":"Line typenode", "zh_CN":"线路类型"}
        self.line_type = line_type
        # {"en":"IPv6 supported", "zh_CN":"是否支持ipv6"}
        self.ipv_6supported = ipv_6supported
        # {"en":"Whether the node has bare metal resources", "zh_CN":"该节点是否有裸机资源"}
        self.bm_supported = bm_supported

    def validate(self):
        self.validate_required(self.nodes, 'nodes')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_name, 'region_name')
        self.validate_required(self.province, 'province')
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.state, 'state')
        self.validate_required(self.line_type, 'line_type')
        self.validate_required(self.ipv_6supported, 'ipv_6supported')
        self.validate_required(self.bm_supported, 'bm_supported')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.name is not None:
            result['name'] = self.name
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.state is not None:
            result['state'] = self.state
        if self.line_type is not None:
            result['lineType'] = self.line_type
        if self.ipv_6supported is not None:
            result['ipv6Supported'] = self.ipv_6supported
        if self.bm_supported is not None:
            result['bmSupported'] = self.bm_supported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('lineType') is not None:
            self.line_type = m.get('lineType')
        if m.get('ipv6Supported') is not None:
            self.ipv_6supported = m.get('ipv6Supported')
        if m.get('bmSupported') is not None:
            self.bm_supported = m.get('bmSupported')
        return self


class VMPQueryNodePaths(TeaModel):
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


class VMPQueryNodeParameters(TeaModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_dir: str = None,
        limit: int = None,
        marker: str = None,
        region_name: str = None,
        province: str = None,
        carrier: str = None,
        line_type: str = None,
        ipv_6supported: str = None,
        bm_supported: str = None,
    ):
        # {"en":"The sorted field name can have multiple values: name, regionname, province", "zh_CN":"排序的字段名称，可以有多个，取值：name、regionName、province"}
        self.sort_key = sort_key
        # {"en":"Sorting direction must follow sortkey, value: desc: descending, default value: ASC: ascending", "zh_CN":"排序方向，必须跟在sortKey后面出现，取值：desc：降序，默认值 asc：升序"}
        self.sort_dir = sort_dir
        # {"en":"The number of items displayed on each page is 20 by default", "zh_CN":"每个页面显示条数，默认是20"}
        self.limit = limit
        # {"en":"Query from the name specified by marker", "zh_CN":"从marker指定的名称开始查询"}
        self.marker = marker
        # {"en":"Node area (see Appendix for details)", "zh_CN":"节点所属区域（区域列表详见附录1：https://www.wangsu.com/document/18204/areas-list?rsr=ws）"}
        self.region_name = region_name
        # {"en":"Node province (see Appendix for details)", "zh_CN":"节点所属省份（详见附录2：https://www.wangsu.com/document/18204/isp-list?rsr=ws）"}
        self.province = province
        # {"en":"Node carrier (see Appendix for details)", "zh_CN":"节点所属运营商：dx-电信；wt-网通；yd-移动"}
        self.carrier = carrier
        # {"en":"Line type: single -- single line node; double -- double line node; triple -- three line node; BGP -- BGP node", "zh_CN":"线路类型：single -- 单线节点；double -- 双线节点；triple -- 三线节点；bgp -- BGP节点"}
        self.line_type = line_type
        # {"en":"IPv6 supported: true: IPv6 supported false: IPv6 not supported", "zh_CN":"是否支持ipv6：True：支持ipv6 False：不支持ipv6"}
        self.ipv_6supported = ipv_6supported
        # {"en":"Whether the node has bare metal resources
        # True: There are bare metal resources
        # False: No bare metal resources, only virtual machine resources", "zh_CN":"该节点是否有裸机资源
        # True：有裸机资源
        # False：没有裸机资源，只有虚拟机资源"}
        self.bm_supported = bm_supported

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_dir is not None:
            result['sortDir'] = self.sort_dir
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.line_type is not None:
            result['lineType'] = self.line_type
        if self.ipv_6supported is not None:
            result['ipv6Supported'] = self.ipv_6supported
        if self.bm_supported is not None:
            result['bmSupported'] = self.bm_supported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortDir') is not None:
            self.sort_dir = m.get('sortDir')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('lineType') is not None:
            self.line_type = m.get('lineType')
        if m.get('ipv6Supported') is not None:
            self.ipv_6supported = m.get('ipv6Supported')
        if m.get('bmSupported') is not None:
            self.bm_supported = m.get('bmSupported')
        return self


class VMPQueryNodeRequestHeader(TeaModel):
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


class VMPQueryNodeResponseHeader(TeaModel):
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






class VMPQueryBandwidthRequest(TeaModel):
    def __init__(
        self,
        node_names: List[str] = None,
    ):
        # {"en":"VMPQueryBandwidthNode array", "zh_CN":"节点数组"}
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_names is not None:
            result['nodeNames'] = self.node_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeNames') is not None:
            self.node_names = m.get('nodeNames')
        return self


class VMPQueryBandwidthNodeBw(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        result: str = None,
    ):
        # {"en":"Operator code", "zh_CN":"运营商代码"}
        self.carrier = carrier
        # {"en":"Whether the node has redundant bandwidth
        # True: redundant bandwidth
        # False: no redundant bandwidth
        # Undefined: node bandwidth statistics are not available. Whether there is redundant bandwidth is unknown. It is recommended to query again later.", "zh_CN":"节点是否有冗余带宽
        # True：有冗余带宽
        # False：无冗余带宽
        # Undefined：节点带宽统计数据不可用，是否有冗余带宽未知，建议稍后重新查询"}
        self.result = result

    def validate(self):
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class VMPQueryBandwidthNode(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        node_bw: List[VMPQueryBandwidthNodeBw] = None,
    ):
        # {"en":"VMPQueryBandwidthNode name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"VMPQueryBandwidthNode bandwidth", "zh_CN":"节点带宽"}
        self.node_bw = node_bw

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.node_bw, 'node_bw')
        if self.node_bw:
            for k in self.node_bw:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.node_bw is not None:
            result['nodeBw'] = []
            for k in self.node_bw:
                result['nodeBw'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('nodeBw') is not None:
            self.node_bw = []
            for k in m.get('nodeBw'):
                temp_model = VMPQueryBandwidthNodeBw()
                self.node_bw.append(temp_model.from_map(k))
        return self


class VMPQueryBandwidthResponse(TeaModel):
    def __init__(
        self,
        nodes: List[VMPQueryBandwidthNode] = None,
    ):
        # {"en":"node", "zh_CN":"节点"}
        self.nodes = nodes

    def validate(self):
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = []
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = []
            for k in m.get('nodes'):
                temp_model = VMPQueryBandwidthNode()
                self.nodes.append(temp_model.from_map(k))
        return self


class VMPQueryBandwidthPaths(TeaModel):
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


class VMPQueryBandwidthParameters(TeaModel):
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


class VMPQueryBandwidthRequestHeader(TeaModel):
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


class VMPQueryBandwidthResponseHeader(TeaModel):
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






class NodeRedundantBandwidth4PstatpRequest(TeaModel):
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


class NodeRedundantBandwidth4PstatpIspBandwidth(TeaModel):
    def __init__(
        self,
        isp: str = None,
        current_bandwidth: int = None,
        available_elastic_bandwidth: int = None,
    ):
        # {"en":"no", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"no", "zh_CN":"节点保障带宽"}
        self.current_bandwidth = current_bandwidth
        # {"en":"no", "zh_CN":"节点冗余带宽"}
        self.available_elastic_bandwidth = available_elastic_bandwidth

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.current_bandwidth, 'current_bandwidth')
        self.validate_required(self.available_elastic_bandwidth, 'available_elastic_bandwidth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.current_bandwidth is not None:
            result['CurrentBandwidth'] = self.current_bandwidth
        if self.available_elastic_bandwidth is not None:
            result['AvailableElasticBandwidth'] = self.available_elastic_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('CurrentBandwidth') is not None:
            self.current_bandwidth = m.get('CurrentBandwidth')
        if m.get('AvailableElasticBandwidth') is not None:
            self.available_elastic_bandwidth = m.get('AvailableElasticBandwidth')
        return self


class NodeRedundantBandwidth4PstatpNodeBandwidth(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        isp_bandwidth: List[NodeRedundantBandwidth4PstatpIspBandwidth] = None,
    ):
        # {"en":"no", "zh_CN":"节点ID"}
        self.room_id = room_id
        # {"en":"no", "zh_CN":"带宽列表"}
        self.isp_bandwidth = isp_bandwidth

    def validate(self):
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.isp_bandwidth, 'isp_bandwidth')
        if self.isp_bandwidth:
            for k in self.isp_bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.isp_bandwidth is not None:
            result['NodeRedundantBandwidth4PstatpIspBandwidth'] = []
            for k in self.isp_bandwidth:
                result['NodeRedundantBandwidth4PstatpIspBandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('NodeRedundantBandwidth4PstatpIspBandwidth') is not None:
            self.isp_bandwidth = []
            for k in m.get('NodeRedundantBandwidth4PstatpIspBandwidth'):
                temp_model = NodeRedundantBandwidth4PstatpIspBandwidth()
                self.isp_bandwidth.append(temp_model.from_map(k))
        return self


class NodeRedundantBandwidth4PstatpResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[NodeRedundantBandwidth4PstatpNodeBandwidth] = None,
    ):
        # {"en":"no", "zh_CN":"接口是否成功"}
        self.code = code
        # {"en":"no", "zh_CN":"带宽列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = []
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = []
            for k in m.get('Data'):
                temp_model = NodeRedundantBandwidth4PstatpNodeBandwidth()
                self.data.append(temp_model.from_map(k))
        return self


class NodeRedundantBandwidth4PstatpPaths(TeaModel):
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


class NodeRedundantBandwidth4PstatpParameters(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        room_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # {"en":"Query account", "zh_CN":"需要查询的账号"}
        self.account_id = account_id
        # {"en":"Node ID", "zh_CN":"厂商侧节点id，不填默认查询账号实际有在用的节点"}
        self.room_id = room_id
        # {"en":"Page Number", "zh_CN":"分页页数，不填默认返回全部数据"}
        self.page_num = page_num
        # {"en":"Page size", "zh_CN":"每页条数，不填时默认10条"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class NodeRedundantBandwidth4PstatpRequestHeader(TeaModel):
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


class NodeRedundantBandwidth4PstatpResponseHeader(TeaModel):
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




