# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetASchemaForARuleFormatRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASchemaForARuleFormatRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASchemaForARuleFormatPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASchemaForARuleFormatParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASchemaForARuleFormatResponseData(TeaModel):
    def __init__(
        self,
        schema: str = None,
    ):
        # {"en":"property configuration json schema.","zh_CN":"property配置的json schema"}
        self.schema = schema

    def validate(self):
        self.validate_required(self.schema, 'schema')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class GetASchemaForARuleFormatResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetASchemaForARuleFormatResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetASchemaForARuleFormatResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetASchemaForARuleFormatResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreatePropertyForMigrationRequestHostnamesCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        certificate_usage: str = None,
    ):
        # {"en":"Certificate ID","zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"certificate usage. data range: default_sni, ssl_bk, gm_sm2_enc, gm_sm2_sign, client_mtls","zh_CN":"证书用途。取值范围：default_sni, dual_sni, gm_sm2_enc, gm_sm2_sign, client_mtls"}
        self.certificate_usage = certificate_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_usage is not None:
            result['certificateUsage'] = self.certificate_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateUsage') is not None:
            self.certificate_usage = m.get('certificateUsage')
        return self


class CreatePropertyForMigrationRequestHostnamesEdgeHostname(TeaModel):
    def __init__(
        self,
        edge_hostname_prefix: str = None,
        comment: str = None,
        edge_hostname_suffix: str = None,
    ):
        # {"en":"edge-hostname prefix","zh_CN":"调度域名前缀"}
        self.edge_hostname_prefix = edge_hostname_prefix
        # {"en":"edge-hostname comment","zh_CN":"调度域名描述"}
        self.comment = comment
        # {"en":"edge-hostname suffix","zh_CN":"调度域名后缀"}
        self.edge_hostname_suffix = edge_hostname_suffix

    def validate(self):
        self.validate_required(self.edge_hostname_prefix, 'edge_hostname_prefix')
        self.validate_required(self.edge_hostname_suffix, 'edge_hostname_suffix')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_hostname_prefix is not None:
            result['edgeHostnamePrefix'] = self.edge_hostname_prefix
        if self.comment is not None:
            result['comment'] = self.comment
        if self.edge_hostname_suffix is not None:
            result['edgeHostnameSuffix'] = self.edge_hostname_suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edgeHostnamePrefix') is not None:
            self.edge_hostname_prefix = m.get('edgeHostnamePrefix')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('edgeHostnameSuffix') is not None:
            self.edge_hostname_suffix = m.get('edgeHostnameSuffix')
        return self


class CreatePropertyForMigrationRequestHostnames(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        certificates: List[CreatePropertyForMigrationRequestHostnamesCertificates] = None,
        edge_hostname: CreatePropertyForMigrationRequestHostnamesEdgeHostname = None,
    ):
        # {"en":"hostname, the length must not exceed 128 characters. A wildcard hostname must start with an asterisk (*).","zh_CN":"域名，长度不超过128个字符。泛域名需要以“*”开头。"}
        self.hostname = hostname
        # {"en":"hostname association ssl configuration","zh_CN":"关联证书配置"}
        self.certificates = certificates
        # {"en":"hostname edge-hostname config","zh_CN":"调度域名配置"}
        self.edge_hostname = edge_hostname

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.edge_hostname:
            self.edge_hostname.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.certificates is not None:
            result['certificates'] = []
            for k in self.certificates:
                result['certificates'].append(k.to_map() if k else None)
        if self.edge_hostname is not None:
            result['edgeHostname'] = self.edge_hostname.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('certificates') is not None:
            self.certificates = []
            for k in m.get('certificates'):
                temp_model = CreatePropertyForMigrationRequestHostnamesCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('edgeHostname') is not None:
            temp_model = CreatePropertyForMigrationRequestHostnamesEdgeHostname()
            self.edge_hostname = temp_model.from_map(m['edgeHostname'])
        return self


