# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class BatchDeleteAPIDefinitionRequest(TeaModel):
    def __init__(
        self,
        id_list: List[str] = None,
    ):
        # {'en':'API definition ID array.', 'zh_CN':'API定义ID数组。'}
        self.id_list = id_list

    def validate(self):
        self.validate_required(self.id_list, 'id_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_list is not None:
            result['idList'] = self.id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idList') is not None:
            self.id_list = m.get('idList')
        return self


class BatchDeleteAPIDefinitionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: bool = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class BatchDeleteAPIDefinitionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BatchDeleteAPIDefinitionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BatchDeleteAPIDefinitionRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class BatchDeleteAPIDefinitionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryAPIDefinitionDetailRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {'en':'API definition ID.', 'zh_CN':'API定义ID。'}
        self.id = id

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class QueryAPIDefinitionDetailApiDefineBasicVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        group_name: str = None,
        remark: str = None,
        domain: str = None,
        path: str = None,
        create_time: str = None,
        update_time: str = None,
    ):
        # {'en':'API definition ID.', 'zh_CN':'API定义ID。'}
        self.id = id
        # {'en':'API name.', 'zh_CN':'API名称。'}
        self.name = name
        # {'en':'API groups.', 'zh_CN':'API分组。'}
        self.group_name = group_name
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark
        # {'en':'Attributed hostname.', 'zh_CN':'归属域名。'}
        self.domain = domain
        # {'en':'API base path.', 'zh_CN':'端点路径。'}
        self.path = path
        # {'en':'Creation time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'创建时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.create_time = create_time
        # {'en':'Update time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'更新时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.path, 'path')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.domain is not None:
            result['domain'] = self.domain
        if self.path is not None:
            result['path'] = self.path
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class QueryAPIDefinitionDetailApiDefineEndpointVO(TeaModel):
    def __init__(
        self,
        request_method: str = None,
        type: str = None,
        match_type: str = None,
        path: str = None,
        case_sensitive: str = None,
        match_path_var: str = None,
    ):
        # {'en':'Request methods.
        # GET:GET, configurable parameter limits
        # POST:POST, configurable parameter limits
        # DELETE:DELETE, configurable parameter limits
        # UPDATE:UPDATE
        # PUT:PUT, configurable parameter limits
        # HEAD:HEAD, configurable parameter limits
        # CONNECT:CONNECT
        # OPTIONS:OPTIONS, configurable parameter limits
        # COPY:COPY
        # LOCK:LOCK
        # UNLOCK:UNLOCK
        # TRACE:TRACE
        # PATCH:PATCH, configurable parameter limits
        # PROPFIND:PROPFIND
        # MKCOL:MKCOL
        # MOVE:MOVE', 'zh_CN':'请求方法。
        # GET：GET，可配置参数限制
        # POST：POST，可配置参数限制
        # DELETE：DELETE，可配置参数限制
        # UPDATE：UPDATE
        # PUT：PUT，可配置参数限制
        # HEAD：HEAD，可配置参数限制
        # CONNECT：CONNECT
        # OPTIONS：OPTIONS，可配置参数限制
        # COPY：COPY
        # LOCK：LOCK
        # UNLOCK：UNLOCK
        # TRACE：TRACE
        # PATCH：PATCH，可配置参数限制
        # PROPFIND：PROPFIND
        # MKCOL：MKCOL
        # MOVE：MOVE'}
        self.request_method = request_method
        # {'en':'API type.
        # NORMAL:Common API
        # WHEN_CASE:Common API', 'zh_CN':'API类型。
        # NORMAL：普通接口
        # WHEN_CASE：when-case接口'}
        self.type = type
        # {'en':'Path matching type.
        # EQUAL: Complete match
        # REGEX: Regular matching', 'zh_CN':'路径匹配类型。
        # EQUAL：完整匹配
        # REGEX：正则匹配'}
        self.match_type = match_type
        # {'en':'API base path.', 'zh_CN':'端点路径。'}
        self.path = path
        # {'en':'Case sensitive.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'大小写是否敏感。
        # TRUE：是
        # FALSE：否'}
        self.case_sensitive = case_sensitive
        # {'en':'Match QueryAPIDefinitionDetailParameters in the Path.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'匹配路径参数。
        # TRUE：是
        # FALSE：否'}
        self.match_path_var = match_path_var

    def validate(self):
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.type, 'type')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.path, 'path')
        self.validate_required(self.case_sensitive, 'case_sensitive')
        self.validate_required(self.match_path_var, 'match_path_var')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.type is not None:
            result['type'] = self.type
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.path is not None:
            result['path'] = self.path
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.match_path_var is not None:
            result['matchPathVar'] = self.match_path_var
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('matchPathVar') is not None:
            self.match_path_var = m.get('matchPathVar')
        return self


