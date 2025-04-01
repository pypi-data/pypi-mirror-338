# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryPrefetchStatusRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        item_id: str = None,
        url: str = None,
        status: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # {'en':'Query the start time of the task creation time, such as 2017-01-10 23:33:26. It is not allowed to query tasks before 7 days ago.', 'zh_CN':'查询的任务创建开始时间，如 2017-01-10 06:33:26，不允许查询3天之前的任务'}
        self.start_time = start_time
        # {'en':'Query the end time of the task creation time, such as 2017-01-10 23:33:26,. The query time is no more than 1 days from the start time.', 'zh_CN':'查询的任务创建结束时间，如 2017-01-10 23:33:26
        # 1）查询跨度不能超过1天；'}
        self.end_time = end_time
        # {'en':'A unique identifier for the same batch of tasks. If you submit multiple urls from an API request, the ID is a unique number for these tasks.
        # Query tasks by batch, such as submitting 10 url refreshes at a time. After the submission is successful, the content management system will return an itemId in the response message.', 'zh_CN':'表示任务单次提交多个url时任务的唯一标识。
        # 按批次查询任务，如单次提交10条url文件预取，提交成功后内容管理系统将返回一个itemId在响应消息里。
        # itemId 和 查询起止时间不能同时为空。'}
        self.item_id = item_id
        # {'en':'It is the url that you want to prefetch. This element only allows one url to be submitted per query.', 'zh_CN':'需要预取的文件完整访问路径（url），单次查询只允许输入一条url'}
        self.url = url
        # {'en':'Task status. The system allows you to select a task status query. These states can be queried:
        # 1.success
        # 2.failure', 'zh_CN':'任务状态，允许执行任务状态过滤查询结果，支持查询的状态有：
        # 1、success
        # 2、failure'}
        self.status = status
        # {'en':'Request page number. The default is 1.', 'zh_CN':'请求页数，缺省情况下，默认为1'}
        self.page_no = page_no
        # {'en':'The number of pages displayed. The default is 20.', 'zh_CN':'每页显示的条数，缺省情况下，默认值为20'}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.url is not None:
            result['url'] = self.url
        if self.status is not None:
            result['status'] = self.status
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class QueryPrefetchStatusResponseResultDetail(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        create_time: str = None,
        finish_time: str = None,
        rate: str = None,
        status: str = None,
        url: str = None,
    ):
        # {'en':'The time at which the content management system begins to get the file.', 'zh_CN':'内容管理系统开始同步文件的时间'}
        self.begin_time = begin_time
        # {'en':'The time at which the content management system receive the request and creates a prefetch task.', 'zh_CN':'内容管理系统接收预取任务成功并创建预取任务的时间'}
        self.create_time = create_time
        # {'en':'The time at which cdn cache the file and the content management system completes the summary task results.', 'zh_CN':'内容管理系统执行预取完成的时间'}
        self.finish_time = finish_time
        # {"en":"The content management system handles the prefetch tasks's success rate. If the success rate is 98%, the value is 98.", "zh_CN":"执行文件预取任务的成功率，如98%，则值为98"}
        self.rate = rate
        # {'en':'The status of the prefetch task. There are several states:
        # Success: Prefetch success.
        # Failure: Prefetch failed.
        # Wait: The prefetch task is waiting to be processed.
        # Run: The prefetch task is being executed.', 'zh_CN':'预取文件的任务状态：
        # success：表示文件预取的任务执行成功
        # failure：表示文件预取的任务执行失败
        # wait：表示文件预取的任务正在排队中
        # run：表示文件预取的任务正在执行中'}
        self.status = status
        # {'en':'Prefetched file URL.', 'zh_CN':'要预取的文件url'}
        self.url = url

    def validate(self):
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.status, 'status')
        self.validate_required(self.url, 'url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.rate is not None:
            result['rate'] = self.rate
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class QueryPrefetchStatusResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        code: int = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        result_detail: List[QueryPrefetchStatusResponseResultDetail] = None,
    ):
        # {'en':'The number of tasks that match the query criteria. If 10 tasks meet the query criteria, the value of count is 10.', 'zh_CN':'表示本次查询结果的数量，如有10个任务符合查询条件，则count的值为10'}
        self.count = count
        # {'en':'The status code of the task creation result. 1 means success, 0 means failure.', 'zh_CN':'任务提交后，系统的响应码，0表示失败，1表示成功'}
        self.code = code
        # {'en':'Content system response message after submitting the task.', 'zh_CN':'表示任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'The total number of pages for task query results.', 'zh_CN':'任务查询结果的总页数'}
        self.page_no = page_no
        # {'en':'How many purge task data is displayed per page.', 'zh_CN':'每页显示多少条预取文件的任务数据'}
        self.page_size = page_size
        # {'en':'Collection of task results.', 'zh_CN':'任务结果的集合'}
        self.result_detail = result_detail

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.result_detail, 'result_detail')
        if self.result_detail:
            for k in self.result_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.result_detail is not None:
            result['resultDetail'] = []
            for k in self.result_detail:
                result['resultDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resultDetail') is not None:
            self.result_detail = []
            for k in m.get('resultDetail'):
                temp_model = QueryPrefetchStatusResponseResultDetail()
                self.result_detail.append(temp_model.from_map(k))
        return self


class QueryPrefetchStatusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPrefetchStatusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPrefetchStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPrefetchStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ApiCmCcmquotaqueryFetchDnaRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ApiCmCcmquotaqueryFetchDnaResponse(TeaModel):
    def __init__(
        self,
        supplier: str = None,
        code: int = None,
        message: str = None,
        max_runing_fetch: int = None,
        fetch_count: int = None,
        fetch_upper: int = None,
        fetch_remain: int = None,
        fetch_size_upper: int = None,
        fetch_size_remain: int = None,
    ):
        # {'en':'It is the logo of our company.', 'zh_CN':'数据提供方'}
        self.supplier = supplier
        # {'en':'The status code of the query result. 0 means success, 1 means failure.', 'zh_CN':'查询结果，0表示成功，1表示失败'}
        self.code = code
        # {'en':'Content system response message after query.', 'zh_CN':'查询的响应消息'}
        self.message = message
        # {'en':'The number of urls back to the origin at the same time.', 'zh_CN':'同时最多有多少条url回源预取'}
        self.max_runing_fetch = max_runing_fetch
        # {'en':'The number of urls that have been prefetched back to the origin today.', 'zh_CN':'当天已经回源预取了多少条url'}
        self.fetch_count = fetch_count
        # {'en':'The maximum number of the prefetch files today.', 'zh_CN':'当天文件预取任务允许提交的最大数量'}
        self.fetch_upper = fetch_upper
        # {'en':'The number of urls that can be prefetched today.', 'zh_CN':'当天文件预取剩余url的数量'}
        self.fetch_remain = fetch_remain
        # {'en':'The maximum size of the prefetch files today. The unit is MB.', 'zh_CN':'当天允许预取的文件大小，单位MB'}
        self.fetch_size_upper = fetch_size_upper
        # {'en':'The size of urls that can be prefetched today.The unit is MB', 'zh_CN':'当天剩余可预取的文件大小，单位MB'}
        self.fetch_size_remain = fetch_size_remain

    def validate(self):
        self.validate_required(self.supplier, 'supplier')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.max_runing_fetch, 'max_runing_fetch')
        self.validate_required(self.fetch_count, 'fetch_count')
        self.validate_required(self.fetch_upper, 'fetch_upper')
        self.validate_required(self.fetch_remain, 'fetch_remain')
        self.validate_required(self.fetch_size_upper, 'fetch_size_upper')
        self.validate_required(self.fetch_size_remain, 'fetch_size_remain')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supplier is not None:
            result['supplier'] = self.supplier
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.max_runing_fetch is not None:
            result['maxRuningFetch'] = self.max_runing_fetch
        if self.fetch_count is not None:
            result['fetchCount'] = self.fetch_count
        if self.fetch_upper is not None:
            result['fetchUpper'] = self.fetch_upper
        if self.fetch_remain is not None:
            result['fetchRemain'] = self.fetch_remain
        if self.fetch_size_upper is not None:
            result['fetchSizeUpper'] = self.fetch_size_upper
        if self.fetch_size_remain is not None:
            result['fetchSizeRemain'] = self.fetch_size_remain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('maxRuningFetch') is not None:
            self.max_runing_fetch = m.get('maxRuningFetch')
        if m.get('fetchCount') is not None:
            self.fetch_count = m.get('fetchCount')
        if m.get('fetchUpper') is not None:
            self.fetch_upper = m.get('fetchUpper')
        if m.get('fetchRemain') is not None:
            self.fetch_remain = m.get('fetchRemain')
        if m.get('fetchSizeUpper') is not None:
            self.fetch_size_upper = m.get('fetchSizeUpper')
        if m.get('fetchSizeRemain') is not None:
            self.fetch_size_remain = m.get('fetchSizeRemain')
        return self


