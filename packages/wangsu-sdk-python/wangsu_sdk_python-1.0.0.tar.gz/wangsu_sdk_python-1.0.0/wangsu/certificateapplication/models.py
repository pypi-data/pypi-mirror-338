# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetDomainControlValidationContentRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        purchase_record_id: str = None,
    ):
        # {"en":"Order ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"Purchase Record ID", "zh_CN":"采购记录ID"}
        self.purchase_record_id = purchase_record_id

    def validate(self):
        pass

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


class GetDomainControlValidationContentDomainValidateInfo(TeaModel):
    def __init__(
        self,
        domain: str = None,
        validate_file_name: str = None,
        validate_content: str = None,
        expire_time: str = None,
        validate_method: str = None,
        validate_status: str = None,
        record_type: str = None,
    ):
        # {"en":"Domain ", "zh_CN":"域名 "}
        self.domain = domain
        # {"en":"Validate File Name  ", "zh_CN":"验证文件名 "}
        self.validate_file_name = validate_file_name
        # {"en":"Validate value ", "zh_CN":"验证内容 "}
        self.validate_content = validate_content
        # {"en":"Expire Time  ", "zh_CN":"过期时间 "}
        self.expire_time = expire_time
        # {"en":"Validate Method", "zh_CN":"CA厂家实际的验证方式"}
        self.validate_method = validate_method
        # {"en":"Validate Status", "zh_CN":"验证状态,{INIT: 初始化, VALIDATE_WAIT: 待验证, VALIDATE_PROCESSING: 验证中, VALIDATE_SUCCESS: 验证成功, VALIDATE_FAILURE: 验证失败}"}
        self.validate_status = validate_status
        # {"en":"recordType", "zh_CN":"记录类型"}
        self.record_type = record_type

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.validate_file_name, 'validate_file_name')
        self.validate_required(self.validate_content, 'validate_content')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.validate_method, 'validate_method')
        self.validate_required(self.validate_status, 'validate_status')
        self.validate_required(self.record_type, 'record_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.validate_file_name is not None:
            result['validateFileName'] = self.validate_file_name
        if self.validate_content is not None:
            result['validateContent'] = self.validate_content
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.validate_method is not None:
            result['validateMethod'] = self.validate_method
        if self.validate_status is not None:
            result['validateStatus'] = self.validate_status
        if self.record_type is not None:
            result['recordType'] = self.record_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('validateFileName') is not None:
            self.validate_file_name = m.get('validateFileName')
        if m.get('validateContent') is not None:
            self.validate_content = m.get('validateContent')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('validateMethod') is not None:
            self.validate_method = m.get('validateMethod')
        if m.get('validateStatus') is not None:
            self.validate_status = m.get('validateStatus')
        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')
        return self


class GetDomainControlValidationContentResp(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        validate_method: str = None,
        auto_validate: str = None,
        domain_validate_infos: List[GetDomainControlValidationContentDomainValidateInfo] = None,
        purchase_record_id: str = None,
    ):
        # {"en":"Order ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"Validate Method", "zh_CN":"验证方式"}
        self.validate_method = validate_method
        # {"en":"Auto Validate", "zh_CN":"是否自动验证"}
        self.auto_validate = auto_validate
        # {"en":"Domain Validate Information", "zh_CN":"域名验证内容列表"}
        self.domain_validate_infos = domain_validate_infos
        # {"en":"Purchase Record ID", "zh_CN":"采购记录ID"}
        self.purchase_record_id = purchase_record_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.validate_method, 'validate_method')
        self.validate_required(self.auto_validate, 'auto_validate')
        self.validate_required(self.domain_validate_infos, 'domain_validate_infos')
        if self.domain_validate_infos:
            for k in self.domain_validate_infos:
                if k:
                    k.validate()
        self.validate_required(self.purchase_record_id, 'purchase_record_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.validate_method is not None:
            result['validateMethod'] = self.validate_method
        if self.auto_validate is not None:
            result['autoValidate'] = self.auto_validate
        if self.domain_validate_infos is not None:
            result['domainValidateInfos'] = []
            for k in self.domain_validate_infos:
                result['domainValidateInfos'].append(k.to_map() if k else None)
        if self.purchase_record_id is not None:
            result['purchaseRecordId'] = self.purchase_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('validateMethod') is not None:
            self.validate_method = m.get('validateMethod')
        if m.get('autoValidate') is not None:
            self.auto_validate = m.get('autoValidate')
        if m.get('domainValidateInfos') is not None:
            self.domain_validate_infos = []
            for k in m.get('domainValidateInfos'):
                temp_model = GetDomainControlValidationContentDomainValidateInfo()
                self.domain_validate_infos.append(temp_model.from_map(k))
        if m.get('purchaseRecordId') is not None:
            self.purchase_record_id = m.get('purchaseRecordId')
        return self


class GetDomainControlValidationContentResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetDomainControlValidationContentResp = None,
    ):
        # {"en":"Result Code, success is 0 ", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result Data", "zh_CN":"响应数据"}
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
            temp_model = GetDomainControlValidationContentResp()
            self.data = temp_model.from_map(m['data'])
        return self


class GetDomainControlValidationContentPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDomainControlValidationContentParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDomainControlValidationContentRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDomainControlValidationContentResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCertificateSalesOrderDetailForWplusRequest(TeaModel):
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
        pass

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


class QueryCertificateSalesOrderDetailForWplusOrderDetail(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        order_status: str = None,
        certificate_id: int = None,
        certificate_name: str = None,
        certificate_brand: str = None,
        certificate_type: str = None,
        description: str = None,
        algorithm: str = None,
        auto_validate: str = None,
        validate_method: str = None,
        auto_renew: str = None,
        validity_days: int = None,
        country: str = None,
        state: str = None,
        city: str = None,
        street: str = None,
        company: str = None,
        department: str = None,
        common_name: str = None,
        email: str = None,
        subject_alternative_names: str = None,
        create_time: str = None,
        error_message: str = None,
        certificate_spec: str = None,
        domain_type: str = None,
        auto_deploy: str = None,
    ):
        # {"en":"orderId", "zh_CN":"订单id"}
        self.order_id = order_id
        # {"en":"orderStatus
        # ACCEPT_SUCCESS: Received successfully
        # APPLYING: Under application
        # APPLy_FAILURE: Application preparation failed
        # VALIDATETWAIT: To be verified
        # VALIDATE_SUCCESS: Verification successful
        # VALIDATE_SAILURE: Validation failed
        # ISSUEAwaIT: To be issued
        # ISSUE_SUCCESS: Issued successfully
        # ISSUE_SFAILURE: Issuance failed
        # CANCELED: Cancel application
        # REVOKED: Revocation
        # DEPLO_SUCCESS: Deployment successful
        # DEPLOy_Failures: Deployment failed", "zh_CN":"订单状态
        # ACCEPT_SUCCESS: 接收成功
        # APPLYING: 申请中
        # APPLY_FAILURE：申请准备失败
        # VALIDATE_WAIT: 待验证
        # VALIDATE_SUCCESS: 验证成功
        # VALIDATE_FAILURE: 验证失败
        # ISSUE_WAIT: 待签发
        # ISSUE_SUCCESS: 签发成功
        # ISSUE_FAILURE: 签发失败
        # CANCELED: 取消申请
        # REVOKED: 吊销
        # DEPLOY_SUCCESS：部署成功
        # DEPLOY_FAILURE：部署失败"}
        self.order_status = order_status
        # {"en":"certificateId", "zh_CN":"证书id"}
        self.certificate_id = certificate_id
        # {"en":"certificateName", "zh_CN":"证书名"}
        self.certificate_name = certificate_name
        # {"en":"certificateBrand", "zh_CN":"证书品牌"}
        self.certificate_brand = certificate_brand
        # {"en":"certificateType", "zh_CN":"证书类型"}
        self.certificate_type = certificate_type
        # {"en":"description", "zh_CN":"描述"}
        self.description = description
        # {"en":"algorithm", "zh_CN":"算法"}
        self.algorithm = algorithm
        # {"en":"autoValidate", "zh_CN":"是否自动验证"}
        self.auto_validate = auto_validate
        # {"en":"validateMethod", "zh_CN":"验证方式"}
        self.validate_method = validate_method
        # {"en":"autoRenew", "zh_CN":"是否自动续订"}
        self.auto_renew = auto_renew
        # {"en":"validityDays", "zh_CN":"有效天数"}
        self.validity_days = validity_days
        # {"en":"country", "zh_CN":"国家代码"}
        self.country = country
        # {"en":"state", "zh_CN":"省"}
        self.state = state
        # {"en":"city", "zh_CN":"市"}
        self.city = city
        # {"en":"street", "zh_CN":"街道"}
        self.street = street
        # {"en":"company", "zh_CN":"公司"}
        self.company = company
        # {"en":"department", "zh_CN":"部门"}
        self.department = department
        # {"en":"commonName", "zh_CN":"通用名"}
        self.common_name = common_name
        # {"en":"email", "zh_CN":"邮箱"}
        self.email = email
        # {"en":"subjectAlternativeNames", "zh_CN":"主体备用名称"}
        self.subject_alternative_names = subject_alternative_names
        # {"en":"createTime", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"errorMessage", "zh_CN":"错误信息"}
        self.error_message = error_message
        # {"en":"certificateSpec", "zh_CN":"证书规格"}
        self.certificate_spec = certificate_spec
        # {"en":"domainType", "zh_CN":"域名类型"}
        self.domain_type = domain_type
        # {"en":"autoDeploy", "zh_CN":"是否自动部署"}
        self.auto_deploy = auto_deploy

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.order_status, 'order_status')
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.certificate_brand, 'certificate_brand')
        self.validate_required(self.certificate_type, 'certificate_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.auto_validate, 'auto_validate')
        self.validate_required(self.validate_method, 'validate_method')
        self.validate_required(self.auto_renew, 'auto_renew')
        self.validate_required(self.validity_days, 'validity_days')
        self.validate_required(self.country, 'country')
        self.validate_required(self.state, 'state')
        self.validate_required(self.city, 'city')
        self.validate_required(self.street, 'street')
        self.validate_required(self.company, 'company')
        self.validate_required(self.department, 'department')
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.email, 'email')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.certificate_spec, 'certificate_spec')
        self.validate_required(self.domain_type, 'domain_type')
        self.validate_required(self.auto_deploy, 'auto_deploy')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.certificate_brand is not None:
            result['certificateBrand'] = self.certificate_brand
        if self.certificate_type is not None:
            result['certificateType'] = self.certificate_type
        if self.description is not None:
            result['description'] = self.description
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.auto_validate is not None:
            result['autoValidate'] = self.auto_validate
        if self.validate_method is not None:
            result['validateMethod'] = self.validate_method
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.validity_days is not None:
            result['validityDays'] = self.validity_days
        if self.country is not None:
            result['country'] = self.country
        if self.state is not None:
            result['state'] = self.state
        if self.city is not None:
            result['city'] = self.city
        if self.street is not None:
            result['street'] = self.street
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.certificate_spec is not None:
            result['certificateSpec'] = self.certificate_spec
        if self.domain_type is not None:
            result['domainType'] = self.domain_type
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('certificateBrand') is not None:
            self.certificate_brand = m.get('certificateBrand')
        if m.get('certificateType') is not None:
            self.certificate_type = m.get('certificateType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('autoValidate') is not None:
            self.auto_validate = m.get('autoValidate')
        if m.get('validateMethod') is not None:
            self.validate_method = m.get('validateMethod')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('validityDays') is not None:
            self.validity_days = m.get('validityDays')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('street') is not None:
            self.street = m.get('street')
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('certificateSpec') is not None:
            self.certificate_spec = m.get('certificateSpec')
        if m.get('domainType') is not None:
            self.domain_type = m.get('domainType')
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        return self


class QueryCertificateSalesOrderDetailForWplusResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryCertificateSalesOrderDetailForWplusOrderDetail = None,
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
            temp_model = QueryCertificateSalesOrderDetailForWplusOrderDetail()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCertificateSalesOrderDetailForWplusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateSalesOrderDetailForWplusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateSalesOrderDetailForWplusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCertificateSalesOrderDetailForWplusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateCertificateApplyingOrderIdentificationInfo(TeaModel):
    def __init__(
        self,
        country: str = None,
        state: str = None,
        city: str = None,
        company: str = None,
        department: str = None,
        common_name: str = None,
        email: str = None,
        street: str = None,
        subject_alternative_names: List[str] = None,
        street_1: str = None,
        phone: str = None,
        postal_code: str = None,
    ):
        # {"en":"Country. An ISO-3166 country code.
        # Range: = 2 characters", "zh_CN":"国家，2个字符的ISO-3166国家代码"}
        self.country = country
        # {"en":"A state or province.", "zh_CN":"省"}
        self.state = state
        # {"en":"A city", "zh_CN":"城市"}
        self.city = city
        # {"en":"A company name", "zh_CN":"公司"}
        self.company = company
        # {"en":"The department associated with the certificate", "zh_CN":"部门"}
        self.department = department
        # {"en":"A common name of the certificate", "zh_CN":"证书的通用名称"}
        self.common_name = common_name
        # {"en":"Email address", "zh_CN":"邮箱"}
        self.email = email
        # {"en":"The street where the company is located", "zh_CN":"街道"}
        self.street = street
        # {"en":"Hostnames that this certificate will serve. Each entry must be a valid hostname such as example.com or a wildcard hostname beginning with '*' such as.example.com.", "zh_CN":"此证书将提供服务的域名。 每个条目必须是有效的域名（例如 example.com）或以“*”开头的泛域名（例如 “*.example.com”）"}
        self.subject_alternative_names = subject_alternative_names
        # {"en":"street1", "zh_CN":"街道"}
        self.street_1 = street_1
        # {"en":"phone", "zh_CN":"联系电话"}
        self.phone = phone
        # {"en":"postalCode", "zh_CN":"邮政编码"}
        self.postal_code = postal_code

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
        if self.street is not None:
            result['street'] = self.street
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        if self.street_1 is not None:
            result['street1'] = self.street_1
        if self.phone is not None:
            result['phone'] = self.phone
        if self.postal_code is not None:
            result['postalCode'] = self.postal_code
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
        if m.get('street') is not None:
            self.street = m.get('street')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        if m.get('street1') is not None:
            self.street_1 = m.get('street1')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('postalCode') is not None:
            self.postal_code = m.get('postalCode')
        return self


class CreateCertificateApplyingOrderLinkman(TeaModel):
    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        phone: str = None,
        email: str = None,
        title: str = None,
    ):
        # {"en":"firstName, Self verify organizational information. This field is mandatory", "zh_CN":"名，自行验证组织信息此字段必填"}
        self.first_name = first_name
        # {"en":"lastName, Self verify organizational information. This field is mandatory", "zh_CN":"姓，自行验证组织信息此字段必填"}
        self.last_name = last_name
        # {"en":"phone, Self verify organizational information. This field is mandatory", "zh_CN":"电话，自行验证组织信息此字段必填"}
        self.phone = phone
        # {"en":"email, Self verify organizational information. This field is mandatory", "zh_CN":"邮箱，自行验证组织信息此字段必填"}
        self.email = email
        # {"en":"title, Self verify organizational information. This field is mandatory", "zh_CN":"职位，自行验证组织信息此字段必填"}
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_name is not None:
            result['firstName'] = self.first_name
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.email is not None:
            result['email'] = self.email
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstName') is not None:
            self.first_name = m.get('firstName')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateCertificateApplyingOrderDnsProviderInfo(TeaModel):
    def __init__(
        self,
        domain: str = None,
        dns_provider_code: str = None,
        dns_api_access: str = None,
    ):
        # {"en":"domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"DNS Provider Code, Support CloudDNS", "zh_CN":"DNS托管商编码，支持CloudDNS"}
        self.dns_provider_code = dns_provider_code
        # {"en":"DNS Api Access, JSON format: The hosting provider is CloudDNS, JSON KEY is accessKey  and secretKey", "zh_CN":"DNS托管商API凭证，JSON格式，托管商为CloudDNS，JSON KEY为accessKey、secretKey"}
        self.dns_api_access = dns_api_access

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.dns_provider_code, 'dns_provider_code')
        self.validate_required(self.dns_api_access, 'dns_api_access')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.dns_provider_code is not None:
            result['dnsProviderCode'] = self.dns_provider_code
        if self.dns_api_access is not None:
            result['dnsApiAccess'] = self.dns_api_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dnsProviderCode') is not None:
            self.dns_provider_code = m.get('dnsProviderCode')
        if m.get('dnsApiAccess') is not None:
            self.dns_api_access = m.get('dnsApiAccess')
        return self