class QueryAPIDefinitionDetailApiDefineAuthVO(TeaModel):
    def __init__(
        self,
        type: str = None,
        auth_key: str = None,
        param_position: str = None,
        param_name: str = None,
        validity_time: int = None,
    ):
        # {'en':'Authentication method.
        # NO_NEED:No authentication required
        # SIGN:Key authentication', 'zh_CN':'鉴权方法。
        # NO_NEED：免鉴权
        # SIGN：秘钥对鉴权'}
        self.type = type
        # {'en':'Authentication key.', 'zh_CN':'鉴权秘钥。'}
        self.auth_key = auth_key
        # {'en':'Authentication parameter location.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie', 'zh_CN':'鉴权参数位置。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie'}
        self.param_position = param_position
        # {'en':'Authentication parameter name.', 'zh_CN':'鉴权参数名称。'}
        self.param_name = param_name
        # {'en':'Authentication token validity period, in seconds.', 'zh_CN':'鉴权有效期，单位秒。'}
        self.validity_time = validity_time

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.auth_key, 'auth_key')
        self.validate_required(self.param_position, 'param_position')
        self.validate_required(self.param_name, 'param_name')
        self.validate_required(self.validity_time, 'validity_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.auth_key is not None:
            result['authKey'] = self.auth_key
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.validity_time is not None:
            result['validityTime'] = self.validity_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('authKey') is not None:
            self.auth_key = m.get('authKey')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('validityTime') is not None:
            self.validity_time = m.get('validityTime')
        return self


class QueryAPIDefinitionDetailApiDefineBodyLimitVO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        content_type: str = None,
        body_limit_max: int = None,
        nest_max: int = None,
        param_count_max: int = None,
    ):
        # {'en':'Request body restriction switch.
        # ON:ON
        # OFF:OFF', 'zh_CN':'请求body限制开关。
        # ON：开启
        # OFF：关闭'}
        self.defend_switch = defend_switch
        # {'en':'Content-Type.
        # FORM:FORM
        # JSON:JSON
        # ANY:ANY
        # EMPTY:EMPTY or NON-EXISTENT', 'zh_CN':'Content-Type。
        # FORM：FORM表单
        # JSON：JSON
        # ANY：任意
        # EMPTY：为空或不存在'}
        self.content_type = content_type
        # {'en':'Maximum body limit(bytes).', 'zh_CN':'Body最大限制(bytes)。'}
        self.body_limit_max = body_limit_max
        # {'en':'Maximum nesting depth.', 'zh_CN':'最大嵌套层数。'}
        self.nest_max = nest_max
        # {'en':'Maximum number of parameters for JSON.', 'zh_CN':'JSON最大参数个数。'}
        self.param_count_max = param_count_max

    def validate(self):
        self.validate_required(self.defend_switch, 'defend_switch')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.body_limit_max, 'body_limit_max')
        self.validate_required(self.nest_max, 'nest_max')
        self.validate_required(self.param_count_max, 'param_count_max')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.body_limit_max is not None:
            result['bodyLimitMax'] = self.body_limit_max
        if self.nest_max is not None:
            result['nestMax'] = self.nest_max
        if self.param_count_max is not None:
            result['paramCountMax'] = self.param_count_max
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('bodyLimitMax') is not None:
            self.body_limit_max = m.get('bodyLimitMax')
        if m.get('nestMax') is not None:
            self.nest_max = m.get('nestMax')
        if m.get('paramCountMax') is not None:
            self.param_count_max = m.get('paramCountMax')
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitBasicVO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        param_check_mode: str = None,
    ):
        # {'en':'Parameter limit.
        # ON:ON
        # OFF:OFF', 'zh_CN':'参数限制。
        # ON：ON
        # OFF：OFF'}
        self.defend_switch = defend_switch
        # {'en':'Query String Parameter Detection Mode.
        # LOOSE:Loose mode - detect some parameters
        # STRICT:Strict mode - checks all parameters', 'zh_CN':'Query String参数检测模式。
        # LOOSE：宽松模式-检测部分参数
        # STRICT：严格模式-检测所有参数'}
        self.param_check_mode = param_check_mode

    def validate(self):
        self.validate_required(self.defend_switch, 'defend_switch')
        self.validate_required(self.param_check_mode, 'param_check_mode')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.param_check_mode is not None:
            result['paramCheckMode'] = self.param_check_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('paramCheckMode') is not None:
            self.param_check_mode = m.get('paramCheckMode')
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitNormalVO(TeaModel):
    def __init__(
        self,
        method: str = None,
        name: str = None,
        param_position: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Request methods.
        # GET:GET
        # POST:POST
        # DELETE:DELETE
        # PUT:PUT
        # HEAD:HEAD
        # OPTIONS:OPTIONS
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # GET：GET
        # POST：POST
        # DELETE：DELETE
        # PUT：PUT
        # HEAD：HEAD
        # OPTIONS：OPTIONS
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Parameter name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter position.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie
        # PATH_PARAMS:Path', 'zh_CN':'参数变量。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie
        # PATH_PARAMS：路径变量'}
        self.param_position = param_position
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'Minimum value/Minimum length.', 'zh_CN':'最小值、最小长度。'}
        self.min_val = min_val
        # {'en':'Maximum value/Maximum length.', 'zh_CN':'最大值、最大长度。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content.', 'zh_CN':'内容。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.method, 'method')
        self.validate_required(self.name, 'name')
        self.validate_required(self.param_position, 'param_position')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_val, 'min_val')
        self.validate_required(self.max_val, 'max_val')
        self.validate_required(self.required, 'required')
        self.validate_required(self.content, 'content')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitFormVO(TeaModel):
    def __init__(
        self,
        method: str = None,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Request methods.
        # POST:POST
        # PUT:PUT
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # POST：POST
        # PUT：PUT
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Parameter name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'Minimum value/Minimum length.', 'zh_CN':'最小值、最小长度。'}
        self.min_val = min_val
        # {'en':'Maximum value/Maximum length.', 'zh_CN':'最大值、最大长度。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content.', 'zh_CN':'内容。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.method, 'method')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_val, 'min_val')
        self.validate_required(self.max_val, 'max_val')
        self.validate_required(self.required, 'required')
        self.validate_required(self.content, 'content')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitJsonChildrenVO(TeaModel):
    def __init__(
        self,
        method: str = None,
        name: str = None,
        level: int = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[str] = None,
    ):
        # {'en':'Request methods.
        # POST:POST
        # PUT:PUT
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # POST：POST
        # PUT：PUT
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Level.', 'zh_CN':'层级。'}
        self.level = level
        # {'en':'Parameter Type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'Minimum value/Minimum length.', 'zh_CN':'最小值、最小长度。'}
        self.min_val = min_val
        # {'en':'Maximum value/Maximum length.', 'zh_CN':'最大值、最大长度。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content.', 'zh_CN':'内容。'}
        self.content = content
        # {'en':'Child node array (JSON string), the structure is consistent with the parent node, required when type= Array.', 'zh_CN':'子节点数组（JSON字符串），结构与父结点一致，type = Array 时必填。'}
        self.children = children

    def validate(self):
        self.validate_required(self.method, 'method')
        self.validate_required(self.name, 'name')
        self.validate_required(self.level, 'level')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_val, 'min_val')
        self.validate_required(self.max_val, 'max_val')
        self.validate_required(self.required, 'required')
        self.validate_required(self.content, 'content')
        self.validate_required(self.children, 'children')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.level is not None:
            result['level'] = self.level
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = self.children
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = m.get('children')
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitJsonVO(TeaModel):
    def __init__(
        self,
        method: str = None,
        name: str = None,
        level: int = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[QueryAPIDefinitionDetailApiDefineParamLimitJsonChildrenVO] = None,
    ):
        # {'en':'Request methods.
        # POST:POST
        # PUT:PUT
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # POST：POST
        # PUT：PUT
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Level.', 'zh_CN':'层级。'}
        self.level = level
        # {'en':'Parameter Type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'Minimum value/Minimum length.', 'zh_CN':'最小值、最小长度。'}
        self.min_val = min_val
        # {'en':'Maximum value/Maximum length.', 'zh_CN':'最大值、最大长度。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content.', 'zh_CN':'内容。'}
        self.content = content
        # {'en':'Child node array, required when type= Array.', 'zh_CN':'子节点数组，type = Array 时必填。'}
        self.children = children

    def validate(self):
        self.validate_required(self.method, 'method')
        self.validate_required(self.name, 'name')
        self.validate_required(self.level, 'level')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_val, 'min_val')
        self.validate_required(self.max_val, 'max_val')
        self.validate_required(self.required, 'required')
        self.validate_required(self.content, 'content')
        self.validate_required(self.children, 'children')
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.level is not None:
            result['level'] = self.level
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = []
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = []
            for k in m.get('children'):
                temp_model = QueryAPIDefinitionDetailApiDefineParamLimitJsonChildrenVO()
                self.children.append(temp_model.from_map(k))
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitMethodVO(TeaModel):
    def __init__(
        self,
        method: str = None,
        body_flag: str = None,
        body_type: str = None,
        normal_param_list: List[QueryAPIDefinitionDetailApiDefineParamLimitNormalVO] = None,
        form_param_list: List[QueryAPIDefinitionDetailApiDefineParamLimitFormVO] = None,
        json_param: QueryAPIDefinitionDetailApiDefineParamLimitJsonVO = None,
    ):
        # {'en':'Request methods.
        # GET:GET
        # POST:POST
        # DELETE:DELETE
        # PUT:PUT
        # HEAD:HEAD
        # OPTIONS:OPTIONS
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # GET：GET
        # POST：POST
        # DELETE：DELETE
        # PUT：PUT
        # HEAD：HEAD
        # OPTIONS：OPTIONS
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Whether to define body parameters.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'是否定义body参数。
        # TRUE：是
        # FALSE：否'}
        self.body_flag = body_flag
        # {'en':'Body parameter type.
        # JSON:JSON
        # FROM:FROM', 'zh_CN':'body参数类型。
        # JSON：JSON
        # FROM：FROM表单'}
        self.body_type = body_type
        # {'en':'Normal parameter list.', 'zh_CN':'普通参数数组。'}
        self.normal_param_list = normal_param_list
        # {'en':'FROM form parameter array.', 'zh_CN':'FROM 表单参数数组。'}
        self.form_param_list = form_param_list
        # {'en':'JSON parameter array.', 'zh_CN':'JSON参数数组。'}
        self.json_param = json_param

    def validate(self):
        self.validate_required(self.method, 'method')
        self.validate_required(self.body_flag, 'body_flag')
        self.validate_required(self.body_type, 'body_type')
        self.validate_required(self.normal_param_list, 'normal_param_list')
        if self.normal_param_list:
            for k in self.normal_param_list:
                if k:
                    k.validate()
        self.validate_required(self.form_param_list, 'form_param_list')
        if self.form_param_list:
            for k in self.form_param_list:
                if k:
                    k.validate()
        self.validate_required(self.json_param, 'json_param')
        if self.json_param:
            self.json_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.body_flag is not None:
            result['bodyFlag'] = self.body_flag
        if self.body_type is not None:
            result['bodyType'] = self.body_type
        if self.normal_param_list is not None:
            result['normalParamList'] = []
            for k in self.normal_param_list:
                result['normalParamList'].append(k.to_map() if k else None)
        if self.form_param_list is not None:
            result['formParamList'] = []
            for k in self.form_param_list:
                result['formParamList'].append(k.to_map() if k else None)
        if self.json_param is not None:
            result['jsonParam'] = self.json_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('bodyFlag') is not None:
            self.body_flag = m.get('bodyFlag')
        if m.get('bodyType') is not None:
            self.body_type = m.get('bodyType')
        if m.get('normalParamList') is not None:
            self.normal_param_list = []
            for k in m.get('normalParamList'):
                temp_model = QueryAPIDefinitionDetailApiDefineParamLimitNormalVO()
                self.normal_param_list.append(temp_model.from_map(k))
        if m.get('formParamList') is not None:
            self.form_param_list = []
            for k in m.get('formParamList'):
                temp_model = QueryAPIDefinitionDetailApiDefineParamLimitFormVO()
                self.form_param_list.append(temp_model.from_map(k))
        if m.get('jsonParam') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineParamLimitJsonVO()
            self.json_param = temp_model.from_map(m['jsonParam'])
        return self