class ApiCmCcmquotaqueryFetchDnaPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ApiCmCcmquotaqueryFetchDnaParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # {"en":"Query the feature's daily limit:
        # Purge: Query the number of daily purge
        # Fetch: Query the number and size of daily prefetch", "zh_CN":"用于指定查询哪种业务类型的每日资源上限，可选值有：
        # purge：表示查询每日刷新缓存的数量限制
        # fetch：表示查询每日预取文件的数量、大小限制"}
        self.type = type

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ApiCmCcmquotaqueryFetchDnaRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ApiCmCcmquotaqueryFetchDnaResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PrefetchRequest(TeaModel):
    def __init__(
        self,
        urls: List[str] = None,
        is_range: int = None,
    ):
        # {'en':'If you need to prefetch several cached URLs. The submitted URL should meet the following format requirements:
        # 1.The URL must start with http:// or https://, url example: http://www.a.com/image/test.png.
        # 2.Each url has a maximum length of 2000 characters.
        # 3.The domain in the URL is must be the domain of the CDN service.
        # 4.If the url contains special characters such as Chinese characters and spaces, our system will generate multiple push tasks. In addition to pushing the original URL, these special characters will be converted int32o ASCII codes and pushed. If you only want to clean up the transcoded URL, you need to use UTF-8 to complete the transcoding before submitting the URL, and then submit the escaped url to our system.
        # 5.No more than 20000 urls per day, and no more than 200G file size (it can be adjusted according to account, contact your technical support).
        # 6.The total number of URLs called by each interface shall not exceed 400'
        # , 'zh_CN':'要预取到CDN节点的url集合，url格式说明：
        # 1、URL 必须以 http:// 或 https:// 开头，输入示例：http://www.a.com/image/test.png。
        # 2、每个url最大长度 2000 字符。
        # 3、每个url所在的域名必须是在我司加速的域名且有预取权限。
        # 4、url中如果包含中文字符，则提交的url需要是中文转义后的url，采用utf-8方式转义。
        # 5、每日不超过20000条，不超过200G文件大小（账号粒度可调，联系技术支持人员调整）。
        # 6、每次接口调用url的总数不超过400条。'}
        self.urls = urls
        # {"en":"Only prefetch a range segment of the file header. The user get the file from the beginning, and they will select quickly their int32erested. If the file header is cached, the first pack time of the user's http request will be short.This feature allows users to filter content faster. For example, if a file has 200MB, only the size of the file 0~range is prefetched, instead of prefetching the entire file. Each account can be configured with a size of the range. If you need to modify the size, please contact us. If this element is assigned a value of 1, the default prefetch is 0~512KB.", "zh_CN":"是否需要预取range段。
        # 
        # 1、默认为0，表示预取完整的文件；
        # 2、1表示预取文件0~512KB的range段（账号粒度可调，联系技术支持人员调整）。"}
        self.is_range = is_range

    def validate(self):
        self.validate_required(self.urls, 'urls')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urls is not None:
            result['urls'] = self.urls
        if self.is_range is not None:
            result['isRange'] = self.is_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('isRange') is not None:
            self.is_range = m.get('isRange')
        return self


class PrefetchResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        item_id: str = None,
    ):
        # {'en':'The status code of the task creation result, 1 means success, 0 means failure.', 'zh_CN':'表示任务创建结果的状态码，1表示任务提交成功，0表示任务提交失败'}
        self.code = code
        # {'en':'Content system response message after submitting the task.', 'zh_CN':'表示任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'After calling the API once and submitting the task successfully, the content system will return an itemId. This ID is the unique identifier for each submission. You can use itemId to batch query the status (success/failure) of the task.', 'zh_CN':'调用一次接口并提交任务成功后，将返回一个itemId，是当次提交任务的唯一标识，通过itemId可批量查询任务的状态（成功/失败）。'}
        self.item_id = item_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.item_id, 'item_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.item_id is not None:
            result['itemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        return self


class PrefetchPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PrefetchParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PrefetchRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PrefetchResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