class CreateCertificateApplyingOrderRequest(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        description: str = None,
        auto_renew: str = None,
        certificate_brand: str = None,
        certificate_spec: str = None,
        certificate_type: str = None,
        algorithm: str = None,
        auto_validate: str = None,
        validate_method: str = None,
        auto_deploy: str = None,
        validity_days: int = None,
        identification_info: CreateCertificateApplyingOrderIdentificationInfo = None,
        backup_certificate_brand: str = None,
        org_validate_method: str = None,
        domain_type: str = None,
        batch_apply: str = None,
        admin: CreateCertificateApplyingOrderLinkman = None,
        tech: CreateCertificateApplyingOrderLinkman = None,
        dns_provider_infos: List[CreateCertificateApplyingOrderDnsProviderInfo] = None,
    ):
        # {"en":"Name of the certificate. The certificate name cannot be the same as your existing certificate.
        # Range: <= 128 characters.", "zh_CN":"证书名称，最长不超过128个字符。证书名称不允许与已有的证书重名."}
        self.certificate_name = certificate_name
        # {"en":"A description of the new certificate.
        # Range: <= 256 characters.", "zh_CN":"证书描述，最长不超过256个字符。"}
        self.description = description
        # {"en":"Automatically Renew your certificate. Selecting 'true' will reduce customization of other fields: 'certificateBrand' must be 'LE','validateMethod' must be 'HTTP', the certificate domain must configure in our acceleration platform; the domain  must CNAME to our acceleration platform.
        # Allowed values: true, false(default) .", "zh_CN":"是否自动续签，取值范围：true、false(默认) 。选择是否在证书到期前为您自动续订证书，开启自动续签，证书品牌必须选择'LE'；验证方式必须选择'HTTP'；申请证书包含的域名必须已在我司加速平台配置，且域名必须已CNAME到我司加速平台。"}
        self.auto_renew = auto_renew
        # {"en":"Certificate Brand. Selecting 'LE' means we apply your certificate through Let's Encrypt (https://letsencrypt.org/docs/challenge-types/) .
        # Allowed value: LE TrustAsia . Note: If the LE brand application fails, it will automatically switch to the ZeroSSL CA manufacturer for certificate application", "zh_CN":"证书品牌，取值范围：LE、TrustAsia 。 'LE '即Let's Encrypt。备注：如果LE品牌申请失败，会自动切换成ZeroSSL CA厂家进行证书申请"}
        self.certificate_brand = certificate_brand
        # {"en":"Certificate Specification,
        # Certificate brand GlobalSign, certificate specification GlobalSignOVMSSSL, certificate type OV, certificate validity days [360], billing;
        # Certificate brand GlobalSign, certificate specification GlobalSignOVSANsMSSL, certificate type OV, certificate validity days [360], billing;
        # Certificate brand TrustAsia, certificate specification TrustAsia TLSC1, certificate type DV, certificate validity days [360], billing;
        # Certificate brand TrustAsia, certificate specification TrustAsiaTLSSANsC1, certificate type DV, certificate validity days [360], billing;
        # Certificate brand TrustAsia, certificate specification TrustAsiaC1DVFree, certificate type DV, certificate validity days [90], free of charge;
        # Certificate brand TrustAsia, certificate specification TrustAsiaC1DVFreeSANS, certificate type DV, certificate validity days [90], free of charge;
        # Certificate brand LE, certificate specification LetsEncryptDVFree, certificate type DV, certificate validity days [90], free of charge;
        # Certificate Brand LE, Certificate Specification LetsEncryptDVFreeSANS, Certificate Type DV, Certificate Validity Days [90], free of charge", "zh_CN":"证书规格,
        # 证书品牌GlobalSign、证书规格GlobalSignOVMSSL、证书类型OV、证书有效天数[360]、计费;
        # 证书品牌GlobalSign、证书规格GlobalSignOVSANsMSSL、证书类型OV、证书有效天数[360]、计费;
        # 证书品牌TrustAsia、证书规格TrustAsiaTLSC1、证书类型DV、证书有效天数[360]、计费;
        # 证书品牌TrustAsia、证书规格TrustAsiaTLSSANsC1、证书类型DV、证书有效天数[360]、计费;
        # 证书品牌TrustAsia、证书规格TrustAsiaC1DVFree、证书类型DV、证书有效天数[90]、免费;
        # 证书品牌TrustAsia、证书规格TrustAsiaC1DVFreeSANS、证书类型DV、证书有效天数[90]、免费;
        # 证书品牌LE、证书规格LetsEncryptDVFree、证书类型DV、证书有效天数[90]、免费;
        # 证书品牌LE、证书规格LetsEncryptDVFreeSANS、证书类型DV、证书有效天数[90]、免费"}
        self.certificate_spec = certificate_spec
        # {"en":"Certificate Type. When 'certificateBrand' specifying 'LE',  'certificateType' only supports 'DV'.
        # TrustAsia supports DV and OV.", "zh_CN":"安全等级，取值范围: DV、OV 。 Let's Encrypt仅支持DV， TrustAsia支持DV和OV。"}
        self.certificate_type = certificate_type
        # {"en":"Certificate Algorithm. When 'certificateBrand' specifying 'LE',  'certificateType' only supports 'RSA2048' and 'ECDSA256'.
        # Allowed values: RSA2048, ECDSA256 .", "zh_CN":"证书算法，取值范围：RSA2048、ECDSA256。 Let's Encrypt仅支持RSA2048与ECDSA256  。"}
        self.algorithm = algorithm
        # {"en":"Automatically validate that you control the domains in the certificate you applied. Selecting 'true' will reduce customization of other fields: 'validateMethod' must be 'HTTP' , the certificate domain must configure in our acceleration platform; the domain must CNAME to our acceleration platform.
        # Allowed values: true, false .", "zh_CN":"是否自动验证，取值范围：true、false。选择是否帮您自动完成证书域名控制权验证。开启自动验证，证书品牌必须选择'LE'；验证方式必须选择'HTTP'；申请证书包含的域名必须已在我司加速平台配置，且域名必须已CNAME到我司加速平台。"}
        self.auto_validate = auto_validate
        # {"en":"Validate Method selected for the order to validate that you control the domains in the certificate. Validate Method must be 'DNS' when 'subjectAlternativeNames'  is a wildcard hostname beginning with '*' such as '*.example.com' .
        # Allowed values: HTTP, DNS .  When applying for a certificate with an IP domain name, only HTTP authentication is supported.", "zh_CN":"验证方式，取值范围：HTTP、DNS 。选择证书域名控制权的验证方式。当申请证书域名'subjectAlternativeNames'为泛域名时，仅支持DNS验证。当申请证书域名为IP时，仅支持HTTP验证。"}
        self.validate_method = validate_method
        # {"en":"Whether to deploy automatically. Value range: true, false, true: automatic deployment, false: manual deployment.", "zh_CN":"是否自动部署，取值范围：true、false，true:自动部署,   false:手动部署"}
        self.auto_deploy = auto_deploy
        # {"en":"Validity Days selected for the certificate. Please refer to the description in the certificateSpec for details.", "zh_CN":"证书有效天数，详见certificateSpec描述"}
        self.validity_days = validity_days
        # {"en":"Certificate Signing Request Informtion.", "zh_CN":"证书签名请求信息 。"}
        self.identification_info = identification_info
        # {"en":"Backup Certificate Brand.
        # The certificate brand LE for a single domain name is optional, and the backup CA certificate brand is TrustAsia ZeroSSL
        # Certificate brand: LE for multiple domain names, optional backup CA certificate brand: TrustAsia
        # Certificate brand ZeroSSL single domain name optional backup CA certificate brand TrustAsia LE
        # Certificate brand TrustAsia single domain name optional backup CA certificate brand is LE ZeroSSL
        # Certificate Brand TrustAsia Multi Domain Optional Backup CA Certificate Brand LE", "zh_CN":"备用CA证书品牌，
        # 证书品牌LE单域名可选备用CA证书品牌为TrustAsia、ZeroSSL
        # 证书品牌LE多域名可选备用CA证书品牌为TrustAsia
        # 证书品牌ZeroSSL单域名可选备用CA证书品牌为TrustAsia、LE
        # 证书品牌TrustAsia单域名可选备用CA证书品牌为LE、ZeroSSL
        # 证书品牌TrustAsia多域名可选备用CA证书品牌为LE"}
        self.backup_certificate_brand = backup_certificate_brand
        # {"en":"orgValidateMethod, default:  Enable pre audit, self_validate:  Self verify organizational information, none: Unorganized information, default value default.", "zh_CN":"组织验证方式, default: 开启预审核、self_validate: 自行验证组织信息、none: 无组织信息，默认值default。"}
        self.org_validate_method = org_validate_method
        # {"en":"domainType, Value range: single multi", "zh_CN":"域名类型，取值范围：single、multi"}
        self.domain_type = domain_type
        # {"en":"batchApply, Value range: true false, Default false", "zh_CN":"是否批量申请，取值范围：true、false，默认false"}
        self.batch_apply = batch_apply
        # {"en":"admin", "zh_CN":"订单管理联系人"}
        self.admin = admin
        # {"en":"tech", "zh_CN":"订单技术联系人"}
        self.tech = tech
        # {"en":"DNS Provider Infomation", "zh_CN":"DNS托管商信息"}
        self.dns_provider_infos = dns_provider_infos

    def validate(self):
        self.validate_required(self.certificate_brand, 'certificate_brand')
        self.validate_required(self.certificate_spec, 'certificate_spec')
        self.validate_required(self.certificate_type, 'certificate_type')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.auto_validate, 'auto_validate')
        self.validate_required(self.validate_method, 'validate_method')
        self.validate_required(self.auto_deploy, 'auto_deploy')
        self.validate_required(self.validity_days, 'validity_days')
        self.validate_required(self.identification_info, 'identification_info')
        if self.identification_info:
            self.identification_info.validate()
        if self.admin:
            self.admin.validate()
        if self.tech:
            self.tech.validate()
        if self.dns_provider_infos:
            for k in self.dns_provider_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.description is not None:
            result['description'] = self.description
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.certificate_brand is not None:
            result['certificateBrand'] = self.certificate_brand
        if self.certificate_spec is not None:
            result['certificateSpec'] = self.certificate_spec
        if self.certificate_type is not None:
            result['certificateType'] = self.certificate_type
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.auto_validate is not None:
            result['autoValidate'] = self.auto_validate
        if self.validate_method is not None:
            result['validateMethod'] = self.validate_method
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.validity_days is not None:
            result['validityDays'] = self.validity_days
        if self.identification_info is not None:
            result['identificationInfo'] = self.identification_info.to_map()
        if self.backup_certificate_brand is not None:
            result['backupCertificateBrand'] = self.backup_certificate_brand
        if self.org_validate_method is not None:
            result['orgValidateMethod'] = self.org_validate_method
        if self.domain_type is not None:
            result['domainType'] = self.domain_type
        if self.batch_apply is not None:
            result['batchApply'] = self.batch_apply
        if self.admin is not None:
            result['admin'] = self.admin.to_map()
        if self.tech is not None:
            result['tech'] = self.tech.to_map()
        if self.dns_provider_infos is not None:
            result['dnsProviderInfos'] = []
            for k in self.dns_provider_infos:
                result['dnsProviderInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('certificateBrand') is not None:
            self.certificate_brand = m.get('certificateBrand')
        if m.get('certificateSpec') is not None:
            self.certificate_spec = m.get('certificateSpec')
        if m.get('certificateType') is not None:
            self.certificate_type = m.get('certificateType')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('autoValidate') is not None:
            self.auto_validate = m.get('autoValidate')
        if m.get('validateMethod') is not None:
            self.validate_method = m.get('validateMethod')
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('validityDays') is not None:
            self.validity_days = m.get('validityDays')
        if m.get('identificationInfo') is not None:
            temp_model = CreateCertificateApplyingOrderIdentificationInfo()
            self.identification_info = temp_model.from_map(m['identificationInfo'])
        if m.get('backupCertificateBrand') is not None:
            self.backup_certificate_brand = m.get('backupCertificateBrand')
        if m.get('orgValidateMethod') is not None:
            self.org_validate_method = m.get('orgValidateMethod')
        if m.get('domainType') is not None:
            self.domain_type = m.get('domainType')
        if m.get('batchApply') is not None:
            self.batch_apply = m.get('batchApply')
        if m.get('admin') is not None:
            temp_model = CreateCertificateApplyingOrderLinkman()
            self.admin = temp_model.from_map(m['admin'])
        if m.get('tech') is not None:
            temp_model = CreateCertificateApplyingOrderLinkman()
            self.tech = temp_model.from_map(m['tech'])
        if m.get('dnsProviderInfos') is not None:
            self.dns_provider_infos = []
            for k in m.get('dnsProviderInfos'):
                temp_model = CreateCertificateApplyingOrderDnsProviderInfo()
                self.dns_provider_infos.append(temp_model.from_map(k))
        return self


class CreateCertificateApplyingOrderResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: dict = None,
        order_id: str = None,
        order_ids: List[str] = None,
        purchase_record_ids: List[str] = None,
    ):
        # {"en":"Result Code, success is 0", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result Data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Order ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"Order ID List", "zh_CN":"订单ID列表"}
        self.order_ids = order_ids
        # {"en":"Purchase Record ID List", "zh_CN":"采购记录ID列表"}
        self.purchase_record_ids = purchase_record_ids

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.order_ids, 'order_ids')
        self.validate_required(self.purchase_record_ids, 'purchase_record_ids')

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
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.purchase_record_ids is not None:
            result['purchaseRecordIds'] = self.purchase_record_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('purchaseRecordIds') is not None:
            self.purchase_record_ids = m.get('purchaseRecordIds')
        return self


class CreateCertificateApplyingOrderPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCertificateApplyingOrderParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCertificateApplyingOrderRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCertificateApplyingOrderResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetCertificateApplyingOrderListPageParam(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
    ):
        # {"en":"Page Size,Range:1-100 (default:100)  ", "zh_CN":"每页大小，1-100，默认值100"}
        self.page_size = page_size
        # {"en":"Page Number, the first page must be 0. 
        # Range:>=0 (default:0)  ", "zh_CN":"页码，当前页，第一页从0开始，必须大于等于0，默认值0"}
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        return self


class GetCertificateApplyingOrderListRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        order_status: List[str] = None,
        certificate_name: str = None,
        domain: str = None,
        start_time: str = None,
        end_time: str = None,
        page_param: GetCertificateApplyingOrderListPageParam = None,
    ):
        # {"en":"GetCertificateApplyingOrderListOrder ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"Status of certificate apply order. Allowed values: ACCEPT_SUCCESS,APPLYING,ISSUE_SUCCESS,ISSUE_FAILURE,REVOKED,CANCELED. ", "zh_CN":"订单状态，取值范围：ACCEPT_SUCCESS,APPLYING,ISSUE_SUCCESS,ISSUE_FAILURE,REVOKED,CANCELED。
        #     ACCEPT_SUCCESS：订单提交成功，待后台发起证书申请；
        #     APPLYING：证书申请中，待域名验证；
        #     ISSUE_SUCCESS：证书签发成功，可进行证书配置与部署；
        #     ISSUE_FAILURE：证书签发失败；
        #     REVOKED：证书已吊销；
        #     CANCELED：已取消证书申请；
        #     "}
        self.order_status = order_status
        # {"en":"Certificate Name ", "zh_CN":"证书名称"}
        self.certificate_name = certificate_name
        # {"en":"Domain ", "zh_CN":"域名 "}
        self.domain = domain
        # {"en":"The time when the certificate order was created. The format is yyyy-MM-dd HH:mm:ss ", "zh_CN":"订单创建时间，格式为：yyyy-MM-dd HH:mm:ss "}
        self.start_time = start_time
        # {"en":"The time when the certificate order was finished. The format is yyyy-MM-dd HH:mm:ss ", "zh_CN":"订单结束时间，格式为：yyyy-MM-dd HH:mm:ss。证书签发成功或证书签发失败，则记录结束时间。 "}
        self.end_time = end_time
        # {"en":"Page Parammeter.", "zh_CN":"分页参数"}
        self.page_param = page_param

    def validate(self):
        if self.page_param:
            self.page_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_param is not None:
            result['pageParam'] = self.page_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageParam') is not None:
            temp_model = GetCertificateApplyingOrderListPageParam()
            self.page_param = temp_model.from_map(m['pageParam'])
        return self


