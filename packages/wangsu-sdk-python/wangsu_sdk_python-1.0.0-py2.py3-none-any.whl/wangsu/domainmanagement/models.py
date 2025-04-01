# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AddDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        language: str = None,
    ):
        # {"en":"Added domain
        # Use English half-width
        # semicolon between
        # two domains if there
        # are multiple to be
        # added.", "zh_CN":"添加的域名
        # 如果添加多个域名，用英文半角分号分隔。"}
        self.domain_name = domain_name
        # {"en":"Return Chinese results for null (default)
        # En: Return the English prompt result", "zh_CN":"为空返回中文结果(默认)
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
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class AddDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code. For detailed description of resCode, please refer to 'Status Codes of Dispatch Business'.", "zh_CN":"状态码，详细说明请参见“业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"recordId, ID of host name record, used to identify this record.", "zh_CN":"域名的详细说明。"}
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


class AddDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateCustomerAnycastIPRecordStatusRequest(TeaModel):
    def __init__(
        self,
        ips: List[str] = None,
        record_status: str = None,
    ):
        # {"en":"Ip list", "zh_CN":"ip 列表"}
        self.ips = ips
        # {"en":"Record Status, For example, lock or unlock; data of length 1 or 2 can be passed.", "zh_CN":"记录状态，例如锁定、非锁定等，可以传长度为1或2的数据"}
        self.record_status = record_status

    def validate(self):
        self.validate_required(self.ips, 'ips')
        self.validate_required(self.record_status, 'record_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ips is not None:
            result['ips'] = self.ips
        if self.record_status is not None:
            result['recordStatus'] = self.record_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('recordStatus') is not None:
            self.record_status = m.get('recordStatus')
        return self


class UpdateCustomerAnycastIPRecordStatusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"The error code that appears when the HTTP status is not 202, indicating the type of error for the current request.", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, when success is successful", "zh_CN":"响应信息，成功时为success"}
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


class UpdateCustomerAnycastIPRecordStatusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateCustomerAnycastIPRecordStatusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateCustomerAnycastIPRecordStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateCustomerAnycastIPRecordStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteCdnDomainServiceRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
    ):
        # {"en":"Accelerate the ID of the domain name in the system
        # Note:
        # 1. See the url in the request example, 123344 for domainId
        # 2. After the domain name is successfully submitted, the location access url in the return parameter can be queried to the domainId of the domain name; You can also query domainId through the Get domain Configuration and Get domain List interfaces", "zh_CN":"加速域名在系统中对应的ID
        # 注意：
        # 1、参看请求示例中的url，123344对应的就是domainId
        # 2、创建域名成功提交后，返回参数中的location访问url中，能够查询到域名对应的domainId；也可以通过【获取域名配置】和【获取域名列表】接口查询到domainId"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class DeleteCdnDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class DeleteCdnDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # {"en":"", "zh_CN":"域名名称或域名id，在请求的url后面"}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        return self


class DeleteCdnDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCdnDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCdnDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PreDeployChangeServerConfigRequestChangeServers(TeaModel):
    def __init__(
        self,
        target_server: str = None,
        data_id: int = None,
    ):
        # {"en":"If it is a universal domain name, set it to a universal domain name, for example, *.56.com.", "zh_CN":"如果是泛域名，需要填写为泛域名，例如：*.56.com"}
        self.target_server = target_server
        # {"en":"Data-id is to indicate a specific group configuration when the client has multiple groups of configurations. Data-id can be retrieved through a query interface. Note: 
        # A. If data-id is passed, it means that one group of configuration items is specified to be modified, and no other group configuration items need to be modified. 
        # B. If multiple groups of configurations are included, some of them are configured with data-id and others are not, then the expression of data-id is used to modify a specific group of configurations, and a new group of configurations is added on the original basis without the expression of data-id. 
        # C. If the data-id is not transmitted, it means that the original configuration will be fully covered by this configuration. 
        # D. If no configuration parameter is passed, only domain name and secondary label are passed, which means that all configuration of domain name secondary service corresponding to this interface is cleared. 
        # E. If there is no specific configuration item in a set of configurations, the data-id must be filled in, and the value is the actual data-id, which means clearing the value of the corresponding data-id configuration item; it is not allowed that there is no specific configuration item or data-id in a set of configurations.", 
        #       "zh_CN":"配置多组配置时，具体某组配置的id。dataId可以通过查询接口获取。 注意： 
        # a、如果有传dataId，说明指定修改其中一组配置项内容，不需求修改其他组配置内容不需要入参； 
        # b、如果入参多组配置，其中有些组配置有传dataId，有些没有传，则有传dataId的表示修改具体某组配置，没有传dataId的表示在原来基础上新增一组配置； 
        # c、如果入参都没有传dataId,表示用本次的配置全量覆盖原先配置； d、如果入参没有传任何配置项参数，只传了域名和二级标签，表示清空这个接口对应域名二级服务所有配置； 
        # e、如果一组配置没有具体的配置项，则dataId必填，且值为实际存在的dataId，表示清空这个dataId对应配置项的值；不允许一组配置没有具体的配置项也没有dataId。
        # "}
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_server is not None:
            result['target-server'] = self.target_server
        if self.data_id is not None:
            result['dataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('target-server') is not None:
            self.target_server = m.get('target-server')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        return self


class PreDeployChangeServerConfigRequest(TeaModel):
    def __init__(
        self,
        change_servers: List[PreDeployChangeServerConfigRequestChangeServers] = None,
    ):
        # {"en":"Change servers configuration, parent tag
        # 1. This must be filled when the hotlinking configuration of streaming media needs to be set
        # 2. Empty the configuration for <change-servers/>", "zh_CN":"【接入域名跳转】
        # 注意：
        # 1、需要取消【接入域名跳转】时，可以传入空节点<change-servers></change-servers>。
        # 2、表示需要设置【接入域名跳转】，此项必填"}
        self.change_servers = change_servers

    def validate(self):
        self.validate_required(self.change_servers, 'change_servers')
        if self.change_servers:
            for k in self.change_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_servers is not None:
            result['change-servers'] = []
            for k in self.change_servers:
                result['change-servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change-servers') is not None:
            self.change_servers = []
            for k in m.get('change-servers'):
                temp_model = PreDeployChangeServerConfigRequestChangeServers()
                self.change_servers.append(temp_model.from_map(k))
        return self


class PreDeployChangeServerConfigResponseData(TeaModel):
    def __init__(
        self,
        pre_deploy_id: str = None,
    ):
        # {"en":"The preliminary deployment id", "zh_CN":"预部署id"}
        self.pre_deploy_id = pre_deploy_id

    def validate(self):
        self.validate_required(self.pre_deploy_id, 'pre_deploy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_deploy_id is not None:
            result['preDeployId'] = self.pre_deploy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preDeployId') is not None:
            self.pre_deploy_id = m.get('preDeployId')
        return self


class PreDeployChangeServerConfigResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: PreDeployChangeServerConfigResponseData = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"The error code", "zh_CN":"错误码"}
        self.code = code
        # {"en":"The message body", "zh_CN":"消息体"}
        self.message = message
        # {"en":"Returns the body of the data.", "zh_CN":"返回数据体"}
        self.data = data
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

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
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = PreDeployChangeServerConfigResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class PreDeployChangeServerConfigPaths(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"The domain whoes need query config.", "zh_CN":"需要查询配置的域名或域名id"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class PreDeployChangeServerConfigParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PreDeployChangeServerConfigRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PreDeployChangeServerConfigResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddDomainGroupRequest(TeaModel):
    def __init__(
        self,
        domain_group_name: str = None,
        service_type: str = None,
        domain_list: List[str] = None,
    ):
        # {"en":"	Domain group name. Only Chinese characters/English alphabet/numbers/underscores are supported, and case insensitive.Up to 32 characters.", "zh_CN":"域名组名称，仅支持输入中文/英文/数字/下划线，不区分大小写，最多可传32个字符。"}
        self.domain_group_name = domain_group_name
        # {"en":"The serviceType that the domain group belongs to.", "zh_CN":"域名组所属加速服务类型"}
        self.service_type = service_type
        # {"en":"Domains associated with domain group.The domain needs to be under the serviceType.", "zh_CN":"域名组关联的域名，域名需要是传入加速服务类型下的域名"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_group_name, 'domain_group_name')
        self.validate_required(self.service_type, 'service_type')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_group_name is not None:
            result['domainGroupName'] = self.domain_group_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainGroupName') is not None:
            self.domain_group_name = m.get('domainGroupName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class AddDomainGroupResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"错误具体状态码"}
        self.code = code
        # {"en":"Message", "zh_CN":"消息提示"}
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


class AddDomainGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDomainGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainByOriginIPRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainByOriginIPResponse(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        x_cnc_request_id: str = None,
        code: int = None,
        originip: str = None,
        domain_list: List[str] = None,
    ):
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id
        # {"en":"Code =200 indicates that relevant data was returned successfully", "zh_CN":"code=200，表示成功返回相关数据"}
        self.code = code
        # {"en":"Query the source station IP", "zh_CN":"查询的源站IP"}
        self.originip = originip
        # {"en":"Returns a list of domain name names corresponding to each source station IP", "zh_CN":"返回各个源站IP对应的域名名称列表"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.originip, 'originip')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        if self.code is not None:
            result['code'] = self.code
        if self.originip is not None:
            result['originip'] = self.originip
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('originip') is not None:
            self.originip = m.get('originip')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class QueryDomainByOriginIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainByOriginIPParameters(TeaModel):
    def __init__(
        self,
        originip: str = None,
    ):
        # {"en":"Source station IP, multiple IPs separated by semicolons", "zh_CN":"源站IP，多个IP用分号隔开
        # 注意：
        # 1、每次查询最多只能传入10个源站IP
        # 2、不支持源站域名的查询
        # 3、高级源匹配到对应IP时也能查到对应域名"}
        self.originip = originip

    def validate(self):
        self.validate_required(self.originip, 'originip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.originip is not None:
            result['originip'] = self.originip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originip') is not None:
            self.originip = m.get('originip')
        return self


class QueryDomainByOriginIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainByOriginIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        domain_name: str = None,
    ):
        # {"en":"Return Chinese results for null (default)
        # En: Return the English prompt result", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language
        # {"en":"Deleted domains
        # Use English half-width
        # semicolon between
        # two domains if there
        # are multiple to be
        # deleted.", "zh_CN":"删除的域名
        # 如果需要删除多个域名，用英文半角分号分隔。"}
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"For more details of status
        # codes resCode, please refer to
        # “Status Codes of Dispatch
        # Business”.", "zh_CN":"状态码，resCode的详细说明请参见附录6： 业务状态码。"}
        self.res_code = res_code
        # {"en":"Detailed description of the
        # status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"Detailed description of the
        # domain.
        # domainId Domain ID
        # domainName Domain name
        # ret Succeed or Fail tag
        # msg Succeed or Fail
        # messages
        # msgEn Succeed or Fail
        # messages", "zh_CN":"域名的详细说明。
        #   domainId 域名ID
        #   domainName 域名名称
        #   ret 成功或失败标识
        #   msg 成功或失败提示
        #   msgEn 成功或失败提示"}
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


class DeleteDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditDomainGroupRequest(TeaModel):
    def __init__(
        self,
        domain_group_id: str = None,
        domain_group_name: str = None,
        service_type: str = None,
        domain_list: List[str] = None,
    ):
        # {"en":"domain group ID", "zh_CN":"域名组ID"}
        self.domain_group_id = domain_group_id
        # {"en":"Domain group name. Only Chinese characters/English alphabet/numbers/underscores are supported, and case insensitive.Up to 32 characters.", "zh_CN":"域名组名称，仅支持输入中文/英文/数字/下划线，不区分大小写，最多可传32个字符。"}
        self.domain_group_name = domain_group_name
        # {"en":"The serviceType that the domain group belongs to", "zh_CN":"域名组所属加速服务类型"}
        self.service_type = service_type
        # {"en":"Domains associated with domain group The domain needs to be under the serviceType", "zh_CN":"域名组关联的域名,域名需要是传入加速服务类型下的域名"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_group_id, 'domain_group_id')
        self.validate_required(self.domain_group_name, 'domain_group_name')
        self.validate_required(self.service_type, 'service_type')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_group_id is not None:
            result['domainGroupId'] = self.domain_group_id
        if self.domain_group_name is not None:
            result['domainGroupName'] = self.domain_group_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainGroupId') is not None:
            self.domain_group_id = m.get('domainGroupId')
        if m.get('domainGroupName') is not None:
            self.domain_group_name = m.get('domainGroupName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class EditDomainGroupResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status Code", "zh_CN":"错误具体状态码"}
        self.code = code
        # {"en":"Message", "zh_CN":"消息提示"}
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


class EditDomainGroupPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDomainGroupParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDomainGroupRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditDomainGroupResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelAcceTypeRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        startdate: str = None,
        enddate: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM若没有输入时、分，则时分默认为00:01；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM,若没有输入时、分，则时分默认为24:00；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class ChannelAcceTypeResponseProviderAccountAcceTypeChannel(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.text = text

    def validate(self):
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class ChannelAcceTypeResponseProviderAccountAcceType(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        channel: List[ChannelAcceTypeResponseProviderAccountAcceTypeChannel] = None,
    ):
        # {'en':'name', 'zh_CN':'加速类型'}
        self.name = name
        # {'en':'value', 'zh_CN':'加速类型值'}
        self.value = value
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.value, 'value')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            for k in self.channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.channel is not None:
            result['channel'] = []
            for k in self.channel:
                result['channel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('channel') is not None:
            self.channel = []
            for k in m.get('channel'):
                temp_model = ChannelAcceTypeResponseProviderAccountAcceTypeChannel()
                self.channel.append(temp_model.from_map(k))
        return self


class ChannelAcceTypeResponseProviderAccount(TeaModel):
    def __init__(
        self,
        login_name: str = None,
        acce_type: ChannelAcceTypeResponseProviderAccountAcceType = None,
    ):
        # {'en':'login-name', 'zh_CN':'日期'}
        self.login_name = login_name
        # {'en':'acce-type', 'zh_CN':'频道'}
        self.acce_type = acce_type

    def validate(self):
        self.validate_required(self.login_name, 'login_name')
        self.validate_required(self.acce_type, 'acce_type')
        if self.acce_type:
            self.acce_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_name is not None:
            result['login-name'] = self.login_name
        if self.acce_type is not None:
            result['acce-type'] = self.acce_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('login-name') is not None:
            self.login_name = m.get('login-name')
        if m.get('acce-type') is not None:
            temp_model = ChannelAcceTypeResponseProviderAccountAcceType()
            self.acce_type = temp_model.from_map(m['acce-type'])
        return self


class ChannelAcceTypeResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        account: ChannelAcceTypeResponseProviderAccount = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'account', 'zh_CN':'账号数据'}
        self.account = account

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.account, 'account')
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.account is not None:
            result['account'] = self.account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('account') is not None:
            temp_model = ChannelAcceTypeResponseProviderAccount()
            self.account = temp_model.from_map(m['account'])
        return self


class ChannelAcceTypeResponse(TeaModel):
    def __init__(
        self,
        provider: ChannelAcceTypeResponseProvider = None,
    ):
        # {'en':'provider', 'zh_CN':'结果'}
        self.provider = provider

    def validate(self):
        self.validate_required(self.provider, 'provider')
        if self.provider:
            self.provider.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider is not None:
            result['provider'] = self.provider.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            temp_model = ChannelAcceTypeResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class ChannelAcceTypePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelAcceTypeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelAcceTypeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelAcceTypeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CancelApiDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelApiDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class CancelApiDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"", "zh_CN":"加速域名在系统中对应的ID
        # 1. 参看请求示例中的url，123344对应的就是domain-id
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class CancelApiDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelApiDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelApiDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EnableSingleDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableSingleDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class EnableSingleDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"Accelerate the ID of the domain name in the system
        # Note:
        # 1. See the url in the request example, 123344 for domain-id
        # 2. After the domain name is successfully submitted, the location access url in the return parameter can be queried to the domain-id of the domain name; You can also query domain-id through the Get domain Configuration and Get domain List interfaces", "zh_CN":"加速域名在系统中对应的ID
        # 注意：
        # 1. 参看请求示例中的url，123344对应的就是domain-id
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class EnableSingleDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableSingleDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableSingleDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EnableDisableHwDomainRequest(TeaModel):
    def __init__(
        self,
        state: str = None,
    ):
        # {"en":"state.online/offline", "zh_CN":"状态.online：启用.offline：停用。"}
        self.state = state

    def validate(self):
        self.validate_required(self.state, 'state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class EnableDisableHwDomainResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"task id.", "zh_CN":"任务id"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class EnableDisableHwDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: EnableDisableHwDomainResponseData = None,
        x_request_id: str = None,
    ):
        # {"en":"The error code, when HTTPStatus is not 201, indicates the type of error the current request is calling.", "zh_CN":"错误代码，当HTTPStatus不为201时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, when success is successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"The response data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_request_id = x_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.x_request_id, 'x_request_id')

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
        if self.x_request_id is not None:
            result['X-Request-Id'] = self.x_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = EnableDisableHwDomainResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('X-Request-Id') is not None:
            self.x_request_id = m.get('X-Request-Id')
        return self


class EnableDisableHwDomainPaths(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"The domain name for the acceleration domain to be deleted", "zh_CN":"要删除的域名"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class EnableDisableHwDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableDisableHwDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableDisableHwDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisableCdnDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableCdnDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class DisableCdnDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"", "zh_CN":"加速域名在系统中对应的ID
        # 1. 参看请求示例中的url，123344对应的就是domainId
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domainId"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class DisableCdnDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableCdnDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableCdnDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisableSingleDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableSingleDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class DisableSingleDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"", "zh_CN":"加速域名在系统中对应的ID
        # 1. 参看请求示例中的url，123344对应的就是domain-id
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class DisableSingleDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableSingleDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisableSingleDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteApiDomainServiceRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_id: str = None,
    ):
        # {"en":"Accelerated domain name, choose one from domain-id. Accelerate the ID of the domain name in the system
        # Note:
        # 1. See the url in the request example, 123344 for domain-id
        # 2、After the domain name is successfully submitted, the location access url in the return parameter can be queried to the domain-id of the domain name; You can also query domain-id through the Get domain Configuration and Get domain List interfaces", "zh_CN":"加速域名与domain-id二选一。
        # domain-id：加速域名在系统中对应的ID
        # domain-name：加速的域名
        # 注意：
        # 1、参看请求示例中的url，123344对应的就是domain-id
        # 2、创建域名成功提交后，返回参数中的location访问url中，能够查询到域名对应的domain-id；也可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_name = domain_name
        # {"en":"Accelerated domain name, choose one from domain-id. Accelerate the ID of the domain name in the system
        # Note:
        # 1. See the url in the request example, 123344 for domain-id
        # 2、After the domain name is successfully submitted, the location access url in the return parameter can be queried to the domain-id of the domain name; You can also query domain-id through the Get domain Configuration and Get domain List interfaces", "zh_CN":"加速域名与domain-id二选一。
        # domain-id：加速域名在系统中对应的ID
        # domain-name：加速的域名
        # 注意：
        # 1、参看请求示例中的url，123344对应的就是domain-id
        # 2、创建域名成功提交后，返回参数中的location访问url中，能够查询到域名对应的domain-id；也可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class DeleteApiDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class DeleteApiDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # {"en":"", "zh_CN":"域名名称或域名id，在请求的url后面"}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        return self


class DeleteApiDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteApiDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteApiDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteHwDomainRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHwDomainResponseData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"task id.", "zh_CN":"任务id"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class DeleteHwDomainResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: DeleteHwDomainResponseData = None,
        x_request_id: str = None,
    ):
        # {"en":"The error code, when HTTPStatus is not 201, indicates the type of error the current request is calling.", "zh_CN":"错误代码，当HTTPStatus不为201时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, when success is successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"The response data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_request_id = x_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.x_request_id, 'x_request_id')

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
        if self.x_request_id is not None:
            result['X-Request-Id'] = self.x_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = DeleteHwDomainResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('X-Request-Id') is not None:
            self.x_request_id = m.get('X-Request-Id')
        return self


class DeleteHwDomainPaths(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"The domain name for the acceleration domain to be deleted", "zh_CN":"要删除的域名"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class DeleteHwDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHwDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHwDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EnableCdnDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableCdnDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class EnableCdnDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"Accelerate the ID of the domain name in the system
        # Note:
        # 1. See the url in the request example, 123344 for domainId
        # 2. After the domain name is successfully submitted, the location access url in the return parameter can be queried to the domainId of the domain name; You can also query domainId through the Get domain Configuration and Get domain List interfaces", "zh_CN":"加速域名在系统中对应的ID
        # 注意：
        # 1. 参看请求示例中的url，123344对应的就是domainId
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domainId"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class EnableCdnDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableCdnDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableCdnDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateChangeServerRequestChangeServers(TeaModel):
    def __init__(
        self,
        target_server: str = None,
        data_id: int = None,
    ):
        # {"en":"If it is a universal domain name, set it to a universal domain name, for example, *.56.com.", "zh_CN":"如果是泛域名，需要填写为泛域名，例如：*.56.com"}
        self.target_server = target_server
        # {"en":"Data-id is to indicate a specific group configuration when the client has multiple groups of configurations. Data-id can be retrieved through a query interface. Note: 
        # A. If data-id is passed, it means that one group of configuration items is specified to be modified, and no other group configuration items need to be modified. 
        # B. If multiple groups of configurations are included, some of them are configured with data-id and others are not, then the expression of data-id is used to modify a specific group of configurations, and a new group of configurations is added on the original basis without the expression of data-id. 
        # C. If the data-id is not transmitted, it means that the original configuration will be fully covered by this configuration. 
        # D. If no configuration parameter is passed, only domain name and secondary label are passed, which means that all configuration of domain name secondary service corresponding to this interface is cleared. 
        # E. If there is no specific configuration item in a set of configurations, the data-id must be filled in, and the value is the actual data-id, which means clearing the value of the corresponding data-id configuration item; it is not allowed that there is no specific configuration item or data-id in a set of configurations.", 
        #       "zh_CN":"配置多组配置时，具体某组配置的id。dataId可以通过查询接口获取。 注意： 
        # a、如果有传dataId，说明指定修改其中一组配置项内容，不需求修改其他组配置内容不需要入参； 
        # b、如果入参多组配置，其中有些组配置有传dataId，有些没有传，则有传dataId的表示修改具体某组配置，没有传dataId的表示在原来基础上新增一组配置； 
        # c、如果入参都没有传dataId,表示用本次的配置全量覆盖原先配置； 
        # d、如果入参没有传任何配置项参数，只传了域名和二级标签，表示清空这个接口对应域名二级服务所有配置； 
        # e、如果一组配置没有具体的配置项，则dataId必填，且值为实际存在的dataId，表示清空这个dataId对应配置项的值；不允许一组配置没有具体的配置项也没有dataId。
        # "}
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_server is not None:
            result['target-server'] = self.target_server
        if self.data_id is not None:
            result['dataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('target-server') is not None:
            self.target_server = m.get('target-server')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        return self


class UpdateChangeServerRequest(TeaModel):
    def __init__(
        self,
        change_servers: List[UpdateChangeServerRequestChangeServers] = None,
    ):
        # {"en":"Change servers configuration, parent tag
        # 1. This must be filled when the hotlinking configuration of streaming media needs to be set
        # 2. Empty the configuration for <change-servers/>", "zh_CN":"【接入域名跳转】
        # 注意：
        # 1、需要取消【接入域名跳转】时，可以传入空节点<change-servers></change-servers>。
        # 2、表示需要设置【接入域名跳转】，此项必填"}
        self.change_servers = change_servers

    def validate(self):
        self.validate_required(self.change_servers, 'change_servers')
        if self.change_servers:
            for k in self.change_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_servers is not None:
            result['change-servers'] = []
            for k in self.change_servers:
                result['change-servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change-servers') is not None:
            self.change_servers = []
            for k in m.get('change-servers'):
                temp_model = UpdateChangeServerRequestChangeServers()
                self.change_servers.append(temp_model.from_map(k))
        return self


class UpdateChangeServerResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"The error code", "zh_CN":"错误码"}
        self.code = code
        # {"en":"The message body", "zh_CN":"消息体"}
        self.message = message
        # {"en":"Returns the body of the data.", "zh_CN":"返回数据体。"}
        self.data = data
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

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
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class UpdateChangeServerPaths(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # {"en":"The domain whoes need query config.", "zh_CN":"需要查询配置的域名或域名id"}
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        return self


class UpdateChangeServerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateChangeServerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateChangeServerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateDispatchDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_id: int = None,
        dispatch_zone: str = None,
        ttl: int = None,
        domain_desc: str = None,
        session_hold: int = None,
        session_interval: int = None,
        language: str = None,
    ):
        # {"en":"domainName", "zh_CN":"域名"}
        self.domain_name = domain_name
        # {"en":"domainId", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"dispatchZone", "zh_CN":"可选，国内：cdngtm.cn， 海外：cdngtm.com；默认值为cdngtm.com"}
        self.dispatch_zone = dispatch_zone
        # {"en":"ttl", "zh_CN":"默认值为10，不得低于10，否则返回解析记录TTL错误提示。"}
        self.ttl = ttl
        # {"en":"Desc", "zh_CN":"备注"}
        self.domain_desc = domain_desc
        # {"en":"sessionHold", "zh_CN":"1：开启  空为不开启"}
        self.session_hold = session_hold
        # {"en":"sessionInterval", "zh_CN":"保持时间"}
        self.session_interval = session_interval
        # {"en":"language", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.dispatch_zone, 'dispatch_zone')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.dispatch_zone is not None:
            result['dispatchZone'] = self.dispatch_zone
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.domain_desc is not None:
            result['domainDesc'] = self.domain_desc
        if self.session_hold is not None:
            result['sessionHold'] = self.session_hold
        if self.session_interval is not None:
            result['sessionInterval'] = self.session_interval
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('dispatchZone') is not None:
            self.dispatch_zone = m.get('dispatchZone')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('domainDesc') is not None:
            self.domain_desc = m.get('domainDesc')
        if m.get('sessionHold') is not None:
            self.session_hold = m.get('sessionHold')
        if m.get('sessionInterval') is not None:
            self.session_interval = m.get('sessionInterval')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class UpdateDispatchDomainResponse(TeaModel):
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


class UpdateDispatchDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateDispatchDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateDispatchDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateDispatchDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetFuzzyPagingDomainListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
        domain_name: List[str] = None,
        query_type: str = None,
        start_time: str = None,
        end_time: str = None,
        domain_status: str = None,
    ):
        # {"en":"Page number must be a positive integer greater than 0", "zh_CN":"分页的页码，必须为大于0的正整数"}
        self.page_number = page_number
        # {"en":"Number of domain name data items for paging, must be a positive integer greater than 0", "zh_CN":"分页的域名数据条数，必须大于0的正整数"}
        self.page_size = page_size
        # {"en":"Specifies the service type of the query, only one type per query, and no default lookup for all types", "zh_CN":"指定查询的服务类型，每次查询只能传一个类型，不传默认查全部类型"}
        self.service_type = service_type
        # {"en":"Specifies the accelerated domain name for the query, allows multiple domains, commas delimited, and no default lookup of all domain names", "zh_CN":"指定查询的加速域名，允许多个域名，逗号分隔，不传默认查全部域名"}
        self.domain_name = domain_name
        # {"en":"Query to accelerated domain name, optional value is: fuzzy_match for fuzzy query; Full_match represents an exact query
        # No fuzzy_match by default, for accelerated domain name only", "zh_CN":"查询加速域名的方式，可选值为：fuzzy_match表示模糊查询；full_match表示精确查询
        # 不传默认为fuzzy_match，仅针对加速域名"}
        self.query_type = query_type
        # {"en":"Query start time, support for years, months, days, hours, minutes, and seconds, for example: 20170101.09 million. Time equals", "zh_CN":"查询开始时间，支持范围为年月日时分秒，例如：20170101090000。时间含等于"}
        self.start_time = start_time
        # {"en":"Query end time, query time within the existence of the accelerated domain name, time is equal to, do not pass the default query all", "zh_CN":"查询结束时间，查询时间段内存在的加速域名，时间含等于，不传默认查询所有"}
        self.end_time = end_time
        # {"en":"Accelerate the status of the domain name, enabled indicates that it is in effect; Disabled indicates that it is Disabled; Deploying means in the process of deployment; Checking indicates that the audit is in progress; Disabling: Indicates disabled, no default lookup for all", "zh_CN":"加速域名的状态，enabled表示已生效；disabled表示已禁用；deploying表示部署中；checking表示审核中；disabling:表示禁用中，不传默认查全部"}
        self.domain_status = domain_status

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.domain_status is not None:
            result['domainStatus'] = self.domain_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('domainStatus') is not None:
            self.domain_status = m.get('domainStatus')
        return self


class GetFuzzyPagingDomainListResponseResultList(TeaModel):
    def __init__(
        self,
        cname: str = None,
        config_form_name: str = None,
        create_time: str = None,
        domain_id: str = None,
        domain_name: str = None,
        operator: str = None,
        origin_ips: str = None,
        service_type: str = None,
        domain_status: str = None,
        deploy_version: str = None,
        cdn_service_status: str = None,
        is_enabled: str = None,
    ):
        # {"en":"Accelerated domain CNAME corresponding to CNAME, for example: 7nt6mrh7sdkslj.cdn30.com", "zh_CN":"加速域名对应的CNAME域名，例如：7nt6mrh7sdkslj.cdn30.com"}
        self.cname = cname
        # {"en":"Configuration name", "zh_CN":"配置单名称"}
        self.config_form_name = config_form_name
        # {"en":"The time format is: 20160323112310", "zh_CN":"时间格式为：20160323112310"}
        self.create_time = create_time
        # {"en":"Corresponding domain ID", "zh_CN":"对应的域名ID"}
        self.domain_id = domain_id
        # {"en":"Accelerated domain name", "zh_CN":"加速域名名称"}
        self.domain_name = domain_name
        # {"en":"Operator of this query", "zh_CN":"本次查询的操作者"}
        self.operator = operator
        # {"en":"Accelerate the origin IP of a domain name", "zh_CN":"加速域名的回源IP"}
        self.origin_ips = origin_ips
        # {"en":"Service type for accelerated domain name", "zh_CN":"加速域名的服务类型"}
        self.service_type = service_type
        # {"en":"Status of accelerated domain name.", "zh_CN":"加速域名的状态"}
        self.domain_status = domain_status
        # {"en":"Deployment version code", "zh_CN":"部署版本号"}
        self.deploy_version = deploy_version
        # {"en":"Does the domain name enable CDN acceleration services, Y and N?", "zh_CN":"域名是否启用CDN加速服务，Y和N"}
        self.cdn_service_status = cdn_service_status
        # {"en":"Whether the accelerated domain name is enabled, Y and N?", "zh_CN":"加速域名是否启用，Y和N"}
        self.is_enabled = is_enabled

    def validate(self):
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.config_form_name, 'config_form_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.origin_ips, 'origin_ips')
        self.validate_required(self.service_type, 'service_type')
        self.validate_required(self.domain_status, 'domain_status')
        self.validate_required(self.deploy_version, 'deploy_version')
        self.validate_required(self.cdn_service_status, 'cdn_service_status')
        self.validate_required(self.is_enabled, 'is_enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['cname'] = self.cname
        if self.config_form_name is not None:
            result['configFormName'] = self.config_form_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.origin_ips is not None:
            result['originIps'] = self.origin_ips
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.domain_status is not None:
            result['domainStatus'] = self.domain_status
        if self.deploy_version is not None:
            result['deployVersion'] = self.deploy_version
        if self.cdn_service_status is not None:
            result['cdnServiceStatus'] = self.cdn_service_status
        if self.is_enabled is not None:
            result['isEnabled'] = self.is_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('configFormName') is not None:
            self.config_form_name = m.get('configFormName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('originIps') is not None:
            self.origin_ips = m.get('originIps')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('domainStatus') is not None:
            self.domain_status = m.get('domainStatus')
        if m.get('deployVersion') is not None:
            self.deploy_version = m.get('deployVersion')
        if m.get('cdnServiceStatus') is not None:
            self.cdn_service_status = m.get('cdnServiceStatus')
        if m.get('isEnabled') is not None:
            self.is_enabled = m.get('isEnabled')
        return self


class GetFuzzyPagingDomainListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        x_cnc_request_id: str = None,
        total_count: int = None,
        total_page_number: int = None,
        page_number: int = None,
        page_size: int = None,
        result_list: List[GetFuzzyPagingDomainListResponseResultList] = None,
    ):
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.code = code
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id
        # {"en":"Responses the page number of the data", "zh_CN":"所有满足条件的数据总条数"}
        self.total_count = total_count
        # {"en":"total pages", "zh_CN":"总页数"}
        self.total_page_number = total_page_number
        # {"en":"Responses the page number of the data", "zh_CN":"返回数据的页码"}
        self.page_number = page_number
        # {"en":"Number of data page", "zh_CN":"每个页面的数据条数"}
        self.page_size = page_size
        # {"en":"Responses status information for the accelerated domain name", "zh_CN":"返回加速域名的状态信息"}
        self.result_list = result_list

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page_number, 'total_page_number')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.result_list, 'result_list')
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.total_page_number is not None:
            result['totalPageNumber'] = self.total_page_number
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result_list is not None:
            result['resultList'] = []
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('totalPageNumber') is not None:
            self.total_page_number = m.get('totalPageNumber')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resultList') is not None:
            self.result_list = []
            for k in m.get('resultList'):
                temp_model = GetFuzzyPagingDomainListResponseResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetFuzzyPagingDomainListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetFuzzyPagingDomainListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetFuzzyPagingDomainListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetFuzzyPagingDomainListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCustomerAnycastIPForWplusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerAnycastIPForWplusAnycastIPDetail(TeaModel):
    def __init__(
        self,
        ip: str = None,
        status: str = None,
        record_status: str = None,
        is_china_mainland: str = None,
    ):
        # {"en":"IP", "zh_CN":"IP"}
        self.ip = ip
        # {"en":"status", "zh_CN":"域名加速状态: USED, AVAILABLE"}
        self.status = status
        # {"en":"Record Status, For example, lock or unlock; data of length 1 or 2 can be passed.", "zh_CN":"记录状态，例如锁定、非锁定等，可以传长度为1或2的数据"}
        self.record_status = record_status
        # {"en":"Is china mainland, 0:NO,1: YES", "zh_CN":"是否属于大陆，0：否，1：是"}
        self.is_china_mainland = is_china_mainland

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.status, 'status')
        self.validate_required(self.record_status, 'record_status')
        self.validate_required(self.is_china_mainland, 'is_china_mainland')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        if self.record_status is not None:
            result['recordStatus'] = self.record_status
        if self.is_china_mainland is not None:
            result['isChinaMainland'] = self.is_china_mainland
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('recordStatus') is not None:
            self.record_status = m.get('recordStatus')
        if m.get('isChinaMainland') is not None:
            self.is_china_mainland = m.get('isChinaMainland')
        return self


class QueryCustomerAnycastIPForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryCustomerAnycastIPForWplusAnycastIPDetail] = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message
        # {"en":"data", "zh_CN":"anycastIp详细"}
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
                temp_model = QueryCustomerAnycastIPForWplusAnycastIPDetail()
                self.data.append(temp_model.from_map(k))
        return self


class QueryCustomerAnycastIPForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerAnycastIPForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerAnycastIPForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerAnycastIPForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        language: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"If no domain entered, it
        # means all domains and
        # domains details under
        # the user are queried
        # and returned.", "zh_CN":"如果没有填写域名，则返回该用户的所有域名及域名相应信息。"}
        self.domain_name = domain_name
        # {"en":"If no domain entered, it
        # means all domains and
        # domains details under
        # the user are queried
        # and returned.", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language
        # {"en":"Paging query page number (from 1) . If it is empty, the default is 1.", "zh_CN":"分页查询页码（从1开始），为空则默认为1"}
        self.page_index = page_index
        # {"en":"Paging query number.If it is empty, the default is 10 thousand.", "zh_CN":"分页查询条数，为空默认为1万条"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.language is not None:
            result['language'] = self.language
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryDomainsResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        domain_id: int = None,
        domain_name: str = None,
        adopt_state: List[str] = None,
        remark: str = None,
        state: int = None,
        ttl: int = None,
        serial_number: int = None,
        email: str = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.res_code = res_code
        # {"en":"domain Id", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain_name = domain_name
        # {"en":"Take-over status. Options: 1
        # means Already in take-over, 0
        # means not in take-over.", "zh_CN":"接管状态。其中：1表示已接管，0表示未接管。"}
        self.adopt_state = adopt_state
        # {"en":"remark", "zh_CN":"备注"}
        self.remark = remark
        # {"en":"domain state: 2: normal, 3: stop, 8: lock, 9: stop and lock", "zh_CN":"域名状态: 2/正常,3/停止,8/正常锁定,9/停止锁定"}
        self.state = state
        # {"en":"soa ttl: A 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. Zero values are interpreted to mean that the RR can only be used for the transaction in progress, and should not be cached. For example, SOA records are always distributed with a zero TTL to prohibit caching. Zero values can also be used for extremely volatile data.", "zh_CN":"soa ttl"}
        self.ttl = ttl
        # {"en":"soa Serial: The unsigned 32-bit version number of the original copy of the zone.", "zh_CN":"soa序列号"}
        self.serial_number = serial_number
        # {"en":"soa Contact: A domain name that specifies the mailbox of the person responsible for this zone.", "zh_CN":"soa邮箱"}
        self.email = email

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.adopt_state, 'adopt_state')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.state, 'state')
        self.validate_required(self.ttl, 'ttl')
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.email, 'email')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_code is not None:
            result['resCode'] = self.res_code
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.adopt_state is not None:
            result['adoptState'] = self.adopt_state
        if self.remark is not None:
            result['remark'] = self.remark
        if self.state is not None:
            result['state'] = self.state
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.email is not None:
            result['email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('adoptState') is not None:
            self.adopt_state = m.get('adoptState')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('email') is not None:
            self.email = m.get('email')
        return self


class QueryDomainsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCustomerDomainNameGroupServiceRequest(TeaModel):
    def __init__(
        self,
        domain_group_name_list: List[str] = None,
    ):
        # {'en':'Domain group name: the default value is all domain group', 'zh_CN':'域名组名称
        # 不传递则默认查询账号下全部域名组；'}
        self.domain_group_name_list = domain_group_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_group_name_list is not None:
            result['domainGroupNameList'] = self.domain_group_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainGroupNameList') is not None:
            self.domain_group_name_list = m.get('domainGroupNameList')
        return self


class QueryCustomerDomainNameGroupServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain_group_name: str = None,
        domain_list: List[str] = None,
        domain_group_id: str = None,
    ):
        # {'en':'Domain group name', 'zh_CN':'域名组名称'}
        self.domain_group_name = domain_group_name
        # {'en':'Domain list', 'zh_CN':'域名列表'}
        self.domain_list = domain_list
        # {'en':'Domain group ID', 'zh_CN':'域名组ID'}
        self.domain_group_id = domain_group_id

    def validate(self):
        self.validate_required(self.domain_group_name, 'domain_group_name')
        self.validate_required(self.domain_list, 'domain_list')
        self.validate_required(self.domain_group_id, 'domain_group_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_group_name is not None:
            result['domainGroupName'] = self.domain_group_name
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.domain_group_id is not None:
            result['domainGroupId'] = self.domain_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainGroupName') is not None:
            self.domain_group_name = m.get('domainGroupName')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('domainGroupId') is not None:
            self.domain_group_id = m.get('domainGroupId')
        return self


class QueryCustomerDomainNameGroupServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryCustomerDomainNameGroupServiceResponseResult] = None,
    ):
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryCustomerDomainNameGroupServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryCustomerDomainNameGroupServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerDomainNameGroupServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerDomainNameGroupServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCustomerDomainNameGroupServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DelDispatchDomainRequest(TeaModel):
    def __init__(
        self,
        domain_ids: str = None,
        language: str = None,
    ):
        # {"en":"Ids of the domains to be deleted Use English half-width semicolon between two domains if there are multiple to be deleted.", "zh_CN":"要删除的域名的Id
        # 如果需要删除多个域名，用英文半角分号分隔。"}
        self.domain_ids = domain_ids
        # {"en":"Ids of the domains to be deleted Use English half-width semicolon between two domains if there are multiple to be deleted.", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class DelDispatchDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: dict = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"Detailed description of the domain. 
        # domainId:Domain ID 
        # domainName:Domain name 
        # dispatchCname:Dispatch CNAME", "zh_CN":"域名的详细说明。
        # domainId 域名ID标识
        # 
        # domainName 域名
        # 
        # dispatchCname 调度CNAME"}
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


class DelDispatchDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DelDispatchDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ControlDispatchDomainRequest(TeaModel):
    def __init__(
        self,
        domain_ids: str = None,
        control_type: int = None,
        language: str = None,
    ):
        # {"en":"domainIds", "zh_CN":"域名id 多个用英文分号隔开 ;"}
        self.domain_ids = domain_ids
        # {"en":"controlType", "zh_CN":"类型: 1 ：启动  2 ：停用"}
        self.control_type = control_type
        # {"en":"language", "zh_CN":"为空返回中文结果(默认)"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_ids, 'domain_ids')
        self.validate_required(self.control_type, 'control_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids
        if self.control_type is not None:
            result['controlType'] = self.control_type
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')
        if m.get('controlType') is not None:
            self.control_type = m.get('controlType')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ControlDispatchDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.res_code = res_code
        # {"en":"detail", "zh_CN":"详情"}
        self.msg = msg
        # {"en":"content", "zh_CN":"domainId调度域名id
        # 
        # code 授权处理结果代码请参见“附录1业务状态码”
        # status 0启用 1停用"}
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


class ControlDispatchDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDispatchDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryApiDomainListServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListServiceResponseDomainList(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_id: int = None,
        cname: str = None,
        service_type: str = None,
        status: str = None,
        cdn_service_status: str = None,
        enabled: str = None,
        last_modified: str = None,
        billing_area: str = None,
    ):
        # {"en":"Name of accelerated domain name", "zh_CN":"加速域名的名称"}
        self.domain_name = domain_name
        # {"en":"The corresponding domain name ID: the domain name ID, used to perform the query and modification operations of the related domain name.", "zh_CN":"对应的域名ID：域名ID，用于执行相关域名的查询、修改操作等。"}
        self.domain_id = domain_id
        # {"en":"Accelerated domain CNAME corresponding to CNAME, for example: 7nt6mrh7sdkslj.cdn30.com", "zh_CN":"加速域名对应的CNAME域名，例如：7nt6mrh7sdkslj.cdn30.com"}
        self.cname = cname
        # {"en":"Speed up the service type of the domain name, the value is:
        # Web/web-https: web acceleration / web acceleration - https
        # Wsa/wsa-https: Total Station Acceleration / Total Station Acceleration - https
        # Vodstream/vod-https: on-demand acceleration/on-demand acceleration - https
        # Download/dl-https: Download acceleration/download acceleration - https
        # livestream/live-https/cloudv-live: Live acceleration/Live acceleration - https/Cloud vedio for live
        # 1028: Content Acceleration;
        # 1115: Dynamic Web Acceleration;
        # 1369: Media Acceleration - RTMP
        # 1391: Download Acceleration
        # 1348: Media Acceleration Live Broadcast
        # 1551: Floodshield", "zh_CN":"加速域名的服务类型，取值：
        # web/web-https：网页加速/网页加速-https
        # wsa/wsa-https：全站加速/全站加速-https
        # vodstream/vod-https：点播加速/点播加速-https
        # download/dl-https：下载加速/下载加速-https
        # livestream/live-https/cloudv-live：直播加速/直播加速-https/云直播
        # appa/s-appa：应用加速/应用安全加速解决方案
        # 1028 : Content Acceleration;
        # 1115 : Dynamic Web Acceleration;
        # 1369 : Media Acceleration - RTMP
        # 1391 : Download Acceleration
        # 1348 : Media Acceleration Live Broadcast
        # 1551 : Floodshield"}
        self.service_type = service_type
        # {"en":"The deployment status of the accelerated domain name: Deployed indicates that the accelerated domain name configuration is complete; InProgress indicates that the deployment task for this accelerated domain name configuration is still in InProgress and may be in a queue, deploy, or fail in any one of the states", "zh_CN":"加速域名的部署状态：Deployed表示该加速域名配置完成部署；InProgress表示该加速域名配置的部署任务还在进行中，可能处于排队、部署中或失败任意一种状态"}
        self.status = status
        # {"en":"Accelerate the CDN service status of the domain name: This is false when the accelerated domain name CDN service is canceled; this is true when the accelerated domain name CDN service is restored.", "zh_CN":"加速域名的CDN服务状态：当取消加速域名CDN服务后，此项为false；当恢复加速域名CDN服务后，此项为true"}
        self.cdn_service_status = cdn_service_status
        # {"en":"Accelerated domain activation: This is false when the accelerated domain name service is disabled; true when the accelerated domain name service is enabled", "zh_CN":"加速域名的启用状态：当禁用加速域名服务后，此项为false；当启用加速域名服务后，此项为true"}
        self.enabled = enabled
        # {"en":"Domain name last modified time,
        # Format: 2024-01-01T22:30:00+08:00", "zh_CN":"域名最近修改时间，格式: 2024-01-01T22:30:00+08:00"}
        self.last_modified = last_modified
        # {"en":"Billing areas.", "zh_CN":"计费区域"}
        self.billing_area = billing_area

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.service_type, 'service_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.cdn_service_status, 'cdn_service_status')
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.last_modified, 'last_modified')
        self.validate_required(self.billing_area, 'billing_area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        if self.domain_id is not None:
            result['domain-id'] = self.domain_id
        if self.cname is not None:
            result['cname'] = self.cname
        if self.service_type is not None:
            result['service-type'] = self.service_type
        if self.status is not None:
            result['status'] = self.status
        if self.cdn_service_status is not None:
            result['cdn-service-status'] = self.cdn_service_status
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.last_modified is not None:
            result['last-modified'] = self.last_modified
        if self.billing_area is not None:
            result['billing-areas'] = self.billing_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        if m.get('domain-id') is not None:
            self.domain_id = m.get('domain-id')
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('service-type') is not None:
            self.service_type = m.get('service-type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('cdn-service-status') is not None:
            self.cdn_service_status = m.get('cdn-service-status')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('last-modified') is not None:
            self.last_modified = m.get('last-modified')
        if m.get('billing-areas') is not None:
            self.billing_area = m.get('billing-areas')
        return self


class QueryApiDomainListServiceResponse(TeaModel):
    def __init__(
        self,
        domain_list: List[QueryApiDomainListServiceResponseDomainList] = None,
    ):
        # {"en":"domain list", "zh_CN":"域名列表"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domain-list'] = []
            for k in self.domain_list:
                result['domain-list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-list') is not None:
            self.domain_list = []
            for k in m.get('domain-list'):
                temp_model = QueryApiDomainListServiceResponseDomainList()
                self.domain_list.append(temp_model.from_map(k))
        return self


class QueryApiDomainListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListServiceParameters(TeaModel):
    def __init__(
        self,
        cname_label: str = None,
    ):
        # {"en":"Public CNAME alias, optional entry, does not indicate all domain names under the query account number
        # The customer has the demand that the domain cname share more than one level, so we introduce the cname-label identifier in the interface, which is a set of domain cname with the same cname-label, and share the first level of cname.", "zh_CN":"共用一级别名标示，可选入参，不选表示查询账号下所有域名
        # 客户存在较多一级域名共用的需求，因此在接口中引入cname-label标识，即拥有相同cname-label的一组域名，共用一级cname。关于cname-label的具体使用方式和注意事项，请参看【创建加速域名】和【修改域名配置】接口"}
        self.cname_label = cname_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname_label is not None:
            result['cname-label'] = self.cname_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname-label') is not None:
            self.cname_label = m.get('cname-label')
        return self


class QueryApiDomainListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListServiceResponseHeader(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['http-status-code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http-status-code') is not None:
            self.http_status = m.get('http-status-code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self






class CreateDomainRequestOriginConfig(TeaModel):
    def __init__(
        self,
        origin_ips: str = None,
        default_origin_host_header: str = None,
    ):
        # {"en":"Origin address, which can be an IP or domain name.
        # 1. Multiple IPs are supported, separated by semicolons.
        # 2. Only one domain name is allowed. IP and domain name cannot exist at the same time.
        # 3. The length cannot exceed 500 characters.
        # 4. The number of IPs cannot exceed 15.", "zh_CN":"回源地址，可以是IP或域名。
        # 1、IP以分号分隔，支持多个。
        # 2、域名只能输入一个。IP与域名不能同时输入。
        # 3、限制最大不能超过500个字符长度。
        # 4、源IP个数不能超过15个。"}
        self.origin_ips = origin_ips
        # {"en":"The Origin HOST for changing the HOST field in the return source HTTP request header. The supported domain name formats, each segement separated by a dot, does not exceed 62 characters, the total length should not exceed 128 characters.
        # .", "zh_CN":"回源HOST，用于更改回源HTTP请求头中的HOST字段。支持格式为: 域名，每段（点号分隔）长度小于等于62，域名总长度小于等于128。"}
        self.default_origin_host_header = default_origin_host_header

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_ips is not None:
            result['origin-ips'] = self.origin_ips
        if self.default_origin_host_header is not None:
            result['default-origin-host-header'] = self.default_origin_host_header
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('origin-ips') is not None:
            self.origin_ips = m.get('origin-ips')
        if m.get('default-origin-host-header') is not None:
            self.default_origin_host_header = m.get('default-origin-host-header')
        return self


class CreateDomainRequestLiveConfig(TeaModel):
    def __init__(
        self,
        stream_type: str = None,
        origin_push_host: str = None,
        live_config_origin_ips: str = None,
    ):
        # {"en":"The live push-pull stream type, the optional values are pull and push, pull means pull flow; push means push flow.", "zh_CN":"直播推拉流类型，可选值为pull和push，pull表示拉流；   push表示推流。"}
        self.stream_type = stream_type
        # {"en":"The push-pull domain name is used to set the push-flow domain name corresponding to the rtmp live streaming domain name. When the stream-type is pull, at least one of the source IP address and the corresponding push-stream domain name is not empty. When the stream-type is push, Incoming.", "zh_CN":"配套推流域名，用于设置rtmp直播拉流域名对应的推流域名，当stream-type为pull时，源站IP和配套推流域名至少一个不为空；当stream-type为push时，无需传入。"}
        self.origin_push_host = origin_push_host
        # {"en":"Source station IP. When the stream-type is pull, at least one of the source station IP and the companion push stream domain name is not empty.
        # 1. If it is a push-pull flow package, fill in 127.0.0.1, and the system will also default to 127.0.0.1.
        # 2. If it is directly returning to the source, fill in the source IP of the source pull stream.
        # ", "zh_CN":"源站IP，当stream-type为pull时，源站IP和配套推流域名至少一个不为空。
        # 1、如果是推拉流配套，则填写127.0.0.1，不传系统也默认为127.0.0.1
        # 2、如果是直接回源拉流，则填写回源拉流的源站IP"}
        self.live_config_origin_ips = live_config_origin_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_type is not None:
            result['stream-type'] = self.stream_type
        if self.origin_push_host is not None:
            result['origin-push-host'] = self.origin_push_host
        if self.live_config_origin_ips is not None:
            result['origin-ips'] = self.live_config_origin_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream-type') is not None:
            self.stream_type = m.get('stream-type')
        if m.get('origin-push-host') is not None:
            self.origin_push_host = m.get('origin-push-host')
        if m.get('origin-ips') is not None:
            self.live_config_origin_ips = m.get('origin-ips')
        return self


class CreateDomainRequestPublishPoints(TeaModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # {"en":"Livestream domain settings. Publish point, support multiple, do not pass the system by default to generate a publishing point uri for [/]", "zh_CN":"发布点，支持多个，不传系统默认生成一条发布点uri为“/”"}
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        return self


class CreateDomainRequestSsl(TeaModel):
    def __init__(
        self,
        use_ssl: str = None,
        use_for_sni: str = None,
        ssl_certificate_id: int = None,
    ):
        # {"en":"Use a certificate, the optional values are true and false, true means to use the certificate, false means not to use the certificate", "zh_CN":"使用证书，可选值为true和false，true表示使用证书，false表示不使用证书"}
        self.use_ssl = use_ssl
        # {"en":"Use sni certificate, the optional values are true and false, true means use sni certificate, false means use shared certificate (not supported)", "zh_CN":"使用sni证书，可选值为true和false，true表示使用sni证书，false表示使用合用证书（暂不支持）"}
        self.use_for_sni = use_for_sni
        # {"en":"Use sni certificate, the optional values are true and false, true means use sni certificate, false means use shared certificate (not supported)", "zh_CN":"证书ID，新增证书成功后，系统返回的证书ID，use-ssl为true时，才能传ssl-certificate-id。"}
        self.ssl_certificate_id = ssl_certificate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.use_ssl is not None:
            result['use-ssl'] = self.use_ssl
        if self.use_for_sni is not None:
            result['use-for-sni'] = self.use_for_sni
        if self.ssl_certificate_id is not None:
            result['ssl-certificate-id'] = self.ssl_certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('use-ssl') is not None:
            self.use_ssl = m.get('use-ssl')
        if m.get('use-for-sni') is not None:
            self.use_for_sni = m.get('use-for-sni')
        if m.get('ssl-certificate-id') is not None:
            self.ssl_certificate_id = m.get('ssl-certificate-id')
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
        domain_name: str = None,
        service_type: str = None,
        service_areas: str = None,
        comment: str = None,
        config_form_id: int = None,
        referenced_domain_name: str = None,
        cname_label: str = None,
        cname_with_customized_prefix: str = None,
        origin_config: CreateDomainRequestOriginConfig = None,
        live_config: CreateDomainRequestLiveConfig = None,
        accelerate_no_china: str = None,
        header_of_clientip: str = None,
        upstream_host: str = None,
        publish_points: List[CreateDomainRequestPublishPoints] = None,
        ssl: CreateDomainRequestSsl = None,
    ):
        # {"en":"Version code , the current version is 1.0.0", "zh_CN":"版本号，当前版本号1.0.0"}
        self.version = version
        # {"en":"Need to access the domain name of the CDN. a generic domain name is supported, starting with the symbol '.', such as.example.com, which also contains a multilevel 'a.b.example.com'.If example.com is filed, the domain name xx.example.com does not need to be filed.", "zh_CN":"需要接入CDN的域名。支持泛域名，以符号“.”开头，如：.example.com，泛域名也包含多级“a.b.example.com”。
        # 如果example.com已备案，那么域名xx.example.com则不需要备案。"}
        self.domain_name = domain_name
        # {"en":"The service type of the accelerated domain name (only one service type can be submitted at a time):
        #   web/web-https: Web page acceleration/Web page acceleration-https
        # wsa/Wsa-https: Full-station acceleration/full-station acceleration-https
        # vodstream/vod-https: on-demand acceleration/on-demand acceleration-https
        # download/dl-https: Download Acceleration/Download Acceleration-https
        # livestream/live-https/cloudv-live: livestream acceleration
        # v6sa/osv6: IPv6 Security&Acceleration Solution/IPv6 One-stop Solution
        # Note:
        # 1. the https in the code, such as web-https does not represent immediate support for https access, you need to upload the certificate to support https.
        #   ", "zh_CN":"加速域名的服务类型（一次只能提交一个服务类型）：
        # web/web-https：网页加速/网页加速-https
        # wsa/wsa-https：全站加速/全站加速-https
        # vodstream/vod-https：点播加速/点播加速-https
        # download/dl-https：下载加速/下载加速-https
        # livestream/live-https/cloudv-live：直播加速
        # v6sa/osv6：ipv6安全加速解决方案/IPv6一体化解决方案
        # 注意：
        # 1、service-type中的https不代表立即开启https，比如web-https中的https并不代表立刻支持https访问，需上传完证书后才可以支持https，切记！"}
        self.service_type = service_type
        # {"en":"The acceleration area of the acceleration domain, if the resource coverage needs to be limited according to the area, the acceleration area needs to be specified.
        #     When no acceleration area is specified, we will provide acceleration services with optimal resource coverage according to the service area opened by the customer. 
        #     Multiple regions are separated by semicolons, and the supported regions are as follows: cn (Mainland China), am (Americas), 
        #     emea (Europe, Middle East, Africa), apac (Asia-Pacific region).",
        # "zh_CN":"加速域名的加速区域，如果有需要根据区域限定资源覆盖时，才需要指定加速区域。未指定加速区域时，我们将按照客户开通的服务区域，以最优的资源覆盖提供加速服务。多个区域以分号分隔，支持配置的区域如下：cn（中国大陆）、am（美洲）、emea（欧洲、中东、非洲）、apac（亚太地区）"}
        self.service_areas = service_areas
        # {"en":"Remarks, up to 1000 characters", "zh_CN":"备注信息，最大限制1000个字符"}
        self.comment = comment
        # {"en":"Configuration template, if you want to add the a domain using some specified configuration by default, you can specify the template id. For more detail, please contract the technical support.",
        #     "zh_CN":"配置单模板，特定的使用场景下，如果希望新增的加速域名参照某些指定配置时，可以指定配置单模板，具体使用请咨询对应的客户负责人。"}
        self.config_form_id = config_form_id
        # {"en":"Refer to the configuration of the specified domain.
        # Note:
        # 1. If the referenced domain uses a certificate, the new domain should be in the 'DNS name' of the certificate.
        # 2. If the referenced domain has no China ICP, while the new domain name has, it may affect the cover resources and service quality.
        # 3. If the referenced domain has China ICP, while the new domain name doesn't, then the cover resources may be re-selected if it does not meet the policy requirements.
        # 4. It is not allowed to reference a domain which is traffic-free.", "zh_CN":"参照指定域名的配置，来创建加速域名。
        # 注意：
        # 1.参照域名如果有使用证书，新增域名也要在对应证书授权范围内。
        # 2.参照未备案域名，新增的域名如果已备案，可能影响资源使用和服务质量。
        # 3.参照备案域名，新增的域名如果未备案，若资源不满足政策要求，可能重选。
        # 4.不允许参照免流域名创建新域名。"}
        self.referenced_domain_name = referenced_domain_name
        # {"en":"If you need to share a CNAME between domains, you can use this parameter. This parameter is a unique label for a public CNAME. Domains with the same cname-label will have the same CNAME. 
        # Note:
        # 1. Domains with the same cname-label have the same coverage.
        # 2. Constraints of sharing a CNAME: consistent service-type, consistent certificate-id (if there is a certificate), consistent service-areas
        # 3. Multiple http domains can share a CNAME, multiple sni https domains can share a CNAME too.
        # 4. When a cname-label is used by a single domain, then the domain can be canceled acceleration. While a cname-label using by more then one domains, they can not be canceled acceleration.
        # 5. Support the purpose of modifying cname by modifying cname-label. )
        # ", "zh_CN":"共用一级标签，若有多个加速域名需要共用一级域名，则可以使用该参数。即拥有相同cname-label的一组域名，共用一级cname。
        # 注意：
        # 1、拥有相同cname-label的域名共用一级cname，且有完全一致的dns覆盖
        # 2、共用一级的约束：加速类型一致(service-type)、证书id一致（certificate-id,如果有证书）、加速区域一致(service-areas)
        # 3、多个http域名可共用一级，多个sni https域名可共用一级
        # 4、单个域名使用cname-label时，域名可cancel；多个域名共用一级时，不允许cancel这些域名
        # 5、支持通过修改cname-label达到修改cname的目的。）
        # "}
        self.cname_label = cname_label
        # {"en":"The first level of cname prefix, true, indicates that the domain cname is used as the cname prefix, otherwise the 14-bit random string (number + letter) is used as the cname prefix.
        # Note: When the prefix is a generic domain name, a wsall is added as a prefix. Such as... Baidu.com.wscloudcdn.com, which will generate wsall.Baidu.com.wscloudcdn.com", "zh_CN":"一级cname前缀，true表示使用域名名称作为cname前缀，否则，使用14位随机串（数字+字母）作为cname前缀。
        #   注意：当前缀是泛域名时，则再增加wsall作为前缀。如.baidu.com.wscloudcdn.com，会生成wsall.baidu.com.wscloudcdn.com"}
        self.cname_with_customized_prefix = cname_with_customized_prefix
        # {"en":"Back-to-origin policy setting, which is used to set the origin site information and the back-to-origin policy of the none-live accelerated domain", "zh_CN":"回源策略设置(非直播域名使用)，用于设置加速域名的源站信息和回源策略。"}
        self.origin_config = origin_config
        # {"en":"Live domain configuration, used to set the push flow of rtmp live acceleration domain (use required)
        # Note: In addition to the API call permission, you need to contact the dedicated customer service to apply for the corresponding API client template.", "zh_CN":"直播域名配置，用于设置rtmp直播加速域名的推拉流（使用需申请）
        # 注意：该节点下的相关参数配置，除开通API调用权限外，还需要联系专属客服申请开通对应的API客户模板"}
        self.live_config = live_config
        # {"en":"Identifies whether a domain name is fully overseas accelerated.
        # Whether the default is false
        # True: indicates that the client domain name is a pure overseas acceleration
        # False: Indicates that the client domain name has accelerated in China", "zh_CN":"标识域名是否是纯海外加速的。
        # 默认是否（false）
        # true ：表示客户域名纯海外加速
        # false：表示客户域名有在中国加速"}
        self.accelerate_no_china = accelerate_no_china
        # {"en":"Pass the response header of client IP. The optional values are Cdn-Src-Ip, X-Forwarded-For and ori_X-Forwarded-For.", "zh_CN":"传递客户端ip的响应头部，可选值为Cdn-Src-Ip、X-Forwarded-For、ori_X-Forwarded-For
        # 1） Cdn-Src-Ip： 回源头部名称为Cdn-Src-Ip，获取与节点进行建联的IP作为客户端IP传递回源。
        # 2） X-Forwarded-For： 回源头部名称为X-Forwarded-For，携带的客户端IP值是Cdn-Src-Ip获取到的建联IP。
        # 3） ori_X-Forwarded-For：客户端请求CDN节点时会自带X-Forwarded-For，则CDN透传此头部和值回源。"}
        self.header_of_clientip = header_of_clientip
        # {"en":"The live streaming domain which is pull domian ,and  directly returned to the source to verify the configuration.
        # which can be an IP or a domain name.
        # Can be IP or domain name. Ip and domain names can only be one. Multiple input parameters are not supported.", "zh_CN":"直播拉流域名，直接回源校验配置。
        # 可以是IP或域名。ip和域名只能一种。不支持多个入参。"}
        self.upstream_host = upstream_host
        # {"en":"Set the publishing point of the live push-pull domain name
        # note:
        # 1. Pull flow and corresponding push flow domain name must be configured with the same publishing point.
        # 2. do not want to modify the publishing point, do not pass the node and the following parameters
        # 3. The publishing point adopts the overlay update. Each time you modify, you need to submit all the publishing points. You cannot submit only the parts that need to be modified.", "zh_CN":"设置直播推拉流域名的发布点
        # 注意：
        # 1、拉流和对应的推流域名，必须配置相同的发布点；
        # 2、不想修改发布点时，不要传入该节点及以下入参；
        # 3、发布点采用覆盖式更新，每次修改时，需要提交全部发布点，不能仅提交需要修改的部分。"}
        self.publish_points = publish_points
        # {"en":"SSL settings, to bind a certificate with the accelerated domain. You can use the interface [AddCertificate] to upload your  certificates. If you want to modify a certificate, please use the interface: [UpdateCertificate]", "zh_CN":"ssl证书设置，用于设置加速域名的ssl证书配置。上传证书请使用接口：【新增证书V2】；若要修改证书，请使用接口：【修改证书V2】"}
        self.ssl = ssl

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.domain_name, 'domain_name')
        if self.origin_config:
            self.origin_config.validate()
        if self.live_config:
            self.live_config.validate()
        if self.publish_points:
            for k in self.publish_points:
                if k:
                    k.validate()
        if self.ssl:
            self.ssl.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        if self.service_type is not None:
            result['service-type'] = self.service_type
        if self.service_areas is not None:
            result['service-areas'] = self.service_areas
        if self.comment is not None:
            result['comment'] = self.comment
        if self.config_form_id is not None:
            result['config-form-id'] = self.config_form_id
        if self.referenced_domain_name is not None:
            result['referenced-domain-name'] = self.referenced_domain_name
        if self.cname_label is not None:
            result['cname-label'] = self.cname_label
        if self.cname_with_customized_prefix is not None:
            result['cname-with-customized-prefix'] = self.cname_with_customized_prefix
        if self.origin_config is not None:
            result['origin-config'] = self.origin_config.to_map()
        if self.live_config is not None:
            result['live-config'] = self.live_config.to_map()
        if self.accelerate_no_china is not None:
            result['accelerate-no-china'] = self.accelerate_no_china
        if self.header_of_clientip is not None:
            result['header-of-clientip'] = self.header_of_clientip
        if self.upstream_host is not None:
            result['upstream-host'] = self.upstream_host
        if self.publish_points is not None:
            result['publish-points'] = []
            for k in self.publish_points:
                result['publish-points'].append(k.to_map() if k else None)
        if self.ssl is not None:
            result['ssl'] = self.ssl.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        if m.get('service-type') is not None:
            self.service_type = m.get('service-type')
        if m.get('service-areas') is not None:
            self.service_areas = m.get('service-areas')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('config-form-id') is not None:
            self.config_form_id = m.get('config-form-id')
        if m.get('referenced-domain-name') is not None:
            self.referenced_domain_name = m.get('referenced-domain-name')
        if m.get('cname-label') is not None:
            self.cname_label = m.get('cname-label')
        if m.get('cname-with-customized-prefix') is not None:
            self.cname_with_customized_prefix = m.get('cname-with-customized-prefix')
        if m.get('origin-config') is not None:
            temp_model = CreateDomainRequestOriginConfig()
            self.origin_config = temp_model.from_map(m['origin-config'])
        if m.get('live-config') is not None:
            temp_model = CreateDomainRequestLiveConfig()
            self.live_config = temp_model.from_map(m['live-config'])
        if m.get('accelerate-no-china') is not None:
            self.accelerate_no_china = m.get('accelerate-no-china')
        if m.get('header-of-clientip') is not None:
            self.header_of_clientip = m.get('header-of-clientip')
        if m.get('upstream-host') is not None:
            self.upstream_host = m.get('upstream-host')
        if m.get('publish-points') is not None:
            self.publish_points = []
            for k in m.get('publish-points'):
                temp_model = CreateDomainRequestPublishPoints()
                self.publish_points.append(temp_model.from_map(k))
        if m.get('ssl') is not None:
            temp_model = CreateDomainRequestSsl()
            self.ssl = temp_model.from_map(m['ssl'])
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        cname: str = None,
        code: str = None,
        message: str = None,
    ):
        # {"en":"The name of the service domain automatically generated by the My company, for example: xxxx.cdn30.com", "zh_CN":"由我司自动生成的服务域名名称，例如：xxxx.cdn30.com"}
        self.cname = cname
        # {"en":"The error code, when HTTPStatus is not 202, indicates the type of error the current request is calling.", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, when success is successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message

    def validate(self):
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['cname'] = self.cname
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDomainResponseHeader(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        x_cnc_request_id: str = None,
        location: str = None,
    ):
        # {"en":"If httpstatus=202, the interface is successfully invoked. And the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况。"}
        self.http_status = http_status
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）。"}
        self.x_cnc_request_id = x_cnc_request_id
        # {"en":"A URL used to access the domain name information, where the domain-id is a unique identifier for the domain name.", "zh_CN":"用于访问该域名信息的URL，其中domain-id为该域名的唯一标识。"}
        self.location = location

    def validate(self):
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')
        self.validate_required(self.location, 'location')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['http status code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http status code') is not None:
            self.http_status = m.get('http status code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self






class DispatchWarnLogRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        domain_id: int = None,
        policy_id: int = None,
        view: str = None,
        warn_type: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Language type The default language: Chinese 'zh_CN': The English 'en'", "zh_CN":"语言类型 默认 中文, 中文  'zh_CN'英文  'en'"}
        self.language = language
        # {"en":"domainId", "zh_CN":"调度域名id"}
        self.domain_id = domain_id
        # {"en":"policyId", "zh_CN":"策略id"}
        self.policy_id = policy_id
        # {"en":"view name", "zh_CN":"线路中文名，支持模糊搜索，例如‘中国电信’"}
        self.view = view
        # {"en":"warnType", "zh_CN":"告警类型 0：调度告警 1：故障告警 2：恢复通知"}
        self.warn_type = warn_type
        # {"en":"Query start time format yyyy-mm-dd HH: MM :ss for example '2021-04-26 18:00:00'", "zh_CN":"查询开始时间 格式yyyy-MM-dd HH:mm:ss  例如‘2021-04-26 18:00:00’"}
        self.start_time = start_time
        # {"en":"End of query format yyyy-mm-dd HH: MM :ss for example '2021-04-26 18:00:00'", "zh_CN":"查询结束时间 格式yyyy-MM-dd HH:mm:ss  例如‘2021-04-26 18:00:00’"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['language'] = self.language
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.view is not None:
            result['view'] = self.view
        if self.warn_type is not None:
            result['warnType'] = self.warn_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('view') is not None:
            self.view = m.get('view')
        if m.get('warnType') is not None:
            self.warn_type = m.get('warnType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class DispatchWarnLogResponse(TeaModel):
    def __init__(
        self,
        res_code: int = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code. See "Scheduling Business Status Codes" for a detailed description of RESCODE.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code", "zh_CN":"状态码的详细说明"}
        self.msg = msg
        # {"en":"data", "zh_CN":"业务数据"}
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


class DispatchWarnLogPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchWarnLogParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchWarnLogRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DispatchWarnLogResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RestoreApiDomainServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RestoreApiDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"Error code, which appears when HTTPStatus is not 202, represents the error type of the current request call", "zh_CN":"错误代码，当HTTPStatus不为202时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, success when successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.http_status = http_status
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.http_status, 'http_status')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.http_status is not None:
            result['http-status-code'] = self.http_status
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('http-status-code') is not None:
            self.http_status = m.get('http-status-code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class RestoreApiDomainServicePaths(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
    ):
        # {"en":"", "zh_CN":"加速域名在系统中对应的ID
        # 1. 参看请求示例中的url，123344对应的就是domain-id
        # 2. 可以通过【获取域名配置】和【获取域名列表】接口查询到domain-id"}
        self.domain_id = domain_id

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class RestoreApiDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RestoreApiDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RestoreApiDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ControlDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        operate: int = None,
        language: str = None,
    ):
        # {"en":"Domain names are separated by English symbols (e.g. aaa.com; bb.com).", "zh_CN":"域名 多个域名用英文符号;隔开（如： aaa.com;bb.com）"}
        self.domain_name = domain_name
        # {"en":"Operation: 1 is enabled; 0 is disabled", "zh_CN":"操作：1 启用；0 停用"}
        self.operate = operate
        # {"en":"Return Chinese results for null (default)
        # En: Return the English prompt result", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.operate, 'operate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.operate is not None:
            result['operate'] = self.operate
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class ControlDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: List[str] = None,
    ):
        # {"en":"Status code. For detailed description of resCode, please refer to 'Status Codes of Dispatch Business'.", "zh_CN":"状态码，详细说明请参见“业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"recordId, ID of host name record, used to identify this record.", "zh_CN":"域名的详细说明。"}
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


class ControlDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ControlDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPagingDomainListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        service_types: List[str] = None,
        domain_names: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        status: str = None,
    ):
        # {"en":"Page number must be a positive integer greater than 0.If not passed, then no paging. If it is passed, pageSize is required.", "zh_CN":"分页的页码，必须为大于0的正整数。不传默认不分页，若传参则pageSize必填.。"}
        self.page_number = page_number
        # {"en":"Number of domain name data items for paging, must be a positive integer greater than 0.If not passed, then no paging. If it is passed, pageSize is required.", "zh_CN":"分页的域名数据条数，必须大于0的正整数。不传默认不分页，若传参则pageSize必填.。"}
        self.page_size = page_size
        # {"en":"Specify the service type to be queried. Multiple services are allowed. Data will be returned if any one service is satisfied. If not passed, all services will be checked by default. For example: [wsa,waf], returns all domains whose services include wsa or include waf.", "zh_CN":"指定查询的服务，允许多个服务，任意一个服务满足就返回数据，不传默认查全部服务。如：[wsa,waf], 则返回服务包含wsa或包含waf的所有域名。"}
        self.service_types = service_types
        # {"en":"Specify the accelerated domain name for the query. Multiple domain names are allowed. If not specified, all domain names will be searched by default.", "zh_CN":"指定查询的加速域名，允许多个域名，不传默认查全部域名。"}
        self.domain_names = domain_names
        # {"en":"RFC3339 formatted date indicating the starting date. Example: 2024-01-01T22:30:00+08:00", "zh_CN":"	查询开始时间，支持时间格式如：2024-01-01T22:30:00+08:00"}
        self.start_time = start_time
        # {"en":"RFC3339 formatted date indicating the ending date. Example: 2024-01-01T22:30:00+08:00", "zh_CN":"查询结束时间，支持时间格式如：2024-01-01T22:30:00+08:00"}
        self.end_time = end_time
        # {"en":" Status of the accelerated domain. Optional value: enabled, disabled, deploying, checking, disabling, deployFailed, disableFailed.", "zh_CN":"加速域名的状态：enabled表示已启用；disabled表示已禁用；deploying表示配置部署中；checking表示审核中；disabling表示禁用中；deployFailed表示配置部署失败；disableFailed表示禁用失败。不传默认查全部"}
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.service_types is not None:
            result['serviceTypes'] = self.service_types
        if self.domain_names is not None:
            result['domainNames'] = self.domain_names
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('serviceTypes') is not None:
            self.service_types = m.get('serviceTypes')
        if m.get('domainNames') is not None:
            self.domain_names = m.get('domainNames')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetPagingDomainListResponseResultList(TeaModel):
    def __init__(
        self,
        cname: str = None,
        create_time: str = None,
        domain_id: str = None,
        domain_name: str = None,
        service_types: List[str] = None,
        status: str = None,
        enabled: str = None,
    ):
        # {"en":"Cname of the accelerated domain", "zh_CN":"加速域名cname，如：a1.example.com.wscdns.com"}
        self.cname = cname
        # {"en":"Create time of the accelerated domain. Example: 2024-01-01T22:30:00+08:00", "zh_CN":"	域名创建时间，时间格式如：2024-01-01T22:30:00+08:00"}
        self.create_time = create_time
        # {"en":"Corresponding domain ID", "zh_CN":"对应的域名ID"}
        self.domain_id = domain_id
        # {"en":"Accelerated domain name", "zh_CN":"加速域名名称"}
        self.domain_name = domain_name
        # {"en":"Service type for accelerated domain name", "zh_CN":"加速域名的服务，如[wsa,waf]。"}
        self.service_types = service_types
        # {"en":"Status of the accelerated domain. Optional value: enabled, disabled, deploying, checking, disabling.", "zh_CN":"	加速域名的状态：enabled表示已启用；disabled表示已禁用；deploying表示部署中；checking表示审核中；disabling表示禁用中；deployFailed表示配置部署失败；disableFailed表示禁用失败"}
        self.status = status
        # {"en":"Accelerated domain enabling status: true indicates that it is enabled, false indicates that it is disabled.", "zh_CN":"加速域名启用状态：true为启用，false为禁用。"}
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.service_types, 'service_types')
        self.validate_required(self.status, 'status')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['cname'] = self.cname
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.service_types is not None:
            result['serviceTypes'] = self.service_types
        if self.status is not None:
            result['status'] = self.status
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('serviceTypes') is not None:
            self.service_types = m.get('serviceTypes')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class GetPagingDomainListResponse(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        total_page_number: int = None,
        page_number: int = None,
        page_size: int = None,
        result_list: List[GetPagingDomainListResponseResultList] = None,
    ):
        # {"en":"Responses the page number of the data", "zh_CN":"所有满足条件的数据总条数"}
        self.total_count = total_count
        # {"en":"total pages", "zh_CN":"总页数"}
        self.total_page_number = total_page_number
        # {"en":"Responses the page number of the data", "zh_CN":"返回数据的页码"}
        self.page_number = page_number
        # {"en":"Number of data page", "zh_CN":"每个页面的数据条数"}
        self.page_size = page_size
        # {"en":"Domain list.", "zh_CN":"域名列表"}
        self.result_list = result_list

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page_number, 'total_page_number')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.result_list, 'result_list')
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.total_page_number is not None:
            result['totalPageNumber'] = self.total_page_number
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result_list is not None:
            result['resultList'] = []
            for k in self.result_list:
                result['resultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('totalPageNumber') is not None:
            self.total_page_number = m.get('totalPageNumber')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resultList') is not None:
            self.result_list = []
            for k in m.get('resultList'):
                temp_model = GetPagingDomainListResponseResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetPagingDomainListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPagingDomainListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPagingDomainListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPagingDomainListResponseHeader(TeaModel):
    def __init__(
        self,
        code: int = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"httpstatus=202; Indicates that the new domain API was successfully invoked, and the current deployment of the new domain can be viewed using x-cnc-request-id in the header", "zh_CN":"httpstatus=202;   表示成功调用新增域名接口，可使用header中的x-cnc-request-id查看当前新增域名的部署情况"}
        self.code = code
        # {"en":"Uniquely identified id for querying tasks per request (for all API)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self






class QueryDispatchDomainsRequest(TeaModel):
    def __init__(
        self,
        start: int = None,
        limit: int = None,
        domain_name: str = None,
        language: str = None,
    ):
        # {"en":"Query inital records by page", "zh_CN":"分页查询起始记录"}
        self.start = start
        # {"en":"Number if quried items by page", "zh_CN":"分页查询条数"}
        self.limit = limit
        # {"en":"Parameter of domain fuzzy search Domain fuzzy search. If no domain entered, it means all domains and domains details under the user are queried and returned.", "zh_CN":"域名模糊搜索参数
        # 域名模糊搜索，如果没有填写域名，则返回该用户的所有域名及域名相应信息。"}
        self.domain_name = domain_name
        # {"en":"Parameter of domain fuzzy search Domain fuzzy search. If no domain entered, it means all domains and domains details under the user are queried and returned.", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        self.validate_required(self.start, 'start')
        self.validate_required(self.limit, 'limit')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['start'] = self.start
        if self.limit is not None:
            result['limit'] = self.limit
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class QueryDispatchDomainsResponseContentRows(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        domain_name: str = None,
        dispatch_cname: str = None,
        policy_count: str = None,
    ):
        # {"en":"domainId", "zh_CN":"域名ID标识"}
        self.domain_id = domain_id
        # {"en":"domainName", "zh_CN":"域名"}
        self.domain_name = domain_name
        # {"en":"Dispatch CNAME", "zh_CN":"调度CNAME"}
        self.dispatch_cname = dispatch_cname
        # {"en":"The number of domain policies", "zh_CN":"域名策略数量"}
        self.policy_count = policy_count

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.dispatch_cname, 'dispatch_cname')
        self.validate_required(self.policy_count, 'policy_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.dispatch_cname is not None:
            result['dispatchCname'] = self.dispatch_cname
        if self.policy_count is not None:
            result['policyCount'] = self.policy_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('dispatchCname') is not None:
            self.dispatch_cname = m.get('dispatchCname')
        if m.get('policyCount') is not None:
            self.policy_count = m.get('policyCount')
        return self


class QueryDispatchDomainsResponseContent(TeaModel):
    def __init__(
        self,
        rows: List[QueryDispatchDomainsResponseContentRows] = None,
    ):
        self.rows = rows

    def validate(self):
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['rows'] = []
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = QueryDispatchDomainsResponseContentRows()
                self.rows.append(temp_model.from_map(k))
        return self


class QueryDispatchDomainsResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: QueryDispatchDomainsResponseContent = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"Detailed description of the domain. count The total number of user's domains rows The queried results of domains", "zh_CN":"域名的详细说明。count 用户域名总数量"}
        self.content = content

    def validate(self):
        self.validate_required(self.res_code, 'res_code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

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
            result['content'] = self.content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resCode') is not None:
            self.res_code = m.get('resCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('content') is not None:
            temp_model = QueryDispatchDomainsResponseContent()
            self.content = temp_model.from_map(m['content'])
        return self


class QueryDispatchDomainsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchDomainsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchDomainsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDispatchDomainsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddDispatchDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        dispatch_zone: str = None,
        language: str = None,
    ):
        # {"en":"The added dispatch domain", "zh_CN":"添加的调度域名"}
        self.domain_name = domain_name
        # {"en":"Dispatch CName suffix Options, domestic: cdngtm.cn, Overseas: ; the default setting is cdngtm.com", "zh_CN":"调度CName后缀
        # 可选，国内：cdngtm.cn， 海外：cdngtm.com；默认值为cdngtm.com"}
        self.dispatch_zone = dispatch_zone
        # {"en":"Dispatch CName suffix Options, domestic: cdngtm.cn, Overseas: ; the default setting is cdngtm.com", "zh_CN":"为空返回中文结果(默认)
        # en:返回英文提示结果"}
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.dispatch_zone is not None:
            result['dispatchZone'] = self.dispatch_zone
        if self.language is not None:
            result['language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('dispatchZone') is not None:
            self.dispatch_zone = m.get('dispatchZone')
        if m.get('language') is not None:
            self.language = m.get('language')
        return self


class AddDispatchDomainResponse(TeaModel):
    def __init__(
        self,
        res_code: str = None,
        msg: str = None,
        content: dict = None,
    ):
        # {"en":"Status code.", "zh_CN":"状态码。resCode的详细说明请参见“调度业务状态码”。"}
        self.res_code = res_code
        # {"en":"Detailed description of the status code.", "zh_CN":"状态码的详细说明。"}
        self.msg = msg
        # {"en":"Detailed description of the domain. 
        # domainId:Domain ID 
        # domainName:Domain name 
        # dispatchCname:Dispatch CNAME", "zh_CN":"域名的详细说明。
        # domainId 域名ID标识
        # 
        # domainName 域名
        # 
        # dispatchCname 调度CNAME"}
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


class AddDispatchDomainPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDispatchDomainParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDispatchDomainRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddDispatchDomainResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryApiDomainListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListResponseDomainSummary(TeaModel):
    def __init__(
        self,
        cname: str = None,
        domain_id: int = None,
        domain_name: str = None,
        origin_ips: str = None,
        service_type: str = None,
        status: str = None,
        enabled: str = None,
    ):
        # {"en":"", "zh_CN":"加速域名对应的CNAME域名，例如：7nt6mrh7sdkslj.cdn30.com"}
        self.cname = cname
        # {"en":"", "zh_CN":"对应的域名ID"}
        self.domain_id = domain_id
        # {"en":"", "zh_CN":"加速域名名称"}
        self.domain_name = domain_name
        # {"en":"", "zh_CN":"加速域名的回源IP"}
        self.origin_ips = origin_ips
        # {"en":"", "zh_CN":"加速域名的服务类型"}
        self.service_type = service_type
        # {"en":"", "zh_CN":"加速域名的部署状态"}
        self.status = status
        # {"en":"", "zh_CN":"加速域名是否启用，true和false"}
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.origin_ips, 'origin_ips')
        self.validate_required(self.service_type, 'service_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['cname'] = self.cname
        if self.domain_id is not None:
            result['domain-id'] = self.domain_id
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        if self.origin_ips is not None:
            result['origin-ips'] = self.origin_ips
        if self.service_type is not None:
            result['service-type'] = self.service_type
        if self.status is not None:
            result['status'] = self.status
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('domain-id') is not None:
            self.domain_id = m.get('domain-id')
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        if m.get('origin-ips') is not None:
            self.origin_ips = m.get('origin-ips')
        if m.get('service-type') is not None:
            self.service_type = m.get('service-type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class QueryApiDomainListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        x_cnc_request_id: str = None,
        domain_summary: List[QueryApiDomainListResponseDomainSummary] = None,
    ):
        # {"en":"", "zh_CN":"httpstatus=202; 表示成功调用新增域名接口"}
        self.code = code
        # {"en":"", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id
        self.domain_summary = domain_summary

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')
        self.validate_required(self.domain_summary, 'domain_summary')
        if self.domain_summary:
            for k in self.domain_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        if self.domain_summary is not None:
            result['domain-summary'] = []
            for k in self.domain_summary:
                result['domain-summary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        if m.get('domain-summary') is not None:
            self.domain_summary = []
            for k in m.get('domain-summary'):
                temp_model = QueryApiDomainListResponseDomainSummary()
                self.domain_summary.append(temp_model.from_map(k))
        return self


class QueryApiDomainListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryApiDomainListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryChangeServerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChangeServerResponseDataChangeServers(TeaModel):
    def __init__(
        self,
        target_server: str = None,
        data_id: int = None,
    ):
        # {"en":"If it is a universal domain name, set it to a universal domain name, for example, *.56.com.", "zh_CN":"如果是泛域名，需要填写为泛域名，例如：*.56.com"}
        self.target_server = target_server
        # {"en":"Data-id is to indicate a specific group configuration when the client has multiple groups of configurations. Data-id can be retrieved through a query interface. Note: A. If data-id is passed, it means that one group of configuration items is specified to be modified, and no other group configuration items need to be modified. B. If multiple groups of configurations are included, some of them are configured with data-id and others are not, then the expression of data-id is used to modify a specific group of configurations, and a new group of configurations is added on the original basis without the expression of data-id. C. If the data-id is not transmitted, it means that the original configuration will be fully covered by this configuration. D. If no configuration parameter is passed, only domain name and secondary label are passed, which means that all configuration of domain name secondary service corresponding to this interface is cleared. E. If there is no specific configuration item in a set of configurations, the data-id must be filled in, and the value is the actual data-id, which means clearing the value of the corresponding data-id configuration item; it is not allowed that there is no specific configuration item or data-id in a set of configurations.", "zh_CN":"配置多组配置时，具体某组配置的id。dataId可以通过查询接口获取。 注意： a、如果有传dataId，说明指定修改其中一组配置项内容，不需求修改其他组配置内容不需要入参； b、如果入参多组配置，其中有些组配置有传dataId，有些没有传，则有传dataId的表示修改具体某组配置，没有传dataId的表示在原来基础上新增一组配置； c、如果入参都没有传dataId,表示用本次的配置全量覆盖原先配置； d、如果入参没有传任何配置项参数，只传了域名和二级标签，表示清空这个接口对应域名二级服务所有配置； e、如果一组配置没有具体的配置项，则dataId必填，且值为实际存在的dataId，表示清空这个dataId对应配置项的值；不允许一组配置没有具体的配置项也没有dataId。"}
        self.data_id = data_id

    def validate(self):
        self.validate_required(self.target_server, 'target_server')
        self.validate_required(self.data_id, 'data_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_server is not None:
            result['change-server'] = self.target_server
        if self.data_id is not None:
            result['dataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change-server') is not None:
            self.target_server = m.get('change-server')
        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')
        return self


class QueryChangeServerResponseData(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
        change_servers: List[QueryChangeServerResponseDataChangeServers] = None,
    ):
        # {"en":"domain id.", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"domain name.", "zh_CN":"域名名称"}
        self.domain_name = domain_name
        # {"en":"Change servers configuration, parent tag
        # 1. This must be filled when the hotlinking configuration of streaming media needs to be set
        # 2. Empty the configuration for <change-servers/>", "zh_CN":"【接入域名跳转】
        # 注意：
        # 1、需要取消【接入域名跳转】时，可以传入空节点<change-servers></change-servers>。
        # 2、表示需要设置【接入域名跳转】，此项必填"}
        self.change_servers = change_servers

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.change_servers, 'change_servers')
        if self.change_servers:
            for k in self.change_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.change_servers is not None:
            result['change-servers'] = []
            for k in self.change_servers:
                result['change-servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('change-servers') is not None:
            self.change_servers = []
            for k in m.get('change-servers'):
                temp_model = QueryChangeServerResponseDataChangeServers()
                self.change_servers.append(temp_model.from_map(k))
        return self


class QueryChangeServerResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryChangeServerResponseData = None,
        x_cnc_request_id: str = None,
    ):
        # {"en":"The error code, when HTTPStatus is not 200, indicates the type of error the current request is calling.", "zh_CN":"错误代码，当HTTPStatus不为200时出现，表示当前请求调用的错误类型"}
        self.code = code
        # {"en":"Response information, when success is successful", "zh_CN":"响应信息，成功时为success"}
        self.message = message
        # {"en":"The response data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Uniquely labeled id for querying each requested task (for all interfaces)", "zh_CN":"唯一标示的id，用于查询每次请求的任务 （适用全部接口）"}
        self.x_cnc_request_id = x_cnc_request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.x_cnc_request_id, 'x_cnc_request_id')

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
        if self.x_cnc_request_id is not None:
            result['x-cnc-request-id'] = self.x_cnc_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryChangeServerResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('x-cnc-request-id') is not None:
            self.x_cnc_request_id = m.get('x-cnc-request-id')
        return self


class QueryChangeServerPaths(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"Domain name or domain name id to query configuration", "zh_CN":"需要查询配置的域名（domainName）或域名id（domainId）"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class QueryChangeServerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChangeServerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChangeServerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




