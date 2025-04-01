# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetACertificatePaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # {"en":"ID of the certificate.","zh_CN": "证书ID。"}
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


class GetACertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateResponseVersions(TeaModel):
    def __init__(
        self,
        version: int = None,
        type: str = None,
        expiration_time: str = None,
        creation_time: str = None,
        fingerprint: str = None,
        comments: str = None,
    ):
        # {"en" : "Range: >= 1 
        # Indicates the version number.", "zh_CN": "取值范围: >= 1 
        # 证书的版本号。"}
        self.version = version
        # {"en" : "Enum: uploaded,selfsigned 
        # Indicates the type of certificate, either 'uploaded' or 'self-signed'.", "zh_CN": "取值范围: uploaded,selfsigned 
        # 证书类型，包括'上传'和'自签名'2种类型。"}
        self.type = type
        # {"en" : "RFC 3339 format string indicating when the certificate expires.", "zh_CN": "RFC3339格式的日期，表示证书的过期时间。"}
        self.expiration_time = expiration_time
        # {"en" : "RFC 3339 format string indicating when the certificate was created.", "zh_CN": "RFC3339格式的日期，表示证书的创建时间。"}
        self.creation_time = creation_time
        # {"en" : "A unique fingerprint associated with the certificate.
        # ", "zh_CN": "与证书关联的唯一指纹。"}
        self.fingerprint = fingerprint
        # {"en" : "Comments about the certificate version.", "zh_CN": "证书版本的描述。"}
        self.comments = comments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.type is not None:
            result['type'] = self.type
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.comments is not None:
            result['comments'] = self.comments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('comments') is not None:
            self.comments = m.get('comments')
        return self


class GetACertificateResponseUsageInProduction(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        hostnames: List[str] = None,
        origins: List[str] = None,
    ):
        # {"en" : "ID of the property using the certificate", "zh_CN": "使用该证书的加速项目ID。"}
        self.property_id = property_id
        # {"en" : "List of hostnames using the certificate.", "zh_CN": "使用该证书的加速域名列表。"}
        self.hostnames = hostnames
        # {"en" : "Names of the property's origins that use the certificate.", "zh_CN": "使用该证书的加速项目源站的名称。"}
        self.origins = origins

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.origins is not None:
            result['origins'] = self.origins
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('origins') is not None:
            self.origins = m.get('origins')
        return self


class GetACertificateResponseUsageInStaging(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        hostnames: List[str] = None,
        origins: List[str] = None,
    ):
        # {"en" : "ID of the property using the certificate.", "zh_CN": "使用该证书的加速项目的ID。"}
        self.property_id = property_id
        # {"en" : "List of hostnames using the certificate.", "zh_CN": "使用该证书的加速域名列表。"}
        self.hostnames = hostnames
        # {"en" : "Names of the property's origins that use the certificate.", "zh_CN": "使用该证书的加速项目源站的名称。"}
        self.origins = origins

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.origins is not None:
            result['origins'] = self.origins
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('origins') is not None:
            self.origins = m.get('origins')
        return self


