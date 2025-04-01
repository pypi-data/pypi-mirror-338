# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class MtrTestRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        area: str = None,
        isp: str = None,
    ):
        # {"en":"需要检测的域名或 IP", "zh_CN":"需要检测的域名或 IP"}
        self.host = host
        # {"en":"监控机所属地区中文名称，支持中国大陆省份、港澳台以及海外国家。
        # 可选值：
        # anhui: 安徽
        # beijing: 北京
        # chongqing: 重庆
        # fujian: 福建
        # gansu: 甘肃
        # guangdong: 广东
        # guangxi: 广西
        # guizhou: 贵州
        # hainan: 海南
        # hebei: 河北
        # heilongjiang: 黑龙江
        # henan: 河南
        # hubei: 湖北
        # hunan: 湖南
        # jiangsu: 江苏
        # jiangxi: 江西
        # jilin: 吉林
        # liaoning: 辽宁
        # neimenggu: 内蒙古
        # ningxia: 宁夏
        # qinghai: 青海
        # shaanxi: 陕西
        # shandong: 山东
        # shanghai: 上海
        # shanxi: 山西
        # sichuan: 四川
        # tianjin: 天津
        # xinjiang: 新疆
        # xizang: 西藏
        # yunnan: 云南
        # zhejiang: 浙江
        # TW: 台湾
        # HK: 香港
        # MO: 澳门
        # AE: 阿联酋
        # AU: 澳大利亚
        # BD: 孟加拉
        # BN: 文莱
        # BR: 巴西
        # CA: 加拿大
        # CL: 智利
        # CO: 哥伦比亚
        # DJ: 吉布提
        # ID: 印度尼西亚
        # IT: 意大利
        # JP: 日本
        # KG: 吉尔吉斯斯坦
        # KH: 柬埔寨
        # KR: 韩国
        # KW: 科威特
        # LA: 老挝
        # MG: 马达加斯加
        # MM: 缅甸
        # MU: 毛里求斯
        # MY: 马来西亚
        # NP: 尼泊尔
        # OM: 阿曼
        # PE: 秘鲁
        # PH: 菲律宾
        # PK: 巴基斯坦
        # QA: 卡塔尔
        # RO: 罗马尼亚
        # RU: 俄罗斯
        # SA: 沙特阿拉伯
        # SE: 瑞典
        # SG: 新加坡
        # TH: 泰国
        # TR: 土耳其
        # US: 美国
        # VN: 越南", "zh_CN":"监控机所属地区中文名称，支持中国大陆省份、港澳台以及海外国家。
        # 可选值：
        # anhui: 安徽
        # beijing: 北京
        # chongqing: 重庆
        # fujian: 福建
        # gansu: 甘肃
        # guangdong: 广东
        # guangxi: 广西
        # guizhou: 贵州
        # hainan: 海南
        # hebei: 河北
        # heilongjiang: 黑龙江
        # henan: 河南
        # hubei: 湖北
        # hunan: 湖南
        # jiangsu: 江苏
        # jiangxi: 江西
        # jilin: 吉林
        # liaoning: 辽宁
        # neimenggu: 内蒙古
        # ningxia: 宁夏
        # qinghai: 青海
        # shaanxi: 陕西
        # shandong: 山东
        # shanghai: 上海
        # shanxi: 山西
        # sichuan: 四川
        # tianjin: 天津
        # xinjiang: 新疆
        # xizang: 西藏
        # yunnan: 云南
        # zhejiang: 浙江
        # TW: 台湾
        # HK: 香港
        # MO: 澳门
        # AE: 阿联酋
        # AU: 澳大利亚
        # BD: 孟加拉
        # BN: 文莱
        # BR: 巴西
        # CA: 加拿大
        # CL: 智利
        # CO: 哥伦比亚
        # DJ: 吉布提
        # ID: 印度尼西亚
        # IT: 意大利
        # JP: 日本
        # KG: 吉尔吉斯斯坦
        # KH: 柬埔寨
        # KR: 韩国
        # KW: 科威特
        # LA: 老挝
        # MG: 马达加斯加
        # MM: 缅甸
        # MU: 毛里求斯
        # MY: 马来西亚
        # NP: 尼泊尔
        # OM: 阿曼
        # PE: 秘鲁
        # PH: 菲律宾
        # PK: 巴基斯坦
        # QA: 卡塔尔
        # RO: 罗马尼亚
        # RU: 俄罗斯
        # SA: 沙特阿拉伯
        # SE: 瑞典
        # SG: 新加坡
        # TH: 泰国
        # TR: 土耳其
        # US: 美国
        # VN: 越南"}
        self.area = area
        # {"en":"监控机所属运营商中文名。
        # 可选值：
        # 0: 中国电信
        # 1: 中国联通
        # 2: 中国铁通
        # 4: 中国移动
        # 5: 中国教育网
        # 9: 中国广电
        # 10: 长城宽带", "zh_CN":"监控机所属运营商中文名。
        # 可选值：
        # 0: 中国电信
        # 1: 中国联通
        # 2: 中国铁通
        # 4: 中国移动
        # 5: 中国教育网
        # 9: 中国广电
        # 10: 长城宽带"}
        self.isp = isp

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.area, 'area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.area is not None:
            result['area'] = self.area
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class MtrTestResponseResultDataItems(TeaModel):
    def __init__(
        self,
        num: int = None,
        ip: str = None,
        location: str = None,
        avg: str = None,
        best: str = None,
        wrst: str = None,
        last: str = None,
        loss: str = None,
        snt: str = None,
    ):
        # {'en':'','zh_CN':'序号'}
        self.num = num
        # {'en':'','zh_CN':'IP'}
        self.ip = ip
        # {'en':'','zh_CN':'所属地区运营商'}
        self.location = location
        # {'en':'The average round-trip time of all traceroute probes, in milliseconds.','zh_CN':'平均时延'}
        self.avg = avg
        # {'en':'The shortest round-trip time of all traceroute probes, in milliseconds.','zh_CN':'最优时延'}
        self.best = best
        # {'en':'The longest round-trip time of all traceroute probes, in milliseconds.','zh_CN':'最差时延'}
        self.wrst = wrst
        # {'en':'','zh_CN':'最近一次时延'}
        self.last = last
        # {'en':'The percentage of packets for which an ICMP reply was not received.','zh_CN':'丢包率'}
        self.loss = loss
        # {'en':'The number of packets sent to each hop.','zh_CN':'每跳发送的数据包数'}
        self.snt = snt

    def validate(self):
        self.validate_required(self.num, 'num')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.location, 'location')
        self.validate_required(self.avg, 'avg')
        self.validate_required(self.best, 'best')
        self.validate_required(self.wrst, 'wrst')
        self.validate_required(self.last, 'last')
        self.validate_required(self.loss, 'loss')
        self.validate_required(self.snt, 'snt')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num is not None:
            result['num'] = self.num
        if self.ip is not None:
            result['ip'] = self.ip
        if self.location is not None:
            result['location'] = self.location
        if self.avg is not None:
            result['avg'] = self.avg
        if self.best is not None:
            result['best'] = self.best
        if self.wrst is not None:
            result['wrst'] = self.wrst
        if self.last is not None:
            result['last'] = self.last
        if self.loss is not None:
            result['loss'] = self.loss
        if self.snt is not None:
            result['snt'] = self.snt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('avg') is not None:
            self.avg = m.get('avg')
        if m.get('best') is not None:
            self.best = m.get('best')
        if m.get('wrst') is not None:
            self.wrst = m.get('wrst')
        if m.get('last') is not None:
            self.last = m.get('last')
        if m.get('loss') is not None:
            self.loss = m.get('loss')
        if m.get('snt') is not None:
            self.snt = m.get('snt')
        return self


class MtrTestResponseResultData(TeaModel):
    def __init__(
        self,
        id: str = None,
        task_id: str = None,
        detect_ip: str = None,
        detect_ip_isp: str = None,
        detect_ip_isp_code: str = None,
        detect_ip_pro: str = None,
        detect_ip_pro_code: str = None,
        detect_result: str = None,
        done_time: int = None,
        status: int = None,
        items: List[MtrTestResponseResultDataItems] = None,
    ):
        # {'en':'', 'zh_CN':'任务 ID'}
        self.id = id
        # {'en':'', 'zh_CN':'任务 ID'}
        self.task_id = task_id
        # {'en':'', 'zh_CN':'监控机 IP'}
        self.detect_ip = detect_ip
        # {'en':'', 'zh_CN':'监控机运营商'}
        self.detect_ip_isp = detect_ip_isp
        # {'en':'', 'zh_CN':'监控机运营商编码'}
        self.detect_ip_isp_code = detect_ip_isp_code
        # {'en':'', 'zh_CN':'监控机所属省份'}
        self.detect_ip_pro = detect_ip_pro
        # {'en':'', 'zh_CN':'监控机所属省份编码'}
        self.detect_ip_pro_code = detect_ip_pro_code
        # {'en':'', 'zh_CN':'探测结果'}
        self.detect_result = detect_result
        # {'en':'', 'zh_CN':'探测结束时间戳'}
        self.done_time = done_time
        # {'en':'', 'zh_CN':'探测状态'}
        self.status = status
        # {'en':'','zh_CN':'每跳记录'}
        self.items = items

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.detect_ip, 'detect_ip')
        self.validate_required(self.detect_ip_isp, 'detect_ip_isp')
        self.validate_required(self.detect_ip_isp_code, 'detect_ip_isp_code')
        self.validate_required(self.detect_ip_pro, 'detect_ip_pro')
        self.validate_required(self.detect_ip_pro_code, 'detect_ip_pro_code')
        self.validate_required(self.detect_result, 'detect_result')
        self.validate_required(self.done_time, 'done_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.detect_ip is not None:
            result['detectIp'] = self.detect_ip
        if self.detect_ip_isp is not None:
            result['detectIpIsp'] = self.detect_ip_isp
        if self.detect_ip_isp_code is not None:
            result['detectIpIspCode'] = self.detect_ip_isp_code
        if self.detect_ip_pro is not None:
            result['detectIpPro'] = self.detect_ip_pro
        if self.detect_ip_pro_code is not None:
            result['detectIpProCode'] = self.detect_ip_pro_code
        if self.detect_result is not None:
            result['detectResult'] = self.detect_result
        if self.done_time is not None:
            result['doneTime'] = self.done_time
        if self.status is not None:
            result['status'] = self.status
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('detectIp') is not None:
            self.detect_ip = m.get('detectIp')
        if m.get('detectIpIsp') is not None:
            self.detect_ip_isp = m.get('detectIpIsp')
        if m.get('detectIpIspCode') is not None:
            self.detect_ip_isp_code = m.get('detectIpIspCode')
        if m.get('detectIpPro') is not None:
            self.detect_ip_pro = m.get('detectIpPro')
        if m.get('detectIpProCode') is not None:
            self.detect_ip_pro_code = m.get('detectIpProCode')
        if m.get('detectResult') is not None:
            self.detect_result = m.get('detectResult')
        if m.get('doneTime') is not None:
            self.done_time = m.get('doneTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = MtrTestResponseResultDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class MtrTestResponseResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_msg: str = None,
        host: str = None,
        data: List[MtrTestResponseResultData] = None,
    ):
        # {'en':'', 'zh_CN':''}
        self.status = status
        # {'en':'', 'zh_CN':''}
        self.error_msg = error_msg
        # {'en':'', 'zh_CN':'目标域名'}
        self.host = host
        # {'en':'data','zh_CN':'探测数据'}
        self.data = data

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.error_msg, 'error_msg')
        self.validate_required(self.host, 'host')
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
        if self.status is not None:
            result['status'] = self.status
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.host is not None:
            result['host'] = self.host
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = MtrTestResponseResultData()
                self.data.append(temp_model.from_map(k))
        return self


class MtrTestResponse(TeaModel):
    def __init__(
        self,
        result: MtrTestResponseResult = None,
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
            temp_model = MtrTestResponseResult()
            self.result = temp_model.from_map(m['result'])
        return self


class MtrTestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MtrTestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MtrTestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MtrTestResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportAvgSpeedDomainIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start date:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. Cannot exceed current time
        # 3. The most recent six-month (183 days) data are available.", "zh_CN":"开始时间:
        #         1. 时间格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        #         2. 不能大于当前时间
        #         3. 最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:MM:ss+08:00. For example, 2019-01-01T10:00:00+08:00
        # 2. The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.
        # 3. Date from, Date to both, the default query past 1 hour; If there is only one unsent, throw an exception
        # 4. Maximum allowed query time interval: 1 hour (with technical support adjustments), meaning that the difference between Date from and dateTo cannot exceed 1 hour.", "zh_CN":"结束时间:
        #         1. 时间格式2016-12-02T10:00:00+08:00
        #         2. 结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间。
        #         3. dateFrom,dateTo二者都未传,默认查询过去的1小时;如仅有一个未传,抛异常
        #         4. 允许查询最大时间间隔:1小时,即dateFrom和dateTo相差不能超过1小时(可联系技术支持调整)。"}
        self.date_to = date_to
        # {"en":"Domain name:
        # 1. The maximum number of domains that can be delivered is 20 by default (contact technical support adjustment);
        # 2. Automatically filter out illegal domain names (pass illegal domain names, will be filtered out, the query results only return the data of legitimate domain names)
        # 3. Domain name exceeding limit, misstatement", "zh_CN":"域名:
        #         1. 可传递域名数量上限默认为20个(可联系技术支持调整)。未传递该入参时查询账号下所有域名,但当账号下域名数量超过限制时不可查询(报错)。
        #         2. 自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)。"}
        self.domain = domain
        # {"en":"Data granularity:
        # 1. default 5m(only support 5 minutes)", "zh_CN":"数据粒度,默认为5m(5分钟,当前只支持5分钟)"}
        self.data_interval = data_interval
        # {"en":"Province chinese name:
        # 1. Query all provinces by default without transferring;
        # 2. Please refer to the description of the province list on the overview page for the values.", "zh_CN":"省份中文名称:
        #         1. 不传默认查询全部省份;
        #         2. 可传递的值详见概览页省份列表说明。"}
        self.province = province
        # {"en":"ISP chinese name:
        # 1. Query all ISP by default without transferring;
        # 2. Please refer to the description of the ISP list on the overview page for the values.", "zh_CN":"运营商中文名称:
        #         1. 不传默认查询全部运营商;
        #         2. 可传递的值详见概览页运营商列表说明。"}
        self.isp = isp
        # {"en":"Group dimension:
        # 1. Optional values:domain,province,isp,you can pass in single or multiple values  
        # 2. The detailed data will be displayed according to the dimension.
        #        ", "zh_CN":"分组维度:
        #         1. 可选值为domain、province、isp,可传入单个或多个值;
        #         2. 有传入则按照该维度展示明细数据;
        #         3. 返回结果层级顺序固定,入参顺序不影响返回结果顺序。例如:'groupBy': ['domain','province']与'groupBy': ['province','domain']返回结果一样。
        #         例如:传递'groupBy': ['domain','province'],则ispData下的isp节点无需返回。"}
        self.group_by = group_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        avg_speed: str = None,
        avg_response_time: str = None,
        avg_first_packet_time: str = None,
        total_response_time: str = None,
    ):
        # {"en":"Time:
        #         1. When the data query granularity is 5m, the format is yyyy-MM-dd HH:mm; the data value of every time slice represents the data value within the previous time granularity range. The first time slice of the day is yyyy-MM-dd 12:05 AM, and the last one is (yyyy-MM-dd+1) 00:00;
        #         2. Return the time slice contained in start time and the time slice contained in end time.", "zh_CN":"时间
        #         1. 查询的数据粒度为5m时,格式为yyyy-MM-dd HH:mm;每一个时间片数据值代表的是前一个时间粒度范围内的数据值。一天开始的时间片是yyyy-MM-dd 00:05,最后一个时间片是(yyyy-MM-dd+1) 00:00。
        #         2. 返回开始时间和结束时间包含的时间片。"}
        self.timestamp = timestamp
        # {"en":"Average download speed: the average download speed of all requests that meet the statistical rules in the time slice.
        # 1. unit: KB/s;
        # 2. Two decimal places are reserved.", "zh_CN":"平均下载速度:时间片(timestamp)内符合统计规则的所有请求的平均下载速度。
        #         1. 计量单位:KB/s;
        #         2. 保留两位小数。"}
        self.avg_speed = avg_speed
        # {"en":"Average response time: the average response time of a single request in a time stamp. Unit : millisecond.", "zh_CN":"平均响应时间:时间片(timestamp)内单条请求平均响应时间。计量单位:毫秒。"}
        self.avg_response_time = avg_response_time
        # {"en":"Average first packet response time: the average first packet response time of a single request in a time slice. Unit: millisecond.", "zh_CN":"平均首包响应时间:时间片(timestamp)内单条请求平均首包响应时间。计量单位:毫秒。"}
        self.avg_first_packet_time = avg_first_packet_time
        # {"en":"Total response time: the response time summary of all requests that meet the statistical rules in the time slice. Unit: millisecond.", "zh_CN":"总响应时间:时间片(timestamp)内符合统计规则的所有请求响应时间汇总。计量单位:毫秒。"}
        self.total_response_time = total_response_time

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.avg_speed, 'avg_speed')
        self.validate_required(self.avg_response_time, 'avg_response_time')
        self.validate_required(self.avg_first_packet_time, 'avg_first_packet_time')
        self.validate_required(self.total_response_time, 'total_response_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.avg_speed is not None:
            result['avgSpeed'] = self.avg_speed
        if self.avg_response_time is not None:
            result['avgResponseTime'] = self.avg_response_time
        if self.avg_first_packet_time is not None:
            result['avgFirstPacketTime'] = self.avg_first_packet_time
        if self.total_response_time is not None:
            result['totalResponseTime'] = self.total_response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('avgSpeed') is not None:
            self.avg_speed = m.get('avgSpeed')
        if m.get('avgResponseTime') is not None:
            self.avg_response_time = m.get('avgResponseTime')
        if m.get('avgFirstPacketTime') is not None:
            self.avg_first_packet_time = m.get('avgFirstPacketTime')
        if m.get('totalResponseTime') is not None:
            self.total_response_time = m.get('totalResponseTime')
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        details: List[ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceDataDetails] = None,
    ):
        # {"en":"ISP chinese name", "zh_CN":"省份中文名称"}
        self.province = province
        # {"en":"details", "zh_CN":"详情数据"}
        self.details = details

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponseResultIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceData] = None,
    ):
        # {"en":"Internet service providers", "zh_CN":"运营商"}
        self.isp = isp
        # {"en":"provinceData", "zh_CN":"省份数据"}
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
                temp_model = ReportAvgSpeedDomainIspProvinceServiceResponseResultIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportAvgSpeedDomainIspProvinceServiceResponseResultIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"ispData", "zh_CN":"ISP数据"}
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
                temp_model = ReportAvgSpeedDomainIspProvinceServiceResponseResultIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportAvgSpeedDomainIspProvinceServiceResponseResult] = None,
    ):
        # {"en":"result", "zh_CN":"结果"}
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
                temp_model = ReportAvgSpeedDomainIspProvinceServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportAvgSpeedDomainIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportAvgSpeedDomainIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportAvgSpeedDomainIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportAvgSpeedDomainIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetLiveStreamPushingStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetLiveStreamPushingStatusResponseDataValue(TeaModel):
    def __init__(
        self,
        deployaddress: str = None,
        inaddress: str = None,
        streamname: str = None,
        fps: int = None,
        lfr: float = None,
        inbandwidth: int = None,
        videotmstmp: str = None,
        audiotmstmp: str = None,
    ):
        # {'en':'Push stream CDN node, that is, the IP address of edge node of the received data source, separated by multiple commas', 'zh_CN':'推流cdn节点，即收到数据源的edge节点IP地址，多个逗号分隔'}
        self.deployaddress = deployaddress
        # {'en':'Push user IP (data source) address, separated by multiple commas', 'zh_CN':'推流用户ip（数据源）地址，多个逗号分隔'}
        self.inaddress = inaddress
        # {'en':'The channel of anchor', 'zh_CN':'主播流名'}
        self.streamname = streamname
        # {'en':'Anchor Current encoding frame rate.Unit: fps', 'zh_CN':'主播当前编码帧率，单位:fps'}
        self.fps = fps
        # {'en':'Current frame loss rate of anchor.Unit: fps', 'zh_CN':'主播当前丢帧率，单位:fps'}
        self.lfr = lfr
        # {'en':'Anchor Current bit rate.Unit: bps', 'zh_CN':'主播当前码率，单位:bps'}
        self.inbandwidth = inbandwidth
        # {'en':'Video timestamps are separated by multiple commas.Unit: ms', 'zh_CN':'视频时间戳 多个逗号分隔，单位:ms'}
        self.videotmstmp = videotmstmp
        # {'en':'Audio timestamp, separated by multiple commas.Unit: ms', 'zh_CN':'音频时间戳，多个逗号分隔，单位:ms'}
        self.audiotmstmp = audiotmstmp

    def validate(self):
        self.validate_required(self.deployaddress, 'deployaddress')
        self.validate_required(self.inaddress, 'inaddress')
        self.validate_required(self.streamname, 'streamname')
        self.validate_required(self.fps, 'fps')
        self.validate_required(self.lfr, 'lfr')
        self.validate_required(self.inbandwidth, 'inbandwidth')
        self.validate_required(self.videotmstmp, 'videotmstmp')
        self.validate_required(self.audiotmstmp, 'audiotmstmp')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployaddress is not None:
            result['deployaddress'] = self.deployaddress
        if self.inaddress is not None:
            result['inaddress'] = self.inaddress
        if self.streamname is not None:
            result['streamname'] = self.streamname
        if self.fps is not None:
            result['fps'] = self.fps
        if self.lfr is not None:
            result['lfr'] = self.lfr
        if self.inbandwidth is not None:
            result['inbandwidth'] = self.inbandwidth
        if self.videotmstmp is not None:
            result['videotmstmp'] = self.videotmstmp
        if self.audiotmstmp is not None:
            result['audiotmstmp'] = self.audiotmstmp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployaddress') is not None:
            self.deployaddress = m.get('deployaddress')
        if m.get('inaddress') is not None:
            self.inaddress = m.get('inaddress')
        if m.get('streamname') is not None:
            self.streamname = m.get('streamname')
        if m.get('fps') is not None:
            self.fps = m.get('fps')
        if m.get('lfr') is not None:
            self.lfr = m.get('lfr')
        if m.get('inbandwidth') is not None:
            self.inbandwidth = m.get('inbandwidth')
        if m.get('videotmstmp') is not None:
            self.videotmstmp = m.get('videotmstmp')
        if m.get('audiotmstmp') is not None:
            self.audiotmstmp = m.get('audiotmstmp')
        return self