class QueryAPIDefinitionDetailApiDefineParamLimitVO(TeaModel):
    def __init__(
        self,
        basic: QueryAPIDefinitionDetailApiDefineParamLimitBasicVO = None,
        method_list: List[QueryAPIDefinitionDetailApiDefineParamLimitMethodVO] = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'Method attributes.', 'zh_CN':'方法属性。'}
        self.method_list = method_list

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        self.validate_required(self.method_list, 'method_list')
        if self.method_list:
            for k in self.method_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.method_list is not None:
            result['methodList'] = []
            for k in self.method_list:
                result['methodList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineParamLimitBasicVO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('methodList') is not None:
            self.method_list = []
            for k in m.get('methodList'):
                temp_model = QueryAPIDefinitionDetailApiDefineParamLimitMethodVO()
                self.method_list.append(temp_model.from_map(k))
        return self


class QueryAPIDefinitionDetailApiDefineVO(TeaModel):
    def __init__(
        self,
        basic: QueryAPIDefinitionDetailApiDefineBasicVO = None,
        endpoint: QueryAPIDefinitionDetailApiDefineEndpointVO = None,
        auth: QueryAPIDefinitionDetailApiDefineAuthVO = None,
        body_limit: QueryAPIDefinitionDetailApiDefineBodyLimitVO = None,
        param_limit: QueryAPIDefinitionDetailApiDefineParamLimitVO = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'Endpoint information.', 'zh_CN':'端点信息。'}
        self.endpoint = endpoint
        # {'en':'Authentication configuration.', 'zh_CN':'鉴权配置。'}
        self.auth = auth
        # {'en':'Body restrictions.', 'zh_CN':'body限制。'}
        self.body_limit = body_limit
        # {'en':'Parameter limit.', 'zh_CN':'参数限制。'}
        self.param_limit = param_limit

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        self.validate_required(self.endpoint, 'endpoint')
        if self.endpoint:
            self.endpoint.validate()
        self.validate_required(self.auth, 'auth')
        if self.auth:
            self.auth.validate()
        self.validate_required(self.body_limit, 'body_limit')
        if self.body_limit:
            self.body_limit.validate()
        self.validate_required(self.param_limit, 'param_limit')
        if self.param_limit:
            self.param_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint.to_map()
        if self.auth is not None:
            result['auth'] = self.auth.to_map()
        if self.body_limit is not None:
            result['bodyLimit'] = self.body_limit.to_map()
        if self.param_limit is not None:
            result['paramLimit'] = self.param_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineBasicVO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('endpoint') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineEndpointVO()
            self.endpoint = temp_model.from_map(m['endpoint'])
        if m.get('auth') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineAuthVO()
            self.auth = temp_model.from_map(m['auth'])
        if m.get('bodyLimit') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineBodyLimitVO()
            self.body_limit = temp_model.from_map(m['bodyLimit'])
        if m.get('paramLimit') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineParamLimitVO()
            self.param_limit = temp_model.from_map(m['paramLimit'])
        return self


class QueryAPIDefinitionDetailResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: QueryAPIDefinitionDetailApiDefineVO = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            temp_model = QueryAPIDefinitionDetailApiDefineVO()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryAPIDefinitionDetailPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAPIDefinitionDetailParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAPIDefinitionDetailRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class QueryAPIDefinitionDetailResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class FeedbackWrongAPIAssetDiscoveryRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        feedback: str = None,
    ):
        # {"en":"API discovery ID.", "zh_CN":"API发现ID。"}
        self.id = id
        # {"en":"Feedback, maximum 200 characters.", "zh_CN":"反馈意见，最多200个字符。"}
        self.feedback = feedback

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.feedback is not None:
            result['feedback'] = self.feedback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')
        return self


class FeedbackWrongAPIAssetDiscoveryResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class FeedbackWrongAPIAssetDiscoveryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FeedbackWrongAPIAssetDiscoveryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FeedbackWrongAPIAssetDiscoveryRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class FeedbackWrongAPIAssetDiscoveryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateAPIDefinitionApiDefineBasicEditDTO(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        group_name: str = None,
        remark: str = None,
    ):
        # {'en':'API define ID.', 'zh_CN':'API定义ID。'}
        self.id = id
        # {'en':'API name, maximum 200 characters.', 'zh_CN':'API名称，最多200个字符。'}
        self.name = name
        # {'en':'API groups, maximum 64 characters.', 'zh_CN':'API分组，最多64个字符。'}
        self.group_name = group_name
        # {'en':'Description, maximum 200 characters.', 'zh_CN':'备注，最多200个字符。'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.group_name, 'group_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateAPIDefinitionApiDefineEndpointEditDTO(TeaModel):
    def __init__(
        self,
        request_method: str = None,
        case_sensitive: str = None,
    ):
        # {'en':'Request methods,Multiple separated by ; sign.
        # GET:GET, configurable parameter limits
        # POST:POST, configurable parameter limits
        # DELETE:DELETE, configurable parameter limits
        # UPDATE:UPDATE
        # PUT:PUT, configurable parameter limits
        # HEAD:HEAD, configurable parameter limits
        # CONNECT:CONNECT
        # OPTIONS:OPTIONS, configurable parameter limits
        # COPY:COPY
        # LOCK:LOCK
        # UNLOCK:UNLOCK
        # TRACE:TRACE
        # PATCH:PATCH, configurable parameter limits
        # PROPFIND:PROPFIND
        # MKCOL:MKCOL
        # MOVE:MOVE', 'zh_CN':'请求方法。多个以 ; 号分隔。
        # GET：GET，可配置参数限制
        # POST：POST，可配置参数限制
        # DELETE：DELETE，可配置参数限制
        # UPDATE：UPDATE
        # PUT：PUT，可配置参数限制
        # HEAD：HEAD，可配置参数限制
        # CONNECT：CONNECT
        # OPTIONS：OPTIONS，可配置参数限制
        # COPY：COPY
        # LOCK：LOCK
        # UNLOCK：UNLOCK
        # TRACE：TRACE
        # PATCH：PATCH，可配置参数限制
        # PROPFIND：PROPFIND
        # MKCOL：MKCOL
        # MOVE：MOVE'}
        self.request_method = request_method
        # {'en':'Case sensitive.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'大小写是否敏感。
        # TRUE：是
        # FALSE：否'}
        self.case_sensitive = case_sensitive

    def validate(self):
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.case_sensitive, 'case_sensitive')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        return self


class UpdateAPIDefinitionApiDefineAuthEditDTO(TeaModel):
    def __init__(
        self,
        type: str = None,
        auth_key: str = None,
        param_position: str = None,
        param_name: str = None,
        validity_time: int = None,
    ):
        # {'en':'Authentication method.
        # NO_NEED:No authentication required
        # SIGN:Key authentication', 'zh_CN':'鉴权方法。
        # NO_NEED：免鉴权
        # SIGN：秘钥对鉴权'}
        self.type = type
        # {'en':'Authentication key, type = SIGN is required. If it has been set, it will be ignored. The format is a 16-digit string containing uppercase and lowercase letters and numbers. Example: gjZkg2E1uNkXBDxj.', 'zh_CN':'鉴权秘钥，type = SIGN 是必填，如已设置则忽略，格式为16位含大小写字母与数字字符串，示例：gjZkg2E1uNkXBDxj。'}
        self.auth_key = auth_key
        # {'en':'Authentication parameter location, type = SIGN is required.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie', 'zh_CN':'鉴权参数位置，type = SIGN 时必填。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie'}
        self.param_position = param_position
        # {'en':'Authentication parameter name, type = SIGN is required.', 'zh_CN':'鉴权参数名称，type = SIGN 时必填。'}
        self.param_name = param_name
        # {'en':'Authentication token validity period, in seconds, type = SIGN is required.', 'zh_CN':'鉴权有效期，单位秒，type = SIGN 时必填。'}
        self.validity_time = validity_time

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.auth_key is not None:
            result['authKey'] = self.auth_key
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.validity_time is not None:
            result['validityTime'] = self.validity_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('authKey') is not None:
            self.auth_key = m.get('authKey')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('validityTime') is not None:
            self.validity_time = m.get('validityTime')
        return self


