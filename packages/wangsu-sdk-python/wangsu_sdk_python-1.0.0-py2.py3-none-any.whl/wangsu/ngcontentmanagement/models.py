# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetPurgeRequestStatusPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a purge request.", "zh_CN": "刷新任务的ID。"}
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


class GetPurgeRequestStatusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeRequestStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeRequestStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeRequestStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeRequestStatusResponseFileHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "HTTP header name.", "zh_CN": "HTTP头部名称。"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP头部值。"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetPurgeRequestStatusResponseDirHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "HTTP header name.", "zh_CN": "HTTP头部名称。"}
        self.name = name
        # {"en" : "alue of an HTTP header.", "zh_CN": "HTTP头部值。"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetPurgeRequestStatusResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        file_urls: List[str] = None,
        file_headers: List[GetPurgeRequestStatusResponseFileHeaders] = None,
        dir_urls: List[str] = None,
        dir_headers: List[GetPurgeRequestStatusResponseDirHeaders] = None,
        regex_patterns: List[str] = None,
        target: str = None,
        submission_time: str = None,
        success_rate: int = None,
        status: str = None,
        action: str = None,
        finish_time: str = None,
        api_request_id: str = None,
        webhook: str = None,
    ):
        # {"en" : "Name of the purge request.", "zh_CN": "刷新请求的名称。"}
        self.name = name
        # {"en" : "The files that were purged.", "zh_CN": "被刷新的文件。"}
        self.file_urls = file_urls
        # {"en" : "If a file's cache key depends on request headers, you can specify the header values that are applicable to purge one version of the cached file. The same set of header values will apply to all entries in fileUrls.  ", "zh_CN": "如果文件的缓存键与请求头相关，则可以指定请求头和值来刷新相应的缓存文件。此处指定的请求头和值将应用于fileUrls中的所有条目。"}
        self.file_headers = file_headers
        # {"en" : "<= 20 items 
        # The directories that were purged.", "zh_CN": "<= 20 条目 
        # 被刷新的目录。"}
        self.dir_urls = dir_urls
        # {"en" : "If a directory's cache key depends on request headers, you can specify the header values that are applicable to purge one version of the cached directory. The same set of header values will apply to all entries in dirUrls.", "zh_CN": "如果目录的缓存键与请求头相关，则可以指定请求头和值来刷新相应的缓存目录。此处指定的请求头和值将应用于dirUrls中的所有条目。"}
        self.dir_headers = dir_headers
        # {"en" : "<= 2 items 
        # Regular expression patterns used to match the cache key. Each must begin with the following format: 
        #  {scheme}://{hostname}/. {scheme} can be http, https, or any which matches any scheme.
        # Example: 
        # https://test.domain.com/my.*\.(jpg|png)\?q=\
        # <br/>
        # For performance considerations, the following restrictions apply:
        # The regular expression pattern following the hostname can be up to 126 characters.
        # 
        # It can consist of up to two unlimited quantifiers ('*', '+', or ',}').
        # The upper limit on a quantifier cannot be more than 59, for example, {1,59}", "zh_CN": "<= 2 条目 
        # 用于匹配缓存键的正则表达式。每一个表达式必须以以下格式开始:
        # {协议}://{域名}/. {协议}可以是http, https或any（表示不限协议）。
        # 示例:
        # https://test.domain.com/my.*\.(jpg|png)\?q=\
        # <br/>
        # 出于性能考虑，使用正则表达式有以下限制：
        # 
        # 在域名后面的正则表达式最多只能包含126个字符。
        # 最多只能包含两个限定符('*'、'+'或',}')。
        # 限定符的上限不能超过59，例如{1,59}"}
        self.regex_patterns = regex_patterns
        # {"en" : "Enum: staging production 
        # Indicates whether the purge is in the staging or production environment.", "zh_CN": "取值范围: staging, production 
        # 刷新任务对应的环境，即演练环境或生产环境。"}
        self.target = target
        # {"en" : "An RFC 3339 date indicating when the purge request was created.", "zh_CN": "RFC 3339格式的日期，表示刷新请求的创建时间。"}
        self.submission_time = submission_time
        # {"en" : "[ 0 .. 100 ] 
        # A percentage that indicates the completion of the purge request.", "zh_CN": "取值范围: [ 0 .. 100 ] 
        # 刷新请求任务的成功率。"}
        self.success_rate = success_rate
        # {"en" : "Enum: waiting, inprogress, finished 
        # Indicates the status of the purge request.", "zh_CN": "取值范围: waiting, inprogress, finished 
        # 刷新请求的任务执行状态，包括等待中，执行中，已完成等状态。"}
        self.status = status
        # {"en" : "Enum: delete, invalidate 
        # This controls whether cached files and directories should be removed altogether from the CDN Pro servers (delete) or flagged as invalid (invalidate).", "zh_CN": "取值范围: delete, invalidate 
        # 刷新请求的类型，包括完全删除(delete)和标记为无效(invalidate)。"}
        self.action = action
        # {"en" : "RFC 3339 date indicating when the purge was completed. It can be empty if the purge is still in progress.", "zh_CN": "RFC 3339格式的日期，表示刷新任务完成的时间。如果刷新还在进行中，则返回空值。"}
        self.finish_time = finish_time
        # {"en" : "Indicates the corresponding API request ID.", "zh_CN": "API请求ID。"}
        self.api_request_id = api_request_id
        # {"en" : "ID of a webhook to call when the purge task completes.", "zh_CN": "刷新任务完成时要调用的webhook的ID。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.file_urls, 'file_urls')
        self.validate_required(self.file_headers, 'file_headers')
        if self.file_headers:
            for k in self.file_headers:
                if k:
                    k.validate()
        self.validate_required(self.dir_urls, 'dir_urls')
        self.validate_required(self.dir_headers, 'dir_headers')
        if self.dir_headers:
            for k in self.dir_headers:
                if k:
                    k.validate()
        self.validate_required(self.regex_patterns, 'regex_patterns')
        self.validate_required(self.target, 'target')
        self.validate_required(self.submission_time, 'submission_time')
        self.validate_required(self.success_rate, 'success_rate')
        self.validate_required(self.status, 'status')
        self.validate_required(self.action, 'action')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.api_request_id, 'api_request_id')
        self.validate_required(self.webhook, 'webhook')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.file_urls is not None:
            result['fileUrls'] = self.file_urls
        if self.file_headers is not None:
            result['fileHeaders'] = []
            for k in self.file_headers:
                result['fileHeaders'].append(k.to_map() if k else None)
        if self.dir_urls is not None:
            result['dirUrls'] = self.dir_urls
        if self.dir_headers is not None:
            result['dirHeaders'] = []
            for k in self.dir_headers:
                result['dirHeaders'].append(k.to_map() if k else None)
        if self.regex_patterns is not None:
            result['regexPatterns'] = self.regex_patterns
        if self.target is not None:
            result['target'] = self.target
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.success_rate is not None:
            result['successRate'] = self.success_rate
        if self.status is not None:
            result['status'] = self.status
        if self.action is not None:
            result['action'] = self.action
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileUrls') is not None:
            self.file_urls = m.get('fileUrls')
        if m.get('fileHeaders') is not None:
            self.file_headers = []
            for k in m.get('fileHeaders'):
                temp_model = GetPurgeRequestStatusResponseFileHeaders()
                self.file_headers.append(temp_model.from_map(k))
        if m.get('dirUrls') is not None:
            self.dir_urls = m.get('dirUrls')
        if m.get('dirHeaders') is not None:
            self.dir_headers = []
            for k in m.get('dirHeaders'):
                temp_model = GetPurgeRequestStatusResponseDirHeaders()
                self.dir_headers.append(temp_model.from_map(k))
        if m.get('regexPatterns') is not None:
            self.regex_patterns = m.get('regexPatterns')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self






class CreateAPurgeRequestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPurgeRequestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPurgeRequestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPurgeRequestRequestFileHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "HTTP header name.", "zh_CN": "HTTP 头部名称"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP 头部的值"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateAPurgeRequestRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        file_urls: List[str] = None,
        file_headers: List[CreateAPurgeRequestRequestFileHeaders] = None,
        dir_urls: List[str] = None,
        regex_patterns: List[str] = None,
        action: str = None,
        target: str = None,
        webhook: str = None,
    ):
        # {"en" : "A description of the purge request.", "zh_CN": "刷新请求的说明。"}
        self.name = name
        # {"en" : "URLs of files to purge.  File URLs should not contain the asterisk character, '*'.   If a directory or filename in a URL includes a percent character, '%', be sure to encode it. A URL can be up to 2048 characters.", "zh_CN": "要刷新的文件的URL。URL不能包含星号字符'*'。如果URL中的目录或文件名包含'%'等特殊符号，需要先进行URL编码。每个URL长度不能超过2048个字符。"}
        self.file_urls = file_urls
        # {"en" : "If a file's cache key depends on request headers, you can specify the header values that are applicable to purge one version of the cached file. The same set of header values will apply to all entries in fileUrls.", "zh_CN": "如果文件的缓存键与请求头相关，则可以指定请求头和值来刷新相应的缓存文件。此处指定的请求头和值将应用于fileUrls中的所有条目。"}
        self.file_headers = file_headers
        # {"en" : "<= 20 items 
        # URLs to purge. URLs must begin with http:// or https:// and can be up to 2048 characters. Use the '*' character to purge multiple files or directories. If a URL has multiple sets of asterisk characters, only the last '*' or '**' will be treated as a wildcard. Other instances of '*' earlier in the URL will be treated as the literal character '*'.
        # <table><tr><th>Example</th><th>Description</th></tr><tr><td>http://test.domain2.com/mydir</td><td>Purge all variations of a single directory, but not its subdirectories or files. Variations may exist if custom cache keys are used.</td></tr><tr><td>http://test.domain2.com/mydir/**</td><td>Purge all files and subdirectories whose cache key begins with http://test.domain2.com/mydir/.</td></tr><tr><td>http://test.domain2.com/mydir/*</td><td>Purge all files, but not subdirectories, within a directory.</td></tr><tr><td>http://test.domain2.com/mydir/*.jpg</td><td>Purge all cache entries ending with the .jpg file extension. Subdirectories of http://test.domain2.com/mydir/ are not purged. </td></tr><tr><td>http://test.domain2.com/mydir/a*</td><td>Purge all files, but not subdirectories, that start with the letter 'a'.</td></tr><tr><td>http://test.domain2.com/mydir/a**</td><td>Purge all files and subdirectories that start with the letter 'a'.</td></tr><tr><td>http://test.domain2.com/mydir/a.jpg</td><td>Purge all variations of 'a.jpg'. Variations may exist if custom cache keys are used.</td></tr><tr><td>http://test.domain2.com/my**jpg</td><td>Purge all entries whose cache key begins with http://test.domain2.com/my and ends with the suffix jpg. The '**' can match anything in the path including additional subdirectories. For example, http://test.domain2.com/mydirectory/picture.jpg would be purged.</td></tr></table>
        # If a directory or filename in a URL includes a percent character, '%', be sure to encode it.", "zh_CN": "<= 20 条目 
        # 要刷新的目录的URL。URL必须以http:// 或者 https://开头，每条URL最多只能包含2048个字符。 在URL中使用'*'字符可以匹配多个文件或目录。如果一条URL中带有多组'*'，则只有最后一个'*'或'**'会被当成通配符来进行匹配，其它的'*'只会被当成普通字符。
        # <table><tr><th>示例</th><th>描述</th></tr><tr><td>http://test.domain2.com/mydir</td><td>刷新单个目录的所有变体，但不包括其子目录或文件。当您自定义了缓存键时，则可能存在变体。</td></tr><tr><td>http://test.domain2.com/mydir/**</td><td>刷新缓存键以http://test.domain2.com/mydir/开头的所有文件和子目录。</td></tr><tr><td>http://test.domain2.com/mydir/*</td><td>刷新目录中的所有文件，但不包括子目录。</td></tr><tr><td>http://test.domain2.com/mydir/*.jpg</td><td>刷新所有以.jpg文件扩展名结尾的缓存，但不会刷新http://test.domain2.com/mydir/ 的子目录。 </td></tr><tr><td>http://test.domain2.com/mydir/a*</td><td>刷新以字母'a'开头的所有文件，但不包括子目录。</td></tr><tr><td>http://test.domain2.com/mydir/a**</td><td>刷新以字母'a'开头的所有文件和子目录。</td></tr><tr><td>http://test.domain2.com/mydir/a.jpg</td><td>刷新'a.jpg'文件的所有变体。当您自定义了缓存键时，则可能存在变体。</td></tr><tr><td>http://test.domain2.com/my**jpg</td><td>刷新缓存键以 http://test.domain2.com/my 开头并以后缀 jpg 结尾的所有条目。'**'可以匹配路径中的任何内容，包括其他子目录。例如，http://test.domain2.com/mydirectory/picture.jpg 将被刷新。</td></tr></table>
        # 如果URL中的目录或文件名包含百分号'%'等特殊符号时，请确保先进行URL编码。"}
        self.dir_urls = dir_urls
        # {"en" : "<= 2 items 
        # Regular expression patterns used to match the cache key. Each must begin with the following format: 
        #  {scheme}://{hostname}/. {scheme} can be http, https, or any, which matches any scheme.
        # Example: 
        # https://test.domain.com/my.*\.(jpg|png)\?q=\
        # <br/>
        # For performance considerations, the following restrictions apply:
        # The regular expression pattern following the hostname can be up to 126 characters.
        # 
        # It can consist of up to two unlimited quantifiers ('*', '+', or ',}').
        # The upper limit on a quantifier cannot be more than 59, for example, {1,59}", "zh_CN": "<= 2 条目 
        # 用于匹配缓存键的正则表达式。
        # 每个表达式必须以
        # {协议}://{域名}/ 格式开头。其中，{协议} 可以是 http, https，或any（表示不限协议）。
        # 示例：
        # https://test.domain.com/my.*\.(jpg|png)\?q=\
        # <br/>
        # 出于性能考虑，使用正则表达式有以下限制：
        # 
        # 在域名后面的正则表达式最多只能包含126个字符。
        # 最多只能包含两个限定符('*'、'+'或',}')。
        # 限定符的上限不能超过59，例如{1,59}"}
        self.regex_patterns = regex_patterns
        # {"en" : "Enum: delete invalidate 
        # Default: invalidate 
        # This controls whether cached files and directories should be removed altogether from the CDN Pro servers (delete) or flagged as invalid (invalidate).", "zh_CN": "取值范围: delete, invalidate 
        # 默认值: invalidate 
        # 指定刷新类型，包括完全删除(delete)和标记为无效(invalidate)。"}
        self.action = action
        # {"en" : "Enum: staging production 
        # Specify if the purge request applies to the staging or production environment.", "zh_CN": "取值范围: staging, production 
        # 指定刷新请求应用于演练环境还是生产环境。"}
        self.target = target
        # {"en" : "ID of a webhook to call when the purge task completes.", "zh_CN": "刷新任务完成时要调用的webhook的ID。"}
        self.webhook = webhook

    def validate(self):
        if self.file_headers:
            for k in self.file_headers:
                if k:
                    k.validate()
        self.validate_required(self.target, 'target')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.file_urls is not None:
            result['fileUrls'] = self.file_urls
        if self.file_headers is not None:
            result['fileHeaders'] = []
            for k in self.file_headers:
                result['fileHeaders'].append(k.to_map() if k else None)
        if self.dir_urls is not None:
            result['dirUrls'] = self.dir_urls
        if self.regex_patterns is not None:
            result['regexPatterns'] = self.regex_patterns
        if self.action is not None:
            result['action'] = self.action
        if self.target is not None:
            result['target'] = self.target
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileUrls') is not None:
            self.file_urls = m.get('fileUrls')
        if m.get('fileHeaders') is not None:
            self.file_headers = []
            for k in m.get('fileHeaders'):
                temp_model = CreateAPurgeRequestRequestFileHeaders()
                self.file_headers.append(temp_model.from_map(k))
        if m.get('dirUrls') is not None:
            self.dir_urls = m.get('dirUrls')
        if m.get('regexPatterns') is not None:
            self.regex_patterns = m.get('regexPatterns')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class CreateAPurgeRequestResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPurgeRequestResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header is a URL representing the new purge request, for example, <code>Location: https://{domain}/cdn/purges/e91e8674-c2c5-4440-a1de-8b2ea99293dd</code>.", "zh_CN":"通过Location响应头返回新建的刷新任务的URL。URL中包含刷新任务的ID，可使用该ID调用'查询刷新任务详情'接口来查看刷新任务详情。URL示例：<code>Location: https://{domain}/cdn/purges/5dca2205f9e9cc0001df7b33"}
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






class GetPrefetchRequestStatusPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a prefetch request.", "zh_CN": "预取请求的 id。"}
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


class GetPrefetchRequestStatusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPrefetchRequestStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPrefetchRequestStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPrefetchRequestStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPrefetchRequestStatusResponseFileListHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "HTTP header name.", "zh_CN": "HTTP头部名称。"}
        self.name = name
        # {"en" : "HTTP header value.", "zh_CN": "HTTP头部值。"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetPrefetchRequestStatusResponseFileList(TeaModel):
    def __init__(
        self,
        url: str = None,
        headers: List[GetPrefetchRequestStatusResponseFileListHeaders] = None,
    ):
        # {"en" : "Range: [ 10 .. 2048 ] characters 
        # A URL to prefetch. It must begin with 'http' or 'https' and can be up to 2048 characters.", "zh_CN": "取值范围: [ 10 .. 2048 ] 字符 
        # 预取的URL。必须以'http'或'https'开头，长度不超过2048个字符。"}
        self.url = url
        # {"en" : "If a URL's cache key depends on request headers, you can specify the header values that are applicable to prefetch one version of the URL.", "zh_CN": "如果需要在缓存键中加入请求头，可用该字段指定请求头。"}
        self.headers = headers

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = GetPrefetchRequestStatusResponseFileListHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class GetPrefetchRequestStatusResponseMetadata(TeaModel):
    def __init__(
        self,
        id: str = None,
        submission_time: str = None,
        success_rate: int = None,
        status: str = None,
        finish_time: str = None,
        api_request_id: str = None,
    ):
        # {"en" : "ID of the prefetch request.", "zh_CN": "预取请求ID。"}
        self.id = id
        # {"en" : "RFC 3339 date indicating when the prefetch request was submitted.", "zh_CN": "RFC 3339格式的日期，表示预取请求的提交时间。"}
        self.submission_time = submission_time
        # {"en" : "Range: [ 0 .. 100 ] 
        # A percentage that indicates the completion of the prefetch request.", "zh_CN": "取值范围: [ 0 .. 100 ] 
        # 预取任务的成功率。"}
        self.success_rate = success_rate
        # {"en" : "Enum: waiting,inprogress,finished 
        # Indicates the status of the prefetch request.", "zh_CN": "取值范围: waiting,inprogress,finished 
        # 预取请求的任务执行状态，包括等待中，进行中，已完成等状态。"}
        self.status = status
        # {"en" : "RFC 3339 date indicating when the prefetch completed.", "zh_CN": "RFC 3339格式的日期，表示预取完成的时间。"}
        self.finish_time = finish_time
        # {"en" : "Indicates the corresponding API request ID.", "zh_CN": "API请求ID。"}
        self.api_request_id = api_request_id

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.submission_time, 'submission_time')
        self.validate_required(self.success_rate, 'success_rate')
        self.validate_required(self.status, 'status')
        self.validate_required(self.api_request_id, 'api_request_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.success_rate is not None:
            result['successRate'] = self.success_rate
        if self.status is not None:
            result['status'] = self.status
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        return self


class GetPrefetchRequestStatusResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        file_list: List[GetPrefetchRequestStatusResponseFileList] = None,
        metadata: GetPrefetchRequestStatusResponseMetadata = None,
        regions: List[str] = None,
        start_time: str = None,
        webhook: str = None,
    ):
        # {"en" : "Range: <= 1000 characters 
        # A short description of the prefetch task.", "zh_CN": "取值范围: <= 1000 字符 
        # 预取请求的简短描述。"}
        self.name = name
        # {"en" : "", "zh_CN": ""}
        self.file_list = file_list
        # {"en" : "Details about the prefetch request's status.", "zh_CN": "预取请求的状态信息。"}
        self.metadata = metadata
        # {"en" : "A list of continents representing the regions in which to perform the prefetch. Omitting the field means the prefetch will be done by all regions' servers.", "zh_CN": "需要预取内容的大洲，以大洲英文名表示。未指定时表示预取内容到所有大洲的服务器。"}
        self.regions = regions
        # {"en" : "RFC 3339 date indicating when the prefetch should begin. This must be in UTC time, for example, '2021-03-06T00:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示开始预取的时间。必须使用UTC时间，例如'2021-03-06T00:00:00Z'。"}
        self.start_time = start_time
        # {"en" : "ID of a webhook to call when the prefetch task completes.", "zh_CN": "预取任务完成时调用的webhook ID。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.file_list, 'file_list')
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()
        self.validate_required(self.metadata, 'metadata')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.regions, 'regions')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.webhook, 'webhook')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.file_list is not None:
            result['fileList'] = []
            for k in self.file_list:
                result['fileList'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.regions is not None:
            result['regions'] = self.regions
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileList') is not None:
            self.file_list = []
            for k in m.get('fileList'):
                temp_model = GetPrefetchRequestStatusResponseFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('metadata') is not None:
            temp_model = GetPrefetchRequestStatusResponseMetadata()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self






class GetPurgeSummaryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeSummaryParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        target: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. The time must be specified using the UTC timezone; it cannot be an offset. Example: startdate=2019-10-30T00:00:00Z ", "zh_CN": "RFC 3339格式的日期，表示查询的开始时间。必须使用UTC时区，不能是其它时区。例如：startdate=2019-10-30T00:00:00Z"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the timeframe. The time must be specified using the UTC timezone; it cannot be an offset. Example: enddate=2019-10-30T00:00:00Z ", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。必须使用UTC时区，不能是其它时区。例如：enddate=2019-10-30T00:00:00Z "}
        self.enddate = enddate
        # {"en" : "Enum: staging production 
        # Default: production 
        # Indicates the environment.", "zh_CN": "取值范围: staging, production 
        # 默认值: production 
        # 刷新请求对应的环境。"}
        self.target = target

    def validate(self):
        self.validate_required(self.startdate, 'startdate')
        self.validate_required(self.enddate, 'enddate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class GetPurgeSummaryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeSummaryRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeSummaryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPurgeSummaryResponse(TeaModel):
    def __init__(
        self,
        requests: int = None,
        file_requests: int = None,
        dir_requests: int = None,
        file_entries: int = None,
        dir_entries: int = None,
        regex_requests: int = None,
        regex_entries: int = None,
    ):
        # {"en" : ">= 0 
        # Number of purge requests.", "zh_CN": "取值范围: >= 0 
        # 刷新请求的数量。"}
        self.requests = requests
        # {"en" : ">= 0 
        # Number of purge API requests with non-empty fileURLs.
        # ", "zh_CN": "取值范围: >= 0 
        # 包含了文件刷新类型的刷新请求的数量。"}
        self.file_requests = file_requests
        # {"en" : ">= 0 
        # Number of purge API requests with non-empty dirUrls.", "zh_CN": "取值范围: >= 0 
        # 包含了目录刷新类型的刷新请求的数量。"}
        self.dir_requests = dir_requests
        # {"en" : ">= 0 
        # Total number of fileUrls' entries in purge requests.", "zh_CN": "取值范围: >= 0 
        # 刷新请求中文件（fileURL）条目的总数。"}
        self.file_entries = file_entries
        # {"en" : ">= 0 
        # Total number of dirUrls' entries in purge requests.", "zh_CN": "取值范围: >= 0 
        # 刷新请求中目录（dirURL）条目的总数。"}
        self.dir_entries = dir_entries
        # {"en" : ">= 0 
        # Number of purge API requests with non-empty regexPatterns.", "zh_CN": "取值范围: >= 0 
        # 包含了正则表达式刷新类型的刷新请求的数量。"}
        self.regex_requests = regex_requests
        # {"en" : ">= 0 
        # Total number of regexPatterns' entries in purge requests.", "zh_CN": "取值范围: >= 0 
        # 刷新请求中正则表达式条目的总数。"}
        self.regex_entries = regex_entries

    def validate(self):
        self.validate_required(self.requests, 'requests')
        self.validate_required(self.file_requests, 'file_requests')
        self.validate_required(self.dir_requests, 'dir_requests')
        self.validate_required(self.file_entries, 'file_entries')
        self.validate_required(self.dir_entries, 'dir_entries')
        self.validate_required(self.regex_requests, 'regex_requests')
        self.validate_required(self.regex_entries, 'regex_entries')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requests is not None:
            result['requests'] = self.requests
        if self.file_requests is not None:
            result['fileRequests'] = self.file_requests
        if self.dir_requests is not None:
            result['dirRequests'] = self.dir_requests
        if self.file_entries is not None:
            result['fileEntries'] = self.file_entries
        if self.dir_entries is not None:
            result['dirEntries'] = self.dir_entries
        if self.regex_requests is not None:
            result['regexRequests'] = self.regex_requests
        if self.regex_entries is not None:
            result['regexEntries'] = self.regex_entries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        if m.get('fileRequests') is not None:
            self.file_requests = m.get('fileRequests')
        if m.get('dirRequests') is not None:
            self.dir_requests = m.get('dirRequests')
        if m.get('fileEntries') is not None:
            self.file_entries = m.get('fileEntries')
        if m.get('dirEntries') is not None:
            self.dir_entries = m.get('dirEntries')
        if m.get('regexRequests') is not None:
            self.regex_requests = m.get('regexRequests')
        if m.get('regexEntries') is not None:
            self.regex_entries = m.get('regexEntries')
        return self






class GetListOfPrefetchRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPrefetchRequestsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        offset: int = None,
        limit: int = None,
        sort_by: str = None,
        sort_order: str = None,
        search: str = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. It must be in UTC time, for example, '2021-03-01T01:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示查询的开始时间。必须为UTC时间，如'2021-03-01T01:00:00Z'。"}
        self.startdate = startdate
        # {"en" : "RFC 3339 date indicating the end of the time period. It must be in UTC time, for example, '2021-03-01T01:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。必须为UTC时间，如'2021-03-01T01:00:00Z'。"}
        self.enddate = enddate
        # {"en" : "Default: 0 Range: >= 0 
        # Index of the first prefetch request to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Range: [ 1 .. 200 ] 
        # Maximum number of prefetch requests to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: submissionTime,finishTime 
        # Controls the order in which prefetch requests are returned. The default is to return the most recently submitted request first.", "zh_CN": "取值范围: submissionTime,finishTime 
        # 返回查询结果的排序依据。默认按预取请求的创建时间降序排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc,desc 
        # Order of prefetch requests. The default is to return the most recent prefetch request first. Enter 'asc' for ascending order or 'desc' for descending order.", "zh_CN": "取值范围: asc,desc 
        # 返回查询结果的排序顺序。默认按预取请求的创建时间降序排序。"}
        self.sort_order = sort_order
        # {"en" : "The value will be used to match on prefetch request names, hostnames, and the task IDs to limit the prefetch requests that are returned.", "zh_CN": "根据搜索关键字匹配预取请求的名称、ID和相关的加速域名，过滤预取请求。"}
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.search is not None:
            result['search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('search') is not None:
            self.search = m.get('search')
        return self


class GetListOfPrefetchRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPrefetchRequestsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPrefetchRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPrefetchRequestsResponsePrefetchRequests(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        status: str = None,
        submission_time: str = None,
        finish_time: str = None,
        success_rate: int = None,
        api_request_id: str = None,
        file_entries: int = None,
        hostnames: List[str] = None,
    ):
        # {"en" : "prefetch request task ID.
        # ", "zh_CN": "预取请求的ID。
        # "}
        self.id = id
        # {"en" : " a short description of the prefetch task.", "zh_CN": "预取请求的简短描述。"}
        self.name = name
        # {"en" : "Enum: waiting,inprogress,finished 
        # Indicates the status of the prefetch request.", "zh_CN": "取值范围: waiting,inprogress,finished 
        # 预取请求的任务执行状态，包括等待中，进行中，已完成等状态。"}
        self.status = status
        # {"en" : "RFC 3339 date indicating when the prefetch request was submitted.", "zh_CN": "RFC 3339格式的日期，表示预取请求的提交时间。"}
        self.submission_time = submission_time
        # {"en" : "RFC 3339 date indicating when the prefetch completed.", "zh_CN": "RFC 3339格式的日期，表示预取任务的完成时间。"}
        self.finish_time = finish_time
        # {"en" : "Range: [ 0 .. 100 ] 
        # A percentage that indicates the completion of the prefetch request.", "zh_CN": "取值范围: [ 0 .. 100 ] 
        # 预取任务的成功率。"}
        self.success_rate = success_rate
        # {"en" : "Indicates the corresponding API request ID.", "zh_CN": "API请求ID。"}
        self.api_request_id = api_request_id
        # {"en" : "Range: >= 1 
        # Number of URLs in the prefetch request.", "zh_CN": "取值范围: >= 1 
        # 预取请求中的URL数量。"}
        self.file_entries = file_entries
        # {"en" : "List of hostnames that were prefetched.", "zh_CN": "预取请求涉及的加速域名。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.success_rate is not None:
            result['successRate'] = self.success_rate
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.file_entries is not None:
            result['fileEntries'] = self.file_entries
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('fileEntries') is not None:
            self.file_entries = m.get('fileEntries')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetListOfPrefetchRequestsResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        prefetch_requests: List[GetListOfPrefetchRequestsResponsePrefetchRequests] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of prefetch requests matching the criteria specified in the query parameters. The actual number of entries in prefetchRequests may be fewer if you specified the parameter.", "zh_CN": "取值范围: >= 0 
        # 预取请求的总数。该数量取决于查询参数。"}
        self.count = count
        # {"en" : "List of prefetch requests.", "zh_CN": "预取请求列表。"}
        self.prefetch_requests = prefetch_requests

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.prefetch_requests, 'prefetch_requests')
        if self.prefetch_requests:
            for k in self.prefetch_requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.prefetch_requests is not None:
            result['prefetchRequests'] = []
            for k in self.prefetch_requests:
                result['prefetchRequests'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('prefetchRequests') is not None:
            self.prefetch_requests = []
            for k in m.get('prefetchRequests'):
                temp_model = GetListOfPrefetchRequestsResponsePrefetchRequests()
                self.prefetch_requests.append(temp_model.from_map(k))
        return self






class GetListOfPurgeRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPurgeRequestsParameters(TeaModel):
    def __init__(
        self,
        startdate: str = None,
        enddate: str = None,
        offset: int = None,
        limit: int = None,
        sort_by: str = None,
        sort_order: str = None,
        search: str = None,
        target: str = None,
        action: str = None,
        max_success_rate: int = None,
    ):
        # {"en" : "RFC 3339 date indicating the beginning of the time period. It must be in UTC time, for example, '2019-11-01T01:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示查询的开始时间。必须为UTC时间，如'2019-11-01T01:00:00Z'。"}
        self.startdate = startdate
        # {"en" : "[ 0 .. 0 ] characters 
        # RFC 3339 date indicating the end of the time period. It must be in UTC time, for example, '2019-11-01T01:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示查询的结束时间。必须为UTC时间，如'2019-11-01T01:00:00Z'。"}
        self.enddate = enddate
        # {"en" : "Default: 0 >= 0 
        # Index of the first purge request to return. ", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Maximum number of purge requests to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: submissionTime finishTime 
        # Default: submissionTime 
        # Controls the order in which purge requests are returned. The default is to return the most recently submitted request first.", "zh_CN": "取值范围: submissionTime, finishTime 
        # 默认值: submissionTime 
        # 返回结果的排序依据。默认按刷新请求的创建时间降序排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc desc 
        # Default: desc 
        # Order of purge requests. The default is to return the most recent purge request first.", "zh_CN": "取值范围: asc, desc 
        # 默认值: desc 
        # 返回结果的排序顺序。"}
        self.sort_order = sort_order
        # {"en" : "The value will be used to match on hostnames and the purge task ID to limit the purge requests that are returned.", "zh_CN": "根据搜索关键字匹配加速域名和刷新任务的ID进行过滤。"}
        self.search = search
        # {"en" : "Enum: production staging 
        # The target environment of the purge request. By default, all are returned.", "zh_CN": "取值范围: production, staging 
        # 根据部署环境来查询刷新请求。默认返回所有环境的刷新请求。"}
        self.target = target
        # {"en" : "Enum: invalidate delete 
        # The type of purge request. By default, all are returned.", "zh_CN": "取值范围: invalidate, delete 
        # 刷新请求的类型。默认返回所有类型的刷新请求。"}
        self.action = action
        # {"en" : "[ 0 .. 100 ] 
        # A decimal value indicating the maximum success rate of purge requests to return. By default, all are returned.", "zh_CN": "取值范围: [ 0 .. 100 ] 
        # 指定最大成功率来查询刷新任务，以十进制值表示。默认返回所有刷新请求。"}
        self.max_success_rate = max_success_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.search is not None:
            result['search'] = self.search
        if self.target is not None:
            result['target'] = self.target
        if self.action is not None:
            result['action'] = self.action
        if self.max_success_rate is not None:
            result['maxSuccessRate'] = self.max_success_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('maxSuccessRate') is not None:
            self.max_success_rate = m.get('maxSuccessRate')
        return self


class GetListOfPurgeRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPurgeRequestsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPurgeRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPurgeRequestsResponsePurgeRequests(TeaModel):
    def __init__(
        self,
        id: str = None,
        submission_time: str = None,
        hostnames: List[str] = None,
        file_entries: int = None,
        dir_entries: int = None,
        target: str = None,
        success_rate: int = None,
        status: str = None,
        finish_time: str = None,
        api_request_id: str = None,
        regex_entries: int = None,
    ):
        # {"en" : "ID associated with the purge request. You can call the Query purge request status API to get further information about it.", "zh_CN": "刷新请求的ID。您可以调用'查询刷新任务详情'接口来获得更多信息。"}
        self.id = id
        # {"en" : "An RFC 3339 date indicating when the purge request was created.", "zh_CN": "RFC 3339格式的日期，表示刷新请求的创建时间。"}
        self.submission_time = submission_time
        # {"en" : "Hostnames affected by the purge request.", "zh_CN": "刷新请求涉及的加速域名。"}
        self.hostnames = hostnames
        # {"en" : ">= 0 
        # Number of file URLs that were part of the purge request.", "zh_CN": "取值范围: >= 0 
        # 刷新请求中文件URL的数量。"}
        self.file_entries = file_entries
        # {"en" : "[ 0 .. 20 ] 
        # Number of directory URLs that were part of the purge request.", "zh_CN": "取值范围: [ 0 .. 20 ] 
        # 刷新请求中目录URL的数量。"}
        self.dir_entries = dir_entries
        # {"en" : "Enum: staging production 
        # Indicates whether the purge is in the staging or production environment.
        # ", "zh_CN": "取值范围: staging, production 
        # 刷新请求对应的环境，即演练环境或生产环境。"}
        self.target = target
        # {"en" : "[ 0 .. 100 ] 
        # A percentage that indicates the completion of the purge request. ", "zh_CN": "取值范围: [ 0 .. 100 ] 
        # 刷新请求任务的成功率。"}
        self.success_rate = success_rate
        # {"en" : "Enum: waiting inprogress finished 
        # Indicates the status of the purge request.", "zh_CN": "取值范围: waiting, inprogress, finished 
        # 刷新请求的执行状态，包括等待中，进行中，已完成等状态。"}
        self.status = status
        # {"en" : "RFC 3339 date indicating when the purge was completed. It can be empty if the purge is still in progress.", "zh_CN": "RFC 3339格式的日期，表示刷新完成的时间。如果刷新还在进行中，则返回空值。"}
        self.finish_time = finish_time
        # {"en" : "Indicates the corresponding API request ID.", "zh_CN": "API请求ID。"}
        self.api_request_id = api_request_id
        # {"en" : ">= 0 
        # Number of regex patterns that were part of the purge request.", "zh_CN": "取值范围: >= 0 
        # 刷新请求中正则表达式的条数。"}
        self.regex_entries = regex_entries

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.file_entries is not None:
            result['fileEntries'] = self.file_entries
        if self.dir_entries is not None:
            result['dirEntries'] = self.dir_entries
        if self.target is not None:
            result['target'] = self.target
        if self.success_rate is not None:
            result['successRate'] = self.success_rate
        if self.status is not None:
            result['status'] = self.status
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.regex_entries is not None:
            result['regexEntries'] = self.regex_entries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('fileEntries') is not None:
            self.file_entries = m.get('fileEntries')
        if m.get('dirEntries') is not None:
            self.dir_entries = m.get('dirEntries')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('regexEntries') is not None:
            self.regex_entries = m.get('regexEntries')
        return self


class GetListOfPurgeRequestsResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        purge_requests: List[GetListOfPurgeRequestsResponsePurgeRequests] = None,
    ):
        # {"en" : ">= 0 
        # Total number of purge requests matching the criteria specified in the query parameters. The actual number of entries in purgeRequests may be fewer if you specified the <limit> parameter.", "zh_CN": "取值范围: >= 0 
        # 刷新请求的总数。该数值取决于查询参数。"}
        self.count = count
        # {"en" : "List of purge requests.", "zh_CN": "刷新请求列表。"}
        self.purge_requests = purge_requests

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.purge_requests, 'purge_requests')
        if self.purge_requests:
            for k in self.purge_requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.purge_requests is not None:
            result['purgeRequests'] = []
            for k in self.purge_requests:
                result['purgeRequests'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('purgeRequests') is not None:
            self.purge_requests = []
            for k in m.get('purgeRequests'):
                temp_model = GetListOfPurgeRequestsResponsePurgeRequests()
                self.purge_requests.append(temp_model.from_map(k))
        return self






class CreateAPrefetchRequestPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPrefetchRequestParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPrefetchRequestRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPrefetchRequestRequestFileListHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "HTTP header name.", "zh_CN": "HTTP 头部名称。"}
        self.name = name
        # {"en" : "HTTP header value.", "zh_CN": "HTTP 头部值。"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateAPrefetchRequestRequestFileList(TeaModel):
    def __init__(
        self,
        url: str = None,
        headers: List[CreateAPrefetchRequestRequestFileListHeaders] = None,
    ):
        # {"en" : "Range: [ 10 .. 2048 ] characters 
        # A URL to prefetch. It must begin with 'http' or 'https' and can be up to 2048 characters.
        # ", "zh_CN": "取值范围: [ 10 .. 2048 ] 字符 
        # 预取的URL。必须以'http'或'https'开头，长度不超过2048个字符。"}
        self.url = url
        # {"en" : "If a URL's cache key depends on request headers, you can specify the header values that are applicable to prefetch one version of the URL.", "zh_CN": "如果需要在缓存键中加入请求头，可用该字段指定请求头。"}
        self.headers = headers

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = CreateAPrefetchRequestRequestFileListHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class CreateAPrefetchRequestRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        file_list: List[CreateAPrefetchRequestRequestFileList] = None,
        regions: List[str] = None,
        start_time: str = None,
        webhook: str = None,
    ):
        # {"en" : "Range: <= 1000 characters 
        # Enter a short description of the prefetch task.", "zh_CN": "取值范围: <= 1000 字符 
        # 预取请求的简短描述。"}
        self.name = name
        # {"en" : "", "zh_CN": ""}
        self.file_list = file_list
        # {"en" : "A list of continents representing the regions in which to perform the prefetch. Specify 'Mainland China' as the region, if prefetch by servers in mainland China only is desired. Omitting the field means the prefetch will be done by all regions' servers.", "zh_CN": "指定需要预取内容的大洲，以大洲英文全名表示，例如Asia, Europe。支持仅预取到中国大陆的服务器，区域名称以Mainland China表示。未指定区域时，表示预取内容到所有大洲的服务器。"}
        self.regions = regions
        # {"en" : "RFC 3339 date indicating when the prefetch should begin. This must be in UTC time, for example, '2021-03-06T00:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示开始预取的时间。必须使用UTC时间，例如'2021-03-06T00:00:00Z'。"}
        self.start_time = start_time
        # {"en" : "ID of a webhook to call when the purge task completes. Wehook menas the callback endpoint as created via the 'Create a webhook' API.", "zh_CN": "刷新任务完成时要调用的webhook的ID。webhook是指通过“创建webhook接口”创建的回调接口。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.file_list, 'file_list')
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.file_list is not None:
            result['fileList'] = []
            for k in self.file_list:
                result['fileList'].append(k.to_map() if k else None)
        if self.regions is not None:
            result['regions'] = self.regions
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileList') is not None:
            self.file_list = []
            for k in m.get('fileList'):
                temp_model = CreateAPrefetchRequestRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('regions') is not None:
            self.regions = m.get('regions')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class CreateAPrefetchRequestResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPrefetchRequestResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header is a URL representing the new prefetch request, for example, <code>Location: https://{domain}/cdn/prefetches/e91e8674-c2c5-4440-a1de-8b2ea99293dd</code>.", "zh_CN":"通过Location响应头返回新建的预取任务的URL。URL中包含预取任务的ID，可使用该ID调用'查询预取任务详情'接口来查看预取任务详情。URL示例：<code>Location: https://{domain}/cdn/prefetches/5dca2205f9e9cc0001df7b33"}
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






class GetAvailablePurgeRequestsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAvailablePurgeRequestsParameters(TeaModel):
    def __init__(
        self,
        target: str = None,
    ):
        # {"en" : "Enum: staging,production 
        # Default: production 
        # Indicates the environment.", "zh_CN": "取值范围: staging,production 
        # 默认值: production 
        # 指定环境查询可用额度，即演练环境或生产环境。"}
        self.target = target

    def validate(self):
        self.validate_required(self.target, 'target')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class GetAvailablePurgeRequestsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAvailablePurgeRequestsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAvailablePurgeRequestsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAvailablePurgeRequestsResponse(TeaModel):
    def __init__(
        self,
        file_purge_tokens: int = None,
        dir_purge_tokens: int = None,
    ):
        # {"en" : "Range: >= 0 
        # Number of file URL purge requests available.", "zh_CN": "取值范围: >= 0 
        # 文件刷新当前的可用额度。"}
        self.file_purge_tokens = file_purge_tokens
        # {"en" : "Range: >= 0 
        #  Number of directory URL purge requests available.", "zh_CN": "取值范围: >= 0 
        # 目录刷新当前的可用额度。"}
        self.dir_purge_tokens = dir_purge_tokens

    def validate(self):
        self.validate_required(self.file_purge_tokens, 'file_purge_tokens')
        self.validate_required(self.dir_purge_tokens, 'dir_purge_tokens')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_purge_tokens is not None:
            result['filePurgeTokens'] = self.file_purge_tokens
        if self.dir_purge_tokens is not None:
            result['dirPurgeTokens'] = self.dir_purge_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filePurgeTokens') is not None:
            self.file_purge_tokens = m.get('filePurgeTokens')
        if m.get('dirPurgeTokens') is not None:
            self.dir_purge_tokens = m.get('dirPurgeTokens')
        return self