class GetLiveStreamPushingStatusResponse(TeaModel):
    def __init__(
        self,
        rettime: str = None,
        retcode: int = None,
        data_value: List[GetLiveStreamPushingStatusResponseDataValue] = None,
    ):
        # {'en':'The time of the data returned', 'zh_CN':'返回的数据的时间'}
        self.rettime = rettime
        # {'en':'Number of data items. 0 is returned if there is no data', 'zh_CN':'数据条数，无数据返回0'}
        self.retcode = retcode
        # {'en':'', 'zh_CN':'推流信息数据集合'}
        self.data_value = data_value

    def validate(self):
        self.validate_required(self.rettime, 'rettime')
        self.validate_required(self.retcode, 'retcode')
        self.validate_required(self.data_value, 'data_value')
        if self.data_value:
            for k in self.data_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rettime is not None:
            result['rettime'] = self.rettime
        if self.retcode is not None:
            result['retcode'] = self.retcode
        if self.data_value is not None:
            result['dataValue'] = []
            for k in self.data_value:
                result['dataValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rettime') is not None:
            self.rettime = m.get('rettime')
        if m.get('retcode') is not None:
            self.retcode = m.get('retcode')
        if m.get('dataValue') is not None:
            self.data_value = []
            for k in m.get('dataValue'):
                temp_model = GetLiveStreamPushingStatusResponseDataValue()
                self.data_value.append(temp_model.from_map(k))
        return self


class GetLiveStreamPushingStatusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetLiveStreamPushingStatusParameters(TeaModel):
    def __init__(
        self,
        u: str = None,
        t: int = None,
        channel: str = None,
        g: str = None,
    ):
        # {'en':'Push domain(multiple domains supported, separated by commas)', 'zh_CN':'推流域名（支持多个域名，以逗号分隔）'}
        self.u = u
        # {'en':'Time, eg: 20160527152300, if not filled in, the current time -5 minutes', 'zh_CN':'时间，eg：20160527152300，不填时为当前时间-5分钟'}
        self.t = t
        # {'en':'Push channel URL (multiple push channel URLs are supported, separated by commas)', 'zh_CN':'推流流名(支持多个推流流名，以逗号分隔)'}
        self.channel = channel
        # {'en':'Query interval. The value can be 10 or 60. The default value is 60
        # When g is 10, query the data of the nearest whole 10 seconds to time t
        # When g is 60, query the data of the nearest whole minute to time t', 'zh_CN':'查询间隔，可选值10、60，默认60
        # 当g为10时，查询距离时间t最近的整10秒点数据
        # 当g为60时，查询距离时间t最近的整分钟点数据'}
        self.g = g

    def validate(self):
        self.validate_required(self.u, 'u')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.u is not None:
            result['u'] = self.u
        if self.t is not None:
            result['t'] = self.t
        if self.channel is not None:
            result['channel'] = self.channel
        if self.g is not None:
            result['g'] = self.g
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('u') is not None:
            self.u = m.get('u')
        if m.get('t') is not None:
            self.t = m.get('t')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('g') is not None:
            self.g = m.get('g')
        return self


class GetLiveStreamPushingStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetLiveStreamPushingStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportOnlineNumIspProvinceServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        data_interval: str = None,
        province: List[str] = None,
        isp: List[str] = None,
        group_by: List[str] = None,
    ):
        # {"en":"Start time:
        # 	1.The format is yyyy-MM-ddTHH:mm:ss+08:00; 
        # 	2.Must be a time that is 183 days earlier than the current time, and the time must be earlier than the current time and dateTo; 
        # 	3.Period between dataFrom and dateTo cannot be longer than 1 hour; 
        # 	4.dateFrom and dateTo can be either both are specified or neither is specifies; 
        # 	5.If neither dateFrom nor dateTo is specified, then by default, data in the last 30 minutes is queried.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于当前时间-183天,并且小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过1小时(可联系技术支持调整);
        # 4.dateFrom和dateTo要么都传递,要么都不传递;
        # 5.dateFrom和dateTo都未传递,则默认查询过去30分钟的数据;"}
        self.date_from = date_from
        # {"en":"End time: 
        # 1.The time format is yyyy-MM-ddTHH:MM:ss+08:00.
        # 2.The end time needs to be greater than the start time. If the end time is greater than the current time, take the current time.", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to
        # {"en":"Domain: 
        # 	1.Allowable maximum number of domain is 20 (can be adjusted by contacting technical support).
        # 	2.Domain is not uploaded: Query all domain names of the account", "zh_CN":"域名:
        # 可传递域名数量上限默认为20个(可联系技术支持调整);
        # 自动过滤掉非法域名(如传递非法域名,会被过滤掉,查询结果只返回合法域名的数据)
        # 域名超过上限,报错"}
        self.domain = domain
        # {"en":"data granularity:
        # 1m: 1 minute
        # 5m: 5 minutes
        # Do not pass default query 5m", "zh_CN":"数据粒度:
        # 1m: 1分钟粒度
        # 5m: 5分钟粒度
        # 不传默认查询 5m"}
        self.data_interval = data_interval
        # {"en":"1.Province is not upload: Query all provinces and aggregate the returned data according to all provinces; 
        # 2.Province is upload: Provinces can transmit Chinese or code. Please refer to the appendix description section of the overview page for the provincial information code table.
        # 
        # 3.Support language request header Accept Language, only support zh-CN and en-US, default to zh-CN. Accept Language: en-US, both the province and isp input and return are in code, otherwise the return is in Chinese.", "zh_CN":"省份
        # 
        # 1.未传递province时：查询所有省份，返回的数据按照所有省份聚合。
        # 
        # 2.有传递province时：省份 可传中文或code。省份信息码表详见概览页附录说明章节
        # 
        # 3.支持语言请求头Accept-Language，只支持zh-CN、en-US，默认为zh-CN。Accept-Language：en-US时，省份及运营商 入参及返回都为code，否则返回的为中文。"}
        self.province = province
        # {"en":"ISP:
        # 1.ISP is not upload: Query all ISPs and aggregate the returned data according to all ISPs; 
        # 2.ISPs is upload: Isp can transmit Chinese or code. Please refer to the appendix description section of the overview page for the ISP information code table.", "zh_CN":"运营商：
        # 1.未传递isp时：查询所有isp，返回的数据按照所有运营商聚合。 
        # 2.有传递isp时：运营商 可传中文或code。运营商信息码表详见概览页附录说明章节"}
        self.isp = isp
        # {"en":"Group by:
        # 	1.Optional value: domain,province,isp; Multiple values can be selected.
        # 	2.If there is an input, the detailed data will be displayed according to this dimension ", "zh_CN":"分组维度:
        # 可选值为domain,province,isp,可传入多个值;
        # 有传入则按照该维度展示明细数据;"}
        self.group_by = group_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.data_interval is not None:
            result['dataInterval'] = self.data_interval
        if self.province is not None:
            result['province'] = self.province
        if self.isp is not None:
            result['isp'] = self.isp
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('dataInterval') is not None:
            self.data_interval = m.get('dataInterval')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceDataDetails(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {"en":"Time, the format is yyyy-MM-dd HH:mm", "zh_CN":"时间,格式为yyyy-MM-dd HH:mm"}
        self.timestamp = timestamp
        # {"en":"online users", "zh_CN":"在线人数"}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceData(TeaModel):
    def __init__(
        self,
        province: str = None,
        details: List[ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceDataDetails] = None,
    ):
        # {"en":"Province", "zh_CN":"省份"}
        self.province = province
        self.details = details

    def validate(self):
        self.validate_required(self.province, 'province')
        self.validate_required(self.details, 'details')
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province is not None:
            result['province'] = self.province
        if self.details is not None:
            result['details'] = []
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('details') is not None:
            self.details = []
            for k in m.get('details'):
                temp_model = ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ReportOnlineNumIspProvinceServiceResponseDataIspData(TeaModel):
    def __init__(
        self,
        isp: str = None,
        province_data: List[ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceData] = None,
    ):
        # {"en":"ISP", "zh_CN":"运营商"}
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
                temp_model = ReportOnlineNumIspProvinceServiceResponseDataIspDataProvinceData()
                self.province_data.append(temp_model.from_map(k))
        return self


class ReportOnlineNumIspProvinceServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        isp_data: List[ReportOnlineNumIspProvinceServiceResponseDataIspData] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
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
                temp_model = ReportOnlineNumIspProvinceServiceResponseDataIspData()
                self.isp_data.append(temp_model.from_map(k))
        return self


class ReportOnlineNumIspProvinceServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportOnlineNumIspProvinceServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"request result information", "zh_CN":"请求结果信息"}
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
                temp_model = ReportOnlineNumIspProvinceServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportOnlineNumIspProvinceServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportOnlineNumIspProvinceServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportOnlineNumIspProvinceServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportOnlineNumIspProvinceServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ConcurrentSessionRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
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
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class ConcurrentSessionResponseProviderDateConcurrent(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'明细数据'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class ConcurrentSessionResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        concurrent: List[ConcurrentSessionResponseProviderDateConcurrent] = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'concurrent', 'zh_CN':'明细数据'}
        self.concurrent = concurrent

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.concurrent, 'concurrent')
        if self.concurrent:
            for k in self.concurrent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.concurrent is not None:
            result['concurrent'] = []
            for k in self.concurrent:
                result['concurrent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('concurrent') is not None:
            self.concurrent = []
            for k in m.get('concurrent'):
                temp_model = ConcurrentSessionResponseProviderDateConcurrent()
                self.concurrent.append(temp_model.from_map(k))
        return self


class ConcurrentSessionResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: ConcurrentSessionResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'明细数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = ConcurrentSessionResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class ConcurrentSessionResponse(TeaModel):
    def __init__(
        self,
        provider: ConcurrentSessionResponseProvider = None,
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
            temp_model = ConcurrentSessionResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class ConcurrentSessionPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ConcurrentSessionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ConcurrentSessionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ConcurrentSessionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthAppaRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        appa_bandwidth_type: str = None,
        need_flow: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"为需要查询带宽数据的起始日期,日期格式为yyyy-mm-dd ；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"为需要查询带宽数据的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"bandwidth type of appa.
        # 1)optional values:appaEdgeUp, appaEdgeDown, appaEdgeSend,appaInterimReceiver,appaInterimSend,appaOriginReceiver,appaSourceUpSae,appaSourceUpNode,appaSourceUpTotal,appaSoruceDownSae,appaSourceDownNod,appaSourceDownTotal.
        # 2)If there are multiple inputs,use ';'as separator.
        # 3)Four type at most at a  time.", "zh_CN":"appaEdgeUp(边缘上行), appaEdgeDown(边缘下行), appaEdgeSend(中转下行),appaInterimReceiver(中转上行),appaInterimSend(回源下行),appaOriginReceiver(回源上行),appaSourceUpSae(源站上行（SAE）),appaSourceUpNode(源站上行（节点）),appaSourceUpTotal(源站下行总带宽（SAE+节点）),appaSoruceDownSae(源站下行（SAE）),appaSourceDownNode(源站下行（节点）),appaSourceDownTotal(源站下行总带宽（SAE+节点）), 多种类型之间用英文分号进行分隔，最多同时只能选择四种类型,"}
        self.appa_bandwidth_type = appa_bandwidth_type
        # {"en":"Whether to return traffic details, 1: yes; 0: no. The default is 0.", "zh_CN":"是否需要返回流量明细，1：需要；0：不需要。默认为0."}
        self.need_flow = need_flow

    def validate(self):
        self.validate_required(self.appa_bandwidth_type, 'appa_bandwidth_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.appa_bandwidth_type is not None:
            result['appaBandwidthType'] = self.appa_bandwidth_type
        if self.need_flow is not None:
            result['needFlow'] = self.need_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('appaBandwidthType') is not None:
            self.appa_bandwidth_type = m.get('appaBandwidthType')
        if m.get('needFlow') is not None:
            self.need_flow = m.get('needFlow')
        return self


class BandwidthAppaResponseProviderDateAppaBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点，格式 yyyy-MM-dd hh:mm:ss'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽，单位Mbps'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class BandwidthAppaResponseProviderDateAppa(TeaModel):
    def __init__(
        self,
        type: str = None,
        channel: str = None,
        bandwidth: List[BandwidthAppaResponseProviderDateAppaBandwidth] = None,
    ):
        # {'en':'type', 'zh_CN':'appa数据类型'}
        self.type = type
        # {'en':'channel', 'zh_CN':'频道名称'}
        self.channel = channel
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.type, 'type')
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.channel is not None:
            result['channel'] = self.channel
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthAppaResponseProviderDateAppaBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthAppaResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        appa: List[BandwidthAppaResponseProviderDateAppa] = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'appa', 'zh_CN':'appa带宽数据'}
        self.appa = appa

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.appa, 'appa')
        if self.appa:
            for k in self.appa:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.appa is not None:
            result['appa'] = []
            for k in self.appa:
                result['appa'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('appa') is not None:
            self.appa = []
            for k in m.get('appa'):
                temp_model = BandwidthAppaResponseProviderDateAppa()
                self.appa.append(temp_model.from_map(k))
        return self


class BandwidthAppaResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthAppaResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'APPA带宽数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = BandwidthAppaResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthAppaResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthAppaResponseProvider = None,
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
            temp_model = BandwidthAppaResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthAppaPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthAppaParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthAppaRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthAppaResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainUserAgentServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        area_code: List[str] = None,
        device_type: str = None,
        orderby: str = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2016-12-02T10:00 + 08:00 (10:0:00 Beijing time on December 2, 2016);
        # 2. Can not exceed the current time;
        # 3. The latest half year (183 days) data can be obtained at most.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00,例如,2016-12-02T10:00:00+08:00(为北京时间2016年12月2日10点0分0秒);
        # 2.不能大于当前时间;
        # 3.最多可获取最近半年(183天)的数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The 1format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 31 days, that is, the difference between dateFrom and dateTo can not exceed 31 days.", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.结束时间需大于开始时间;
        # 3.结束时间如果大于当前时间,取当前时间;
        # 4.dateFrom,dateTo二者都未传,默认查询过去的24小时;如仅有一个未传,抛异常;
        # 5.允许查询最大间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"Domains:
        # 1.Domain is not uploaded: Query all domain names of the account (More than 20 domains will error,you can contact technical support for adjustment);
        # 2.Domain is uploaded: Up to 20 domains are supported(you can contact technical support for adjustment).", "zh_CN":"域名:
        # 1.未传递domain时:查询账号下所有全部域名(域名超过20个则报错,可联系技术支持调整);
        # 2.有传递domain时:域名最多支持传20个(可联系技术支持调整)"}
        self.domain = domain
        # {"en":"Acceleration area:
        # Acceleration areaCode is not uploaded, query all acceleration areas by default.", "zh_CN":"加速区域:未传递areaCode时,默认查询所有加速区域。"}
        self.area_code = area_code
        # {"en":"Query type:
        # 1.The optional values are browser, brand, os;The defalut value is browser.
        # 2.When the value is browser, query according to the browser.
        # 3.When the value is brand, query based on the mobile device brand.
        # 4.When the value is os, query according to the operating system.", "zh_CN":"查询类型
        # 1.可选值为browser,brand,os,不传默认按照browser查询;
        # 2.值为browser时,则根据浏览器查询;
        # 3.值为brand时,则根据移动设备品牌查询;
        # 4.值为os时,则根据操作系统查询。"}
        self.device_type = device_type
        # {"en":"Order by:
        # 	1.The optional values are flow and request;
        # 	2.If not passed, the default is request;
        # 	3.When the value is flow, the query results are sorted in descending order of traffic, and when the value is request, they are sorted in descending order of the number of requests.", "zh_CN":"排序:
        # 1.可选值为flow、request;
        # 2.不传默认为request;
        # 3.值为flow时查询结果按流量降序排列,值为request时按请求数降序排列"}
        self.orderby = orderby

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.area_code is not None:
            result['areaCode'] = self.area_code
        if self.device_type is not None:
            result['deviceType'] = self.device_type
        if self.orderby is not None:
            result['orderby'] = self.orderby
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('areaCode') is not None:
            self.area_code = m.get('areaCode')
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')
        if m.get('orderby') is not None:
            self.orderby = m.get('orderby')
        return self


class ReportDomainUserAgentServiceResponseData(TeaModel):
    def __init__(
        self,
        user_agent: str = None,
        flow: int = None,
        request: int = None,
    ):
        # {"en":"UA", "zh_CN":"UA"}
        self.user_agent = user_agent
        # {"en":"Flow value. Unit is MB and 2 digits of decimals are allowed.", "zh_CN":"流量,保留2位小数,单位MB"}
        self.flow = flow
        # {"en":"Number of requests.", "zh_CN":"请求数"}
        self.request = request

    def validate(self):
        self.validate_required(self.user_agent, 'user_agent')
        self.validate_required(self.flow, 'flow')
        self.validate_required(self.request, 'request')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.flow is not None:
            result['flow'] = self.flow
        if self.request is not None:
            result['request'] = self.request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('request') is not None:
            self.request = m.get('request')
        return self


class ReportDomainUserAgentServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportDomainUserAgentServiceResponseData] = None,
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
                temp_model = ReportDomainUserAgentServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainUserAgentServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainUserAgentServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainUserAgentServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainUserAgentServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDailyLiveTranscodingDurationRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
        transcode_type: str = None,
        definition: str = None,
        is_audio: str = None,
        timezone: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"This parameter specifies if the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way:
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"Transcoding type, values can be h264, h265, zdgq_264, zdgq_265, cf_264, cf_265, or other. Multiple transcoding types should be separated by a semicolon. If some of the transcoding types are incorrect, the system will return data for the correct types; if all transcoding types are incorrect, it will return an error 'invalid transcodeType.' If not provided or left empty, it defaults to all types.", "zh_CN":"转码类型,值为h264、h265、zdgq_264、zdgq_265、cf_264、cf_265，other 多个转码类型用英文分号;分隔开。当传入转码类型部分错误时，返回正确的类型的数据；当传入转码类型全部错误时，返回错误invalid transcodeType. 不填或为空，默认为所有类型."}
        self.transcode_type = transcode_type
        # {"en":"Resolution types include LD480, SD720, HD1080, 2K, 4K, 8K, SD576. Multiple resolutions are separated by a semicolon. When isAudio=1, this parameter is invalid and will return an error. Param definition must be empty when querying audio data.", "zh_CN":"清晰度类型,值为LD480、SD720、HD1080、2K、4K、8K、SD576，多个清晰度用英文分号;分隔开, 当isAudio=1时，此入参无效返回错误 param definition must be empty when query audio data."}
        self.definition = definition
        # {"en":"Audio/Video Type, 1: Audio 2: Video. Defaults to 2 if not selected or empty. Only a single value is allowed.", "zh_CN":"音视频类型, 1:音频   2:视频. 不选或者为空时默认为2. 只能输入单个值."}
        self.is_audio = is_audio
        # {"en":"Greenwich time zone, the parameter format GMT+09:00 means East Nine District, GMT-09:00 means West Nine District, if not passed, the default is the local time zone (East Eight District)", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.transcode_type is not None:
            result['transcodeType'] = self.transcode_type
        if self.definition is not None:
            result['definition'] = self.definition
        if self.is_audio is not None:
            result['isAudio'] = self.is_audio
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('transcodeType') is not None:
            self.transcode_type = m.get('transcodeType')
        if m.get('definition') is not None:
            self.definition = m.get('definition')
        if m.get('isAudio') is not None:
            self.is_audio = m.get('isAudio')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class QueryDailyLiveTranscodingDurationResponseProviderDateTranscodingLive(TeaModel):
    def __init__(
        self,
        time: str = None,
        h_264: str = None,
        h_265: str = None,
        zdgq__264: str = None,
        zdgq__265: str = None,
        voice: str = None,
        total: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'h264 transcoding time', 'zh_CN':'h264转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.h_264 = h_264
        # {'en':'h265 transcoding time', 'zh_CN':'h265转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.h_265 = h_265
        # {'en':'zdgq_264 transcoding time', 'zh_CN':'zdgq_264转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.zdgq__264 = zdgq__264
        # {'en':'zdgq_265 transcoding time', 'zh_CN':'zdgq_265转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.zdgq__265 = zdgq__265
        # {'en':'voice transcoding time', 'zh_CN':'voice转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.voice = voice
        # {'en':'total transcoding time', 'zh_CN':'总转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.total = total

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.h_264, 'h_264')
        self.validate_required(self.h_265, 'h_265')
        self.validate_required(self.zdgq__264, 'zdgq__264')
        self.validate_required(self.zdgq__265, 'zdgq__265')
        self.validate_required(self.voice, 'voice')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.h_264 is not None:
            result['h264'] = self.h_264
        if self.h_265 is not None:
            result['h265'] = self.h_265
        if self.zdgq__264 is not None:
            result['zdgq_264'] = self.zdgq__264
        if self.zdgq__265 is not None:
            result['zdgq_265'] = self.zdgq__265
        if self.voice is not None:
            result['voice'] = self.voice
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('h264') is not None:
            self.h_264 = m.get('h264')
        if m.get('h265') is not None:
            self.h_265 = m.get('h265')
        if m.get('zdgq_264') is not None:
            self.zdgq__264 = m.get('zdgq_264')
        if m.get('zdgq_265') is not None:
            self.zdgq__265 = m.get('zdgq_265')
        if m.get('voice') is not None:
            self.voice = m.get('voice')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryDailyLiveTranscodingDurationResponseProviderDateTranscoding(TeaModel):
    def __init__(
        self,
        name: str = None,
        live: List[QueryDailyLiveTranscodingDurationResponseProviderDateTranscodingLive] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'live', 'zh_CN':'直播转码时长数据'}
        self.live = live

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.live, 'live')
        if self.live:
            for k in self.live:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.live is not None:
            result['live'] = []
            for k in self.live:
                result['live'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('live') is not None:
            self.live = []
            for k in m.get('live'):
                temp_model = QueryDailyLiveTranscodingDurationResponseProviderDateTranscodingLive()
                self.live.append(temp_model.from_map(k))
        return self


class QueryDailyLiveTranscodingDurationResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        transcoding: QueryDailyLiveTranscodingDurationResponseProviderDateTranscoding = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'transcoding', 'zh_CN':'转码类型'}
        self.transcoding = transcoding

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.transcoding, 'transcoding')
        if self.transcoding:
            self.transcoding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.transcoding is not None:
            result['transcoding'] = self.transcoding.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('transcoding') is not None:
            temp_model = QueryDailyLiveTranscodingDurationResponseProviderDateTranscoding()
            self.transcoding = temp_model.from_map(m['transcoding'])
        return self


class QueryDailyLiveTranscodingDurationResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: QueryDailyLiveTranscodingDurationResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'直播转码时长每日统计数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = QueryDailyLiveTranscodingDurationResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class QueryDailyLiveTranscodingDurationResponse(TeaModel):
    def __init__(
        self,
        provider: QueryDailyLiveTranscodingDurationResponseProvider = None,
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
            temp_model = QueryDailyLiveTranscodingDurationResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class QueryDailyLiveTranscodingDurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDailyLiveTranscodingDurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDailyLiveTranscodingDurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDailyLiveTranscodingDurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelValueRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        dataformat: str = None,
        is_exact_match: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '00:01'.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM若没有输入时、分，则时分默认为00:01；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd hh:MM.If 'hh:MM' not specified,it means '24:00'.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,精确到分钟,日期格式为yyyy-mm-dd hh:MM,若没有输入时、分，则时分默认为24:00；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        return self


class ChannelValueResponseProviderDateInformation(TeaModel):
    def __init__(
        self,
        channel: str = None,
        charge_method: str = None,
        acce_type: str = None,
        value: str = None,
        unit: str = None,
        peak_value: str = None,
        peak_time: str = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel
        # {'en':'charge method', 'zh_CN':'计费方式'}
        self.charge_method = charge_method
        # {'en':'acce type', 'zh_CN':'加速类型'}
        self.acce_type = acce_type
        # {'en':'value', 'zh_CN':'计费值'}
        self.value = value
        # {'en':'unit', 'zh_CN':'单位'}
        self.unit = unit
        # {'en':'peak value', 'zh_CN':'峰值'}
        self.peak_value = peak_value
        # {'en':'peak time', 'zh_CN':'峰值时间'}
        self.peak_time = peak_time

    def validate(self):
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.charge_method, 'charge_method')
        self.validate_required(self.acce_type, 'acce_type')
        self.validate_required(self.value, 'value')
        self.validate_required(self.unit, 'unit')
        self.validate_required(self.peak_value, 'peak_value')
        self.validate_required(self.peak_time, 'peak_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.charge_method is not None:
            result['chargeMethod'] = self.charge_method
        if self.acce_type is not None:
            result['acceType'] = self.acce_type
        if self.value is not None:
            result['value'] = self.value
        if self.unit is not None:
            result['unit'] = self.unit
        if self.peak_value is not None:
            result['peakValue'] = self.peak_value
        if self.peak_time is not None:
            result['peakTime'] = self.peak_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('chargeMethod') is not None:
            self.charge_method = m.get('chargeMethod')
        if m.get('acceType') is not None:
            self.acce_type = m.get('acceType')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('peakValue') is not None:
            self.peak_value = m.get('peakValue')
        if m.get('peakTime') is not None:
            self.peak_time = m.get('peakTime')
        return self


class ChannelValueResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        information: ChannelValueResponseProviderDateInformation = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'information', 'zh_CN':'信息集'}
        self.information = information

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.information, 'information')
        if self.information:
            self.information.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.information is not None:
            result['information'] = self.information.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('information') is not None:
            temp_model = ChannelValueResponseProviderDateInformation()
            self.information = temp_model.from_map(m['information'])
        return self


class ChannelValueResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: ChannelValueResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'频道流量数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = ChannelValueResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class ChannelValueResponse(TeaModel):
    def __init__(
        self,
        provider: ChannelValueResponseProvider = None,
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
            temp_model = ChannelValueResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class ChannelValuePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelValueResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainStreamDurationServiceRequestDomainStream(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream: List[str] = None,
    ):
        # {"en":"Domain name: 
        # 1. The maximum number of domain names that can be transferred is 1 by default; 
        # 2. Automatically filter out invalid domain names (if an illegal domain name is transferred, it will be filtered out, and the query results will only return the data of valid domain names).", "zh_CN":"域名:
        # 1、可传递域名数量上限默认为1个;
        # 2、自动过滤掉无效域名(如传递非法域名,会被过滤掉,查询结果只返回有效域名的数据)。"}
        self.domain = domain
        # {"en":"stream name:
        # Just pass the publishing point + stream name, Example: live/test-20180101-test where live is a publishing point and test-20180101-test is a stream name", "zh_CN":"流名:
        # 只需要传发布点+流名,例如:live/test-20180101-test ,其中live是发布点，test-20180101-test是流名"}
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class ReportDomainStreamDurationServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain_stream: List[ReportDomainStreamDurationServiceRequestDomainStream] = None,
    ):
        # {"en":"Start time: 
        # 1.Format is yyyyMMdd; 
        # 2.Must be smaller than the current system time; 
        # 3.Default value of current time is used if the field is not specified; 
        # 4.You can only query data for the last 6 months.
        # ", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-dd,例如,2021-08-10
        # 2.不能大于当前时间
        # 3.只能查询最近半年内数据。"}
        self.date_from = date_from
        # {"en":"End Time:
        # 1. The time format is yyyy-MM-dd
        # 2. The end time must be greater than the start time. If the end time is greater than the current time, take the current time
        # 3. Both dateFrom and dateTo have not been passed, and the past 7 days are queried by default; if only one has not been passed, an exception will be thrown
        # 4. The maximum time interval allowed for query: 31 days, that is, the difference between dateFrom and dateTo cannot exceed 31 days", "zh_CN":"结束时间:
        # 1.时间格式为yyyy-MM-dd
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的7天;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔:31天,即dateFrom和dateTo相差不能超过31天。"}
        self.date_to = date_to
        # {"en":"-", "zh_CN":"-"}
        self.domain_stream = domain_stream

    def validate(self):
        if self.domain_stream:
            for k in self.domain_stream:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain_stream is not None:
            result['domainStream'] = []
            for k in self.domain_stream:
                result['domainStream'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domainStream') is not None:
            self.domain_stream = []
            for k in m.get('domainStream'):
                temp_model = ReportDomainStreamDurationServiceRequestDomainStream()
                self.domain_stream.append(temp_model.from_map(k))
        return self


class ReportDomainStreamDurationServiceResponseDataStreamListDurationDetailList(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        duration: int = None,
    ):
        # {"en":"Stream start time", "zh_CN":"推流起始时间"}
        self.start_time = start_time
        # {"en":"Stream end time", "zh_CN":"推流终止时间"}
        self.end_time = end_time
        # {"en":"Streaming duration, in milliseconds", "zh_CN":"推流时长,单位为毫秒"}
        self.duration = duration

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class ReportDomainStreamDurationServiceResponseDataStreamList(TeaModel):
    def __init__(
        self,
        stream: str = None,
        sum_time: int = None,
        duration_detail_list: List[ReportDomainStreamDurationServiceResponseDataStreamListDurationDetailList] = None,
    ):
        # {"en":"domain + publishing point + stream name", "zh_CN":"流名(域名+发布点+流名)"}
        self.stream = stream
        # {"en":"The sum of the flow duration of the flow name in the corresponding time period, in milliseconds", "zh_CN":"对应时间段内流名推流时长之和,单位为毫秒"}
        self.sum_time = sum_time
        # {"en":"-", "zh_CN":"-"}
        self.duration_detail_list = duration_detail_list

    def validate(self):
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.sum_time, 'sum_time')
        self.validate_required(self.duration_detail_list, 'duration_detail_list')
        if self.duration_detail_list:
            for k in self.duration_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.sum_time is not None:
            result['sumTime'] = self.sum_time
        if self.duration_detail_list is not None:
            result['durationDetailList'] = []
            for k in self.duration_detail_list:
                result['durationDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('sumTime') is not None:
            self.sum_time = m.get('sumTime')
        if m.get('durationDetailList') is not None:
            self.duration_detail_list = []
            for k in m.get('durationDetailList'):
                temp_model = ReportDomainStreamDurationServiceResponseDataStreamListDurationDetailList()
                self.duration_detail_list.append(temp_model.from_map(k))
        return self


class ReportDomainStreamDurationServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream_list: List[ReportDomainStreamDurationServiceResponseDataStreamList] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"-", "zh_CN":"-"}
        self.stream_list = stream_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.stream_list, 'stream_list')
        if self.stream_list:
            for k in self.stream_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream_list is not None:
            result['streamList'] = []
            for k in self.stream_list:
                result['streamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('streamList') is not None:
            self.stream_list = []
            for k in m.get('streamList'):
                temp_model = ReportDomainStreamDurationServiceResponseDataStreamList()
                self.stream_list.append(temp_model.from_map(k))
        return self


class ReportDomainStreamDurationServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportDomainStreamDurationServiceResponseData] = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the result of the request", "zh_CN":"请求结果的详细数据"}
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
                temp_model = ReportDomainStreamDurationServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainStreamDurationServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamDurationServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamDurationServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamDurationServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class FlowAppaChannelRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
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
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class FlowAppaChannelResponseProviderDateTotal(TeaModel):
    def __init__(
        self,
        name: str = None,
        edgeup: str = None,
        edgedown: str = None,
        total: str = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'edgeup', 'zh_CN':'边缘上行总流量,单位Mbps'}
        self.edgeup = edgeup
        # {'en':'edgedown', 'zh_CN':'边缘下行总流量,单位Mbps'}
        self.edgedown = edgedown
        # {'en':'total', 'zh_CN':'汇总'}
        self.total = total

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.edgeup, 'edgeup')
        self.validate_required(self.edgedown, 'edgedown')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.edgeup is not None:
            result['edgeup'] = self.edgeup
        if self.edgedown is not None:
            result['edgedown'] = self.edgedown
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('edgeup') is not None:
            self.edgeup = m.get('edgeup')
        if m.get('edgedown') is not None:
            self.edgedown = m.get('edgedown')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class FlowAppaChannelResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        edgeup: str = None,
        edgedown: str = None,
        total: str = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'edgeup', 'zh_CN':'边缘上行总流量,单位Mbps'}
        self.edgeup = edgeup
        # {'en':'edgedown', 'zh_CN':'边缘下行总流量,单位Mbps'}
        self.edgedown = edgedown
        # {'en':'total', 'zh_CN':'汇总'}
        self.total = total

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.edgeup, 'edgeup')
        self.validate_required(self.edgedown, 'edgedown')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.edgeup is not None:
            result['edgeup'] = self.edgeup
        if self.edgedown is not None:
            result['edgedown'] = self.edgedown
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('edgeup') is not None:
            self.edgeup = m.get('edgeup')
        if m.get('edgedown') is not None:
            self.edgedown = m.get('edgedown')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class FlowAppaChannelResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        total: FlowAppaChannelResponseProviderDateTotal = None,
        channel: FlowAppaChannelResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'total', 'zh_CN':'汇总'}
        self.total = total
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.total, 'total')
        if self.total:
            self.total.validate()
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.total is not None:
            result['total'] = self.total.to_map()
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('total') is not None:
            temp_model = FlowAppaChannelResponseProviderDateTotal()
            self.total = temp_model.from_map(m['total'])
        if m.get('channel') is not None:
            temp_model = FlowAppaChannelResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class FlowAppaChannelResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: FlowAppaChannelResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'请求数数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = FlowAppaChannelResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class FlowAppaChannelResponse(TeaModel):
    def __init__(
        self,
        provider: FlowAppaChannelResponseProvider = None,
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
            temp_model = FlowAppaChannelResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class FlowAppaChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowAppaChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowAppaChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class FlowAppaChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportUrlDlFinishServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        url: str = None,
    ):
        # {'en':'Start time
        # 
        # 1.         The   format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.         Must   be a time that is 183 days earlier than the current time, and the time must   be earlier than the current time and dateTo;
        # 
        # 3.         Period   between dataFrom and dateTo cannot be longer than 7 days;
        # 
        # 4.         dateFrom   and dateTo can be either both are specified or neither is specifies;
        # 
        # 5.         If   neither dateFrom nor dateTo is specified, then by default, data in the last   24 hour is queried', 'zh_CN':'开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于当前时间-183天，并且小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过7天；（可联系技术支持调整）
        # 4.dateFrom和dateTo要么都传递，要么都不传递；
        # 5.dateFrom和dateTo都未传递，则默认查询过去24小时的数据'}
        self.date_from = date_from
        # {'en':'End time
        # 
        # 1.         The   format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 
        # 2.         Must   be greater than dateFrom; if it&rsquo;s greater than the current time, then the   current time is assigned as the value;', 'zh_CN':'结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；如果大于当前时间，则重新赋值为当前时间；'}
        self.date_to = date_to
        # {'en':'Domain names, domain number   limits can be adjusted depending on different accounts. The default value is   20', 'zh_CN':'域名，域名个数限制根据账号可调，默认为20个'}
        self.domain = domain
        # {'en':'url：
        # 1. fuzzy matching is supported.
        # 2.Several are separated by ','.', 'zh_CN':'url：
        # 1.支持模糊匹配。
        # 2.多个用 '，'隔开。'}
        self.url = url

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ReportUrlDlFinishServiceResponseResult(TeaModel):
    def __init__(
        self,
        url: str = None,
        num: str = None,
    ):
        # {'en':'The top500 of url', 'zh_CN':'top500的url'}
        self.url = url
        # {'en':'Number of successful downloads', 'zh_CN':'下载成功数'}
        self.num = num

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.num, 'num')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.num is not None:
            result['num'] = self.num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('num') is not None:
            self.num = m.get('num')
        return self


class ReportUrlDlFinishServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportUrlDlFinishServiceResponseResult] = None,
    ):
        # {'en':'-', 'zh_CN':'请求结果的详细数据'}
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
                temp_model = ReportUrlDlFinishServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportUrlDlFinishServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlDlFinishServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlDlFinishServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportUrlDlFinishServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryDDoSMitigatedBandwidthBySuiteOrProductRequest(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        package_id: str = None,
        need_detail: int = None,
        enddate: str = None,
        custom_code: str = None,
        acctype: str = None,
        contract_id: str = None,
    ):
        # {"en":"Start time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"开始时间，yyyy-MM-dd HH:mm:ss。"}
        self.startdate = startdate
        # {"en":"PackageId or acctype should be selected at least one.", "zh_CN":"套餐ID: packageId和acctype至少传一个,但不能同时传。"}
        self.package_id = package_id
        # {"en":"need Detail : 1
        # no need Detail: 0
        # default : 1.", "zh_CN":"是否需要查看域名或是转发规则带宽的详细信息：0：不需要；1：需要，默认需要。"}
        self.need_detail = need_detail
        # {"en":"End time, yyyy-MM-dd HH:mm:ss.", "zh_CN":"结束时间，yyyy-MM-dd HH:mm:ss。"}
        self.enddate = enddate
        # {"en":"Customer English Name.", "zh_CN":"客户英文名。"}
        self.custom_code = custom_code
        # {"en":"PackageId or acctype should be selected at least one.
        # acctype( Only One can be selected): gess, fsa, app-s, dms-https, wss, dms, wss-https, s-appa, esa, wsa-https, 1551.", "zh_CN":"PackageId和acctype不能同时传且至少传一个；产品外部服务类型,只支持传1个:gess，fsa，app-s，dms-https，wss, dms， wss-https，s-appa，esa，wsa-https，1551。"}
        self.acctype = acctype
        # {"en":"ContractId", "zh_CN":"合同号  
        # 支持按Contract# item#粒度查询
        # 当ContractId不为空时，会替换掉packageId"}
        self.contract_id = contract_id

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.custom_code, 'custom_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.package_id is not None:
            result['packageId'] = self.package_id
        if self.need_detail is not None:
            result['needDetail'] = self.need_detail
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.acctype is not None:
            result['acctype'] = self.acctype
        if self.contract_id is not None:
            result['ContractId'] = self.contract_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('packageId') is not None:
            self.package_id = m.get('packageId')
        if m.get('needDetail') is not None:
            self.need_detail = m.get('needDetail')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('acctype') is not None:
            self.acctype = m.get('acctype')
        if m.get('ContractId') is not None:
            self.contract_id = m.get('ContractId')
        return self


class QueryDDoSMitigatedBandwidthBySuiteOrProductResponse(TeaModel):
    def __init__(
        self,
        msg: str = None,
        at_bw: str = None,
        peak_stat: str = None,
        code: str = None,
    ):
        # {"en":"错误信息或Success。", "zh_CN":"Error message or Success."}
        self.msg = msg
        # {"en":"CleanBandwidth:
        #     time: "2018-08-21 00:00:00"
        #    atFlow: cleaned bandwidth Mbps", "zh_CN":"带宽信息： 
        # Time："2018-08-21 00:00:00"
        # atFlow：已清洗的带宽　Mbps"}
        self.at_bw = at_bw
        # {"en":"peak information:
        #    peakTime: "2018-08-21 00:00:00"
        #    peakValue:  peak of Clean Bandwidth (Mbps)
        #    mitigatedTraffic: Cleaned flow (GB)", "zh_CN":"峰值统计信息：
        # peakTime：峰值时间 "2018-08-21 00:00:00"
        # peakValue：DDoS攻击峰值带宽Mbps
        # mitigatedTraffic：已清洗的流量 GB"}
        self.peak_stat = peak_stat
        # {"en":"Return 200 means success, please see <Error code> to check other status code.", "zh_CN":"200状态码表示请求成功，其他状态码说明请参见《错误码》。"}
        self.code = code

    def validate(self):
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.at_bw, 'at_bw')
        self.validate_required(self.peak_stat, 'peak_stat')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.at_bw is not None:
            result['at_bw'] = self.at_bw
        if self.peak_stat is not None:
            result['peakStat'] = self.peak_stat
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('at_bw') is not None:
            self.at_bw = m.get('at_bw')
        if m.get('peakStat') is not None:
            self.peak_stat = m.get('peakStat')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class QueryDDoSMitigatedBandwidthBySuiteOrProductPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDDoSMitigatedBandwidthBySuiteOrProductParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDDoSMitigatedBandwidthBySuiteOrProductRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryDDoSMitigatedBandwidthBySuiteOrProductResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CloudDirectDurationRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        region: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
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
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.region is not None:
            result['region'] = self.region
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class CloudDirectDurationResponseProviderDateResultDuration(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'明细数据'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class CloudDirectDurationResponseProviderDateResult(TeaModel):
    def __init__(
        self,
        duration: List[CloudDirectDurationResponseProviderDateResultDuration] = None,
    ):
        # {'en':'duration', 'zh_CN':'明细数据'}
        self.duration = duration

    def validate(self):
        self.validate_required(self.duration, 'duration')
        if self.duration:
            for k in self.duration:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = []
            for k in self.duration:
                result['duration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = []
            for k in m.get('duration'):
                temp_model = CloudDirectDurationResponseProviderDateResultDuration()
                self.duration.append(temp_model.from_map(k))
        return self


class CloudDirectDurationResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        total_duration: str = None,
        result: CloudDirectDurationResponseProviderDateResult = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'totalDuration', 'zh_CN':'汇总'}
        self.total_duration = total_duration
        # {'en':'result', 'zh_CN':'明细数据'}
        self.result = result

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.total_duration, 'total_duration')
        self.validate_required(self.result, 'result')
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.total_duration is not None:
            result['totalDuration'] = self.total_duration
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('totalDuration') is not None:
            self.total_duration = m.get('totalDuration')
        if m.get('result') is not None:
            temp_model = CloudDirectDurationResponseProviderDateResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CloudDirectDurationResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: CloudDirectDurationResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'明细数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = CloudDirectDurationResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class CloudDirectDurationResponse(TeaModel):
    def __init__(
        self,
        provider: CloudDirectDurationResponseProvider = None,
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
            temp_model = CloudDirectDurationResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class CloudDirectDurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CloudDirectDurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CloudDirectDurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CloudDirectDurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BandwidthUploadRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        flow_type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1)optional values:xml, json.
        # 2)'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Bandwidth types.
        # 1)optional values:edgeUp,midUp.
        # 2)If there are multiple inpus,use ';' as delemeter.", "zh_CN":"带宽类型：edgeUp：边缘上行, midUp：中间上行, 多个类型以英文分号';'分隔. 空默认为边缘上行(edgeUp)"}
        self.flow_type = flow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.flow_type is not None:
            result['flowType'] = self.flow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('flowType') is not None:
            self.flow_type = m.get('flowType')
        return self


