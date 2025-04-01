# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VmpInstanceReplaceIpRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ips: List[str] = None,
    ):
        # {"en":"vm id", "zh_CN":"云主机ID"}
        self.instance_id = instance_id
        # {"en":"server old replace ips", "zh_CN":"虚拟机待更换ip列表"}
        self.instance_ips = instance_ips

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_ips, 'instance_ips')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_ips is not None:
            result['instanceIps'] = self.instance_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceIps') is not None:
            self.instance_ips = m.get('instanceIps')
        return self


class VmpInstanceReplaceIpResponse(TeaModel):
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


class VmpInstanceReplaceIpPaths(TeaModel):
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


class VmpInstanceReplaceIpParameters(TeaModel):
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


class VmpInstanceReplaceIpRequestHeader(TeaModel):
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


class VmpInstanceReplaceIpResponseHeader(TeaModel):
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






class ConvertFreeTypeInstanceToChargeTypeRequest(TeaModel):
    def __init__(
        self,
        servers: str = None,
    ):
        # {"en":"Unique cloud host identity.Up to 100 IDs can be sent at a time, separated by the half comma character ', '.", "zh_CN":"云主机唯一标识。单次最多可发送100 条ID，ID 之间用半角逗号字符','隔开。"}
        self.servers = servers

    def validate(self):
        self.validate_required(self.servers, 'servers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servers is not None:
            result['servers'] = self.servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        return self


class ConvertFreeTypeInstanceToChargeTypeErrorMsg(TeaModel):
    def __init__(
        self,
        code: str = None,
        key: str = None,
        msg: str = None,
    ):
        # {"en":"error code", "zh_CN":"错误编码"}
        self.code = code
        # {"en":"instance id", "zh_CN":"实例id"}
        self.key = key
        # {"en":"error msg", "zh_CN":"错误信息"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.key, 'key')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.key is not None:
            result['key'] = self.key
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ConvertFreeTypeInstanceToChargeTypeResponse(TeaModel):
    def __init__(
        self,
        batch_error_msg: List[ConvertFreeTypeInstanceToChargeTypeErrorMsg] = None,
    ):
        self.batch_error_msg = batch_error_msg

    def validate(self):
        self.validate_required(self.batch_error_msg, 'batch_error_msg')
        if self.batch_error_msg:
            for k in self.batch_error_msg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_error_msg is not None:
            result['batchErrorMsg'] = []
            for k in self.batch_error_msg:
                result['batchErrorMsg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchErrorMsg') is not None:
            self.batch_error_msg = []
            for k in m.get('batchErrorMsg'):
                temp_model = ConvertFreeTypeInstanceToChargeTypeErrorMsg()
                self.batch_error_msg.append(temp_model.from_map(k))
        return self


class ConvertFreeTypeInstanceToChargeTypePaths(TeaModel):
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


class ConvertFreeTypeInstanceToChargeTypeParameters(TeaModel):
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


class ConvertFreeTypeInstanceToChargeTypeRequestHeader(TeaModel):
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


class ConvertFreeTypeInstanceToChargeTypeResponseHeader(TeaModel):
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






class ManageInstanceTagsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        tag: str = None,
    ):
        # {"en":"The cloud host ID, with multiple IDs separated by the half corner comma character ', '.", "zh_CN":"云主机id，多个ID 之间用半角逗号字符','隔开。"}
        self.id = id
        # {"en":"New instance label value;If the value is null, the instance label of the specified cloud host is deleted.", "zh_CN":"新的实例标签值；如果值为空，则表示删除指定云主机的实例标签。"}
        self.tag = tag

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.tag, 'tag')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class ManageInstanceTagsResponse(TeaModel):
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


class ManageInstanceTagsPaths(TeaModel):
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


class ManageInstanceTagsParameters(TeaModel):
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


class ManageInstanceTagsRequestHeader(TeaModel):
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


class ManageInstanceTagsResponseHeader(TeaModel):
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






class VmpInstanceBandwidth5MinQueryRequest(TeaModel):
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


class VmpInstanceBandwidth5MinQueryBandwidth(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        ip: str = None,
        stat_time: str = None,
        out: str = None,
        in_: str = None,
        ext_in: str = None,
        ext_out: str = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商：dx-电信；wt-网通；yd-移动"}
        self.carrier = carrier
        # {"en":"instance ip", "zh_CN":"实例IP"}
        self.ip = ip
        # {"en":"The bandwidth collection time, formatted as YYYYMMDDHHMM, is 5 minutes granularity", "zh_CN":"带宽采集时间，格式yyyyMMddHHmm，为5分钟粒度"}
        self.stat_time = stat_time
        # {"en":"Total outflow bandwidth (including intra-node flow) in Mbps", "zh_CN":"总流出带宽（含节点内流量），单位Mbps"}
        self.out = out
        # {"en":"Total inflow bandwidth (including intra-node traffic) in Mbps", "zh_CN":"总流入带宽（含节点内流量），单位Mbps"}
        self.in_ = in_
        # {"en":"Inflow bandwidth of external network (not including intra-node traffic), unit of Mbps", "zh_CN":"外网流入带宽（不含节点内流量），单位Mbps"}
        self.ext_in = ext_in
        # {"en":"Outflow bandwidth of the external network (excluding intra-node traffic), unit of Mbps", "zh_CN":"外网流出带宽（不含节点内流量），单位Mbps"}
        self.ext_out = ext_out

    def validate(self):
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.stat_time, 'stat_time')
        self.validate_required(self.out, 'out')
        self.validate_required(self.in_, 'in_')
        self.validate_required(self.ext_in, 'ext_in')
        self.validate_required(self.ext_out, 'ext_out')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.ip is not None:
            result['ip'] = self.ip
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.out is not None:
            result['out'] = self.out
        if self.in_ is not None:
            result['in'] = self.in_
        if self.ext_in is not None:
            result['extIn'] = self.ext_in
        if self.ext_out is not None:
            result['extOut'] = self.ext_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('out') is not None:
            self.out = m.get('out')
        if m.get('in') is not None:
            self.in_ = m.get('in')
        if m.get('extIn') is not None:
            self.ext_in = m.get('extIn')
        if m.get('extOut') is not None:
            self.ext_out = m.get('extOut')
        return self


