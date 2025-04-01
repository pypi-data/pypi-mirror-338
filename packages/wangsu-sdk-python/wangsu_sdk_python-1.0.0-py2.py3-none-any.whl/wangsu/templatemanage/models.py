# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VMPQueryNodeServersRequest(TeaModel):
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


class VMPQueryNodeServersServer(TeaModel):
    def __init__(
        self,
        province: str = None,
        carrier: str = None,
        node_name: str = None,
        count: str = None,
    ):
        # {"en":"Province", "zh_CN":"节点所属省份（详见附录2：https://www.wangsu.com/document/18204/isp-list?rsr=ws）"}
        self.province = province
        # {"en":"Carrier", "zh_CN":"节点所属运营商：dx-电信；wt-网通；yd-移动"}
        self.carrier = carrier
        # {"en":"Node Name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"Number of instances that can be created", "zh_CN":"可创建的实例的数量"}
        self.count = count

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class VMPQueryNodeServersResponse(TeaModel):
    def __init__(
        self,
        servers: List[VMPQueryNodeServersServer] = None,
    ):
        # {"en":"Instance quantity information", "zh_CN":"实例数量信息列表"}
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
                temp_model = VMPQueryNodeServersServer()
                self.servers.append(temp_model.from_map(k))
        return self


class VMPQueryNodeServersPaths(TeaModel):
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


class VMPQueryNodeServersParameters(TeaModel):
    def __init__(
        self,
        province: str = None,
        carrier: str = None,
        node_name: str = None,
        flavor_id: str = None,
        protocols: int = None,
        network_type: str = None,
        use_unique_ip_segment: int = None,
    ):
        # {"en":"Province", "zh_CN":"节点所属省份（详见附录2：https://www.wangsu.com/document/18204/isp-list?rsr=ws）"}
        self.province = province
        # {"en":"Carrier", "zh_CN":"节点所属运营商：dx-电信；wt-网通；yd-移动"}
        self.carrier = carrier
        # {"en":"Node Name", "zh_CN":"节点名称，表示指定节点创建实例"}
        self.node_name = node_name
        # {"en":"FlavorId", "zh_CN":"实例规格标识（可通过实例规格查询接口进行查询：https://www.wangsu.com/document/api-doc/22811?rsr=ws）"}
        self.flavor_id = flavor_id
        # {"en":"Protocols:
        # 4:only ipv4
        # 6:only ipv6
        # 0:both ipv4 & ipv6", "zh_CN":"是否需要多ip协议地址
        # 4：只需要ipv4地址，默认值
        # 6：只需要ipv6地址
        # 0：ipv4、ipv6都需要"}
        self.protocols = protocols
        # {"en":"Virtual machine network type:
        # ANY - the default;
        # DPDK - DPDK network.", "zh_CN":"虚拟机网络类型：
        # ANY-默认；
        # DPDK-DPDK网络。"}
        self.network_type = network_type
        # {"en":"Use unique IP segment", "zh_CN":"是否使用唯一网段 
        # 1：是 
        # -1：否"}
        self.use_unique_ip_segment = use_unique_ip_segment

    def validate(self):
        self.validate_required(self.flavor_id, 'flavor_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.flavor_id is not None:
            result['flavorId'] = self.flavor_id
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.use_unique_ip_segment is not None:
            result['useUniqueIpSegment'] = self.use_unique_ip_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('flavorId') is not None:
            self.flavor_id = m.get('flavorId')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('useUniqueIpSegment') is not None:
            self.use_unique_ip_segment = m.get('useUniqueIpSegment')
        return self


class VMPQueryNodeServersRequestHeader(TeaModel):
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


class VMPQueryNodeServersResponseHeader(TeaModel):
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