class CreatePropertyForMigrationRequest(TeaModel):
    def __init__(
        self,
        service_type: str = None,
        property_comment: str = None,
        variables: str = None,
        property_name: str = None,
        version_comment: str = None,
        rules: str = None,
        hostnames: List[CreatePropertyForMigrationRequestHostnames] = None,
    ):
        # {"en":"Unique identifier for the product. Optional values include wsa, wsa-https.","zh_CN":"服务类型，对外产品的唯一标识。可选值: wsa, wsa-https"}
        self.service_type = service_type
        # {"en":"A descriptive comment for the property. The length must not exceed 256 characters.","zh_CN":"项目的描述。长度不超过256个字符。"}
        self.property_comment = property_comment
        # {"en":"The Variables feature allows you to define variables, assign values to them, and reuse them in functional test cases. A variable consists of a name and a value.","zh_CN":"变量"}
        self.variables = variables
        # {"en":"The name of the property. The length must not exceed 128 characters.","zh_CN":"项目的名称。长度不超过128个字符。"}
        self.property_name = property_name
        # {"en":"A descriptive comment for the property version. The length must not exceed 256 characters.","zh_CN":"版本描述。长度不超过256个字符。"}
        self.version_comment = version_comment
        # {"en":"Rules","zh_CN":"规则"}
        self.rules = rules
        # {"en":"hostnames","zh_CN":"域名列表"}
        self.hostnames = hostnames

    def validate(self):
        self.validate_required(self.hostnames, 'hostnames')
        if self.hostnames:
            for k in self.hostnames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.property_comment is not None:
            result['propertyComment'] = self.property_comment
        if self.variables is not None:
            result['variables'] = self.variables
        if self.property_name is not None:
            result['propertyName'] = self.property_name
        if self.version_comment is not None:
            result['versionComment'] = self.version_comment
        if self.rules is not None:
            result['rules'] = self.rules
        if self.hostnames is not None:
            result['hostnames'] = []
            for k in self.hostnames:
                result['hostnames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('propertyComment') is not None:
            self.property_comment = m.get('propertyComment')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        if m.get('propertyName') is not None:
            self.property_name = m.get('propertyName')
        if m.get('versionComment') is not None:
            self.version_comment = m.get('versionComment')
        if m.get('rules') is not None:
            self.rules = m.get('rules')
        if m.get('hostnames') is not None:
            self.hostnames = []
            for k in m.get('hostnames'):
                temp_model = CreatePropertyForMigrationRequestHostnames()
                self.hostnames.append(temp_model.from_map(k))
        return self


class CreatePropertyForMigrationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropertyForMigrationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropertyForMigrationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropertyForMigrationResponseData(TeaModel):
    def __init__(
        self,
        property_version: int = None,
        property_name: str = None,
        property_id: int = None,
    ):
        # {"en":"The version of the property.","zh_CN":"项目的版本"}
        self.property_version = property_version
        # {"en":"The name of the property.","zh_CN":"项目的名称"}
        self.property_name = property_name
        # {"en":"Property ID","zh_CN":"项目标识"}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_version, 'property_version')
        self.validate_required(self.property_name, 'property_name')
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_version is not None:
            result['propertyVersion'] = self.property_version
        if self.property_name is not None:
            result['propertyName'] = self.property_name
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyVersion') is not None:
            self.property_version = m.get('propertyVersion')
        if m.get('propertyName') is not None:
            self.property_name = m.get('propertyName')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class CreatePropertyForMigrationResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePropertyForMigrationResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreatePropertyForMigrationResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreatePropertyForMigrationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryHWAntiHotlinkingConfigRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRulesDecryptKey(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        expiry_time: str = None,
    ):
        # {"en":"Secret Key", "zh_CN":"解密秘钥内容"}
        self.secret_key = secret_key
        # {"en":"Secret Key", "zh_CN":"解密秘钥对应的过期时间，-1表示永不过期，入参格式精确到秒，例如：20180731100000"}
        self.expiry_time = expiry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['Secret Key'] = self.secret_key
        if self.expiry_time is not None:
            result['Expiry Time'] = self.expiry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Secret Key') is not None:
            self.secret_key = m.get('Secret Key')
        if m.get('Expiry Time') is not None:
            self.expiry_time = m.get('Expiry Time')
        return self


class QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRules(TeaModel):
    def __init__(
        self,
        data_id: int = None,
        path_pattern: str = None,
        except_path_pattern: str = None,
        forbidden_ips: str = None,
        allowed_ips: str = None,
        forbidden_method: str = None,
        allowed_method: str = None,
        decrypt_algorithm: str = None,
        decrypt_key: List[QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRulesDecryptKey] = None,
        cipher_expiry_time: str = None,
        authorize_to_origin_rules: str = None,
        authorize_method: str = None,
        authorize_url: str = None,
        authorize_pattern: str = None,
        authorize_key: str = None,
        authorize_cdn: str = None,
    ):
        # {"en":"When configuring multiple configuration sets, the specific configuration set's ID. The data-id can be obtained through the query interface. Note: a. If data-id is provided, it indicates the modification of a specific Configuration Item in one of the configuration sets. No modification is needed for other configuration sets. b. If multiple configuration sets are provided as input, and some have data-id while others do not, then those with data-id represent modifications to specific configuration sets, whereas those without data-id represent new configurations added on top of existing ones. c. If none of the inputs have data-id, it means the current configuration completely overrides the previous configuration. d. If no configuration parameters are provided and only the domain and secondary tag are transmitted, it indicates clearing all configurations corresponding to the domain's secondary service for this interface. e. If a configuration set has no specific Configuration Item, then data-id is required with an actual existing data-id value, indicating the clearing of the Configuration Item corresponding to this data-id. A configuration set with no specific Configuration Item and no data-id is not allowed.", "zh_CN":"配置多组配置时，具体某组配置的id。data-id可以通过查询接口获取。 注意： a、如果有传data-id，说明指定修改其中一组配置项内容，不需求修改其他组配置内容不需要入参；  b、如果入参多组配置，其中有些组配置有传data-id，有些没有传，则有传data-id的表示修改具体某组配置，没有传data-id的表示在原来基础上新增一组配置；  c、如果入参都没有传data-id,表示用本次的配置全量覆盖原先配置；  d、如果入参没有传任何配置项参数，只传了域名和二级标签，表示清空这个接口对应域名二级服务所有配置；  e、如果一组配置没有具体的配置项，则data-id必填，且值为实际存在的data-id，表示清空这个data-id对应配置项的值；不允许一组配置没有具体的配置项也没有data-id。"}
        self.data_id = data_id
        # {"en":"The url matching mode supports regularization. If all matches, the input parameters can be configured as: .*", "zh_CN":"url匹配模式，支持正则，如果是全部匹配，入参可以配置为：.*"}
        self.path_pattern = path_pattern
        # {"en":"Exceptional url matching mode, except for some URLs: such as abc.jpg, do not do anti-theft chain function
        # E.g: ^https?://[^/]+/.*\.m3u8", "zh_CN":"例外的url匹配模式，某些URL除外：如abc.jpg，不做防盗链功能
        # 客户入参参考：^https?://[^/]+/.*\.m3u8"}
        self.except_path_pattern = except_path_pattern
        # {"en":"Prohibited IP segment
        # Input parameter limit reference interface limit
        # Forbidden IP and exceptional IP cannot be configured at the same time", "zh_CN":"禁止的IP段
        # 支持输入IP或IP段，IP段之间用分号(;)隔开，如1.1.1.0/24;2.2.2.2
        # 禁止的IP和例外的IP，只能一个有值"}
        self.forbidden_ips = forbidden_ips
        # {"en":"The exception IP segment supports input IP or IP segment, and the IP segments are separated by a semicolon (;), such as 1.1.1.0/24; 2.2.2.2, some IP exceptions, no anti-theft chain", "zh_CN":"例外的IP段，支持输入IP或IP段，IP段之间用分号(;)隔开，如1.1.1.0/24;2.2.2.2，某些IP例外，不做防盗链"}
        self.allowed_ips = allowed_ips
        # {"en":"Forbidden Method", "zh_CN":"禁止的请求方法,组合入参：allowed-method判断，如果入参有allowed-method内容，则不允许配置forbidden-method。一个域名只能配置一种IP性质配置。 客户实际配置生效的是禁止的还是例外的，由最后一次入参的值决定，接口限制只能入参forbidden-method或allowed-method。如原先客户配置的是禁止的请求方法，本次入参是例外的请求方法，实际生效的是例外的请求方法 多个值用分号隔开 客户入参参考：get;post"}
        self.forbidden_method = forbidden_method
        # {"en":"Allowed Method", "zh_CN":"例外的请求方法,组合入参：allowed-method判断，如果入参有allowed-imethod内容，则不允许配置forbidden-imethod。一个域名只能配置一种IP性质配置。 客户实际配置生效的是禁止的还是例外的，由最后一次入参的值决定，接口限制只能入参forbidden-method或allowed-method。如原先客户配置的是禁止的请求方法，本次入参是例外的请求方法，实际生效的是例外的请求方法 多个值用分号隔开 客户入参参考：get"}
        self.allowed_method = allowed_method
        # {"en":"Decrypt Algorithm", "zh_CN":"解密算法，入参支持：空|aes-base64|aes-base64-level。 入参只能选择一种算法， 支持不传：不传就默认客户不用这个防盗链算法 如果传：aes-base64，表示点播算法； 如果传aes-base64-level，表示直播算法"}
        self.decrypt_algorithm = decrypt_algorithm
        # {"en":"Decrypt Key", "zh_CN":"秘钥集合，如果解密算法的入参不为空，则组内容不能为空。如果有多组秘钥信息，需要输入多组。一组内容包括：解密秘钥和秘钥过期时间 示例： <decrypt-key>-----一组秘钥信息    <secret-key>D915581AA2EF37B4</secret-key>    <expiry-time>-1</expiry-time> </decrypt-key> <decrypt-key>---一组秘钥信息    <secret-key>D915581AA2EF37B4</secret-key>    <expiry-time>20180731100000</expiry-time> </decrypt-key>"}
        self.decrypt_key = decrypt_key
        # {"en":"Cipher Expiry Time", "zh_CN":"防盗链过期时间：精确到秒，例如：5分钟过期，则入参为300。如果不传则是0，表示马上过期，"}
        self.cipher_expiry_time = cipher_expiry_time
        # {"en":"Authorize To Origin Rules", "zh_CN":"是否回源鉴权，支持不传，不传为空，如果传： true：表示要回源鉴权 false:不需要回源鉴权"}
        self.authorize_to_origin_rules = authorize_to_origin_rules
        # {"en":"Authorize Method", "zh_CN":"回源鉴权方式。支持入参：video、live。"}
        self.authorize_method = authorize_method
        # {"en":"Authorize Url", "zh_CN":"回源加密串取uri的url。支持正则输入。 入参参考： 点播:^https?://[^/]+((/?[^/]+/)+).*($|\?) 直播：^https?://([^/]+(/?[^/]+/)+[^\.]+).*($|\?)"}
        self.authorize_url = authorize_url
        # {"en":"Authorize Pattern", "zh_CN":"回源加密串取uri的字段，支持正则输入，例如：$1"}
        self.authorize_pattern = authorize_pattern
        # {"en":"Authorize Key", "zh_CN":"回源鉴权秘钥，入参参考：huawei"}
        self.authorize_key = authorize_key
        # {"en":"Authorize Cdn", "zh_CN":"回源参数hw_cdn的值：代表配置回源鉴权CDN厂家的标识。参考入参： 如果是解密算法是aes-base64-level，则回源参数hw_cdn的值，建议输入：ws-hw"}
        self.authorize_cdn = authorize_cdn

    def validate(self):
        if self.decrypt_key:
            for k in self.decrypt_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['data-id'] = self.data_id
        if self.path_pattern is not None:
            result['path-pattern'] = self.path_pattern
        if self.except_path_pattern is not None:
            result['except-path-pattern'] = self.except_path_pattern
        if self.forbidden_ips is not None:
            result['forbidden-ips'] = self.forbidden_ips
        if self.allowed_ips is not None:
            result['allowed-ips'] = self.allowed_ips
        if self.forbidden_method is not None:
            result['forbidden-method'] = self.forbidden_method
        if self.allowed_method is not None:
            result['allowed-method'] = self.allowed_method
        if self.decrypt_algorithm is not None:
            result['decrypt-algorithm'] = self.decrypt_algorithm
        if self.decrypt_key is not None:
            result['decrypt-key'] = []
            for k in self.decrypt_key:
                result['decrypt-key'].append(k.to_map() if k else None)
        if self.cipher_expiry_time is not None:
            result['cipher-expiry-time'] = self.cipher_expiry_time
        if self.authorize_to_origin_rules is not None:
            result['authorize-to-origin-rules'] = self.authorize_to_origin_rules
        if self.authorize_method is not None:
            result['authorize-method'] = self.authorize_method
        if self.authorize_url is not None:
            result['authorize-url'] = self.authorize_url
        if self.authorize_pattern is not None:
            result['authorize-pattern'] = self.authorize_pattern
        if self.authorize_key is not None:
            result['authorize-key'] = self.authorize_key
        if self.authorize_cdn is not None:
            result['authorize-cdn'] = self.authorize_cdn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data-id') is not None:
            self.data_id = m.get('data-id')
        if m.get('path-pattern') is not None:
            self.path_pattern = m.get('path-pattern')
        if m.get('except-path-pattern') is not None:
            self.except_path_pattern = m.get('except-path-pattern')
        if m.get('forbidden-ips') is not None:
            self.forbidden_ips = m.get('forbidden-ips')
        if m.get('allowed-ips') is not None:
            self.allowed_ips = m.get('allowed-ips')
        if m.get('forbidden-method') is not None:
            self.forbidden_method = m.get('forbidden-method')
        if m.get('allowed-method') is not None:
            self.allowed_method = m.get('allowed-method')
        if m.get('decrypt-algorithm') is not None:
            self.decrypt_algorithm = m.get('decrypt-algorithm')
        if m.get('decrypt-key') is not None:
            self.decrypt_key = []
            for k in m.get('decrypt-key'):
                temp_model = QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRulesDecryptKey()
                self.decrypt_key.append(temp_model.from_map(k))
        if m.get('cipher-expiry-time') is not None:
            self.cipher_expiry_time = m.get('cipher-expiry-time')
        if m.get('authorize-to-origin-rules') is not None:
            self.authorize_to_origin_rules = m.get('authorize-to-origin-rules')
        if m.get('authorize-method') is not None:
            self.authorize_method = m.get('authorize-method')
        if m.get('authorize-url') is not None:
            self.authorize_url = m.get('authorize-url')
        if m.get('authorize-pattern') is not None:
            self.authorize_pattern = m.get('authorize-pattern')
        if m.get('authorize-key') is not None:
            self.authorize_key = m.get('authorize-key')
        if m.get('authorize-cdn') is not None:
            self.authorize_cdn = m.get('authorize-cdn')
        return self


class QueryHWAntiHotlinkingConfigResponse(TeaModel):
    def __init__(
        self,
        huawei_visit_control_rules: List[QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRules] = None,
    ):
        # {"en":"Anti-theft chain configuration
        # note:
        # 1. When you need to cancel the anti-theft chain configuration settings, you can pass in the empty node <cache-time-behaviors></cache-time-behaviors>.
        # 2. When it is necessary to set the anti-theft chain configuration, this item is required.", "zh_CN":"防盗链配置
        # 注意：
        # 1. 需要取消防盗链配置设置时，可以传入空节点<cache-time-behaviors></cache-time-behaviors>。
        # 2. 表示需要设置防盗链配置时，此项必填"}
        self.huawei_visit_control_rules = huawei_visit_control_rules

    def validate(self):
        self.validate_required(self.huawei_visit_control_rules, 'huawei_visit_control_rules')
        if self.huawei_visit_control_rules:
            for k in self.huawei_visit_control_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.huawei_visit_control_rules is not None:
            result['huawei-visit-control-rules'] = []
            for k in self.huawei_visit_control_rules:
                result['huawei-visit-control-rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('huawei-visit-control-rules') is not None:
            self.huawei_visit_control_rules = []
            for k in m.get('huawei-visit-control-rules'):
                temp_model = QueryHWAntiHotlinkingConfigResponseHuaweiVisitControlRules()
                self.huawei_visit_control_rules.append(temp_model.from_map(k))
        return self


class QueryHWAntiHotlinkingConfigPaths(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"The domain name for the acceleration domain.", "zh_CN":"加速域名。"}
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


class QueryHWAntiHotlinkingConfigParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryHWAntiHotlinkingConfigRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryHWAntiHotlinkingConfigResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteRuleForWplusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteRuleForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteRuleForWplusPaths(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"rule ID","zh_CN":"规则ID"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleID'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleID') is not None:
            self.rule_id = m.get('ruleID')
        return self


class DeleteRuleForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteRuleForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class DeleteRuleForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChangeRuleStatusForWplusRequest(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # {"en":"The status of the rule.data range:enable,disable","zh_CN":"规则的状态，可选值：enable，disable"}
        self.status = status

    def validate(self):
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ChangeRuleStatusForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChangeRuleStatusForWplusPaths(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"rule ID","zh_CN":"规则ID"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class ChangeRuleStatusForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChangeRuleStatusForWplusResponseData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"Rule ID","zh_CN":"规则标识"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class ChangeRuleStatusForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ChangeRuleStatusForWplusResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ChangeRuleStatusForWplusResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ChangeRuleStatusForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryRuleForWplusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRuleForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRuleForWplusPaths(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"rule ID","zh_CN":"规则ID"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class QueryRuleForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRuleForWplusResponseDataAction(TeaModel):
    def __init__(
        self,
        name: str = None,
        options: str = None,
    ):
        # {"en":"Action name","zh_CN":"动作名称"}
        self.name = name
        # {"en":"Action options.","zh_CN":"动作参数。"}
        self.options = options

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.options, 'options')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        return self


class QueryRuleForWplusResponseData(TeaModel):
    def __init__(
        self,
        phase: str = None,
        condition: str = None,
        action: QueryRuleForWplusResponseDataAction = None,
        comment: str = None,
        rule_id: int = None,
        priority: int = None,
        enabled: bool = None,
    ):
        # {"en":"Phase,data range:connectPhase,requestPhase,cachePhase,originPhase,responsePhase","zh_CN":"阶段，可选值：connectPhase，requestPhase，cachePhase，originPhase，responsePhase"}
        self.phase = phase
        # {"en":"The condition in the rule","zh_CN":"规则中的条件表达式"}
        self.condition = condition
        # {"en":"Rule action","zh_CN":"规则动作"}
        self.action = action
        # {"en":"Comment","zh_CN":"规则的备注"}
        self.comment = comment
        # {"en":"The ID of the rule","zh_CN":"规则的标识"}
        self.rule_id = rule_id
        # {"en":"The priority of rule.","zh_CN":"规则排序"}
        self.priority = priority
        # {"en":"The state of rue.data range: false, true.","zh_CN":"规则状态。可选值：false，true。false为禁用，true为启用。"}
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.action, 'action')
        if self.action:
            self.action.validate()
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.condition is not None:
            result['condition'] = self.condition
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.priority is not None:
            result['priority'] = self.priority
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('action') is not None:
            temp_model = QueryRuleForWplusResponseDataAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class QueryRuleForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryRuleForWplusResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryRuleForWplusResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryRuleForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChangeRulePriorityForWplusRequest(TeaModel):
    def __init__(
        self,
        priority: int = None,
    ):
        # {"en":"The priority of the rule","zh_CN":"规则的顺序"}
        self.priority = priority

    def validate(self):
        self.validate_required(self.priority, 'priority')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self


class ChangeRulePriorityForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChangeRulePriorityForWplusPaths(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"rule ID","zh_CN":"规则ID"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class ChangeRulePriorityForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChangeRulePriorityForWplusResponseData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"Rule ID","zh_CN":"规则标识"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class ChangeRulePriorityForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ChangeRulePriorityForWplusResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ChangeRulePriorityForWplusResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ChangeRulePriorityForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateRuleForWplusRequestActionOptions(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateRuleForWplusRequestAction(TeaModel):
    def __init__(
        self,
        name: str = None,
        options: UpdateRuleForWplusRequestActionOptions = None,
    ):
        # {"en":"Action name","zh_CN":"动作名称"}
        self.name = name
        # {"en":"Action options.","zh_CN":"动作参数,详情查看schema接口"}
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            temp_model = UpdateRuleForWplusRequestActionOptions()
            self.options = temp_model.from_map(m['options'])
        return self


class UpdateRuleForWplusRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        condition: str = None,
        action: UpdateRuleForWplusRequestAction = None,
        comment: str = None,
        priority: int = None,
        enabled: bool = None,
    ):
        # {"en":"Phase,data range:connectPhase,requestPhase,cachePhase,originPhase,responsePhase","zh_CN":"阶段，可选值：connectPhase，requestPhase，cachePhase，originPhase，responsePhase"}
        self.phase = phase
        # {"en":"The condition in the rule","zh_CN":"规则中的条件表达式"}
        self.condition = condition
        # {"en":"Rule action","zh_CN":"规则动作"}
        self.action = action
        # {"en":"Comment","zh_CN":"备注"}
        self.comment = comment
        # {"en":"The priority of rule.default:1","zh_CN":"排序，默认值为1"}
        self.priority = priority
        # {"en":"The status of rule.data range: false, true.default:true","zh_CN":"状态。可选值：false，true。false为禁用，true为启用。默认值为true。"}
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.action, 'action')
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.condition is not None:
            result['condition'] = self.condition
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.priority is not None:
            result['priority'] = self.priority
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('action') is not None:
            temp_model = UpdateRuleForWplusRequestAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class UpdateRuleForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateRuleForWplusPaths(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"rule ID","zh_CN":"规则ID"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class UpdateRuleForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateRuleForWplusResponseData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"Rule ID","zh_CN":"规则标识"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class UpdateRuleForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateRuleForWplusResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateRuleForWplusResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateRuleForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateRuleForWplusRequestActionOptions(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRuleForWplusRequestAction(TeaModel):
    def __init__(
        self,
        name: str = None,
        options: CreateRuleForWplusRequestActionOptions = None,
    ):
        # {"en":"Action name","zh_CN":"动作名称"}
        self.name = name
        # {"en":"Action options.","zh_CN":"动作参数,详情查看schema接口"}
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            temp_model = CreateRuleForWplusRequestActionOptions()
            self.options = temp_model.from_map(m['options'])
        return self


class CreateRuleForWplusRequest(TeaModel):
    def __init__(
        self,
        phase: str = None,
        condition: str = None,
        action: CreateRuleForWplusRequestAction = None,
        comment: str = None,
        priority: int = None,
        enabled: bool = None,
    ):
        # {"en":"Phase,data range:connectPhase,requestPhase,cachePhase,originPhase,responsePhase","zh_CN":"阶段	，可选值：connectPhase，requestPhase，cachePhase，originPhase，responsePhase"}
        self.phase = phase
        # {"en":"The condition in the rule","zh_CN":"规则中的条件表达式"}
        self.condition = condition
        # {"en":"Rule action","zh_CN":"规则动作"}
        self.action = action
        # {"en":"Comment","zh_CN":"备注"}
        self.comment = comment
        # {"en":"The priority of rule.default:1","zh_CN":"规则排序，默认值为1"}
        self.priority = priority
        # {"en":"The state of rue.data range: true, false.default:true","zh_CN":"规则状态。可选值：false，true。false为禁用，true为启用。默认值为true。"}
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.action, 'action')
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.condition is not None:
            result['condition'] = self.condition
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.priority is not None:
            result['priority'] = self.priority
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('action') is not None:
            temp_model = CreateRuleForWplusRequestAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class CreateRuleForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRuleForWplusPaths(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        version: int = None,
    ):
        # {"en":"property ID","zh_CN":"项目ID"}
        self.property_id = property_id
        # {"en":"property version","zh_CN":"项目版本"}
        self.version = version

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateRuleForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRuleForWplusResponseData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # {"en":"Rule ID","zh_CN":"规则标识"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class CreateRuleForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateRuleForWplusResponseData = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.","zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response data.","zh_CN":"接口响应数据"}
        self.data = data
        # {"en":"Response error message if failed.","zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateRuleForWplusResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateRuleForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