class UpdateAPIDefinitionApiDefineBodyLimitEditDTO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        content_type: str = None,
        body_limit_max: int = None,
        nest_max: int = None,
        param_count_max: int = None,
    ):
        # {'en':'Request body restriction switch. default value:OFF.
        # ON:On
        # OFF:Off', 'zh_CN':'请求body限制开关。默认值：关。
        # ON：开启
        # OFF：关闭'}
        self.defend_switch = defend_switch
        # {'en':'Content-Type, required when defendSwitch = ON.
        # FORM:FORM
        # JSON:JSON
        # ANY:ANY
        # EMPTY:EMPTY or NON-EXISTENT', 'zh_CN':'Content-Type，defendSwitch = ON 时必填。
        # FORM：FORM表单
        # JSON：JSON
        # ANY：任意
        # EMPTY：为空或不存在'}
        self.content_type = content_type
        # {'en':'Maximum body limit(bytes).', 'zh_CN':'Body最大限制(bytes)。'}
        self.body_limit_max = body_limit_max
        # {'en':'Maximum nesting depth, enter the maximum allowable JSON nesting depth in the request body.', 'zh_CN':'最大嵌套层数，输入允许的请求body中JSON嵌套层数最大值。'}
        self.nest_max = nest_max
        # {'en':'Maximum number of parameters for JSON, enter the maximum number of JSON parameters allowed in the request body.', 'zh_CN':'JSON最大参数个数，输入允许的请求body中JSON参数个数的最大值。'}
        self.param_count_max = param_count_max

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.body_limit_max is not None:
            result['bodyLimitMax'] = self.body_limit_max
        if self.nest_max is not None:
            result['nestMax'] = self.nest_max
        if self.param_count_max is not None:
            result['paramCountMax'] = self.param_count_max
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('bodyLimitMax') is not None:
            self.body_limit_max = m.get('bodyLimitMax')
        if m.get('nestMax') is not None:
            self.nest_max = m.get('nestMax')
        if m.get('paramCountMax') is not None:
            self.param_count_max = m.get('paramCountMax')
        return self


class UpdateAPIDefinitionApiDefineParamLimitBasicEditDTO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        param_check_mode: str = None,
    ):
        # {'en':'Parameter limit.
        # ON:On
        # OFF:Off', 'zh_CN':'参数限制。
        # ON：开启
        # OFF：关闭'}
        self.defend_switch = defend_switch
        # {'en':'Query String Parameter Detection Mode, required when defendSwitch = ON.
        # LOOSE:Loose mode - detect some parameters
        # STRICT:Strict mode - checks all parameters', 'zh_CN':'Query String参数检测模式，defendSwitch = ON 时必填。
        # LOOSE：宽松模式-检测部分参数
        # STRICT：严格模式-检测所有参数'}
        self.param_check_mode = param_check_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.param_check_mode is not None:
            result['paramCheckMode'] = self.param_check_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('paramCheckMode') is not None:
            self.param_check_mode = m.get('paramCheckMode')
        return self


class UpdateAPIDefinitionApiDefineParamLimitNormalEditDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        param_position: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Parameter name, when paramPosition = PATH_PARAMS, the path need to be matched, for example: /basePath/{name}/.', 'zh_CN':'参数名称，paramPosition = PATH_PARAMS 时需匹配路径变量，例如：/basePath/{name}/。'}
        self.name = name
        # {'en':'Parameter position.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie
        # PATH_PARAMS:Path, endpoint.matchPathVar needs to equal TRUE', 'zh_CN':'参数位置。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie
        # PATH_PARAMS：路径变量，endpoint.matchPathVar需等于TRUE'}
        self.param_position = param_position
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, Multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateAPIDefinitionApiDefineParamLimitFormEditDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Parameter name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class UpdateAPIDefinitionApiDefineParamLimitJsonChildrenDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[str] = None,
    ):
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter Type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Child node array (JSON string), the structure is consistent with the parent node, required when type= Array.', 'zh_CN':'子节点数组（JSON字符串），结构与父结点一致，type = Array 时必填。'}
        self.children = children

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = self.children
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = m.get('children')
        return self


class UpdateAPIDefinitionApiDefineParamLimitJsonEditDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[UpdateAPIDefinitionApiDefineParamLimitJsonChildrenDTO] = None,
    ):
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter Type.
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Array of child nodes, required when type= Array.', 'zh_CN':'子节点数组，type = Array 时必填。'}
        self.children = children

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = []
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = []
            for k in m.get('children'):
                temp_model = UpdateAPIDefinitionApiDefineParamLimitJsonChildrenDTO()
                self.children.append(temp_model.from_map(k))
        return self


class UpdateAPIDefinitionApiDefineParamLimitMethodEditDTO(TeaModel):
    def __init__(
        self,
        method: str = None,
        body_flag: str = None,
        body_type: str = None,
        normal_param_list: List[UpdateAPIDefinitionApiDefineParamLimitNormalEditDTO] = None,
        form_param_list: List[UpdateAPIDefinitionApiDefineParamLimitFormEditDTO] = None,
        json_param: UpdateAPIDefinitionApiDefineParamLimitJsonEditDTO = None,
    ):
        # {'en':'Request methods.
        # GET:GET
        # POST:POST
        # DELETE:DELETE
        # PUT:PUT
        # HEAD:HEAD
        # OPTIONS:OPTIONS
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # GET：GET
        # POST：POST
        # DELETE：DELETE
        # PUT：PUT
        # HEAD：HEAD
        # OPTIONS：OPTIONS
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Whether to define body parameters, required when method = POST/PUT/PATCH.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'是否定义body参数，method = POST/PUT/PATCH时必填。
        # TRUE：是
        # FALSE：否'}
        self.body_flag = body_flag
        # {'en':'Body parameter type, required when bodyFlag = TRUE.
        # JSON:JSON
        # FROM:FROM', 'zh_CN':'body参数类型，bodyFlag = TRUE 时必填。
        # JSON：JSON
        # FROM：FROM表单'}
        self.body_type = body_type
        # {'en':'Normal parameter list.', 'zh_CN':'普通参数数组。'}
        self.normal_param_list = normal_param_list
        # {'en':'FROM form parameter array, Optional when bodyType = FROM.', 'zh_CN':'FROM 表单参数数组，bodyType = FROM 时选填。'}
        self.form_param_list = form_param_list
        # {'en':'JSON parameter array, Optional when bodyType = JSON.', 'zh_CN':'JSON参数数组，bodyType = JSON 时选填。'}
        self.json_param = json_param

    def validate(self):
        if self.normal_param_list:
            for k in self.normal_param_list:
                if k:
                    k.validate()
        if self.form_param_list:
            for k in self.form_param_list:
                if k:
                    k.validate()
        if self.json_param:
            self.json_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.body_flag is not None:
            result['bodyFlag'] = self.body_flag
        if self.body_type is not None:
            result['bodyType'] = self.body_type
        if self.normal_param_list is not None:
            result['normalParamList'] = []
            for k in self.normal_param_list:
                result['normalParamList'].append(k.to_map() if k else None)
        if self.form_param_list is not None:
            result['formParamList'] = []
            for k in self.form_param_list:
                result['formParamList'].append(k.to_map() if k else None)
        if self.json_param is not None:
            result['jsonParam'] = self.json_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('bodyFlag') is not None:
            self.body_flag = m.get('bodyFlag')
        if m.get('bodyType') is not None:
            self.body_type = m.get('bodyType')
        if m.get('normalParamList') is not None:
            self.normal_param_list = []
            for k in m.get('normalParamList'):
                temp_model = UpdateAPIDefinitionApiDefineParamLimitNormalEditDTO()
                self.normal_param_list.append(temp_model.from_map(k))
        if m.get('formParamList') is not None:
            self.form_param_list = []
            for k in m.get('formParamList'):
                temp_model = UpdateAPIDefinitionApiDefineParamLimitFormEditDTO()
                self.form_param_list.append(temp_model.from_map(k))
        if m.get('jsonParam') is not None:
            temp_model = UpdateAPIDefinitionApiDefineParamLimitJsonEditDTO()
            self.json_param = temp_model.from_map(m['jsonParam'])
        return self