class BandwidthUploadResponseProviderDateChannelBandwidth(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'带宽'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class BandwidthUploadResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        bandwidth: List[BandwidthUploadResponseProviderDateChannelBandwidth] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'带宽数据'}
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.bandwidth, 'bandwidth')
        if self.bandwidth:
            for k in self.bandwidth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = []
            for k in self.bandwidth:
                result['bandwidth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = []
            for k in m.get('bandwidth'):
                temp_model = BandwidthUploadResponseProviderDateChannelBandwidth()
                self.bandwidth.append(temp_model.from_map(k))
        return self


class BandwidthUploadResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: BandwidthUploadResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = BandwidthUploadResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class BandwidthUploadResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: BandwidthUploadResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'频道带宽数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = BandwidthUploadResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class BandwidthUploadResponse(TeaModel):
    def __init__(
        self,
        provider: BandwidthUploadResponseProvider = None,
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
            temp_model = BandwidthUploadResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class BandwidthUploadPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthUploadParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthUploadRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BandwidthUploadResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class HttpTestRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        area: str = None,
        isp: str = None,
    ):
        # {"en":"URL", "zh_CN":"指定检测的 URL"}
        self.url = url
        # {"en":"area", "zh_CN":"监控机所属地区中文名称，支持中国大陆省份、港澳台以及海外国家。
        # 可选值：
        # anhui: 安徽
        # beijing: 北京
        # chongqing: 重庆
        # fujian: 福建
        # gansu: 甘肃
        # guangdong: 广东
        # guangxi: 广西
        # guizhou: 贵州
        # hainan: 海南
        # hebei: 河北
        # heilongjiang: 黑龙江
        # henan: 河南
        # hubei: 湖北
        # hunan: 湖南
        # jiangsu: 江苏
        # jiangxi: 江西
        # jilin: 吉林
        # liaoning: 辽宁
        # neimenggu: 内蒙古
        # ningxia: 宁夏
        # qinghai: 青海
        # shaanxi: 陕西
        # shandong: 山东
        # shanghai: 上海
        # shanxi: 山西
        # sichuan: 四川
        # tianjin: 天津
        # xinjiang: 新疆
        # xizang: 西藏
        # yunnan: 云南
        # zhejiang: 浙江
        # TW: 台湾
        # HK: 香港
        # MO: 澳门
        # AE: 阿联酋
        # AU: 澳大利亚
        # BD: 孟加拉
        # BN: 文莱
        # BR: 巴西
        # CA: 加拿大
        # CL: 智利
        # CO: 哥伦比亚
        # DJ: 吉布提
        # ID: 印度尼西亚
        # IT: 意大利
        # JP: 日本
        # KG: 吉尔吉斯斯坦
        # KH: 柬埔寨
        # KR: 韩国
        # KW: 科威特
        # LA: 老挝
        # MG: 马达加斯加
        # MM: 缅甸
        # MU: 毛里求斯
        # MY: 马来西亚
        # NP: 尼泊尔
        # OM: 阿曼
        # PE: 秘鲁
        # PH: 菲律宾
        # PK: 巴基斯坦
        # QA: 卡塔尔
        # RO: 罗马尼亚
        # RU: 俄罗斯
        # SA: 沙特阿拉伯
        # SE: 瑞典
        # SG: 新加坡
        # TH: 泰国
        # TR: 土耳其
        # US: 美国
        # VN: 越南"}
        self.area = area
        # {"en":"isp", "zh_CN":"监控机所属运营商中文名。
        # 可选值：
        # 0: 中国电信
        # 1: 中国联通
        # 2: 中国铁通
        # 4: 中国移动
        # 5: 中国教育网
        # 9: 中国广电
        # 10: 长城宽带"}
        self.isp = isp

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.area, 'area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.area is not None:
            result['area'] = self.area
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class HttpTestResponseResultData(TeaModel):
    def __init__(
        self,
        id: str = None,
        task_id: str = None,
        url: str = None,
        detect_ip: str = None,
        detect_ip_isp: str = None,
        detect_ip_isp_code: str = None,
        detect_ip_pro: str = None,
        detect_ip_pro_code: str = None,
        target_ip: str = None,
        target_ip_isp: str = None,
        target_ip_pro: str = None,
        target_location: str = None,
        dns_ip: str = None,
        connect_time: int = None,
        dns_time: int = None,
        redirect_time: int = None,
        response_time: int = None,
        use_time: int = None,
        done_time: int = None,
        error_code: str = None,
        file_size: int = None,
        rate: float = None,
        http_code: str = None,
        request_header: str = None,
        response_header: str = None,
        status: int = None,
    ):
        # {'en':'id', 'zh_CN':'任务 ID'}
        self.id = id
        # {'en':'task id', 'zh_CN':'任务 ID'}
        self.task_id = task_id
        # {'en':'url', 'zh_CN':'目标 URL'}
        self.url = url
        # {'en':'monitor ip', 'zh_CN':'监控机 IP'}
        self.detect_ip = detect_ip
        # {'en':'monitor isp', 'zh_CN':'监控机运营商'}
        self.detect_ip_isp = detect_ip_isp
        # {'en':'monitor isp code', 'zh_CN':'监控机运营商编码'}
        self.detect_ip_isp_code = detect_ip_isp_code
        # {'en':'monitor province', 'zh_CN':'监控机所属省份'}
        self.detect_ip_pro = detect_ip_pro
        # {'en':'monitor province code', 'zh_CN':'监控机所属省份编码'}
        self.detect_ip_pro_code = detect_ip_pro_code
        # {'en':'target ip', 'zh_CN':'探测目标 IP'}
        self.target_ip = target_ip
        # {'en':'target isp', 'zh_CN':'探测目标运营商'}
        self.target_ip_isp = target_ip_isp
        # {'en':'tartget province', 'zh_CN':'探测目标所属省份'}
        self.target_ip_pro = target_ip_pro
        # {'en':'target province and isp', 'zh_CN':'探测目标省份运营商'}
        self.target_location = target_location
        # {'en':'dns', 'zh_CN':'DNS'}
        self.dns_ip = dns_ip
        # {'en':'connect time', 'zh_CN':'建联耗时，单位：毫秒'}
        self.connect_time = connect_time
        # {'en':'dns time', 'zh_CN':'DNS 查询耗时，单位：毫秒'}
        self.dns_time = dns_time
        # {'en':'http redirect time', 'zh_CN':'重定向耗时，单位：毫秒'}
        self.redirect_time = redirect_time
        # {'en':'response time', 'zh_CN':'响应耗时，单位：毫秒'}
        self.response_time = response_time
        # {'en':'all time', 'zh_CN':'探测总耗时，单位：毫秒'}
        self.use_time = use_time
        # {'en':'end time', 'zh_CN':'探测结束时间戳'}
        self.done_time = done_time
        # {'en':'error code', 'zh_CN':'错误码'}
        self.error_code = error_code
        # {'en':'file size', 'zh_CN':'下载文件大小，单位：Byte'}
        self.file_size = file_size
        # {'en':'download rate', 'zh_CN':'下载速率，单位：KBytes/s'}
        self.rate = rate
        # {'en':'http status code', 'zh_CN':'HTTP 状态码'}
        self.http_code = http_code
        # {'en':'http request header', 'zh_CN':'请求头'}
        self.request_header = request_header
        # {'en':'http response header', 'zh_CN':'响应头'}
        self.response_header = response_header
        # {'en':'status', 'zh_CN':'探测状态'}
        self.status = status

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.url, 'url')
        self.validate_required(self.detect_ip, 'detect_ip')
        self.validate_required(self.detect_ip_isp, 'detect_ip_isp')
        self.validate_required(self.detect_ip_isp_code, 'detect_ip_isp_code')
        self.validate_required(self.detect_ip_pro, 'detect_ip_pro')
        self.validate_required(self.detect_ip_pro_code, 'detect_ip_pro_code')
        self.validate_required(self.target_ip, 'target_ip')
        self.validate_required(self.target_ip_isp, 'target_ip_isp')
        self.validate_required(self.target_ip_pro, 'target_ip_pro')
        self.validate_required(self.target_location, 'target_location')
        self.validate_required(self.dns_ip, 'dns_ip')
        self.validate_required(self.connect_time, 'connect_time')
        self.validate_required(self.dns_time, 'dns_time')
        self.validate_required(self.redirect_time, 'redirect_time')
        self.validate_required(self.response_time, 'response_time')
        self.validate_required(self.use_time, 'use_time')
        self.validate_required(self.done_time, 'done_time')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.http_code, 'http_code')
        self.validate_required(self.request_header, 'request_header')
        self.validate_required(self.response_header, 'response_header')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.url is not None:
            result['url'] = self.url
        if self.detect_ip is not None:
            result['detectIp'] = self.detect_ip
        if self.detect_ip_isp is not None:
            result['detectIpIsp'] = self.detect_ip_isp
        if self.detect_ip_isp_code is not None:
            result['detectIpIspCode'] = self.detect_ip_isp_code
        if self.detect_ip_pro is not None:
            result['detectIpPro'] = self.detect_ip_pro
        if self.detect_ip_pro_code is not None:
            result['detectIpProCode'] = self.detect_ip_pro_code
        if self.target_ip is not None:
            result['targetIp'] = self.target_ip
        if self.target_ip_isp is not None:
            result['targetIpIsp'] = self.target_ip_isp
        if self.target_ip_pro is not None:
            result['targetIpPro'] = self.target_ip_pro
        if self.target_location is not None:
            result['targetLocation'] = self.target_location
        if self.dns_ip is not None:
            result['dnsIp'] = self.dns_ip
        if self.connect_time is not None:
            result['connectTime'] = self.connect_time
        if self.dns_time is not None:
            result['dnsTime'] = self.dns_time
        if self.redirect_time is not None:
            result['redirectTime'] = self.redirect_time
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.use_time is not None:
            result['useTime'] = self.use_time
        if self.done_time is not None:
            result['doneTime'] = self.done_time
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.rate is not None:
            result['rate'] = self.rate
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_header is not None:
            result['requestHeader'] = self.request_header
        if self.response_header is not None:
            result['responseHeader'] = self.response_header
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('detectIp') is not None:
            self.detect_ip = m.get('detectIp')
        if m.get('detectIpIsp') is not None:
            self.detect_ip_isp = m.get('detectIpIsp')
        if m.get('detectIpIspCode') is not None:
            self.detect_ip_isp_code = m.get('detectIpIspCode')
        if m.get('detectIpPro') is not None:
            self.detect_ip_pro = m.get('detectIpPro')
        if m.get('detectIpProCode') is not None:
            self.detect_ip_pro_code = m.get('detectIpProCode')
        if m.get('targetIp') is not None:
            self.target_ip = m.get('targetIp')
        if m.get('targetIpIsp') is not None:
            self.target_ip_isp = m.get('targetIpIsp')
        if m.get('targetIpPro') is not None:
            self.target_ip_pro = m.get('targetIpPro')
        if m.get('targetLocation') is not None:
            self.target_location = m.get('targetLocation')
        if m.get('dnsIp') is not None:
            self.dns_ip = m.get('dnsIp')
        if m.get('connectTime') is not None:
            self.connect_time = m.get('connectTime')
        if m.get('dnsTime') is not None:
            self.dns_time = m.get('dnsTime')
        if m.get('redirectTime') is not None:
            self.redirect_time = m.get('redirectTime')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('useTime') is not None:
            self.use_time = m.get('useTime')
        if m.get('doneTime') is not None:
            self.done_time = m.get('doneTime')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestHeader') is not None:
            self.request_header = m.get('requestHeader')
        if m.get('responseHeader') is not None:
            self.response_header = m.get('responseHeader')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class HttpTestResponseResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_msg: str = None,
        test_id: str = None,
        url: str = None,
        data: List[HttpTestResponseResultData] = None,
    ):
        # {'en':'status', 'zh_CN':'状态码'}
        self.status = status
        # {'en':'error message', 'zh_CN':'异常信息'}
        self.error_msg = error_msg
        # {'en':'test id', 'zh_CN':'任务 ID'}
        self.test_id = test_id
        # {'en':'url', 'zh_CN':'目标 URL'}
        self.url = url
        # {'en':'data','zh_CN':'探测数据'}
        self.data = data

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.error_msg, 'error_msg')
        self.validate_required(self.test_id, 'test_id')
        self.validate_required(self.url, 'url')
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
        if self.status is not None:
            result['status'] = self.status
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.test_id is not None:
            result['testId'] = self.test_id
        if self.url is not None:
            result['url'] = self.url
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('testId') is not None:
            self.test_id = m.get('testId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = HttpTestResponseResultData()
                self.data.append(temp_model.from_map(k))
        return self


class HttpTestResponse(TeaModel):
    def __init__(
        self,
        result: HttpTestResponseResult = None,
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
            temp_model = HttpTestResponseResult()
            self.result = temp_model.from_map(m['result'])
        return self


class HttpTestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpTestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpTestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpTestResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class Query5minLiveTranscodingDurationRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        channel: str = None,
        is_exact_match: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
        transcode_type: str = None,
        definition: str = None,
        is_audio: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"This parameter specifies if the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"acceleration type:
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way.
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"Transcoding type, values can be h264, h265, zdgq_264, zdgq_265, cf_264, cf_265, or other. Multiple transcoding types should be separated by a semicolon. If some of the transcoding types are incorrect, the system will return data for the correct types; if all transcoding types are incorrect, it will return an error 'invalid transcodeType.' If not provided or left empty, it defaults to all types.", "zh_CN":"转码类型,值为h264、h265、zdgq_264、zdgq_265、cf_264、cf_265，other 多个转码类型用英文分号;分隔开。当传入转码类型部分错误时，返回正确的类型的数据；当传入转码类型全部错误时，返回错误invalid transcodeType. 不填或为空，默认为所有类型."}
        self.transcode_type = transcode_type
        # {"en":"Resolution types include LD480, SD720, HD1080, 2K, 4K, 8K, SD576. Multiple resolutions are separated by a semicolon. When isAudio=1, this parameter is invalid and will return an error. Param definition must be empty when querying audio data.", "zh_CN":"清晰度类型,值为LD480、SD720、HD1080、2K、4K、8K、SD576，多个清晰度用英文分号;分隔开, 当isAudio=1时，此入参无效返回错误 param definition must be empty when query audio data."}
        self.definition = definition
        # {"en":"Audio/Video Type, 1: Audio 2: Video. Defaults to 2 if not selected or empty. Only a single value is allowed.", "zh_CN":"音视频类型, 1:音频   2:视频. 不选或者为空时默认为2. 只能输入单个值."}
        self.is_audio = is_audio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.transcode_type is not None:
            result['transcodeType'] = self.transcode_type
        if self.definition is not None:
            result['definition'] = self.definition
        if self.is_audio is not None:
            result['isAudio'] = self.is_audio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('transcodeType') is not None:
            self.transcode_type = m.get('transcodeType')
        if m.get('definition') is not None:
            self.definition = m.get('definition')
        if m.get('isAudio') is not None:
            self.is_audio = m.get('isAudio')
        return self


class Query5minLiveTranscodingDurationResponseProviderDateTranscodingLive(TeaModel):
    def __init__(
        self,
        time: str = None,
        h_264: str = None,
        h_265: str = None,
        zdgq__264: str = None,
        zdgq__265: str = None,
        voice: str = None,
        cf__264: str = None,
        cf__265: str = None,
        definition__2k: str = None,
        definition__4k: str = None,
        definition__8k: str = None,
        definition__ld480: str = None,
        definition__sd720: str = None,
        definition__hd1080: str = None,
        definition__sd576: str = None,
        total: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'h264 transcoding time', 'zh_CN':'h264转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.h_264 = h_264
        # {'en':'h265 transcoding time', 'zh_CN':'h265转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.h_265 = h_265
        # {'en':'zdgq_264 transcoding time', 'zh_CN':'zdgq_264转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.zdgq__264 = zdgq__264
        # {'en':'zdgq_265 transcoding time', 'zh_CN':'zdgq_265转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.zdgq__265 = zdgq__265
        # {'en':'voice transcoding time', 'zh_CN':'voice转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.voice = voice
        # {'en':'cf_264 transcoding time', 'zh_CN':'cf_264转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.cf__264 = cf__264
        # {'en':'cf_265 transcoding time', 'zh_CN':'cf_265转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.cf__265 = cf__265
        # {'en':'definition_2K transcoding time', 'zh_CN':'definition_2K转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__2k = definition__2k
        # {'en':'definition_4K transcoding time', 'zh_CN':'definition_4K转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__4k = definition__4k
        # {'en':'definition_8K transcoding time', 'zh_CN':'definition_8K转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__8k = definition__8k
        # {'en':'definition_LD480 transcoding time', 'zh_CN':'definition_LD480转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__ld480 = definition__ld480
        # {'en':'definition_SD720 transcoding time', 'zh_CN':'definition_SD720转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__sd720 = definition__sd720
        # {'en':'definition_HD1080 transcoding time', 'zh_CN':'definition_HD1080转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__hd1080 = definition__hd1080
        # {'en':'definition_SD576 transcoding time', 'zh_CN':'definition_SD576转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.definition__sd576 = definition__sd576
        # {'en':'total transcoding time', 'zh_CN':'总转码类型的转码时长(单位分钟，固定保留2位小数)'}
        self.total = total

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.h_264, 'h_264')
        self.validate_required(self.h_265, 'h_265')
        self.validate_required(self.zdgq__264, 'zdgq__264')
        self.validate_required(self.zdgq__265, 'zdgq__265')
        self.validate_required(self.voice, 'voice')
        self.validate_required(self.cf__264, 'cf__264')
        self.validate_required(self.cf__265, 'cf__265')
        self.validate_required(self.definition__2k, 'definition__2k')
        self.validate_required(self.definition__4k, 'definition__4k')
        self.validate_required(self.definition__8k, 'definition__8k')
        self.validate_required(self.definition__ld480, 'definition__ld480')
        self.validate_required(self.definition__sd720, 'definition__sd720')
        self.validate_required(self.definition__hd1080, 'definition__hd1080')
        self.validate_required(self.definition__sd576, 'definition__sd576')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.h_264 is not None:
            result['h264'] = self.h_264
        if self.h_265 is not None:
            result['h265'] = self.h_265
        if self.zdgq__264 is not None:
            result['zdgq_264'] = self.zdgq__264
        if self.zdgq__265 is not None:
            result['zdgq_265'] = self.zdgq__265
        if self.voice is not None:
            result['voice'] = self.voice
        if self.cf__264 is not None:
            result['cf_264'] = self.cf__264
        if self.cf__265 is not None:
            result['cf_265'] = self.cf__265
        if self.definition__2k is not None:
            result['definition_2K'] = self.definition__2k
        if self.definition__4k is not None:
            result['definition_4K'] = self.definition__4k
        if self.definition__8k is not None:
            result['definition_8K'] = self.definition__8k
        if self.definition__ld480 is not None:
            result['definition_LD480'] = self.definition__ld480
        if self.definition__sd720 is not None:
            result['definition_SD720'] = self.definition__sd720
        if self.definition__hd1080 is not None:
            result['definition_HD1080'] = self.definition__hd1080
        if self.definition__sd576 is not None:
            result['definition_SD576'] = self.definition__sd576
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('h264') is not None:
            self.h_264 = m.get('h264')
        if m.get('h265') is not None:
            self.h_265 = m.get('h265')
        if m.get('zdgq_264') is not None:
            self.zdgq__264 = m.get('zdgq_264')
        if m.get('zdgq_265') is not None:
            self.zdgq__265 = m.get('zdgq_265')
        if m.get('voice') is not None:
            self.voice = m.get('voice')
        if m.get('cf_264') is not None:
            self.cf__264 = m.get('cf_264')
        if m.get('cf_265') is not None:
            self.cf__265 = m.get('cf_265')
        if m.get('definition_2K') is not None:
            self.definition__2k = m.get('definition_2K')
        if m.get('definition_4K') is not None:
            self.definition__4k = m.get('definition_4K')
        if m.get('definition_8K') is not None:
            self.definition__8k = m.get('definition_8K')
        if m.get('definition_LD480') is not None:
            self.definition__ld480 = m.get('definition_LD480')
        if m.get('definition_SD720') is not None:
            self.definition__sd720 = m.get('definition_SD720')
        if m.get('definition_HD1080') is not None:
            self.definition__hd1080 = m.get('definition_HD1080')
        if m.get('definition_SD576') is not None:
            self.definition__sd576 = m.get('definition_SD576')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class Query5minLiveTranscodingDurationResponseProviderDateTranscoding(TeaModel):
    def __init__(
        self,
        name: str = None,
        live: List[Query5minLiveTranscodingDurationResponseProviderDateTranscodingLive] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'live', 'zh_CN':'直播转码时长数据'}
        self.live = live

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.live, 'live')
        if self.live:
            for k in self.live:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.live is not None:
            result['live'] = []
            for k in self.live:
                result['live'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('live') is not None:
            self.live = []
            for k in m.get('live'):
                temp_model = Query5minLiveTranscodingDurationResponseProviderDateTranscodingLive()
                self.live.append(temp_model.from_map(k))
        return self


class Query5minLiveTranscodingDurationResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        transcoding: Query5minLiveTranscodingDurationResponseProviderDateTranscoding = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'transcoding', 'zh_CN':'转码类型'}
        self.transcoding = transcoding

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.transcoding, 'transcoding')
        if self.transcoding:
            self.transcoding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.transcoding is not None:
            result['transcoding'] = self.transcoding.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('transcoding') is not None:
            temp_model = Query5minLiveTranscodingDurationResponseProviderDateTranscoding()
            self.transcoding = temp_model.from_map(m['transcoding'])
        return self


class Query5minLiveTranscodingDurationResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: Query5minLiveTranscodingDurationResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'直播转码时长数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = Query5minLiveTranscodingDurationResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class Query5minLiveTranscodingDurationResponse(TeaModel):
    def __init__(
        self,
        provider: Query5minLiveTranscodingDurationResponseProvider = None,
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
            temp_model = Query5minLiveTranscodingDurationResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class Query5minLiveTranscodingDurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class Query5minLiveTranscodingDurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class Query5minLiveTranscodingDurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class Query5minLiveTranscodingDurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PicProcessStatisticsRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        region: str = None,
        dataformat: str = None,
        result_type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope.
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way:
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        return self


class PicProcessStatisticsResponseProviderDateChannelPicflowhit(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'请求数'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class PicProcessStatisticsResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        picflowhit: List[PicProcessStatisticsResponseProviderDateChannelPicflowhit] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'picflowhit', 'zh_CN':'请求数数据'}
        self.picflowhit = picflowhit

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.picflowhit, 'picflowhit')
        if self.picflowhit:
            for k in self.picflowhit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.picflowhit is not None:
            result['picflowhit'] = []
            for k in self.picflowhit:
                result['picflowhit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('picflowhit') is not None:
            self.picflowhit = []
            for k in m.get('picflowhit'):
                temp_model = PicProcessStatisticsResponseProviderDateChannelPicflowhit()
                self.picflowhit.append(temp_model.from_map(k))
        return self


class PicProcessStatisticsResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: PicProcessStatisticsResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = PicProcessStatisticsResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class PicProcessStatisticsResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: PicProcessStatisticsResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'明细数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.result_type, 'result_type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('date') is not None:
            temp_model = PicProcessStatisticsResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class PicProcessStatisticsResponse(TeaModel):
    def __init__(
        self,
        provider: PicProcessStatisticsResponseProvider = None,
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
            temp_model = PicProcessStatisticsResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class PicProcessStatisticsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PicProcessStatisticsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PicProcessStatisticsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PicProcessStatisticsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainStreamHlsOnlineServiceRequestDomainStream(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream: List[str] = None,
    ):
        # {"en":"domian", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"stream: 'publishing point'/'stream'; 
        # 					For example: live/test-20200101-test.flv ,'live' is the publishing point, 'test-20200101-test' is stream;
        # 					If the stream is not transmitted, all stream under the domain will be queried by default", "zh_CN":"流名:发布点/流名。
        # 					例如:live/test-20200101-test.flv ,其中live是发布点, test-20200101-test是流名;
        # 					不传,默认查询指定域名下的所有流的数据"}
        self.stream = stream

    def validate(self):
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class ReportDomainStreamHlsOnlineServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain_stream: List[ReportDomainStreamHlsOnlineServiceRequestDomainStream] = None,
    ):
        # {"en":"Start time:
        # 1. Time format is yyyy-MM-ddTHH:mm:ss+08:00,
        # 2. No bigger than the current time.
        # 3. Data in the last 183 days at most can be queried.", "zh_CN":"开始时间:
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00
        # 2.不能大于当前时间
        # 3.最多可获取最近半年(183天)的数据"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The time format is yyyy-MM-ddTHH:mm:ss+08:00
        # 2. End time should be greater than start time. If the end time is greater than current time, current time will be used.
        # 3. If both fields of dataFrom and dateTo are left empty, then data in the last 10minutes will be queried by default; if only one field is filled in and one is left empty, then exception will be occur.
        # 4. Allowable maximum time range for query: 1 hour, means the period between dateFrom to dateTo should not exceed 1 hour (can be adjusted by contacting technical support).", "zh_CN":"结束时间:
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间,结束时间如果大于当前时间,取当前时间
        # 3.dateFrom,dateTo二者都未传,默认查询过去的10分钟;如仅有一个未传,抛异常
        # 4.允许查询最大时间间隔1小时:即dateFrom和dateTo相差不能超过1小时。(可联系技术支持调整)"}
        self.date_to = date_to
        # {"en":"Domain&stream group:
        # 1.Allowable maximum number of domain&stream group is 20 (can be adjusted by contacting technical support).
        # 2.Domain: a group of domain&stream only can include one domain,and the domain is required
        # 3.Stream:There is no limit on the number of stream names under a group of domain&stream. If the stream is not transmitted, all stream under the domain will be queried by default", "zh_CN":"域名和流名组:
        # 1.可传递的域名和流名组数量上限默认为20组(可联系技术支持调整);
        # 2.域名domain:一组域名和流名组中只能传递单个域名,且域名必须传递;
        # 3.流名stream:一组域名和流名组下(即单个域名下)不限制流名个数,流名未传递时默认查询域名下所有流名"}
        self.domain_stream = domain_stream

    def validate(self):
        self.validate_required(self.domain_stream, 'domain_stream')
        if self.domain_stream:
            for k in self.domain_stream:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain_stream is not None:
            result['domainStream'] = []
            for k in self.domain_stream:
                result['domainStream'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domainStream') is not None:
            self.domain_stream = []
            for k in m.get('domainStream'):
                temp_model = ReportDomainStreamHlsOnlineServiceRequestDomainStream()
                self.domain_stream.append(temp_model.from_map(k))
        return self


class ReportDomainStreamHlsOnlineServiceResponseDataStreamDetails(TeaModel):
    def __init__(
        self,
        stream: str = None,
        online_count: str = None,
    ):
        # {"en":"stream", "zh_CN":"流名"}
        self.stream = stream
        # {"en":"The number of online people corresponding to the stream", "zh_CN":"该流名对应的在线人数"}
        self.online_count = online_count

    def validate(self):
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.online_count, 'online_count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream is not None:
            result['stream'] = self.stream
        if self.online_count is not None:
            result['onlineCount'] = self.online_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('onlineCount') is not None:
            self.online_count = m.get('onlineCount')
        return self


class ReportDomainStreamHlsOnlineServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream_count: str = None,
        total_online_count: str = None,
        stream_details: List[ReportDomainStreamHlsOnlineServiceResponseDataStreamDetails] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Number of streams under domain name", "zh_CN":"域名下的流个数"}
        self.stream_count = stream_count
        # {"en":"The number of online people corresponding to the domain.The value is the cumulative number of online people of all stream under the domain", "zh_CN":"该频道下总的在线人数,值为频道下所有流名的在线人数累加"}
        self.total_online_count = total_online_count
        self.stream_details = stream_details

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.stream_count, 'stream_count')
        self.validate_required(self.total_online_count, 'total_online_count')
        self.validate_required(self.stream_details, 'stream_details')
        if self.stream_details:
            for k in self.stream_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream_count is not None:
            result['streamCount'] = self.stream_count
        if self.total_online_count is not None:
            result['totalOnlineCount'] = self.total_online_count
        if self.stream_details is not None:
            result['streamDetails'] = []
            for k in self.stream_details:
                result['streamDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('streamCount') is not None:
            self.stream_count = m.get('streamCount')
        if m.get('totalOnlineCount') is not None:
            self.total_online_count = m.get('totalOnlineCount')
        if m.get('streamDetails') is not None:
            self.stream_details = []
            for k in m.get('streamDetails'):
                temp_model = ReportDomainStreamHlsOnlineServiceResponseDataStreamDetails()
                self.stream_details.append(temp_model.from_map(k))
        return self


class ReportDomainStreamHlsOnlineServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportDomainStreamHlsOnlineServiceResponseData] = None,
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
                temp_model = ReportDomainStreamHlsOnlineServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportDomainStreamHlsOnlineServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamHlsOnlineServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamHlsOnlineServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainStreamHlsOnlineServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportDomainListExistFlowServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
    ):
        # {"en":"Start time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 1 days;4.You can only query data for the last 2 years.", "zh_CN":"开始时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须小于当前时间和dateTo;
        # 3.dateFrom和dateTo相差不能超过1天;
        # 4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time:
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;
        # 3.If it's greater than the current time, then the current time is assigned as the value;", "zh_CN":"结束时间:
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.必须大于dateFrom;
        # 3.如果大于当前时间,则重新赋值为当前时间;"}
        self.date_to = date_to

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        return self


