# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteACaCertificateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACaCertificateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class DeleteACaCertificatePaths(TeaModel):
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


class DeleteACaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteACaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateACaCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        content: str = None,
        comment: str = None,
        type: str = None,
        parent_certificate_id: str = None,
        skip_expired: bool = None,
    ):
        # {"en":"Certificate name", "zh_CN":"证书名称"}
        self.certificate_name = certificate_name
        # {"en":"Certificate content, in PEM format. ", "zh_CN":"证书内容，PEM格式。例如：
        # -----BEGIN CERTIFICATE-----\
        # ……
        # -----END CERTIFICATE-----"}
        self.content = content
        # {"en":"comment.", "zh_CN":"备注"}
        self.comment = comment
        # {"en":"Certificate type,can be ROOT or NODE. ", "zh_CN":"证书的类型，可选值：ROOT,NODE。ROOT表示根证书，NODE表示子证书"}
        self.type = type
        # {"en":"parent certificate Id,if the certificate type is NODE, it cannot be empty.", "zh_CN":"父证书id，如果证书类型为NODE，则必填"}
        self.parent_certificate_id = parent_certificate_id
        # {"en":"Skip the constraints that have expired.", "zh_CN":"是否跳过校验证书是否已过期的约束"}
        self.skip_expired = skip_expired

    def validate(self):
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.content, 'content')
        self.validate_required(self.type, 'type')
        self.validate_required(self.skip_expired, 'skip_expired')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.content is not None:
            result['content'] = self.content
        if self.comment is not None:
            result['comment'] = self.comment
        if self.type is not None:
            result['type'] = self.type
        if self.parent_certificate_id is not None:
            result['parentCertificateId'] = self.parent_certificate_id
        if self.skip_expired is not None:
            result['skipExpired'] = self.skip_expired
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('parentCertificateId') is not None:
            self.parent_certificate_id = m.get('parentCertificateId')
        if m.get('skipExpired') is not None:
            self.skip_expired = m.get('skipExpired')
        return self


class UpdateACaCertificateResponse(TeaModel):
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


class UpdateACaCertificatePaths(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
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


class UpdateACaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateACaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateACaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetACaCertificateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACaCertificateResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: dict = None,
        certificate_id: str = None,
        certificate_name: str = None,
        type: str = None,
        parent_certificate_id: str = None,
        parent_certificate_name: str = None,
        validity_from: str = None,
        validity_to: str = None,
        creation_time: str = None,
        algorithm: str = None,
        version: str = None,
        issuer: str = None,
        serial_number: str = None,
        content: str = None,
        expire_status: str = None,
        comment: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"detail", "zh_CN":"详情"}
        self.data = data
        # {"en":"Certificate ID.", "zh_CN":"证书ID。"}
        self.certificate_id = certificate_id
        # {"en":"Certificate name.", "zh_CN":"证书名称。"}
        self.certificate_name = certificate_name
        # {"en":"Certificate type, ROOT or NODE.", "zh_CN":"证书类型,取值ROOT或NODE。"}
        self.type = type
        # {"en":"Parent certificate Id.", "zh_CN":"父证书id。"}
        self.parent_certificate_id = parent_certificate_id
        # {"en":"Parent certificate name.", "zh_CN":"父证书名称。"}
        self.parent_certificate_name = parent_certificate_name
        # {"en":"Certificate validity from.", "zh_CN":"证书有效期开始时间。"}
        self.validity_from = validity_from
        # {"en":"Certificate validity to.", "zh_CN":"证书有效期结束时间。"}
        self.validity_to = validity_to
        # {"en":"Certificate create time.", "zh_CN":"证书创建时间。"}
        self.creation_time = creation_time
        # {"en":"algorithm", "zh_CN":"私钥算法。"}
        self.algorithm = algorithm
        # {"en":"version", "zh_CN":"version"}
        self.version = version
        # {"en":"issuer", "zh_CN":"颁发机构"}
        self.issuer = issuer
        # {"en":"serial number", "zh_CN":"序列号"}
        self.serial_number = serial_number
        # {"en":"certificate content", "zh_CN":"证书内容"}
        self.content = content
        # {"en":"Certificate expire status, 0-normal, 1-nearly expired, 2-already expired.", "zh_CN":"证书过期状态，0-正常，1-临近过期，2-已过期。"}
        self.expire_status = expire_status
        # {"en":"comment.", "zh_CN":"备注。"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.parent_certificate_id, 'parent_certificate_id')
        self.validate_required(self.parent_certificate_name, 'parent_certificate_name')
        self.validate_required(self.validity_from, 'validity_from')
        self.validate_required(self.validity_to, 'validity_to')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.version, 'version')
        self.validate_required(self.issuer, 'issuer')
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.content, 'content')
        self.validate_required(self.expire_status, 'expire_status')
        self.validate_required(self.comment, 'comment')

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
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.type is not None:
            result['type'] = self.type
        if self.parent_certificate_id is not None:
            result['parentCertificateId'] = self.parent_certificate_id
        if self.parent_certificate_name is not None:
            result['parentCertificateName'] = self.parent_certificate_name
        if self.validity_from is not None:
            result['validityFrom'] = self.validity_from
        if self.validity_to is not None:
            result['validityTo'] = self.validity_to
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.version is not None:
            result['version'] = self.version
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.content is not None:
            result['content'] = self.content
        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('parentCertificateId') is not None:
            self.parent_certificate_id = m.get('parentCertificateId')
        if m.get('parentCertificateName') is not None:
            self.parent_certificate_name = m.get('parentCertificateName')
        if m.get('validityFrom') is not None:
            self.validity_from = m.get('validityFrom')
        if m.get('validityTo') is not None:
            self.validity_to = m.get('validityTo')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class GetACaCertificatePaths(TeaModel):
    def __init__(
        self,
        certifiate_id: str = None,
    ):
        # {"en":"CA certificate ID", "zh_CN":"CA证书ID"}
        self.certifiate_id = certifiate_id

    def validate(self):
        self.validate_required(self.certifiate_id, 'certifiate_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certifiate_id is not None:
            result['certificate-id'] = self.certifiate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificate-id') is not None:
            self.certifiate_id = m.get('certificate-id')
        return self


class GetACaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetACaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AssociateDomainWithCaCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        usage: str = None,
        domains: List[str] = None,
    ):
        # {"en":"Certificate ID", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate usage, Allowed values: CLIENT_MTLS, ORIGIN_MTLS .", "zh_CN":"证书用途，取值范围：CLIENT_MTLS、ORIGIN_MTLS "}
        self.usage = usage
        # {"en":"Associated domains.", "zh_CN":"关联域名列表"}
        self.domains = domains

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.usage, 'usage')
        self.validate_required(self.domains, 'domains')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.usage is not None:
            result['usage'] = self.usage
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class AssociateDomainWithCaCertificateResponse(TeaModel):
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


class AssociateDomainWithCaCertificatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateDomainWithCaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateDomainWithCaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AssociateDomainWithCaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateACaCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        content: str = None,
        comment: str = None,
        type: str = None,
        parent_certificate_id: str = None,
        skip_expired: bool = None,
    ):
        # {"en":"Certificate name", "zh_CN":"证书名称"}
        self.certificate_name = certificate_name
        # {"en":"Certificate content, in PEM format. ", "zh_CN":"证书内容，PEM格式。例如：
        # -----BEGIN CERTIFICATE-----\
        # ……
        # -----END CERTIFICATE-----"}
        self.content = content
        # {"en":"comment.", "zh_CN":"备注"}
        self.comment = comment
        # {"en":"Certificate type,can be ROOT or NODE. ", "zh_CN":"证书的类型，可选值：ROOT,NODE。ROOT表示根证书，NODE表示子证书"}
        self.type = type
        # {"en":"parent certificate Id,if the certificate type is NODE, it cannot be empty.", "zh_CN":"父证书ID，如果证书类型为NODE，则必填"}
        self.parent_certificate_id = parent_certificate_id
        # {"en":"Skip the constraints that have expired.", "zh_CN":"是否跳过校验证书是否已过期的约束"}
        self.skip_expired = skip_expired

    def validate(self):
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.content, 'content')
        self.validate_required(self.type, 'type')
        self.validate_required(self.skip_expired, 'skip_expired')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.content is not None:
            result['content'] = self.content
        if self.comment is not None:
            result['comment'] = self.comment
        if self.type is not None:
            result['type'] = self.type
        if self.parent_certificate_id is not None:
            result['parentCertificateId'] = self.parent_certificate_id
        if self.skip_expired is not None:
            result['skipExpired'] = self.skip_expired
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('parentCertificateId') is not None:
            self.parent_certificate_id = m.get('parentCertificateId')
        if m.get('skipExpired') is not None:
            self.skip_expired = m.get('skipExpired')
        return self