class UpdateAPIDefinitionApiDefineParamLimitEditDTO(TeaModel):
    def __init__(
        self,
        basic: UpdateAPIDefinitionApiDefineParamLimitBasicEditDTO = None,
        change_param_limit_method_list: List[str] = None,
        method_list: List[UpdateAPIDefinitionApiDefineParamLimitMethodEditDTO] = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'There are request methods for changing configurations.
        # GET:GET
        # POST:POST
        # DELETE:DELETE
        # PUT:PUT
        # HEAD:HEAD
        # OPTIONS:OPTIONS
        # PATCH:PATCH', 'zh_CN':'有变更配置的请求方法。
        # GET：GET
        # POST：POST
        # DELETE：DELETE
        # PUT：PUT
        # HEAD：HEAD
        # OPTIONS：OPTIONS
        # PATCH：PATCH'}
        self.change_param_limit_method_list = change_param_limit_method_list
        # {'en':'Method attributes.', 'zh_CN':'方法属性。'}
        self.method_list = method_list

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        if self.method_list:
            for k in self.method_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.change_param_limit_method_list is not None:
            result['changeParamLimitMethodList'] = self.change_param_limit_method_list
        if self.method_list is not None:
            result['methodList'] = []
            for k in self.method_list:
                result['methodList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = UpdateAPIDefinitionApiDefineParamLimitBasicEditDTO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('changeParamLimitMethodList') is not None:
            self.change_param_limit_method_list = m.get('changeParamLimitMethodList')
        if m.get('methodList') is not None:
            self.method_list = []
            for k in m.get('methodList'):
                temp_model = UpdateAPIDefinitionApiDefineParamLimitMethodEditDTO()
                self.method_list.append(temp_model.from_map(k))
        return self


class UpdateAPIDefinitionRequest(TeaModel):
    def __init__(
        self,
        basic: UpdateAPIDefinitionApiDefineBasicEditDTO = None,
        endpoint: UpdateAPIDefinitionApiDefineEndpointEditDTO = None,
        auth: UpdateAPIDefinitionApiDefineAuthEditDTO = None,
        body_limit: UpdateAPIDefinitionApiDefineBodyLimitEditDTO = None,
        param_limit: UpdateAPIDefinitionApiDefineParamLimitEditDTO = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'Endpoint information.', 'zh_CN':'端点信息。'}
        self.endpoint = endpoint
        # {'en':'Authentication configuration.', 'zh_CN':'鉴权配置。'}
        self.auth = auth
        # {'en':'Body restrictions.', 'zh_CN':'body限制。'}
        self.body_limit = body_limit
        # {'en':'Parameter limit.', 'zh_CN':'参数限制。'}
        self.param_limit = param_limit

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        if self.endpoint:
            self.endpoint.validate()
        if self.auth:
            self.auth.validate()
        if self.body_limit:
            self.body_limit.validate()
        if self.param_limit:
            self.param_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint.to_map()
        if self.auth is not None:
            result['auth'] = self.auth.to_map()
        if self.body_limit is not None:
            result['bodyLimit'] = self.body_limit.to_map()
        if self.param_limit is not None:
            result['paramLimit'] = self.param_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = UpdateAPIDefinitionApiDefineBasicEditDTO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('endpoint') is not None:
            temp_model = UpdateAPIDefinitionApiDefineEndpointEditDTO()
            self.endpoint = temp_model.from_map(m['endpoint'])
        if m.get('auth') is not None:
            temp_model = UpdateAPIDefinitionApiDefineAuthEditDTO()
            self.auth = temp_model.from_map(m['auth'])
        if m.get('bodyLimit') is not None:
            temp_model = UpdateAPIDefinitionApiDefineBodyLimitEditDTO()
            self.body_limit = temp_model.from_map(m['bodyLimit'])
        if m.get('paramLimit') is not None:
            temp_model = UpdateAPIDefinitionApiDefineParamLimitEditDTO()
            self.param_limit = temp_model.from_map(m['paramLimit'])
        return self


class UpdateAPIDefinitionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateAPIDefinitionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPIDefinitionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPIDefinitionRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class UpdateAPIDefinitionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListAPIAssetDiscoveryRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        path_list: List[str] = None,
        define_status: str = None,
        order_by: str = None,
    ):
        # {"en":"Hostname list.", "zh_CN":"域名列表。"}
        self.domain_list = domain_list
        # {"en":"API base path.", "zh_CN":"端点路径。"}
        self.path_list = path_list
        # {"en":"Definition state.
        # DEFINED: Defined
        # UNDEFINED:Undefined", "zh_CN":"定义状态。
        # DEFINED: 已定义
        # UNDEFINED:未定义"}
        self.define_status = define_status
        # {"en":"Sort, format: field1,sort1;field2,sort2.
        # Optional field:
        # lastDiscoveryTime: Last discovery time
        # firstDiscoveryTime: First discovery time
        # reqCount24h: 24h Requests
        # Optional sort:
        # ascending:Ascend
        # descending:Descend.", "zh_CN":"排序，格式：字段1,排序1;字段2,排序2。
        # 可选字段：
        # lastDiscoveryTime：最新发现时间
        # firstDiscoveryTime：首次发现时间
        # reqCount24h：24h调用量
        # 可选排序：
        # ascending：升序
        # descending：降序"}
        self.order_by = order_by

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.path_list is not None:
            result['pathList'] = self.path_list
        if self.define_status is not None:
            result['defineStatus'] = self.define_status
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('pathList') is not None:
            self.path_list = m.get('pathList')
        if m.get('defineStatus') is not None:
            self.define_status = m.get('defineStatus')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self


class ListAPIAssetDiscoveryApiDiscoveryLogVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        domain: str = None,
        path: str = None,
        last_discovery_time: str = None,
        first_discovery_time: str = None,
        req_count_24h: int = None,
        define_status: str = None,
    ):
        # {"en":"API discovery ID.", "zh_CN":"API发现ID。"}
        self.id = id
        # {"en":"Hostname.", "zh_CN":"域名。"}
        self.domain = domain
        # {"en":"API base path.", "zh_CN":"端点路径。"}
        self.path = path
        # {"en":"Last Discovery Time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"最新发现时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.last_discovery_time = last_discovery_time
        # {"en":"First Discovery Time, format: yyyy-MM-dd HH:mm:ss.", "zh_CN":"首次发现时间，格式：yyyy-MM-dd HH:mm:ss。"}
        self.first_discovery_time = first_discovery_time
        # {"en":"24h Requests.", "zh_CN":"24h调用量。"}
        self.req_count_24h = req_count_24h
        # {"en":"Status.
        # DEFINED: Defined
        # UNDEFINED:Pending", "zh_CN":"定义状态。
        # DEFINED: 已定义
        # UNDEFINED: 待确认"}
        self.define_status = define_status

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.path, 'path')
        self.validate_required(self.last_discovery_time, 'last_discovery_time')
        self.validate_required(self.first_discovery_time, 'first_discovery_time')
        self.validate_required(self.req_count_24h, 'req_count_24h')
        self.validate_required(self.define_status, 'define_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.domain is not None:
            result['domain'] = self.domain
        if self.path is not None:
            result['path'] = self.path
        if self.last_discovery_time is not None:
            result['lastDiscoveryTime'] = self.last_discovery_time
        if self.first_discovery_time is not None:
            result['firstDiscoveryTime'] = self.first_discovery_time
        if self.req_count_24h is not None:
            result['reqCount24h'] = self.req_count_24h
        if self.define_status is not None:
            result['defineStatus'] = self.define_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('lastDiscoveryTime') is not None:
            self.last_discovery_time = m.get('lastDiscoveryTime')
        if m.get('firstDiscoveryTime') is not None:
            self.first_discovery_time = m.get('firstDiscoveryTime')
        if m.get('reqCount24h') is not None:
            self.req_count_24h = m.get('reqCount24h')
        if m.get('defineStatus') is not None:
            self.define_status = m.get('defineStatus')
        return self


class ListAPIAssetDiscoveryResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListAPIAssetDiscoveryApiDiscoveryLogVO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {"en":"Description.", "zh_CN":"描述信息。"}
        self.msg = msg
        # {"en":"Data.", "zh_CN":"出参数据。"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = ListAPIAssetDiscoveryApiDiscoveryLogVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListAPIAssetDiscoveryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListAPIAssetDiscoveryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListAPIAssetDiscoveryRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class ListAPIAssetDiscoveryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateAPIDefinitionApiDefineBasicAddDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        group_name: str = None,
        domain: str = None,
        remark: str = None,
    ):
        # {'en':'API name, maximum 200 characters.', 'zh_CN':'API名称，最多200个字符。'}
        self.name = name
        # {'en':'API groups, maximum 64 characters.', 'zh_CN':'API分组，最多64个字符。'}
        self.group_name = group_name
        # {'en':'Hostname.', 'zh_CN':'所属域名。'}
        self.domain = domain
        # {'en':'Description, maximum 200 characters.', 'zh_CN':'备注，最多200个字符。'}
        self.remark = remark

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateAPIDefinitionApiDefineEndpointAddDTO(TeaModel):
    def __init__(
        self,
        request_method: str = None,
        type: str = None,
        match_type: str = None,
        path: str = None,
        case_sensitive: str = None,
        match_path_var: str = None,
    ):
        # {'en':'Request methods.Multiple separated by ; sign.
        # GET:GET, configurable parameter limits
        # POST:POST, configurable parameter limits
        # DELETE:DELETE, configurable parameter limits
        # UPDATE:UPDATE
        # PUT:PUT, configurable parameter limits
        # HEAD:HEAD, configurable parameter limits
        # CONNECT:CONNECT
        # OPTIONS:OPTIONS, configurable parameter limits
        # COPY:COPY
        # LOCK:LOCK
        # UNLOCK:UNLOCK
        # TRACE:TRACE
        # PATCH:PATCH, configurable parameter limits
        # PROPFIND:PROPFIND
        # MKCOL:MKCOL
        # MOVE:MOVE', 'zh_CN':'请求方法。多个以 ; 号分隔。
        # GET：GET，可配置参数限制
        # POST：POST，可配置参数限制
        # DELETE：DELETE，可配置参数限制
        # UPDATE：UPDATE
        # PUT：PUT，可配置参数限制
        # HEAD：HEAD，可配置参数限制
        # CONNECT：CONNECT
        # OPTIONS：OPTIONS，可配置参数限制
        # COPY：COPY
        # LOCK：LOCK
        # UNLOCK：UNLOCK
        # TRACE：TRACE
        # PATCH：PATCH，可配置参数限制
        # PROPFIND：PROPFIND
        # MKCOL：MKCOL
        # MOVE：MOVE'}
        self.request_method = request_method
        # {'en':'API type.
        # NORMAL:Common API, the path does not contain query string parameters, such as http://www.test.com/api.
        # WHEN_CASE:Common API, the path contains query string parameters, such as http://www.test.com/api?action=1 and http://www.test.com/api?action=2 are two different APIs.', 'zh_CN':'API类型。
        # NORMAL：普通接口，路径中不包含query string参数的普通接口，如http://www.test.com/api。
        # WHEN_CASE：when-case接口，路径中包含query string参数，如http://www.test.com/api?action=1与http://www.test.com/api?action=2 是两个不同的接口。'}
        self.type = type
        # {'en':'Path matching type, EQUAL is passed when type = WHEM_CASE.
        # EQUAL: Complete match
        # REGEX: Regular matching', 'zh_CN':'路径匹配类型，type = WHEN_CASE 时传 EQUAL。
        # EQUAL：完整匹配
        # REGEX：正则匹配'}
        self.match_type = match_type
        # {'en':'API base Path, only English characters, underscores, hyphens, or numbers are supported, maximum 200 characters.', 'zh_CN':'端点路径，只支持英文字符、下划线、短横线或数字，最多200个字符。'}
        self.path = path
        # {'en':'Case sensitive, whether the endpoint path is case-sensitive. Example for case sensitive: /Order and /order are two different API paths.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'大小写是否敏感，端点路径是否区分大小写。若大小写敏感，示例：/Order 和 /order为两不同的API路径。
        # TRUE：是
        # FALSE：否'}
        self.case_sensitive = case_sensitive
        # {'en':'Match CreateAPIDefinitionParameters in the Path(Effective when type = NORMAL && matchType = EQUAL), with matching path parameters turned on, you can use curly braces "{}" to define path parameters. Example: /basePath/{pathParam1}/{pathParam2}/{pathParam3}.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'匹配路径参数（type = NORMAL && matchType = EQUAL 时生效），开启匹配路径参数后，您可以使用花括号({})来定义路径参数。例：/basePath/{pathParam1}/{pathParam2}/{pathParam3}。
        # TRUE：是
        # FALSE：否'}
        self.match_path_var = match_path_var

    def validate(self):
        self.validate_required(self.request_method, 'request_method')
        self.validate_required(self.type, 'type')
        self.validate_required(self.match_type, 'match_type')
        self.validate_required(self.path, 'path')
        self.validate_required(self.case_sensitive, 'case_sensitive')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_method is not None:
            result['requestMethod'] = self.request_method
        if self.type is not None:
            result['type'] = self.type
        if self.match_type is not None:
            result['matchType'] = self.match_type
        if self.path is not None:
            result['path'] = self.path
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.match_path_var is not None:
            result['matchPathVar'] = self.match_path_var
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestMethod') is not None:
            self.request_method = m.get('requestMethod')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('matchPathVar') is not None:
            self.match_path_var = m.get('matchPathVar')
        return self


