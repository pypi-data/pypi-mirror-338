# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryCsrServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrServiceResponseData(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryCsrServiceResponseData = None,
        id: str = None,
        name: str = None,
        algorithm: str = None,
        csr_file: str = None,
        domain: str = None,
        sans: List[str] = None,
        comment: str = None,
        country: str = None,
        state: str = None,
        city: str = None,
        company: str = None,
        department: str = None,
    ):
        # {"en":"Request result code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Request result data", "zh_CN":"请求结果数据"}
        self.data = data
        # {"en":"CSR ID", "zh_CN":"CSR ID"}
        self.id = id
        # {"en":"CSR name, which cannot be repeated", "zh_CN":"csr名称，不能重复"}
        self.name = name
        # {"en":"Key algorithm: RSA/EC", "zh_CN":"密钥算法：RSA/EC 二选一"}
        self.algorithm = algorithm
        # {"en":"csr content", "zh_CN":"CSR内容"}
        self.csr_file = csr_file
        # {"en":"The main domain name", "zh_CN":"主域名"}
        self.domain = domain
        # {"en":"Backup domain name list", "zh_CN":"备份域名列表"}
        self.sans = sans
        # {"en":"comment", "zh_CN":"备注"}
        self.comment = comment
        # {"en":"Country or region", "zh_CN":"国家地区"}
        self.country = country
        # {"en":"state", "zh_CN":"州"}
        self.state = state
        # {"en":"city", "zh_CN":"城市"}
        self.city = city
        # {"en":"company", "zh_CN":"公司"}
        self.company = company
        # {"en":"department", "zh_CN":"部门"}
        self.department = department

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.csr_file, 'csr_file')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.sans, 'sans')
        self.validate_required(self.comment, 'comment')
        self.validate_required(self.country, 'country')
        self.validate_required(self.state, 'state')
        self.validate_required(self.city, 'city')
        self.validate_required(self.company, 'company')
        self.validate_required(self.department, 'department')

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.csr_file is not None:
            result['csr-file'] = self.csr_file
        if self.domain is not None:
            result['domain'] = self.domain
        if self.sans is not None:
            result['sans'] = self.sans
        if self.comment is not None:
            result['comment'] = self.comment
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = QueryCsrServiceResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('csr-file') is not None:
            self.csr_file = m.get('csr-file')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
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
        return self


class QueryCsrServicePaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"CSR ID", "zh_CN":"CSR ID"}
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


class QueryCsrServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateTheCsrRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        algorithm: str = None,
        domain: str = None,
        sans: List[str] = None,
        country: str = None,
        state: str = None,
        city: str = None,
        company: str = None,
        department: str = None,
        comment: str = None,
    ):
        # {"en":"Enter a unique name representing your CSR. This is shown in the SSL List in the portal but is not shared with the certificate authority. This field is required.", "zh_CN":"csr名称，不能重复"}
        self.name = name
        # {"en":"Key algorithm: RSA/EC
        # Choose RSA if you will use the RSA algorithm for your certificate. Choose EC if you will be using Elliptic Curve Cryptography instead.", "zh_CN":"密钥算法：RSA/EC 二选一"}
        self.algorithm = algorithm
        # {"en":"The main domain name", "zh_CN":"主域名"}
        self.domain = domain
        # {"en":"If you wish to specify subject alternative names for your certificate.Wildcards are permitted. Specify '*' in front of the domain name. For example, *.domain.com.You must enter like this
        # sans': [
        # 		'aaa.com',
        # 		'bbb.com'
        # 	]", "zh_CN":"备份域名列表"}
        self.sans = sans
        # {"en":"Choose the country where your organization is located.", "zh_CN":"国家地区"}
        self.country = country
        # {"en":"Enter the state/region where your organization is located. This shouldn't be abbreviated.", "zh_CN":"州"}
        self.state = state
        # {"en":"Enter the city where your organization is located.", "zh_CN":"城市"}
        self.city = city
        # {"en":"Enter the legal name for your company. Do not abbreviate.", "zh_CN":"公司"}
        self.company = company
        # {"en":"department", "zh_CN":"部门"}
        self.department = department
        # {"en":"Enter a department name if appropriate.", "zh_CN":"备注"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.domain is not None:
            result['domain'] = self.domain
        if self.sans is not None:
            result['sans'] = self.sans
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
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
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
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class CreateTheCsrResponseData(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateTheCsrResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: CreateTheCsrResponseData = None,
        id: str = None,
    ):
        # {"en":"Request result code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Request result data", "zh_CN":"请求结果数据"}
        self.data = data
        # {"en":"Added CSR ID after success, child node of data node", "zh_CN":"新增成功后的csr id ，&ldquo;data&rdquo;节点的子节点"}
        self.id = id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.id, 'id')

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
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            temp_model = CreateTheCsrResponseData()
            self.data = temp_model.from_map(m['data'])
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateTheCsrPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateTheCsrParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateTheCsrRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateTheCsrResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryCsrListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrListResponseCsrRecords(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        algorithm: str = None,
        domain: str = None,
        comment: str = None,
    ):
        # {"en":"CSR ID", "zh_CN":"CSR ID"}
        self.id = id
        # {"en":"CSR name", "zh_CN":"csr名称"}
        self.name = name
        # {"en":"Key algorithm", "zh_CN":"密钥算法"}
        self.algorithm = algorithm
        # {"en":"The main domain name", "zh_CN":"主域名"}
        self.domain = domain
        # {"en":"comment", "zh_CN":"备注"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.algorithm, 'algorithm')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.comment, 'comment')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.domain is not None:
            result['domain'] = self.domain
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class QueryCsrListResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        csr_records: List[QueryCsrListResponseCsrRecords] = None,
    ):
        # {"en":"Request result code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Request result data", "zh_CN":"请求结果数据"}
        self.csr_records = csr_records

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.csr_records, 'csr_records')
        if self.csr_records:
            for k in self.csr_records:
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
        if self.csr_records is not None:
            result['csr-records'] = []
            for k in self.csr_records:
                result['csr-records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('csr-records') is not None:
            self.csr_records = []
            for k in m.get('csr-records'):
                temp_model = QueryCsrListResponseCsrRecords()
                self.csr_records.append(temp_model.from_map(k))
        return self


class QueryCsrListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCsrListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteCsrRecordRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCsrRecordResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Request result code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Request result data", "zh_CN":"请求结果数据"}
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


class DeleteCsrRecordPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"Request id", "zh_CN":"请求id"}
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


class DeleteCsrRecordParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCsrRecordRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCsrRecordResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