class CreateACaCertificateResponse(TeaModel):
    def __init__(
        self,
        location: str = None,
        code: str = None,
        message: str = None,
    ):
        # {"en":"The URL used to access the certificate file where certificate-id is the unique token that the system generates for the certificate and whose value is a string", "zh_CN":"用于访问该证书文件的URL，其中certificate-id为系统为该证书生成的唯一标示，其值为字符串"}
        self.location = location
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"响应信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.location, 'location')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateACaCertificatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateACaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCaCertificateListRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        page_number: int = None,
        page_size: int = None,
        relate_domains: List[str] = None,
        expire_status: List[str] = None,
        algorithm: str = None,
        is_like: str = None,
    ):
        # {"en":"QueryCaCertificateListCertificate name", "zh_CN":"证书名称"}
        self.certificate_name = certificate_name
        # {"en":"Page number, must great than 0.", "zh_CN":"当前页数,大于0"}
        self.page_number = page_number
        # {"en":"Page size,must great than 0 and not allowed to exceed 500.", "zh_CN":"每页记录数,大于0小于500"}
        self.page_size = page_size
        # {"en":"related domain names.", "zh_CN":"关联的域名"}
        self.relate_domains = relate_domains
        # {"en":"QueryCaCertificateListCertificate expire status, 0-normal, 1-nearly expired, 2-already expired.", "zh_CN":"证书过期状态，0-正常，1-临近过期，2-已过期"}
        self.expire_status = expire_status
        # {"en":"algorithm.", "zh_CN":"私钥算法"}
        self.algorithm = algorithm
        # {"en":"Match mode, effects on parameter certificateName and relateDomains.", "zh_CN":"匹配方式,作用与证书名称以及关联域名"}
        self.is_like = is_like

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.is_like, 'is_like')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.relate_domains is not None:
            result['relateDomains'] = self.relate_domains
        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.is_like is not None:
            result['isLike'] = self.is_like
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('relateDomains') is not None:
            self.relate_domains = m.get('relateDomains')
        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('isLike') is not None:
            self.is_like = m.get('isLike')
        return self


class QueryCaCertificateListRelatedDomain(TeaModel):
    def __init__(
        self,
        usage: str = None,
        domains: List[str] = None,
    ):
        # {"en":"QueryCaCertificateListCertificate usage, CLIENT_MTLS or ORIGIN_MTLS.", "zh_CN":"证书用途，取值CLIENT_MTLS或ORIGIN_MTLS"}
        self.usage = usage
        # {"en":"Domain list", "zh_CN":"域名列表"}
        self.domains = domains

    def validate(self):
        self.validate_required(self.usage, 'usage')
        self.validate_required(self.domains, 'domains')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.usage is not None:
            result['usage'] = self.usage
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class QueryCaCertificateListCertificate(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        certificate_name: str = None,
        type: str = None,
        parent_certificate_id: str = None,
        validity_from: str = None,
        validity_to: str = None,
        related_domain_list: List[QueryCaCertificateListRelatedDomain] = None,
        algorithm: str = None,
        expire_status: str = None,
        comment: str = None,
    ):
        # {"en":"QueryCaCertificateListCertificate ID.", "zh_CN":"证书ID。"}
        self.certificate_id = certificate_id
        # {"en":"QueryCaCertificateListCertificate name.", "zh_CN":"证书名称。"}
        self.certificate_name = certificate_name
        # {"en":"QueryCaCertificateListCertificate type, ROOT or NODE.", "zh_CN":"证书类型,取值ROOT或NODE。"}
        self.type = type
        # {"en":"Parent certificate Id. ", "zh_CN":"父证书id。"}
        self.parent_certificate_id = parent_certificate_id
        # {"en":"QueryCaCertificateListCertificate validity from.", "zh_CN":"证书有效期开始时间。"}
        self.validity_from = validity_from
        # {"en":"QueryCaCertificateListCertificate validity to.", "zh_CN":"证书有效期结束时间。"}
        self.validity_to = validity_to
        # {"en":"Related domain list.", "zh_CN":"关联的域名。"}
        self.related_domain_list = related_domain_list
        # {"en":"algorithm ", "zh_CN":"私钥算法。"}
        self.algorithm = algorithm
        # {"en":"QueryCaCertificateListCertificate expire status, 0-normal, 1-nearly expired, 2-already expired.", "zh_CN":"证书过期状态，0-正常，1-临近过期，2-已过期。"}
        self.expire_status = expire_status
        # {"en":"comment.", "zh_CN":"备注。"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.parent_certificate_id, 'parent_certificate_id')
        self.validate_required(self.validity_from, 'validity_from')
        self.validate_required(self.validity_to, 'validity_to')
        self.validate_required(self.related_domain_list, 'related_domain_list')
        if self.related_domain_list:
            for k in self.related_domain_list:
                if k:
                    k.validate()
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.expire_status, 'expire_status')
        self.validate_required(self.comment, 'comment')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.type is not None:
            result['type'] = self.type
        if self.parent_certificate_id is not None:
            result['parentCertificateId'] = self.parent_certificate_id
        if self.validity_from is not None:
            result['validityFrom'] = self.validity_from
        if self.validity_to is not None:
            result['validityTo'] = self.validity_to
        if self.related_domain_list is not None:
            result['relatedDomainList'] = []
            for k in self.related_domain_list:
                result['relatedDomainList'].append(k.to_map() if k else None)
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.expire_status is not None:
            result['expireStatus'] = self.expire_status
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('parentCertificateId') is not None:
            self.parent_certificate_id = m.get('parentCertificateId')
        if m.get('validityFrom') is not None:
            self.validity_from = m.get('validityFrom')
        if m.get('validityTo') is not None:
            self.validity_to = m.get('validityTo')
        if m.get('relatedDomainList') is not None:
            self.related_domain_list = []
            for k in m.get('relatedDomainList'):
                temp_model = QueryCaCertificateListRelatedDomain()
                self.related_domain_list.append(temp_model.from_map(k))
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('expireStatus') is not None:
            self.expire_status = m.get('expireStatus')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class QueryCaCertificateListPageInfo(TeaModel):
    def __init__(
        self,
        total_number: int = None,
        page_number: int = None,
        page_size: int = None,
        total_page_number: int = None,
    ):
        # {"en":"Total Number", "zh_CN":"总数"}
        self.total_number = total_number
        # {"en":"Page Number", "zh_CN":"页码"}
        self.page_number = page_number
        # {"en":"Page Size", "zh_CN":"每页大小 "}
        self.page_size = page_size
        # {"en":"Total Page Number", "zh_CN":"总页码数"}
        self.total_page_number = total_page_number

    def validate(self):
        self.validate_required(self.total_number, 'total_number')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_page_number, 'total_page_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_number is not None:
            result['totalNumber'] = self.total_number
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_page_number is not None:
            result['totalPageNumber'] = self.total_page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalNumber') is not None:
            self.total_number = m.get('totalNumber')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalPageNumber') is not None:
            self.total_page_number = m.get('totalPageNumber')
        return self


class QueryCaCertificateListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        certificates: List[QueryCaCertificateListCertificate] = None,
        page_info: QueryCaCertificateListPageInfo = None,
    ):
        # {"en":"Result Code, success is 0 ", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"QueryCaCertificateListCertificate list", "zh_CN":"ca证书列表"}
        self.certificates = certificates
        # {"en":"Page Info", "zh_CN":"分页数据"}
        self.page_info = page_info

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.certificates, 'certificates')
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        self.validate_required(self.page_info, 'page_info')
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.certificates is not None:
            result['certificates'] = []
            for k in self.certificates:
                result['certificates'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['pageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('certificates') is not None:
            self.certificates = []
            for k in m.get('certificates'):
                temp_model = QueryCaCertificateListCertificate()
                self.certificates.append(temp_model.from_map(k))
        if m.get('pageInfo') is not None:
            temp_model = QueryCaCertificateListPageInfo()
            self.page_info = temp_model.from_map(m['pageInfo'])
        return self


class QueryCaCertificateListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCaCertificateListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCaCertificateListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCaCertificateListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisassociateDomainWithCaCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        usage: str = None,
        domains: List[str] = None,
    ):
        # {"en":"Certificate ID", "zh_CN":"证书ID"}
        self.certificate_id = certificate_id
        # {"en":"Certificate usage, Allowed value: CLIENT_MTLS,ORIGIN_MTLS  .", "zh_CN":"证书用途，取值范围：CLIENT_MTLS、ORIGIN_MTLS "}
        self.usage = usage
        # {"en":"Associated domains.", "zh_CN":"关联域名列表"}
        self.domains = domains

    def validate(self):
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.usage, 'usage')
        self.validate_required(self.domains, 'domains')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.usage is not None:
            result['usage'] = self.usage
        if self.domains is not None:
            result['domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        if m.get('domains') is not None:
            self.domains = m.get('domains')
        return self


class DisassociateDomainWithCaCertificateResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Status code", "zh_CN":"响应码"}
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


class DisassociateDomainWithCaCertificatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateDomainWithCaCertificateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateDomainWithCaCertificateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisassociateDomainWithCaCertificateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




