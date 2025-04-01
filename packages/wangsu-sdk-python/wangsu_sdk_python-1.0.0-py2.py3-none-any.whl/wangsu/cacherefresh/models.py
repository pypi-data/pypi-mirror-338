# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class RegexUrlPurgeRequest(TeaModel):
    def __init__(
        self,
        url_regulars: List[str] = None,
    ):
        # {"en":"To clean up the cached regular url collection, the format of the regular url is:
        # 1) The URL conforms to the regular expression. Enter the example: http://www.a.com/(.*).png. To push the http://www.abc.com/test/.*\\.txt regular expression, you need to escape the backslash when using the interface, ie http://www.abc.com/test/.*\\.txt.
        # 2) The domain name of each regular url must be the domain name accelerated by our company.
        # 3) The maximum length of each regular url is 2000 characters.
        # 4) If the regular url contains special characters, you need to escape and use utf-8 to escape
        # 5) The same regular URL, the system will go to heavy and submit.
        # 6) The default is 500 strips/day, which is the upper limit shared with the directory push.", "zh_CN":"要清理缓存的正则url集合，正则url的格式要求：
        # 1）URL 符合正则表达式，输入示例：http://www.a.com/(.*).png。如要推送&nbsp;http://www.abc.com/test/.*\\.txt&nbsp;正则表达式，在使用接口需要对反斜杠进行转义，即&nbsp;http://www.abc.com/test/.*\\.txt。
        # 2）每个正则url所在的域名必须是在我司加速的域名。
        # 3）每个正则url最大长度 2000 字符。
        # 4）正则url中如果包含特殊字符，需要进行转义，采用utf-8方式转义
        # 5) 相同的正则URL，系统会去重后提交。
        # 6）默认500条/天。"}
        self.url_regulars = url_regulars

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_regulars is not None:
            result['urlRegulars'] = self.url_regulars
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urlRegulars') is not None:
            self.url_regulars = m.get('urlRegulars')
        return self


class RegexUrlPurgeResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        item_id: str = None,
    ):
        # {'en':'Status code indicating the result of the task creation', 'zh_CN':'表示任务创建结果的状态码'}
        self.code = code
        # {'en':'Indicates the response message of the system after the task is submitted.', 'zh_CN':'表示任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'After the interface is called once and the task is successfully submitted, it will return an itemamId, which is the unique identifier of the task submitted at that time. The itemId can be used to query the status (success/failure) of the task in batches.', 'zh_CN':'调用一次接口并提交任务成功后，将返回一个iteamId，是当次提交任务的唯一标识，通过itemId可批量查询任务的状态（成功/失败）。'}
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


class RegexUrlPurgePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RegexUrlPurgeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RegexUrlPurgeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RegexUrlPurgeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PurgeRequest(TeaModel):
    def __init__(
        self,
        urls: List[str] = None,
        dirs: List[str] = None,
        url_action: str = None,
        dir_action: str = None,
    ):
        # {"en":"If you need to purge several cached URLs. The submitted URL should meet the following format requirements:
        # 1) The URL must start with \'http://\' or \'https://\', url example: http://www.a.com/image/test.png.
        # 2) Each url has a maximum length of 1000 characters.
        # 3) The domain in the URL is must be the domain of the CDN service.
        # Note: URLs and dirs cannot be empty at the same time.","zh_CN":"要清理缓存的url集合，url的格式要求：
        # 1）URL 必须以\'http://\' 或 \'https://\' 开头，输入示例：http://www.a.com/image/test.png。
        # 2）每个url最大长度 2000 字符。
        # 3）每个url所在的域名必须是在我司加速的域名。
        # 4）刷新url每日不超过5000条（账号粒度可调，可联系技术支持调整），
        # 5）每次接口调用urls和dirs的总数不超过500条。
        # 注意：urls和dirs不能同时为空。"}
        self.urls = urls
        # {"en":"Need to purge the cached directory collection, the submitted directory should meet the following format requirements:
        # 1) Must start with 'http://domain name/' and end with '/', such as refreshing all files under the directory test, the format of the submitted directory is: http://www.a.com/test/.
        # 2) Each directory has a maximum length of 1000 characters.
        # 3) The domain name in directory must be the domain name of the CDN service.", "zh_CN":"指要清理缓存的目录集合，dir的格式要求：
        # 1）必须以'http://域名/'开始，以'/'结尾， 如刷新目录test下所有文件，输入格式为：http://www.a.com/test/；
        # 2）每个目录最大长度 1000 字符。
        # 3）每个目录所在的域名必须是在我司加速的域名。
        # 4）目录刷新默认过期，不支持目录删除。
        # 5）刷新目录每日不超过500条（账号粒度可调，可联系技术支持调整）
        # 注意：urls和dirs不能同时为空。"}
        self.dirs = dirs
        # {"en":"1) default: default value, the url cache is processed using the pre-configured operation type of domain. When no value is assigned to this element or the element is not submitted, the configuration of domain is read by default.
        # 2) delete: ignore the operation type in the domain configuration, directly delete the cache file of the submitted url.
        # 3) expire: Ignore the operation type in the domain  configuration, and set the file with the cached commit url to expire. When there is a http access for the first time, a request is made to the origin server to check if the file is up-to-date. If the origin has a new file, the new version is directly pulled back from the source station and returned to the user. If there is no update, then the source station responds with http code 304, and the CDN provides the cache file in the edge node to the user.", "zh_CN":"仅对入参'urls'有效，指清理url缓存要以哪种类型操作：
        # 1）default：默认值，以频道预先配置好的操作类型处理url缓存，当不赋值或未传参时，默认取频道配置。
        # 2）delete：忽略频道配置里的操作类型，当前提交urls里的所有url，直接删除节点的缓存文件
        # 3）expire：忽略频道配置里的操作类型，当前提交urls里的所有url，将有缓存的节点置为过期，当第一次有访问时，回源站校验文件是否更新，有更新时从源站重新拉取新版本返回给客户，未有更新时则源站响应304，提供节点缓存文件给客户。"}
        self.url_action = url_action
        # {"en":"It refers to the type of operation to clean up the dir cache, which is only valid for dirs elements. When no assignment or parameters are passed, the default channel configuration is selected. The optional values of this parameter are as follows:
        # 1) delete: ignore the type of operation in the channel configuration, delete the cache directory of the node directly.
        # 2) expire: ignore the type of operation in the channel configuration, set the cached node to expire, when the first visit, check whether the directory of the source station is updated, when there is an update, retrieve the new version from the source station to return to the customer, and when there is no update, the source station responds 304, providing the cached directory of the node to the customer.
        # Note: The use of directory delete function will result in all files cached in the directory empty, all files need to be retrieved, resulting in increased backsource bandwidth. Because of the high risk, the permission does not open by default. If you need to open this function, please contact the corresponding customer service technical support to apply for opening. Only the customer\'s account can be transferred to delete after opening.","zh_CN":"指清理dir缓存要以哪种类型操作，仅对dirs元素有效，当不赋值或未传参时，默认取频道配置。该参数可选值如下：
        # 1）delete：忽略频道配置里的操作类型，直接删除节点的缓存目录。
        # 2）expire：忽略频道配置里的操作类型，将有缓存的节点置为过期，当第一次有访问时，回源站校验目录是否更新，有更新时从源站重新拉取新版本返回给客户，未有更新时则源站响应304，提供节点缓存目录给客户。
        # 注：使用目录删除（delete）功能，会导致该目录下所有文件缓存全部清空，所有文件需要重新回源拉取，造成回源带宽增加。由于风险较大，该权限默认不开启，如需开启该功能，请联系对应的客服技术支持进行申请开启，开通后只有该客户的账号才能传入delete。"}
        self.dir_action = dir_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.urls is not None:
            result['urls'] = self.urls
        if self.dirs is not None:
            result['dirs'] = self.dirs
        if self.url_action is not None:
            result['urlAction'] = self.url_action
        if self.dir_action is not None:
            result['dirAction'] = self.dir_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        if m.get('dirs') is not None:
            self.dirs = m.get('dirs')
        if m.get('urlAction') is not None:
            self.url_action = m.get('urlAction')
        if m.get('dirAction') is not None:
            self.dir_action = m.get('dirAction')
        return self


class PurgeResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        item_id: str = None,
    ):
        # {"en":"The status code of the task creation result, 1 means success, 0 means failure.","zh_CN":"表示任务创建结果的状态码，1表示成功，0表示失败"}
        self.code = code
        # {"en":"Content system response message after submitting the task.", "zh_CN":"表示任务提交后，系统的响应消息"}
        self.message = message
        # {"en":"After calling the API once and submitting the task successfully, the content system will return an itemId. This ID is the unique identifier for each submission. You can use itemId to batch query the status (success/failure) of the task.", "zh_CN":"调用一次接口并提交任务成功后，将返回一个iteamId，是当次提交任务的唯一标识，通过itemId可批量查询任务的状态（成功/失败）。"}
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


class PurgePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryPurgeResidualsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeResidualsResponse(TeaModel):
    def __init__(
        self,
        supplier: str = None,
        code: int = None,
        message: str = None,
        url_upper: int = None,
        dir_upper: int = None,
        url_remain: int = None,
        dir_remain: int = None,
        tag_upper: int = None,
        tag_remain: int = None,
    ):
        # {'en':'It is the logo of our company.', 'zh_CN':'数据提供方'}
        self.supplier = supplier
        # {'en':'The status code of the query result. 0 means success, 1 means failure.', 'zh_CN':'查询结果，0表示成功，1表示失败'}
        self.code = code
        # {'en':'Content system response message after query.', 'zh_CN':'查询的响应消息'}
        self.message = message
        # {'en':'The maximum number of the purge url today.', 'zh_CN':'当天url刷新任务允许提交的最大数量'}
        self.url_upper = url_upper
        # {'en':'The maximum number of the purge directory today.', 'zh_CN':'当天目录刷新任务允许提交的最大数量'}
        self.dir_upper = dir_upper
        # {'en':'The number of urls that can be purged today.', 'zh_CN':'当天url刷新任务允许提交的剩余数量'}
        self.url_remain = url_remain
        # {'en':'The number of directorys that can be purged today.', 'zh_CN':'当天目录刷新任务允许提交的剩余数量'}
        self.dir_remain = dir_remain
        # {'en':'The maximum number of the purge tag today.', 'zh_CN':'当天tag任务允许提交的最大数量'}
        self.tag_upper = tag_upper
        # {'en':'The number of urls that can be purged tag today.', 'zh_CN':'当天tag任务允许提交的剩余数量'}
        self.tag_remain = tag_remain

    def validate(self):
        self.validate_required(self.supplier, 'supplier')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.url_upper, 'url_upper')
        self.validate_required(self.dir_upper, 'dir_upper')
        self.validate_required(self.url_remain, 'url_remain')
        self.validate_required(self.dir_remain, 'dir_remain')
        self.validate_required(self.tag_upper, 'tag_upper')
        self.validate_required(self.tag_remain, 'tag_remain')

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
        if self.url_upper is not None:
            result['urlUpper'] = self.url_upper
        if self.dir_upper is not None:
            result['dirUpper'] = self.dir_upper
        if self.url_remain is not None:
            result['urlRemain'] = self.url_remain
        if self.dir_remain is not None:
            result['dirRemain'] = self.dir_remain
        if self.tag_upper is not None:
            result['tagUpper'] = self.tag_upper
        if self.tag_remain is not None:
            result['tagRemain'] = self.tag_remain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('urlUpper') is not None:
            self.url_upper = m.get('urlUpper')
        if m.get('dirUpper') is not None:
            self.dir_upper = m.get('dirUpper')
        if m.get('urlRemain') is not None:
            self.url_remain = m.get('urlRemain')
        if m.get('dirRemain') is not None:
            self.dir_remain = m.get('dirRemain')
        if m.get('tagUpper') is not None:
            self.tag_upper = m.get('tagUpper')
        if m.get('tagRemain') is not None:
            self.tag_remain = m.get('tagRemain')
        return self


class QueryPurgeResidualsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeResidualsParameters(TeaModel):
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


class QueryPurgeResidualsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeResidualsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PurgeFileWithTagRequest(TeaModel):
    def __init__(
        self,
        tag: str = None,
        action: str = None,
    ):
        # {"en":"Tag value:
        # 1. Multiple tag values are available, separated, and a maximum of 30 values are allowed
        # 2. The maximum length of each tag value is 128 characters
        # 3. Characters not allowed in tag values are: Chinese, <whitespace> and '*''(),:;&lt;=&gt;?@[]{}<>'", "zh_CN":"tag的值：
        # 1.多个tag值用,隔开,最大允许30个值
        # 2.每个tag值最大长度为128字符
        # 3.不允许特殊字符，特殊字符是指：中文，空格符及*''(),:;&lt;=&gt;?@[]{}<>"}
        self.tag = tag
        # {'en':'Refresh action,If not filled, the default is to delete, 0 is deleted; 1 is expired', 'zh_CN':'刷新动作
        # 1、不填的话默认是删除
        # 2、0代表删除；1代表过期'}
        self.action = action

    def validate(self):
        self.validate_required(self.tag, 'tag')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['tag'] = self.tag
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class PurgeFileWithTagResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        item_id: str = None,
    ):
        # {'en':'code', 'zh_CN':'表示任务创建结果的状态码'}
        self.code = code
        # {'en':'message', 'zh_CN':'表示任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'itemId', 'zh_CN':'调用一次接口并提交任务成功后，将返回一个iteamId，是当次提交任务的唯一标识，通过itemId可批量查询任务的状态（成功/失败）。'}
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


class PurgeFileWithTagPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeFileWithTagParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeFileWithTagRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PurgeFileWithTagResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryPurgeLimitRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeLimitResponse(TeaModel):
    def __init__(
        self,
        url_upper: int = None,
        url_remain: int = None,
        dir_upper: int = None,
        dir_remain: int = None,
        regex_upper: int = None,
        regex_remain: int = None,
        tag_upper: int = None,
        tag_remain: int = None,
        code: int = None,
        message: str = None,
        supplier: str = None,
    ):
        # {'en':'url purge daily limit','zh_CN':'url 每日上限'}
        self.url_upper = url_upper
        # {'en':'url purge remain','zh_CN':'url每日剩余量'}
        self.url_remain = url_remain
        # {'en':'dir purge daily limit','zh_CN':'目录每日上限'}
        self.dir_upper = dir_upper
        # {'en':'dir purge remain','zh_CN':'目录每日剩余量'}
        self.dir_remain = dir_remain
        # {'en':'regex purge daily limit','zh_CN':'正则每日上限'}
        self.regex_upper = regex_upper
        # {'en':'regex purge remain','zh_CN':'正则每日剩余量'}
        self.regex_remain = regex_remain
        # {'en':'tag purge daily limit','zh_CN':'tag每日上限'}
        self.tag_upper = tag_upper
        # {'en':'tag purge remain','zh_CN':'tag每日剩余量'}
        self.tag_remain = tag_remain
        # {'en':'error code','zh_CN':'错误码'}
        self.code = code
        # {'en':'message','zh_CN':'错误信息'}
        self.message = message
        # {'en':'supplier','zh_CN':'供应方'}
        self.supplier = supplier

    def validate(self):
        self.validate_required(self.url_upper, 'url_upper')
        self.validate_required(self.url_remain, 'url_remain')
        self.validate_required(self.dir_upper, 'dir_upper')
        self.validate_required(self.dir_remain, 'dir_remain')
        self.validate_required(self.regex_upper, 'regex_upper')
        self.validate_required(self.regex_remain, 'regex_remain')
        self.validate_required(self.tag_upper, 'tag_upper')
        self.validate_required(self.tag_remain, 'tag_remain')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.supplier, 'supplier')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_upper is not None:
            result['urlUpper'] = self.url_upper
        if self.url_remain is not None:
            result['urlRemain'] = self.url_remain
        if self.dir_upper is not None:
            result['dirUpper'] = self.dir_upper
        if self.dir_remain is not None:
            result['dirRemain'] = self.dir_remain
        if self.regex_upper is not None:
            result['regexUpper'] = self.regex_upper
        if self.regex_remain is not None:
            result['regexRemain'] = self.regex_remain
        if self.tag_upper is not None:
            result['tagUpper'] = self.tag_upper
        if self.tag_remain is not None:
            result['tagRemain'] = self.tag_remain
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.supplier is not None:
            result['supplier'] = self.supplier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urlUpper') is not None:
            self.url_upper = m.get('urlUpper')
        if m.get('urlRemain') is not None:
            self.url_remain = m.get('urlRemain')
        if m.get('dirUpper') is not None:
            self.dir_upper = m.get('dirUpper')
        if m.get('dirRemain') is not None:
            self.dir_remain = m.get('dirRemain')
        if m.get('regexUpper') is not None:
            self.regex_upper = m.get('regexUpper')
        if m.get('regexRemain') is not None:
            self.regex_remain = m.get('regexRemain')
        if m.get('tagUpper') is not None:
            self.tag_upper = m.get('tagUpper')
        if m.get('tagRemain') is not None:
            self.tag_remain = m.get('tagRemain')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')
        return self


class QueryPurgeLimitPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeLimitParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeLimitRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeLimitResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryPurgeStatusRequest(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        item_id: str = None,
        url: str = None,
        status: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # {'en':'Start time of task creation,The format is yyyy-MM-dd HH:MM:ss; For example 2017-01-10 06:33:26,Can only query refresh tasks within 3 days.', 'zh_CN':'任务创建开始时间，格式为yyyy-MM-dd HH:mm:ss；例如 2017-01-10 06:33:26，只能查询3天之内的刷新任务。'}
        self.start_time = start_time
        # {'en':'End time of task creation,The format is yyyy-MM-dd HH:MM:ss; For example 2017-01-10 06:33:26', 'zh_CN':'任务创建结束时间，格式为yyyy-MM-dd HH:mm:ss；例如 2017-01-10 06:33:26，'}
        self.end_time = end_time
        # {'en':'A unique identifier for the same batch of tasks. If you submit multiple URLs from an API request, the ID is a unique number for these tasks.Query tasks by batch, such as submitting 10 url refreshes at a time. After successful submission, the content management system will return an itemId in the response message.', 'zh_CN':'表示任务单次提交多个url时任务的唯一标识。按批次查询任务，如单次提交10条url刷新，提交成功后内容管理系统将返回一个itemId在响应消息里。itemId 和 查询起止时间不能同时为空。'}
        self.item_id = item_id
        # {'en':'The cached url needs to be refreshed (url type could be directory, regular file, tag, and common file), and a single call allows only one url to be entered', 'zh_CN':'需要刷新缓存的url(支持目录、正则、tag、文件)，单次调用只允许输入一条url'}
        self.url = url
        # {'en':'Task status. The system allows you to select a task status query. These states can be queried:Success: Purge success.Failure: Purge failed.Wait: The purge task is waiting to be processed.Run: The purge task is being executed.', 'zh_CN':'任务状态，允许指定任务状态过滤，支持查询的状态有：1）success2）failure3）wait4）run'}
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


class QueryPurgeStatusResultDetail(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        create_time: str = None,
        finish_time: str = None,
        rate: str = None,
        status: str = None,
        url: str = None,
        is_dir: int = None,
    ):
        # {'en':'Time for content management system to start cache refresh task', 'zh_CN':'内容管理系统开始执行缓存刷新任务的时间'}
        self.begin_time = begin_time
        # {'en':'Time the content management system creates a cache refresh task', 'zh_CN':'内容管理系统创建缓存刷新任务的时间'}
        self.create_time = create_time
        # {'en':'Content management system executes and summarizes the completion time of cache refresh tasks', 'zh_CN':'内容管理系统执行并汇总缓存刷新任务的完成时间'}
        self.finish_time = finish_time
        # {'en':'Success rate for performing cache refresh tasks, such as 98%, the value is 98', 'zh_CN':'执行缓存刷新任务的成功率，如98%，则值为98'}
        self.rate = rate
        # {'en':'Cache refresh task execution status, which has the following states:Success: Indicates that the task that refreshes the file cache has performed successfully Failure:  Indicates that the task that refreshes the file cache has performed failed Wait: Indicates that the task of refreshing the cache is in the queue Run: Indicates that the task of refreshing the cache is in progress', 'zh_CN':'缓存刷新任务执行的状态，有以下几种状态：success：表示刷新文件缓存的任务执行成功 failure：表示刷新文件缓存的任务执行失败 wait：表示刷新缓存的任务正在排队中 run：表示刷新缓存的任务正在执行中'}
        self.status = status
        # {'en':'Refresh the cache of a file or directory.', 'zh_CN':'执行缓存刷新的具体文件或目录'}
        self.url = url
        # {'en':'The operation type of the purge task:0: Refresh a specific file 1:  regular file 2: Refresh all files in a directory 3: Refresh  a tag', 'zh_CN':'刷新任务的操作类型：0：刷新某个具体文件 1：正则文件 2：刷新某个目录下的所有文件 3：刷新某个tag'}
        self.is_dir = is_dir

    def validate(self):
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.status, 'status')
        self.validate_required(self.url, 'url')
        self.validate_required(self.is_dir, 'is_dir')

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
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
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
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        return self


class QueryPurgeStatusResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        code: int = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        result_detail: List[QueryPurgeStatusResultDetail] = None,
    ):
        # {'en':'The number of results for this query, count for 10 if 10 tasks are eligible for a query', 'zh_CN':'本次查询结果的数量，如有10个任务符合查询条件，则count的值为10'}
        self.count = count
        # {"en":"After the task commits, the system's response code, 0 means failure, and 1 means success", "zh_CN":"任务提交后，系统的响应码，0表示失败，1表示成功"}
        self.code = code
        # {'en':'System response message after task submit.', 'zh_CN':'任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'Total page count of task query results', 'zh_CN':'任务查询结果的总页数'}
        self.page_no = page_no
        # {'en':'How many refresh task data per page', 'zh_CN':'每页显示多少条刷新任务数据'}
        self.page_size = page_size
        # {'en':'Set of task results', 'zh_CN':'任务结果的集合'}
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
                temp_model = QueryPurgeStatusResultDetail()
                self.result_detail.append(temp_model.from_map(k))
        return self


class QueryPurgeStatusPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeStatusParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeStatusRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryPurgeStatusResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