class GetACertificateResponse(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        name: str = None,
        description: str = None,
        versions: List[GetACertificateResponseVersions] = None,
        auto_renew: str = None,
        usage_in_production: List[GetACertificateResponseUsageInProduction] = None,
        version_in_staging: int = None,
        usage_in_staging: List[GetACertificateResponseUsageInStaging] = None,
        version_in_production: int = None,
        force_renew: bool = None,
    ):
        # {"en" : "ID of the certificate", "zh_CN": "证书ID。"}
        self.certificate_id = certificate_id
        # {"en" : "Name of the certificate.", "zh_CN": "证书名称。"}
        self.name = name
        # {"en" : "A description of the certificate.", "zh_CN": "证书描述。"}
        self.description = description
        # {"en" : "Describes the versions of the certificate that have been created. You can obtain further details about each version by calling the Query a certificate version's details API.", "zh_CN": "证书版本列表。您可以通过调用'查询证书版本信息'接口来获取每个版本的更多信息。"}
        self.versions = versions
        # {"en" : "Enum: Off,LE 
        # A value of 'LE' indicates that auto renewal via Let's Encrypt (https://letsencrypt.org/docs/challenge-types/) is enabled.", "zh_CN": "取值范围: Off,LE 
        # 是否自动更新。'LE'值表示开启 Let's Encrypt 自动更新。"}
        self.auto_renew = auto_renew
        # {"en" : "Indicates who is using the certificate in production.", "zh_CN": "证书在生产环境中的使用情况。"}
        self.usage_in_production = usage_in_production
        # {"en" : "Range: >= 1 
        # Indicates the version of the certificate deployed to staging.", "zh_CN": "取值范围: >= 1 
        # 表示部署到演练环境的证书版本。"}
        self.version_in_staging = version_in_staging
        # {"en" : "Indicates the customers using the certificate in staging.", "zh_CN": "证书在演练环境中的使用情况。"}
        self.usage_in_staging = usage_in_staging
        # {"en" : "Range: >= 1 
        # Indicates the version of the certificate deployed to production.", "zh_CN": "取值范围: >= 1 
        # 表示部署到生产环境的证书版本。"}
        self.version_in_production = version_in_production
        # {"en" : "A value of true requests the certificate to be auto-renewed as soon as possible instead of waiting for the certificate to expire in 15 days. The value will be set to false after a successful renewal.", "zh_CN": "是否强制更新。当值为true时表示要求尽快自动更新证书，而不是等待证书在 15 天后过期。 证书成功更新后，该值将设置为false。"}
        self.force_renew = force_renew

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.versions, 'versions')
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()
        self.validate_required(self.auto_renew, 'auto_renew')
        self.validate_required(self.usage_in_production, 'usage_in_production')
        if self.usage_in_production:
            for k in self.usage_in_production:
                if k:
                    k.validate()
        self.validate_required(self.version_in_staging, 'version_in_staging')
        self.validate_required(self.usage_in_staging, 'usage_in_staging')
        if self.usage_in_staging:
            for k in self.usage_in_staging:
                if k:
                    k.validate()
        self.validate_required(self.version_in_production, 'version_in_production')
        self.validate_required(self.force_renew, 'force_renew')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.versions is not None:
            result['versions'] = []
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.usage_in_production is not None:
            result['usageInProduction'] = []
            for k in self.usage_in_production:
                result['usageInProduction'].append(k.to_map() if k else None)
        if self.version_in_staging is not None:
            result['versionInStaging'] = self.version_in_staging
        if self.usage_in_staging is not None:
            result['usageInStaging'] = []
            for k in self.usage_in_staging:
                result['usageInStaging'].append(k.to_map() if k else None)
        if self.version_in_production is not None:
            result['versionInProduction'] = self.version_in_production
        if self.force_renew is not None:
            result['forceRenew'] = self.force_renew
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versions') is not None:
            self.versions = []
            for k in m.get('versions'):
                temp_model = GetACertificateResponseVersions()
                self.versions.append(temp_model.from_map(k))
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('usageInProduction') is not None:
            self.usage_in_production = []
            for k in m.get('usageInProduction'):
                temp_model = GetACertificateResponseUsageInProduction()
                self.usage_in_production.append(temp_model.from_map(k))
        if m.get('versionInStaging') is not None:
            self.version_in_staging = m.get('versionInStaging')
        if m.get('usageInStaging') is not None:
            self.usage_in_staging = []
            for k in m.get('usageInStaging'):
                temp_model = GetACertificateResponseUsageInStaging()
                self.usage_in_staging.append(temp_model.from_map(k))
        if m.get('versionInProduction') is not None:
            self.version_in_production = m.get('versionInProduction')
        if m.get('forceRenew') is not None:
            self.force_renew = m.get('forceRenew')
        return self






class DownloadTheCsrPaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # {"en" : "ID of the certificate.", "zh_CN": "证书的ID。"}
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


class DownloadTheCsrParameters(TeaModel):
    def __init__(
        self,
        dcv: str = None,
    ):
        # {"en" : "Enum: sectigo 
        # This optional parameter can be used to request a domain control validation (DCV) file. Currently, we support the certificate authority, Sectigo, by specifying 'sectigo' as the value of the parameter.", "zh_CN": "取值范围: sectigo 
        # 可选参数，用于获取域控制验证(DCV)文件。目前，我们支持证书颁发机构Sectigo，您可将'sectigo'指定为参数值。"}
        self.dcv = dcv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dcv is not None:
            result['dcv'] = self.dcv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dcv') is not None:
            self.dcv = m.get('dcv')
        return self


class DownloadTheCsrRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadTheCsrRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadTheCsrResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DownloadTheCsrResponseDcvFile(TeaModel):
    def __init__(
        self,
        uri: str = None,
        expiration_time: str = None,
    ):
        # {"en" : "A URI that is accessible on your hostnames using the certificate. The file's content will consist of a SHA-256 hash and the domain sectigo.com. Example:
        # 
        # <pre>
        # a6e96b23f9e2add3f79c2907ded1adc43961b05f6d702758a200a8ec8b4d7115
        # sectigo.com
        # </pre>", "zh_CN": "使用到该证书的加速域名可访问到的一个路径。该文件的内容由一个SHA-256哈希值和域名sectigo.com 组成。例如：
        # 
        # <pre>
        # a6e96b23f9e2add3f79c2907ded1adc43961b05f6d702758a200a8ec8b4d7115
        # sectigo.com
        # </pre>"}
        self.uri = uri
        # {"en" : "An RFC 3339 date indicating when the file expires.", "zh_CN": "RFC3339格式的日期，表示CSR文件的过期时间。"}
        self.expiration_time = expiration_time

    def validate(self):
        self.validate_required(self.uri, 'uri')
        self.validate_required(self.expiration_time, 'expiration_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['uri'] = self.uri
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        return self


class DownloadTheCsrResponse(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        csr: str = None,
        latest_version: int = None,
        dcv_file: DownloadTheCsrResponseDcvFile = None,
    ):
        # {"en" : "ID of the certificate.", "zh_CN": "证书的ID。"}
        self.certificate_id = certificate_id
        # {"en" : "The CSR.", "zh_CN": "证书签名请求（CSR）文件。"}
        self.csr = csr
        # {"en" : "Range: >= 1 
        # Most recent version of the certifiate.", "zh_CN": "取值范围: >= 1 
        # 证书的最新版本。"}
        self.latest_version = latest_version
        # {"en" : "This field is only returned if the dcv query parameter is specified.", "zh_CN": "仅当指定了dcv 查询参数时才会返回此字段。"}
        self.dcv_file = dcv_file

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.csr, 'csr')
        self.validate_required(self.latest_version, 'latest_version')
        self.validate_required(self.dcv_file, 'dcv_file')
        if self.dcv_file:
            self.dcv_file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.csr is not None:
            result['csr'] = self.csr
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.dcv_file is not None:
            result['dcvFile'] = self.dcv_file.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('csr') is not None:
            self.csr = m.get('csr')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('dcvFile') is not None:
            temp_model = DownloadTheCsrResponseDcvFile()
            self.dcv_file = temp_model.from_map(m['dcvFile'])
        return self






class GetACertificateVersionsDetailsPaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        version: int = None,
    ):
        # {"en" : "ID of a certificate.", "zh_CN": "证书id。"}
        self.certificate_id = certificate_id
        # {"en" : "Version of the certificate. ", "zh_CN": "证书版本。"}
        self.version = version

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetACertificateVersionsDetailsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateVersionsDetailsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateVersionsDetailsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateVersionsDetailsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACertificateVersionsDetailsResponseChainCertificates(TeaModel):
    def __init__(
        self,
        subject: str = None,
        expiration_time: str = None,
        signature_algo: str = None,
        issuer: str = None,
    ):
        # {"en" : "Subject of the certificate.", "zh_CN": "证书主体。"}
        self.subject = subject
        # {"en" : "RFC 3339 format date indicating when the certificate expires.", "zh_CN": "RFC3339格式的日期，表示证书的过期时间。"}
        self.expiration_time = expiration_time
        # {"en" : "Algorithm of the certificate.", "zh_CN": "证书的算法。"}
        self.signature_algo = signature_algo
        # {"en" : "Issuer of the chain certificate.", "zh_CN": "链证书的颁发者。"}
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subject is not None:
            result['subject'] = self.subject
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.signature_algo is not None:
            result['signatureAlgo'] = self.signature_algo
        if self.issuer is not None:
            result['issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('signatureAlgo') is not None:
            self.signature_algo = m.get('signatureAlgo')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        return self


class GetACertificateVersionsDetailsResponse(TeaModel):
    def __init__(
        self,
        version: int = None,
        comments: str = None,
        expiration_time: str = None,
        creation_time: str = None,
        subject: str = None,
        signature_algo: str = None,
        serial_number: str = None,
        in_production: bool = None,
        in_staging: bool = None,
        fingerprint: str = None,
        algorithm: str = None,
        key_length: int = None,
        subject_alternative_names: List[str] = None,
        chain_certificates: List[GetACertificateVersionsDetailsResponseChainCertificates] = None,
        issuer: str = None,
    ):
        # {"en" : "Range: >= 1 
        # The certificate version.", "zh_CN": "取值范围: >= 1 
        # 证书版本。"}
        self.version = version
        # {"en" : "Comments about the certificate version.
        # ", "zh_CN": "证书版本的描述。"}
        self.comments = comments
        # {"en" : "An RFC3339 format date indicating when the certificate version expires.", "zh_CN": "RFC3339格式的日期，表示证书版本的过期时间。"}
        self.expiration_time = expiration_time
        # {"en" : "An RFC 3339 format date indicating when the certificate version was created.", "zh_CN": "RFC3339格式的日期，用于表示证书版本创建的时间。"}
        self.creation_time = creation_time
        # {"en" : "The certificate subject.", "zh_CN": "证书主体。"}
        self.subject = subject
        # {"en" : "The signature algorithm used by the certificate.", "zh_CN": "证书使用的签名算法。"}
        self.signature_algo = signature_algo
        # {"en" : "The serial number associated with the certificate.
        # ", "zh_CN": "与证书相关联的序列号。"}
        self.serial_number = serial_number
        # {"en" : "Indicates whether the certificate version is currently deployed to production.", "zh_CN": "表示证书版本当前是否已部署到生产环境。"}
        self.in_production = in_production
        # {"en" : "Indicates whether the certificate version is currently deployed to staging.
        # ", "zh_CN": "表示证书版本当前是否已部署到演练环境。"}
        self.in_staging = in_staging
        # {"en" : "certificate fingerprint.", "zh_CN": "证书指纹。"}
        self.fingerprint = fingerprint
        # {"en" : "The encryption algorithm.
        # ", "zh_CN": "加密算法。"}
        self.algorithm = algorithm
        # {"en" : "Number of bits used in encryption.
        # ", "zh_CN": "加密算法使用的位数。
        # "}
        self.key_length = key_length
        # {"en" : "List of hostnames served by the certificate. Wildcards are permitted, for example, *.domain.com.
        # ", "zh_CN": "证书所涵盖的域名列表（SAN）。允许使用通配符，例如，*.domain.com。
        # "}
        self.subject_alternative_names = subject_alternative_names
        # {"en" : "Describes the certificate chain.", "zh_CN": "链证书。"}
        self.chain_certificates = chain_certificates
        # {"en" : "Issuer of the certificate.", "zh_CN": "证书的颁发者。"}
        self.issuer = issuer

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.comments, 'comments')
        self.validate_required(self.expiration_time, 'expiration_time')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.subject, 'subject')
        self.validate_required(self.signature_algo, 'signature_algo')
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.in_production, 'in_production')
        self.validate_required(self.in_staging, 'in_staging')
        self.validate_required(self.fingerprint, 'fingerprint')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.key_length, 'key_length')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')
        self.validate_required(self.chain_certificates, 'chain_certificates')
        if self.chain_certificates:
            for k in self.chain_certificates:
                if k:
                    k.validate()
        self.validate_required(self.issuer, 'issuer')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.comments is not None:
            result['comments'] = self.comments
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.subject is not None:
            result['subject'] = self.subject
        if self.signature_algo is not None:
            result['signatureAlgo'] = self.signature_algo
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.in_production is not None:
            result['inProduction'] = self.in_production
        if self.in_staging is not None:
            result['inStaging'] = self.in_staging
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.key_length is not None:
            result['keyLength'] = self.key_length
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        if self.chain_certificates is not None:
            result['chainCertificates'] = []
            for k in self.chain_certificates:
                result['chainCertificates'].append(k.to_map() if k else None)
        if self.issuer is not None:
            result['issuer'] = self.issuer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('comments') is not None:
            self.comments = m.get('comments')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('signatureAlgo') is not None:
            self.signature_algo = m.get('signatureAlgo')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('inProduction') is not None:
            self.in_production = m.get('inProduction')
        if m.get('inStaging') is not None:
            self.in_staging = m.get('inStaging')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('keyLength') is not None:
            self.key_length = m.get('keyLength')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        if m.get('chainCertificates') is not None:
            self.chain_certificates = []
            for k in m.get('chainCertificates'):
                temp_model = GetACertificateVersionsDetailsResponseChainCertificates()
                self.chain_certificates.append(temp_model.from_map(k))
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        return self






class DeleteACertificatePaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # {"en" : "ID of the certificate.", "zh_CN": "证书 id。"}
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


class DeleteACertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACertificateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACertificateResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateACertificatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACertificateRequestNewVersionIdentificationInfo(TeaModel):
    def __init__(
        self,
        country: str = None,
        state: str = None,
        city: str = None,
        company: str = None,
        department: str = None,
        common_name: str = None,
        email: str = None,
        subject_alternative_names: List[str] = None,
    ):
        # {"en" : "Range: [ 2 .. 2 ] characters 
        # An ISO-3166 country code.", "zh_CN": "取值范围: [ 2 .. 2 ] 字符 
        # ISO-3166国家代码。"}
        self.country = country
        # {"en" : "A state or province.", "zh_CN": "州或省。"}
        self.state = state
        # {"en" : "A city.", "zh_CN": "城市。"}
        self.city = city
        # {"en" : "A company name.", "zh_CN": "公司名称。"}
        self.company = company
        # {"en" : "The department associated with the certificate.", "zh_CN": "与证书关联的部门。"}
        self.department = department
        # {"en" : "A common name for the certificate.", "zh_CN": "证书的通用名称。"}
        self.common_name = common_name
        # {"en" : "An email address.", "zh_CN": "邮箱地址。"}
        self.email = email
        # {"en" : "Hostnames that this certificate will serve. Each entry must be a valid hostname such as domain.com or a wildcard hostname beginning with '*' such as *.domain.com.", "zh_CN": "此证书涵盖的加速域名（SAN）列表。每个条目必须是有效的加速域名，例如 domain.com
        # 或者是以'*'开头的泛域名，例如：*.domain.com。"}
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['country'] = self.country
        if self.state is not None:
            result['state'] = self.state
        if self.city is not None:
            result['city'] = self.city
        if self.company is not None:
            result['company'] = self.company
        if self.department is not None:
            result['department'] = self.department
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.email is not None:
            result['email'] = self.email
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('company') is not None:
            self.company = m.get('company')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        return self