class GetCertificateApplyingOrderListOrder(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        order_status: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        certificate_brand: str = None,
        certificate_type: str = None,
        auto_renew: str = None,
        description: str = None,
        common_name: str = None,
        subject_alternative_names: str = None,
        create_time: str = None,
    ):
        # {"en":"GetCertificateApplyingOrderListOrder ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"Status of certificate apply order.
        # Allowed values: ACCEPT_SUCCESS,APPLYING,ISSUE_SUCCESS,ISSUE_FAILURE,REVOKED,CANCELED.  ", "zh_CN":"证书订单状态，取值范围：ACCEPT_SUCCESS,APPLYING,ISSUE_SUCCESS,ISSUE_FAILURE,REVOKED,CANCELED。"}
        self.order_status = order_status
        # {"en":"Certificate ID ", "zh_CN":"证书ID "}
        self.certificate_id = certificate_id
        # {"en":"Certificate Name ", "zh_CN":"证书名称 "}
        self.certificate_name = certificate_name
        # {"en":"Certificate Brand ", "zh_CN":"证书品牌"}
        self.certificate_brand = certificate_brand
        # {"en":"Certificate Type ", "zh_CN":"证书类型 "}
        self.certificate_type = certificate_type
        # {"en":"Auto Renew ", "zh_CN":"是否自动续签 "}
        self.auto_renew = auto_renew
        # {"en":"Description ", "zh_CN":"描述 "}
        self.description = description
        # {"en":"Common Name of the certificate ", "zh_CN":"证书的通用名称 "}
        self.common_name = common_name
        # {"en":"SAN ", "zh_CN":"主体备用名称 "}
        self.subject_alternative_names = subject_alternative_names
        # {"en":"Create Time ", "zh_CN":"创建时间 "}
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.order_status, 'order_status')
        self.validate_required(self.certificate_id, 'certificate_id')
        self.validate_required(self.certificate_name, 'certificate_name')
        self.validate_required(self.certificate_brand, 'certificate_brand')
        self.validate_required(self.certificate_type, 'certificate_type')
        self.validate_required(self.auto_renew, 'auto_renew')
        self.validate_required(self.description, 'description')
        self.validate_required(self.common_name, 'common_name')
        self.validate_required(self.subject_alternative_names, 'subject_alternative_names')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.order_status is not None:
            result['orderStatus'] = self.order_status
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['certificateName'] = self.certificate_name
        if self.certificate_brand is not None:
            result['certificateBrand'] = self.certificate_brand
        if self.certificate_type is not None:
            result['certificateType'] = self.certificate_type
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.description is not None:
            result['description'] = self.description
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.subject_alternative_names is not None:
            result['subjectAlternativeNames'] = self.subject_alternative_names
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('orderStatus') is not None:
            self.order_status = m.get('orderStatus')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('certificateName') is not None:
            self.certificate_name = m.get('certificateName')
        if m.get('certificateBrand') is not None:
            self.certificate_brand = m.get('certificateBrand')
        if m.get('certificateType') is not None:
            self.certificate_type = m.get('certificateType')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('subjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('subjectAlternativeNames')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class GetCertificateApplyingOrderListPageInfo(TeaModel):
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


class GetCertificateApplyingOrderListResp(TeaModel):
    def __init__(
        self,
        orders: List[GetCertificateApplyingOrderListOrder] = None,
        page_info: GetCertificateApplyingOrderListPageInfo = None,
    ):
        # {"en":"GetCertificateApplyingOrderListOrder list", "zh_CN":"订单列表"}
        self.orders = orders
        # {"en":"Page Info", "zh_CN":"分页数据"}
        self.page_info = page_info

    def validate(self):
        self.validate_required(self.orders, 'orders')
        if self.orders:
            for k in self.orders:
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
        if self.orders is not None:
            result['orders'] = []
            for k in self.orders:
                result['orders'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['pageInfo'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orders') is not None:
            self.orders = []
            for k in m.get('orders'):
                temp_model = GetCertificateApplyingOrderListOrder()
                self.orders.append(temp_model.from_map(k))
        if m.get('pageInfo') is not None:
            temp_model = GetCertificateApplyingOrderListPageInfo()
            self.page_info = temp_model.from_map(m['pageInfo'])
        return self


class GetCertificateApplyingOrderListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetCertificateApplyingOrderListResp = None,
    ):
        # {"en":"Result Code, success is 0 ", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result Data", "zh_CN":"响应数据"}
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
            temp_model = GetCertificateApplyingOrderListResp()
            self.data = temp_model.from_map(m['data'])
        return self


class GetCertificateApplyingOrderListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCertificateApplyingOrderListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCertificateApplyingOrderListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCertificateApplyingOrderListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CancelCertificateApplyingOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        purchase_record_id: str = None,
    ):
        # {"en":"The orderId", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"The purchaseRecordId", "zh_CN":"采购记录ID"}
        self.purchase_record_id = purchase_record_id

    def validate(self):
        pass

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


class CancelCertificateApplyingOrderResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Result Code, 0 means successful ", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
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


class CancelCertificateApplyingOrderPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelCertificateApplyingOrderParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelCertificateApplyingOrderRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CancelCertificateApplyingOrderResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




