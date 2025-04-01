# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryCDNServiceRealIPRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCDNServiceRealIPResponseResultWhiteipList(TeaModel):
    def __init__(
        self,
        whiteiplist: List[str] = None,
        domain_name: List[str] = None,
    ):
        # {'en':'Ip List', 'zh_CN':'真实服务IP列表'}
        self.whiteiplist = whiteiplist
        # {'en':'Domain List', 'zh_CN':'域名列表'}
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.whiteiplist, 'whiteiplist')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.whiteiplist is not None:
            result['whiteiplist'] = self.whiteiplist
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('whiteiplist') is not None:
            self.whiteiplist = m.get('whiteiplist')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        return self


class QueryCDNServiceRealIPResponseResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        whiteip_list: QueryCDNServiceRealIPResponseResultWhiteipList = None,
    ):
        self.code = code
        # {'en':'Real service IP list of domains', 'zh_CN':'域名对应的真实服务IP列表'}
        self.whiteip_list = whiteip_list

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.whiteip_list, 'whiteip_list')
        if self.whiteip_list:
            self.whiteip_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.whiteip_list is not None:
            result['whiteipList'] = self.whiteip_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('whiteipList') is not None:
            temp_model = QueryCDNServiceRealIPResponseResultWhiteipList()
            self.whiteip_list = temp_model.from_map(m['whiteipList'])
        return self


class QueryCDNServiceRealIPResponse(TeaModel):
    def __init__(
        self,
        result: QueryCDNServiceRealIPResponseResult = None,
    ):
        # {'en':'result', 'zh_CN':'结果'}
        self.result = result

    def validate(self):
        self.validate_required(self.result, 'result')
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            temp_model = QueryCDNServiceRealIPResponseResult()
            self.result = temp_model.from_map(m['result'])
        return self


class QueryCDNServiceRealIPPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCDNServiceRealIPParameters(TeaModel):
    def __init__(
        self,
        domain: str = None,
        viewtype: str = None,
        iptype: str = None,
    ):
        # {'en':'Domain names. Which are separated by semicolons, and it supports 20 domains at max.', 'zh_CN':'域名，以英文分号分隔，最多20个域名'}
        self.domain = domain
        # {'en':'Node type. Default value is all. 
        #     Optional values:
        #     dyfu: dynamic relay;
        #     stfu: static relay; 
        #     fu: dynamic relays and static relays;
        #     edge: edge node;
        #     all: dynamic relays, static relaysand edge nodes.', 'zh_CN':'节点类型，不传默认all。
        # 	dyfu：动态父； stfu:静态父； fu：动态父+静态父；&nbsp; edge ：边缘机器；&nbsp; all：动静+边缘机器。'}
        self.viewtype = viewtype
        # {'en':'IP form. Default value is ipseg. 
        #     Optional values:
        #     realip: real IP; 
        #     ipseg: IP segment.', 'zh_CN':'ip形式，不传默认 ipseg。	realip：真实IP ； ipseg：ip段。'}
        self.iptype = iptype

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.viewtype is not None:
            result['viewtype'] = self.viewtype
        if self.iptype is not None:
            result['iptype'] = self.iptype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('viewtype') is not None:
            self.viewtype = m.get('viewtype')
        if m.get('iptype') is not None:
            self.iptype = m.get('iptype')
        return self


class QueryCDNServiceRealIPRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryCDNServiceRealIPResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CheckIsCusWhiteIpRequest(TeaModel):
    def __init__(
        self,
        white_name: str = None,
        type: str = None,
        white_hash: str = None,
        ip: str = None,
    ):
        # {"en":"entername", "zh_CN":"客户英文名"}
        self.white_name = white_name
        # {"en":"resource pool type: comm_white relay_white", "zh_CN":"资源池类型【可选】 普通：comm_white；仅中转：relay_white"}
        self.type = type
        # {"en":"ip white hash verify value format hash1:hash2", "zh_CN":"资源池 hash值 hash1:hash2， 如果ipv6独立 则：hash1:hash2:y"}
        self.white_hash = white_hash
        # {"en":"check ips,split by ,", "zh_CN":"检查的ip，多个,隔开"}
        self.ip = ip

    def validate(self):
        self.validate_required(self.white_name, 'white_name')
        self.validate_required(self.white_hash, 'white_hash')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_name is not None:
            result['white_name'] = self.white_name
        if self.type is not None:
            result['type'] = self.type
        if self.white_hash is not None:
            result['white_hash'] = self.white_hash
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('white_name') is not None:
            self.white_name = m.get('white_name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('white_hash') is not None:
            self.white_hash = m.get('white_hash')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class CheckIsCusWhiteIpResponse(TeaModel):
    def __init__(
        self,
        ret_code: str = None,
        data: List[str] = None,
        msg: str = None,
    ):
        # {"en":"Return status code success represents normal fail represents abnormality", "zh_CN":"返回状态码 success 代表正常 fail 代表异常"}
        self.ret_code = ret_code
        # {"en":"return is every ip in use with yes or no", "zh_CN":"返回每个ip是否是在用服务资源池IP，格式为yes或者no"}
        self.data = data
        # {"en":"return fail message", "zh_CN":"返回报错提示消息"}
        self.msg = msg

    def validate(self):
        self.validate_required(self.ret_code, 'ret_code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.msg, 'msg')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['ret_code'] = self.ret_code
        if self.data is not None:
            result['data'] = self.data
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ret_code') is not None:
            self.ret_code = m.get('ret_code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CheckIsCusWhiteIpPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIsCusWhiteIpParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIsCusWhiteIpRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CheckIsCusWhiteIpResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QuerySpecificIPBelongRequest(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        # {'en':'IP address, use English comma to separate two items. Every IP address needs to following regular expression rule of   ((2[0-4]\\d|25[0-5]|1\\d\\d|0|[1-9]\\d?)\\.){3}(2[0-4]\\d|25[0-5]|1\\d\\d|0|[1-9]\\d?).   The default number of IPs cannot exceed 20 (you can contact technical support to adjust) .', 'zh_CN':'ip地址，以英文逗号分隔，每个ip都需要符合正则((2[0-4]\\d|25[0-5]|1\\d\\d|0|[1-9]\\d?)\\.){3}(2[0-4]\\d|25[0-5]|1\\d\\d|0|[1-9]\\d?)，ip个数默认不能超过20（可联系技术支持调整）'}
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


class QuerySpecificIPBelongResponseCheckList(TeaModel):
    def __init__(
        self,
        response: str = None,
        ip: str = None,
    ):
        # {'en':'yes: the IP belongs to Our system,
        #         no: the IP does not belong to Our system', 'zh_CN':'yes：ip属于我司，no：ip不属于我司'}
        self.response = response
        # {'en':'IP addresses', 'zh_CN':'ip地址'}
        self.ip = ip

    def validate(self):
        self.validate_required(self.response, 'response')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response is not None:
            result['response'] = self.response
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('response') is not None:
            self.response = m.get('response')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class QuerySpecificIPBelongResponse(TeaModel):
    def __init__(
        self,
        check_list: List[QuerySpecificIPBelongResponseCheckList] = None,
    ):
        # {'en':'checkList', 'zh_CN':'结果数据'}
        self.check_list = check_list

    def validate(self):
        self.validate_required(self.check_list, 'check_list')
        if self.check_list:
            for k in self.check_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_list is not None:
            result['checkList'] = []
            for k in self.check_list:
                result['checkList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkList') is not None:
            self.check_list = []
            for k in m.get('checkList'):
                temp_model = QuerySpecificIPBelongResponseCheckList()
                self.check_list.append(temp_model.from_map(k))
        return self


class QuerySpecificIPBelongPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySpecificIPBelongParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySpecificIPBelongRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerySpecificIPBelongResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class IpInfoServiceRequest(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        # {'en':'The list of IP that needs to be querying is 20 times a single time.', 'zh_CN':'需要查询的IP列表，单次最大20个（联系技术支持可调上限）'}
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


class IpInfoServiceResponseResult(TeaModel):
    def __init__(
        self,
        ip: str = None,
        is_cdn_ip: bool = None,
        country: str = None,
        province: str = None,
        city: str = None,
        isp: str = None,
    ):
        # {'en':'IP addresses', 'zh_CN':'IP地址'}
        self.ip = ip
        # {'en':'Whether to network the our IP
        # 
        #         1.true is the node IP of our CDN
        # 
        #         2.false is not the node IP of the CDN', 'zh_CN':'是否我司CDN的IP
        #         1.true 是我司CDN的节点IP
        #         2.false &nbsp; 不是我司CDN的节点IP'}
        self.is_cdn_ip = is_cdn_ip
        # {'en':'If it is not a node of the CDN, it will not return; if it is not planned, it will return unknown.', 'zh_CN':'归属国家地区；不是我司CDN的节点，不返回；如未规划的则返回未知。'}
        self.country = country
        # {'en':'If it is not a node of the CDN, it will not return; if it is not planned, it will return unknown.', 'zh_CN':'归属省份；不是我司CDN的节点，不返回；如未规划的则返回未知；'}
        self.province = province
        # {'en':'If it is not a node of the CDN, it will not return; if it is not planned, it will return unknown.', 'zh_CN':'归属城市；不是我司CDN的节点，不返回；如未规划的则返回未知；'}
        self.city = city
        # {'en':'If it is not a node of the CDN, it will not return; if it is not planned, it will return unknown.', 'zh_CN':'归属运营商；不是我司CDN的节点，不返回；如未规划的则返回未知。'}
        self.isp = isp

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.is_cdn_ip, 'is_cdn_ip')
        self.validate_required(self.country, 'country')
        self.validate_required(self.province, 'province')
        self.validate_required(self.city, 'city')
        self.validate_required(self.isp, 'isp')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.is_cdn_ip is not None:
            result['isCdnIp'] = self.is_cdn_ip
        if self.country is not None:
            result['country'] = self.country
        if self.province is not None:
            result['province'] = self.province
        if self.city is not None:
            result['city'] = self.city
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('isCdnIp') is not None:
            self.is_cdn_ip = m.get('isCdnIp')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class IpInfoServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[IpInfoServiceResponseResult] = None,
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
                temp_model = IpInfoServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class IpInfoServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpInfoServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpInfoServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IpInfoServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