class VmpInstanceBandwidth5MinQueryServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        bandwidths: List[VmpInstanceBandwidth5MinQueryBandwidth] = None,
    ):
        # {"en":"instance id", "zh_CN":"实例唯一标识"}
        self.id = id
        # {"en":"VmpInstanceBandwidth5MinQueryBandwidth information", "zh_CN":"带宽信息"}
        self.bandwidths = bandwidths

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.bandwidths, 'bandwidths')
        if self.bandwidths:
            for k in self.bandwidths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.bandwidths is not None:
            result['bandwidths'] = []
            for k in self.bandwidths:
                result['bandwidths'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('bandwidths') is not None:
            self.bandwidths = []
            for k in m.get('bandwidths'):
                temp_model = VmpInstanceBandwidth5MinQueryBandwidth()
                self.bandwidths.append(temp_model.from_map(k))
        return self


class VmpInstanceBandwidth5MinQueryResponse(TeaModel):
    def __init__(
        self,
        servers: List[VmpInstanceBandwidth5MinQueryServer] = None,
    ):
        # {"en":"Instance information array", "zh_CN":"实例信息数组"}
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
                temp_model = VmpInstanceBandwidth5MinQueryServer()
                self.servers.append(temp_model.from_map(k))
        return self


class VmpInstanceBandwidth5MinQueryPaths(TeaModel):
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


class VmpInstanceBandwidth5MinQueryParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        stat_time: str = None,
        carrier: str = None,
    ):
        # {"en":"The ID of the virtual machine to query. At most 30 queries can be made at a time, ids 
        #  are separated by character  ','", "zh_CN":"云主机ID。单次最多查询 20 条 ID，ID 之间用半角逗号字符','隔开。"}
        self.ids = ids
        # {"en":"Query time range in format: yyyymmddhhmm-yyyymmddhhmm
        # Query data for nearly 90 days, a single query no more than 3 days.
        # For example: 202001201730-202001201930 means to query 2020-01-20 17:30 to 19:30 monitoring data.", "zh_CN":"查询时间范围，格式：yyyyMMddHHmm- yyyyMMddHHmm
        # 查询近90天的数据，单次查询不超过10天。
        # 例如：202001201730-202001201930表示查询2020-01-20 17:30到19:30的带宽数据。"}
        self.stat_time = stat_time
        # {"en":"The ISP code  ", "zh_CN":"主要用于多线实例流量拆分时过滤所属运营商：dx-电信；wt-网通；yd-移动。一次仅允许传入一个运营商参数"}
        self.carrier = carrier

    def validate(self):
        self.validate_required(self.ids, 'ids')
        self.validate_required(self.stat_time, 'stat_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.stat_time is not None:
            result['statTime'] = self.stat_time
        if self.carrier is not None:
            result['carrier'] = self.carrier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('statTime') is not None:
            self.stat_time = m.get('statTime')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        return self


class VmpInstanceBandwidth5MinQueryRequestHeader(TeaModel):
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


class VmpInstanceBandwidth5MinQueryResponseHeader(TeaModel):
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






class UpdateEcciInstanceAssignIp(TeaModel):
    def __init__(
        self,
        isp_id: int = None,
        ipv_4: bool = None,
        ipv_6: bool = None,
    ):
        # {"en":"ip operator id", "zh_CN":"ip所属运营商id"}
        self.isp_id = isp_id
        # {"en":"Whether to assign ipv4 ip, ipv4 is assigned by default", "zh_CN":"是否分配ipv4的ip，默认分配ipv4"}
        self.ipv_4 = ipv_4
        # {"en":"Whether to assign ipv6 ip", "zh_CN":"是否分配ipv6的ip"}
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp_id is not None:
            result['ispId'] = self.isp_id
        if self.ipv_4 is not None:
            result['ipv4'] = self.ipv_4
        if self.ipv_6 is not None:
            result['ipv6'] = self.ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ispId') is not None:
            self.isp_id = m.get('ispId')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        return self


class UpdateEcciInstanceInstanceDistribution(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        replicas: int = None,
        assign_ips: List[UpdateEcciInstanceAssignIp] = None,
    ):
        # {"en":"distribution cluster name", "zh_CN":"部署集群名称"}
        self.cluster = cluster
        # {"en":"Number of desired pods", "zh_CN":"预期 Pod 的数量"}
        self.replicas = replicas
        # {"en":"assigned ip attributes", "zh_CN":"分配ip属性"}
        self.assign_ips = assign_ips

    def validate(self):
        self.validate_required(self.cluster, 'cluster')
        self.validate_required(self.replicas, 'replicas')
        self.validate_required(self.assign_ips, 'assign_ips')
        if self.assign_ips:
            for k in self.assign_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.assign_ips is not None:
            result['assignIps'] = []
            for k in self.assign_ips:
                result['assignIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('assignIps') is not None:
            self.assign_ips = []
            for k in m.get('assignIps'):
                temp_model = UpdateEcciInstanceAssignIp()
                self.assign_ips.append(temp_model.from_map(k))
        return self


class UpdateEcciInstanceContainerEnvRef(TeaModel):
    def __init__(
        self,
        name: str = None,
        field_path: str = None,
    ):
        # {"en":"Environment variable name", "zh_CN":"环境变量名称"}
        self.name = name
        # {"en":"Path to the field to be selected by downwardapi", "zh_CN":"downwardapi要选择的字段的路径"}
        self.field_path = field_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.field_path, 'field_path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.field_path is not None:
            result['fieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')
        return self


class UpdateEcciInstanceVolumeMount(TeaModel):
    def __init__(
        self,
        name: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # {"en":"This must match the Name of a Volume", "zh_CN":"此字段必须与卷的名称匹配"}
        self.name = name
        # {"en":"Path within the container at which the volume should be mounted. Must not contain ':'", "zh_CN":"容器内卷的挂载路径。不得包含 ':'"}
        self.mount_path = mount_path
        # {"en":"Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false", "zh_CN":"如果为 true，则以只读方式挂载，否则（false 或未设置）以读写方式挂载。默认为 false"}
        self.read_only = read_only

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.mount_path, 'mount_path')
        self.validate_required(self.read_only, 'read_only')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class UpdateEcciInstanceContainer(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        memory_limit: str = None,
        name: str = None,
        image: str = None,
        command: List[str] = None,
        args: List[str] = None,
        working_dir: str = None,
        env: Dict[str, str] = None,
        env_ref: List[UpdateEcciInstanceContainerEnvRef] = None,
        volume_mounts: List[UpdateEcciInstanceVolumeMount] = None,
    ):
        # {"en":"UpdateEcciInstanceContainer cpu limit, the sum of all container cpu limits cannot exceed the instance cpu limit", "zh_CN":"容器cpu限制,所有容器cpu限制总和不能超过实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"UpdateEcciInstanceContainer memory limit, the sum of all container memory limits cannot exceed the instance memory limit", "zh_CN":"容器内存限制,所有容器内存限制总和不能超过实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"UpdateEcciInstanceContainer name", "zh_CN":"容器名称"}
        self.name = name
        # {"en":"UpdateEcciInstanceContainer image", "zh_CN":"容器镜像"}
        self.image = image
        # {"en":"Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided.", "zh_CN":"入口点数组。不在 Shell 中执行。如果未提供，则使用容器镜像的 ENTRYPOINT"}
        self.command = command
        # {"en":"Arguments to the entrypoint. The container image's CMD is used if this is not provided", "zh_CN":"entrypoint 的参数。如果未提供，则使用容器镜像的 CMD 设置"}
        self.args = args
        # {"en":"UpdateEcciInstanceContainer's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image", "zh_CN":"容器的工作目录。如果未指定，将使用容器运行时的默认值，默认值可能在容器镜像中配置"}
        self.working_dir = working_dir
        # {"en":"ist of environment variables to set in the container", "zh_CN":"要在容器中设置的环境变量列表"}
        self.env = env
        # {"en":"downwardapi type sensitive environment variables, authorization required", "zh_CN":"downwardapi 类型敏感环境变量,需授权"}
        self.env_ref = env_ref
        # {"en":"Pod volumes to mount into the container's filesystem. Cannot be updated", "zh_CN":"要挂载到容器文件系统中的 Pod 卷。无法更新"}
        self.volume_mounts = volume_mounts

    def validate(self):
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.name, 'name')
        self.validate_required(self.image, 'image')
        if self.env_ref:
            for k in self.env_ref:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.image is not None:
            result['image'] = self.image
        if self.command is not None:
            result['command'] = self.command
        if self.args is not None:
            result['args'] = self.args
        if self.working_dir is not None:
            result['workingDir'] = self.working_dir
        if self.env is not None:
            result['env'] = self.env
        if self.env_ref is not None:
            result['envRef'] = []
            for k in self.env_ref:
                result['envRef'].append(k.to_map() if k else None)
        if self.volume_mounts is not None:
            result['volumeMounts'] = []
            for k in self.volume_mounts:
                result['volumeMounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('envRef') is not None:
            self.env_ref = []
            for k in m.get('envRef'):
                temp_model = UpdateEcciInstanceContainerEnvRef()
                self.env_ref.append(temp_model.from_map(k))
        if m.get('volumeMounts') is not None:
            self.volume_mounts = []
            for k in m.get('volumeMounts'):
                temp_model = UpdateEcciInstanceVolumeMount()
                self.volume_mounts.append(temp_model.from_map(k))
        return self


class UpdateEcciInstancePodVolumeClaim(TeaModel):
    def __init__(
        self,
        claim_name: str = None,
    ):
        # {"en":"the name of a PersistentVolumeClaim in the same namespace as the pod using this volume", "zh_CN":"与使用此卷的 Pod 位于同一名字空间中的 PersistentVolumeClaim 的名称"}
        self.claim_name = claim_name

    def validate(self):
        self.validate_required(self.claim_name, 'claim_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_name is not None:
            result['claimName'] = self.claim_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('claimName') is not None:
            self.claim_name = m.get('claimName')
        return self


class UpdateEcciInstanceHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # {"en":"path of the directory on the host. If the path is a symlink, it will follow the link to the real path", "zh_CN":"目录在主机上的路径。如果该路径是一个符号链接，则它将沿着链接指向真实路径"}
        self.path = path
        # {"en":"type for HostPath Volume Defaults to ''", "zh_CN":"卷的类型。默认为 ''"}
        self.type = type

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateEcciInstancePodVolume(TeaModel):
    def __init__(
        self,
        name: str = None,
        persistent_volume_claim: UpdateEcciInstancePodVolumeClaim = None,
        host_path: UpdateEcciInstanceHostPathVolume = None,
    ):
        # {"en":"name of the volume. Must be a DNS_LABEL and unique within the pod.", "zh_CN":"卷的名称。必须是 DNS_LABEL 且在 Pod 内是唯一的。"}
        self.name = name
        # {"en":"represents a reference to a PersistentVolumeClaim in the same namespace", "zh_CN":"表示对同一名字空间中 PersistentVolumeClaim 的引用"}
        self.persistent_volume_claim = persistent_volume_claim
        # {"en":"Represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this.", "zh_CN":"表示主机上预先存在的文件或目录，它们将被直接暴露给容器。 这种卷通常用于系统代理或允许查看主机的其他特权操作。大多数容器不需要这种卷。"}
        self.host_path = host_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.persistent_volume_claim, 'persistent_volume_claim')
        if self.persistent_volume_claim:
            self.persistent_volume_claim.validate()
        self.validate_required(self.host_path, 'host_path')
        if self.host_path:
            self.host_path.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.persistent_volume_claim is not None:
            result['persistentVolumeClaim'] = self.persistent_volume_claim.to_map()
        if self.host_path is not None:
            result['hostPath'] = self.host_path.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('persistentVolumeClaim') is not None:
            temp_model = UpdateEcciInstancePodVolumeClaim()
            self.persistent_volume_claim = temp_model.from_map(m['persistentVolumeClaim'])
        if m.get('hostPath') is not None:
            temp_model = UpdateEcciInstanceHostPathVolume()
            self.host_path = temp_model.from_map(m['hostPath'])
        return self


class UpdateEcciInstanceLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
        operator: str = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.values, 'values')
        self.validate_required(self.operator, 'operator')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class UpdateEcciInstanceLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[UpdateEcciInstanceLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        self.validate_required(self.match_labels, 'match_labels')
        self.validate_required(self.match_expressions, 'match_expressions')
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = UpdateEcciInstanceLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdateEcciInstancePodAffinityTerm(TeaModel):
    def __init__(
        self,
        label_selector: UpdateEcciInstanceLabelSelector = None,
        namespaces: List[str] = None,
        topology_key: str = None,
    ):
        # {"en":"A label query over a set of resources, in this case pods.", "zh_CN":"对一组资源的标签查询，在这里资源为 Pod。"}
        self.label_selector = label_selector
        # {"en":"pod's namespace", "zh_CN":" Pod 的名字空间"}
        self.namespaces = namespaces
        # {"en":"This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.", "zh_CN":"此 Pod 应与指定名字空间中与标签选择算符匹配的 Pod 集合位于同一位置（亲和性） 或位于不同位置（反亲和性），这里的“在同一位置”意味着运行在一个节点上，其键名为 topologyKey 的标签值与运行所选 Pod 集合中的某 Pod 的任何节点上的标签值匹配。 不允许使用空的 topologyKey。"}
        self.topology_key = topology_key

    def validate(self):
        self.validate_required(self.label_selector, 'label_selector')
        if self.label_selector:
            self.label_selector.validate()
        self.validate_required(self.namespaces, 'namespaces')
        self.validate_required(self.topology_key, 'topology_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.namespaces is not None:
            result['namespaces'] = self.namespaces
        if self.topology_key is not None:
            result['topologyKey'] = self.topology_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = UpdateEcciInstanceLabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')
        if m.get('topologyKey') is not None:
            self.topology_key = m.get('topologyKey')
        return self


class UpdateEcciInstanceWeightedPodAffinityTerm(TeaModel):
    def __init__(
        self,
        weight: int = None,
        pod_affinity_term: UpdateEcciInstancePodAffinityTerm = None,
    ):
        # {"en":"associated with matching the corresponding podAffinityTerm, in the range 1-100.", "zh_CN":"匹配相应 podAffinityTerm 条件的权重，范围为 1-100。"}
        self.weight = weight
        # {"en":"Required. A pod affinity term, associated with the corresponding weight.", "zh_CN":"必需的字段。一个 Pod 亲和性条件，对应一个与相应的权重值。"}
        self.pod_affinity_term = pod_affinity_term

    def validate(self):
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.pod_affinity_term, 'pod_affinity_term')
        if self.pod_affinity_term:
            self.pod_affinity_term.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['weight'] = self.weight
        if self.pod_affinity_term is not None:
            result['podAffinityTerm'] = self.pod_affinity_term.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('podAffinityTerm') is not None:
            temp_model = UpdateEcciInstancePodAffinityTerm()
            self.pod_affinity_term = temp_model.from_map(m['podAffinityTerm'])
        return self


class UpdateEcciInstancePodAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[UpdateEcciInstancePodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[UpdateEcciInstanceWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的亲和性要求（例如：由于 Pod 标签更新）， 系统可能会也可能不会尝试最终将 Pod 从其节点中逐出。 当此列表中有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器会更倾向于将 Pod 调度到满足该字段指定的亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。最优选择是权重总和最大的节点， 即对于满足所有调度要求（资源请求、requiredDuringScheduling 亲和表达式等）的每个节点， 通过迭代该字段的元素来计算总和，如果节点具有与相应 podAffinityTerm 匹配的 Pod，则将“权重”添加到总和中； 具有最高总和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = UpdateEcciInstancePodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = UpdateEcciInstanceWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class UpdateEcciInstancePodAntiAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[UpdateEcciInstancePodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[UpdateEcciInstanceWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的反亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的反亲和性要求（例如：由于 Pod 标签更新）， 系统可能会或可能不会尝试最终将 Pod 从其节点中逐出。 当有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器更倾向于将 Pod 调度到满足该字段指定的反亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。 最优选的节点是权重总和最大的节点，即对于满足所有调度要求（资源请求、requiredDuringScheduling 反亲和性表达式等）的每个节点，通过遍历元素来计算总和如果节点具有与相应 podAffinityTerm 匹配的 Pod，则此字段并在总和中添加\"权重\"；具有最高加和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = UpdateEcciInstancePodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = UpdateEcciInstanceWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class UpdateEcciInstanceAffinity(TeaModel):
    def __init__(
        self,
        pod_affinity: UpdateEcciInstancePodAffinity = None,
        pod_anti_affinity: UpdateEcciInstancePodAntiAffinity = None,
    ):
        # {"en":"A group of inter pod affinity scheduling rules.", "zh_CN":"一组 Pod 间亲和性调度规则。"}
        self.pod_affinity = pod_affinity
        # {"en":"A group of node affinity scheduling rules.", "zh_CN":"一组节点亲和性调度规则。"}
        self.pod_anti_affinity = pod_anti_affinity

    def validate(self):
        self.validate_required(self.pod_affinity, 'pod_affinity')
        if self.pod_affinity:
            self.pod_affinity.validate()
        self.validate_required(self.pod_anti_affinity, 'pod_anti_affinity')
        if self.pod_anti_affinity:
            self.pod_anti_affinity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_affinity is not None:
            result['podAffinity'] = self.pod_affinity.to_map()
        if self.pod_anti_affinity is not None:
            result['podAntiAffinity'] = self.pod_anti_affinity.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('podAffinity') is not None:
            temp_model = UpdateEcciInstancePodAffinity()
            self.pod_affinity = temp_model.from_map(m['podAffinity'])
        if m.get('podAntiAffinity') is not None:
            temp_model = UpdateEcciInstancePodAntiAffinity()
            self.pod_anti_affinity = temp_model.from_map(m['podAntiAffinity'])
        return self


class UpdateEcciInstancePodSpec(TeaModel):
    def __init__(
        self,
        containers: List[UpdateEcciInstanceContainer] = None,
        restart_policy: str = None,
        termination_grace_period_seconds: int = None,
        volumes: List[UpdateEcciInstancePodVolume] = None,
        affinity: UpdateEcciInstanceAffinity = None,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
    ):
        # {"en":"List of containers belonging to the pod. There must be at least one container in a Pod. ", "zh_CN":"属于 Pod 的容器列表。Pod 中必须至少有一个容器。"}
        self.containers = containers
        # {"en":"Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always.", "zh_CN":"Pod 内所有容器的重启策略。Always、OnFailure、Never 之一。默认为 Always。"}
        self.restart_policy = restart_policy
        # {"en":"Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.", "zh_CN":"可选字段，表示 Pod 需要体面终止的所需的时长（以秒为单位）。字段值可以在删除请求中减少。 字段值必须是非负整数。零值表示收到 kill 信号则立即停止（没有机会关闭）。 如果此值为 nil，则将使用默认宽限期。 宽限期是从 Pod 中运行的进程收到终止信号后，到进程被 kill 信号强制停止之前，Pod 可以继续存在的时间（以秒为单位）。 应该将此值设置为比你的进程的预期清理时间更长。默认为 30 秒。"}
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # {"en":"List of volumes that can be mounted by containers belonging to the pod.", "zh_CN":"可以由属于 Pod 的容器挂载的卷列表。"}
        self.volumes = volumes
        # {"en":"If specified, the pod's scheduling constraints", "zh_CN":"如果指定了，则作为 Pod 的调度约束。"}
        self.affinity = affinity
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels

    def validate(self):
        self.validate_required(self.containers, 'containers')
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        self.validate_required(self.restart_policy, 'restart_policy')
        self.validate_required(self.termination_grace_period_seconds, 'termination_grace_period_seconds')
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()
        self.validate_required(self.affinity, 'affinity')
        if self.affinity:
            self.affinity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.containers is not None:
            result['containers'] = []
            for k in self.containers:
                result['containers'].append(k.to_map() if k else None)
        if self.restart_policy is not None:
            result['restartPolicy'] = self.restart_policy
        if self.termination_grace_period_seconds is not None:
            result['terminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.volumes is not None:
            result['volumes'] = []
            for k in self.volumes:
                result['volumes'].append(k.to_map() if k else None)
        if self.affinity is not None:
            result['affinity'] = self.affinity.to_map()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.labels is not None:
            result['labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containers') is not None:
            self.containers = []
            for k in m.get('containers'):
                temp_model = UpdateEcciInstanceContainer()
                self.containers.append(temp_model.from_map(k))
        if m.get('restartPolicy') is not None:
            self.restart_policy = m.get('restartPolicy')
        if m.get('terminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('terminationGracePeriodSeconds')
        if m.get('volumes') is not None:
            self.volumes = []
            for k in m.get('volumes'):
                temp_model = UpdateEcciInstancePodVolume()
                self.volumes.append(temp_model.from_map(k))
        if m.get('affinity') is not None:
            temp_model = UpdateEcciInstanceAffinity()
            self.affinity = temp_model.from_map(m['affinity'])
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        return self


class UpdateEcciInstanceRequest(TeaModel):
    def __init__(
        self,
        distributions: UpdateEcciInstanceInstanceDistribution = None,
        allocate_public_ip: bool = None,
        pod_spec: UpdateEcciInstancePodSpec = None,
        assign_ips: List[UpdateEcciInstanceAssignIp] = None,
    ):
        # {"en":"instance distribution", "zh_CN":"实例分发属性"}
        self.distributions = distributions
        # {"en":"Whether to assign public IP", "zh_CN":"是否分配公网ip"}
        self.allocate_public_ip = allocate_public_ip
        # {"en":"Specification of the desired behavior of the pod.", "zh_CN":"Pod 预期行为的规约。"}
        self.pod_spec = pod_spec
        # {"en":"assigned ip attributes", "zh_CN":"分配ip属性"}
        self.assign_ips = assign_ips

    def validate(self):
        self.validate_required(self.distributions, 'distributions')
        if self.distributions:
            self.distributions.validate()
        self.validate_required(self.allocate_public_ip, 'allocate_public_ip')
        self.validate_required(self.pod_spec, 'pod_spec')
        if self.pod_spec:
            self.pod_spec.validate()
        if self.assign_ips:
            for k in self.assign_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributions is not None:
            result['distributions'] = self.distributions.to_map()
        if self.allocate_public_ip is not None:
            result['allocatePublicIp'] = self.allocate_public_ip
        if self.pod_spec is not None:
            result['podSpec'] = self.pod_spec.to_map()
        if self.assign_ips is not None:
            result['assignIps'] = []
            for k in self.assign_ips:
                result['assignIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('distributions') is not None:
            temp_model = UpdateEcciInstanceInstanceDistribution()
            self.distributions = temp_model.from_map(m['distributions'])
        if m.get('allocatePublicIp') is not None:
            self.allocate_public_ip = m.get('allocatePublicIp')
        if m.get('podSpec') is not None:
            temp_model = UpdateEcciInstancePodSpec()
            self.pod_spec = temp_model.from_map(m['podSpec'])
        if m.get('assignIps') is not None:
            self.assign_ips = []
            for k in m.get('assignIps'):
                temp_model = UpdateEcciInstanceAssignIp()
                self.assign_ips.append(temp_model.from_map(k))
        return self


class UpdateEcciInstanceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateEcciInstancePaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"ecci instance name", "zh_CN":"ecci实例名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateEcciInstanceParameters(TeaModel):
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


class UpdateEcciInstanceRequestHeader(TeaModel):
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


class UpdateEcciInstanceResponseHeader(TeaModel):
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


class UpdateEcciInstanceContainerPort(TeaModel):
    def __init__(
        self,
        name: str = None,
        container_port: int = None,
        protocol: str = None,
    ):
        # {"en":"If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services", "zh_CN":"如果设置此字段，这必须是 IANA_SVC_NAME 并且在 Pod 中唯一。 Pod 中的每个命名端口都必须具有唯一的名称。服务可以引用的端口的名称"}
        self.name = name
        # {"en":"Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536", "zh_CN":"要在 Pod 的 IP 地址上公开的端口号。这必须是有效的端口号，0 < x < 65536"}
        self.container_port = container_port
        # {"en":"Protocol for port. Must be UDP, TCP, or SCTP. Defaults to \"TCP\"", "zh_CN":"端口协议。必须是 UDP、TCP 或 SCTP。默认为 TCP"}
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.container_port is not None:
            result['containerPort'] = self.container_port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('containerPort') is not None:
            self.container_port = m.get('containerPort')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self






class GetEcciInstanceRequest(TeaModel):
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


class GetEcciInstanceContainerEnvRef(TeaModel):
    def __init__(
        self,
        name: str = None,
        field_path: str = None,
    ):
        # {"en":"Environment variable name", "zh_CN":"环境变量名称"}
        self.name = name
        # {"en":"Path to the field to be selected by downwardapi", "zh_CN":"downwardapi要选择的字段的路径"}
        self.field_path = field_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.field_path, 'field_path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.field_path is not None:
            result['fieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')
        return self


class GetEcciInstanceVolumeMount(TeaModel):
    def __init__(
        self,
        name: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # {"en":"This must match the Name of a Volume", "zh_CN":"此字段必须与卷的名称匹配"}
        self.name = name
        # {"en":"Path within the container at which the volume should be mounted. Must not contain ':'", "zh_CN":"容器内卷的挂载路径。不得包含 ':'"}
        self.mount_path = mount_path
        # {"en":"Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false", "zh_CN":"如果为 true，则以只读方式挂载，否则（false 或未设置）以读写方式挂载。默认为 false"}
        self.read_only = read_only

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.mount_path, 'mount_path')
        self.validate_required(self.read_only, 'read_only')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class GetEcciInstanceContainer(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        memory_limit: str = None,
        name: str = None,
        image: str = None,
        command: List[str] = None,
        args: List[str] = None,
        working_dir: str = None,
        env: Dict[str, str] = None,
        env_ref: List[GetEcciInstanceContainerEnvRef] = None,
        volume_mounts: List[GetEcciInstanceVolumeMount] = None,
    ):
        # {"en":"GetEcciInstanceContainer cpu limit, the sum of all container cpu limits cannot exceed the instance cpu limit", "zh_CN":"容器cpu限制,所有容器cpu限制总和不能超过实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"GetEcciInstanceContainer memory limit, the sum of all container memory limits cannot exceed the instance memory limit", "zh_CN":"容器内存限制,所有容器内存限制总和不能超过实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"GetEcciInstanceContainer name", "zh_CN":"容器名称"}
        self.name = name
        # {"en":"GetEcciInstanceContainer image", "zh_CN":"容器镜像"}
        self.image = image
        # {"en":"Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided.", "zh_CN":"入口点数组。不在 Shell 中执行。如果未提供，则使用容器镜像的 ENTRYPOINT"}
        self.command = command
        # {"en":"Arguments to the entrypoint. The container image's CMD is used if this is not provided", "zh_CN":"entrypoint 的参数。如果未提供，则使用容器镜像的 CMD 设置"}
        self.args = args
        # {"en":"GetEcciInstanceContainer's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image", "zh_CN":"容器的工作目录。如果未指定，将使用容器运行时的默认值，默认值可能在容器镜像中配置"}
        self.working_dir = working_dir
        # {"en":"ist of environment variables to set in the container", "zh_CN":"要在容器中设置的环境变量列表"}
        self.env = env
        # {"en":"downwardapi type sensitive environment variables, authorization required", "zh_CN":"downwardapi 类型敏感环境变量,需授权"}
        self.env_ref = env_ref
        # {"en":"Pod volumes to mount into the container's filesystem. Cannot be updated", "zh_CN":"要挂载到容器文件系统中的 Pod 卷。无法更新"}
        self.volume_mounts = volume_mounts

    def validate(self):
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.name, 'name')
        self.validate_required(self.image, 'image')
        if self.env_ref:
            for k in self.env_ref:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.image is not None:
            result['image'] = self.image
        if self.command is not None:
            result['command'] = self.command
        if self.args is not None:
            result['args'] = self.args
        if self.working_dir is not None:
            result['workingDir'] = self.working_dir
        if self.env is not None:
            result['env'] = self.env
        if self.env_ref is not None:
            result['envRef'] = []
            for k in self.env_ref:
                result['envRef'].append(k.to_map() if k else None)
        if self.volume_mounts is not None:
            result['volumeMounts'] = []
            for k in self.volume_mounts:
                result['volumeMounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('envRef') is not None:
            self.env_ref = []
            for k in m.get('envRef'):
                temp_model = GetEcciInstanceContainerEnvRef()
                self.env_ref.append(temp_model.from_map(k))
        if m.get('volumeMounts') is not None:
            self.volume_mounts = []
            for k in m.get('volumeMounts'):
                temp_model = GetEcciInstanceVolumeMount()
                self.volume_mounts.append(temp_model.from_map(k))
        return self


class GetEcciInstancePodVolumeClaim(TeaModel):
    def __init__(
        self,
        claim_name: str = None,
    ):
        # {"en":"the name of a PersistentVolumeClaim in the same namespace as the pod using this volume", "zh_CN":"与使用此卷的 Pod 位于同一名字空间中的 PersistentVolumeClaim 的名称"}
        self.claim_name = claim_name

    def validate(self):
        self.validate_required(self.claim_name, 'claim_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_name is not None:
            result['claimName'] = self.claim_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('claimName') is not None:
            self.claim_name = m.get('claimName')
        return self


class GetEcciInstanceHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # {"en":"path of the directory on the host. If the path is a symlink, it will follow the link to the real path", "zh_CN":"目录在主机上的路径。如果该路径是一个符号链接，则它将沿着链接指向真实路径"}
        self.path = path
        # {"en":"type for HostPath Volume Defaults to ''", "zh_CN":"卷的类型。默认为 ''"}
        self.type = type

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetEcciInstancePodVolume(TeaModel):
    def __init__(
        self,
        name: str = None,
        persistent_volume_claim: GetEcciInstancePodVolumeClaim = None,
        host_path: GetEcciInstanceHostPathVolume = None,
    ):
        # {"en":"name of the volume. Must be a DNS_LABEL and unique within the pod.", "zh_CN":"卷的名称。必须是 DNS_LABEL 且在 Pod 内是唯一的。"}
        self.name = name
        # {"en":"represents a reference to a PersistentVolumeClaim in the same namespace", "zh_CN":"表示对同一名字空间中 PersistentVolumeClaim 的引用"}
        self.persistent_volume_claim = persistent_volume_claim
        # {"en":"Represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this.", "zh_CN":"表示主机上预先存在的文件或目录，它们将被直接暴露给容器。 这种卷通常用于系统代理或允许查看主机的其他特权操作。大多数容器不需要这种卷。"}
        self.host_path = host_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.persistent_volume_claim, 'persistent_volume_claim')
        if self.persistent_volume_claim:
            self.persistent_volume_claim.validate()
        self.validate_required(self.host_path, 'host_path')
        if self.host_path:
            self.host_path.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.persistent_volume_claim is not None:
            result['persistentVolumeClaim'] = self.persistent_volume_claim.to_map()
        if self.host_path is not None:
            result['hostPath'] = self.host_path.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('persistentVolumeClaim') is not None:
            temp_model = GetEcciInstancePodVolumeClaim()
            self.persistent_volume_claim = temp_model.from_map(m['persistentVolumeClaim'])
        if m.get('hostPath') is not None:
            temp_model = GetEcciInstanceHostPathVolume()
            self.host_path = temp_model.from_map(m['hostPath'])
        return self


class GetEcciInstanceLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
        operator: str = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.values, 'values')
        self.validate_required(self.operator, 'operator')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class GetEcciInstanceLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[GetEcciInstanceLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        self.validate_required(self.match_labels, 'match_labels')
        self.validate_required(self.match_expressions, 'match_expressions')
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetEcciInstanceLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetEcciInstancePodAffinityTerm(TeaModel):
    def __init__(
        self,
        label_selector: GetEcciInstanceLabelSelector = None,
        namespaces: List[str] = None,
        topology_key: str = None,
    ):
        # {"en":"A label query over a set of resources, in this case pods.", "zh_CN":"对一组资源的标签查询，在这里资源为 Pod。"}
        self.label_selector = label_selector
        # {"en":"pod's namespace", "zh_CN":" Pod 的名字空间"}
        self.namespaces = namespaces
        # {"en":"This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.", "zh_CN":"此 Pod 应与指定名字空间中与标签选择算符匹配的 Pod 集合位于同一位置（亲和性） 或位于不同位置（反亲和性），这里的“在同一位置”意味着运行在一个节点上，其键名为 topologyKey 的标签值与运行所选 Pod 集合中的某 Pod 的任何节点上的标签值匹配。 不允许使用空的 topologyKey。"}
        self.topology_key = topology_key

    def validate(self):
        self.validate_required(self.label_selector, 'label_selector')
        if self.label_selector:
            self.label_selector.validate()
        self.validate_required(self.namespaces, 'namespaces')
        self.validate_required(self.topology_key, 'topology_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.namespaces is not None:
            result['namespaces'] = self.namespaces
        if self.topology_key is not None:
            result['topologyKey'] = self.topology_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = GetEcciInstanceLabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')
        if m.get('topologyKey') is not None:
            self.topology_key = m.get('topologyKey')
        return self


class GetEcciInstanceWeightedPodAffinityTerm(TeaModel):
    def __init__(
        self,
        weight: int = None,
        pod_affinity_term: GetEcciInstancePodAffinityTerm = None,
    ):
        # {"en":"associated with matching the corresponding podAffinityTerm, in the range 1-100.", "zh_CN":"匹配相应 podAffinityTerm 条件的权重，范围为 1-100。"}
        self.weight = weight
        # {"en":"Required. A pod affinity term, associated with the corresponding weight.", "zh_CN":"必需的字段。一个 Pod 亲和性条件，对应一个与相应的权重值。"}
        self.pod_affinity_term = pod_affinity_term

    def validate(self):
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.pod_affinity_term, 'pod_affinity_term')
        if self.pod_affinity_term:
            self.pod_affinity_term.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['weight'] = self.weight
        if self.pod_affinity_term is not None:
            result['podAffinityTerm'] = self.pod_affinity_term.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('podAffinityTerm') is not None:
            temp_model = GetEcciInstancePodAffinityTerm()
            self.pod_affinity_term = temp_model.from_map(m['podAffinityTerm'])
        return self


class GetEcciInstancePodAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[GetEcciInstancePodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[GetEcciInstanceWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的亲和性要求（例如：由于 Pod 标签更新）， 系统可能会也可能不会尝试最终将 Pod 从其节点中逐出。 当此列表中有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器会更倾向于将 Pod 调度到满足该字段指定的亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。最优选择是权重总和最大的节点， 即对于满足所有调度要求（资源请求、requiredDuringScheduling 亲和表达式等）的每个节点， 通过迭代该字段的元素来计算总和，如果节点具有与相应 podAffinityTerm 匹配的 Pod，则将“权重”添加到总和中； 具有最高总和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = GetEcciInstancePodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = GetEcciInstanceWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class GetEcciInstancePodAntiAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[GetEcciInstancePodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[GetEcciInstanceWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的反亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的反亲和性要求（例如：由于 Pod 标签更新）， 系统可能会或可能不会尝试最终将 Pod 从其节点中逐出。 当有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器更倾向于将 Pod 调度到满足该字段指定的反亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。 最优选的节点是权重总和最大的节点，即对于满足所有调度要求（资源请求、requiredDuringScheduling 反亲和性表达式等）的每个节点，通过遍历元素来计算总和如果节点具有与相应 podAffinityTerm 匹配的 Pod，则此字段并在总和中添加\"权重\"；具有最高加和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = GetEcciInstancePodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = GetEcciInstanceWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class GetEcciInstanceAffinity(TeaModel):
    def __init__(
        self,
        pod_affinity: GetEcciInstancePodAffinity = None,
        pod_anti_affinity: GetEcciInstancePodAntiAffinity = None,
    ):
        # {"en":"A group of inter pod affinity scheduling rules.", "zh_CN":"一组 Pod 间亲和性调度规则。"}
        self.pod_affinity = pod_affinity
        # {"en":"A group of node affinity scheduling rules.", "zh_CN":"一组节点亲和性调度规则。"}
        self.pod_anti_affinity = pod_anti_affinity

    def validate(self):
        self.validate_required(self.pod_affinity, 'pod_affinity')
        if self.pod_affinity:
            self.pod_affinity.validate()
        self.validate_required(self.pod_anti_affinity, 'pod_anti_affinity')
        if self.pod_anti_affinity:
            self.pod_anti_affinity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_affinity is not None:
            result['podAffinity'] = self.pod_affinity.to_map()
        if self.pod_anti_affinity is not None:
            result['podAntiAffinity'] = self.pod_anti_affinity.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('podAffinity') is not None:
            temp_model = GetEcciInstancePodAffinity()
            self.pod_affinity = temp_model.from_map(m['podAffinity'])
        if m.get('podAntiAffinity') is not None:
            temp_model = GetEcciInstancePodAntiAffinity()
            self.pod_anti_affinity = temp_model.from_map(m['podAntiAffinity'])
        return self


class GetEcciInstancePodSpec(TeaModel):
    def __init__(
        self,
        containers: List[GetEcciInstanceContainer] = None,
        restart_policy: str = None,
        termination_grace_period_seconds: int = None,
        volumes: List[GetEcciInstancePodVolume] = None,
        affinity: GetEcciInstanceAffinity = None,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        kata_runtime: bool = None,
    ):
        # {"en":"List of containers belonging to the pod. There must be at least one container in a Pod. ", "zh_CN":"属于 Pod 的容器列表。Pod 中必须至少有一个容器。"}
        self.containers = containers
        # {"en":"Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always.", "zh_CN":"Pod 内所有容器的重启策略。Always、OnFailure、Never 之一。默认为 Always。"}
        self.restart_policy = restart_policy
        # {"en":"Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.", "zh_CN":"可选字段，表示 Pod 需要体面终止的所需的时长（以秒为单位）。字段值可以在删除请求中减少。 字段值必须是非负整数。零值表示收到 kill 信号则立即停止（没有机会关闭）。 如果此值为 nil，则将使用默认宽限期。 宽限期是从 Pod 中运行的进程收到终止信号后，到进程被 kill 信号强制停止之前，Pod 可以继续存在的时间（以秒为单位）。 应该将此值设置为比你的进程的预期清理时间更长。默认为 30 秒。"}
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # {"en":"List of volumes that can be mounted by containers belonging to the pod.", "zh_CN":"可以由属于 Pod 的容器挂载的卷列表。"}
        self.volumes = volumes
        # {"en":"If specified, the pod's scheduling constraints", "zh_CN":"如果指定了，则作为 Pod 的调度约束。"}
        self.affinity = affinity
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Whether to use kata runtime, Use kata by default", "zh_CN":"是否使用kata运行时,默认使用kata"}
        self.kata_runtime = kata_runtime

    def validate(self):
        self.validate_required(self.containers, 'containers')
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        self.validate_required(self.restart_policy, 'restart_policy')
        self.validate_required(self.termination_grace_period_seconds, 'termination_grace_period_seconds')
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()
        self.validate_required(self.affinity, 'affinity')
        if self.affinity:
            self.affinity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.containers is not None:
            result['containers'] = []
            for k in self.containers:
                result['containers'].append(k.to_map() if k else None)
        if self.restart_policy is not None:
            result['restartPolicy'] = self.restart_policy
        if self.termination_grace_period_seconds is not None:
            result['terminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.volumes is not None:
            result['volumes'] = []
            for k in self.volumes:
                result['volumes'].append(k.to_map() if k else None)
        if self.affinity is not None:
            result['affinity'] = self.affinity.to_map()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.labels is not None:
            result['labels'] = self.labels
        if self.kata_runtime is not None:
            result['kataRuntime'] = self.kata_runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containers') is not None:
            self.containers = []
            for k in m.get('containers'):
                temp_model = GetEcciInstanceContainer()
                self.containers.append(temp_model.from_map(k))
        if m.get('restartPolicy') is not None:
            self.restart_policy = m.get('restartPolicy')
        if m.get('terminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('terminationGracePeriodSeconds')
        if m.get('volumes') is not None:
            self.volumes = []
            for k in m.get('volumes'):
                temp_model = GetEcciInstancePodVolume()
                self.volumes.append(temp_model.from_map(k))
        if m.get('affinity') is not None:
            temp_model = GetEcciInstanceAffinity()
            self.affinity = temp_model.from_map(m['affinity'])
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('kataRuntime') is not None:
            self.kata_runtime = m.get('kataRuntime')
        return self


class GetEcciInstanceIspIp(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        name_en: str = None,
        ipv_4: str = None,
        ipv_6: str = None,
    ):
        # {"en":"operator id", "zh_CN":"运营商id"}
        self.id = id
        # {"en":"Operator Chinese name", "zh_CN":"运营商中文名"}
        self.name = name
        # {"en":"Operator english name", "zh_CN":"运营商英文名"}
        self.name_en = name_en
        # {"en":"ipv4 ip", "zh_CN":"ipv4 ip"}
        self.ipv_4 = ipv_4
        # {"en":"ipv6 ip", "zh_CN":"ipv6 ip"}
        self.ipv_6 = ipv_6

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_en, 'name_en')
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
        if self.name_en is not None:
            result['nameEn'] = self.name_en
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
        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        return self


class GetEcciInstanceSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"spread field support: group or cluster", "zh_CN":"分组策略,当前支持: group, cluster"}
        self.spread_by_field = spread_by_field
        # {"en":"max groups in field. by default 1", "zh_CN":"策略需要的最大分组个数.默认: 1"}
        self.max_groups = max_groups
        # {"en":"min groups in field. by default 1", "zh_CN":"策略需要的最小分组个数.默认: 1"}
        self.min_groups = min_groups

    def validate(self):
        self.validate_required(self.spread_by_field, 'spread_by_field')
        self.validate_required(self.max_groups, 'max_groups')
        self.validate_required(self.min_groups, 'min_groups')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class GetEcciInstanceClusterFailover(TeaModel):
    def __init__(
        self,
        cluster_failover: int = None,
        toleration_seconds: int = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"the cluser faileover. 0: off, 1: on. default 0", "zh_CN":"集群故障转移开关.0: 关闭,1打开. 默认:0 "}
        self.cluster_failover = cluster_failover
        # {"en":"the tolerationSeconds of the workload unhealthy. default 300", "zh_CN":"应用创建后多久时间没有runing,超过认为不健康.默认300秒"}
        self.toleration_seconds = toleration_seconds
        # {"en":"PurgeMode represents how to deal with the legacy applications on the cluster from which the application is migrated.only support Graciously", "zh_CN":"应用漂移后,旧应用的删除模式.只支持 Graciously 平滑删除"}
        self.purge_mode = purge_mode
        # {"en":"GracePeriodSeconds is the maximum waiting duration in seconds before application on the migrated cluster should be deleted. default:300", "zh_CN":"平滑删除时间. 默认:300秒 "}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        self.validate_required(self.cluster_failover, 'cluster_failover')
        self.validate_required(self.toleration_seconds, 'toleration_seconds')
        self.validate_required(self.purge_mode, 'purge_mode')
        self.validate_required(self.grace_period_seconds, 'grace_period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_failover is not None:
            result['clusterFailover'] = self.cluster_failover
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterFailover') is not None:
            self.cluster_failover = m.get('clusterFailover')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class GetEcciInstanceClusterBehavior(TeaModel):
    def __init__(
        self,
        spread_constraint: List[GetEcciInstanceSpreadConstraint] = None,
        cluster_failover: GetEcciInstanceClusterFailover = None,
    ):
        # {"en":"a list of the scheduling constraints", "zh_CN":"调度策略列表"}
        self.spread_constraint = spread_constraint
        # {"en":"cluster faileover", "zh_CN":"集群重调度"}
        self.cluster_failover = cluster_failover

    def validate(self):
        self.validate_required(self.spread_constraint, 'spread_constraint')
        if self.spread_constraint:
            for k in self.spread_constraint:
                if k:
                    k.validate()
        self.validate_required(self.cluster_failover, 'cluster_failover')
        if self.cluster_failover:
            self.cluster_failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_constraint is not None:
            result['spreadConstraint'] = []
            for k in self.spread_constraint:
                result['spreadConstraint'].append(k.to_map() if k else None)
        if self.cluster_failover is not None:
            result['clusterFailover'] = self.cluster_failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadConstraint') is not None:
            self.spread_constraint = []
            for k in m.get('spreadConstraint'):
                temp_model = GetEcciInstanceSpreadConstraint()
                self.spread_constraint.append(temp_model.from_map(k))
        if m.get('clusterFailover') is not None:
            temp_model = GetEcciInstanceClusterFailover()
            self.cluster_failover = temp_model.from_map(m['clusterFailover'])
        return self


class GetEcciInstanceEcciInstanceDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        display_name: str = None,
        private_ips: List[str] = None,
        cluster_name: str = None,
        cpu_limit: str = None,
        memory_limit: str = None,
        cpu_request: str = None,
        memory_request: str = None,
        status: str = None,
        containers: int = None,
        running_containers: int = None,
        description: str = None,
        pod_spec: GetEcciInstancePodSpec = None,
        create_time: str = None,
        update_time: str = None,
        area: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        allocate_public_ip: bool = None,
        isps: List[GetEcciInstanceIspIp] = None,
        failover: bool = None,
        colocation: bool = None,
        cluster_behavior: GetEcciInstanceClusterBehavior = None,
    ):
        # {"en":"Instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Instance display name", "zh_CN":"实例展示名称"}
        self.display_name = display_name
        # {"en":"private ip list", "zh_CN":"内网ip列表"}
        self.private_ips = private_ips
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"instance cpu limit", "zh_CN":"实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"instance memory limit", "zh_CN":"实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"Minimum amount of cpu resources required", "zh_CN":"cpu 要求最小资源量"}
        self.cpu_request = cpu_request
        # {"en":"Minimum amount of memory resources required", "zh_CN":"内存要求最小资源量"}
        self.memory_request = memory_request
        # {"en":"pod status", "zh_CN":"pod状态"}
        self.status = status
        # {"en":"Number of containers ", "zh_CN":"容器数量"}
        self.containers = containers
        # {"en":"Number of running containers ", "zh_CN":"运行中容器数量"}
        self.running_containers = running_containers
        # {"en":"description ", "zh_CN":"描述"}
        self.description = description
        # {"en":"Specification of the desired behavior of the pod.", "zh_CN":"Pod 预期行为的规约。"}
        self.pod_spec = pod_spec
        # {"en":"create time ", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"update time ", "zh_CN":"更新时间"}
        self.update_time = update_time
        # {"en":"area", "zh_CN":"区域"}
        self.area = area
        # {"en":"country", "zh_CN":"国家"}
        self.country = country
        # {"en":"province", "zh_CN":"省份"}
        self.province = province
        # {"en":"city", "zh_CN":"城市"}
        self.city = city
        # {"en":"Whether to assign public IP", "zh_CN":"是否分配公网ip"}
        self.allocate_public_ip = allocate_public_ip
        # {"en":"IP operator list", "zh_CN":"ip运营商列表"}
        self.isps = isps
        # {"en":"Whether to enable fault scheduling", "zh_CN":"是否开启故障调度"}
        self.failover = failover
        # {"en":"is colocation resource or not", "zh_CN":"是否在离线混部资源"}
        self.colocation = colocation
        # {"en":"the cluster behavior", "zh_CN":"集群策略配置"}
        self.cluster_behavior = cluster_behavior

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.private_ips, 'private_ips')
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.cpu_request, 'cpu_request')
        self.validate_required(self.memory_request, 'memory_request')
        self.validate_required(self.status, 'status')
        self.validate_required(self.containers, 'containers')
        self.validate_required(self.running_containers, 'running_containers')
        self.validate_required(self.description, 'description')
        self.validate_required(self.pod_spec, 'pod_spec')
        if self.pod_spec:
            self.pod_spec.validate()
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.area, 'area')
        self.validate_required(self.country, 'country')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.allocate_public_ip, 'allocate_public_ip')
        self.validate_required(self.isps, 'isps')
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()
        self.validate_required(self.failover, 'failover')
        self.validate_required(self.colocation, 'colocation')
        self.validate_required(self.cluster_behavior, 'cluster_behavior')
        if self.cluster_behavior:
            self.cluster_behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.private_ips is not None:
            result['privateIps'] = self.private_ips
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.cpu_request is not None:
            result['cpuRequest'] = self.cpu_request
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.status is not None:
            result['status'] = self.status
        if self.containers is not None:
            result['containers'] = self.containers
        if self.running_containers is not None:
            result['runningContainers'] = self.running_containers
        if self.description is not None:
            result['description'] = self.description
        if self.pod_spec is not None:
            result['podSpec'] = self.pod_spec.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.area is not None:
            result['area'] = self.area
        if self.country is not None:
            result['country'] = self.country
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.allocate_public_ip is not None:
            result['allocatePublicIp'] = self.allocate_public_ip
        if self.isps is not None:
            result['isps'] = []
            for k in self.isps:
                result['isps'].append(k.to_map() if k else None)
        if self.failover is not None:
            result['failover'] = self.failover
        if self.colocation is not None:
            result['colocation'] = self.colocation
        if self.cluster_behavior is not None:
            result['clusterBehavior'] = self.cluster_behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('privateIps') is not None:
            self.private_ips = m.get('privateIps')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('cpuRequest') is not None:
            self.cpu_request = m.get('cpuRequest')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('containers') is not None:
            self.containers = m.get('containers')
        if m.get('runningContainers') is not None:
            self.running_containers = m.get('runningContainers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('podSpec') is not None:
            temp_model = GetEcciInstancePodSpec()
            self.pod_spec = temp_model.from_map(m['podSpec'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('allocatePublicIp') is not None:
            self.allocate_public_ip = m.get('allocatePublicIp')
        if m.get('isps') is not None:
            self.isps = []
            for k in m.get('isps'):
                temp_model = GetEcciInstanceIspIp()
                self.isps.append(temp_model.from_map(k))
        if m.get('failover') is not None:
            self.failover = m.get('failover')
        if m.get('colocation') is not None:
            self.colocation = m.get('colocation')
        if m.get('clusterBehavior') is not None:
            temp_model = GetEcciInstanceClusterBehavior()
            self.cluster_behavior = temp_model.from_map(m['clusterBehavior'])
        return self


class GetEcciInstanceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetEcciInstanceEcciInstanceDetail = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"instanceDetail", "zh_CN":"实例详情"}
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
            temp_model = GetEcciInstanceEcciInstanceDetail()
            self.data = temp_model.from_map(m['data'])
        return self


class GetEcciInstancePaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"instance name", "zh_CN":"实例名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetEcciInstanceParameters(TeaModel):
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


class GetEcciInstanceRequestHeader(TeaModel):
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


class GetEcciInstanceResponseHeader(TeaModel):
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






class DeleteEcciInstanceRequest(TeaModel):
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


class DeleteEcciInstanceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEcciInstancePaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"instance name", "zh_CN":"实例名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteEcciInstanceParameters(TeaModel):
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


class DeleteEcciInstanceRequestHeader(TeaModel):
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


class DeleteEcciInstanceResponseHeader(TeaModel):
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






class InstanceRebuildRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        image_id: str = None,
        password: str = None,
        retain_data_disk: int = None,
    ):
        # {"en":"vm id", "zh_CN":"云主机ID"}
        self.id = id
        # {"en":"Image ID", "zh_CN":"镜像ID（指定了镜像ID则使用指定的镜像重装，否则使用原镜像重装）"}
        self.image_id = image_id
        # {"en":"password", "zh_CN":"密码（使用公共镜像重装必须指定密码，使用自定义镜像可不指定）"}
        self.password = password
        # {"en":"Retain Data Disk", "zh_CN":"是否保留数据盘（1：是；-1：否）"}
        self.retain_data_disk = retain_data_disk

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.password is not None:
            result['password'] = self.password
        if self.retain_data_disk is not None:
            result['retainDataDisk'] = self.retain_data_disk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('retainDataDisk') is not None:
            self.retain_data_disk = m.get('retainDataDisk')
        return self


class InstanceRebuildResponse(TeaModel):
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


class InstanceRebuildPaths(TeaModel):
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


class InstanceRebuildParameters(TeaModel):
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


class InstanceRebuildRequestHeader(TeaModel):
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


class InstanceRebuildResponseHeader(TeaModel):
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






class GetTokenRequest(TeaModel):
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


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"token", "zh_CN":"token"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
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
            self.data = m.get('data')
        return self


class GetTokenPaths(TeaModel):
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


class GetTokenParameters(TeaModel):
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


class GetTokenRequestHeader(TeaModel):
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


class GetTokenResponseHeader(TeaModel):
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






class VMPRemoveInstanceRequest(TeaModel):
    def __init__(
        self,
        servers: str = None,
    ):
        # {"en":"Instance ID", "zh_CN":"实例唯一标识。单次最多可发送100 条ID，ID 之间用半角逗号字符“,”隔开。"}
        self.servers = servers

    def validate(self):
        self.validate_required(self.servers, 'servers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servers is not None:
            result['servers'] = self.servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        return self


class VMPRemoveInstanceResponse(TeaModel):
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


class VMPRemoveInstancePaths(TeaModel):
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


class VMPRemoveInstanceParameters(TeaModel):
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


class VMPRemoveInstanceRequestHeader(TeaModel):
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


class VMPRemoveInstanceResponseHeader(TeaModel):
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






class QueryGpsRequest(TeaModel):
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


class QueryGpsGpsInfo(TeaModel):
    def __init__(
        self,
        longitude: float = None,
        latitude: float = None,
        instance_id: str = None,
        status: str = None,
        message: str = None,
    ):
        # {"en":"longitude", "zh_CN":"经度"}
        self.longitude = longitude
        # {"en":"latitude", "zh_CN":"纬度"}
        self.latitude = latitude
        # {"en":"instance id", "zh_CN":"实例id"}
        self.instance_id = instance_id
        # {"en":"query status", "zh_CN":"查询状态"}
        self.status = status
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.longitude, 'longitude')
        self.validate_required(self.latitude, 'latitude')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryGpsResponse(TeaModel):
    def __init__(
        self,
        data: List[QueryGpsGpsInfo] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"list of ephone instances", "zh_CN":"云手机实例列表"}
        self.data = data
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = QueryGpsGpsInfo()
                self.data.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryGpsPaths(TeaModel):
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


class QueryGpsParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        name: str = None,
    ):
        # {"en":"instance ID to be queried", "zh_CN":"要查询的实例id"}
        self.ids = ids
        # {"en":"instance name bo be queried", "zh_CN":"要查询的实例名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryGpsRequestHeader(TeaModel):
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


class QueryGpsResponseHeader(TeaModel):
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






class ScreenshotEphoneInstanceScreenshotObject(TeaModel):
    def __init__(
        self,
        id: str = None,
        size: str = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.id = id
        # {"en":"screenshot image size, optional value:  tiny, small, medium, large", "zh_CN":"截图大小，可选值有: tiny, small, medium, large"}
        self.size = size

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.size, 'size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ScreenshotEphoneInstanceRequest(TeaModel):
    def __init__(
        self,
        ephones: List[ScreenshotEphoneInstanceScreenshotObject] = None,
    ):
        # {"en":"list of instances to operate on", "zh_CN":"操作实例的数组对象"}
        self.ephones = ephones

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = ScreenshotEphoneInstanceScreenshotObject()
                self.ephones.append(temp_model.from_map(k))
        return self


class ScreenshotEphoneInstanceScreenshotData(TeaModel):
    def __init__(
        self,
        id: str = None,
        data: str = None,
        message: str = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.id = id
        # {"en":"data encoded via base64 for screenshot image", "zh_CN":"base64编码过的截图数据"}
        self.data = data
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ScreenshotEphoneInstanceResponse(TeaModel):
    def __init__(
        self,
        ephones: List[ScreenshotEphoneInstanceScreenshotData] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.ephones = ephones
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = ScreenshotEphoneInstanceScreenshotData()
                self.ephones.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ScreenshotEphoneInstancePaths(TeaModel):
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


class ScreenshotEphoneInstanceParameters(TeaModel):
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


class ScreenshotEphoneInstanceRequestHeader(TeaModel):
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


class ScreenshotEphoneInstanceResponseHeader(TeaModel):
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






class VMPInstanceOperationRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
    ):
        # {"en":"Instance action.
        # Values:
        # START: START the
        # SHUTDOWN: SHUTDOWN
        # REBOOT: Force a REBOOT", "zh_CN":"实例操作动作。
        # 取值：
        # START：启动
        # SHUTDOWN：正常关机
        # REBOOT：强制重启"}
        self.operation = operation

    def validate(self):
        self.validate_required(self.operation, 'operation')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        return self


class VMPInstanceOperationResponse(TeaModel):
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


class VMPInstanceOperationPaths(TeaModel):
    def __init__(
        self,
        server_id: str = None,
    ):
        # {"en":"Unique identity of virtual machine", "zh_CN":"实例唯一标识"}
        self.server_id = server_id

    def validate(self):
        self.validate_required(self.server_id, 'server_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['serverId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverId') is not None:
            self.server_id = m.get('serverId')
        return self


class VMPInstanceOperationParameters(TeaModel):
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


class VMPInstanceOperationRequestHeader(TeaModel):
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


class VMPInstanceOperationResponseHeader(TeaModel):
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






class ManageEphoneInstanceAppParamsObject(TeaModel):
    def __init__(
        self,
        oem_image: str = None,
        longitude: str = None,
        latitude: str = None,
        hardware: str = None,
        retain_data: str = None,
    ):
        # {"en":"oem image id", "zh_CN":"oem镜像id"}
        self.oem_image = oem_image
        # {"en":"longitude", "zh_CN":"经度"}
        self.longitude = longitude
        # {"en":"latitude", "zh_CN":"纬度"}
        self.latitude = latitude
        # {"en":"hardware info in json format", "zh_CN":"json 格式的硬件信息"}
        self.hardware = hardware
        # {"en":"retain user data", "zh_CN":"renew重装系统时生效，指定true可保留用户数据，不指定或者指定false会清空用户数据"}
        self.retain_data = retain_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_image is not None:
            result['oemImage'] = self.oem_image
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.hardware is not None:
            result['hardware'] = self.hardware
        if self.retain_data is not None:
            result['retainData'] = self.retain_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemImage') is not None:
            self.oem_image = m.get('oemImage')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('hardware') is not None:
            self.hardware = m.get('hardware')
        if m.get('retainData') is not None:
            self.retain_data = m.get('retainData')
        return self


class ManageEphoneInstanceOperateObject(TeaModel):
    def __init__(
        self,
        id: str = None,
        op: str = None,
        params: ManageEphoneInstanceAppParamsObject = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.id = id
        # {"en":"operate type", "zh_CN":"操作类型，可选值：delete, reboot, renew, clear, setGps, createH5"}
        self.op = op
        # {"en":"app operaate params", "zh_CN":"app 操作的参数"}
        self.params = params

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.op, 'op')
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.op is not None:
            result['op'] = self.op
        if self.params is not None:
            result['params'] = self.params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('params') is not None:
            temp_model = ManageEphoneInstanceAppParamsObject()
            self.params = temp_model.from_map(m['params'])
        return self


class ManageEphoneInstanceRequest(TeaModel):
    def __init__(
        self,
        ephones: List[ManageEphoneInstanceOperateObject] = None,
    ):
        # {"en":"list of instances to operate on", "zh_CN":"操作实例的数组对象"}
        self.ephones = ephones

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = ManageEphoneInstanceOperateObject()
                self.ephones.append(temp_model.from_map(k))
        return self


class ManageEphoneInstanceTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        message: str = None,
    ):
        # {"en":"task id", "zh_CN":"任务单id"}
        self.id = id
        # {"en":"message", "zh_CN":"任务单消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ManageEphoneInstanceResponse(TeaModel):
    def __init__(
        self,
        tasks: List[ManageEphoneInstanceTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['tasks'] = []
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = []
            for k in m.get('tasks'):
                temp_model = ManageEphoneInstanceTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ManageEphoneInstancePaths(TeaModel):
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


class ManageEphoneInstanceParameters(TeaModel):
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


class ManageEphoneInstanceRequestHeader(TeaModel):
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


class ManageEphoneInstanceResponseHeader(TeaModel):
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






class RunEphoneAdbShellAdbObject(TeaModel):
    def __init__(
        self,
        id: str = None,
        command: str = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.id = id
        # {"en":"adb shell command content", "zh_CN":"adb shell 命令的内容"}
        self.command = command

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.command, 'command')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('command') is not None:
            self.command = m.get('command')
        return self


class RunEphoneAdbShellRequest(TeaModel):
    def __init__(
        self,
        ephones: List[RunEphoneAdbShellAdbObject] = None,
    ):
        # {"en":"list of instances to run adb shell on", "zh_CN":"要执行adb shell的实例数组对象"}
        self.ephones = ephones

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = RunEphoneAdbShellAdbObject()
                self.ephones.append(temp_model.from_map(k))
        return self


class RunEphoneAdbShellTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        message: str = None,
    ):
        # {"en":"task id", "zh_CN":"任务单id"}
        self.id = id
        # {"en":"message", "zh_CN":"任务单消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RunEphoneAdbShellResponse(TeaModel):
    def __init__(
        self,
        tasks: List[RunEphoneAdbShellTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['tasks'] = []
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = []
            for k in m.get('tasks'):
                temp_model = RunEphoneAdbShellTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RunEphoneAdbShellPaths(TeaModel):
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


class RunEphoneAdbShellParameters(TeaModel):
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


class RunEphoneAdbShellRequestHeader(TeaModel):
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


class RunEphoneAdbShellResponseHeader(TeaModel):
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






class VMPQueryInstanceRequest(TeaModel):
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


class VMPQueryInstanceAccessIP(TeaModel):
    def __init__(
        self,
        address: str = None,
        carrier: str = None,
        protocol: int = None,
    ):
        # {"en":"Ip address", "zh_CN":"Ip地址"}
        self.address = address
        # {"en":"IP address operator", "zh_CN":"Ip地址所属运营商"}
        self.carrier = carrier
        # {"en":"Protocol type: 4: IPv4 address; 6: IPv6 address", "zh_CN":"协议类型：4：ipv4地址；6：ipv6地址"}
        self.protocol = protocol

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.protocol, 'protocol')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class VMPQueryInstanceDiskInfo(TeaModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
        category: str = None,
    ):
        # {"en":"Disk size (GB)", "zh_CN":"磁盘大小（GB）"}
        self.size = size
        # {"en":"Disk Purpose: System - System disk;DATA - DATA plate", "zh_CN":"磁盘用途：SYSTEM-系统盘；DATA-数据盘"}
        self.type = type
        # {"en":"Disk type: HDD/SSD", "zh_CN":"磁盘类型：HDD/SSD"}
        self.category = category

    def validate(self):
        self.validate_required(self.size, 'size')
        self.validate_required(self.type, 'type')
        self.validate_required(self.category, 'category')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class VMPQueryInstanceServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_name: str = None,
        province: str = None,
        carrier: str = None,
        image_id: str = None,
        flavor_id: str = None,
        name: str = None,
        state: str = None,
        created_at: str = None,
        access_ipv_4: str = None,
        private_ipv_4: str = None,
        private_ipv_6: str = None,
        key_name: str = None,
        node_name: str = None,
        access_ip: List[VMPQueryInstanceAccessIP] = None,
        is_free: str = None,
        is_bm: int = None,
        security_group_ids: List[str] = None,
        disk_info: List[VMPQueryInstanceDiskInfo] = None,
        tag: str = None,
    ):
        # {"en":"Unique identity of virtual machine", "zh_CN":"实例唯一标识"}
        self.id = id
        # {"en":"Virtual Machine Area", "zh_CN":"实例所属区域"}
        self.region_name = region_name
        # {"en":"Province of virtual machine", "zh_CN":"实例所属省份"}
        self.province = province
        # {"en":"Operator of virtual machine", "zh_CN":"实例所属运营商"}
        self.carrier = carrier
        # {"en":"Virtual machine image information", "zh_CN":"实例镜像信息"}
        self.image_id = image_id
        # {"en":"Virtual machine specifications", "zh_CN":"实例规格"}
        self.flavor_id = flavor_id
        # {"en":"Virtual machine name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Virtual machine status", "zh_CN":"实例状态"}
        self.state = state
        # {"en":"Virtual machine creation time", "zh_CN":"实例创建时间"}
        self.created_at = created_at
        # {"en":"Virtual machine IP address", "zh_CN":"实例IP地址"}
        self.access_ipv_4 = access_ipv_4
        # {"en":"IPv4 address of virtual machine intranet. If intranet is specified when creating virtual machine, intranet IP is returned. Otherwise, it is empty.", "zh_CN":"实例内网IPv4地址，如果创建实例时指定了需要内网，则返回内网IPv4，否则是空"}
        self.private_ipv_4 = private_ipv_4
        # {"en":"IPv6 address of virtual machine intranet. If intranet is specified when creating virtual machine, intranet IP is returned. Otherwise, it is empty.", "zh_CN":"实例内网IPv6地址，如果创建实例时指定了需要内网，则返回内网IPv6，否则是空"}
        self.private_ipv_6 = private_ipv_6
        # {"en":"Virtual machine login SSH key pair name", "zh_CN":"实例登录SSH秘钥对名称"}
        self.key_name = key_name
        # {"en":"Node name, the name of the node where the virtual machine is located. Through this node name, you can query the real-time redundant bandwidth of each node.", "zh_CN":"节点名称，实例所在节点名称，通过这个节点名称可以查询每个节点的实时冗余带宽情况"}
        self.node_name = node_name
        # {"en":"Virtual machine IP address", "zh_CN":"实例ip地址"}
        self.access_ip = access_ip
        # {"en":"If it is free instance, value: YES free instance, NO billing instance", "zh_CN":"是否免费实例，取值：YES 免费实例，NO 计费实例"}
        self.is_free = is_free
        # {"en":"1 indicates that the instance is bare metal
        # -1 indicates that the instance is a virtual machine", "zh_CN":"1表示该实例是裸机
        # -1表示该实例是虚拟机"}
        self.is_bm = is_bm
        # {"en":"A list of security group IDs for instance bindings", "zh_CN":"实例绑定的安全组id列表"}
        self.security_group_ids = security_group_ids
        # {"en":"Disk information", "zh_CN":"磁盘信息"}
        self.disk_info = disk_info
        # {"en":"instance tag", "zh_CN":"实例标签"}
        self.tag = tag

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.region_name, 'region_name')
        self.validate_required(self.province, 'province')
        self.validate_required(self.carrier, 'carrier')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.flavor_id, 'flavor_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.state, 'state')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.access_ipv_4, 'access_ipv_4')
        self.validate_required(self.private_ipv_4, 'private_ipv_4')
        self.validate_required(self.private_ipv_6, 'private_ipv_6')
        self.validate_required(self.key_name, 'key_name')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.access_ip, 'access_ip')
        if self.access_ip:
            for k in self.access_ip:
                if k:
                    k.validate()
        self.validate_required(self.is_free, 'is_free')
        self.validate_required(self.is_bm, 'is_bm')
        self.validate_required(self.security_group_ids, 'security_group_ids')
        self.validate_required(self.disk_info, 'disk_info')
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()
        self.validate_required(self.tag, 'tag')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.flavor_id is not None:
            result['flavorId'] = self.flavor_id
        if self.name is not None:
            result['name'] = self.name
        if self.state is not None:
            result['state'] = self.state
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.access_ipv_4 is not None:
            result['accessIPv4'] = self.access_ipv_4
        if self.private_ipv_4 is not None:
            result['privateIPv4'] = self.private_ipv_4
        if self.private_ipv_6 is not None:
            result['privateIPv6'] = self.private_ipv_6
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.access_ip is not None:
            result['accessIP'] = []
            for k in self.access_ip:
                result['accessIP'].append(k.to_map() if k else None)
        if self.is_free is not None:
            result['isFree'] = self.is_free
        if self.is_bm is not None:
            result['isBm'] = self.is_bm
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.disk_info is not None:
            result['diskInfo'] = []
            for k in self.disk_info:
                result['diskInfo'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('flavorId') is not None:
            self.flavor_id = m.get('flavorId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('accessIPv4') is not None:
            self.access_ipv_4 = m.get('accessIPv4')
        if m.get('privateIPv4') is not None:
            self.private_ipv_4 = m.get('privateIPv4')
        if m.get('privateIPv6') is not None:
            self.private_ipv_6 = m.get('privateIPv6')
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('accessIP') is not None:
            self.access_ip = []
            for k in m.get('accessIP'):
                temp_model = VMPQueryInstanceAccessIP()
                self.access_ip.append(temp_model.from_map(k))
        if m.get('isFree') is not None:
            self.is_free = m.get('isFree')
        if m.get('isBm') is not None:
            self.is_bm = m.get('isBm')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('diskInfo') is not None:
            self.disk_info = []
            for k in m.get('diskInfo'):
                temp_model = VMPQueryInstanceDiskInfo()
                self.disk_info.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class VMPQueryInstanceResponse(TeaModel):
    def __init__(
        self,
        servers: List[VMPQueryInstanceServer] = None,
    ):
        # {"en":"Virtual machine information array", "zh_CN":"实例信息数组"}
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
                temp_model = VMPQueryInstanceServer()
                self.servers.append(temp_model.from_map(k))
        return self


class VMPQueryInstancePaths(TeaModel):
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


class VMPQueryInstanceParameters(TeaModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_dir: str = None,
        limit: int = None,
        marker: str = None,
        ids: str = None,
        region_name: str = None,
        province: str = None,
        carrier: str = None,
        image_id: str = None,
        flavor_id: str = None,
        name: str = None,
        ips: str = None,
        state: str = None,
        is_free: str = None,
        is_bm: str = None,
        tags: str = None,
        ipv_6format: str = None,
    ):
        # {"en":"Sort field name, can have more than one, value:
        # Name, regionName, createdAt, type, state, nodeName, etc", "zh_CN":"排序的字段名称，可以有多个，取值：
        # name、regionName、createdAt、province、state、nodeName等"}
        self.sort_key = sort_key
        # {"en":"There can be multiple field names for sorting, with values:
        # 
        # Name, regionname, createdat, province, state, nodeName, etc.'", "zh_CN":"排序方向，必须跟在sortKey后面出现，取值：
        # desc：降序，默认值
        # asc：升序"}
        self.sort_dir = sort_dir
        # {"en":"The number of items displayed on each page is 20 by default", "zh_CN":"每个页面显示条数，默认是20"}
        self.limit = limit
        # {"en":"Query from the virtual machine ID specified by the marker", "zh_CN":"从marker指定的实例id开始查询，升序查询（若要分页查询，则不能指定sortKey参数）"}
        self.marker = marker
        # {"en":"Virtual machine ID. A maximum of 100 IDS can be queried at a time. The IDs are separated by a half angle comma character ','.", "zh_CN":"实例ID。单次最多查询 100 条 ID，ID 之间用半角逗号字符','隔开。"}
        self.ids = ids
        # {"en":"Name of the region, for example, South China region is Huanan, refer to Appendix 3", "zh_CN":"区域名称（区域列表详见附录1：https://www.wangsu.com/document/18204/areas-list?rsr=ws）"}
        self.region_name = region_name
        # {"en":"Province of virtual machine", "zh_CN":"实例所属省份（详见附录2：https://www.wangsu.com/document/18204/isp-list?rsr=ws）"}
        self.province = province
        # {"en":"Operator of virtual machine", "zh_CN":"实例所属运营商：dx-电信；wt-网通；yd-移动"}
        self.carrier = carrier
        # {"en":"Virtual machine image identity", "zh_CN":"实例镜像标识"}
        self.image_id = image_id
        # {"en":"Virtual machine specification ID", "zh_CN":"实例规格标识"}
        self.flavor_id = flavor_id
        # {"en":"Virtual machine name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Virtual machine ips. A maximum of 100 IPS can be queried at a time. The IPs are separated by a half angle comma character ','.", "zh_CN":"实例IP。单次最多查询 100 条 IP，IP 之间用半角逗号字符','隔开。"}
        self.ips = ips
        # {"en":"Virtual machine status, value (meaning to query virtual machines in the following status)
        # 
        # Running status
        # 
        # Building new status
        # 
        # Stopped stop
        # 
        # ERROR error
        # 
        # Deleting destroying
        # 
        # Restarting
        # 
        # Starting
        # 
        # Stopping", "zh_CN":"实例状态，取值（意为查询处于下述状态的虚拟机）
        # RUNNING 运行状态
        # BUILDING 新建状态
        # STOPPED 停机
        # ERROR 错误
        # DELETING 销毁中
        # RESTARTING  重启中
        # STARTING  启动中
        # STOPPING  停止中"}
        self.state = state
        # {"en":"Whether it is a free instance, value:
        # Yes free instances, NO billed instances", "zh_CN":"是否免费实例，取值:
        # YES 免费实例，NO 计费实例"}
        self.is_free = is_free
        # {"en":"1 means to query only bare-metal instances,
        # -1 means that only virtual machine instances are queried,
        # Without this parameter all cloud hosts are queried", "zh_CN":"1表示只查询裸机实例，
        # -1表示只查询虚拟机实例，
        # 不带这个参数表示查询所有云主机"}
        self.is_bm = is_bm
        # {"en":"Cloud Host Label
        # Multiple values are separated by a half corner comma, and the relationship between multiple values is or, that is, the instance label equals any one of these multiple values", "zh_CN":"云主机标签
        # 多个值用半角逗号隔开，多个值是或者的关系，即实例标签等于这多个中的任意一个就满足条件"}
        self.tags = tags
        # {"en":"ipv6 formate: 1: Zero Compressed(default); 6: With Leading Zero Suppression; 3: Full Address", "zh_CN":"ipv6格式：1：省略零压缩格式(默认)；2：省略前导零格式; 3: 完整格式"}
        self.ipv_6format = ipv_6format

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
        if self.ids is not None:
            result['ids'] = self.ids
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.flavor_id is not None:
            result['flavorId'] = self.flavor_id
        if self.name is not None:
            result['name'] = self.name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.state is not None:
            result['state'] = self.state
        if self.is_free is not None:
            result['isFree'] = self.is_free
        if self.is_bm is not None:
            result['isBm'] = self.is_bm
        if self.tags is not None:
            result['tags'] = self.tags
        if self.ipv_6format is not None:
            result['ipv6Format'] = self.ipv_6format
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
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('flavorId') is not None:
            self.flavor_id = m.get('flavorId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('isFree') is not None:
            self.is_free = m.get('isFree')
        if m.get('isBm') is not None:
            self.is_bm = m.get('isBm')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('ipv6Format') is not None:
            self.ipv_6format = m.get('ipv6Format')
        return self


class VMPQueryInstanceRequestHeader(TeaModel):
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


class VMPQueryInstanceResponseHeader(TeaModel):
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






class InstanceIPV6ManagementRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        instance_id: str = None,
    ):
        # {"en":"Operation:
        # ALLOCATION - ipv6 application
        # REMOVE - ipv6 is removed", "zh_CN":"操作：
        # ALLOCATION-ipv6申请 
        # REMOVE-ipv6移除"}
        self.action = action
        # {"en":"Instance ID (single only)", "zh_CN":"实例id（只支持单个）"}
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.action, 'action')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class InstanceIPV6ManagementResponse(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        access_ipv_6: List[str] = None,
    ):
        # {"en":"none", "zh_CN":"实例id"}
        self.instance_id = instance_id
        # {"en":"Instance IPv6 addresses, one for each operator if it is a multi-line node", "zh_CN":"实例ipv6地址，如果是多线节点，每个运营商各分配一个地址"}
        self.access_ipv_6 = access_ipv_6

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.access_ipv_6, 'access_ipv_6')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.access_ipv_6 is not None:
            result['accessIPv6'] = self.access_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('accessIPv6') is not None:
            self.access_ipv_6 = m.get('accessIPv6')
        return self


class InstanceIPV6ManagementPaths(TeaModel):
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


class InstanceIPV6ManagementParameters(TeaModel):
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


class InstanceIPV6ManagementRequestHeader(TeaModel):
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


class InstanceIPV6ManagementResponseHeader(TeaModel):
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






class GetEcciInstanceListRequest(TeaModel):
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


class GetEcciInstanceListIspIp(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        name_en: str = None,
        ipv_4: str = None,
        ipv_6: str = None,
    ):
        # {"en":"operator id", "zh_CN":"运营商id"}
        self.id = id
        # {"en":"Operator Chinese name", "zh_CN":"运营商中文名"}
        self.name = name
        # {"en":"Operator english name", "zh_CN":"运营商英文名"}
        self.name_en = name_en
        # {"en":"ipv4 ip", "zh_CN":"ipv4 ip"}
        self.ipv_4 = ipv_4
        # {"en":"ipv6 ip", "zh_CN":"ipv6 ip"}
        self.ipv_6 = ipv_6

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_en, 'name_en')
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
        if self.name_en is not None:
            result['nameEn'] = self.name_en
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
        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        return self


class GetEcciInstanceListEcciInstanceSummary(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        display_name: str = None,
        private_ips: List[str] = None,
        cluster_name: str = None,
        cpu_limit: str = None,
        cpu_request: str = None,
        memory_limit: str = None,
        memory_request: str = None,
        status: str = None,
        create_time: str = None,
        area: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        pod_name: str = None,
        isps: List[GetEcciInstanceListIspIp] = None,
        colocation: bool = None,
    ):
        # {"en":"Instance id", "zh_CN":"实例d"}
        self.id = id
        # {"en":"Instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Instance display name", "zh_CN":"实例展示名称"}
        self.display_name = display_name
        # {"en":"private ip list", "zh_CN":"内网ip列表"}
        self.private_ips = private_ips
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"instance cpu limit", "zh_CN":"实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"Minimum amount of cpu resources required", "zh_CN":"cpu 要求最小资源量"}
        self.cpu_request = cpu_request
        # {"en":"instance memory limit", "zh_CN":"实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"Minimum amount of memory resources required", "zh_CN":"内存要求最小资源量"}
        self.memory_request = memory_request
        # {"en":"pod status", "zh_CN":"pod状态"}
        self.status = status
        # {"en":"create time ", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"area", "zh_CN":"区域"}
        self.area = area
        # {"en":"country", "zh_CN":"国家"}
        self.country = country
        # {"en":"province", "zh_CN":"省份"}
        self.province = province
        # {"en":"city", "zh_CN":"城市"}
        self.city = city
        # {"en":"pod name", "zh_CN":"pod名称"}
        self.pod_name = pod_name
        # {"en":"IP operator list", "zh_CN":"ip运营商列表"}
        self.isps = isps
        # {"en":"is colocation resource or not", "zh_CN":"是否在离线混部资源"}
        self.colocation = colocation

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.display_name, 'display_name')
        self.validate_required(self.private_ips, 'private_ips')
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.cpu_request, 'cpu_request')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.memory_request, 'memory_request')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.area, 'area')
        self.validate_required(self.country, 'country')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.pod_name, 'pod_name')
        self.validate_required(self.isps, 'isps')
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()
        self.validate_required(self.colocation, 'colocation')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.private_ips is not None:
            result['privateIps'] = self.private_ips
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.cpu_request is not None:
            result['cpuRequest'] = self.cpu_request
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.area is not None:
            result['area'] = self.area
        if self.country is not None:
            result['country'] = self.country
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.pod_name is not None:
            result['podName'] = self.pod_name
        if self.isps is not None:
            result['isps'] = []
            for k in self.isps:
                result['isps'].append(k.to_map() if k else None)
        if self.colocation is not None:
            result['colocation'] = self.colocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('privateIps') is not None:
            self.private_ips = m.get('privateIps')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('cpuRequest') is not None:
            self.cpu_request = m.get('cpuRequest')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('podName') is not None:
            self.pod_name = m.get('podName')
        if m.get('isps') is not None:
            self.isps = []
            for k in m.get('isps'):
                temp_model = GetEcciInstanceListIspIp()
                self.isps.append(temp_model.from_map(k))
        if m.get('colocation') is not None:
            self.colocation = m.get('colocation')
        return self


class GetEcciInstanceListInstances(TeaModel):
    def __init__(
        self,
        instances: List[GetEcciInstanceListEcciInstanceSummary] = None,
        total: int = None,
    ):
        # {"en":"ecci instance", "zh_CN":"ecci 实例"}
        self.instances = instances
        # {"en":"total instance", "zh_CN":"实例总数量"}
        self.total = total

    def validate(self):
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = []
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = []
            for k in m.get('instances'):
                temp_model = GetEcciInstanceListEcciInstanceSummary()
                self.instances.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetEcciInstanceListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetEcciInstanceListInstances = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ecci instance list", "zh_CN":"ecci实例列表"}
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
            temp_model = GetEcciInstanceListInstances()
            self.data = temp_model.from_map(m['data'])
        return self


class GetEcciInstanceListPaths(TeaModel):
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


class GetEcciInstanceListParameters(TeaModel):
    def __init__(
        self,
        key: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Keyword: instance name/id/ip", "zh_CN":"关键字: 实例名称/id/ip"}
        self.key = key
        # {"en":"page index", "zh_CN":"页数"}
        self.page_index = page_index
        # {"en":"Number per page", "zh_CN":"每页个数"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetEcciInstanceListRequestHeader(TeaModel):
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


class GetEcciInstanceListResponseHeader(TeaModel):
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






class VMPCreateInstancePivateIpv6Info(TeaModel):
    def __init__(
        self,
        net_no: int = None,
        private_cidr: str = None,
        private_ip: str = None,
    ):
        # {"en":"Inner network number", "zh_CN":"内网编号（1-对应v4的内网1；2-对应v4的内网2）"}
        self.net_no = net_no
        # {"en":"Inner network ipv6 cidr", "zh_CN":"指定内网IPv6 CIDR"}
        self.private_cidr = private_cidr
        # {"en":"Inner network ipv6 address:", "zh_CN":"指定内网IPv6地址"}
        self.private_ip = private_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_no is not None:
            result['netNo'] = self.net_no
        if self.private_cidr is not None:
            result['privateCidr'] = self.private_cidr
        if self.private_ip is not None:
            result['privateIp'] = self.private_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('netNo') is not None:
            self.net_no = m.get('netNo')
        if m.get('privateCidr') is not None:
            self.private_cidr = m.get('privateCidr')
        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')
        return self


class VMPCreateInstanceDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
        category: str = None,
        is_independent: str = None,
    ):
        # {"en":"VMPCreateInstanceDisk size (GB)", "zh_CN":"磁盘大小（GB）"}
        self.size = size
        # {"en":"VMPCreateInstanceDisk Purpose: 
        # System - System disk;
        # DATA - DATA plate", "zh_CN":"磁盘用途：
        # SYSTEM-系统盘；
        # DATA-数据盘"}
        self.type = type
        # {"en":"VMPCreateInstanceDisk type: HDD/SSD", "zh_CN":"磁盘类型：HDD/SSD"}
        self.category = category
        # {"en":"Is isolate: 1(Yes) / -1(No)", "zh_CN":"是否独立盘：1(是) / -1(否)"}
        self.is_independent = is_independent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        if self.category is not None:
            result['category'] = self.category
        if self.is_independent is not None:
            result['isIndependent'] = self.is_independent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('isIndependent') is not None:
            self.is_independent = m.get('isIndependent')
        return self


class VMPCreateInstanceServer(TeaModel):
    def __init__(
        self,
        region_name: str = None,
        province: str = None,
        carrier: str = None,
        node_name: str = None,
        image_id: str = None,
        flavor_id: str = None,
        name: str = None,
        user_data: str = None,
        count: int = None,
        password: str = None,
        key_name: str = None,
        inner_net: str = None,
        cidr: str = None,
        private_ipv_4: str = None,
        inner_net_2: str = None,
        cidr_2: str = None,
        private_ipv_42: str = None,
        private_ipv_6info: List[VMPCreateInstancePivateIpv6Info] = None,
        protocols: int = None,
        ipv_4native_attribute: str = None,
        ipv_6native_attribute: str = None,
        is_free: str = None,
        security_group_ids: List[str] = None,
        disk_info: List[VMPCreateInstanceDisk] = None,
        server_group: str = None,
        tag: str = None,
        use_unique_ip_segment: int = None,
        random_allocate_ip: int = None,
        default_gateway: str = None,
        policy_routing_type: int = None,
        private_gateway_flag: int = None,
        nic_allocate_type: int = None,
        single_public_ipv_4cidr: str = None,
    ):
        # {"en":"Virtual machine area (see Appendix for details)", "zh_CN":"实例所属区域（节点名称nodeName和区域regionName至少需要上传一个。
        #     区域列表详见附录1：https://www.wangsu.com/document/18204/areas-list?rsr=ws）"}
        self.region_name = region_name
        # {"en":"Province of virtual machine (see Appendix for details)", "zh_CN":"实例所属省份（详见附录2：https://www.wangsu.com/document/18204/isp-list?rsr=ws）"}
        self.province = province
        # {"en":"If the operator of the virtual machine (see the appendix for details) carries this parameter, please keep it consistent with the carrier returned from the '3.4 node list query' interface.", "zh_CN":"实例所属运营商（dx-电信；wt-网通；yd-移动）如果携带了该参数，请与'3.4节点列表查询'接口返回的carrier保持一致"}
        self.carrier = carrier
        # {"en":"Node name, indicating that the specified node creates a virtual machine (the node name returned by interface 3.4)", "zh_CN":"节点名称，表示指定节点创建实例（节点名称可通过资源管理-节点列表查询接口获取）"}
        self.node_name = node_name
        # {"en":"Virtual machine image identity", "zh_CN":"实例镜像标识"}
        self.image_id = image_id
        # {"en":"Virtual machine specification ID", "zh_CN":"实例规格标识"}
        self.flavor_id = flavor_id
        # {"en":"Virtual machine name. If the created quantity is greater than 1, the real name is spliced with 3 digits after the parameter. For example, instance 0001, instance 0002", "zh_CN":"实例名称，如果创建数量大于1，则真实名称是在该参数后拼接3位数字。如instance_0001，instance_0002"}
        self.name = name
        # {"en":"Inject user data, support to inject text, text file or gzip file. The maximum length of injected content is 32KB. For content injection, Base64 format encoding is required.", "zh_CN":"注入用户数据，支持注入文本、文本文件或gzip文件。注入内容最大长度32KB。注入内容，需要进行base64格式编码。"}
        self.user_data = user_data
        # {"en":"Number of virtual machines applied", "zh_CN":"申请实例数量"}
        self.count = count
        # {"en":"Virtual machine root login password", "zh_CN":"实例root用户登录密码（如果选择的是公共镜像，则密码password必填）"}
        self.password = password
        # {"en":"The name of the SSH secret key pair for virtual machine login. If this parameter is specified, the password login mode is disabled by default, and the password parameter is invalid at the same time.", "zh_CN":"实例登录SSH秘钥对名称，如果指定该参数，默认禁用密码登录方式，password参数同时失效"}
        self.key_name = key_name
        # {"en":"Whether the virtual machine needs intranet, value:
        # Yes: intranet required
        # No: no intranet is required, default value'", "zh_CN":"实例是否需要内网网络，取值：
        # YES：需要内网
        # NO：不需要内网，默认值"}
        self.inner_net = inner_net
        # {"en":"CIDR of virtual machine intranet is meaningful only when innernet = yes", "zh_CN":"实例内网的cidr，只有innerNet=YES时才有意义"}
        self.cidr = cidr
        # {"en":"If IP address is specified, it must be within the scope of CIDR, otherwise creation fails.", "zh_CN":"实例内网ip地址，如果指定了ip，必须在cidr的范围内，否则创建失败"}
        self.private_ipv_4 = private_ipv_4
        # {"en":"Whether the virtual machine needs intranet2, value:
        # Yes: intranet2 required
        # No: no intranet2 is required, default value'", "zh_CN":"实例是否需要内网2网络，取值：
        # YES：需要内网2
        # NO：不需要内网2，默认值"}
        self.inner_net_2 = inner_net_2
        # {"en":"CIDR of virtual machine intranet2 is meaningful only when innernet = yes", "zh_CN":"实例内网2的cidr，只有innerNet2=YES时才有意义"}
        self.cidr_2 = cidr_2
        # {"en":"If IP address is specified, it must be within the scope of CIDR2, otherwise creation fails.", "zh_CN":"实例内网2ip地址，如果指定了ip，必须在cidr2的范围内，否则创建失败"}
        self.private_ipv_42 = private_ipv_42
        # {"en":"Inner ipv6 info", "zh_CN":"内网IPv6信息"}
        self.private_ipv_6info = private_ipv_6info
        # {"en":"Whether multiple IP protocol addresses are required
        # 
        # 4: only IPv4 address is required, default value
        # 
        # 0: both IPv4 and IPv6 need'", "zh_CN":"是否需要多ip协议地址
        # 4：只需要ipv4地址，默认值
        # 0：ipv4、ipv6都需要"}
        self.protocols = protocols
        # {"en":"IPv4 native attribute, 1: non-native;-1: native;", "zh_CN":"IPv4原生属性，1：非原生；-1：原生；不指定默认随机分配原生属性"}
        self.ipv_4native_attribute = ipv_4native_attribute
        # {"en":"IPv6 native attribute, 1: non-native;-1: native;", "zh_CN":"IPv6原生属性，1：非原生；-1：原生；不指定默认随机分配原生属性"}
        self.ipv_6native_attribute = ipv_6native_attribute
        # {"en":"Whether the instance is free or not, the default billing instance, and the bare machine instance cannot be free, values are as follows:
        # Yes: Free instances
        # No: Billing instance
        # If you are using a free instance, you need to configure permissions in advance", "zh_CN":"是否免费实例，默认计费实例，裸机实例不能免费，取值：
        # YES：免费实例
        # NO：计费实例
        # 如果使用免费实例，需要提前配置权限"}
        self.is_free = is_free
        # {"en":"Specify a security group ID to create multiple security groups separated by commas, up to 5
        # If you are creating a bare machine, you cannot specify a security group", "zh_CN":"指定安全组id进行创建，多个安全组以逗号分隔，最多指定5个
        # 如果是创建裸机，不能指定安全组"}
        self.security_group_ids = security_group_ids
        # {"en":"VMPCreateInstanceDisk information
        # If this information is carried, the disk definition on the template will be ignored and the instance disk will be created with this information, not for bare-metal instance creation", "zh_CN":"磁盘信息
        # 如果携带该信息，将忽略模板上的磁盘定义，以该信息创建实例磁盘，不适用于裸机实例创建"}
        self.disk_info = disk_info
        # {"en":"Anti-affinity group name
        # Virtual machines with the same ServerGroup are created on different hosts", "zh_CN":"反亲和性组名称
        # 拥有相同serverGroup的虚拟机会被创建在不同的宿主机上"}
        self.server_group = server_group
        # {"en":"Instance Tag", "zh_CN":"实例标签"}
        self.tag = tag
        # {"en":"Use  unique ip segment", "zh_CN":"是否使用唯一网段
        # 1：是
        # -1：否"}
        self.use_unique_ip_segment = use_unique_ip_segment
        # {"en":"Allocate IP randomly", "zh_CN":"是否需要随机分配IPv4
        # 1：是
        # -1：否"}
        self.random_allocate_ip = random_allocate_ip
        # {"en":"Default Gateway", "zh_CN":"默认网关运营商如：dx-电信；yd-移动；wt-网通"}
        self.default_gateway = default_gateway
        # {"en":"Policy routing type", "zh_CN":"策略路由类型：0-目的地址策略路由（默认）；1-源地址策略路由；"}
        self.policy_routing_type = policy_routing_type
        # {"en":"Private gateway flag", "zh_CN":"内网网关标识：1-分配内网网关"}
        self.private_gateway_flag = private_gateway_flag
        # {"en":"Nic allocate type", "zh_CN":"实例网卡分配方式：0-多个ip共用一张网卡（默认）；1-每个ip独立一张网卡；2-V4V6混合，同协议IP同网卡，不同线路IP不同网卡"}
        self.nic_allocate_type = nic_allocate_type
        # {"en":"Ipv4 cidr", "zh_CN":"指定外网IPv4网段CIDR(不支持多线)"}
        self.single_public_ipv_4cidr = single_public_ipv_4cidr

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.flavor_id, 'flavor_id')
        if self.private_ipv_6info:
            for k in self.private_ipv_6info:
                if k:
                    k.validate()
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.province is not None:
            result['province'] = self.province
        if self.carrier is not None:
            result['carrier'] = self.carrier
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.flavor_id is not None:
            result['flavorId'] = self.flavor_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.count is not None:
            result['count'] = self.count
        if self.password is not None:
            result['password'] = self.password
        if self.key_name is not None:
            result['keyName'] = self.key_name
        if self.inner_net is not None:
            result['innerNet'] = self.inner_net
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.private_ipv_4 is not None:
            result['privateIPv4'] = self.private_ipv_4
        if self.inner_net_2 is not None:
            result['innerNet2'] = self.inner_net_2
        if self.cidr_2 is not None:
            result['cidr2'] = self.cidr_2
        if self.private_ipv_42 is not None:
            result['privateIPv42'] = self.private_ipv_42
        if self.private_ipv_6info is not None:
            result['privateIpv6Info'] = []
            for k in self.private_ipv_6info:
                result['privateIpv6Info'].append(k.to_map() if k else None)
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.ipv_4native_attribute is not None:
            result['ipv4NativeAttribute'] = self.ipv_4native_attribute
        if self.ipv_6native_attribute is not None:
            result['ipv6NativeAttribute'] = self.ipv_6native_attribute
        if self.is_free is not None:
            result['isFree'] = self.is_free
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.disk_info is not None:
            result['diskInfo'] = []
            for k in self.disk_info:
                result['diskInfo'].append(k.to_map() if k else None)
        if self.server_group is not None:
            result['serverGroup'] = self.server_group
        if self.tag is not None:
            result['tag'] = self.tag
        if self.use_unique_ip_segment is not None:
            result['useUniqueIpSegment'] = self.use_unique_ip_segment
        if self.random_allocate_ip is not None:
            result['randomAllocateIp'] = self.random_allocate_ip
        if self.default_gateway is not None:
            result['defaultGateway'] = self.default_gateway
        if self.policy_routing_type is not None:
            result['policyRoutingType'] = self.policy_routing_type
        if self.private_gateway_flag is not None:
            result['privateGatewayFlag'] = self.private_gateway_flag
        if self.nic_allocate_type is not None:
            result['nicAllocateType'] = self.nic_allocate_type
        if self.single_public_ipv_4cidr is not None:
            result['singlePublicIpv4Cidr'] = self.single_public_ipv_4cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('flavorId') is not None:
            self.flavor_id = m.get('flavorId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('keyName') is not None:
            self.key_name = m.get('keyName')
        if m.get('innerNet') is not None:
            self.inner_net = m.get('innerNet')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('privateIPv4') is not None:
            self.private_ipv_4 = m.get('privateIPv4')
        if m.get('innerNet2') is not None:
            self.inner_net_2 = m.get('innerNet2')
        if m.get('cidr2') is not None:
            self.cidr_2 = m.get('cidr2')
        if m.get('privateIPv42') is not None:
            self.private_ipv_42 = m.get('privateIPv42')
        if m.get('privateIpv6Info') is not None:
            self.private_ipv_6info = []
            for k in m.get('privateIpv6Info'):
                temp_model = VMPCreateInstancePivateIpv6Info()
                self.private_ipv_6info.append(temp_model.from_map(k))
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('ipv4NativeAttribute') is not None:
            self.ipv_4native_attribute = m.get('ipv4NativeAttribute')
        if m.get('ipv6NativeAttribute') is not None:
            self.ipv_6native_attribute = m.get('ipv6NativeAttribute')
        if m.get('isFree') is not None:
            self.is_free = m.get('isFree')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('diskInfo') is not None:
            self.disk_info = []
            for k in m.get('diskInfo'):
                temp_model = VMPCreateInstanceDisk()
                self.disk_info.append(temp_model.from_map(k))
        if m.get('serverGroup') is not None:
            self.server_group = m.get('serverGroup')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('useUniqueIpSegment') is not None:
            self.use_unique_ip_segment = m.get('useUniqueIpSegment')
        if m.get('randomAllocateIp') is not None:
            self.random_allocate_ip = m.get('randomAllocateIp')
        if m.get('defaultGateway') is not None:
            self.default_gateway = m.get('defaultGateway')
        if m.get('policyRoutingType') is not None:
            self.policy_routing_type = m.get('policyRoutingType')
        if m.get('privateGatewayFlag') is not None:
            self.private_gateway_flag = m.get('privateGatewayFlag')
        if m.get('nicAllocateType') is not None:
            self.nic_allocate_type = m.get('nicAllocateType')
        if m.get('singlePublicIpv4Cidr') is not None:
            self.single_public_ipv_4cidr = m.get('singlePublicIpv4Cidr')
        return self


class VMPCreateInstanceRequest(TeaModel):
    def __init__(
        self,
        servers: List[VMPCreateInstanceServer] = None,
    ):
        # {"en":"Creating array objects for virtual machines", "zh_CN":"创建实例的数组对象"}
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
                temp_model = VMPCreateInstanceServer()
                self.servers.append(temp_model.from_map(k))
        return self


class VMPCreateInstanceResponse(TeaModel):
    def __init__(
        self,
        servers: List[str] = None,
    ):
        # {"en":"Virtual machine identity list", "zh_CN":"实例标识列表"}
        self.servers = servers

    def validate(self):
        self.validate_required(self.servers, 'servers')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servers is not None:
            result['servers'] = self.servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        return self


class VMPCreateInstancePaths(TeaModel):
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


class VMPCreateInstanceParameters(TeaModel):
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


class VMPCreateInstanceRequestHeader(TeaModel):
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


class VMPCreateInstanceResponseHeader(TeaModel):
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






class CreateDeploymentContainerEnvRef(TeaModel):
    def __init__(
        self,
        name: str = None,
        field_path: str = None,
    ):
        # {"en":"Environment variable name", "zh_CN":"环境变量名称"}
        self.name = name
        # {"en":"Path to the field to be selected by downwardapi", "zh_CN":"downwardapi要选择的字段的路径"}
        self.field_path = field_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.field_path, 'field_path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.field_path is not None:
            result['fieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')
        return self


class CreateDeploymentVolumeMount(TeaModel):
    def __init__(
        self,
        name: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # {"en":"This must match the Name of a Volume", "zh_CN":"此字段必须与卷的名称匹配"}
        self.name = name
        # {"en":"Path within the container at which the volume should be mounted. Must not contain ':'", "zh_CN":"容器内卷的挂载路径。不得包含 ':'"}
        self.mount_path = mount_path
        # {"en":"Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false", "zh_CN":"如果为 true，则以只读方式挂载，否则（false 或未设置）以读写方式挂载。默认为 false"}
        self.read_only = read_only

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.mount_path, 'mount_path')
        self.validate_required(self.read_only, 'read_only')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class CreateDeploymentContainer(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        memory_limit: str = None,
        name: str = None,
        image: str = None,
        command: List[str] = None,
        args: List[str] = None,
        working_dir: str = None,
        env: Dict[str, str] = None,
        env_ref: List[CreateDeploymentContainerEnvRef] = None,
        volume_mounts: List[CreateDeploymentVolumeMount] = None,
    ):
        # {"en":"CreateDeploymentContainer cpu limit, the sum of all container cpu limits cannot exceed the instance cpu limit", "zh_CN":"容器cpu限制,所有容器cpu限制总和不能超过实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"CreateDeploymentContainer memory limit, the sum of all container memory limits cannot exceed the instance memory limit", "zh_CN":"容器内存限制,所有容器内存限制总和不能超过实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"CreateDeploymentContainer name", "zh_CN":"容器名称"}
        self.name = name
        # {"en":"CreateDeploymentContainer image", "zh_CN":"容器镜像"}
        self.image = image
        # {"en":"Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided.", "zh_CN":"入口点数组。不在 Shell 中执行。如果未提供，则使用容器镜像的 ENTRYPOINT"}
        self.command = command
        # {"en":"Arguments to the entrypoint. The container image's CMD is used if this is not provided", "zh_CN":"entrypoint 的参数。如果未提供，则使用容器镜像的 CMD 设置"}
        self.args = args
        # {"en":"CreateDeploymentContainer's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image", "zh_CN":"容器的工作目录。如果未指定，将使用容器运行时的默认值，默认值可能在容器镜像中配置"}
        self.working_dir = working_dir
        # {"en":"ist of environment variables to set in the container", "zh_CN":"要在容器中设置的环境变量列表"}
        self.env = env
        # {"en":"downwardapi type sensitive environment variables, authorization required", "zh_CN":"downwardapi 类型敏感环境变量,需授权"}
        self.env_ref = env_ref
        # {"en":"Pod volumes to mount into the container's filesystem. Cannot be updated", "zh_CN":"要挂载到容器文件系统中的 Pod 卷。无法更新"}
        self.volume_mounts = volume_mounts

    def validate(self):
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.name, 'name')
        self.validate_required(self.image, 'image')
        if self.env_ref:
            for k in self.env_ref:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.image is not None:
            result['image'] = self.image
        if self.command is not None:
            result['command'] = self.command
        if self.args is not None:
            result['args'] = self.args
        if self.working_dir is not None:
            result['workingDir'] = self.working_dir
        if self.env is not None:
            result['env'] = self.env
        if self.env_ref is not None:
            result['envRef'] = []
            for k in self.env_ref:
                result['envRef'].append(k.to_map() if k else None)
        if self.volume_mounts is not None:
            result['volumeMounts'] = []
            for k in self.volume_mounts:
                result['volumeMounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('workingDir') is not None:
            self.working_dir = m.get('workingDir')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('envRef') is not None:
            self.env_ref = []
            for k in m.get('envRef'):
                temp_model = CreateDeploymentContainerEnvRef()
                self.env_ref.append(temp_model.from_map(k))
        if m.get('volumeMounts') is not None:
            self.volume_mounts = []
            for k in m.get('volumeMounts'):
                temp_model = CreateDeploymentVolumeMount()
                self.volume_mounts.append(temp_model.from_map(k))
        return self


class CreateDeploymentPodVolumeClaim(TeaModel):
    def __init__(
        self,
        claim_name: str = None,
    ):
        # {"en":"the name of a PersistentVolumeClaim in the same namespace as the pod using this volume", "zh_CN":"与使用此卷的 Pod 位于同一名字空间中的 PersistentVolumeClaim 的名称"}
        self.claim_name = claim_name

    def validate(self):
        self.validate_required(self.claim_name, 'claim_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_name is not None:
            result['claimName'] = self.claim_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('claimName') is not None:
            self.claim_name = m.get('claimName')
        return self


class CreateDeploymentHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # {"en":"path of the directory on the host. If the path is a symlink, it will follow the link to the real path", "zh_CN":"目录在主机上的路径。如果该路径是一个符号链接，则它将沿着链接指向真实路径"}
        self.path = path
        # {"en":"type for HostPath Volume Defaults to ''", "zh_CN":"卷的类型。默认为 ''"}
        self.type = type

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDeploymentPodVolume(TeaModel):
    def __init__(
        self,
        name: str = None,
        persistent_volume_claim: CreateDeploymentPodVolumeClaim = None,
        host_path: CreateDeploymentHostPathVolume = None,
    ):
        # {"en":"name of the volume. Must be a DNS_LABEL and unique within the pod.", "zh_CN":"卷的名称。必须是 DNS_LABEL 且在 Pod 内是唯一的。"}
        self.name = name
        # {"en":"represents a reference to a PersistentVolumeClaim in the same namespace", "zh_CN":"表示对同一名字空间中 PersistentVolumeClaim 的引用"}
        self.persistent_volume_claim = persistent_volume_claim
        # {"en":"Represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this.", "zh_CN":"表示主机上预先存在的文件或目录，它们将被直接暴露给容器。 这种卷通常用于系统代理或允许查看主机的其他特权操作。大多数容器不需要这种卷。"}
        self.host_path = host_path

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.persistent_volume_claim, 'persistent_volume_claim')
        if self.persistent_volume_claim:
            self.persistent_volume_claim.validate()
        self.validate_required(self.host_path, 'host_path')
        if self.host_path:
            self.host_path.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.persistent_volume_claim is not None:
            result['persistentVolumeClaim'] = self.persistent_volume_claim.to_map()
        if self.host_path is not None:
            result['hostPath'] = self.host_path.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('persistentVolumeClaim') is not None:
            temp_model = CreateDeploymentPodVolumeClaim()
            self.persistent_volume_claim = temp_model.from_map(m['persistentVolumeClaim'])
        if m.get('hostPath') is not None:
            temp_model = CreateDeploymentHostPathVolume()
            self.host_path = temp_model.from_map(m['hostPath'])
        return self


class CreateDeploymentLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
        operator: str = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.values, 'values')
        self.validate_required(self.operator, 'operator')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        if self.operator is not None:
            result['operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        return self


class CreateDeploymentLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[CreateDeploymentLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        self.validate_required(self.match_labels, 'match_labels')
        self.validate_required(self.match_expressions, 'match_expressions')
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreateDeploymentLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreateDeploymentPodAffinityTerm(TeaModel):
    def __init__(
        self,
        label_selector: CreateDeploymentLabelSelector = None,
        namespaces: List[str] = None,
        topology_key: str = None,
    ):
        # {"en":"A label query over a set of resources, in this case pods.", "zh_CN":"对一组资源的标签查询，在这里资源为 Pod。"}
        self.label_selector = label_selector
        # {"en":"pod's namespace", "zh_CN":" Pod 的名字空间"}
        self.namespaces = namespaces
        # {"en":"This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.", "zh_CN":"此 Pod 应与指定名字空间中与标签选择算符匹配的 Pod 集合位于同一位置（亲和性） 或位于不同位置（反亲和性），这里的“在同一位置”意味着运行在一个节点上，其键名为 topologyKey 的标签值与运行所选 Pod 集合中的某 Pod 的任何节点上的标签值匹配。 不允许使用空的 topologyKey。"}
        self.topology_key = topology_key

    def validate(self):
        self.validate_required(self.label_selector, 'label_selector')
        if self.label_selector:
            self.label_selector.validate()
        self.validate_required(self.namespaces, 'namespaces')
        self.validate_required(self.topology_key, 'topology_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.namespaces is not None:
            result['namespaces'] = self.namespaces
        if self.topology_key is not None:
            result['topologyKey'] = self.topology_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = CreateDeploymentLabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')
        if m.get('topologyKey') is not None:
            self.topology_key = m.get('topologyKey')
        return self


class CreateDeploymentWeightedPodAffinityTerm(TeaModel):
    def __init__(
        self,
        weight: int = None,
        pod_affinity_term: CreateDeploymentPodAffinityTerm = None,
    ):
        # {"en":"associated with matching the corresponding podAffinityTerm, in the range 1-100.", "zh_CN":"匹配相应 podAffinityTerm 条件的权重，范围为 1-100。"}
        self.weight = weight
        # {"en":"Required. A pod affinity term, associated with the corresponding weight.", "zh_CN":"必需的字段。一个 Pod 亲和性条件，对应一个与相应的权重值。"}
        self.pod_affinity_term = pod_affinity_term

    def validate(self):
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.pod_affinity_term, 'pod_affinity_term')
        if self.pod_affinity_term:
            self.pod_affinity_term.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['weight'] = self.weight
        if self.pod_affinity_term is not None:
            result['podAffinityTerm'] = self.pod_affinity_term.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('podAffinityTerm') is not None:
            temp_model = CreateDeploymentPodAffinityTerm()
            self.pod_affinity_term = temp_model.from_map(m['podAffinityTerm'])
        return self


class CreateDeploymentPodAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[CreateDeploymentPodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[CreateDeploymentWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的亲和性要求（例如：由于 Pod 标签更新）， 系统可能会也可能不会尝试最终将 Pod 从其节点中逐出。 当此列表中有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器会更倾向于将 Pod 调度到满足该字段指定的亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。最优选择是权重总和最大的节点， 即对于满足所有调度要求（资源请求、requiredDuringScheduling 亲和表达式等）的每个节点， 通过迭代该字段的元素来计算总和，如果节点具有与相应 podAffinityTerm 匹配的 Pod，则将“权重”添加到总和中； 具有最高总和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = CreateDeploymentPodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = CreateDeploymentWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class CreateDeploymentPodAntiAffinity(TeaModel):
    def __init__(
        self,
        required_during_scheduling_ignored_during_execution: List[CreateDeploymentPodAffinityTerm] = None,
        preferred_during_scheduling_ignored_during_execution: List[CreateDeploymentWeightedPodAffinityTerm] = None,
    ):
        # {"en":"If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", "zh_CN":"如果在调度时不满足该字段指定的反亲和性要求，则该 Pod 不会被调度到该节点上。 如果在 Pod 执行期间的某个时间点不再满足此字段指定的反亲和性要求（例如：由于 Pod 标签更新）， 系统可能会或可能不会尝试最终将 Pod 从其节点中逐出。 当有多个元素时，每个 podAffinityTerm 对应的节点列表是取其交集的，即必须满足所有条件。"}
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        # {"en":"The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", "zh_CN":"调度器更倾向于将 Pod 调度到满足该字段指定的反亲和性表达式的节点， 但它可能会选择违反一个或多个表达式的节点。 最优选的节点是权重总和最大的节点，即对于满足所有调度要求（资源请求、requiredDuringScheduling 反亲和性表达式等）的每个节点，通过遍历元素来计算总和如果节点具有与相应 podAffinityTerm 匹配的 Pod，则此字段并在总和中添加\"权重\"；具有最高加和的节点是最优选的。"}
        self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    def validate(self):
        self.validate_required(self.required_during_scheduling_ignored_during_execution, 'required_during_scheduling_ignored_during_execution')
        if self.required_during_scheduling_ignored_during_execution:
            for k in self.required_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()
        self.validate_required(self.preferred_during_scheduling_ignored_during_execution, 'preferred_during_scheduling_ignored_during_execution')
        if self.preferred_during_scheduling_ignored_during_execution:
            for k in self.preferred_during_scheduling_ignored_during_execution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_during_scheduling_ignored_during_execution is not None:
            result['requiredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.required_during_scheduling_ignored_during_execution:
                result['requiredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        if self.preferred_during_scheduling_ignored_during_execution is not None:
            result['preferredDuringSchedulingIgnoredDuringExecution'] = []
            for k in self.preferred_during_scheduling_ignored_during_execution:
                result['preferredDuringSchedulingIgnoredDuringExecution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredDuringSchedulingIgnoredDuringExecution') is not None:
            self.required_during_scheduling_ignored_during_execution = []
            for k in m.get('requiredDuringSchedulingIgnoredDuringExecution'):
                temp_model = CreateDeploymentPodAffinityTerm()
                self.required_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        if m.get('preferredDuringSchedulingIgnoredDuringExecution') is not None:
            self.preferred_during_scheduling_ignored_during_execution = []
            for k in m.get('preferredDuringSchedulingIgnoredDuringExecution'):
                temp_model = CreateDeploymentWeightedPodAffinityTerm()
                self.preferred_during_scheduling_ignored_during_execution.append(temp_model.from_map(k))
        return self


class CreateDeploymentAffinity(TeaModel):
    def __init__(
        self,
        pod_affinity: CreateDeploymentPodAffinity = None,
        pod_anti_affinity: CreateDeploymentPodAntiAffinity = None,
    ):
        # {"en":"A group of inter pod affinity scheduling rules.", "zh_CN":"一组 Pod 间亲和性调度规则。"}
        self.pod_affinity = pod_affinity
        # {"en":"A group of node affinity scheduling rules.", "zh_CN":"一组节点亲和性调度规则。"}
        self.pod_anti_affinity = pod_anti_affinity

    def validate(self):
        self.validate_required(self.pod_affinity, 'pod_affinity')
        if self.pod_affinity:
            self.pod_affinity.validate()
        self.validate_required(self.pod_anti_affinity, 'pod_anti_affinity')
        if self.pod_anti_affinity:
            self.pod_anti_affinity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_affinity is not None:
            result['podAffinity'] = self.pod_affinity.to_map()
        if self.pod_anti_affinity is not None:
            result['podAntiAffinity'] = self.pod_anti_affinity.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('podAffinity') is not None:
            temp_model = CreateDeploymentPodAffinity()
            self.pod_affinity = temp_model.from_map(m['podAffinity'])
        if m.get('podAntiAffinity') is not None:
            temp_model = CreateDeploymentPodAntiAffinity()
            self.pod_anti_affinity = temp_model.from_map(m['podAntiAffinity'])
        return self


class CreateDeploymentSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"spread field support: group or cluster", "zh_CN":"分组策略,当前支持: group, cluster"}
        self.spread_by_field = spread_by_field
        # {"en":"max groups in field. by default 1", "zh_CN":"策略需要的最大分组个数.默认: 1"}
        self.max_groups = max_groups
        # {"en":"min groups in field. by default 1", "zh_CN":"策略需要的最小分组个数.默认: 1"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class CreateDeploymentClusterFailover(TeaModel):
    def __init__(
        self,
        cluster_failover: int = None,
        toleration_seconds: int = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"the cluser faileover. 0: off, 1: on. default 0", "zh_CN":"集群故障转移开关.0: 关闭,1打开. 默认:0 "}
        self.cluster_failover = cluster_failover
        # {"en":"the tolerationSeconds of the workload unhealthy. default 300", "zh_CN":"应用创建后多久时间没有runing,超过认为不健康.默认300秒"}
        self.toleration_seconds = toleration_seconds
        # {"en":"PurgeMode represents how to deal with the legacy applications on the cluster from which the application is migrated.only support Graciously", "zh_CN":"应用漂移后,旧应用的删除模式.只支持 Graciously 平滑删除"}
        self.purge_mode = purge_mode
        # {"en":"GracePeriodSeconds is the maximum waiting duration in seconds before application on the migrated cluster should be deleted. default:300", "zh_CN":"平滑删除时间. 默认:300秒 "}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        self.validate_required(self.cluster_failover, 'cluster_failover')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_failover is not None:
            result['clusterFailover'] = self.cluster_failover
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterFailover') is not None:
            self.cluster_failover = m.get('clusterFailover')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class CreateDeploymentClusterBehavior(TeaModel):
    def __init__(
        self,
        spread_constraint: List[CreateDeploymentSpreadConstraint] = None,
        cluster_failover: CreateDeploymentClusterFailover = None,
    ):
        # {"en":"a list of the scheduling constraints", "zh_CN":"调度策略列表"}
        self.spread_constraint = spread_constraint
        # {"en":"cluster faileover", "zh_CN":"集群重调度"}
        self.cluster_failover = cluster_failover

    def validate(self):
        if self.spread_constraint:
            for k in self.spread_constraint:
                if k:
                    k.validate()
        if self.cluster_failover:
            self.cluster_failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_constraint is not None:
            result['spreadConstraint'] = []
            for k in self.spread_constraint:
                result['spreadConstraint'].append(k.to_map() if k else None)
        if self.cluster_failover is not None:
            result['clusterFailover'] = self.cluster_failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadConstraint') is not None:
            self.spread_constraint = []
            for k in m.get('spreadConstraint'):
                temp_model = CreateDeploymentSpreadConstraint()
                self.spread_constraint.append(temp_model.from_map(k))
        if m.get('clusterFailover') is not None:
            temp_model = CreateDeploymentClusterFailover()
            self.cluster_failover = temp_model.from_map(m['clusterFailover'])
        return self


class CreateDeploymentPodSpec(TeaModel):
    def __init__(
        self,
        containers: List[CreateDeploymentContainer] = None,
        restart_policy: str = None,
        termination_grace_period_seconds: int = None,
        volumes: List[CreateDeploymentPodVolume] = None,
        affinity: CreateDeploymentAffinity = None,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        kata_runtime: bool = None,
        colocation: bool = None,
        cluster_behavior: CreateDeploymentClusterBehavior = None,
    ):
        # {"en":"List of containers belonging to the pod. There must be at least one container in a Pod. ", "zh_CN":"属于 Pod 的容器列表。Pod 中必须至少有一个容器。"}
        self.containers = containers
        # {"en":"Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always.", "zh_CN":"Pod 内所有容器的重启策略。Always、OnFailure、Never 之一。默认为 Always。"}
        self.restart_policy = restart_policy
        # {"en":"Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.", "zh_CN":"可选字段，表示 Pod 需要体面终止的所需的时长（以秒为单位）。字段值可以在删除请求中减少。 字段值必须是非负整数。零值表示收到 kill 信号则立即停止（没有机会关闭）。 如果此值为 nil，则将使用默认宽限期。 宽限期是从 Pod 中运行的进程收到终止信号后，到进程被 kill 信号强制停止之前，Pod 可以继续存在的时间（以秒为单位）。 应该将此值设置为比你的进程的预期清理时间更长。默认为 30 秒。"}
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # {"en":"List of volumes that can be mounted by containers belonging to the pod.", "zh_CN":"可以由属于 Pod 的容器挂载的卷列表。"}
        self.volumes = volumes
        # {"en":"If specified, the pod's scheduling constraints", "zh_CN":"如果指定了，则作为 Pod 的调度约束。"}
        self.affinity = affinity
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Whether to use kata runtime, Use kata by default", "zh_CN":"是否使用kata运行时,默认使用kata"}
        self.kata_runtime = kata_runtime
        # {"en":"is colocation resource or not", "zh_CN":"是否在离线混部资源"}
        self.colocation = colocation
        # {"en":"the cluster behavior", "zh_CN":"集群策略配置"}
        self.cluster_behavior = cluster_behavior

    def validate(self):
        self.validate_required(self.containers, 'containers')
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        self.validate_required(self.restart_policy, 'restart_policy')
        self.validate_required(self.termination_grace_period_seconds, 'termination_grace_period_seconds')
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()
        self.validate_required(self.affinity, 'affinity')
        if self.affinity:
            self.affinity.validate()
        if self.cluster_behavior:
            self.cluster_behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.containers is not None:
            result['containers'] = []
            for k in self.containers:
                result['containers'].append(k.to_map() if k else None)
        if self.restart_policy is not None:
            result['restartPolicy'] = self.restart_policy
        if self.termination_grace_period_seconds is not None:
            result['terminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.volumes is not None:
            result['volumes'] = []
            for k in self.volumes:
                result['volumes'].append(k.to_map() if k else None)
        if self.affinity is not None:
            result['affinity'] = self.affinity.to_map()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.labels is not None:
            result['labels'] = self.labels
        if self.kata_runtime is not None:
            result['kataRuntime'] = self.kata_runtime
        if self.colocation is not None:
            result['colocation'] = self.colocation
        if self.cluster_behavior is not None:
            result['clusterBehavior'] = self.cluster_behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containers') is not None:
            self.containers = []
            for k in m.get('containers'):
                temp_model = CreateDeploymentContainer()
                self.containers.append(temp_model.from_map(k))
        if m.get('restartPolicy') is not None:
            self.restart_policy = m.get('restartPolicy')
        if m.get('terminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('terminationGracePeriodSeconds')
        if m.get('volumes') is not None:
            self.volumes = []
            for k in m.get('volumes'):
                temp_model = CreateDeploymentPodVolume()
                self.volumes.append(temp_model.from_map(k))
        if m.get('affinity') is not None:
            temp_model = CreateDeploymentAffinity()
            self.affinity = temp_model.from_map(m['affinity'])
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('kataRuntime') is not None:
            self.kata_runtime = m.get('kataRuntime')
        if m.get('colocation') is not None:
            self.colocation = m.get('colocation')
        if m.get('clusterBehavior') is not None:
            temp_model = CreateDeploymentClusterBehavior()
            self.cluster_behavior = temp_model.from_map(m['clusterBehavior'])
        return self


class CreateDeploymentEcciInstanceSpec(TeaModel):
    def __init__(
        self,
        cpu_limit: str = None,
        memory_limit: str = None,
        description: str = None,
        pod_spec: CreateDeploymentPodSpec = None,
        failover: bool = None,
    ):
        # {"en":"Instance cpu limit", "zh_CN":"实例cpu限制"}
        self.cpu_limit = cpu_limit
        # {"en":"Instance memory limit", "zh_CN":"实例内存限制"}
        self.memory_limit = memory_limit
        # {"en":"Instance description", "zh_CN":"实例描述"}
        self.description = description
        # {"en":"Specification of the desired behavior of the pod.", "zh_CN":"Pod 预期行为的规约。"}
        self.pod_spec = pod_spec
        # {"en":"Failover, whether the pod is rescheduled after a node exception, the default is false", "zh_CN":"故障转移,node异常后pod是否重新调度,默认false"}
        self.failover = failover

    def validate(self):
        self.validate_required(self.cpu_limit, 'cpu_limit')
        self.validate_required(self.memory_limit, 'memory_limit')
        self.validate_required(self.pod_spec, 'pod_spec')
        if self.pod_spec:
            self.pod_spec.validate()
        self.validate_required(self.failover, 'failover')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.description is not None:
            result['description'] = self.description
        if self.pod_spec is not None:
            result['podSpec'] = self.pod_spec.to_map()
        if self.failover is not None:
            result['failover'] = self.failover
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('podSpec') is not None:
            temp_model = CreateDeploymentPodSpec()
            self.pod_spec = temp_model.from_map(m['podSpec'])
        if m.get('failover') is not None:
            self.failover = m.get('failover')
        return self


class CreateDeploymentAssignIp(TeaModel):
    def __init__(
        self,
        isp_id: int = None,
        ipv_4: bool = None,
        ipv_6: bool = None,
    ):
        # {"en":"ip operator id", "zh_CN":"ip所属运营商id"}
        self.isp_id = isp_id
        # {"en":"Whether to assign ipv4 ip, ipv4 is assigned by default", "zh_CN":"是否分配ipv4的ip，默认分配ipv4"}
        self.ipv_4 = ipv_4
        # {"en":"Whether to assign ipv6 ip", "zh_CN":"是否分配ipv6的ip"}
        self.ipv_6 = ipv_6

    def validate(self):
        self.validate_required(self.isp_id, 'isp_id')
        self.validate_required(self.ipv_4, 'ipv_4')
        self.validate_required(self.ipv_6, 'ipv_6')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp_id is not None:
            result['ispId'] = self.isp_id
        if self.ipv_4 is not None:
            result['ipv4'] = self.ipv_4
        if self.ipv_6 is not None:
            result['ipv6'] = self.ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ispId') is not None:
            self.isp_id = m.get('ispId')
        if m.get('ipv4') is not None:
            self.ipv_4 = m.get('ipv4')
        if m.get('ipv6') is not None:
            self.ipv_6 = m.get('ipv6')
        return self


class CreateDeploymentInstanceDistribution(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        cluster_selector: Dict[str, str] = None,
        replicas: int = None,
        assign_ips: List[CreateDeploymentAssignIp] = None,
    ):
        # {"en":"distribution cluster name", "zh_CN":"部署集群名称"}
        self.cluster = cluster
        # {"en":"the cluster selector", "zh_CN":"集群标签选择. 这字段和集群名称二选一"}
        self.cluster_selector = cluster_selector
        # {"en":"Number of desired pods", "zh_CN":"预期 Pod 的数量"}
        self.replicas = replicas
        # {"en":"assigned ip attributes", "zh_CN":"分配ip属性"}
        self.assign_ips = assign_ips

    def validate(self):
        self.validate_required(self.replicas, 'replicas')
        self.validate_required(self.assign_ips, 'assign_ips')
        if self.assign_ips:
            for k in self.assign_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.cluster_selector is not None:
            result['clusterSelector'] = self.cluster_selector
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.assign_ips is not None:
            result['assignIps'] = []
            for k in self.assign_ips:
                result['assignIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('clusterSelector') is not None:
            self.cluster_selector = m.get('clusterSelector')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('assignIps') is not None:
            self.assign_ips = []
            for k in m.get('assignIps'):
                temp_model = CreateDeploymentAssignIp()
                self.assign_ips.append(temp_model.from_map(k))
        return self


class CreateDeploymentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        spec: CreateDeploymentEcciInstanceSpec = None,
        distributions: List[CreateDeploymentInstanceDistribution] = None,
        allocate_public_ip: bool = None,
    ):
        # {"en":"ecci instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"specification of the desired behavior of the Ecci.", "zh_CN":"Ecci 预期行为的规约"}
        self.spec = spec
        # {"en":"instance distribution", "zh_CN":"实例分发属性"}
        self.distributions = distributions
        # {"en":"Whether to assign public IP", "zh_CN":"是否分配公网ip"}
        self.allocate_public_ip = allocate_public_ip

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        self.validate_required(self.distributions, 'distributions')
        if self.distributions:
            for k in self.distributions:
                if k:
                    k.validate()
        self.validate_required(self.allocate_public_ip, 'allocate_public_ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.distributions is not None:
            result['distributions'] = []
            for k in self.distributions:
                result['distributions'].append(k.to_map() if k else None)
        if self.allocate_public_ip is not None:
            result['allocatePublicIp'] = self.allocate_public_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            temp_model = CreateDeploymentEcciInstanceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('distributions') is not None:
            self.distributions = []
            for k in m.get('distributions'):
                temp_model = CreateDeploymentInstanceDistribution()
                self.distributions.append(temp_model.from_map(k))
        if m.get('allocatePublicIp') is not None:
            self.allocate_public_ip = m.get('allocatePublicIp')
        return self


class CreateDeploymentInstanceName(TeaModel):
    def __init__(
        self,
        name: str = None,
        display_name: str = None,
    ):
        # {"en":"Instance name", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"Instance display name", "zh_CN":"实例展示名称"}
        self.display_name = display_name

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class CreateDeploymentDeploySummary(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        replicas: int = None,
        created_replicas: int = None,
        ip_allocated_replicas: int = None,
        instance_names: List[CreateDeploymentInstanceName] = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"Number of desired pods", "zh_CN":"预期 Pod 的数量"}
        self.replicas = replicas
        # {"en":"Number of created pods", "zh_CN":"已创建 Pod 的数量"}
        self.created_replicas = created_replicas
        # {"en":"The number of IP addresses assigned to the instance", "zh_CN":"实例分配ip数量"}
        self.ip_allocated_replicas = ip_allocated_replicas
        # {"en":"Instance name list", "zh_CN":"实例名称列表"}
        self.instance_names = instance_names

    def validate(self):
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.replicas, 'replicas')
        self.validate_required(self.created_replicas, 'created_replicas')
        self.validate_required(self.ip_allocated_replicas, 'ip_allocated_replicas')
        self.validate_required(self.instance_names, 'instance_names')
        if self.instance_names:
            for k in self.instance_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.created_replicas is not None:
            result['createdReplicas'] = self.created_replicas
        if self.ip_allocated_replicas is not None:
            result['ipAllocatedReplicas'] = self.ip_allocated_replicas
        if self.instance_names is not None:
            result['instanceNames'] = []
            for k in self.instance_names:
                result['instanceNames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('createdReplicas') is not None:
            self.created_replicas = m.get('createdReplicas')
        if m.get('ipAllocatedReplicas') is not None:
            self.ip_allocated_replicas = m.get('ipAllocatedReplicas')
        if m.get('instanceNames') is not None:
            self.instance_names = []
            for k in m.get('instanceNames'):
                temp_model = CreateDeploymentInstanceName()
                self.instance_names.append(temp_model.from_map(k))
        return self


class CreateDeploymentSummary(TeaModel):
    def __init__(
        self,
        deploy_summaries: List[CreateDeploymentDeploySummary] = None,
    ):
        # {"en":"Instance properties", "zh_CN":"实例属性"}
        self.deploy_summaries = deploy_summaries

    def validate(self):
        self.validate_required(self.deploy_summaries, 'deploy_summaries')
        if self.deploy_summaries:
            for k in self.deploy_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_summaries is not None:
            result['deploySummaries'] = []
            for k in self.deploy_summaries:
                result['deploySummaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploySummaries') is not None:
            self.deploy_summaries = []
            for k in m.get('deploySummaries'):
                temp_model = CreateDeploymentDeploySummary()
                self.deploy_summaries.append(temp_model.from_map(k))
        return self


class CreateDeploymentResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateDeploymentSummary = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ecci object", "zh_CN":"ecci对象"}
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
            temp_model = CreateDeploymentSummary()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateDeploymentPaths(TeaModel):
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


class CreateDeploymentParameters(TeaModel):
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


class CreateDeploymentRequestHeader(TeaModel):
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


class CreateDeploymentResponseHeader(TeaModel):
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






class GetClusterListRequest(TeaModel):
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


class GetClusterListIsp(TeaModel):
    def __init__(
        self,
        isp_id: int = None,
        isp_en: str = None,
        isp_cn: str = None,
    ):
        # {"en":"operator id", "zh_CN":"运营商id"}
        self.isp_id = isp_id
        # {"en":"operator english name", "zh_CN":"运营商英文名"}
        self.isp_en = isp_en
        # {"en":"operator chinese name", "zh_CN":"运营商中文名"}
        self.isp_cn = isp_cn

    def validate(self):
        self.validate_required(self.isp_id, 'isp_id')
        self.validate_required(self.isp_en, 'isp_en')
        self.validate_required(self.isp_cn, 'isp_cn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp_id is not None:
            result['ispId'] = self.isp_id
        if self.isp_en is not None:
            result['ispEn'] = self.isp_en
        if self.isp_cn is not None:
            result['ispCn'] = self.isp_cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ispId') is not None:
            self.isp_id = m.get('ispId')
        if m.get('ispEn') is not None:
            self.isp_en = m.get('ispEn')
        if m.get('ispCn') is not None:
            self.isp_cn = m.get('ispCn')
        return self


class GetClusterListClusterSummary(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
        area: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        isps: List[GetClusterListIsp] = None,
        kata_runtime: bool = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"cluster chinese name", "zh_CN":"集群中文名称"}
        self.name_cn = name_cn
        # {"en":"area", "zh_CN":"区域"}
        self.area = area
        # {"en":"country", "zh_CN":"国家"}
        self.country = country
        # {"en":"province", "zh_CN":"省份"}
        self.province = province
        # {"en":"city", "zh_CN":"城市"}
        self.city = city
        # {"en":"IP operator list", "zh_CN":"ip运营商列表"}
        self.isps = isps
        # {"en":"Whether to support kata runtime", "zh_CN":"是否支持kata运行时"}
        self.kata_runtime = kata_runtime

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.area, 'area')
        self.validate_required(self.country, 'country')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.isps, 'isps')
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()
        self.validate_required(self.kata_runtime, 'kata_runtime')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        if self.area is not None:
            result['area'] = self.area
        if self.country is not None:
            result['country'] = self.country
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.isps is not None:
            result['isps'] = []
            for k in self.isps:
                result['isps'].append(k.to_map() if k else None)
        if self.kata_runtime is not None:
            result['kataRuntime'] = self.kata_runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('isps') is not None:
            self.isps = []
            for k in m.get('isps'):
                temp_model = GetClusterListIsp()
                self.isps.append(temp_model.from_map(k))
        if m.get('kataRuntime') is not None:
            self.kata_runtime = m.get('kataRuntime')
        return self


class GetClusterListClusterList(TeaModel):
    def __init__(
        self,
        clusters: List[GetClusterListClusterSummary] = None,
        total: int = None,
    ):
        # {"en":"cluster list", "zh_CN":"集群列表"}
        self.clusters = clusters
        # {"en":"total clusters", "zh_CN":"集群总数量"}
        self.total = total

    def validate(self):
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = GetClusterListClusterSummary()
                self.clusters.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetClusterListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetClusterListClusterList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"cluster list", "zh_CN":"集群列表"}
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
            temp_model = GetClusterListClusterList()
            self.data = temp_model.from_map(m['data'])
        return self


class GetClusterListPaths(TeaModel):
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


class GetClusterListParameters(TeaModel):
    def __init__(
        self,
        node_ids: List[str] = None,
        isp_ids: List[str] = None,
        page_index: int = None,
        page_size: int = None,
        kata_runtime: str = None,
    ):
        # {"en":"node ids", "zh_CN":"节点ids"}
        self.node_ids = node_ids
        # {"en":"operator ids", "zh_CN":"运营商ids"}
        self.isp_ids = isp_ids
        # {"en":"page index", "zh_CN":"页数"}
        self.page_index = page_index
        # {"en":"page size", "zh_CN":"每页个数"}
        self.page_size = page_size
        # {"en":"0: does not support kataruntime, 1: supports kataruntime, others: all", "zh_CN":"0: 不支持kataruntime, 1: 支持kataruntime, 其他: 全部"}
        self.kata_runtime = kata_runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_ids is not None:
            result['nodeIds'] = self.node_ids
        if self.isp_ids is not None:
            result['ispIds'] = self.isp_ids
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.kata_runtime is not None:
            result['kataRuntime'] = self.kata_runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeIds') is not None:
            self.node_ids = m.get('nodeIds')
        if m.get('ispIds') is not None:
            self.isp_ids = m.get('ispIds')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('kataRuntime') is not None:
            self.kata_runtime = m.get('kataRuntime')
        return self


class GetClusterListRequestHeader(TeaModel):
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


class GetClusterListResponseHeader(TeaModel):
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






class InstanceDiskScalingDiskParam(TeaModel):
    def __init__(
        self,
        size: int = None,
        category: str = None,
    ):
        # {"en":"disk size GB", "zh_CN":"磁盘大小，单位GB"}
        self.size = size
        # {"en":"disk type ,HDD/SDD", "zh_CN":"磁盘类型，取值：
        # HDD：普通硬盘
        # SSD：固态硬盘"}
        self.category = category

    def validate(self):
        self.validate_required(self.size, 'size')
        self.validate_required(self.category, 'category')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['size'] = self.size
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class InstanceDiskScalingRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        disk_info: List[InstanceDiskScalingDiskParam] = None,
    ):
        # {"en":"instance id", "zh_CN":"实例id"}
        self.id = id
        self.disk_info = disk_info

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.disk_info, 'disk_info')
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.disk_info is not None:
            result['diskInfo'] = []
            for k in self.disk_info:
                result['diskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('diskInfo') is not None:
            self.disk_info = []
            for k in m.get('diskInfo'):
                temp_model = InstanceDiskScalingDiskParam()
                self.disk_info.append(temp_model.from_map(k))
        return self


class InstanceDiskScalingDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        type: str = None,
        size: int = None,
    ):
        # {"en":"disk category，HDD/SDD", "zh_CN":"磁盘类型，HDD/SDD"}
        self.category = category
        # {"en":"disk type ,DATA：data disk, SYSTEM：system disk", "zh_CN":"磁盘类型,DATA：数据盘, SYSTEM：系统盘"}
        self.type = type
        # {"en":"disk size GB", "zh_CN":"磁盘大小，单位GB"}
        self.size = size

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.type, 'type')
        self.validate_required(self.size, 'size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.type is not None:
            result['type'] = self.type
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class InstanceDiskScalingServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        disk_info: List[InstanceDiskScalingDisk] = None,
    ):
        # {"en":"server id", "zh_CN":"实例id"}
        self.id = id
        self.disk_info = disk_info

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.disk_info, 'disk_info')
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.disk_info is not None:
            result['diskInfo'] = []
            for k in self.disk_info:
                result['diskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('diskInfo') is not None:
            self.disk_info = []
            for k in m.get('diskInfo'):
                temp_model = InstanceDiskScalingDisk()
                self.disk_info.append(temp_model.from_map(k))
        return self


class InstanceDiskScalingResponse(TeaModel):
    def __init__(
        self,
        server: InstanceDiskScalingServer = None,
    ):
        # {"en":"instance info", "zh_CN":"实例信息"}
        self.server = server

    def validate(self):
        self.validate_required(self.server, 'server')
        if self.server:
            self.server.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server is not None:
            result['server'] = self.server.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('server') is not None:
            temp_model = InstanceDiskScalingServer()
            self.server = temp_model.from_map(m['server'])
        return self


class InstanceDiskScalingPaths(TeaModel):
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


class InstanceDiskScalingParameters(TeaModel):
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


class InstanceDiskScalingRequestHeader(TeaModel):
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


class InstanceDiskScalingResponseHeader(TeaModel):
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






class ApiVmpInstanceBandwidthAggregationQueryDnaRequest(TeaModel):
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


class ApiVmpInstanceBandwidthAggregationQueryDnaResponse(TeaModel):
    def __init__(
        self,
        servers: List[str] = None,
        id: str = None,
        ext_traffic_in: str = None,
        ext_traffic_out: str = None,
    ):
        # {"en":"instances detail info", "zh_CN":"虚拟机详细信息"}
        self.servers = servers
        # {"en":"instance Id", "zh_CN":"实例Id"}
        self.id = id
        # {"en":"External Inbound Traffic Summary (MB)", "zh_CN":"外网流入流量汇总值（MB）"}
        self.ext_traffic_in = ext_traffic_in
        # {"en":"External outbound Traffic Summary (MB)", "zh_CN":"外网流出流量汇总值（MB）"}
        self.ext_traffic_out = ext_traffic_out

    def validate(self):
        self.validate_required(self.servers, 'servers')
        self.validate_required(self.id, 'id')
        self.validate_required(self.ext_traffic_in, 'ext_traffic_in')
        self.validate_required(self.ext_traffic_out, 'ext_traffic_out')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servers is not None:
            result['servers'] = self.servers
        if self.id is not None:
            result['id'] = self.id
        if self.ext_traffic_in is not None:
            result['extTrafficIn'] = self.ext_traffic_in
        if self.ext_traffic_out is not None:
            result['extTrafficOut'] = self.ext_traffic_out
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('extTrafficIn') is not None:
            self.ext_traffic_in = m.get('extTrafficIn')
        if m.get('extTrafficOut') is not None:
            self.ext_traffic_out = m.get('extTrafficOut')
        return self


class ApiVmpInstanceBandwidthAggregationQueryDnaPaths(TeaModel):
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


class ApiVmpInstanceBandwidthAggregationQueryDnaParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Instance ID: A maximum of 20 IDs can be sent at a time, and IDs are separated by a comma character ','.", "zh_CN":"实例ID，单次最多可发送20条ID，ID之间用半角逗号字符“,”隔开。"}
        self.ids = ids
        # {"en":"Start time,format: YYYY-MM-DD. You can only query the flow data within the last 90 days, and the query range cannot exceed 31 days at a time.", "zh_CN":"查询开始时间，格式yyyy-MM-dd。最多只能查询90天内的流量数据，且单次查询时间范围不超过31天。"}
        self.start_time = start_time
        # {"en":"End time: YYYY-MM-DD,and the query range cannot exceed 31 days at a time.", "zh_CN":"查询结束时间，格式yyyy-MM-dd，单次查询时间范围不超过31天。"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.ids, 'ids')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class ApiVmpInstanceBandwidthAggregationQueryDnaRequestHeader(TeaModel):
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


class ApiVmpInstanceBandwidthAggregationQueryDnaResponseHeader(TeaModel):
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






class QueryInstanceListRequest(TeaModel):
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


class QueryInstanceListImage(TeaModel):
    def __init__(
        self,
        os_version: int = None,
    ):
        # {"en":"os version", "zh_CN":"操作系统版本"}
        self.os_version = os_version

    def validate(self):
        self.validate_required(self.os_version, 'os_version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        return self


class QueryInstanceListResource(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
        storage: int = None,
    ):
        # {"en":"cpu", "zh_CN":"cpu核数"}
        self.cpu = cpu
        # {"en":"memory", "zh_CN":"内存"}
        self.memory = memory
        # {"en":"disk storage", "zh_CN":"存储容量"}
        self.storage = storage

    def validate(self):
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.storage, 'storage')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        if self.storage is not None:
            result['storage'] = self.storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        return self


class QueryInstanceListResolution(TeaModel):
    def __init__(
        self,
        width: int = None,
        height: int = None,
    ):
        # {"en":"screen width", "zh_CN":"屏幕宽"}
        self.width = width
        # {"en":"screen height", "zh_CN":"屏幕高"}
        self.height = height

    def validate(self):
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.width is not None:
            result['width'] = self.width
        if self.height is not None:
            result['height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('height') is not None:
            self.height = m.get('height')
        return self


class QueryInstanceListEphone(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        image: QueryInstanceListImage = None,
        resource: QueryInstanceListResource = None,
        resolution: QueryInstanceListResolution = None,
        adb_address: str = None,
        h_5address: str = None,
        state: str = None,
    ):
        # {"en":"id of instance", "zh_CN":"实例id"}
        self.id = id
        # {"en":"name of instance", "zh_CN":"实例名称"}
        self.name = name
        # {"en":"image info", "zh_CN":"镜像信息"}
        self.image = image
        # {"en":"resource of instance", "zh_CN":"实例资源详情"}
        self.resource = resource
        # {"en":"resolution", "zh_CN":"手机分辨率"}
        self.resolution = resolution
        # {"en":"instance adb address", "zh_CN":"实例adb连接地址"}
        self.adb_address = adb_address
        # {"en":"instance h5 address", "zh_CN":"实例h5连接地址"}
        self.h_5address = h_5address
        # {"en":"state of instance", "zh_CN":"实例状态"}
        self.state = state

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.image, 'image')
        if self.image:
            self.image.validate()
        self.validate_required(self.resource, 'resource')
        if self.resource:
            self.resource.validate()
        self.validate_required(self.resolution, 'resolution')
        if self.resolution:
            self.resolution.validate()
        self.validate_required(self.adb_address, 'adb_address')
        self.validate_required(self.h_5address, 'h_5address')
        self.validate_required(self.state, 'state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.image is not None:
            result['image'] = self.image.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.resolution is not None:
            result['resolution'] = self.resolution.to_map()
        if self.adb_address is not None:
            result['adbAddress'] = self.adb_address
        if self.h_5address is not None:
            result['h5Address'] = self.h_5address
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('image') is not None:
            temp_model = QueryInstanceListImage()
            self.image = temp_model.from_map(m['image'])
        if m.get('resource') is not None:
            temp_model = QueryInstanceListResource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('resolution') is not None:
            temp_model = QueryInstanceListResolution()
            self.resolution = temp_model.from_map(m['resolution'])
        if m.get('adbAddress') is not None:
            self.adb_address = m.get('adbAddress')
        if m.get('h5Address') is not None:
            self.h_5address = m.get('h5Address')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class QueryInstanceListResponse(TeaModel):
    def __init__(
        self,
        ephones: List[QueryInstanceListEphone] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"list of ephone instances", "zh_CN":"云手机实例列表"}
        self.ephones = ephones
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = QueryInstanceListEphone()
                self.ephones.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryInstanceListPaths(TeaModel):
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


class QueryInstanceListParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        name: str = None,
    ):
        # {"en":"instance ID to be queried", "zh_CN":"要查询的实例id"}
        self.ids = ids
        # {"en":"instance name bo be queried", "zh_CN":"要查询的实例名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryInstanceListRequestHeader(TeaModel):
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


class QueryInstanceListResponseHeader(TeaModel):
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






class CreateEphoneInstanceSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        cpu: int = None,
        memory: int = None,
    ):
        # {"en":"ephone spec type", "zh_CN":"边缘云手机配置类型，可选值：basic-基础型，standard-通用型，professional-旗舰型"}
        self.type = type
        # {"en":"cpu resource", "zh_CN":"边缘云手机CPU核数"}
        self.cpu = cpu
        # {"en":"memory resource", "zh_CN":"边缘云手机内存大小"}
        self.memory = memory

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        return self


class CreateEphoneInstanceEphone(TeaModel):
    def __init__(
        self,
        spec: CreateEphoneInstanceSpec = None,
        resolution: str = None,
        name: str = None,
        node_name: str = None,
        os_version: str = None,
        oem_image: str = None,
        count: int = None,
    ):
        # {"en":"ephone spec", "zh_CN":"云手机详细配置"}
        self.spec = spec
        # {"en":"ephone resolution", "zh_CN":"云手机分辨率"}
        self.resolution = resolution
        # {"en":"ephone alias name", "zh_CN":"云手机名称"}
        self.name = name
        # {"en":"nodeName", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"osVersion", "zh_CN":"操作系统版本，如Android10，Android11"}
        self.os_version = os_version
        # {"en":"oem image id", "zh_CN":"oem镜像id"}
        self.oem_image = oem_image
        # {"en":"ephone counts", "zh_CN":"申请实例数量"}
        self.count = count

    def validate(self):
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.name is not None:
            result['name'] = self.name
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.oem_image is not None:
            result['oemImage'] = self.oem_image
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spec') is not None:
            temp_model = CreateEphoneInstanceSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('oemImage') is not None:
            self.oem_image = m.get('oemImage')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class CreateEphoneInstanceRequest(TeaModel):
    def __init__(
        self,
        ephones: List[CreateEphoneInstanceEphone] = None,
    ):
        # {"en":"list of ephones", "zh_CN":"云手机请求列表"}
        self.ephones = ephones

    def validate(self):
        self.validate_required(self.ephones, 'ephones')
        if self.ephones:
            for k in self.ephones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ephones is not None:
            result['ephones'] = []
            for k in self.ephones:
                result['ephones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ephones') is not None:
            self.ephones = []
            for k in m.get('ephones'):
                temp_model = CreateEphoneInstanceEphone()
                self.ephones.append(temp_model.from_map(k))
        return self


class CreateEphoneInstanceTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        message: str = None,
    ):
        # {"en":"task id", "zh_CN":"任务单id"}
        self.id = id
        # {"en":"message", "zh_CN":"任务单消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateEphoneInstanceResponse(TeaModel):
    def __init__(
        self,
        tasks: List[CreateEphoneInstanceTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['tasks'] = []
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = []
            for k in m.get('tasks'):
                temp_model = CreateEphoneInstanceTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateEphoneInstancePaths(TeaModel):
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


class CreateEphoneInstanceParameters(TeaModel):
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


class CreateEphoneInstanceRequestHeader(TeaModel):
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


class CreateEphoneInstanceResponseHeader(TeaModel):
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






class EditInstanceServer(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # {"en":"EditInstanceServer id", "zh_CN":"要更新的实例id"}
        self.id = id
        # {"en":"New instance name
        # Constraints:
        # 1. Length of 2-128 characters
        # 2. Must start with a letter, and can only contain letters, numbers, underlines, lines, and dots", "zh_CN":"新的实例名称
        # 约束：
        # 1. 长度2-128个字符
        # 2. 必须以字母开头，且只能包含字母、数字、下划线、横线、点号"}
        self.name = name

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class EditInstanceRequest(TeaModel):
    def __init__(
        self,
        server: List[EditInstanceServer] = None,
    ):
        # {"en":"server", "zh_CN":"实例信息对象"}
        self.server = server

    def validate(self):
        self.validate_required(self.server, 'server')
        if self.server:
            for k in self.server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server is not None:
            result['server'] = []
            for k in self.server:
                result['server'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('server') is not None:
            self.server = []
            for k in m.get('server'):
                temp_model = EditInstanceServer()
                self.server.append(temp_model.from_map(k))
        return self


class EditInstanceResponse(TeaModel):
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


class EditInstancePaths(TeaModel):
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


class EditInstanceParameters(TeaModel):
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


class EditInstanceRequestHeader(TeaModel):
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


class EditInstanceResponseHeader(TeaModel):
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