class CreateAPIDefinitionApiDefineAuthAddDTO(TeaModel):
    def __init__(
        self,
        type: str = None,
        auth_key: str = None,
        param_position: str = None,
        param_name: str = None,
        validity_time: int = None,
    ):
        # {'en':'Authentication method.
        # NO_NEED:No authentication required
        # SIGN:Key authentication', 'zh_CN':'鉴权方法。
        # NO_NEED：免鉴权
        # SIGN：秘钥对鉴权'}
        self.type = type
        # {'en':'Authentication key, type = SIGN is required, the format is a 16-digit string containing uppercase and lowercase letters and numbers, example: gjZkg2E1uNkXBDxj.', 'zh_CN':'鉴权秘钥，type = SIGN 时必填，格式为16位含大小写字母与数字字符串，示例：gjZkg2E1uNkXBDxj。'}
        self.auth_key = auth_key
        # {'en':'Authentication parameter location, type = SIGN is required.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie', 'zh_CN':'鉴权参数位置，type = SIGN 时必填。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie'}
        self.param_position = param_position
        # {'en':'Authentication parameter name, type = SIGN is required.', 'zh_CN':'鉴权参数名称，type = SIGN 时必填。'}
        self.param_name = param_name
        # {'en':'Authentication token validity period, in seconds, type = SIGN is required.', 'zh_CN':'鉴权有效期，单位秒，type = SIGN 时必填。'}
        self.validity_time = validity_time

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.auth_key is not None:
            result['authKey'] = self.auth_key
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.validity_time is not None:
            result['validityTime'] = self.validity_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('authKey') is not None:
            self.auth_key = m.get('authKey')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('validityTime') is not None:
            self.validity_time = m.get('validityTime')
        return self


class CreateAPIDefinitionApiDefineBodyLimitAddDTO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        content_type: str = None,
        body_limit_max: int = None,
        nest_max: int = None,
        param_count_max: int = None,
    ):
        # {'en':'Request body restriction switch.default value:OFF.
        # ON:On
        # OFF:Off', 'zh_CN':'请求body限制开关。默认值：关。
        # ON：开启
        # OFF：关闭'}
        self.defend_switch = defend_switch
        # {'en':'Content-Type, required when defendSwitch = ON.
        # FORM:FORM
        # JSON:JSON
        # ANY:ANY
        # EMPTY:EMPTY or NON-EXISTENT', 'zh_CN':'Content-Type，defendSwitch = ON 时必填。
        # FORM：FORM表单
        # JSON：JSON
        # ANY：任意
        # EMPTY：为空或不存在'}
        self.content_type = content_type
        # {'en':'Maximum body limit(bytes).', 'zh_CN':'Body最大限制(bytes)。'}
        self.body_limit_max = body_limit_max
        # {'en':'Maximum nesting depth, enter the maximum allowable JSON nesting depth in the request body.', 'zh_CN':'最大嵌套层数，输入允许的请求body中JSON嵌套层数最大值。'}
        self.nest_max = nest_max
        # {'en':'Maximum number of parameters for JSON, enter the maximum number of JSON parameters allowed in the request body.', 'zh_CN':'JSON最大参数个数，输入允许的请求body中JSON参数个数的最大值。'}
        self.param_count_max = param_count_max

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.body_limit_max is not None:
            result['bodyLimitMax'] = self.body_limit_max
        if self.nest_max is not None:
            result['nestMax'] = self.nest_max
        if self.param_count_max is not None:
            result['paramCountMax'] = self.param_count_max
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('bodyLimitMax') is not None:
            self.body_limit_max = m.get('bodyLimitMax')
        if m.get('nestMax') is not None:
            self.nest_max = m.get('nestMax')
        if m.get('paramCountMax') is not None:
            self.param_count_max = m.get('paramCountMax')
        return self


