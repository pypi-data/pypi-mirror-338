# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryRefreshPageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        status: List[str] = None,
        start_time: str = None,
        end_time: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # {"en":"query url", "zh_CN":"查询的 URL"}
        self.url = url
        # {"en":"refresh status 1- wait; 2- success; 3- fail;", "zh_CN":"刷新状态 1 -表示待刷新; 2 -刷新成功; 3- 刷新失败;"}
        self.status = status
        # {"en":"Start Time; yyyy-mm-dd hh:mm:ss.", "zh_CN":"开始时间; yyyy-mm-dd hh:mm:ss."}
        self.start_time = start_time
        # {"en":"end Time;yyyy-mm-dd hh:mm:ss.", "zh_CN":"结束时间;yyyy-mm-dd hh:mm:ss."}
        self.end_time = end_time
        # {"en":"page Num", "zh_CN":"当前页"}
        self.page_num = page_num
        # {"en":"Page Size", "zh_CN":"每页记录数"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.status is not None:
            result['status'] = self.status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryRefreshPageRefreshSiteLog(TeaModel):
    def __init__(
        self,
        url: str = None,
        status: int = None,
        run_time: str = None,
        end_time: str = None,
        comment: str = None,
    ):
        # {"en":"refresh URL，support like search", "zh_CN":"刷新URL,支持模糊查询"}
        self.url = url
        # {"en":"refresh status 1 wait ，2，success，3 fail", "zh_CN":"刷新状态 1 待刷新，2，刷新成功，3失败"}
        self.status = status
        # {"en":"refresh time", "zh_CN":"刷新时间"}
        self.run_time = run_time
        # {"en":"End Time", "zh_CN":"结束时间"}
        self.end_time = end_time
        # {"en":"comment，run result", "zh_CN":"备注,执行结果"}
        self.comment = comment

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.status, 'status')
        self.validate_required(self.run_time, 'run_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.comment, 'comment')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.status is not None:
            result['status'] = self.status
        if self.run_time is not None:
            result['runTime'] = self.run_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.comment is not None:
            result['comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('runTime') is not None:
            self.run_time = m.get('runTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        return self


class QueryRefreshPageRefreshSiteLogPage(TeaModel):
    def __init__(
        self,
        total: int = None,
        pages: int = None,
        list: List[QueryRefreshPageRefreshSiteLog] = None,
    ):
        # {"en":"record count", "zh_CN":"总记录数"}
        self.total = total
        # {"en":"total page", "zh_CN":"页数"}
        self.pages = pages
        # {"en":"page data list", "zh_CN":"每页数据列表"}
        self.list = list

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.pages, 'pages')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.pages is not None:
            result['pages'] = self.pages
        if self.list is not None:
            result['list'] = []
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        if m.get('list') is not None:
            self.list = []
            for k in m.get('list'):
                temp_model = QueryRefreshPageRefreshSiteLog()
                self.list.append(temp_model.from_map(k))
        return self


class QueryRefreshPageResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryRefreshPageRefreshSiteLogPage = None,
    ):
        # {"en":"code，success is 0", "zh_CN":"状态码，成功为0"}
        self.code = code
        # {"en":"error message or Success", "zh_CN":"错误信息或Success"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回值"}
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
            temp_model = QueryRefreshPageRefreshSiteLogPage()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryRefreshPagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRefreshPageParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRefreshPageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryRefreshPageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RefreshByUrlsRequest(TeaModel):
    def __init__(
        self,
        urls: List[str] = None,
        refresh_type: int = None,
        delay_minutes: int = None,
        order_time: str = None,
    ):
        # {"en":"refresh page url", "zh_CN":"刷新页面URL"}
        self.urls = urls
        # {"en":"refresh mode 1: now 2:delayed 3: order", "zh_CN":"刷新方式 1: 表示即可 2:延时 3: 预约"}
        self.refresh_type = refresh_type
        # {"en":"delay minutes（unit min）,if refreshType=2 the current is not null", "zh_CN":"延时分钟（单位分钟），当 refreshType=2 不能为空"}
        self.delay_minutes = delay_minutes
        # {"en":"order Time; yyyy-mm-dd hh:mm:ss. if refreshType=3 the current is not null", "zh_CN":"预约时间; yyyy-mm-dd hh:mm:ss. 当 refreshType=3 不能为空"}
        self.order_time = order_time

    def validate(self):
        self.validate_required(self.urls, 'urls')
        self.validate_required(self.refresh_type, 'refresh_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urls is not None:
            result['urls'] = self.urls
        if self.refresh_type is not None:
            result['refreshType'] = self.refresh_type
        if self.delay_minutes is not None:
            result['delayMinutes'] = self.delay_minutes
        if self.order_time is not None:
            result['orderTime'] = self.order_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('refreshType') is not None:
            self.refresh_type = m.get('refreshType')
        if m.get('delayMinutes') is not None:
            self.delay_minutes = m.get('delayMinutes')
        if m.get('orderTime') is not None:
            self.order_time = m.get('orderTime')
        return self


class RefreshByUrlsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"code，success is 0", "zh_CN":"状态码，成功为0"}
        self.code = code
        # {"en":"error message or Success", "zh_CN":"错误信息或Success"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回值"}
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


class RefreshByUrlsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RefreshByUrlsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RefreshByUrlsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RefreshByUrlsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




