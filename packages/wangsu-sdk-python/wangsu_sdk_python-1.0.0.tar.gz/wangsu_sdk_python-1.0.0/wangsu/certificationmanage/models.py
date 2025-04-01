# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ReissueCertificateForWplusRequest(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        description: str = None,
        algorithm: str = None,
        validate_method: str = None,
        auto_validate: str = None,
        auto_deploy: str = None,
        common_name: str = None,
        subject_alternative_names: List[str] = None,
    ):
        # {"en":"Certificate id", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate description", "zh_CN":"证书描述"}
        self.description = description
        # {"en":"Certificate algorithm, RSA2048 or ECDSA256", "zh_CN":"证书算法，取值范围：RSA2048、ECDSA256"}
        self.algorithm = algorithm
        # {"en":"Certificate validate method, HTTP or DNS", "zh_CN":"验证方式，取值范围：HTTP、DNS"}
        self.validate_method = validate_method
        # {"en":"Is auto validate, true or false", "zh_CN":"是否自动验证，取值范围：true、false"}
        self.auto_validate = auto_validate
        # {"en":"Is auto deploy, true or false", "zh_CN":"是否自动部署，取值范围：true、false"}
        self.auto_deploy = auto_deploy
        # {"en":"Common name", "zh_CN":"通用名称"}
        self.common_name = common_name
        # {"en":"Subject alternative name", "zh_CN":"主体备用名称"}
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.validate_method, 'validate_method')
        self.validate_required(self.auto_validate, 'auto_validate')
        self.validate_required(self.auto_deploy, 'auto_deploy')
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.description is not None:
            result['description'] = self.description
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.validate_method is not None:
            result['validateMethod'] = self.validate_method
        if self.auto_validate is not None:
            result['autoValidate'] = self.auto_validate
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('validateMethod') is not None:
            self.validate_method = m.get('validateMethod')
        if m.get('autoValidate') is not None:
            self.auto_validate = m.get('autoValidate')
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        return self


class ReissueCertificateForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message
        # {"en":"Sale order id", "zh_CN":"销售订单id"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ReissueCertificateForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReissueCertificateForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReissueCertificateForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReissueCertificateForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetCertificateContentRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCertificateContentResponse(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        name: str = None,
        comment: str = None,
        share_ssl: bool = None,
        ssl_certificate: str = None,
        ssl_key: str = None,
        ssl_certificate_chain: str = None,
    ):
        # {"en":"certificate id", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"The certificate name is unique under a customer.
        # Note:
        # 1. Support single domain, multi domain and wildcard domain name.
        # 2. For example, the authorized domain name of certificate A is *.example.com , a.example2.com, b.example2.com test.example.com , a.example2.com, can be associated with certificate A, while the domain name c.example2.com cannot use certificate A.", "zh_CN":"证书名称，客户粒度下是唯一的
        # 
        # 注意：
        # 1、支持单域名、多域名和泛域名证书，即证书的授权域名允许为多个域名，或者泛域名
        # 2、例如：证书A的授权域名为 *.example.com，a.example2.com，b.example2.com，则域名test.example.com，a.example2.com，都可以关联使用证书A，而域名c.example2.com不能使用证书A"}
        self.name = name
        # {"en":"Comment for a certificate.", "zh_CN":"证书文件的备注"}
        self.comment = comment
        # {"en":"Specified a shared certificate. True means shared.", "zh_CN":"是否共享，true表示共享证书，false表示非共享证书"}
        self.share_ssl = share_ssl
        # {"en":"Certificate content. The encryption algorithm is the same as the creating a certificate.
        # Encryption algorithm: First get md5 value of the request header 'Date'. Then take the left 8 bits of MD5 value as the key and the right 8 bits as the IV. At lase, encode the encrypted binary content with Base64. For example:
        # date=`env LANG=\"en_US.UTF-8\" date -u \"+%a, %d %b %Y %H:%M:%S GMT\"`
        # md5str=`echo -n $date | openssl md5`
        # key=`echo -n ${md5str:$((-32)):$((8))}|hexdump -e '8/1 \"%02X\"'`
        # iv=`echo -n ${md5str:$((-8))}|hexdump -e '8/1 \"%02X\"'`
        # Note:
        # 1.Decryption command: file is the content of the certificate file (CRT, key, CA) responded by the interface
        # cat $file |base64 -d|openssl enc -des -K $key -iv $iv -nosalt -d
        # 2. The date time of the HTTP request header must be the same as that of the above certificate encryption.", "zh_CN":"crt文件内容，已加密。加密算法同新增证书的加密算法。
        # 加密算法说明：将http头中的Date值做md5运算，将md5值的左8位作为key，右8位作为iv，然后对文件内容作des加密，将加密后的二进制内容作base64编码，以下为示例参考：
        # date=`env LANG=\"en_US.UTF-8\" date -u \"+%a, %d %b %Y %H:%M:%S GMT\"`
        # md5str=`echo -n $date | openssl md5`
        # key=`echo -n ${md5str:$((-32)):$((8))}|hexdump -e '8/1 \"%02X\"'`
        # iv=`echo -n ${md5str:$((-8))}|hexdump -e '8/1 \"%02X\"'`
        # 注意：
        # 1、解密命令如下，file就是接口响应的证书文件内容（crt，key，ca）
        # cat $file |base64 -d|openssl enc -des -K $key -iv $iv -nosalt -d
        # 2、http请求头的Date时间必须和上述证书加解密的时间一致"}
        self.ssl_certificate = ssl_certificate
        # {"en":"Certificate key. The encryption algorithm is the same as creating a  new certificate", "zh_CN":"key文件内容，已加密。加密算法同新增证书的加密算法。"}
        self.ssl_key = ssl_key
        # {"en":"Certificate chain. The encryption algorithm is the same as the new certificate.", "zh_CN":"ca文件内容，已加密。加密方式同新增证书的加密方式。"}
        self.ssl_certificate_chain = ssl_certificate_chain

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.share_ssl, 'share_ssl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificate-id'] = self.certificate_id
        if self.name is not None:
            result['name'] = self.name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.share_ssl is not None:
            result['share-ssl:'] = self.share_ssl
        if self.ssl_certificate is not None:
            result['ssl-certificate'] = self.ssl_certificate
        if self.ssl_key is not None:
            result['ssl-key'] = self.ssl_key
        if self.ssl_certificate_chain is not None:
            result['ssl-certificate-chain'] = self.ssl_certificate_chain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificate-id') is not None:
            self.certificate_id = m.get('certificate-id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('share-ssl:') is not None:
            self.share_ssl = m.get('share-ssl:')
        if m.get('ssl-certificate') is not None:
            self.ssl_certificate = m.get('ssl-certificate')
        if m.get('ssl-key') is not None:
            self.ssl_key = m.get('ssl-key')
        if m.get('ssl-certificate-chain') is not None:
            self.ssl_certificate_chain = m.get('ssl-certificate-chain')
        return self


class GetCertificateContentPaths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"Certificate ID, corresponding to the* in the interface address", "zh_CN":"证书ID，对应接口url中的*\
        # 注意：参看请求示例中的url，100166对应的就是certificate-id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificate-id'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificate-id') is not None:
            self.certificate_id = m.get('certificate-id')
        return self


class GetCertificateContentParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCertificateContentRequestHeader(TeaModel):
    def __init__(
        self,
        date: str = None,
    ):
        # {"en":"Date.  Formatting to comply with RFC 1123 specifications as for Thu, 17 May 2012 19:37:58 GMT ", "zh_CN":"时间戳，格式需符合RFC 1123规范，如Thu, 17 May 2012 19:37:58 GMT "}
        self.date = date

    def validate(self):
        self.validate_required(self.date, 'date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        return self


class GetCertificateContentResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDomainMultiCertConfigRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainMultiCertConfigCertInfo(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        certificate_name: str = None,
        comment: str = None,
        serial: str = None,
    ):
        # {"en":"certificateId", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"certificateName", "zh_CN":"证书名称"}
        self.certificate_name = certificate_name
        # {"en":"comment", "zh_CN":"备注"}
        self.comment = comment
        # {"en":"serial", "zh_CN":"序列号"}
        self.serial = serial

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.serial, 'serial')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.serial is not None:
            result['serial'] = self.serial
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('serial') is not None:
            self.serial = m.get('serial')
        return self


class QueryDomainMultiCertConfigDomainCertConfig(TeaModel):
    def __init__(
        self,
        cert_usage: str = None,
        cert_infos: List[QueryDomainMultiCertConfigCertInfo] = None,
    ):
        # {"en":"certUsage", "zh_CN":"证书用途 "}
        self.cert_usage = cert_usage
        # {"en":"certInfos", "zh_CN":"证书信息"}
        self.cert_infos = cert_infos

    def validate(self):
        self.validate_required(self.cert_usage, 'cert_usage')
        self.validate_required(self.cert_infos, 'cert_infos')
        if self.cert_infos:
            for k in self.cert_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_usage is not None:
            result['certUsage'] = self.cert_usage
        if self.cert_infos is not None:
            result['certInfos'] = []
            for k in self.cert_infos:
                result['certInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certUsage') is not None:
            self.cert_usage = m.get('certUsage')
        if m.get('certInfos') is not None:
            self.cert_infos = []
            for k in m.get('certInfos'):
                temp_model = QueryDomainMultiCertConfigCertInfo()
                self.cert_infos.append(temp_model.from_map(k))
        return self


class QueryDomainMultiCertConfigData(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
        tlsversion: str = None,
        enable_ocsp: str = None,
        cipher_suites: str = None,
        domain_cert_configs: List[QueryDomainMultiCertConfigDomainCertConfig] = None,
    ):
        # {"en":"domainId", "zh_CN":"域名ID"}
        self.domain_id = domain_id
        # {"en":"domainName", "zh_CN":"域名名称"}
        self.domain_name = domain_name
        # {"en":"TLSVersion", "zh_CN":"TLS版本"}
        self.tlsversion = tlsversion
        # {"en":"enableOCSP", "zh_CN":"启用OCSP，默认不启用，可选值true、false。没配置返回"}
        self.enable_ocsp = enable_ocsp
        # {"en":"cipherSuites", "zh_CN":"设置cipher加密套件"}
        self.cipher_suites = cipher_suites
        # {"en":"domainCertConfigs", "zh_CN":"证书配置"}
        self.domain_cert_configs = domain_cert_configs

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.tlsversion, 'tlsversion')
        self.validate_required(self.enable_ocsp, 'enable_ocsp')
        self.validate_required(self.cipher_suites, 'cipher_suites')
        self.validate_required(self.domain_cert_configs, 'domain_cert_configs')
        if self.domain_cert_configs:
            for k in self.domain_cert_configs:
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
        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion
        if self.enable_ocsp is not None:
            result['enableOCSP'] = self.enable_ocsp
        if self.cipher_suites is not None:
            result['cipherSuites'] = self.cipher_suites
        if self.domain_cert_configs is not None:
            result['domainCertConfigs'] = []
            for k in self.domain_cert_configs:
                result['domainCertConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('enableOCSP') is not None:
            self.enable_ocsp = m.get('enableOCSP')
        if m.get('cipherSuites') is not None:
            self.cipher_suites = m.get('cipherSuites')
        if m.get('domainCertConfigs') is not None:
            self.domain_cert_configs = []
            for k in m.get('domainCertConfigs'):
                temp_model = QueryDomainMultiCertConfigDomainCertConfig()
                self.domain_cert_configs.append(temp_model.from_map(k))
        return self


class QueryDomainMultiCertConfigResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryDomainMultiCertConfigData = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"message", "zh_CN":"结果信息"}
        self.message = message
        # {"en":"data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryDomainMultiCertConfigData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryDomainMultiCertConfigPaths(TeaModel):
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


class QueryDomainMultiCertConfigParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainMultiCertConfigRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDomainMultiCertConfigResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteCertificateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCertificateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[str] = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteCertificatePaths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to delete.", "zh_CN":"需要删除的证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class DeleteCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DownloadConfirmLetterTemplateForWplusRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        purchase_record_id: str = None,
    ):
        # {"en":"orderId", "zh_CN":"订单id"}
        self.order_id = order_id
        # {"en":"purchaseRecordId", "zh_CN":"采购记录ID"}
        self.purchase_record_id = purchase_record_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.purchase_record_id, 'purchase_record_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.purchase_record_id is not None:
            result['purchaseRecordId'] = self.purchase_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('purchaseRecordId') is not None:
            self.purchase_record_id = m.get('purchaseRecordId')
        return self


class DownloadConfirmLetterTemplateForWplusDataContent(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_data: str = None,
    ):
        # {"en":"fileName", "zh_CN":"信息确认函模板名称"}
        self.file_name = file_name
        # {"en":"fileData", "zh_CN":"信息确认函模板内容"}
        self.file_data = file_data

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_data, 'file_data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_data is not None:
            result['fileData'] = self.file_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileData') is not None:
            self.file_data = m.get('fileData')
        return self


class DownloadConfirmLetterTemplateForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: DownloadConfirmLetterTemplateForWplusDataContent = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message
        # {"en":"data", "zh_CN":"订单详情"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = DownloadConfirmLetterTemplateForWplusDataContent()
            self.data = temp_model.from_map(m['data'])
        return self


class DownloadConfirmLetterTemplateForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadConfirmLetterTemplateForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadConfirmLetterTemplateForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadConfirmLetterTemplateForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UploadConfirmLetterForWplusRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        purchase_record_id: str = None,
        file_data: str = None,
    ):
        # {"en":"orderId", "zh_CN":"订单id"}
        self.order_id = order_id
        # {"en":"purchaseRecordId", "zh_CN":"采购记录ID"}
        self.purchase_record_id = purchase_record_id
        # {"en":"fileData", "zh_CN":"信息确认函内容"}
        self.file_data = file_data

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.purchase_record_id, 'purchase_record_id')
        self.validate_required(self.file_data, 'file_data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.purchase_record_id is not None:
            result['purchaseRecordId'] = self.purchase_record_id
        if self.file_data is not None:
            result['fileData'] = self.file_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('purchaseRecordId') is not None:
            self.purchase_record_id = m.get('purchaseRecordId')
        if m.get('fileData') is not None:
            self.file_data = m.get('fileData')
        return self


class UploadConfirmLetterForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
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


class UploadConfirmLetterForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UploadConfirmLetterForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UploadConfirmLetterForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UploadConfirmLetterForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RevokeCertificateServiceForWplusRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # {"en":"certificateId", "zh_CN":"证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class RevokeCertificateServiceForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
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


class RevokeCertificateServiceForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RevokeCertificateServiceForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RevokeCertificateServiceForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RevokeCertificateServiceForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCertificateRelatedDomainsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateRelatedDomainsResponseDataDomains(TeaModel):
    def __init__(
        self,
        domain_id: int = None,
        domain_name: str = None,
    ):
        # {"en":"Domain ID", "zh_CN":"域名id"}
        self.domain_id = domain_id
        # {"en":"Domain name", "zh_CN":"域名名称"}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        return self


class QueryCertificateRelatedDomainsResponseData(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        domains: List[QueryCertificateRelatedDomainsResponseDataDomains] = None,
    ):
        # {"en":"Certificate ID", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate related domains", "zh_CN":"在用该证书的加速域名列表"}
        self.domains = domains

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.domains is not None:
            result['domains'] = []
            for k in self.domains:
                result['domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('domains') is not None:
            self.domains = []
            for k in m.get('domains'):
                temp_model = QueryCertificateRelatedDomainsResponseDataDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class QueryCertificateRelatedDomainsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: QueryCertificateRelatedDomainsResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryCertificateRelatedDomainsResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCertificateRelatedDomainsPaths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to query.", "zh_CN":"需要查询的证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class QueryCertificateRelatedDomainsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateRelatedDomainsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateRelatedDomainsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddGmCertificateForWplusCertificate(TeaModel):
    def __init__(
        self,
        name: str = None,
        comment: str = None,
        certificate: str = None,
        private_key: str = None,
    ):
        # {"en":"name", "zh_CN":"证书名"}
        self.name = name
        # {"en":"comment", "zh_CN":"描述"}
        self.comment = comment
        # {"en":"certificate", "zh_CN":"crt内容"}
        self.certificate = certificate
        # {"en":"privateKey", "zh_CN":"私钥内容"}
        self.private_key = private_key

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.certificate, 'certificate')
        self.validate_required(self.private_key, 'private_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        return self


class AddGmCertificateForWplusRequest(TeaModel):
    def __init__(
        self,
        signature_certificate: AddGmCertificateForWplusCertificate = None,
        encryption_certificate: AddGmCertificateForWplusCertificate = None,
    ):
        # {"en":"Signature certificate info", "zh_CN":"签名证书信息"}
        self.signature_certificate = signature_certificate
        # {"en":"Encryption certificate info", "zh_CN":"加密证书信息"}
        self.encryption_certificate = encryption_certificate

    def validate(self):
        self.validate_required(self.signature_certificate, 'signature_certificate')
        if self.signature_certificate:
            self.signature_certificate.validate()
        self.validate_required(self.encryption_certificate, 'encryption_certificate')
        if self.encryption_certificate:
            self.encryption_certificate.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_certificate is not None:
            result['signatureCertificate'] = self.signature_certificate.to_map()
        if self.encryption_certificate is not None:
            result['encryptionCertificate'] = self.encryption_certificate.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('signatureCertificate') is not None:
            temp_model = AddGmCertificateForWplusCertificate()
            self.signature_certificate = temp_model.from_map(m['signatureCertificate'])
        if m.get('encryptionCertificate') is not None:
            temp_model = AddGmCertificateForWplusCertificate()
            self.encryption_certificate = temp_model.from_map(m['encryptionCertificate'])
        return self


class AddGmCertificateForWplusResp(TeaModel):
    def __init__(
        self,
        signature_certificate_id: str = None,
        encryption_certificate_id: str = None,
    ):
        # {"en":"signature certificate id", "zh_CN":"签名证书id"}
        self.signature_certificate_id = signature_certificate_id
        # {"en":"encryption certificate id", "zh_CN":"加密证书id"}
        self.encryption_certificate_id = encryption_certificate_id

    def validate(self):
        self.validate_required(self.signature_certificate_id, 'signature_certificate_id')
        self.validate_required(self.encryption_certificate_id, 'encryption_certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_certificate_id is not None:
            result['signatureCertificateId'] = self.signature_certificate_id
        if self.encryption_certificate_id is not None:
            result['encryptionCertificateId'] = self.encryption_certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('signatureCertificateId') is not None:
            self.signature_certificate_id = m.get('signatureCertificateId')
        if m.get('encryptionCertificateId') is not None:
            self.encryption_certificate_id = m.get('encryptionCertificateId')
        return self


class AddGmCertificateForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: AddGmCertificateForWplusResp = None,
    ):
        # {"en":"code", "zh_CN":"错误码，成功为0"}
        self.code = code
        # {"en":"error message", "zh_CN":"错误信息"}
        self.message = message
        # {"en":"data", "zh_CN":"响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = AddGmCertificateForWplusResp()
            self.data = temp_model.from_map(m['data'])
        return self


class AddGmCertificateForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddGmCertificateForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddGmCertificateForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddGmCertificateForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCertificateInfoRequest(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to query.", "zh_CN":"指定要查询的证书ID，在URI上"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class QueryCertificateInfoResponseDataSubjectAlternativeNames(TeaModel):
    def __init__(
        self,
        subject_alternative_name: str = None,
    ):
        # {"en":"Subject Alternative Name", "zh_CN":"证书绑定的附加域名"}
        self.subject_alternative_name = subject_alternative_name

    def validate(self):
        self.validate_required(self.subject_alternative_name, 'subject_alternative_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subject_alternative_name is not None:
            result['subjectAlternativeName'] = self.subject_alternative_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subjectAlternativeName') is not None:
            self.subject_alternative_name = m.get('subjectAlternativeName')
        return self


class QueryCertificateInfoResponseData(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        name: str = None,
        comment: str = None,
        serial: str = None,
        not_before: str = None,
        not_after: str = None,
        common_name: str = None,
        subject_alternative_names: List[QueryCertificateInfoResponseDataSubjectAlternativeNames] = None,
    ):
        # {"en":"certificate Id", "zh_CN":"证书ID。"}
        self.certificate_id = certificate_id
        # {"en":"certificate name", "zh_CN":"证书名称。"}
        self.name = name
        # {"en":"comment", "zh_CN":"备注信息。"}
        self.comment = comment
        # {"en":"certificate serial", "zh_CN":"证书序列号。"}
        self.serial = serial
        # {"en":"not befoe", "zh_CN":"签发时间。"}
        self.not_before = not_before
        # {"en":"not after", "zh_CN":"到期时间。"}
        self.not_after = not_after
        # {"en":"common name", "zh_CN":"证书绑定的主域名。"}
        self.common_name = common_name
        # {"en":"Subject Alternative Names", "zh_CN":"证书绑定的附加域名列表。"}
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.serial, 'serial')
        self.validate_required(self.not_before, 'not_before')
        self.validate_required(self.not_after, 'not_after')
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')
        if self.subject_alternative_names:
            for k in self.subject_alternative_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.name is not None:
            result['name'] = self.name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.serial is not None:
            result['serial'] = self.serial
        if self.not_before is not None:
            result['notBefore'] = self.not_before
        if self.not_after is not None:
            result['notAfter'] = self.not_after
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = []
            for k in self.subject_alternative_names:
                result['subjectAlternativeNames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('serial') is not None:
            self.serial = m.get('serial')
        if m.get('notBefore') is not None:
            self.not_before = m.get('notBefore')
        if m.get('notAfter') is not None:
            self.not_after = m.get('notAfter')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = []
            for k in m.get('subjectAlternativeNames'):
                temp_model = QueryCertificateInfoResponseDataSubjectAlternativeNames()
                self.subject_alternative_names.append(temp_model.from_map(k))
        return self


class QueryCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: QueryCertificateInfoResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryCertificateInfoResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCertificateInfoPaths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to query.", "zh_CN":"需要查询的证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class QueryCertificateInfoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCertificateListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateListResponseSslCertificatesRelatedDomains(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
    ):
        # {"en":"Accelerated domain name ID", "zh_CN":"加速域名ID"}
        self.domain_id = domain_id
        # {"en":"Name of accelerated domain name", "zh_CN":"加速域名的名称"}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain-id'] = self.domain_id
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-id') is not None:
            self.domain_id = m.get('domain-id')
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        return self


class QueryCertificateListResponseSslCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        name: str = None,
        comment: str = None,
        share_ssl: str = None,
        certificate_validity_from: str = None,
        certificate_validity_to: str = None,
        related_domains: List[QueryCertificateListResponseSslCertificatesRelatedDomains] = None,
        dns_names: List[str] = None,
        certificate_serial: str = None,
        crt_md_5: str = None,
        key_md_5: str = None,
        ca_md_5: str = None,
        certificate_issuer: str = None,
    ):
        # {"en":"Certificate ID", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate name, unique to customer granularity", "zh_CN":"证书名称，客户粒度下是唯一的"}
        self.name = name
        # {"en":"Remarks on cerfiticate file", "zh_CN":"证书文件的备注"}
        self.comment = comment
        # {"en":"Shared, optional values are true and false, true represents shared certificates, false represents unshared certificates, default is false
        # This certificate allows cross-customer use when share-ssl is true. (The API does not support cross-customer use certificates. Contact customer service for manual configuration if required.)", "zh_CN":"是否共享，true表示共享证书，false表示非共享证书"}
        self.share_ssl = share_ssl
        # {"en":"Certificate effective start time (CST), such as 2016-08-01 07:00:00", "zh_CN":"证书有效期的起始时间（CST时区），例如：2016-08-01 07:00:00"}
        self.certificate_validity_from = certificate_validity_from
        # {"en":"Certificate effective end time (CST), such as 2018-08-01 19:00:00", "zh_CN":"证书有效期的到期时间（CST时区），例如：2018-08-01 19:00:00"}
        self.certificate_validity_to = certificate_validity_to
        # {"en":"List of domain names using the current certificate", "zh_CN":"使用当前证书的域名列表"}
        self.related_domains = related_domains
        # {"en":"dns-names", "zh_CN":"授权域名列表，证书使用者可选名称，父标签"}
        self.dns_names = dns_names
        # {"en":"The CRT certificate serial number", "zh_CN":"crt证书序列号"}
        self.certificate_serial = certificate_serial
        # {"en":"The MD5 value of CRT file.", "zh_CN":"CRT文件内容的md5值。"}
        self.crt_md_5 = crt_md_5
        # {"en":"The MD5 value of KEY file.", "zh_CN":"KEY文件内容的md5值。"}
        self.key_md_5 = key_md_5
        # {"en":"The MD5 value of CA file.", "zh_CN":"CA。"}
        self.ca_md_5 = ca_md_5
        # {"en":"The CRT certificate issuer", "zh_CN":"crt证书颁布者"}
        self.certificate_issuer = certificate_issuer

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.share_ssl, 'share_ssl')
        self.validate_required(self.certificate_validity_from, 'certificate_validity_from')
        self.validate_required(self.certificate_validity_to, 'certificate_validity_to')
        self.validate_required(self.related_domains, 'related_domains')
        if self.related_domains:
            for k in self.related_domains:
                if k:
                    k.validate()
        self.validate_required(self.dns_names, 'dns_names')
        self.validate_required(self.certificate_serial, 'certificate_serial')
        self.validate_required(self.crt_md_5, 'crt_md_5')
        self.validate_required(self.key_md_5, 'key_md_5')
        self.validate_required(self.ca_md_5, 'ca_md_5')
        self.validate_required(self.certificate_issuer, 'certificate_issuer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificate-id'] = self.certificate_id
        if self.name is not None:
            result['name'] = self.name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.share_ssl is not None:
            result['share-ssl'] = self.share_ssl
        if self.certificate_validity_from is not None:
            result['certificate-validity-from'] = self.certificate_validity_from
        if self.certificate_validity_to is not None:
            result['certificate-validity-to'] = self.certificate_validity_to
        if self.related_domains is not None:
            result['related-domains'] = []
            for k in self.related_domains:
                result['related-domains'].append(k.to_map() if k else None)
        if self.dns_names is not None:
            result['dns-names'] = self.dns_names
        if self.certificate_serial is not None:
            result['certificate-serial'] = self.certificate_serial
        if self.crt_md_5 is not None:
            result['crt-md5'] = self.crt_md_5
        if self.key_md_5 is not None:
            result['key-md5'] = self.key_md_5
        if self.ca_md_5 is not None:
            result['ca-md5'] = self.ca_md_5
        if self.certificate_issuer is not None:
            result['certificate-issuer'] = self.certificate_issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificate-id') is not None:
            self.certificate_id = m.get('certificate-id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('share-ssl') is not None:
            self.share_ssl = m.get('share-ssl')
        if m.get('certificate-validity-from') is not None:
            self.certificate_validity_from = m.get('certificate-validity-from')
        if m.get('certificate-validity-to') is not None:
            self.certificate_validity_to = m.get('certificate-validity-to')
        if m.get('related-domains') is not None:
            self.related_domains = []
            for k in m.get('related-domains'):
                temp_model = QueryCertificateListResponseSslCertificatesRelatedDomains()
                self.related_domains.append(temp_model.from_map(k))
        if m.get('dns-names') is not None:
            self.dns_names = m.get('dns-names')
        if m.get('certificate-serial') is not None:
            self.certificate_serial = m.get('certificate-serial')
        if m.get('crt-md5') is not None:
            self.crt_md_5 = m.get('crt-md5')
        if m.get('key-md5') is not None:
            self.key_md_5 = m.get('key-md5')
        if m.get('ca-md5') is not None:
            self.ca_md_5 = m.get('ca-md5')
        if m.get('certificate-issuer') is not None:
            self.certificate_issuer = m.get('certificate-issuer')
        return self


class QueryCertificateListResponse(TeaModel):
    def __init__(
        self,
        ssl_certificates: List[QueryCertificateListResponseSslCertificates] = None,
    ):
        # {"en":"Certificate list information", "zh_CN":"证书列表信息"}
        self.ssl_certificates = ssl_certificates

    def validate(self):
        self.validate_required(self.ssl_certificates, 'ssl_certificates')
        if self.ssl_certificates:
            for k in self.ssl_certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_certificates is not None:
            result['ssl-certificates'] = []
            for k in self.ssl_certificates:
                result['ssl-certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ssl-certificates') is not None:
            self.ssl_certificates = []
            for k in m.get('ssl-certificates'):
                temp_model = QueryCertificateListResponseSslCertificates()
                self.ssl_certificates.append(temp_model.from_map(k))
        return self


class QueryCertificateListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCertificateContentRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateContentResponseData(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
        certificate: str = None,
    ):
        # {"en":"Certificate ID", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate content", "zh_CN":"证书内容，PEM格式"}
        self.certificate = certificate

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate, 'certificate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate is not None:
            result['certificate'] = self.certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        return self


class QueryCertificateContentResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: QueryCertificateContentResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryCertificateContentResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCertificateContentPaths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to query.", "zh_CN":"需要查询的证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class QueryCertificateContentParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateContentRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateContentResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditCertificateV2Request(TeaModel):
    def __init__(
        self,
        name: str = None,
        certificate: str = None,
        private_key: str = None,
        auto_renew: str = None,
        is_need_alarm: str = None,
        csr_id: int = None,
        comment: str = None,
    ):
        # {"en":"Certificate name", "zh_CN":"证书名称"}
        self.name = name
        # {"en":"Certificate, PEM certificate.", "zh_CN":"证书内容，PEM格式。例如：
        # -----BEGIN CERTIFICATE-----\
        # ……
        # -----END CERTIFICATE-----"}
        self.certificate = certificate
        # {"en":"Private key of the certificate, PEM certificate. Not required when you specify a csrId.", "zh_CN":"证书密钥，PEM格式。例如：
        # -----BEGIN RSA PRIVATE KEY-----\
        # ……
        # -----BEGIN RSA PRIVATE KEY-----"}
        self.private_key = private_key
        # {"en":"Automatically renew", "zh_CN":"是否自动续签，取值范围false或者true"}
        self.auto_renew = auto_renew
        # {"en":"Do you want to send an expiration alarm", "zh_CN":"是否需要证书过期告警，取值范围false或者true"}
        self.is_need_alarm = is_need_alarm
        # {"en":"Csr ID, the id returned by the interface "Create CSR".", "zh_CN":"csrId，证书申请文件的id"}
        self.csr_id = csr_id
        # {"en":"Comment", "zh_CN":"备注信息"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.is_need_alarm is not None:
            result['isNeedAlarm'] = self.is_need_alarm
        if self.csr_id is not None:
            result['csrId'] = self.csr_id
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('isNeedAlarm') is not None:
            self.is_need_alarm = m.get('isNeedAlarm')
        if m.get('csrId') is not None:
            self.csr_id = m.get('csrId')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class EditCertificateV2Response(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class EditCertificateV2Paths(TeaModel):
    def __init__(
        self,
        certificate_id: int = None,
    ):
        # {"en":"The certificate ID you want to modify.", "zh_CN":"需要修改的证书id"}
        self.certificate_id = certificate_id

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        return self


class EditCertificateV2Parameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditCertificateV2RequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditCertificateV2ResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddCertificateServiceV2Request(TeaModel):
    def __init__(
        self,
        name: str = None,
        certificate: str = None,
        private_key: str = None,
        csr_id: int = None,
        comment: str = None,
    ):
        # {"en":"Certificate name", "zh_CN":"证书名称"}
        self.name = name
        # {"en":"Certificate, PEM certificate, including CRT file and CA file.", "zh_CN":"证书内容，PEM格式，包含CRT文件、CA文件。例如：
        # -----BEGIN CERTIFICATE-----\
        # ……
        # -----END CERTIFICATE-----"}
        self.certificate = certificate
        # {"en":"Private key of the certificate, PEM certificate. Not required when you specify a csrId.", "zh_CN":"证书密钥，PEM格式。例如：
        # -----BEGIN RSA PRIVATE KEY-----\
        # ……
        # -----BEGIN RSA PRIVATE KEY-----\
        # 当指定csrId时，无需上传证书密钥。"}
        self.private_key = private_key
        # {"en":"Csr ID, the id returned by the interface \"Create CSR\".", "zh_CN":"csrId，证书申请文件的id。"}
        self.csr_id = csr_id
        # {"en":"comment", "zh_CN":"备注"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.certificate, 'certificate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        if self.csr_id is not None:
            result['csrId'] = self.csr_id
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        if m.get('csrId') is not None:
            self.csr_id = m.get('csrId')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class AddCertificateServiceV2Response(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"响应信息"}
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


class AddCertificateServiceV2Paths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddCertificateServiceV2Parameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddCertificateServiceV2RequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddCertificateServiceV2ResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The URL used to access the certificate file where certificate-id is the unique token that the system generates for the certificate and whose value is a string", "zh_CN":"用于访问该证书文件的URL，其中certificate-id为系统为该证书生成的唯一标示，其值为字符串"}
        self.location = location

    def validate(self):
        self.validate_required(self.location, 'location')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        return self




