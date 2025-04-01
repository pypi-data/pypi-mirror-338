# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AddRecordRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        dc_name: str = None,
        dc_type: str = None,
        dc_view: str = None,
        dc_value: str = None,
        mx_pri: int = None,
        ttl: int = None,
        language: str = None,
    ):
        # {"en":"The domain whose
        # DNS records to be
        # added", "zh_CN":"需要添加解析记录的域名"}
        self.domain_name = domain_name
        # {"en":"Host name records", "zh_CN":"主机记录
        # CloudDNS支持的记录类型：A、AAAA、CNAME、TXT、SRV和MX"}
        self.dc_name = dc_name
        # {"en":"Record type.
        # 
        # Record types supported by CloudDNS: A, AAAA, CNAME, TXT, SRV, MX", "zh_CN":"记录类型
        # CloudDNS支持的记录类型：A、AAAA、CNAME、TXT、SRV、MX"}
        self.dc_type = dc_type
        # {"en":"Line
        # Please refer to the
        # Appendix for pair
        # details of lines", "zh_CN":"线路，线路代码对应表请参考附录"}
        self.dc_view = dc_view
        # {"en":"Record value
        # (Special formats of
        # SRV type: priority,
        # space, weight, port
        # number, space, target
        # address)", "zh_CN":"记录值(SRV类型特殊格式：优先级、空格、权重、空格、端口号、空格、目标地址）"}
        self.dc_value = dc_value
        # {"en":"MX priority
        # This parameter is
        # required if 'MX' is
        # selected for 'Record
        # type'.
        # Value range is 1-50;
        # the default value is 5.
        # The smaller a number
        # is, the higher priority it
        # has.", "zh_CN":"MX优先级：
        # 如果“记录类型”选择“MX”，则需配置该参数
        # 取值范围为1~50，默认为5。数值越小，则优先级越高"}
        self.mx_pri = mx_pri
        # {"en":"The survival time for
        # cache. The default", "zh_CN":"指缓存的生存时间。默认可配置为600s。"}
        self.ttl = ttl
        # {"en":"Return Chinese results for null (default)
        # En: Return the English prompt result", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.dc_name, 'dc_name')
        self.validate_required(self.dc_type, 'dc_type')
        self.validate_required(self.dc_view, 'dc_view')
        self.validate_required(self.dc_value, 'dc_value')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.dc_name is not None:
            result['dcName'] = self.dc_name
        if self.dc_type is not None:
            result['dcType'] = self.dc_type
        if self.dc_view is not None:
            result['dcView'] = self.dc_view
        if self.dc_value is not None:
            result['dcValue'] = self.dc_value
        if self.mx_pri is not None:
            result['mxPri'] = self.mx_pri
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('dcName') is not None:
            self.dc_name = m.get('dcName')
        if m.get('dcType') is not None:
            self.dc_type = m.get('dcType')
        if m.get('dcView') is not None:
            self.dc_view = m.get('dcView')
        if m.get('dcValue') is not None:
            self.dc_value = m.get('dcValue')
        if m.get('mxPri') is not None:
            self.mx_pri = m.get('mxPri')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class AddRecordResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        record_id: List[str] = None,
    ):
        # {"en":"Status code. For detailed description of resCode, please refer to 'Status Codes of Dispatch Business'.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"recordId, ID of host name record, used to identify this record.", "zh_CN":"主机记录的ID，用于标识该记录。"}
        self.record_id = record_id

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.record_id is not None:
            result['recordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        return self


class AddRecordPaths(TeaModel):
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


class AddRecordParameters(TeaModel):
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


class AddRecordRequestHeader(TeaModel):
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


class AddRecordResponseHeader(TeaModel):
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






class QueryRecordsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        param: str = None,
        dc_name: str = None,
        dc_type: str = None,
        dc_view: str = None,
        dc_view_id: str = None,
        dc_value: str = None,
        state: int = None,
        language: str = None,
    ):
        # {"en":"The domain whose DNS records to be viewed", "zh_CN":"需要查询解析记录的域名"}
        self.domain_name = domain_name
        # {"en":"Fuzzy query(no need to enter this parameter if accurate query is used). Used this parameter to fuzzy query 'Host name records', 'Record type', 'Record value'.", "zh_CN":"模糊查询 (如果需要精确查询，则这个参数不填)。根据此查询参数对“主机记录”，“记录类型”，“记录值”进行模糊查询"}
        self.param = param
        # {"en":"Host name records(accurate query)", "zh_CN":"主机记录 （精确查询）"}
        self.dc_name = dc_name
        # {"en":"Record type(accurate query) CloudDNS supports the following record types: A, AAAA, CNAME and MX", "zh_CN":"记录类型（精确查询）
        # CloudDNS支持的记录类型：A、AAAA、CNAME、TXT和MX"}
        self.dc_type = dc_type
        # {"en":"Chinese name of the line(accurate query), for example: China Telecom", "zh_CN":"线路中文名称（精确查询）例如：中国电信"}
        self.dc_view = dc_view
        # {"en":"Line ID (accurate query)", "zh_CN":"线路ID(精确查询)"}
        self.dc_view_id = dc_view_id
        # {"en":"Record value(accurate query)", "zh_CN":"记录值（精确查询）"}
        self.dc_value = dc_value
        # {"en":"Status of DNS record. (Accurate query)Normal: 2; Suspend:1; All:0", "zh_CN":"解析记录状态。（精确查询）正常：2 停用：1 全部：0"}
        self.state = state
        # {"en":"Status of DNS record. (Accurate query)Normal: 2; Suspend:1; All:0", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.param is not None:
            result['param'] = self.param
        if self.dc_name is not None:
            result['dcName'] = self.dc_name
        if self.dc_type is not None:
            result['dcType'] = self.dc_type
        if self.dc_view is not None:
            result['dcView'] = self.dc_view
        if self.dc_view_id is not None:
            result['dcViewId'] = self.dc_view_id
        if self.dc_value is not None:
            result['dcValue'] = self.dc_value
        if self.state is not None:
            result['state'] = self.state
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('dcName') is not None:
            self.dc_name = m.get('dcName')
        if m.get('dcType') is not None:
            self.dc_type = m.get('dcType')
        if m.get('dcView') is not None:
            self.dc_view = m.get('dcView')
        if m.get('dcViewId') is not None:
            self.dc_view_id = m.get('dcViewId')
        if m.get('dcValue') is not None:
            self.dc_value = m.get('dcValue')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class QueryRecordsResponseContent(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        dc_name: str = None,
        dc_type: str = None,
        dc_view: int = None,
        dc_value: str = None,
        state: int = None,
        mx_pri: int = None,
        ttl: int = None,
        auth: int = None,
    ):
        # {"en":"ID of host name record", "zh_CN":"主机记录ID"}
        self.record_id = record_id
        # {"en":"Host name records", "zh_CN":"主机记录"}
        self.dc_name = dc_name
        # {"en":"Record type
        # CloudDNS supports the
        # following record types: A,
        # AAAA, CNAME and MX", "zh_CN":"记录类型
        # CloudDNS支持的记录类型：A、AAAA、CNAME、TXT和MX"}
        self.dc_type = dc_type
        # {"en":"Line  Please refer to the Appendix
        # for pair details of lines", "zh_CN":"线路，线路代码对应表请参考附录"}
        self.dc_view = dc_view
        # {"en":"Record value", "zh_CN":"记录值"}
        self.dc_value = dc_value
        # {"en":"Status of DNS record. Normal:
        # 2; Suspend:1", "zh_CN":"解析记录状态。正常：2 停用：1"}
        self.state = state
        # {"en":"MX priority
        # This parameter is required if
        # 'MX' is selected for 'Record
        # type'.
        # Value range is 1-50; the
        # default value is 5. The smaller
        # a number is, the higher priority
        # it has.", "zh_CN":"MX优先级，注意点：
        # 1.如果“记录类型”选择“MX”，则需配置该参数
        # 2.取值范围为1~50，默认为5。数值越小，则优先级越高"}
        self.mx_pri = mx_pri
        # {"en":"The survival time for cache.
        # The default configured value is
        # 600s.", "zh_CN":"指缓存的生存时间。默认可配置为600s。"}
        self.ttl = ttl
        # {"en":"Operation permissions: 1, read-only 2, read and write", "zh_CN":"操作权限：1、只读 2、读写"}
        self.auth = auth

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.dc_name, 'dc_name')
        self.validate_required(self.dc_type, 'dc_type')
        self.validate_required(self.dc_view, 'dc_view')
        self.validate_required(self.dc_value, 'dc_value')
        self.validate_required(self.state, 'state')
        self.validate_required(self.mx_pri, 'mx_pri')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.auth, 'auth')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.dc_name is not None:
            result['dcName'] = self.dc_name
        if self.dc_type is not None:
            result['dcType'] = self.dc_type
        if self.dc_view is not None:
            result['dcView'] = self.dc_view
        if self.dc_value is not None:
            result['dcValue'] = self.dc_value
        if self.state is not None:
            result['state'] = self.state
        if self.mx_pri is not None:
            result['mxPri'] = self.mx_pri
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.auth is not None:
            result['auth'] = self.auth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('dcName') is not None:
            self.dc_name = m.get('dcName')
        if m.get('dcType') is not None:
            self.dc_type = m.get('dcType')
        if m.get('dcView') is not None:
            self.dc_view = m.get('dcView')
        if m.get('dcValue') is not None:
            self.dc_value = m.get('dcValue')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('mxPri') is not None:
            self.mx_pri = m.get('mxPri')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('auth') is not None:
            self.auth = m.get('auth')
        return self


class QueryRecordsResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: List[QueryRecordsResponseContent] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"Detailed description of the
        # status code.", "zh_CN":"状态码详细说明"}
        self.msg = msg
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
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
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = QueryRecordsResponseContent()
                self.content.append(temp_model.from_map(k))
        return self


class QueryRecordsPaths(TeaModel):
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


class QueryRecordsParameters(TeaModel):
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


class QueryRecordsRequestHeader(TeaModel):
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


class QueryRecordsResponseHeader(TeaModel):
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






class ControlRecordRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        record_ids: str = None,
        operate: int = None,
        language: str = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain_name = domain_name
        # {"en":"ID of host name
        # record, use ; to
        # separate two", "zh_CN":"主机记录ID,多个用英文;分隔"}
        self.record_ids = record_ids
        # {"en":"Operation: 1 Disable; 2
        # Enable", "zh_CN":"操作：1停用；2启用"}
        self.operate = operate
        # {"en":"Operation: 1 Disable; 2
        # Enable", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.record_ids, 'record_ids')
        self.validate_required(self.operate, 'operate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.record_ids is not None:
            result['recordIds'] = self.record_ids
        if self.operate is not None:
            result['operate'] = self.operate
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('recordIds') is not None:
            self.record_ids = m.get('recordIds')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ControlRecordResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"Detailed description of the
        # status code.", "zh_CN":"状态码详细说明"}
        self.msg = msg
        # {"en":"recordId, ID of host name
        # record
        # code msg of status code,
        # detailed description of the
        # status code.", "zh_CN":"recordId 主机记录ID
        # code 状态码
        # msg 状态码详细说明"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ControlRecordPaths(TeaModel):
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


class ControlRecordParameters(TeaModel):
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


class ControlRecordRequestHeader(TeaModel):
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


class ControlRecordResponseHeader(TeaModel):
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






class ConfigShareOperRequest(TeaModel):
    def __init__(
        self,
        operate: int = None,
        config_share: List[str] = None,
    ):
        # {"en":"operate: 1-add", "zh_CN":"操作：1 新增"}
        self.operate = operate
        # {"en":"share object", "zh_CN":"授权对象"}
        self.config_share = config_share

    def validate(self):
        self.validate_required(self.operate, 'operate')
        self.validate_required(self.config_share, 'config_share')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate is not None:
            result['operate'] = self.operate
        if self.config_share is not None:
            result['configShare'] = self.config_share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('configShare') is not None:
            self.config_share = m.get('configShare')
        return self


class ConfigShareOperResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"detail", "zh_CN":"详情"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ConfigShareOperPaths(TeaModel):
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


class ConfigShareOperParameters(TeaModel):
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


class ConfigShareOperRequestHeader(TeaModel):
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


class ConfigShareOperResponseHeader(TeaModel):
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






class ModifyRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        domain_name: str = None,
        dc_name: str = None,
        dc_type: str = None,
        dc_view: int = None,
        dc_value: str = None,
        mx_pri: int = None,
        ttl: int = None,
        language: str = None,
    ):
        # {"en":"ID of host name record", "zh_CN":"主机记录ID"}
        self.record_id = record_id
        # {"en":"The domain whose DNS records to be added", "zh_CN":"需要添加解析记录的域名"}
        self.domain_name = domain_name
        # {"en":"Host name records", "zh_CN":"主机记录"}
        self.dc_name = dc_name
        # {"en":"Record type CloudDNS supports the following record types: A, AAAA, CNAME, TXT, SRV and MX", "zh_CN":"主机记录
        # CloudDNS支持的记录类型：A、AAAA、CNAME、TXT、SRV和MX"}
        self.dc_type = dc_type
        # {"en":"Line Please refer to the Appendix for pair details of lines", "zh_CN":"线路，线路代码对应表请参考附录"}
        self.dc_view = dc_view
        # {"en":"Record value (Special formats of SRV type: priority, space, weight, port number, space, target address)", "zh_CN":"记录值(SRV类型特殊格式：优先级、空格、权重、空格、端口号、空格、目标地址）"}
        self.dc_value = dc_value
        # {"en":"MX priority This parameter is required if 'MX' is selected for 'Record type'. Value range is 1-50; the default value is 5. The smaller a number is, the higher priority it has.", "zh_CN":"MX优先级：
        # 如果“记录类型”选择“MX”，则需配置该参数
        # 取值范围为1~50，默认为5。数值越小，则优先级越高"}
        self.mx_pri = mx_pri
        # {"en":"The survival time for cache. The default configured value is 600s.", "zh_CN":"指缓存的生存时间。默认可配置为600s。"}
        self.ttl = ttl
        # {"en":"The survival time for cache. The default configured value is 600s.", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.dc_name, 'dc_name')
        self.validate_required(self.dc_type, 'dc_type')
        self.validate_required(self.dc_view, 'dc_view')
        self.validate_required(self.dc_value, 'dc_value')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.dc_name is not None:
            result['dcName'] = self.dc_name
        if self.dc_type is not None:
            result['dcType'] = self.dc_type
        if self.dc_view is not None:
            result['dcView'] = self.dc_view
        if self.dc_value is not None:
            result['dcValue'] = self.dc_value
        if self.mx_pri is not None:
            result['mxPri'] = self.mx_pri
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('dcName') is not None:
            self.dc_name = m.get('dcName')
        if m.get('dcType') is not None:
            self.dc_type = m.get('dcType')
        if m.get('dcView') is not None:
            self.dc_view = m.get('dcView')
        if m.get('dcValue') is not None:
            self.dc_value = m.get('dcValue')
        if m.get('mxPri') is not None:
            self.mx_pri = m.get('mxPri')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ModifyRecordResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: dict = None,
    ):
        # {"en":"Status code. For detailed description of resCode, please refer to "Status Codes of Dispatch Business".", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"recordId, ID of host name record, used to identify this record.", "zh_CN":"recordId 主机记录的ID，用于标识该记录。"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ModifyRecordPaths(TeaModel):
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


class ModifyRecordParameters(TeaModel):
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


class ModifyRecordRequestHeader(TeaModel):
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


class ModifyRecordResponseHeader(TeaModel):
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






class DelRecordRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
        language: str = None,
    ):
        # {"en":"ID of host name record", "zh_CN":"主机记录ID"}
        self.record_id = record_id
        # {"en":"ID of host name record", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class DelRecordResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
    ):
        # {"en":"Status code. For detailed
        # description of resCode, please
        # refer to 'Status Codes of
        # Dispatch Business'.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the
        # status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DelRecordPaths(TeaModel):
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


class DelRecordParameters(TeaModel):
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


class DelRecordRequestHeader(TeaModel):
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


class DelRecordResponseHeader(TeaModel):
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