class CreateACertificateRequestNewVersion(TeaModel):
    def __init__(
        self,
        comments: str = None,
        private_key: str = None,
        certificate: str = None,
        chain_cert: str = None,
        identification_info: CreateACertificateRequestNewVersionIdentificationInfo = None,
    ):
        # {"en" : "Comments about the certificate version.", "zh_CN": "证书版本的描述。"}
        self.comments = comments
        # {"en" : "The value must be either the private key in PEM format and encrypted with the API key and timestamp OR the literal string 'RSA2048' or 'ECC256' if you opt to generate a self-signed certificate. The key must be encrypted with AES-128-CBC and base64-encoded. This helps protect your key when you upload it to CDN Pro.", "zh_CN": "用于指定证书私钥，必须是PEM格式的私钥。如果您选择生成自签名证书，则此处的值应为'RSA2048'或'ECC256'。请使用您API账号的密钥和时间戳对私钥进行加密再上传。请使用AES-128-CBC加密算法，并用base64编码。当您将私钥上传到CDN Pro时，这种加密方式可以保护您的私钥。"}
        self.private_key = private_key
        # {"en" : "Enter the certificate in PEM format or the literal string 'GENERATE' if you wish that we create a self-signed certificate valid for ten days for test purposes. If you enter 'GENERATE', then you must also specify either 'RSA2048' or 'ECC256' as the value of the privateKey field to choose the encryption for the self-signed certificate.", "zh_CN": "用于指定证书（公钥），必须是PEM格式。如果您希望系统自动生成自签名证书（有效期 10 天）用于测试，则此处的值应为'GENERATE'。 当您指定'GENERATE'时，必须同时指定'RSA2048'或'ECC256'作为 privateKey 字段的值，用于选择加密算法生成自签名证书。"}
        self.certificate = certificate
        # {"en" : "The chain certificate in PEM format.", "zh_CN": "用于指定链证书。必须是PEM格式"}
        self.chain_cert = chain_cert
        # {"en" : "Information submitted when generating a self-signed certificate.", "zh_CN": "当您选择生成自签名证书时，需提交以下信息。"}
        self.identification_info = identification_info

    def validate(self):
        if self.identification_info:
            self.identification_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['comments'] = self.comments
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.chain_cert is not None:
            result['chainCert'] = self.chain_cert
        if self.identification_info is not None:
            result['identificationInfo'] = self.identification_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comments') is not None:
            self.comments = m.get('comments')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('chainCert') is not None:
            self.chain_cert = m.get('chainCert')
        if m.get('identificationInfo') is not None:
            temp_model = CreateACertificateRequestNewVersionIdentificationInfo()
            self.identification_info = temp_model.from_map(m['identificationInfo'])
        return self


class CreateACertificateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        auto_renew: str = None,
        new_version: CreateACertificateRequestNewVersion = None,
        force_renew: bool = None,
    ):
        # {"en" : "Name of the certificate.", "zh_CN": "证书名称。"}
        self.name = name
        # {"en" : "A description of the new certificate.
        # ", "zh_CN": "证书描述。"}
        self.description = description
        # {"en" : "Enum: LE,Off 
        # Specifying 'LE' requests that we automatically renew your certificate through Let's Encrypt (https://letsencrypt.org/docs/challenge-types/) when it is close to expiring. ", "zh_CN": "取值范围: LE,Off 
        # 是否开启证书自动更新。当值为'LE'时，我们将会在证书即将到期时通过Let's Encrypt自动更新您的证书。"}
        self.auto_renew = auto_renew
        # {"en" : "This object is used to specify the initial version of the certificate.", "zh_CN": "证书的第一个版本。"}
        self.new_version = new_version
        # {"en" : "Default: False 
        # A value of true requests the certificate to be auto-renewed as soon as possible instead of waiting for the certificate to expire in 15 days. The value will be set to false after a successful renewal.", "zh_CN": "默认值: False 
        # 是否强制更新。当值为true时表示要求尽快自动更新证书，而不是等待证书在 15 天后过期。 
        # 证书成功更新后，该值将设置为false。"}
        self.force_renew = force_renew

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.new_version:
            self.new_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.new_version is not None:
            result['newVersion'] = self.new_version.to_map()
        if self.force_renew is not None:
            result['forceRenew'] = self.force_renew
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('newVersion') is not None:
            temp_model = CreateACertificateRequestNewVersion()
            self.new_version = temp_model.from_map(m['newVersion'])
        if m.get('forceRenew') is not None:
            self.force_renew = m.get('forceRenew')
        return self


class CreateACertificateResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACertificateResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header's value will be a URL allowing you to get details about the new certificate.  Example: <code>Location: http://ngapi.cdnetworks.com/cdn/certificates/d60b730d9a586425677940cc</code>", "zh_CN":"通过Location响应头返回新建的证书的URL。URL中包含证书的ID，可使用该ID调用'查询证书详情'接口来查看证书详细信息。URL示例：<code>Location: http://open.chinanetcenter.com/cdn/certificates/5dca2205f9e9cc0001df7b33"}
        self.location = location

    def validate(self):
        self.validate_required(self.location, 'location')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self






class UpdateACertificatePaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # {"en" : "ID of the certificate.", "zh_CN": "证书 id。"}
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


class UpdateACertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateACertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateACertificateRequestNewVersionIdentificationInfo(TeaModel):
    def __init__(
        self,
        country: str = None,
        state: str = None,
        city: str = None,
        company: str = None,
        department: str = None,
        common_name: str = None,
        email: str = None,
        subject_alternative_names: List[str] = None,
    ):
        # {"en" : "Range: [ 2 .. 2 ] characters 
        # An ISO-3166 country code.", "zh_CN": "取值范围: [ 2 .. 2 ] 字符 
        # ISO-3166国家代码。"}
        self.country = country
        # {"en" : "A state or province.", "zh_CN": "州或省。"}
        self.state = state
        # {"en" : "A city.", "zh_CN": "城市。"}
        self.city = city
        # {"en" : "A company name.", "zh_CN": "公司名称。"}
        self.company = company
        # {"en" : "The department associated with the certificate.", "zh_CN": "与证书关联的部门。"}
        self.department = department
        # {"en" : "A common name for the certificate.", "zh_CN": "证书的通用名称。"}
        self.common_name = common_name
        # {"en" : "An email address.", "zh_CN": "邮箱地址。"}
        self.email = email
        # {"en" : "Hostnames that this certificate will serve. Each entry must be a valid hostname such as domain.com or a wildcard hostname beginning with '*' such as *.domain.com.", "zh_CN": "此证书涵盖的加速域名。每个条目必须是有效的加速域名，例如 domain.com
        # 或者是以'*'开头的泛域名，例如：*.domain.com。"}
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['country'] = self.country
        if self.state is not None:
            result['state'] = self.state
        if self.city is not None:
            result['city'] = self.city
        if self.company is not None:
            result['company'] = self.company
        if self.department is not None:
            result['department'] = self.department
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.email is not None:
            result['email'] = self.email
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('company') is not None:
            self.company = m.get('company')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        return self


class UpdateACertificateRequestNewVersion(TeaModel):
    def __init__(
        self,
        private_key: str = None,
        certificate: str = None,
        chain_cert: str = None,
        identification_info: UpdateACertificateRequestNewVersionIdentificationInfo = None,
    ):
        # {"en" : "If not present, the value will be copied from the latest version of the certificate. Please refer to the description of the privateKey field in the Create a certificate API for details about the format.", "zh_CN": "如果未指定该字段，则将从证书的最新版本中复制。 具体格式请参考'创建证书'接口中privateKey字段的说明。"}
        self.private_key = private_key
        # {"en" : "If not present, the value will be copied from the latest version of the certificate. Please refer to the description of the certificate field in the Create a certificate API for details about the format.", "zh_CN": "如果未指定该字段，则将从证书的最新版本中复制。 具体格式请参考'创建证书'接口中certificate字段的说明。"}
        self.certificate = certificate
        # {"en" : "This field must be filled in if the privateKey and certificate fields are both omitted. In this case, only the chain certificate will be updated. The chain certificate must be in PEM format.", "zh_CN": "当privateKey和certificate字段都未指定时，该字段必须填写。在这种情况下，只有链证书将被更新。链证书的格式必须为PEM。"}
        self.chain_cert = chain_cert
        # {"en" : "Information submitted when generating a self-signed certificate.", "zh_CN": "生成自签名证书时提交的信息。"}
        self.identification_info = identification_info

    def validate(self):
        if self.identification_info:
            self.identification_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.chain_cert is not None:
            result['chainCert'] = self.chain_cert
        if self.identification_info is not None:
            result['identificationInfo'] = self.identification_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('chainCert') is not None:
            self.chain_cert = m.get('chainCert')
        if m.get('identificationInfo') is not None:
            temp_model = UpdateACertificateRequestNewVersionIdentificationInfo()
            self.identification_info = temp_model.from_map(m['identificationInfo'])
        return self


class UpdateACertificateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        auto_renew: str = None,
        new_version: UpdateACertificateRequestNewVersion = None,
        force_renew: bool = None,
    ):
        # {"en" : "Name of the certificate.", "zh_CN": "证书名称。"}
        self.name = name
        # {"en" : "Description of the certificate.", "zh_CN": "证书描述。"}
        self.description = description
        # {"en" : "Enum: Off,LE 
        # Indicates whether the certificate will be renewed with Let's Encrypt.", "zh_CN": "取值范围: Off,LE 
        # 是否开启证书自动更新。当值为'LE'时，我们将会在证书即将到期时通过Let's Encrypt自动更新您的证书。"}
        self.auto_renew = auto_renew
        # {"en" : "If this field is present, a new version of the certificate will be created. If the identificationInfo field is not provided, then the information will be copied from the latest version of the certificate.", "zh_CN": "如果该字段存在，则将创建一个新的证书版本。如果没有提供identiationinfo字段，则相关信息将从证书的最新版本中复制。"}
        self.new_version = new_version
        # {"en" : "Default: False 
        # A value of true requests the certificate to be auto-renewed as soon as possible instead of waiting for the certificate to expire in 15 days. The value will be set to false after a successful renewal.", "zh_CN": "默认值: False 
        # 是否强制更新。当值为true时表示要求尽快自动更新证书，而不是等待证书在 15 天后过期。 证书成功更新后，该值将设置为false。"}
        self.force_renew = force_renew

    def validate(self):
        if self.new_version:
            self.new_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.new_version is not None:
            result['newVersion'] = self.new_version.to_map()
        if self.force_renew is not None:
            result['forceRenew'] = self.force_renew
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('newVersion') is not None:
            temp_model = UpdateACertificateRequestNewVersion()
            self.new_version = temp_model.from_map(m['newVersion'])
        if m.get('forceRenew') is not None:
            self.force_renew = m.get('forceRenew')
        return self


class UpdateACertificateResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateACertificateResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header returns a URL to the specific certificate version if a new one is created.  Example:  <code>Location: http://open.chinanetcenter.com/cdn/certificates/329f12c1fe6708c23c31e91f/versions/5</code>", "zh_CN":"通过Location响应头返回新创建的证书版本的URL。示例：<code>Location:http://open.chinanetcenter.com/cdn/certificates/329f12c1fe6708c23c31e91f/versions/5</code>"}
        self.location = location

    def validate(self):
        self.validate_required(self.location, 'location')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self






class GetListOfCertificatesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfCertificatesParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        offset: int = None,
        limit: int = None,
        target: str = None,
        auto_renew: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # {"en" : "This parameter specifies a keyword to be searched in the 'name' field of the certificate.", "zh_CN": "指定关键字，按证书名称查询证书。"}
        self.search = search
        # {"en" : "Default: 0 Range: >= 0 
        # The offset indicates the index of the first certificate to return. The default is 0.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: <= 200 
        # The limit indicates the maximum number of certificates to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: all,staging,production 
        # Filters the results based on where the certificate has been deployed. <table><tr><th>Value</th><th>Effect</th></tr><tr><td></td><td>An empty target parameter results in all certificates being returned whether or not they have been deployed.</td></tr><td>all</td><td>Return all certificates deployed to either staging or production environments.</td></tr><tr><td>staging</td><td>Only return certificates deployed to staging.</td></tr><tr><td>production</td><td>Only return certificates deployed to production.</td></tr></table>
        # ", "zh_CN": "取值范围: all,staging,production 
        # 根据证书的部署环境查询证书。 <table> <tr><th>取值</th><th>返回数据</th></tr> <tr><td></td><td>当该参数为空时，返回所有证书，无论证书是否已部署。</td></tr> <tr><td>all</td><td>返回所有已部署的证书，包括部署到演练环境和生产环境的证书。</td></tr> <tr><td>staging</td><td>只返回部署到演练环境的证书。</td></tr> <tr><td>production</td><td>只返回部署到生产环境的证书。</td></tr> </table>"}
        self.target = target
        # {"en" : "Enum: LE,Off 
        # Filter results based on auto renewal status. By default, all certificates are returned.", "zh_CN": "取值范围: LE,Off 
        # 根据是否设置自动更新来查询证书。LE指通过Let's Encrypt自动更新，Off指未开启自动更新。"}
        self.auto_renew = auto_renew
        # {"en" : "Enum: creationTime,lastUpdateTime,expirationTime,productionExpirationTime 
        # Default: lastUpdateTime 
        # Returns certificates sorted by this field.", "zh_CN": "取值范围: creationTime,lastUpdateTime,expirationTime,productionExpirationTime 
        # 默认值: lastUpdateTime 
        # 查询结果的排序依据。支持按证书的创建时间，最后一次更新时间，证书过期时间，证书在生产环境中的版本的过期时间来排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc,desc 
        # Default: desc 
        # Return results sorted in this order ('asc' for ascending order, 'desc' for descending order).
        # ", "zh_CN": "取值范围: asc,desc 
        # 默认值: desc 
        # 查询结果的排序顺序，即升序（asc）或者降序（desc）。"}
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.target is not None:
            result['target'] = self.target
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        return self


class GetListOfCertificatesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfCertificatesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfCertificatesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfCertificatesResponseCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        name: str = None,
        latest_version: int = None,
        auto_renew: str = None,
        creation_time: str = None,
        expiration_time: str = None,
        last_update_time: str = None,
        version_in_production: int = None,
        version_in_staging: int = None,
        production_expiration_time: str = None,
        staging_expiration_time: str = None,
        force_renew: bool = None,
    ):
        # {"en" : "An ID representing the certificate. You can call GET /cdn/certificates/{certificate ID} to get details about a certificate.", "zh_CN": "证书的ID。您可以通过调用'查询证书详情'接口来获取证书的详细信息。"}
        self.certificate_id = certificate_id
        # {"en" : "Name of the certificate.", "zh_CN": "证书名称。"}
        self.name = name
        # {"en" : "Range: >= 1 
        # The latest version of the certificate.", "zh_CN": "取值范围: >= 1 
        # 证书的最新版本。"}
        self.latest_version = latest_version
        # {"en" : "Enum: LE,Off 
        # This is set to 'LE' if you have chosen to autorenew the certificate using Let's Encrypt.", "zh_CN": "取值范围: LE,Off 
        # 如果您选择使用Let's Encrypt自动续订证书，则将此项设置为'LE'。"}
        self.auto_renew = auto_renew
        # {"en" : "An RFC3339 format date indicates when the certificate was added to the system.", "zh_CN": "RFC3339格式的日期，表示证书在CDN Pro的创建时间。"}
        self.creation_time = creation_time
        # {"en" : "An RFC3339 format date indicating when the latest version of the certificate expires.
        # ", "zh_CN": "RFC3339格式的日期，表示证书最新版本的到期时间。
        # "}
        self.expiration_time = expiration_time
        # {"en" : "An RFC3339 format date indicates when the certificate was last updated.
        # ", "zh_CN": "RFC3339格式的日期，表示证书最近一次更新的时间。
        # "}
        self.last_update_time = last_update_time
        # {"en" : "Range: >= 1 
        # Indicates the version of the certificate deployed to production.", "zh_CN": "取值范围: >= 1 
        # 证书部署到生产环境的版本。"}
        self.version_in_production = version_in_production
        # {"en" : "Range: >= 1 
        # Indicates the version of the certificate deployed to staging.", "zh_CN": "取值范围: >= 1 
        # 证书部署到演练环境的版本。"}
        self.version_in_staging = version_in_staging
        # {"en" : "RFC 3339 date indicating when the version deployed to production will expire.", "zh_CN": "RFC3339格式的日期，表示部署到生产环境的版本的过期时间。"}
        self.production_expiration_time = production_expiration_time
        # {"en" : "RFC 3339 date indicating when the version deployed to staging will expire.", "zh_CN": "RFC3339格式的日期，表示部署到演练环境的版本的过期时间。"}
        self.staging_expiration_time = staging_expiration_time
        # {"en" : "Setting the value to true requests the certificate to be auto-renewed as soon as possible instead of waiting for the certificate to expire in 15 days. The value will be set to false after a successful renewal.", "zh_CN": "是否强制更新。当值为true时表示要求尽快自动更新证书，而不是等待证书在 15 天后过期。 证书成功更新后，该值将设置为false。"}
        self.force_renew = force_renew

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.name is not None:
            result['name'] = self.name
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.version_in_production is not None:
            result['versionInProduction'] = self.version_in_production
        if self.version_in_staging is not None:
            result['versionInStaging'] = self.version_in_staging
        if self.production_expiration_time is not None:
            result['productionExpirationTime'] = self.production_expiration_time
        if self.staging_expiration_time is not None:
            result['stagingExpirationTime'] = self.staging_expiration_time
        if self.force_renew is not None:
            result['forceRenew'] = self.force_renew
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('versionInProduction') is not None:
            self.version_in_production = m.get('versionInProduction')
        if m.get('versionInStaging') is not None:
            self.version_in_staging = m.get('versionInStaging')
        if m.get('productionExpirationTime') is not None:
            self.production_expiration_time = m.get('productionExpirationTime')
        if m.get('stagingExpirationTime') is not None:
            self.staging_expiration_time = m.get('stagingExpirationTime')
        if m.get('forceRenew') is not None:
            self.force_renew = m.get('forceRenew')
        return self


class GetListOfCertificatesResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        certificates: List[GetListOfCertificatesResponseCertificates] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of available certificates. The actual number returned depends on the query parameters.", "zh_CN": "取值范围: >= 0 
        # 证书的总数。返回的实际数量取决于查询参数。"}
        self.count = count
        # {"en" : "List of certificates.", "zh_CN": "证书列表。"}
        self.certificates = certificates

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.certificates, 'certificates')
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.certificates is not None:
            result['certificates'] = []
            for k in self.certificates:
                result['certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('certificates') is not None:
            self.certificates = []
            for k in m.get('certificates'):
                temp_model = GetListOfCertificatesResponseCertificates()
                self.certificates.append(temp_model.from_map(k))
        return self




