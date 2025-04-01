# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class IcpQueryServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IcpQueryServiceResponseDomainIcpDataList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        icp_number: str = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Registration No.", "zh_CN":"备案号"}
        self.icp_number = icp_number

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.icp_number, 'icp_number')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.icp_number is not None:
            result['icp-number'] = self.icp_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('icp-number') is not None:
            self.icp_number = m.get('icp-number')
        return self


class IcpQueryServiceResponse(TeaModel):
    def __init__(
        self,
        domain_icp_data_list: List[IcpQueryServiceResponseDomainIcpDataList] = None,
    ):
        # {'en':'domainIcpData', 'zh_CN':'域名备案信息'}
        self.domain_icp_data_list = domain_icp_data_list

    def validate(self):
        self.validate_required(self.domain_icp_data_list, 'domain_icp_data_list')
        if self.domain_icp_data_list:
            for k in self.domain_icp_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_icp_data_list is not None:
            result['domain-icp-data'] = []
            for k in self.domain_icp_data_list:
                result['domain-icp-data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-icp-data') is not None:
            self.domain_icp_data_list = []
            for k in m.get('domain-icp-data'):
                temp_model = IcpQueryServiceResponseDomainIcpDataList()
                self.domain_icp_data_list.append(temp_model.from_map(k))
        return self


class IcpQueryServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IcpQueryServiceParameters(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # {"en":"Domain names, multiple domain names are separated by English semicolons. The maximum number of domain names is 20.", "zh_CN":"域名，多个以英文分号分隔。域名数上限为20个。"}
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


class IcpQueryServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IcpQueryServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryBandwidthLimitTaskListServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthLimitTaskListServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        bandwidth_limit: int = None,
        task_name: str = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain_name = domain_name
        # {'en':'Maximum bandwidth set', 'zh_CN':'设置的最大带宽值'}
        self.bandwidth_limit = bandwidth_limit
        # {'en':'Task name', 'zh_CN':'任务名称'}
        self.task_name = task_name

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.bandwidth_limit, 'bandwidth_limit')
        self.validate_required(self.task_name, 'task_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.bandwidth_limit is not None:
            result['bandwidthLimit'] = self.bandwidth_limit
        if self.task_name is not None:
            result['taskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('bandwidthLimit') is not None:
            self.bandwidth_limit = m.get('bandwidthLimit')
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        return self


class QueryBandwidthLimitTaskListServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryBandwidthLimitTaskListServiceResponseResult] = None,
    ):
        # {'en':'result', 'zh_CN':'结果'}
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
                temp_model = QueryBandwidthLimitTaskListServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryBandwidthLimitTaskListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthLimitTaskListServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthLimitTaskListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryBandwidthLimitTaskListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryForbiddingVisitorIPsByLabelCodeServiceRequest(TeaModel):
    def __init__(
        self,
        label_code_list: List[str] = None,
        ip_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # {"en":"List of forbidding Label Code", "zh_CN":"封禁标签列表"}
        self.label_code_list = label_code_list
        # {"en":"List of forbidding IP, leave it empty to query all ", "zh_CN":"封禁IP列表,放空则查询全部"}
        self.ip_list = ip_list
        # {"en":"Current page number,the first page starts from 0,default 0 ", "zh_CN":"分页，当前页，第一页从0开始，默认0"}
        self.page_no = page_no
        # {"en":"Page size,must be greater than 0,default 100 ", "zh_CN":"每页大小，必须大于0，默认100"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.label_code_list, 'label_code_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_code_list is not None:
            result['labelCodeList'] = self.label_code_list
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCodeList') is not None:
            self.label_code_list = m.get('labelCodeList')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryDetailData(TeaModel):
    def __init__(
        self,
        label_code: str = None,
        label_name: str = None,
        ip: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        # {"en":"Label Code", "zh_CN":"标签编码"}
        self.label_code = label_code
        # {"en":"Label Name", "zh_CN":"标签名称"}
        self.label_name = label_name
        # {"en":"IP forbidding", "zh_CN":"封禁的IP"}
        self.ip = ip
        # {"en":"Start time of forbidden", "zh_CN":"封禁开始时间"}
        self.start_time = start_time
        # {"en":"End time of forbidden", "zh_CN":"封禁结束时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.label_code, 'label_code')
        self.validate_required(self.label_name, 'label_name')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_code is not None:
            result['labelCode'] = self.label_code
        if self.label_name is not None:
            result['labelName'] = self.label_name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCode') is not None:
            self.label_code = m.get('labelCode')
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryResponseData(TeaModel):
    def __init__(
        self,
        total: int = None,
        page_no: int = None,
        page_size: int = None,
        result: List[QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryDetailData] = None,
    ):
        # {"en":"Total count ", "zh_CN":"总数据条数"}
        self.total = total
        # {"en":"Current page number,the first page starts from 0,default 0 ", "zh_CN":"分页，当前页，第一页从0开始，默认0"}
        self.page_no = page_no
        # {"en":"Page size,must be greater than 0,default 100 ", "zh_CN":"每页大小，必须大于0，默认100"}
        self.page_size = page_size
        # {"en":"Query results", "zh_CN":"查询结果"}
        self.result = result

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
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
        if self.total is not None:
            result['total'] = self.total
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result is not None:
            result['result'] = []
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('result') is not None:
            self.result = []
            for k in m.get('result'):
                temp_model = QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryDetailData()
                self.result.append(temp_model.from_map(k))
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryResponseData = None,
    ):
        # {"en":"Result Code", "zh_CN":"响应码"}
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
            temp_model = QueryForbiddingVisitorIPsByLabelCodeServiceLabelIpQueryResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryForbiddingVisitorIPsByLabelCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByLabelCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ForbidOrResumeVisitorIPsByLabelCodeServiceOperationObject(TeaModel):
    def __init__(
        self,
        label_code: str = None,
        ip_list: List[str] = None,
    ):
        # {"en":"Label Code (Please contact technical support for assistance)", "zh_CN":"标签编码（请联系专属技术支持获取）"}
        self.label_code = label_code
        # {"en":"List of IPs to forbid or resume. The maximum number of IPs is 10,000. The IP address can be v4 or v6,only supports IPV4 segment, does not support IPV6 segment.", "zh_CN":"待封禁或解禁的IP列表。IP个数上限为10000个。支持IPV4、IPV6格式，仅支持IPV4段，不支持IPV6段"}
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.label_code, 'label_code')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_code is not None:
            result['labelCode'] = self.label_code
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCode') is not None:
            self.label_code = m.get('labelCode')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceRequest(TeaModel):
    def __init__(
        self,
        operation_object_list: List[ForbidOrResumeVisitorIPsByLabelCodeServiceOperationObject] = None,
        operation_type: int = None,
        forbid_time: int = None,
    ):
        # {"en":"List of operating objects ", "zh_CN":"操作对象列表"}
        self.operation_object_list = operation_object_list
        # {"en":"Operation Type, 1: forbid; 2: resume ", "zh_CN":"操作类型， 1: 封禁； 2: 解禁 "}
        self.operation_type = operation_type
        # {"en":"Forbid Duration(minutes),The maximum value is 2628000 minutes(five years), and it will automatically be set to 2628000 if exceeded. Required for forbidding operation, non-required for resuming operation.", "zh_CN":"封禁时长（分钟），最大值为2628000分钟（即五年），超过自动设置为2628000。封禁操作时，必填，解禁时非必填。"}
        self.forbid_time = forbid_time

    def validate(self):
        self.validate_required(self.operation_object_list, 'operation_object_list')
        if self.operation_object_list:
            for k in self.operation_object_list:
                if k:
                    k.validate()
        self.validate_required(self.operation_type, 'operation_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_object_list is not None:
            result['operationObjectList'] = []
            for k in self.operation_object_list:
                result['operationObjectList'].append(k.to_map() if k else None)
        if self.operation_type is not None:
            result['operationType'] = self.operation_type
        if self.forbid_time is not None:
            result['forbidTime'] = self.forbid_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationObjectList') is not None:
            self.operation_object_list = []
            for k in m.get('operationObjectList'):
                temp_model = ForbidOrResumeVisitorIPsByLabelCodeServiceOperationObject()
                self.operation_object_list.append(temp_model.from_map(k))
        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')
        if m.get('forbidTime') is not None:
            self.forbid_time = m.get('forbidTime')
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceForbidIpOperateResponseData(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        label_code: str = None,
        failed_ip_list: List[str] = None,
    ):
        # {"en":" Error Code", "zh_CN":"业务错误码"}
        self.err_code = err_code
        # {"en":"Error Message", "zh_CN":"业务错误信息"}
        self.err_message = err_message
        # {"en":"Label Code", "zh_CN":"标签编码"}
        self.label_code = label_code
        # {"en":"List of Failed IPs", "zh_CN":"失败的IP列表"}
        self.failed_ip_list = failed_ip_list

    def validate(self):
        self.validate_required(self.err_code, 'err_code')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.label_code, 'label_code')
        self.validate_required(self.failed_ip_list, 'failed_ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.label_code is not None:
            result['labelCode'] = self.label_code
        if self.failed_ip_list is not None:
            result['failedIpList'] = self.failed_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('labelCode') is not None:
            self.label_code = m.get('labelCode')
        if m.get('failedIpList') is not None:
            self.failed_ip_list = m.get('failedIpList')
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: ForbidOrResumeVisitorIPsByLabelCodeServiceForbidIpOperateResponseData = None,
    ):
        # {"en":"Result Code.If it shows `PartialSuccess`, please pay attention to the details of partial failures in errCode ", "zh_CN":"响应码，如果为“PartialSuccess”，请关注errCode中部分失败的详情"}
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
            temp_model = ForbidOrResumeVisitorIPsByLabelCodeServiceForbidIpOperateResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByLabelCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ForbidOrResumeVisitorIPsByDomainServiceRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        ip_list: List[str] = None,
        operation_type: int = None,
        forbid_time: int = None,
    ):
        # {"en":"List of Domains", "zh_CN":"域名列表"}
        self.domain_list = domain_list
        # {"en":"List of IPs to forbid or resume.The IP address can be v4 or v6,only supports IPV4 segment, does not support IPV6 segment.", "zh_CN":"待封禁或解禁的IP列表。支持IPV4、IPV6格式，仅支持IPV4段，不支持IPV6段"}
        self.ip_list = ip_list
        # {"en":"Operate Type(1: forbid; 2: resume;)", "zh_CN":"操作类型(1: 封禁； 2: 解禁；)"}
        self.operation_type = operation_type
        # {"en":"Forbid duration(minute), default 43200(means 30 days),max 2628000(means 5 years),it is recommended to specify a number,such as 30", "zh_CN":"封禁时长（分钟），不传默认为43200（30天），最大支持2628000（5年），建议指定具体的数值，比如 30"}
        self.forbid_time = forbid_time

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')
        self.validate_required(self.ip_list, 'ip_list')
        self.validate_required(self.operation_type, 'operation_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.operation_type is not None:
            result['operationType'] = self.operation_type
        if self.forbid_time is not None:
            result['forbidTime'] = self.forbid_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')
        if m.get('forbidTime') is not None:
            self.forbid_time = m.get('forbidTime')
        return self


class ForbidOrResumeVisitorIPsByDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[str] = None,
        err_code: str = None,
        err_message: str = None,
        domain: str = None,
        failed_ip_list: List[str] = None,
    ):
        # {"en":"Result Code.If it shows `36010032`,means `partial success`, please pay attention to the details of partial failures in errCode, adjust and try again", "zh_CN":"响应码，如果为“36010032”，意味着部分成功，请关注errCode中部分失败的详情"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result Data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Error Code", "zh_CN":"业务错误码"}
        self.err_code = err_code
        # {"en":"Error Message", "zh_CN":"业务错误信息"}
        self.err_message = err_message
        # {"en":"Failed Domain", "zh_CN":"失败的域名"}
        self.domain = domain
        # {"en":"List of Failed IPs", "zh_CN":"失败的IP列表"}
        self.failed_ip_list = failed_ip_list

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.err_code, 'err_code')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.failed_ip_list, 'failed_ip_list')

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
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.domain is not None:
            result['domain'] = self.domain
        if self.failed_ip_list is not None:
            result['failedIpList'] = self.failed_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('failedIpList') is not None:
            self.failed_ip_list = m.get('failedIpList')
        return self


class ForbidOrResumeVisitorIPsByDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidOrResumeVisitorIPsByDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportServerIpCountryCodeServiceRequest(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        country_code: List[str] = None,
    ):
        # {'en':'Domain name:
        # 1.The maximum number of transferable domain names is 50 ;
        # 2.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)', 'zh_CN':'域名：
        # 1.可传递域名数量上限为50个；
        # 2.自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。'}
        self.domain = domain
        # {'en':'countryCode
        # 
        # 1Up to 10 States consulted on a one-time basis;
        # 2.Transitive values:
        # 
        # ae:Arab Emirates
        # 
        # ar:Argentina
        # 
        # at:Austria
        # 
        # au:Australia
        # 
        # bd:Bangladesh
        # 
        # be:Belgium
        # 
        # bnBrunei
        # 
        # br:Brazil
        # 
        # by:Belarus
        # 
        # ca:Canada
        # 
        # ch:Switzerland
        # 
        # cl:Chile
        # 
        # cn:China
        # 
        # co:Colombia
        # 
        # cz:Czech-Republic
        # 
        # de:Germany
        # 
        # dk:Denmark
        # 
        # dz:Algeria
        # 
        # eg:Egypt
        # 
        # es:Spain
        # 
        # fi:Finland
        # 
        # fr:France
        # 
        # gb:UK
        # 
        # gr:Greece
        # 
        # hk:Hong Kong
        # 
        # hu:Hungary
        # 
        # id:Indonesia
        # 
        # ie:Ireland
        # 
        # il:Israel
        # 
        # in:India
        # 
        # iq:Iraq
        # 
        # ir:Iran
        # 
        # it:Italy
        # 
        # jp:Japan
        # 
        # ke:Kenya
        # 
        # kg:Kyrgyzstan
        # 
        # kh:Cambodia
        # 
        # kr:South Korea
        # 
        # kw:Kuwait
        # 
        # kz:Kazakhstan
        # 
        # la:Laos
        # 
        # lt:Lithuania
        # 
        # ma:Morocco
        # 
        # mm:Myanmar
        # 
        # mn:Mongolia
        # 
        # mo:Macau
        # 
        # mx:Mexico
        # 
        # my:Malaysia
        # 
        # ng:Nigeria
        # 
        # nl:Netherlands
        # 
        # no:Norway
        # 
        # np:Nepal
        # 
        # nz:New Zealand
        # 
        # pe:Peru
        # 
        # ph:Philippines
        # 
        # pk:Pakistan
        # 
        # pl:Poland
        # 
        # pt:Portugal
        # 
        # qa:Qatar
        # 
        # ro:Romania
        # 
        # rs:Serbia
        # 
        # ru:Russian Federation
        # 
        # sa:Saudia Arabia
        # 
        # se:Sweden
        # 
        # sg:Singapore
        # 
        # sk:Slovak-Republic
        # 
        # th:Thailand
        # 
        # tr:Turkey
        # 
        # tw:Taiwan
        # 
        # tz:Tanzania
        # 
        # ua:Ukraine
        # 
        # us:USA
        # 
        # uy:Uruguay
        # 
        # uz:Uzbekistan
        # 
        # ve:Venezuela
        # 
        # vn:Vietnam
        # 
        # za:South Africa', 'zh_CN':'国家地区代号：
        # 1.单次最多查询 10 个国家；
        # 2.可传递的值：
        # 
        # ae：阿联酋
        # 
        # ar：阿根廷
        # 
        # at：奥地利
        # 
        # au：澳大利亚
        # 
        # bd：孟加拉
        # 
        # be：比利时
        # 
        # bn：文莱
        # 
        # br：巴西
        # 
        # by：白俄罗斯
        # 
        # ca：加拿大
        # 
        # ch：瑞士
        # 
        # cl：智利
        # 
        # cn：中国大陆
        # 
        # co：哥伦比亚
        # 
        # cz：捷克
        # 
        # de：德国
        # 
        # dk：丹麦
        # 
        # dz：阿尔及利亚
        # 
        # eg：埃及
        # 
        # es：西班牙
        # 
        # fi：芬兰
        # 
        # fr：法国
        # 
        # gb：英国
        # 
        # gr：希腊
        # 
        # hk：香港
        # 
        # hu：匈牙利
        # 
        # id：印度尼西亚
        # 
        # ie：爱尔兰
        # 
        # il：以色列
        # 
        # in：印度
        # 
        # iq：伊拉克
        # 
        # ir：伊朗
        # 
        # it：意大利
        # 
        # jp：日本
        # 
        # ke：肯尼亚
        # 
        # kg：吉尔吉斯斯坦
        # 
        # kh：柬埔寨
        # 
        # kr：韩国
        # 
        # kw：科威特
        # 
        # kz：哈萨克斯坦
        # 
        # la：老挝
        # 
        # lt：立陶宛
        # 
        # ma：摩洛哥
        # 
        # mm：缅甸
        # 
        # mn：蒙古
        # 
        # mo：澳门
        # 
        # mx：墨西哥
        # 
        # my：马来西亚
        # 
        # ng：尼日利亚
        # 
        # nl：荷兰
        # 
        # no：挪威
        # 
        # np：尼泊尔
        # 
        # nz：新西兰
        # 
        # pe：秘鲁
        # 
        # ph：菲律宾
        # 
        # pk：巴基斯坦
        # 
        # pl：波兰
        # 
        # pt：葡萄牙
        # 
        # qa：卡塔尔
        # 
        # ro：罗马尼亚
        # 
        # rs：塞尔维亚
        # 
        # ru：俄罗斯
        # 
        # sa：沙特阿拉伯
        # 
        # se：瑞典
        # 
        # sg：新加坡
        # 
        # sk：斯洛伐克
        # 
        # th：泰国
        # 
        # tr：土耳其
        # 
        # tw：台湾
        # 
        # tz：坦桑尼亚
        # 
        # ua：乌克兰
        # 
        # us：美国
        # 
        # uy：乌拉圭
        # 
        # uz：乌兹别克斯坦
        # 
        # ve：委内瑞拉
        # 
        # vn：越南
        # 
        # za：南非'}
        self.country_code = country_code

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.country_code, 'country_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.country_code is not None:
            result['countryCode'] = self.country_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('countryCode') is not None:
            self.country_code = m.get('countryCode')
        return self