class ReportDomainListExistFlowServiceResponse(TeaModel):
    def __init__(
        self,
        domain_num: int = None,
        domain_list: List[str] = None,
    ):
        # {"en":"Number of domains that have generated traffic", "zh_CN":"有量的域名数量"}
        self.domain_num = domain_num
        # {"en":"List of the domains that have generated traffic", "zh_CN":"有量的域名列表"}
        self.domain_list = domain_list

    def validate(self):
        self.validate_required(self.domain_num, 'domain_num')
        self.validate_required(self.domain_list, 'domain_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_num is not None:
            result['domainNum'] = self.domain_num
        if self.domain_list is not None:
            result['domainList'] = self.domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainNum') is not None:
            self.domain_num = m.get('domainNum')
        if m.get('domainList') is not None:
            self.domain_list = m.get('domainList')
        return self


class ReportDomainListExistFlowServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainListExistFlowServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainListExistFlowServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportDomainListExistFlowServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportStreamListServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: str = None,
    ):
        # {"en":"Start time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be smaller than the current time and dateTo;
        # 3.Period between dataFrom and dateTo cannot be longer than 3 days;4.You can only query data for the last 2 years.", "zh_CN":"开始时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须小于当前时间和dateTo；
        # 3.dateFrom和dateTo相差不能超过3天；
        # 4.只能查询最近2年内数据。"}
        self.date_from = date_from
        # {"en":"End time
        # 1.The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2.Must be greater than dateFrom;", "zh_CN":"结束时间
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.必须大于dateFrom；"}
        self.date_to = date_to
        # {"en":"Domain, must follow regular expression rule of (([\w-]{1,62})?(\.[\w-]{1,62})+)", "zh_CN":"域名，需要符合正则(([\w-]{1,62})?(\.[\w-]{1,62})+)"}
        self.domain = domain

    def validate(self):
        self.validate_required(self.date_from, 'date_from')
        self.validate_required(self.date_to, 'date_to')
        self.validate_required(self.domain, 'domain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ReportStreamListServiceResponseResult(TeaModel):
    def __init__(
        self,
        domain: str = None,
        stream_list: List[str] = None,
    ):
        # {"en":"Domain", "zh_CN":"域名"}
        self.domain = domain
        # {"en":"Domain list", "zh_CN":"流名列表"}
        self.stream_list = stream_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.stream_list, 'stream_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.stream_list is not None:
            result['streamList'] = self.stream_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('streamList') is not None:
            self.stream_list = m.get('streamList')
        return self


class ReportStreamListServiceResponse(TeaModel):
    def __init__(
        self,
        result: List[ReportStreamListServiceResponseResult] = None,
    ):
        # {"en":"", "zh_CN":""}
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
                temp_model = ReportStreamListServiceResponseResult()
                self.result.append(temp_model.from_map(k))
        return self


class ReportStreamListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamListServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportStreamListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryLiveRecordingDurationRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        timezone: str = None,
        channel: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期 ,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期 ,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"GMT time zone, parameter format: GMT+09:00 means east 9th zone, GMT-09:00 means west 9th zone, if not transmitted, the default is local time zone (east 8th zone).", "zh_CN":"格林尼治时区，参数格式 GMT+09:00 表示东九区，GMT-09:00 表示西9区，不传则默认为本地时区（东八区）"}
        self.timezone = timezone
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way
        # 1.If specified 1, get the merged result.
        # 2.If  specified 2,get the separate result.
        # 3.If specifed 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.channel is not None:
            result['channel'] = self.channel
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        return self


class QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannelLive(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'hit count', 'zh_CN':'明细数据'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        live: List[QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannelLive] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'明细数据'}
        self.live = live

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.live, 'live')
        if self.live:
            for k in self.live:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.live is not None:
            result['live'] = []
            for k in self.live:
                result['live'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('live') is not None:
            self.live = []
            for k in m.get('live'):
                temp_model = QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannelLive()
                self.live.append(temp_model.from_map(k))
        return self


class QueryLiveRecordingDurationResponseProviderDateRecordingTime(TeaModel):
    def __init__(
        self,
        name: str = None,
        channel: QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannel = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        self.channel = channel

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('channel') is not None:
            temp_model = QueryLiveRecordingDurationResponseProviderDateRecordingTimeChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class QueryLiveRecordingDurationResponseProviderDate(TeaModel):
    def __init__(
        self,
        start: str = None,
        end: str = None,
        recording_time: QueryLiveRecordingDurationResponseProviderDateRecordingTime = None,
    ):
        # {'en':'start', 'zh_CN':'开始时间'}
        self.start = start
        # {'en':'end', 'zh_CN':'结束时间'}
        self.end = end
        # {'en':'channel', 'zh_CN':'频道'}
        self.recording_time = recording_time

    def validate(self):
        self.validate_required(self.start, 'start')
        self.validate_required(self.end, 'end')
        self.validate_required(self.recording_time, 'recording_time')
        if self.recording_time:
            self.recording_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.recording_time is not None:
            result['recordingTime'] = self.recording_time.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('recordingTime') is not None:
            temp_model = QueryLiveRecordingDurationResponseProviderDateRecordingTime()
            self.recording_time = temp_model.from_map(m['recordingTime'])
        return self


class QueryLiveRecordingDurationResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: QueryLiveRecordingDurationResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'请明细数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.result_type, 'result_type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('date') is not None:
            temp_model = QueryLiveRecordingDurationResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class QueryLiveRecordingDurationResponse(TeaModel):
    def __init__(
        self,
        provider: QueryLiveRecordingDurationResponseProvider = None,
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
            temp_model = QueryLiveRecordingDurationResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class QueryLiveRecordingDurationPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveRecordingDurationParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveRecordingDurationRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveRecordingDurationResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class HttpDnsStatisticsRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        accetype: str = None,
        dataformat: str = None,
        is_exact_match: str = None,
        result_type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Querying date, the date format is yyyy-mm-dd, and the current date will be adopted by default if the field is not selected or left empty;", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"Querying start date, and the date format is yyyy-mm-dd.
        # The parameter needs to work in concert with enddate, and it will be invalid if there exists date parameter", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"Querying end date, and the date format is yyyy-mm-dd.
        # The parameter should work in concert with the parameter startdate. It will be invalid if there exists date parameter", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"Querying domain, and use English semicolon ;  as separator if there are multiple domains; all domains of the user will be queried if the field is not selected or left empty.", "zh_CN":"查询的频道，多个频道值请用英文分号;，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"查询域名所属的加速类型，如accetype=web。多个请用英文分号“;”分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"Response result format, and the supporting format is xml and json. Default as xml.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Whether the channel matches exactly: when true, the full domain name must be provided (at this point, any invalid or duplicate channels entered by the user will be filtered out, and a 403 error will be returned if all input channels are invalid). When not true, all channels ending with the user-entered channel are displayed. The default is true.", "zh_CN":" 频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"Whether the display of results includes merged values: Enter 1 to provide merged results; enter 2 to provide only split values; if not selected or left empty, the default is 1.", "zh_CN":"结果的显示是否提供合并值。填写1时：提供合并结果；填写2时：只提供拆分值；不选或者为空时默认为1。"}
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.result_type is not None:
            result['resultType'] = self.result_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        return self


class HttpDnsStatisticsResponseProviderDateChannelHttpdns(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点'}
        self.time = time
        # {'en':'bandwidth', 'zh_CN':'解析量'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class HttpDnsStatisticsResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        total: str = None,
        httpdns: List[HttpDnsStatisticsResponseProviderDateChannelHttpdns] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'total', 'zh_CN':'总解析量'}
        self.total = total
        # {'en':'httpdns', 'zh_CN':'解析量数据'}
        self.httpdns = httpdns

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.total, 'total')
        self.validate_required(self.httpdns, 'httpdns')
        if self.httpdns:
            for k in self.httpdns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.total is not None:
            result['total'] = self.total
        if self.httpdns is not None:
            result['httpdns'] = []
            for k in self.httpdns:
                result['httpdns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('httpdns') is not None:
            self.httpdns = []
            for k in m.get('httpdns'):
                temp_model = HttpDnsStatisticsResponseProviderDateChannelHttpdns()
                self.httpdns.append(temp_model.from_map(k))
        return self


class HttpDnsStatisticsResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: HttpDnsStatisticsResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = HttpDnsStatisticsResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class HttpDnsStatisticsResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: HttpDnsStatisticsResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'解析量数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.result_type, 'result_type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('date') is not None:
            temp_model = HttpDnsStatisticsResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class HttpDnsStatisticsResponse(TeaModel):
    def __init__(
        self,
        provider: HttpDnsStatisticsResponseProvider = None,
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
            temp_model = HttpDnsStatisticsResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class HttpDnsStatisticsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpDnsStatisticsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpDnsStatisticsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class HttpDnsStatisticsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class WafHitRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1)With format yyyy-mm-dd.
        # 2)If not specified,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1)Must work with 'enddate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd.
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期，日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1)Must work with 'startdate' and they  specify the query date scope. 
        # 2)With format yyyy-mm-dd
        # 3)If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1)If there are multiple inputs,use  ';' as separator.
        # 2)If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"This parameter specifies if the 'channel' parameter should be exactly matched:
        # 1)'true' as default.
        # 2) If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403)。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1)If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2)If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"acceleration type.
        # 1)If there are multiple inputs,use ';' as separator.
        # 2)If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
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
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        return self


class WafHitResponseProviderDateChannelWafhit(TeaModel):
    def __init__(
        self,
        time: str = None,
        text: str = None,
    ):
        # {'en':'time of every 5 duration,with format yyyy-mmm-dd hh:MM:ss', 'zh_CN':'waf请求数5分钟粒度时间，格式yyyy-mm-dd hh:MM:ss'}
        self.time = time
        # {'en':'displaying the waf request.', 'zh_CN':'waf请求数'}
        self.text = text

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class WafHitResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        wafhit: List[WafHitResponseProviderDateChannelWafhit] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'bandwidth', 'zh_CN':'waf 请求数数据'}
        self.wafhit = wafhit

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.wafhit, 'wafhit')
        if self.wafhit:
            for k in self.wafhit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.wafhit is not None:
            result['wafhit'] = []
            for k in self.wafhit:
                result['wafhit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('wafhit') is not None:
            self.wafhit = []
            for k in m.get('wafhit'):
                temp_model = WafHitResponseProviderDateChannelWafhit()
                self.wafhit.append(temp_model.from_map(k))
        return self


class WafHitResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: WafHitResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = WafHitResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class WafHitResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        date: WafHitResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'data', 'zh_CN':'waf 请求数数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            temp_model = WafHitResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class WafHitResponse(TeaModel):
    def __init__(
        self,
        provider: WafHitResponseProvider = None,
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
            temp_model = WafHitResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class WafHitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WafHitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WafHitRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WafHitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryLiveStreamStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveStreamStatusResponseDataValue(TeaModel):
    def __init__(
        self,
        streamname: str = None,
        deployaddress: str = None,
        inaddress: str = None,
        hists: int = None,
        inbandwidth: int = None,
        bandwidth: int = None,
        delay: int = None,
        fps: int = None,
        lfr: float = None,
        ofr: int = None,
        resolution: str = None,
        video_codec: str = None,
        audio_codec: str = None,
        gop: int = None,
    ):
        # {'en':'The channel of anchor', 'zh_CN':'主播流名'}
        self.streamname = streamname
        # {'en':'IP address of the CDN node', 'zh_CN':'推流cdn节点IP'}
        self.deployaddress = deployaddress
        # {'en':'Anchor exit Address', 'zh_CN':'主播出口地址'}
        self.inaddress = inaddress
        # {'en':'The number of online', 'zh_CN':'在线人数'}
        self.hists = hists
        # {'en':'Anchor Current bit rate (transcoding stream has no bit rate data) unit: BPS', 'zh_CN':'主播当前码率(转码流没有码率数据) 单位：bps'}
        self.inbandwidth = inbandwidth
        # {'en':'Channel current viewing bandwidth unit: BPS ', 'zh_CN':'频道当前观看带宽 单位：bps'}
        self.bandwidth = bandwidth
        # {'en':'Anchor delay (MS)', 'zh_CN':'主播延迟(ms)'}
        self.delay = delay
        # {'en':'Anchor Current encoding frame rate(fps)', 'zh_CN':'主播当前编码帧率(fps)'}
        self.fps = fps
        # {'en':'Current frame loss rate of anchor(fps)', 'zh_CN':'主播当前丢帧率(fps)'}
        self.lfr = lfr
        # {'en':'Anchor raw frame rate(fps)', 'zh_CN':'主播原始帧率(fps)'}
        self.ofr = ofr
        # {'en':'The resolution of the', 'zh_CN':'分辨率'}
        self.resolution = resolution
        # {'en':'Video coding', 'zh_CN':'视频编码'}
        self.video_codec = video_codec
        # {'en':'Audio coding', 'zh_CN':'音频编码'}
        self.audio_codec = audio_codec
        # {'en':'Keyframe interval', 'zh_CN':'关键帧间隔,有传expand才会返回'}
        self.gop = gop

    def validate(self):
        self.validate_required(self.streamname, 'streamname')
        self.validate_required(self.deployaddress, 'deployaddress')
        self.validate_required(self.inaddress, 'inaddress')
        self.validate_required(self.hists, 'hists')
        self.validate_required(self.inbandwidth, 'inbandwidth')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.delay, 'delay')
        self.validate_required(self.fps, 'fps')
        self.validate_required(self.lfr, 'lfr')
        self.validate_required(self.ofr, 'ofr')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.video_codec, 'video_codec')
        self.validate_required(self.audio_codec, 'audio_codec')
        self.validate_required(self.gop, 'gop')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.streamname is not None:
            result['streamname'] = self.streamname
        if self.deployaddress is not None:
            result['deployaddress'] = self.deployaddress
        if self.inaddress is not None:
            result['inaddress'] = self.inaddress
        if self.hists is not None:
            result['hists'] = self.hists
        if self.inbandwidth is not None:
            result['inbandwidth'] = self.inbandwidth
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.delay is not None:
            result['delay'] = self.delay
        if self.fps is not None:
            result['fps'] = self.fps
        if self.lfr is not None:
            result['lfr'] = self.lfr
        if self.ofr is not None:
            result['ofr'] = self.ofr
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.video_codec is not None:
            result['video_codec'] = self.video_codec
        if self.audio_codec is not None:
            result['audio_codec'] = self.audio_codec
        if self.gop is not None:
            result['gop'] = self.gop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('streamname') is not None:
            self.streamname = m.get('streamname')
        if m.get('deployaddress') is not None:
            self.deployaddress = m.get('deployaddress')
        if m.get('inaddress') is not None:
            self.inaddress = m.get('inaddress')
        if m.get('hists') is not None:
            self.hists = m.get('hists')
        if m.get('inbandwidth') is not None:
            self.inbandwidth = m.get('inbandwidth')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('delay') is not None:
            self.delay = m.get('delay')
        if m.get('fps') is not None:
            self.fps = m.get('fps')
        if m.get('lfr') is not None:
            self.lfr = m.get('lfr')
        if m.get('ofr') is not None:
            self.ofr = m.get('ofr')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('video_codec') is not None:
            self.video_codec = m.get('video_codec')
        if m.get('audio_codec') is not None:
            self.audio_codec = m.get('audio_codec')
        if m.get('gop') is not None:
            self.gop = m.get('gop')
        return self


