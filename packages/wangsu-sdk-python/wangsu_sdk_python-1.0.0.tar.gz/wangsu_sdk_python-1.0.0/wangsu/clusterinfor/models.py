# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ListClusterRequest(TeaModel):
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


class ListClusterCluster(TeaModel):
    def __init__(
        self,
        cluster_cn_name: str = None,
        cluster_name: str = None,
        cluster_alias: str = None,
        country: str = None,
        area: str = None,
        province: str = None,
        city: str = None,
        isp: str = None,
        country_en: str = None,
        area_en: str = None,
        province_en: str = None,
        city_en: str = None,
        pool_type: int = None,
    ):
        # {"en":"chinese name of the clustere", "zh_CN":"集群中文名"}
        self.cluster_cn_name = cluster_cn_name
        # {"en":"cluster name", "zh_CN":"集群名"}
        self.cluster_name = cluster_name
        # {"en":"cluster alias", "zh_CN":"集群别名"}
        self.cluster_alias = cluster_alias
        # {"en":"country name", "zh_CN":"集群所在国家名称"}
        self.country = country
        # {"en":"area", "zh_CN":"集群所在区域"}
        self.area = area
        # {"en":"province name", "zh_CN":"集群所在省份名称"}
        self.province = province
        # {"en":"city name", "zh_CN":"集群所在城市名称"}
        self.city = city
        # {"en":"isp", "zh_CN":"集群支持的运营商"}
        self.isp = isp
        # {"en":"country name", "zh_CN":"集群所在国家英文名"}
        self.country_en = country_en
        # {"en":"the English name of area", "zh_CN":"集群所在区域英文名"}
        self.area_en = area_en
        # {"en":"the English name of province", "zh_CN":"集群所在省份英文名"}
        self.province_en = province_en
        # {"en":"the English name of city", "zh_CN":"集群所在城市英文名"}
        self.city_en = city_en
        # {"en":"cluster pool type(0,1:Universal,2: GPU,3: Storage)", "zh_CN":"集群业务类型(0,1:通用型,2: gpu型,3: 存储型)"}
        self.pool_type = pool_type

    def validate(self):
        self.validate_required(self.cluster_cn_name, 'cluster_cn_name')
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.cluster_alias, 'cluster_alias')
        self.validate_required(self.country, 'country')
        self.validate_required(self.area, 'area')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.country_en, 'country_en')
        self.validate_required(self.area_en, 'area_en')
        self.validate_required(self.province_en, 'province_en')
        self.validate_required(self.city_en, 'city_en')
        self.validate_required(self.pool_type, 'pool_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_cn_name is not None:
            result['clusterCnName'] = self.cluster_cn_name
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cluster_alias is not None:
            result['clusterAlias'] = self.cluster_alias
        if self.country is not None:
            result['country'] = self.country
        if self.area is not None:
            result['area'] = self.area
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.isp is not None:
            result['isp'] = self.isp
        if self.country_en is not None:
            result['countryEn'] = self.country_en
        if self.area_en is not None:
            result['areaEn'] = self.area_en
        if self.province_en is not None:
            result['provinceEn'] = self.province_en
        if self.city_en is not None:
            result['cityEn'] = self.city_en
        if self.pool_type is not None:
            result['poolType'] = self.pool_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterCnName') is not None:
            self.cluster_cn_name = m.get('clusterCnName')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('clusterAlias') is not None:
            self.cluster_alias = m.get('clusterAlias')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('countryEn') is not None:
            self.country_en = m.get('countryEn')
        if m.get('areaEn') is not None:
            self.area_en = m.get('areaEn')
        if m.get('provinceEn') is not None:
            self.province_en = m.get('provinceEn')
        if m.get('cityEn') is not None:
            self.city_en = m.get('cityEn')
        if m.get('poolType') is not None:
            self.pool_type = m.get('poolType')
        return self


class ListClusterResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: List[ListClusterCluster] = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"cluster", "zh_CN":"集群列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = ListClusterCluster()
                self.data.append(temp_model.from_map(k))
        return self


class ListClusterPaths(TeaModel):
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


class ListClusterParameters(TeaModel):
    def __init__(
        self,
        label_selector: str = None,
    ):
        # {"en":"labelSelector", "zh_CN":"labelSelector"}
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListClusterRequestHeader(TeaModel):
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


class ListClusterResponseHeader(TeaModel):
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






class ListPoolsPoolResource(TeaModel):
    def __init__(
        self,
        group: str = None,
        type: str = None,
    ):
        # {"en":"resource group", "zh_CN":"资源分组"}
        self.group = group
        # {"en":"resource type", "zh_CN":"资源类型"}
        self.type = type

    def validate(self):
        self.validate_required(self.group, 'group')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListPoolsRequest(TeaModel):
    def __init__(
        self,
        resources: List[ListPoolsPoolResource] = None,
    ):
        # {"en":"resource request", "zh_CN":"集群拥有的资源"}
        self.resources = resources

    def validate(self):
        self.validate_required(self.resources, 'resources')
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resources is not None:
            result['resources'] = []
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resources') is not None:
            self.resources = []
            for k in m.get('resources'):
                temp_model = ListPoolsPoolResource()
                self.resources.append(temp_model.from_map(k))
        return self


class ListPoolsPoolClusterInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
        alias: str = None,
        type: int = None,
        id: int = None,
        country: str = None,
        area: str = None,
        province: str = None,
        city: str = None,
        isp: str = None,
    ):
        # {"en":"poolCluster name", "zh_CN":"调度池名称"}
        self.name = name
        # {"en":"poolCluster cn name", "zh_CN":"调度池中文名"}
        self.name_cn = name_cn
        # {"en":"poolCluster alias", "zh_CN":"调度池别名"}
        self.alias = alias
        # {"en":"poolCluster type", "zh_CN":"调度池类别"}
        self.type = type
        # {"en":"poolCluster id", "zh_CN":"调度池ID"}
        self.id = id
        # {"en":"country", "zh_CN":"国家"}
        self.country = country
        # {"en":"area", "zh_CN":"地区"}
        self.area = area
        # {"en":"province", "zh_CN":"省份"}
        self.province = province
        # {"en":"city", "zh_CN":"城市"}
        self.city = city
        # {"en":"isp", "zh_CN":"运营商"}
        self.isp = isp

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.alias, 'alias')
        self.validate_required(self.type, 'type')
        self.validate_required(self.id, 'id')
        self.validate_required(self.country, 'country')
        self.validate_required(self.area, 'area')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.isp, 'isp')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        if self.alias is not None:
            result['alias'] = self.alias
        if self.type is not None:
            result['type'] = self.type
        if self.id is not None:
            result['id'] = self.id
        if self.country is not None:
            result['country'] = self.country
        if self.area is not None:
            result['area'] = self.area
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class ListPoolsPoolClusterListResp(TeaModel):
    def __init__(
        self,
        total: int = None,
        infos: List[ListPoolsPoolClusterInfo] = None,
    ):
        # {"en":"poolCluster total", "zh_CN":"调度池总数"}
        self.total = total
        # {"en":"poolCluster list", "zh_CN":"调度池列表"}
        self.infos = infos

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.infos, 'infos')
        if self.infos:
            for k in self.infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.infos is not None:
            result['infos'] = []
            for k in self.infos:
                result['infos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('infos') is not None:
            self.infos = []
            for k in m.get('infos'):
                temp_model = ListPoolsPoolClusterInfo()
                self.infos.append(temp_model.from_map(k))
        return self


class ListPoolsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListPoolsPoolClusterListResp = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ListPoolsPoolClusterListResp", "zh_CN":"ListPoolsPoolClusterListResp"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListPoolsPoolClusterListResp()
            self.data = temp_model.from_map(m['data'])
        return self


class ListPoolsPaths(TeaModel):
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


class ListPoolsParameters(TeaModel):
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


class ListPoolsRequestHeader(TeaModel):
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


class ListPoolsResponseHeader(TeaModel):
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






class QueryEdgeContainerBandwidthServiceRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        cluster: str = None,
    ):
        # {"en": "start_time", "zh_CN": "开始时间戳(毫秒)"}
        self.start_time = start_time
        # {"en": "end_time", "zh_CN": "结束时间戳(毫秒)"}
        self.end_time = end_time
        # {"en": "cluster", "zh_CN": "集群"}
        self.cluster = cluster

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.cluster is not None:
            result['cluster'] = self.cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        return self