class ReportServerIpCountryCodeServiceResponseDataCountryData(TeaModel):
    def __init__(
        self,
        country_name_zh: str = None,
        country_name_en: str = None,
        server_ip: List[str] = None,
    ):
        # {'en':'Chinese country name', 'zh_CN':'中文国家名'}
        self.country_name_zh = country_name_zh
        # {'en':'English country name', 'zh_CN':'英文国家名'}
        self.country_name_en = country_name_en
        # {'en':'server IP list', 'zh_CN':'覆盖节点IP列表'}
        self.server_ip = server_ip

    def validate(self):
        self.validate_required(self.country_name_zh, 'country_name_zh')
        self.validate_required(self.country_name_en, 'country_name_en')
        self.validate_required(self.server_ip, 'server_ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_name_zh is not None:
            result['countryNameZH'] = self.country_name_zh
        if self.country_name_en is not None:
            result['countryNameEN'] = self.country_name_en
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryNameZH') is not None:
            self.country_name_zh = m.get('countryNameZH')
        if m.get('countryNameEN') is not None:
            self.country_name_en = m.get('countryNameEN')
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        return self


class ReportServerIpCountryCodeServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        country_data: List[ReportServerIpCountryCodeServiceResponseDataCountryData] = None,
    ):
        # {'en':'domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'Detailed data on the results of the request', 'zh_CN':'请求结果的详细数据'}
        self.country_data = country_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.country_data, 'country_data')
        if self.country_data:
            for k in self.country_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.country_data is not None:
            result['countryData'] = []
            for k in self.country_data:
                result['countryData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('countryData') is not None:
            self.country_data = []
            for k in m.get('countryData'):
                temp_model = ReportServerIpCountryCodeServiceResponseDataCountryData()
                self.country_data.append(temp_model.from_map(k))
        return self


class ReportServerIpCountryCodeServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportServerIpCountryCodeServiceResponseData] = None,
    ):
        # {'en':'request result status code', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'Request result information', 'zh_CN':'请求结果信息'}
        self.message = message
        # {'en':'domain', 'zh_CN':'-'}
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
                temp_model = ReportServerIpCountryCodeServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportServerIpCountryCodeServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpCountryCodeServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpCountryCodeServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpCountryCodeServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class IpDomainServiceRequest(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        # {"en":"IP", "zh_CN":"IP"}
        self.ip = ip

    def validate(self):
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class IpDomainServiceResponseData(TeaModel):
    def __init__(
        self,
        ip: str = None,
        status: str = None,
        domain_list: List[str] = None,
    ):
        # {"en":"ip", "zh_CN":"IP名称"}
        self.ip = ip
        # {"en":"Whether to use:
        # 
        #   idle --IP not used yet;
        #   runing -- IP in use;
        #   out of range -- IP is not in a queryable range", "zh_CN":"是否使用:
        #   idle -- 暂未使用;
        #   runing -- 使用中;
        #   out of range -- 不在查询范围内的ip"}
        self.status = status
        # {"en":"List of domain using this IP.The domain list of the IP that was idle or out of range was empty", "zh_CN":"用该IP的域名列表,未使用的ip/不在查询范围内的ip,域名列表为空"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.status, 'status')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class IpDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[IpDomainServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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
                temp_model = IpDomainServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class IpDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AkamaiIpPermitServiceRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        client_secret: str = None,
        client_token: str = None,
        host: str = None,
        network_list_id: str = None,
        ip: str = None,
    ):
        # {"en":"accessToken", "zh_CN":"accessToken"}
        self.access_token = access_token
        # {"en":"clientSecret", "zh_CN":"clientSecret"}
        self.client_secret = client_secret
        # {"en":"clientToken", "zh_CN":"clientToken"}
        self.client_token = client_token
        # {"en":"host", "zh_CN":"host"}
        self.host = host
        # {"en":"Unique identifier for each network list.", "zh_CN":"每个网络列表的唯一标识符。"}
        self.network_list_id = network_list_id
        # {"en":"Support single IP, Support IP segment, example 8.7.6.0/24", "zh_CN":"支持单个ip, 支持IP段, 示例8.7.6.0/24"}
        self.ip = ip

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        self.validate_required(self.client_secret, 'client_secret')
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.host, 'host')
        self.validate_required(self.network_list_id, 'network_list_id')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.host is not None:
            result['host'] = self.host
        if self.network_list_id is not None:
            result['networkListId'] = self.network_list_id
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('networkListId') is not None:
            self.network_list_id = m.get('networkListId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class AkamaiIpPermitServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[str] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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


class AkamaiIpPermitServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpPermitServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpPermitServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpPermitServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AkamaiIpForbiddenServiceRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        client_secret: str = None,
        client_token: str = None,
        host: str = None,
        network_list_id: str = None,
        ip: List[str] = None,
        email: List[str] = None,
    ):
        # {"en":"accessToken", "zh_CN":"accessToken"}
        self.access_token = access_token
        # {"en":"clientSecret", "zh_CN":"clientSecret"}
        self.client_secret = client_secret
        # {"en":"clientToken", "zh_CN":"clientToken"}
        self.client_token = client_token
        # {"en":"host", "zh_CN":"host"}
        self.host = host
        # {"en":"Unique identifier for each network list.", "zh_CN":"每个网络列表的唯一标识符。"}
        self.network_list_id = network_list_id
        # {"en":"1.The number of IP addresses to block is adjustable according to the account number.The default is 10000;
        # 2.Support IP segment, example 8.7.6.0/24", "zh_CN":"1. 要封禁IP地址，IP个数限制根据账号可调，默认为10000个
        # 2.支持IP段，示例 8.7.6.0/24"}
        self.ip = ip
        # {"en":"Mail receiver activated networkListId status after blocking successfully", "zh_CN":"封禁成功后激活networkListId 状态的邮件接收人"}
        self.email = email

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        self.validate_required(self.client_secret, 'client_secret')
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.host, 'host')
        self.validate_required(self.network_list_id, 'network_list_id')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.host is not None:
            result['host'] = self.host
        if self.network_list_id is not None:
            result['networkListId'] = self.network_list_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.email is not None:
            result['email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('networkListId') is not None:
            self.network_list_id = m.get('networkListId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('email') is not None:
            self.email = m.get('email')
        return self


class AkamaiIpForbiddenServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[str] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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


class AkamaiIpForbiddenServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpForbiddenServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpForbiddenServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AkamaiIpForbiddenServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryForbiddingVisitorIPsByDomainServiceRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        ip_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # {"en":"List of forbidding domain", "zh_CN":"封禁域名列表"}
        self.domain_list = domain_list
        # {"en":"List of forbidding IP", "zh_CN":"封禁IP列表"}
        self.ip_list = ip_list
        # {"en":"Current page number,the first page starts from 0,default 0", "zh_CN":"分页，当前页，第一页从0开始，默认0"}
        self.page_no = page_no
        # {"en":"Page size,must be greater than 0,default 100, the maximum is 1000 ", "zh_CN":"每页大小，必须大于0，默认100，最大1000"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryForbiddingVisitorIPsByDomainServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: dict = None,
        total: int = None,
        page_no: int = None,
        page_size: int = None,
        result: List[str] = None,
        domain: str = None,
        ip: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        # {"en":"Result Code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result Data", "zh_CN":"响应数据"}
        self.data = data
        # {"en":"Total count", "zh_CN":"总数据条数"}
        self.total = total
        # {"en":"Current page number,the first page starts from 0,default 0", "zh_CN":"分页，当前页，第一页从0开始，默认0"}
        self.page_no = page_no
        # {"en":"Page size,must be greater than 0,default 100, the maximum is 1000", "zh_CN":"每页大小，必须大于0，默认100，最大1000"}
        self.page_size = page_size
        # {"en":"Query results", "zh_CN":"查询结果"}
        self.result = result
        # {"en":"Domain forbidding", "zh_CN":"封禁的域名"}
        self.domain = domain
        # {"en":"IP forbidding", "zh_CN":"封禁的IP"}
        self.ip = ip
        # {"en":"Start time of forbidden", "zh_CN":"封禁开始时间"}
        self.start_time = start_time
        # {"en":"End time of forbidden", "zh_CN":"封禁结束时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.result, 'result')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.total is not None:
            result['total'] = self.total
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result is not None:
            result['result'] = self.result
        if self.domain is not None:
            result['domain'] = self.domain
        if self.ip is not None:
            result['ip'] = self.ip
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class QueryForbiddingVisitorIPsByDomainServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByDomainServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByDomainServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingVisitorIPsByDomainServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryForbiddingIPWhitelistServiceRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        label_code_list: List[str] = None,
        ip_list: List[str] = None,
        whitelist_types: List[str] = None,
        page_size: int = None,
        page_no: int = None,
    ):
        # {"en":"List of Domains, leave it empty to query all ", "zh_CN":"域名列表，为空时查全部 "}
        self.domain_list = domain_list
        # {"en":"List of Label Code, leave it empty to query all ", "zh_CN":"标签列表，为空时查全部 "}
        self.label_code_list = label_code_list
        # {"en":"List of Whitelist IPs, leave it empty to query all ", "zh_CN":"IP列表，为空时查全部 "}
        self.ip_list = ip_list
        # {"en":"List of Whitelist Types, 0:'Customer Granularity', 1:'Domain Granularity', 2:'Label Granularity', leave it empty to query all ", "zh_CN":"白名单类型列表，0:客户粒度，1:域名粒度，2:标签粒度，为空时查全部 "}
        self.whitelist_types = whitelist_types
        # {"en":"Page size,must be greater than 0,default 100 ", "zh_CN":"每页大小，必须大于0，默认100 "}
        self.page_size = page_size
        # {"en":"Current page number,the first page starts from 0,default 0  ", "zh_CN":"分页，当前页，第一页从0开始，默认0 "}
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        if self.label_code_list is not None:
            result['labelCodeList'] = self.label_code_list
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.whitelist_types is not None:
            result['whitelistTypes'] = self.whitelist_types
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        if m.get('labelCodeList') is not None:
            self.label_code_list = m.get('labelCodeList')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('whitelistTypes') is not None:
            self.whitelist_types = m.get('whitelistTypes')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        return self


class QueryForbiddingIPWhitelistServiceIpWhitelist(TeaModel):
    def __init__(
        self,
        whitelist_type: str = None,
        whitelist_object: str = None,
        ip: str = None,
    ):
        # {"en":"Whitelist Type, 0:'Customer Granularity', 1:'Domain Granularity', 2:'Label Granularity' ", "zh_CN":"白名单类型，0:客户粒度，1:域名粒度，2:标签粒度 "}
        self.whitelist_type = whitelist_type
        # {"en":"Whitelist Object, must be CustomerCode or Domain or Label Code,It depends on the `Whitelist Type` ", "zh_CN":"白名单对象，客户编码或加速域名或标签编码，取决于白名单类型 "}
        self.whitelist_object = whitelist_object
        # {"en":"Whitelist IP", "zh_CN":"白名单IP"}
        self.ip = ip

    def validate(self):
        self.validate_required(self.whitelist_type, 'whitelist_type')
        self.validate_required(self.whitelist_object, 'whitelist_object')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.whitelist_type is not None:
            result['whitelistType'] = self.whitelist_type
        if self.whitelist_object is not None:
            result['whitelistObject'] = self.whitelist_object
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('whitelistType') is not None:
            self.whitelist_type = m.get('whitelistType')
        if m.get('whitelistObject') is not None:
            self.whitelist_object = m.get('whitelistObject')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class QueryForbiddingIPWhitelistServiceData(TeaModel):
    def __init__(
        self,
        total: int = None,
        page_size: int = None,
        page_no: int = None,
        results: List[QueryForbiddingIPWhitelistServiceIpWhitelist] = None,
    ):
        # {"en":"Total count", "zh_CN":"总数据条数"}
        self.total = total
        # {"en":"Page size,must be greater than 0,default 100", "zh_CN":"每页大小，必须大于0，默认100"}
        self.page_size = page_size
        # {"en":"Current page number,the first page starts from 0,default 0 ", "zh_CN":"分页，当前页，第一页从0开始，默认0 "}
        self.page_no = page_no
        # {"en":"Query results", "zh_CN":"查询结果"}
        self.results = results

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.results is not None:
            result['results'] = []
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('results') is not None:
            self.results = []
            for k in m.get('results'):
                temp_model = QueryForbiddingIPWhitelistServiceIpWhitelist()
                self.results.append(temp_model.from_map(k))
        return self


class QueryForbiddingIPWhitelistServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryForbiddingIPWhitelistServiceData = None,
    ):
        # {"en":"Result Code", "zh_CN":"响应码，成功为0"}
        self.code = code
        # {"en":"Result Message", "zh_CN":"响应信息"}
        self.message = message
        # {"en":"Result QueryForbiddingIPWhitelistServiceData", "zh_CN":"响应数据"}
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
            temp_model = QueryForbiddingIPWhitelistServiceData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryForbiddingIPWhitelistServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingIPWhitelistServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingIPWhitelistServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbiddingIPWhitelistServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryAllBandwidthLimitTaskListServiceRequest(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        ignore_task_status: str = None,
        contain_domain: str = None,
    ):
        # {"en":"Domain:
        # 1. The maximum number of domain is 100 by default (you can contact technical support for adjustment);
        # 2. Automatically filter out invalid domain (an illegal domain will be filtered, and the query result will only return the data of valid domains).", "zh_CN":"域名:
        # 1.可传递域名数量上限默认为100个(可联系技术支持调整);
        # 2.自动过滤掉无效域名(如传递非法域名,会被过滤,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"Whether to ignore task status.
        # 0: No, only return the configuration whose task status is enabled; default: 0;
        # 1: Yes, return whether the task status is open or closed.", "zh_CN":"是否忽略任务状态。0:否,只返回任务状态为开启的配置;默认:0; 1:是,不论任务状态是开启还是关闭都返回。"}
        self.ignore_task_status = ignore_task_status
        # {"en":"Whether the returned data contains all customer domain names involved in the task, the default is 0;
        # 0: no;
        # 1: Yes.", "zh_CN":"返回数据是否包含任务涉及的所有客户域名。0:否;默认:0;1:是。"}
        self.contain_domain = contain_domain

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.ignore_task_status is not None:
            result['ignoreTaskStatus'] = self.ignore_task_status
        if self.contain_domain is not None:
            result['containDomain'] = self.contain_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ignoreTaskStatus') is not None:
            self.ignore_task_status = m.get('ignoreTaskStatus')
        if m.get('containDomain') is not None:
            self.contain_domain = m.get('containDomain')
        return self