class QueryLiveStreamStatusResponse(TeaModel):
    def __init__(
        self,
        rettime: str = None,
        retcode: int = None,
        histscount: int = None,
        bandwidthcount: int = None,
        datetime: int = None,
        data_value: List[QueryLiveStreamStatusResponseDataValue] = None,
    ):
        # {'en':'The time of the data returned', 'zh_CN':'返回的数据的时间'}
        self.rettime = rettime
        # {'en':'Number of data items. 0 is returned if there is no data', 'zh_CN':'数据条数，无数据返回0'}
        self.retcode = retcode
        # {'en':'Total onlines', 'zh_CN':'总在线人数'}
        self.histscount = histscount
        # {'en':'Total channel bandwidth', 'zh_CN':'总频道带宽'}
        self.bandwidthcount = bandwidthcount
        # {'en':'Timestamp', 'zh_CN':'数据的时间戳,如果有传t,则等于t'}
        self.datetime = datetime
        # {'en':'', 'zh_CN':'数据集合'}
        self.data_value = data_value

    def validate(self):
        self.validate_required(self.rettime, 'rettime')
        self.validate_required(self.retcode, 'retcode')
        self.validate_required(self.histscount, 'histscount')
        self.validate_required(self.bandwidthcount, 'bandwidthcount')
        self.validate_required(self.datetime, 'datetime')
        self.validate_required(self.data_value, 'data_value')
        if self.data_value:
            for k in self.data_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rettime is not None:
            result['rettime'] = self.rettime
        if self.retcode is not None:
            result['retcode'] = self.retcode
        if self.histscount is not None:
            result['histscount'] = self.histscount
        if self.bandwidthcount is not None:
            result['bandwidthcount'] = self.bandwidthcount
        if self.datetime is not None:
            result['datetime'] = self.datetime
        if self.data_value is not None:
            result['dataValue'] = []
            for k in self.data_value:
                result['dataValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rettime') is not None:
            self.rettime = m.get('rettime')
        if m.get('retcode') is not None:
            self.retcode = m.get('retcode')
        if m.get('histscount') is not None:
            self.histscount = m.get('histscount')
        if m.get('bandwidthcount') is not None:
            self.bandwidthcount = m.get('bandwidthcount')
        if m.get('datetime') is not None:
            self.datetime = m.get('datetime')
        if m.get('dataValue') is not None:
            self.data_value = []
            for k in m.get('dataValue'):
                temp_model = QueryLiveStreamStatusResponseDataValue()
                self.data_value.append(temp_model.from_map(k))
        return self


class QueryLiveStreamStatusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveStreamStatusParameters(TeaModel):
    def __init__(
        self,
        u: str = None,
        t: str = None,
        channel: str = None,
        d: str = None,
        showport: str = None,
        g: str = None,
        realtime: str = None,
        expand: str = None,
    ):
        # {'en':'Domain (multiple domains supported, separated by commas)', 'zh_CN':'域名（支持多个域名，以逗号分隔）'}
        self.u = u
        # {'en':'20160527152300, non-real-time indicates the current time -5 minutes, real-time indicates the current time -30 seconds
        # A:
        # (t is not transmitted, the current system time is obtained and rounded to second (for example, 2017/3/28 14:38:55 rounded to second 2017/3/28 14:38:50 rounded to second);) If the query interval g=10, the final time (dateFrom) is rounded in seconds (e.g. 2017/3/28 14:38:55 after rounded in seconds 2017/3/28 14:38:50); If the g! =10, rounded minutes: (e.g. 2017/3/28 14:38:55 rounded seconds 2017/3/28 14:38:00); DateTo = dataFrom + 9 (9 seconds)', 'zh_CN':'20160527152300，不填为当前时间-5分钟
        # 详解：
        # （t不传，获取当前系统时间，对秒取整(如：2017/3/28 14:38:55 对秒取整后2017/3/28 14:38:50)；）如果查询间隔g=10，最后获得的时间对秒取整(如：2017/3/28 14:38:55 对秒取整后2017/3/28 14:38:50)；如果g!=10，对分钟取整：(如：2017/3/28 14:38:55 对秒取整后2017/3/28 14:38:00);'}
        self.t = t
        # {'en':'Channel URL (simple channel url are supported,eg:push1.test.com/test/test1)', 'zh_CN':'流名(支持单流名，如：push1.test.com/test/test1)'}
        self.channel = channel
        # {'en':'Optional value: push or pull. The default value is push
        # Push stands for watershed name
        # Pull indicates the name of a pull basin', 'zh_CN':'域名类型，可选值：push、pull，默认push
        # push代表推流域名
        # pull代表拉流域名'}
        self.d = d
        # {'en':'The value can be true or false. The default value is false
        # Only realtime data is returned when realtime=true', 'zh_CN':'是否返回端口，可选值：true、false，默认false
        # '}
        self.showport = showport
        # {'en':'Query interval. The value can be 10 or 60. The default value is 60
        # When g is 10, query the data of the nearest whole 10 seconds to time t
        # When g is 60, query the data of the nearest whole minute to time t', 'zh_CN':'查询间隔，可选值10、60，默认60
        # 当g为10时，查询距离时间t最近的整10秒点数据
        # 当g为60时，查询距离时间t最近的整分钟点数据'}
        self.g = g
        # {'en':'it is query realtime datas,default false', 'zh_CN':'是否返回实时数据，默认false'}
        self.realtime = realtime
        # {'en':'Data extension fields(Only supports non-real-time query), providing optional return fields:gop', 'zh_CN':'数据扩展字段(仅支持按非实时查)，提供可选返回字段：gop'}
        self.expand = expand

    def validate(self):
        self.validate_required(self.u, 'u')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.u is not None:
            result['u'] = self.u
        if self.t is not None:
            result['t'] = self.t
        if self.channel is not None:
            result['channel'] = self.channel
        if self.d is not None:
            result['d'] = self.d
        if self.showport is not None:
            result['showport'] = self.showport
        if self.g is not None:
            result['g'] = self.g
        if self.realtime is not None:
            result['realtime'] = self.realtime
        if self.expand is not None:
            result['expand'] = self.expand
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('u') is not None:
            self.u = m.get('u')
        if m.get('t') is not None:
            self.t = m.get('t')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('d') is not None:
            self.d = m.get('d')
        if m.get('showport') is not None:
            self.showport = m.get('showport')
        if m.get('g') is not None:
            self.g = m.get('g')
        if m.get('realtime') is not None:
            self.realtime = m.get('realtime')
        if m.get('expand') is not None:
            self.expand = m.get('expand')
        return self


class QueryLiveStreamStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryLiveStreamStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class AttOverViewRequest(TeaModel):
    def __init__(
        self,
        cust: str = None,
        date: str = None,
        startdate: str = None,
        enddate: str = None,
        channel: str = None,
        is_exact_match: str = None,
        region: str = None,
        accetype: str = None,
        dataformat: str = None,
        result_type: str = None,
        attack_type: str = None,
    ):
        # {"en":"cust_en_name of sub-client.
        # When a merged-account wants to  view the information of the subclient,the cust_en_name is required.", "zh_CN":"合并账号下的某个客户的英文名，当合并账号要查看子客户的信息时，必须填写子客户的英文名"}
        self.cust = cust
        # {"en":"Specifies the query date:
        # 1.With format yyyy-mm-dd.
        # 2.If not Specifies,it means today as default.", "zh_CN":"查询的日期，日期格式为yyyy-mm-dd,不选或者为空时默认为当天；"}
        self.date = date
        # {"en":"1.Must work with 'enddate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的起始日期,日期格式为yyyy-mm-dd；此参数需与enddate参数配合,若存在date参数,则该参数无效"}
        self.startdate = startdate
        # {"en":"1.Must work with 'startdate' and they  specify the query date scope. 
        # 2.With format yyyy-mm-dd.
        # 3.If there is a 'date' parameter,this parameter will be omitted.", "zh_CN":"查询的结束日期,日期格式为yyyy-mm-dd；此参数需与startdate参数配合,若存在date参数,则该参数无效。"}
        self.enddate = enddate
        # {"en":"domains that been queried:
        # 1.If there are multiple inputs,use  ';' as separator.
        # 2.If not specified, it means all the domains of the account .", "zh_CN":"查询的频道，多个频道值请用英文分号';'，不选或者为空时默认为所查询客户的所有频道"}
        self.channel = channel
        # {"en":"Specifies if  the 'channel' parameter should be exactly matched:
        # 1.'true' as default.
        # 2. If not 'true',it will query data of channels that ends with any item of input 'channel's.", "zh_CN":"&nbsp;频道是否完全匹配,为true时，必须填写完整的域名(此时会过滤用户输入的无效或重复频道,所有输入频道都无效时返403.。不为true时，显示以用户输入的频道为结尾的所有频道。默认为true"}
        self.is_exact_match = is_exact_match
        # {"en":"1.If there are multiple inputs,use ';' as separator.For example,u can use 'region=cn;apac' to query data of cn and apac region.
        # 2.If not specified, it means all the regions.", "zh_CN":"查询的加速区域的缩写，多个区域请用英文分号';'分隔开，如查询大陆及亚太区域，参数填写为：'region=cn;apac'。不选或者为空时默认为全部区域。"}
        self.region = region
        # {"en":"Acceleration type.
        # 1.If there are multiple inputs,use ';' as separator.
        # 2.If not specified or specified as 'all', it means all the accetypes.", "zh_CN":"加速类型参数，如accetype=web。多个请用英文分号';'分隔开，不填或值为all表示所有类型"}
        self.accetype = accetype
        # {"en":"The response format:
        # 1.optional values:xml, json.
        # 2.'xml' as default.", "zh_CN":"返回结果格式,支持格式为xml和json,默认为xml"}
        self.dataformat = dataformat
        # {"en":"Display statistic result in merged or separate way.
        # 1.If specified 1,get the merged result.
        # 2.If specified 2,get the separate result.
        # 3.If specified 3,get both merged result and separate result.
        # 4.If not specified,means '1'.", "zh_CN":"&nbsp;结果的显示是否提供合并值。填写1时：只提供合并结果；填写2时：只提供拆分值；填写3时：既提供合并值，又提供拆分值。不选或者为空时默认为'1'。"}
        self.result_type = result_type
        # {"en":"attack Type.
        # 1.Including DDOS,WAF and BOT.
        # 2.inputs 'DDOS' matches 'DDOS' data,'BOT' matches 'BOT' data,and 'WAF' matches  all types started with 'WAF'.
        # 3.If there are multiple  inputss,use english ';' as separator.
        # 4.If not specified,means all the types.", "zh_CN":"攻击类型DDOS、WAF或BOT。填写DDOS时匹配DDOS数据，填写WAF时匹配WAF_xxx数据，填写BOT时匹配BOT数据，多个类型之间用英文分号;隔开;不填或放空默认为全部类型"}
        self.attack_type = attack_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cust is not None:
            result['cust'] = self.cust
        if self.date is not None:
            result['date'] = self.date
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel
        if self.is_exact_match is not None:
            result['isExactMatch'] = self.is_exact_match
        if self.region is not None:
            result['region'] = self.region
        if self.accetype is not None:
            result['accetype'] = self.accetype
        if self.dataformat is not None:
            result['dataformat'] = self.dataformat
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cust') is not None:
            self.cust = m.get('cust')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('isExactMatch') is not None:
            self.is_exact_match = m.get('isExactMatch')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('accetype') is not None:
            self.accetype = m.get('accetype')
        if m.get('dataformat') is not None:
            self.dataformat = m.get('dataformat')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        return self


class AttOverViewResponseProviderDateChannelOverView(TeaModel):
    def __init__(
        self,
        channel: str = None,
        hit: str = None,
        deny: str = None,
    ):
        # {'en':'timestamp', 'zh_CN':'时间点，格式 yyyy-MM-dd hh:mm:ss'}
        self.channel = channel
        # {'en':'total request number.', 'zh_CN':'总请求数'}
        self.hit = hit
        # {'en':'total denied request number.', 'zh_CN':'总访问拒绝数'}
        self.deny = deny

    def validate(self):
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.hit, 'hit')
        self.validate_required(self.deny, 'deny')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.hit is not None:
            result['hit'] = self.hit
        if self.deny is not None:
            result['deny'] = self.deny
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('hit') is not None:
            self.hit = m.get('hit')
        if m.get('deny') is not None:
            self.deny = m.get('deny')
        return self


class AttOverViewResponseProviderDateChannel(TeaModel):
    def __init__(
        self,
        name: str = None,
        over_view: List[AttOverViewResponseProviderDateChannelOverView] = None,
    ):
        # {'en':'channel', 'zh_CN':'频道'}
        self.name = name
        # {'en':'overview', 'zh_CN':'安全防护安全状况汇总数据'}
        self.over_view = over_view

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.over_view, 'over_view')
        if self.over_view:
            for k in self.over_view:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.over_view is not None:
            result['over-view'] = []
            for k in self.over_view:
                result['over-view'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('over-view') is not None:
            self.over_view = []
            for k in m.get('over-view'):
                temp_model = AttOverViewResponseProviderDateChannelOverView()
                self.over_view.append(temp_model.from_map(k))
        return self


class AttOverViewResponseProviderDate(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        channel: AttOverViewResponseProviderDateChannel = None,
    ):
        # {'en':'startdate', 'zh_CN':'开始时间'}
        self.startdate = startdate
        # {'en':'enddate', 'zh_CN':'结束时间'}
        self.enddate = enddate
        # {'en':'channel', 'zh_CN':'频道'}
        self.channel = channel

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')
        self.validate_required(self.channel, 'channel')
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.channel is not None:
            result['channel'] = self.channel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('channel') is not None:
            temp_model = AttOverViewResponseProviderDateChannel()
            self.channel = temp_model.from_map(m['channel'])
        return self


class AttOverViewResponseProvider(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        result_type: str = None,
        date: AttOverViewResponseProviderDate = None,
    ):
        # {'en':'tenant', 'zh_CN':'租户'}
        self.name = name
        # {'en':'type', 'zh_CN':'接口类型'}
        self.type = type
        # {'en':'resultType', 'zh_CN':'统计类型'}
        self.result_type = result_type
        # {'en':'data', 'zh_CN':'安全防护安全状况汇总数据'}
        self.date = date

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.result_type, 'result_type')
        self.validate_required(self.date, 'date')
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.result_type is not None:
            result['resultType'] = self.result_type
        if self.date is not None:
            result['date'] = self.date.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        if m.get('date') is not None:
            temp_model = AttOverViewResponseProviderDate()
            self.date = temp_model.from_map(m['date'])
        return self


