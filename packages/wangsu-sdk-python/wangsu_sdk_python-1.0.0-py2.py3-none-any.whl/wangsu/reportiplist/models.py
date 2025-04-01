# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryCdnIpListDomainList(TeaModel):
    def __init__(
        self,
        domain_name: List[str] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
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


class QueryCdnIpListRequest(TeaModel):
    def __init__(
        self,
        domain_list: QueryCdnIpListDomainList = None,
    ):
        # {"en":"Domain list.
        # 1. All domains are queried if this field is not specified;
        # 2. Number of domains can be adjusted depending on different accounts. The default value is 20(this limit applies to the empty value);", "zh_CN":"域名列表
        # 域名个数限制根据账号可调，默认为20个（不传递时同样受此限制）；"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_list, 'domain_list')
        if self.domain_list:
            self.domain_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['domain-list'] = self.domain_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-list') is not None:
            temp_model = QueryCdnIpListDomainList()
            self.domain_list = temp_model.from_map(m['domain-list'])
        return self


class QueryCdnIpListResponseResultServerList(TeaModel):
    def __init__(
        self,
        server: str = None,
    ):
        # {"en":"Server node IP", "zh_CN":"覆盖节点IP"}
        self.server = server

    def validate(self):
        self.validate_required(self.server, 'server')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server is not None:
            result['server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('server') is not None:
            self.server = m.get('server')
        return self


class QueryCdnIpListResponseResult(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        server_list: List[QueryCdnIpListResponseResultServerList] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain_name = domain_name
        # {"en":"serverList", "zh_CN":"服务数据"}
        self.server_list = server_list

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.server_list, 'server_list')
        if self.server_list:
            for k in self.server_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain-name'] = self.domain_name
        if self.server_list is not None:
            result['server-list'] = []
            for k in self.server_list:
                result['server-list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-name') is not None:
            self.domain_name = m.get('domain-name')
        if m.get('server-list') is not None:
            self.server_list = []
            for k in m.get('server-list'):
                temp_model = QueryCdnIpListResponseResultServerList()
                self.server_list.append(temp_model.from_map(k))
        return self


class QueryCdnIpListResponse(TeaModel):
    def __init__(
        self,
        result: List[QueryCdnIpListResponseResult] = None,
    ):
        # {"en":"domainServerList", "zh_CN":"CDN服务IP数据"}
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
            result['domain-server-list'] = []
            for k in self.result:
                result['domain-server-list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain-server-list') is not None:
            self.result = []
            for k in m.get('domain-server-list'):
                temp_model = QueryCdnIpListResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryCdnIpListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCdnIpListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCdnIpListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCdnIpListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportServerIpIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
        isp: List[str] = None,
        province: List[str] = None,
        group_by: List[str] = None,
    ):
        # {'en':'Domain:
        # 1.the maximum number of transitive domain names is 20 by default.
        # 2.Automatically filter out illegal domain names (e.g. passing illegal domain names will be filtered out, and the search results will only return the legal domain name data)', 'zh_CN':'域名列表
        # 1. 可传递域名数量上限默认为20个（可联系技术支持调整）。未传递该入参时查询账号下所有域名，但当账号下域名数量超过限制时不可查询（报错）;
        # 2. 自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）;'}
        self.domain = domain
        # {'en':'ISP.Default Query for All ISPs', 'zh_CN':'运营商，不传默认查询全部运营商；'}
        self.isp = isp
        # {'en':'Province, do not pass the default query for all provinces; optional province information:
        # anhui,beijing,chongqing,fujian,guangdong,gansu,guangxi,guizhou,henan,hubei,hebei,hainan,heilongjiang,
        # hunan,jilin,jiangsu,jiangxi,liaoning,neimenggu,ningxia,qinghai,sichuan,shandong,shanghai,shanxi2 (Shaanxi),shanxi1 (Shanxi)
        # ,tianjin,xinjiang,xizang,yunnan,zhejiang,qita (other)', 'zh_CN':'省份，不传默认查询全部省份；可选省份信息:
        # anhui,beijing,chongqing,fujian,guangdong,gansu,guangxi,guizhou,henan,hubei,hebei,hainan,heilongjiang,
        # hunan,jilin,jiangsu,jiangxi,liaoning,neimenggu,ningxia,qinghai,sichuan,shandong,shanghai,shanxi2（陕西）,shanxi1（山西）
        # ,tianjin,xinjiang,xizang,yunnan,zhejiang,qita（其它）'}
        self.province = province
        # {"en":"Group dimension:
        # 1.Optional values:domain,province,isp,you can pass in single or multiple values
        # 2.The detailed data will be displayed according to the dimension.
        # 3.The order of entering parameters does not affect the order of returned results", "zh_CN":"分组维度
        # 1. 可选值为domain、province、isp，可传入单个或多个值；
        # 2. 有传入则按照该维度展示明细数据；
        # 3. 返回结果层级顺序固定，入参顺序不影响返回结果顺序。例如：'groupBy': ['domain','province']与'groupBy': ['province','domain']返回结果一样。"}
        self.group_by = group_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province is not None:
            result['province'] = self.province
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportServerIpIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        server_ip_data: List[str] = None,
    ):
        # {'en':'Province', 'zh_CN':'省份'}
        self.province = province
        # {'en':'IP list of the covered node', 'zh_CN':'覆盖节点IP列表'}
        self.server_ip_data = server_ip_data

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.server_ip_data, 'server_ip_data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.server_ip_data is not None:
            result['serverIpData'] = self.server_ip_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('serverIpData') is not None:
            self.server_ip_data = m.get('serverIpData')
        return self


class ReportServerIpIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportServerIpIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {'en':'ISP', 'zh_CN':'运营商'}
        self.isp = isp
        self.province_data = province_data

    def validate(self):
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.province_data, 'province_data')
        if self.province_data:
            for k in self.province_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['isp'] = self.isp
        if self.province_data is not None:
            result['provinceData'] = []
            for k in self.province_data:
                result['provinceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('provinceData') is not None:
            self.province_data = []
            for k in m.get('provinceData'):
                temp_model = ReportServerIpIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportServerIpIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportServerIpIspProvinceServiceResponseResultIspData] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        self.isp_data = isp_data

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.isp_data, 'isp_data')
        if self.isp_data:
            for k in self.isp_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.isp_data is not None:
            result['ispData'] = []
            for k in self.isp_data:
                result['ispData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ispData') is not None:
            self.isp_data = []
            for k in m.get('ispData'):
                temp_model = ReportServerIpIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportServerIpIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportServerIpIspProvinceServiceResponseResult] = None,
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
                temp_model = ReportServerIpIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportServerIpIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportServerIpExistFlowServiceRequest(TeaModel):
    def __init__(
        self,
        domain: List[str] = None,
    ):
        # {'en':'domain:
        # 
        # 1.The maximum number of passable domains is 20 by default (you can contact technical support tp adjust it).
        # 2.Automatically filter out illegal domains (e.g. passing illegal domains will be filtered out, and the search results will only return the legal domain name data)', 'zh_CN':'域名：
        # 
        # 可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。'}
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


class ReportServerIpExistFlowServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ip_list: List[str] = None,
    ):
        # {'en':'Domain', 'zh_CN':'域名'}
        self.domain = domain
        # {'en':'Service IP List of domains that have traffic', 'zh_CN':'域名对应的有流量的服务IP列表'}
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self


class ReportServerIpExistFlowServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportServerIpExistFlowServiceResponseResult] = None,
    ):
        # {'en':'Result', 'zh_CN':'结果'}
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
                temp_model = ReportServerIpExistFlowServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportServerIpExistFlowServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpExistFlowServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpExistFlowServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerIpExistFlowServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportServerListServiceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerListServiceResponse(TeaModel):
    def __init__(
        self,
        ip: str = None,
        isp: str = None,
        area: str = None,
    ):
        # {"en":"IP", "zh_CN":"节点 IP"}
        self.ip = ip
        # {"en":"ISP", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"Area", "zh_CN":"区域"}
        self.area = area

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.area, 'area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.isp is not None:
            result['isp'] = self.isp
        if self.area is not None:
            result['area'] = self.area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('area') is not None:
            self.area = m.get('area')
        return self


class ReportServerListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerListServiceParameters(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # {"en":"Domain:
        # 1.The maximum number of deliverable domain names is 20 by default;
        # 2.Note that the domain_name of the input parameter is separated by a semicolon, and the semicolon needs to be escaped %3b;
        # 3.Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names);
        # ", "zh_CN":"域名：
        # 
        # 可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 注意入参的domain_name分号隔开，分号需要转义%3b；
        # 自动过滤掉非法域名（如传递非法域名，会被过滤掉，查询结果只返回合法域名的数据）。"}
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        return self


class ReportServerListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportServerListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