class QueryAllBandwidthLimitTaskListServiceResponseDataContent(TeaModel):
    def __init__(
        self,
        task_name: str = None,
        task_type: str = None,
        task_status: str = None,
        ctrl_mode: str = None,
        ctrl_value: str = None,
        domain_list: List[str] = None,
    ):
        # {"en":"taskName", "zh_CN":"任务名称"}
        self.task_name = task_name
        # {"en":"Domain name configuration task types: 1. Static bandwidth control task, 2. Bandwidth buyout task, 3. Flow buyout task, 4. Request number buyout task, 5. Redundant pool speed limit task, 6. Back-to-source task, 7. POP running high scheduling task (this kind of task is quite special, the domain name is a global quantity, so as long as there is configuration, it will be enabled by default), 8. IP ban task", "zh_CN":"域名配置的任务类型:1静态带宽控制任务,2带宽买断任务,3流量买断任务,4请求数买断任务,5冗余池限速任务,6回源任务,7POP跑高调度任务(此种任务比较特殊,域名为全局量,所以只要有配置,就默认开启),8IP封禁任务"}
        self.task_type = task_type
        # {"en":"Task status, 0: task is off, 1: task is on.", "zh_CN":"任务状态,0表示任务关闭,1表示任务开启。"}
        self.task_status = task_status
        # {"en":"Control strategy. 0 means squid default, 1 rejects, 2 when taskType=8, is ladder blocked, the rest is redirected ip, 3 when taskType=6, is backup source, the rest is speed limit = rejection + maximum download rate, 4 speed limit = rejection + timeout to disconnect, 5 does not process, controls each connection at minimum speed, does not process the excess part, 6 backups, 7 redirects domain name, 8 redirects URL", "zh_CN":"控制策略。0表示squid默认,1拒绝,2当taskType=8时,为阶梯封禁,其余为重定向ip,3当taskType=6时,为主备回源,其余为限速=拒绝+最大下载速率,4限速=拒绝+超时断开连接,5不处理,按最小速率控制每个连接,超出部分不处理,6回源,7重定向域名,8重定向URL"}
        self.ctrl_mode = ctrl_mode
        # {"en":"Bandwidth limit value, when taskType=1,2,5,6, in Mbps, when taskType=3, in G, when taskType=4, in MH (millions), when taskType=7, in -1, there is no bandwidth limit value, when taskType=8, in seconds.", "zh_CN":"带宽限制值,当taskType=1,2,5,6时,单位为Mbps,当taskType=3,单位为G,当taskType=4,单位为MH(百万个),当taskType=7,为-1,表示没有带宽限制值,当taskType=8,单位为次。"}
        self.ctrl_value = ctrl_value
        # {"en":"List of customer domains involved under the task. Values are only available when entering ContainOrichannelName=1.", "zh_CN":"任务下涉及的客户域名列表。只有在入参containOrichannelName=1的时候有值。"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.task_name, 'task_name')
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.task_status, 'task_status')
        self.validate_required(self.ctrl_mode, 'ctrl_mode')
        self.validate_required(self.ctrl_value, 'ctrl_value')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_name is not None:
            result['taskName'] = self.task_name
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.ctrl_mode is not None:
            result['ctrlMode'] = self.ctrl_mode
        if self.ctrl_value is not None:
            result['ctrlValue'] = self.ctrl_value
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('ctrlMode') is not None:
            self.ctrl_mode = m.get('ctrlMode')
        if m.get('ctrlValue') is not None:
            self.ctrl_value = m.get('ctrlValue')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class QueryAllBandwidthLimitTaskListServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        is_exist: str = None,
        content: List[QueryAllBandwidthLimitTaskListServiceResponseDataContent] = None,
    ):
        # {"en":"domain", "zh_CN":"客户域名"}
        self.domain = domain
        # {"en":"Whether there is a configuration control task, 0: no, 1: yes", "zh_CN":"是否有配置控制任务,0表示没有,1表示有"}
        self.is_exist = is_exist
        self.content = content

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.is_exist, 'is_exist')
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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.is_exist is not None:
            result['isExist'] = self.is_exist
        if self.content is not None:
            result['content'] = []
            for k in self.content:
                result['content'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('isExist') is not None:
            self.is_exist = m.get('isExist')
        if m.get('content') is not None:
            self.content = []
            for k in m.get('content'):
                temp_model = QueryAllBandwidthLimitTaskListServiceResponseDataContent()
                self.content.append(temp_model.from_map(k))
        return self


class QueryAllBandwidthLimitTaskListServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[QueryAllBandwidthLimitTaskListServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
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
                temp_model = QueryAllBandwidthLimitTaskListServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAllBandwidthLimitTaskListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAllBandwidthLimitTaskListServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAllBandwidthLimitTaskListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryAllBandwidthLimitTaskListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectList(TeaModel):
    def __init__(
        self,
        whitelist_object: str = None,
        ip_list: List[str] = None,
    ):
        # {"en":"Whitelist Object,must be Domain or Label Code.When the whitelist type is `customer granularity`, this field must be empty ", "zh_CN":"白名单操作对象，白名单类型“域名粒度”时，请填写加速域名，白名单类型“标签粒度”时，请填写标签编码，白名单类型为“客户粒度”时，此值必须为空 "}
        self.whitelist_object = whitelist_object
        # {"en":"List of Whitelist IPs ", "zh_CN":"白名单IP列表"}
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.whitelist_object is not None:
            result['whitelistObject'] = self.whitelist_object
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('whitelistObject') is not None:
            self.whitelist_object = m.get('whitelistObject')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self


class AddOrRemoveForbiddingIPWhitelistServiceRequest(TeaModel):
    def __init__(
        self,
        whitelist_object_list: List[AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectList] = None,
        operation_type: str = None,
        whitelist_type: str = None,
        force_resume: bool = None,
    ):
        # {"en":"Whitelist Objects", "zh_CN":"白名单操作对象列表 "}
        self.whitelist_object_list = whitelist_object_list
        # {"en":"Operation Type, 1:add, 2:remove ", "zh_CN":"操作类型，1:新增，2:删除 "}
        self.operation_type = operation_type
        # {"en":"Whitelist Type, 0:'Customer Granularity', 1:'Domain Granularity', 2:'Label Granularity' ", "zh_CN":"白名单类型，0:客户粒度，1:域名粒度，2:标签粒度 "}
        self.whitelist_type = whitelist_type
        # {"en":"Force resume,default 'false'. When adding, simultaneously resume IPs that are still forbidding at the corresponding granularity ", "zh_CN":"是否强制解禁，默认否。添加时，同时解禁对应粒度下还处于封禁中的IP。"}
        self.force_resume = force_resume

    def validate(self):
        self.validate_required(self.whitelist_object_list, 'whitelist_object_list')
        if self.whitelist_object_list:
            for k in self.whitelist_object_list:
                if k:
                    k.validate()
        self.validate_required(self.operation_type, 'operation_type')
        self.validate_required(self.whitelist_type, 'whitelist_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.whitelist_object_list is not None:
            result['whitelistObjectList'] = []
            for k in self.whitelist_object_list:
                result['whitelistObjectList'].append(k.to_map() if k else None)
        if self.operation_type is not None:
            result['operationType'] = self.operation_type
        if self.whitelist_type is not None:
            result['whitelistType'] = self.whitelist_type
        if self.force_resume is not None:
            result['forceResume'] = self.force_resume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('whitelistObjectList') is not None:
            self.whitelist_object_list = []
            for k in m.get('whitelistObjectList'):
                temp_model = AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectList()
                self.whitelist_object_list.append(temp_model.from_map(k))
        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')
        if m.get('whitelistType') is not None:
            self.whitelist_type = m.get('whitelistType')
        if m.get('forceResume') is not None:
            self.force_resume = m.get('forceResume')
        return self


class AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectOperateResult(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        whitelist_object: str = None,
        whitelist_type: str = None,
        failed_ip_list: List[str] = None,
    ):
        # {"en":"Error Code", "zh_CN":"业务错误码"}
        self.err_code = err_code
        # {"en":"Error Message", "zh_CN":"业务错误信息"}
        self.err_message = err_message
        # {"en":"Whitelist Object", "zh_CN":"白名单操作对象"}
        self.whitelist_object = whitelist_object
        # {"en":"Whitelist Type, 0:'Customer Granularity', 1:'Domain Granularity', 2:'Label Granularity' ", "zh_CN":"白名单类型，0:客户粒度，1:域名粒度，2:标签粒度 "}
        self.whitelist_type = whitelist_type
        # {"en":"List of Failed IPs", "zh_CN":"失败的IP列表"}
        self.failed_ip_list = failed_ip_list

    def validate(self):
        self.validate_required(self.err_code, 'err_code')
        self.validate_required(self.err_message, 'err_message')
        self.validate_required(self.whitelist_object, 'whitelist_object')
        self.validate_required(self.whitelist_type, 'whitelist_type')
        self.validate_required(self.failed_ip_list, 'failed_ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.whitelist_object is not None:
            result['whitelistObject'] = self.whitelist_object
        if self.whitelist_type is not None:
            result['whitelistType'] = self.whitelist_type
        if self.failed_ip_list is not None:
            result['failedIpList'] = self.failed_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('whitelistObject') is not None:
            self.whitelist_object = m.get('whitelistObject')
        if m.get('whitelistType') is not None:
            self.whitelist_type = m.get('whitelistType')
        if m.get('failedIpList') is not None:
            self.failed_ip_list = m.get('failedIpList')
        return self


class AddOrRemoveForbiddingIPWhitelistServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectOperateResult] = None,
    ):
        # {"en":"Result Code.If it shows `36010032`,means `partial success`, please pay attention to the details of partial failures in errCode.", "zh_CN":"响应码，成功为0，如果为“36010032”部分成功，请关注errCode中部分失败的详情 "}
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
                temp_model = AddOrRemoveForbiddingIPWhitelistServiceWhitelistObjectOperateResult()
                self.data.append(temp_model.from_map(k))
        return self


class AddOrRemoveForbiddingIPWhitelistServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddOrRemoveForbiddingIPWhitelistServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddOrRemoveForbiddingIPWhitelistServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddOrRemoveForbiddingIPWhitelistServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