class CreateAPIDefinitionApiDefineParamLimitBasicAddDTO(TeaModel):
    def __init__(
        self,
        defend_switch: str = None,
        param_check_mode: str = None,
    ):
        # {'en':'Parameter limit.
        # ON:On
        # OFF:Off', 'zh_CN':'参数限制。
        # ON：开启
        # OFF：关闭'}
        self.defend_switch = defend_switch
        # {'en':'Query String Parameter Detection Mode, required when defendSwitch = ON.
        # LOOSE:Loose mode - detect some parameters
        # STRICT:Strict mode - checks all parameters', 'zh_CN':'Query String参数检测模式，defendSwitch = ON 时必填。
        # LOOSE：宽松模式-检测部分参数
        # STRICT：严格模式-检测所有参数'}
        self.param_check_mode = param_check_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defend_switch is not None:
            result['defendSwitch'] = self.defend_switch
        if self.param_check_mode is not None:
            result['paramCheckMode'] = self.param_check_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defendSwitch') is not None:
            self.defend_switch = m.get('defendSwitch')
        if m.get('paramCheckMode') is not None:
            self.param_check_mode = m.get('paramCheckMode')
        return self


class CreateAPIDefinitionApiDefineParamLimitNormalAddDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        param_position: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Parameter name, when paramPosition = PATH_PARAMS, the path need to be matched, for example: /basePath/{name}/.', 'zh_CN':'参数名称，paramPosition = PATH_PARAMS 时需匹配路径变量，例如：/basePath/{name}/。'}
        self.name = name
        # {'en':'Parameter position.
        # HTTP_HEADER:Http Header
        # QUERY_STRING:Query String
        # COOKIE:Cookie
        # PATH_PARAMS:Path, endpoint.matchPathVar needs to equal TRUE', 'zh_CN':'参数位置。
        # HTTP_HEADER：Http Header
        # QUERY_STRING：Query String
        # COOKIE：Cookie
        # PATH_PARAMS：路径变量，endpoint.matchPathVar需等于TRUE'}
        self.param_position = param_position
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration,multiple separated by  ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.param_position is not None:
            result['paramPosition'] = self.param_position
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paramPosition') is not None:
            self.param_position = m.get('paramPosition')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateAPIDefinitionApiDefineParamLimitFormAddDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        remark: str = None,
    ):
        # {'en':'Parameter name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateAPIDefinitionApiDefineParamLimitJsonAddChildrenDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[str] = None,
    ):
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter Type.
        # Integer:Integer
        # Number:Number
        # String:String
        # Boolean:Boolean
        # Enumeration:Enumeration
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Integer：整数
        # Number：数字
        # String：字符串
        # Boolean：布尔
        # Enumeration：枚举
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Child node array (JSON string), the structure is consistent with the parent node, required when type= Array.', 'zh_CN':'子节点数组（JSON字符串），结构与父结点一致，type = Array 时必填。'}
        self.children = children

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = self.children
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = m.get('children')
        return self


class CreateAPIDefinitionApiDefineParamLimitJsonAddDTO(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        min_val: str = None,
        max_val: str = None,
        required: str = None,
        content: str = None,
        children: List[CreateAPIDefinitionApiDefineParamLimitJsonAddChildrenDTO] = None,
    ):
        # {'en':'Parameter Name.', 'zh_CN':'参数名称。'}
        self.name = name
        # {'en':'Parameter Type.
        # Array:Array
        # Json:JSON Object', 'zh_CN':'参数类型。
        # Array：数组
        # Json：JSON对象'}
        self.type = type
        # {'en':'type = Integer/Number:minimum value, type = String:minimum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最小值，type = String：最小长度，type = Boolean/Enumeration：置空。'}
        self.min_val = min_val
        # {'en':'type = Integer/Number:maximum value, type = String:maximum length, type = Boolean/Enumeration:leave blank.', 'zh_CN':'type = Integer/Number：最大值，type = String：最大长度，type = Boolean/Enumeration：置空。'}
        self.max_val = max_val
        # {'en':'Required.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'必带参数。
        # TRUE：是
        # FALSE：否'}
        self.required = required
        # {'en':'Content (maximum 2000 characters), required when type = Enumeration, multiple separated by ; sign.', 'zh_CN':'内容（最多2000个字符），type = Enumeration 时必填，多个以 ; 号分隔。'}
        self.content = content
        # {'en':'Child node array, required when type= Array.', 'zh_CN':'子节点数组，type = Array 时必填。'}
        self.children = children

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.min_val is not None:
            result['minVal'] = self.min_val
        if self.max_val is not None:
            result['maxVal'] = self.max_val
        if self.required is not None:
            result['required'] = self.required
        if self.content is not None:
            result['content'] = self.content
        if self.children is not None:
            result['children'] = []
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('minVal') is not None:
            self.min_val = m.get('minVal')
        if m.get('maxVal') is not None:
            self.max_val = m.get('maxVal')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('children') is not None:
            self.children = []
            for k in m.get('children'):
                temp_model = CreateAPIDefinitionApiDefineParamLimitJsonAddChildrenDTO()
                self.children.append(temp_model.from_map(k))
        return self


class CreateAPIDefinitionApiDefineParamLimitMethodAddDTO(TeaModel):
    def __init__(
        self,
        method: str = None,
        body_flag: str = None,
        body_type: str = None,
        normal_param_list: List[CreateAPIDefinitionApiDefineParamLimitNormalAddDTO] = None,
        form_param_list: List[CreateAPIDefinitionApiDefineParamLimitFormAddDTO] = None,
        json_param: CreateAPIDefinitionApiDefineParamLimitJsonAddDTO = None,
    ):
        # {'en':'Request methods.
        # GET:GET
        # POST:POST
        # DELETE:DELETE
        # PUT:PUT
        # HEAD:HEAD
        # OPTIONS:OPTIONS
        # PATCH:PATCH', 'zh_CN':'请求方法。
        # GET：GET
        # POST：POST
        # DELETE：DELETE
        # PUT：PUT
        # HEAD：HEAD
        # OPTIONS：OPTIONS
        # PATCH：PATCH'}
        self.method = method
        # {'en':'Whether to define body parameters, required when method = POST/PUT/PATCH.
        # TRUE:Yes
        # FALSE:No', 'zh_CN':'是否定义body参数，method = POST/PUT/PATCH时必填。
        # TRUE：是
        # FALSE：否'}
        self.body_flag = body_flag
        # {'en':'Body parameter type, required when bodyFlag = TRUE.
        # JSON:JSON
        # FROM:FROM', 'zh_CN':'body参数类型，bodyFlag = TRUE 时必填。
        # JSON：JSON
        # FROM：FROM表单'}
        self.body_type = body_type
        # {'en':'Normal parameter list.', 'zh_CN':'普通参数数组。'}
        self.normal_param_list = normal_param_list
        # {'en':'FROM form parameter array, Optional when bodyType = FROM.', 'zh_CN':'FROM 表单参数数组，bodyType = FROM 时选填。'}
        self.form_param_list = form_param_list
        # {'en':'JSON parameter array, Optional when bodyType = JSON.', 'zh_CN':'JSON参数数组，bodyType = JSON 时选填。'}
        self.json_param = json_param

    def validate(self):
        if self.normal_param_list:
            for k in self.normal_param_list:
                if k:
                    k.validate()
        if self.form_param_list:
            for k in self.form_param_list:
                if k:
                    k.validate()
        if self.json_param:
            self.json_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method is not None:
            result['method'] = self.method
        if self.body_flag is not None:
            result['bodyFlag'] = self.body_flag
        if self.body_type is not None:
            result['bodyType'] = self.body_type
        if self.normal_param_list is not None:
            result['normalParamList'] = []
            for k in self.normal_param_list:
                result['normalParamList'].append(k.to_map() if k else None)
        if self.form_param_list is not None:
            result['formParamList'] = []
            for k in self.form_param_list:
                result['formParamList'].append(k.to_map() if k else None)
        if self.json_param is not None:
            result['jsonParam'] = self.json_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('bodyFlag') is not None:
            self.body_flag = m.get('bodyFlag')
        if m.get('bodyType') is not None:
            self.body_type = m.get('bodyType')
        if m.get('normalParamList') is not None:
            self.normal_param_list = []
            for k in m.get('normalParamList'):
                temp_model = CreateAPIDefinitionApiDefineParamLimitNormalAddDTO()
                self.normal_param_list.append(temp_model.from_map(k))
        if m.get('formParamList') is not None:
            self.form_param_list = []
            for k in m.get('formParamList'):
                temp_model = CreateAPIDefinitionApiDefineParamLimitFormAddDTO()
                self.form_param_list.append(temp_model.from_map(k))
        if m.get('jsonParam') is not None:
            temp_model = CreateAPIDefinitionApiDefineParamLimitJsonAddDTO()
            self.json_param = temp_model.from_map(m['jsonParam'])
        return self