class QueryEdgeContainerBandwidthServiceResponse(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        data_points: List[str] = None,
        bw_direction: str = None,
        data_point: List[str] = None,
        max: float = None,
        timestamp: int = None,
        cpu: int = None,
        memory: int = None,
        pvc: int = None,
    ):
        # {"en": "cluster", "zh_CN": "集群名称"}
        self.cluster = cluster
        self.data_points = data_points
        # {"en": "upstream or downstream", "zh_CN": "请求方向,流入/流出"}
        self.bw_direction = bw_direction
        self.data_point = data_point
        # {"en": "bandwidth", "zh_CN": "每5分钟的带宽平均值"}
        self.max = max
        # {"en": "timestamp", "zh_CN": "毫秒级别时间戳"}
        self.timestamp = timestamp
        # {"en": "cpu_size", "zh_CN": "时间范围内CPU使⽤最⼤值"}
        self.cpu = cpu
        # {"en": "memory_size", "zh_CN": "时间范围内内存使⽤最⼤值"}
        self.memory = memory
        # {"en": "pvc", "zh_CN": "时间范围内使⽤最⼤值"}
        self.pvc = pvc

    def validate(self):
        self.validate_required(self.cluster, 'cluster')
        self.validate_required(self.data_points, 'data_points')
        self.validate_required(self.bw_direction, 'bw_direction')
        self.validate_required(self.data_point, 'data_point')
        self.validate_required(self.max, 'max')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.pvc, 'pvc')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.data_points is not None:
            result['data_points'] = self.data_points
        if self.bw_direction is not None:
            result['bw_direction'] = self.bw_direction
        if self.data_point is not None:
            result['data_point'] = self.data_point
        if self.max is not None:
            result['max'] = self.max
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        if self.pvc is not None:
            result['pvc'] = self.pvc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('data_points') is not None:
            self.data_points = m.get('data_points')
        if m.get('bw_direction') is not None:
            self.bw_direction = m.get('bw_direction')
        if m.get('data_point') is not None:
            self.data_point = m.get('data_point')
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('pvc') is not None:
            self.pvc = m.get('pvc')
        return self


class QueryEdgeContainerBandwidthServicePaths(TeaModel):
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


class QueryEdgeContainerBandwidthServiceParameters(TeaModel):
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


class QueryEdgeContainerBandwidthServiceRequestHeader(TeaModel):
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


class QueryEdgeContainerBandwidthServiceResponseHeader(TeaModel):
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