class AttOverViewResponse(TeaModel):
    def __init__(
        self,
        provider: AttOverViewResponseProvider = None,
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
            temp_model = AttOverViewResponseProvider()
            self.provider = temp_model.from_map(m['provider'])
        return self


class AttOverViewPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AttOverViewParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AttOverViewRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AttOverViewResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ReportBandwidthLowDelayP2pServiceRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        domain: List[str] = None,
        group_by: List[str] = None,
    ):
        # {'en':'-', 'zh_CN':'开始时间：
        # 1.时间格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2021-05-19T10:00:00+08:00（为北京时间2021年5月19日10点0分0秒）
        # 2.不能大于当前时间
        # 3.最多可获取最近半年（183天）的数据'}
        self.date_from = date_from
        # {'en':'-', 'zh_CN':'结束时间：
        # 1.时间格式yyyy-MM-ddTHH:mm:ss+08:00
        # 2.结束时间需大于开始时间，结束时间如果大于当前时间，取当前时间
        # 3.dateFrom，dateTo二者都未传，默认查询过去的1小时；如仅有一个未传，抛异常
        # 4.允许查询最大时间间隔：1天，即dateFrom和dateTo相差不能超过1天。（可联系技术支持调整）'}
        self.date_to = date_to
        # {'en':'-', 'zh_CN':'域名：
        # 1、可传递域名数量上限默认为20个（可联系技术支持调整）；
        # 2、自动过滤掉无效域名（如传递非法域名，会被过滤掉，查询结果只返回有效域名的数据）。'}
        self.domain = domain
        # {'en':'-', 'zh_CN':'可选值：domain
        # 不传默认聚合所有频道数据'}
        self.group_by = group_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.domain is not None:
            result['domain'] = self.domain
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class ReportBandwidthLowDelayP2pServiceResponseDataDetailList(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # {'en':'-', 'zh_CN':'时间片,返回开始时间和结束时间包含的时间片。时间格式：yyyy-MM-dd HH:mm'}
        self.timestamp = timestamp
        # {'en':'-', 'zh_CN':'P2P带宽'}
        self.value = value

    def validate(self):
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ReportBandwidthLowDelayP2pServiceResponseData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        detail_list: List[ReportBandwidthLowDelayP2pServiceResponseDataDetailList] = None,
    ):
        # {'en':'-', 'zh_CN':'域名，聚合全部域名数据不返回该字段'}
        self.domain = domain
        # {'en':'-', 'zh_CN':'请求结果的详细数据'}
        self.detail_list = detail_list

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.detail_list, 'detail_list')
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.detail_list is not None:
            result['detailList'] = []
            for k in self.detail_list:
                result['detailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('detailList') is not None:
            self.detail_list = []
            for k in m.get('detailList'):
                temp_model = ReportBandwidthLowDelayP2pServiceResponseDataDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class ReportBandwidthLowDelayP2pServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: List[ReportBandwidthLowDelayP2pServiceResponseData] = None,
    ):
        # {'en':'-', 'zh_CN':'请求结果状态码'}
        self.code = code
        # {'en':'-', 'zh_CN':'请求结果信息'}
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
                temp_model = ReportBandwidthLowDelayP2pServiceResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class ReportBandwidthLowDelayP2pServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthLowDelayP2pServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthLowDelayP2pServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ReportBandwidthLowDelayP2pServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DnsTestRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        dns_type: str = None,
        dns_server: str = None,
        area: str = None,
        isp: str = None,
    ):
        # {"en":"Domain name or IP to be detected", "zh_CN":"需要检测的域名或 IP"}
        self.host = host
        # {"en":"DNS record type, optional values: A, CNAME, SOA, TXT, MX, NS", "zh_CN":"DNS 记录类型，可选值：A、CNAME、SOA、TXT、MX、NS"}
        self.dns_type = dns_type
        # {"en":"Specify a DNS server, such as 8.8.8.8", "zh_CN":"指定 DNS 服务器，如 114.114.114.114"}
        self.dns_server = dns_server
        # {"en":"The region of the monitor belongs to, supports mainland China provinces, Hong Kong, Macao and Taiwan, as well as overseas countries.
        # optional values:, anhui, beijing, chongqing, fujian, gansu, guangdong, guangxi, guizhou, hainan, hebei, heilongjiang, henan, hubei, hunan, jiangsu, jiangxi, jilin, liaoning, neimenggu, ningxia, qinghai, shaanxi, shandong, shanghai, shanxi, sichuan, tianjin, xinjiang, xizang, yunnan, zhejiang, TW, HK, MO, AE, AU, BD, BN, BR, CA, CL, CO, DJ, ID, IT, JP, KG, KH, KR, KW, LA, MG, MM, MU, MY, NP, OM, PE, PH, PK, QA, RO, RU, SA, SE, SG, TH, TR, US, VN", "zh_CN":"监控机所属地区，支持中国大陆省份、港澳台以及海外国家。
        # 可选值：
        # anhui: 安徽
        # beijing: 北京
        # chongqing: 重庆
        # fujian: 福建
        # gansu: 甘肃
        # guangdong: 广东
        # guangxi: 广西
        # guizhou: 贵州
        # hainan: 海南
        # hebei: 河北
        # heilongjiang: 黑龙江
        # henan: 河南
        # hubei: 湖北
        # hunan: 湖南
        # jiangsu: 江苏
        # jiangxi: 江西
        # jilin: 吉林
        # liaoning: 辽宁
        # neimenggu: 内蒙古
        # ningxia: 宁夏
        # qinghai: 青海
        # shaanxi: 陕西
        # shandong: 山东
        # shanghai: 上海
        # shanxi: 山西
        # sichuan: 四川
        # tianjin: 天津
        # xinjiang: 新疆
        # xizang: 西藏
        # yunnan: 云南
        # zhejiang: 浙江
        # TW: 台湾
        # HK: 香港
        # MO: 澳门
        # AE: 阿联酋
        # AU: 澳大利亚
        # BD: 孟加拉
        # BN: 文莱
        # BR: 巴西
        # CA: 加拿大
        # CL: 智利
        # CO: 哥伦比亚
        # DJ: 吉布提
        # ID: 印度尼西亚
        # IT: 意大利
        # JP: 日本
        # KG: 吉尔吉斯斯坦
        # KH: 柬埔寨
        # KR: 韩国
        # KW: 科威特
        # LA: 老挝
        # MG: 马达加斯加
        # MM: 缅甸
        # MU: 毛里求斯
        # MY: 马来西亚
        # NP: 尼泊尔
        # OM: 阿曼
        # PE: 秘鲁
        # PH: 菲律宾
        # PK: 巴基斯坦
        # QA: 卡塔尔
        # RO: 罗马尼亚
        # RU: 俄罗斯
        # SA: 沙特阿拉伯
        # SE: 瑞典
        # SG: 新加坡
        # TH: 泰国
        # TR: 土耳其
        # US: 美国
        # VN: 越南"}
        self.area = area
        # {"en":"ISP
        # optional values: 
        # 0: China-Telecom
        # 1: China-Unicom
        # 2: China-Tietong
        # 4: China-Mobile
        # 5: China-Education-and-Research
        # 9: China-Cable-Television
        # 10: GreatWall-Broadband", "zh_CN":"监控机所属运营商中文名。
        # 可选值：
        # 0: 中国电信
        # 1: 中国联通
        # 2: 中国铁通
        # 4: 中国移动
        # 5: 中国教育网
        # 9: 中国广电
        # 10: 长城宽带"}
        self.isp = isp

    def validate(self):
        self.validate_required(self.host, 'host')
        self.validate_required(self.dns_type, 'dns_type')
        self.validate_required(self.dns_server, 'dns_server')
        self.validate_required(self.area, 'area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.dns_type is not None:
            result['dnsType'] = self.dns_type
        if self.dns_server is not None:
            result['dnsServer'] = self.dns_server
        if self.area is not None:
            result['area'] = self.area
        if self.isp is not None:
            result['isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('dnsType') is not None:
            self.dns_type = m.get('dnsType')
        if m.get('dnsServer') is not None:
            self.dns_server = m.get('dnsServer')
        if m.get('area') is not None:
            self.area = m.get('area')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        return self


class DnsTestResponseResultDataAnswerList(TeaModel):
    def __init__(
        self,
        id: str = None,
        test_id: str = None,
        address: str = None,
        dns_class: str = None,
        dns_type: str = None,
        result: str = None,
        ttl: int = None,
    ):
        # {'en':'id','zh_CN':'ID'}
        self.id = id
        # {'en':'tess id','zh_CN':'任务 ID'}
        self.test_id = test_id
        # {'en':'isp','zh_CN':'记录所属地区运营商'}
        self.address = address
        # {'en':'dns class','zh_CN':'DNS 记录'}
        self.dns_class = dns_class
        # {'en':'dns type','zh_CN':'DNS 记录类型'}
        self.dns_type = dns_type
        # {'en':'dns record','zh_CN':'DNS 记录值'}
        self.result = result
        # {'en':'time to live', 'zh_CN':'TTL'}
        self.ttl = ttl

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.test_id, 'test_id')
        self.validate_required(self.address, 'address')
        self.validate_required(self.dns_class, 'dns_class')
        self.validate_required(self.dns_type, 'dns_type')
        self.validate_required(self.result, 'result')
        self.validate_required(self.ttl, 'ttl')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.test_id is not None:
            result['testId'] = self.test_id
        if self.address is not None:
            result['address'] = self.address
        if self.dns_class is not None:
            result['dnsClass'] = self.dns_class
        if self.dns_type is not None:
            result['dnsType'] = self.dns_type
        if self.result is not None:
            result['result'] = self.result
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('testId') is not None:
            self.test_id = m.get('testId')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('dnsClass') is not None:
            self.dns_class = m.get('dnsClass')
        if m.get('dnsType') is not None:
            self.dns_type = m.get('dnsType')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class DnsTestResponseResultData(TeaModel):
    def __init__(
        self,
        id: str = None,
        task_id: str = None,
        question_url: str = None,
        detect_ip: str = None,
        detect_ip_isp: str = None,
        detect_ip_isp_code: str = None,
        detect_ip_pro: str = None,
        detect_ip_pro_code: str = None,
        server: str = None,
        detect_time: str = None,
        done_time: int = None,
        query_time: int = None,
        status: int = None,
        status_code: str = None,
        answer: str = None,
        answer_list: List[DnsTestResponseResultDataAnswerList] = None,
    ):
        # {'en':'task id', 'zh_CN':'任务 ID'}
        self.id = id
        # {'en':'task id', 'zh_CN':'任务 ID'}
        self.task_id = task_id
        # {'en':'domain', 'zh_CN':'目标域名'}
        self.question_url = question_url
        # {'en':'monitor IP', 'zh_CN':'监控机 IP'}
        self.detect_ip = detect_ip
        # {'en':'monitor ISP', 'zh_CN':'监控机运营商'}
        self.detect_ip_isp = detect_ip_isp
        # {'en':'monitor ISP', 'zh_CN':'监控机运营商编码'}
        self.detect_ip_isp_code = detect_ip_isp_code
        # {'en':'monitor province', 'zh_CN':'监控机所属省份'}
        self.detect_ip_pro = detect_ip_pro
        # {'en':'monitor province code', 'zh_CN':'监控机所属省份编码'}
        self.detect_ip_pro_code = detect_ip_pro_code
        # {'en':'dns server', 'zh_CN':'DNS'}
        self.server = server
        # {'en':'time', 'zh_CN':'探测时间'}
        self.detect_time = detect_time
        # {'en':'end time', 'zh_CN':'探测结束时间戳'}
        self.done_time = done_time
        # {'en':'dns query time', 'zh_CN':'查询耗时，单位：毫秒'}
        self.query_time = query_time
        # {'en':'status', 'zh_CN':'探测状态'}
        self.status = status
        # {'en':'status code', 'zh_CN':'HTTP 状态码'}
        self.status_code = status_code
        # {'en':'dns answer', 'zh_CN':'DNS'}
        self.answer = answer
        # {'en':'dns result','zh_CN':'解析结果'}
        self.answer_list = answer_list

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.question_url, 'question_url')
        self.validate_required(self.detect_ip, 'detect_ip')
        self.validate_required(self.detect_ip_isp, 'detect_ip_isp')
        self.validate_required(self.detect_ip_isp_code, 'detect_ip_isp_code')
        self.validate_required(self.detect_ip_pro, 'detect_ip_pro')
        self.validate_required(self.detect_ip_pro_code, 'detect_ip_pro_code')
        self.validate_required(self.server, 'server')
        self.validate_required(self.detect_time, 'detect_time')
        self.validate_required(self.done_time, 'done_time')
        self.validate_required(self.query_time, 'query_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.answer, 'answer')
        self.validate_required(self.answer_list, 'answer_list')
        if self.answer_list:
            for k in self.answer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.question_url is not None:
            result['questionUrl'] = self.question_url
        if self.detect_ip is not None:
            result['detectIp'] = self.detect_ip
        if self.detect_ip_isp is not None:
            result['detectIpIsp'] = self.detect_ip_isp
        if self.detect_ip_isp_code is not None:
            result['detectIpIspCode'] = self.detect_ip_isp_code
        if self.detect_ip_pro is not None:
            result['detectIpPro'] = self.detect_ip_pro
        if self.detect_ip_pro_code is not None:
            result['detectIpProCode'] = self.detect_ip_pro_code
        if self.server is not None:
            result['server'] = self.server
        if self.detect_time is not None:
            result['detectTime'] = self.detect_time
        if self.done_time is not None:
            result['doneTime'] = self.done_time
        if self.query_time is not None:
            result['queryTime'] = self.query_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.answer is not None:
            result['answer'] = self.answer
        if self.answer_list is not None:
            result['answerList'] = []
            for k in self.answer_list:
                result['answerList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('questionUrl') is not None:
            self.question_url = m.get('questionUrl')
        if m.get('detectIp') is not None:
            self.detect_ip = m.get('detectIp')
        if m.get('detectIpIsp') is not None:
            self.detect_ip_isp = m.get('detectIpIsp')
        if m.get('detectIpIspCode') is not None:
            self.detect_ip_isp_code = m.get('detectIpIspCode')
        if m.get('detectIpPro') is not None:
            self.detect_ip_pro = m.get('detectIpPro')
        if m.get('detectIpProCode') is not None:
            self.detect_ip_pro_code = m.get('detectIpProCode')
        if m.get('server') is not None:
            self.server = m.get('server')
        if m.get('detectTime') is not None:
            self.detect_time = m.get('detectTime')
        if m.get('doneTime') is not None:
            self.done_time = m.get('doneTime')
        if m.get('queryTime') is not None:
            self.query_time = m.get('queryTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('answerList') is not None:
            self.answer_list = []
            for k in m.get('answerList'):
                temp_model = DnsTestResponseResultDataAnswerList()
                self.answer_list.append(temp_model.from_map(k))
        return self


class DnsTestResponseResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_msg: str = None,
        test_id: str = None,
        host: str = None,
        data: List[DnsTestResponseResultData] = None,
    ):
        # {'en':'status', 'zh_CN':'状态码'}
        self.status = status
        # {'en':'error message', 'zh_CN':'错误信息'}
        self.error_msg = error_msg
        # {'en':'test id', 'zh_CN':'任务 ID'}
        self.test_id = test_id
        # {'en':'domain', 'zh_CN':'目标域名'}
        self.host = host
        # {'en':'data','zh_CN':'探测数据'}
        self.data = data

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.error_msg, 'error_msg')
        self.validate_required(self.test_id, 'test_id')
        self.validate_required(self.host, 'host')
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
        if self.status is not None:
            result['status'] = self.status
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.test_id is not None:
            result['testId'] = self.test_id
        if self.host is not None:
            result['host'] = self.host
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('testId') is not None:
            self.test_id = m.get('testId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = DnsTestResponseResultData()
                self.data.append(temp_model.from_map(k))
        return self


class DnsTestResponse(TeaModel):
    def __init__(
        self,
        result: DnsTestResponseResult = None,
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
            temp_model = DnsTestResponseResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DnsTestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DnsTestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DnsTestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DnsTestResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryOnlineViewerCountRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOnlineViewerCountResponseDataValue(TeaModel):
    def __init__(
        self,
        prog: str = None,
        time: str = None,
        value: int = None,
        error_value: int = None,
    ):
        # {'en':'Stream name', 'zh_CN':'流名'}
        self.prog = prog
        # {'en':'Time is displayed only if the query time range (channel, FROM, and to parameters) is not empty', 'zh_CN':'时间，仅当查询时间范围，即channel，from和to参数不为空时才显示'}
        self.time = time
        # {'en':'The number of online', 'zh_CN':'在线人数'}
        self.value = value
        # {'en':'Abnormal online number, only need customers return', 'zh_CN':'异常在线人数，只对需要客户进行返回'}
        self.error_value = error_value

    def validate(self):
        self.validate_required(self.prog, 'prog')
        self.validate_required(self.time, 'time')
        self.validate_required(self.value, 'value')
        self.validate_required(self.error_value, 'error_value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prog is not None:
            result['prog'] = self.prog
        if self.time is not None:
            result['time'] = self.time
        if self.value is not None:
            result['value'] = self.value
        if self.error_value is not None:
            result['errorValue'] = self.error_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prog') is not None:
            self.prog = m.get('prog')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('errorValue') is not None:
            self.error_value = m.get('errorValue')
        return self


class QueryOnlineViewerCountResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        error_count: int = None,
        retcode: int = None,
        rettime: str = None,
        data_value: List[QueryOnlineViewerCountResponseDataValue] = None,
    ):
        # {'en':'Total number of online users. This parameter is displayed only when from and to are empty', 'zh_CN':'在线总人数，仅当查询时间点，即from和to为空时才显示'}
        self.count = count
        # {'en':'Total abnormal online number, only need customers return', 'zh_CN':'异常总在线人数，只对有需要客户进行返回'}
        self.error_count = error_count
        # {'en':'The number of data items is displayed only when from and to are empty.', 'zh_CN':'数据条数，仅当查询时间点，即from和to为空时才显示'}
        self.retcode = retcode
        # {'en':'The time of the data returned', 'zh_CN':'返回的数据的时间'}
        self.rettime = rettime
        # {'en':'', 'zh_CN':'数据集合'}
        self.data_value = data_value

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.error_count, 'error_count')
        self.validate_required(self.retcode, 'retcode')
        self.validate_required(self.rettime, 'rettime')
        self.validate_required(self.data_value, 'data_value')
        if self.data_value:
            for k in self.data_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.retcode is not None:
            result['retcode'] = self.retcode
        if self.rettime is not None:
            result['rettime'] = self.rettime
        if self.data_value is not None:
            result['dataValue'] = []
            for k in self.data_value:
                result['dataValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('retcode') is not None:
            self.retcode = m.get('retcode')
        if m.get('rettime') is not None:
            self.rettime = m.get('rettime')
        if m.get('dataValue') is not None:
            self.data_value = []
            for k in m.get('dataValue'):
                temp_model = QueryOnlineViewerCountResponseDataValue()
                self.data_value.append(temp_model.from_map(k))
        return self


class QueryOnlineViewerCountPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOnlineViewerCountParameters(TeaModel):
    def __init__(
        self,
        u: str = None,
        t: str = None,
        d: str = None,
        channel: str = None,
        from_: str = None,
        to: str = None,
        g: str = None,
        realtime: str = None,
        unpack: str = None,
    ):
        # {'en':'Domain (multiple domains supported, separated by commas)', 'zh_CN':'域名（支持多个域名，以逗号分隔）'}
        self.u = u
        # {'en':'Time,eg:20160527152300.If the parameter is not specified, the value is 3 minutes', 'zh_CN':'时间，eg：20160527152300，不填为当前时间-3分钟'}
        self.t = t
        # {'en':'The domain type can be pull or push. If this parameter is not specified, the default value is pull', 'zh_CN':'域名类型，pull或push，不填时默认为pull'}
        self.d = d
        # {'en':'Channel URL(single channel query only),It is not recommended to query with this parameter, and the performance of range query is poor.', 'zh_CN':'频道URL(仅支持单频道查询),不建议带该参数查询，范围查询性能较差'}
        self.channel = channel
        # {'en':'Start time, eg: 20160803103500, when both from and to are filled or left blank, channel parameter is mandatory. The query time span is two hours at most. If the query time exceeds two hours, the system queries the data within two hours from the start time and the number of online users within the last 7 days', 'zh_CN':'开始时间，eg: 20160803103500，from和to都填或都不填，都填时channel参数必填，查询时间跨度最大为两个小时，如果超过两个小时，将查询开始时间两个小时内的数据，可查近7天内在线人数数据'}
        self.from_ = from_
        # {'en':'End time, eg: 20160803103900, when both from and to are filled or left blank, channel parameter is mandatory. The query time span is two hours at most. If the query time exceeds two hours, the system queries the data within two hours from the start time and the number of online users in the last 7 days', 'zh_CN':'结束时间，eg: 20160803103900，from和to都填或都不填，都填时channel参数必填，查询时间跨度最大为两个小时，如果超过两个小时，将查询开始时间两个小时内的数据，可查近7天内在线人数数据'}
        self.to = to
        # {'en':'Query interval, optional value: 10, 60s.
        # When g is 10, the number of online users every 10 seconds is queried;
        # When g is 60, the number of online users at the whole minute within the time range is queried.', 'zh_CN':'查询间隔，可选值10、60s，
        # 当g为10时，查询时间范围内每10秒的在线人数
        # 当g为60时，查询时间范围内整分钟点对应的在线人数'}
        self.g = g
        # {'en':'it is query realtime datas,default false', 'zh_CN':'是否返回实时数据，默认false'}
        self.realtime = realtime
        # {'en':'The default value is false. If the value is true, the domain data is split. If the value is false, the domain data is merged', 'zh_CN':'域名拆分控制，默认为false，为true时，拆分域名数据，为false时，合并域名数据'}
        self.unpack = unpack

    def validate(self):
        self.validate_required(self.u, 'u')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.u is not None:
            result['u'] = self.u
        if self.t is not None:
            result['t'] = self.t
        if self.d is not None:
            result['d'] = self.d
        if self.channel is not None:
            result['channel'] = self.channel
        if self.from_ is not None:
            result['from'] = self.from_
        if self.to is not None:
            result['to'] = self.to
        if self.g is not None:
            result['g'] = self.g
        if self.realtime is not None:
            result['realtime'] = self.realtime
        if self.unpack is not None:
            result['unpack'] = self.unpack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('u') is not None:
            self.u = m.get('u')
        if m.get('t') is not None:
            self.t = m.get('t')
        if m.get('d') is not None:
            self.d = m.get('d')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('g') is not None:
            self.g = m.get('g')
        if m.get('realtime') is not None:
            self.realtime = m.get('realtime')
        if m.get('unpack') is not None:
            self.unpack = m.get('unpack')
        return self


class QueryOnlineViewerCountRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOnlineViewerCountResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