class CreateAPIDefinitionApiDefineParamLimitAddDTO(TeaModel):
    def __init__(
        self,
        basic: CreateAPIDefinitionApiDefineParamLimitBasicAddDTO = None,
        method_list: List[CreateAPIDefinitionApiDefineParamLimitMethodAddDTO] = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'Method attributes.', 'zh_CN':'方法属性。'}
        self.method_list = method_list

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        if self.method_list:
            for k in self.method_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.method_list is not None:
            result['methodList'] = []
            for k in self.method_list:
                result['methodList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = CreateAPIDefinitionApiDefineParamLimitBasicAddDTO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('methodList') is not None:
            self.method_list = []
            for k in m.get('methodList'):
                temp_model = CreateAPIDefinitionApiDefineParamLimitMethodAddDTO()
                self.method_list.append(temp_model.from_map(k))
        return self


class CreateAPIDefinitionRequest(TeaModel):
    def __init__(
        self,
        basic: CreateAPIDefinitionApiDefineBasicAddDTO = None,
        endpoint: CreateAPIDefinitionApiDefineEndpointAddDTO = None,
        auth: CreateAPIDefinitionApiDefineAuthAddDTO = None,
        body_limit: CreateAPIDefinitionApiDefineBodyLimitAddDTO = None,
        param_limit: CreateAPIDefinitionApiDefineParamLimitAddDTO = None,
    ):
        # {'en':'Basic information.', 'zh_CN':'基础信息。'}
        self.basic = basic
        # {'en':'Endpoint information.', 'zh_CN':'端点信息。'}
        self.endpoint = endpoint
        # {'en':'Authentication configuration.', 'zh_CN':'鉴权配置。'}
        self.auth = auth
        # {'en':'Body restrictions.', 'zh_CN':'body限制。'}
        self.body_limit = body_limit
        # {'en':'Parameter limit.', 'zh_CN':'参数限制。'}
        self.param_limit = param_limit

    def validate(self):
        self.validate_required(self.basic, 'basic')
        if self.basic:
            self.basic.validate()
        self.validate_required(self.endpoint, 'endpoint')
        if self.endpoint:
            self.endpoint.validate()
        self.validate_required(self.auth, 'auth')
        if self.auth:
            self.auth.validate()
        if self.body_limit:
            self.body_limit.validate()
        if self.param_limit:
            self.param_limit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['basic'] = self.basic.to_map()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint.to_map()
        if self.auth is not None:
            result['auth'] = self.auth.to_map()
        if self.body_limit is not None:
            result['bodyLimit'] = self.body_limit.to_map()
        if self.param_limit is not None:
            result['paramLimit'] = self.param_limit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = CreateAPIDefinitionApiDefineBasicAddDTO()
            self.basic = temp_model.from_map(m['basic'])
        if m.get('endpoint') is not None:
            temp_model = CreateAPIDefinitionApiDefineEndpointAddDTO()
            self.endpoint = temp_model.from_map(m['endpoint'])
        if m.get('auth') is not None:
            temp_model = CreateAPIDefinitionApiDefineAuthAddDTO()
            self.auth = temp_model.from_map(m['auth'])
        if m.get('bodyLimit') is not None:
            temp_model = CreateAPIDefinitionApiDefineBodyLimitAddDTO()
            self.body_limit = temp_model.from_map(m['bodyLimit'])
        if m.get('paramLimit') is not None:
            temp_model = CreateAPIDefinitionApiDefineParamLimitAddDTO()
            self.param_limit = temp_model.from_map(m['paramLimit'])
        return self


class CreateAPIDefinitionResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: str = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'API definition ID.', 'zh_CN':'API定义ID。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateAPIDefinitionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPIDefinitionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPIDefinitionRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class CreateAPIDefinitionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListAPIDefinitionsRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        name_list: List[str] = None,
        group_name_list: List[str] = None,
        desc: bool = None,
    ):
        # {'en':'Hostname array, by default all valid hostnames.', 'zh_CN':'域名数组，默认所有生效域名。'}
        self.domain_list = domain_list
        # {'en':'API name array.', 'zh_CN':'API名称数组。'}
        self.name_list = name_list
        # {'en':'API grouped array.', 'zh_CN':'API分组数组。'}
        self.group_name_list = group_name_list
        # {'en':'Sorting method, reverse order by default.
        # true: Modify time in reverse order
        # false: Modify time sequence', 'zh_CN':'排序方式，默认倒序。
        # true：修改时间倒序
        # false：修改时间正序'}
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.name_list is not None:
            result['nameList'] = self.name_list
        if self.group_name_list is not None:
            result['groupNameList'] = self.group_name_list
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')
        if m.get('groupNameList') is not None:
            self.group_name_list = m.get('groupNameList')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self


class ListAPIDefinitionsApiDefineBasicVO(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        group_name: str = None,
        remark: str = None,
        domain: str = None,
        path: str = None,
        create_time: str = None,
        update_time: str = None,
    ):
        # {'en':'API definition ID.', 'zh_CN':'API定义ID。'}
        self.id = id
        # {'en':'API name.', 'zh_CN':'API名称。'}
        self.name = name
        # {'en':'API groups.', 'zh_CN':'API分组。'}
        self.group_name = group_name
        # {'en':'Description.', 'zh_CN':'备注。'}
        self.remark = remark
        # {'en':'Attributed hostname.', 'zh_CN':'归属域名。'}
        self.domain = domain
        # {'en':'API base path.', 'zh_CN':'端点路径。'}
        self.path = path
        # {'en':'Creation time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'创建时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.create_time = create_time
        # {'en':'Update time, format: yyyy-MM-dd HH:mm:ss.', 'zh_CN':'更新时间，格式：yyyy-MM-dd HH:mm:ss。'}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.path, 'path')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.domain is not None:
            result['domain'] = self.domain
        if self.path is not None:
            result['path'] = self.path
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListAPIDefinitionsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: List[ListAPIDefinitionsApiDefineBasicVO] = None,
    ):
        # {'en':'Please refer to the error code for exceptions.', 'zh_CN':'请参照错误码。','dictionary':'belong=WAAP-MS-Ext|dict=waap_retCodeEnum'}
        self.code = code
        # {'en':'Description.', 'zh_CN':'描述信息。'}
        self.msg = msg
        # {'en':'Data.', 'zh_CN':'出参数据。'}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = ListAPIDefinitionsApiDefineBasicVO()
                self.data.append(temp_model.from_map(k))
        return self


class ListAPIDefinitionsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListAPIDefinitionsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListAPIDefinitionsRequestHeader(TeaModel):
    def __init__(
        self,
        service_type: str = None,
    ):
        # {"zh_CN":"安全服务类型。有使用多个不同的安全服务时，需要填写具体的服务类型。","en":"Security service type. Please enter a specific service type, if you purchase multiple security services.","dictionary":"belong=WAAP-MS-Ext|dict=waap_serviceType"}
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class ListAPIDefinitionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




