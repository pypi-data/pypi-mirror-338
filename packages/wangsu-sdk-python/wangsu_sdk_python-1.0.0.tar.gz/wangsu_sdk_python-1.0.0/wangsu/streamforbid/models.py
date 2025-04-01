# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class StopLivestreamingRequest(TeaModel):
    def __init__(
        self,
        live_url: str = None,
        type: str = None,
    ):
        # {"en":"Push  or pull  address complete url, URL format requirements:
        # 1) The URL must start with'http:/'or'https:/' or'rtmp', and enter an example: http://www.a.com/live/201802221082.
        # 2) The maximum length of each URL is 1000 characters.
        # 3) The domain name of each URL must be the domain name of our company which is speeded up by live broadcasting.
        # 4) If a question mark is included in the url, only the URL before the question mark is submitted.", "zh_CN":"推流或拉流的地址完整的url，url的格式要求：
        # 1）URL 必须以'http://' 或 'https://' 或&lsquo;rtmp&rsquo;开头，输入示例：http://www.a.com/live/201802221082。
        # 2）每个url最大长度 1000 字符。
        # 3）每个url所在的域名必须是在我司直播加速的域名。
        # 4）url中如果包含问号，则只需提交问号前面的url。"}
        self.live_url = live_url
        # {'en':'The values are: play (back-source pull), publish (live push).', 'zh_CN':'值为：play (回源拉流)，publish(直播推流)。'}
        self.type = type

    def validate(self):
        self.validate_required(self.live_url, 'live_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_url is not None:
            result['liveUrl'] = self.live_url
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveUrl') is not None:
            self.live_url = m.get('liveUrl')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class StopLivestreamingResponse(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
    ):
        # {'en':'message', 'zh_CN':'错误信息'}
        self.message = message
        # {'en':'code', 'zh_CN':'错误码'}
        self.code = code

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class StopLivestreamingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopLivestreamingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopLivestreamingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StopLivestreamingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryForbidLivestreamRecordRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        url: str = None,
    ):
        # {'en':'channel', 'zh_CN':'加速域名，如果账号没有域名权限，调用成功但接口会返回错误的提示信息。注：一次只能查询一个域名'}
        self.channel = channel
        # {'en':'url,Complete push stream or pull stream url', 'zh_CN':'推流或拉流的地址完整的url，即具体某个直播的频道url'}
        self.url = url

    def validate(self):
        self.validate_required(self.channel, 'channel')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class QueryForbidLivestreamRecordResultDetail(TeaModel):
    def __init__(
        self,
        channel: str = None,
        url: str = None,
        start_time: str = None,
        end_time: str = None,
        ip: str = None,
    ):
        # {'en':'channel', 'zh_CN':'禁止推流或拉流的域名'}
        self.channel = channel
        # {'en':'url', 'zh_CN':'禁止推流或拉流的地址完整的url'}
        self.url = url
        # {'en':'start time, format:1532413615', 'zh_CN':'开始禁止播放流的时间，格式为 1532413615'}
        self.start_time = start_time
        # {'en':'end time,format:1532413615', 'zh_CN':'流恢复播放的时间，例如 1532413615'}
        self.end_time = end_time
        # {'en':'ip of forbidden user', 'zh_CN':'禁止某个客户观看直播的用户IP'}
        self.ip = ip

    def validate(self):
        self.validate_required(self.channel, 'channel')
        self.validate_required(self.url, 'url')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.url is not None:
            result['url'] = self.url
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class QueryForbidLivestreamRecordResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result_detail: List[QueryForbidLivestreamRecordResultDetail] = None,
    ):
        # {'en':'result code,00 means success', 'zh_CN':'表示提交结果，00表示成功'}
        self.code = code
        # {'en':'result message', 'zh_CN':'表示任务提交后，系统的响应消息'}
        self.message = message
        # {'en':'Set of task results', 'zh_CN':'任务结果的集合'}
        self.result_detail = result_detail

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
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
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.result_detail is not None:
            result['resultDetail'] = []
            for k in self.result_detail:
                result['resultDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('resultDetail') is not None:
            self.result_detail = []
            for k in m.get('resultDetail'):
                temp_model = QueryForbidLivestreamRecordResultDetail()
                self.result_detail.append(temp_model.from_map(k))
        return self


class QueryForbidLivestreamRecordPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbidLivestreamRecordParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbidLivestreamRecordRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryForbidLivestreamRecordResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ForbidLivestreamingRequest(TeaModel):
    def __init__(
        self,
        live_url: str = None,
        reltime: str = None,
        abstime_start: str = None,
        abstime_end: str = None,
        type: str = None,
    ):
        # {"en":"'Only one URL can be submitted at a time, the address of push or pull flow is complete, URL format requirements:
        # 1) The URL must start with'http:/'or'https:/' or'rtmp', and enter an example: http://www.a.com/live/201802221082.
        # 2) The maximum length of each URL is 1000 characters.
        # 3) If a question mark is included in the url, only the URL before the question mark is submitted.
        # 4) Maximum 500 times a day. '", "zh_CN":"一次只能提交一个url，推流或拉流的地址完整的url，url的格式要求：
        # 
        # 1）URL 必须以'http://' 或 'https://' 或&lsquo;rtmp&rsquo;开头，输入示例：http://www.a.com/live/201802221082。
        # 
        # 2）每个url最大长度 1000 字符。
        # 
        # 3）url中如果包含问号，则只需提交问号前面的url。
        # 
        # 4）每天最大500次，禁止，恢复，停止3个操作共用上限。"}
        self.live_url = live_url
        # {"en":"Relative time, the time interval in which the operation takes effect, is calculated from the current time.
        # Unit: seconds
        # For example: reltime = 300, from the current time to ban 300 seconds
        # Note:
        # 1) When both abstime_end and reltime parameters are passed, only reltime parameters are valid.
        # 2) When reltime, abstime_end and reltime parameters are not set, the default one-day ban is applied.
        # 3) When reltime is less than or equal to 0, it is set to 1 day.
        # 4) When reltime is greater than 30 days, it is set to 30 days.'", "zh_CN":"相对时间，表示操作生效的时间区间，从当前时间开始计算。
        # 单位为：秒
        # 如：reltime=300，从当前时间开始禁播300s
        # 
        # 注：
        # 
        # 1)abstime_end和reltime参数都传时，仅reltime参数有效
        # 
        # 2)reltime、abstime_end和reltime参数都没有设置时，默认禁播1天
        # 
        # 3)reltime小于等于0时，会设置为1天
        # 
        # 4)reltime大于30天时，会设置为30天"}
        self.reltime = reltime
        # {'en':'Start time, only support current time,not future time; use with abstime_end parameter in seconds;
        # The time format is yyyymmddHMMSS or 10-digit UNIX timestamp, such as 20140306121035, 1511256503.
        # Abstime_start < current time or abstime_start is empty, default starts at current time.
        # Note:
        # 1) When both abstime_end and reltime parameters are passed, only reltime parameters are valid.
        # 2) When reltime, abstime_end and reltime parameters are not set, the default one-day ban is applied.
        # 3) abstime_start is larger than the current time of 30 days and will report errors.', 'zh_CN':'开始时间，只支持从当前时间开始，不支持未来时间；与abstime_end参数配合使用，单位为：秒； 
        # 时间格式为：yyyymmddHHMMSS或10进制unix时间戳，如：20140306121035、1511256503
        # abstime_start < 当前时间 或 abstime_start 为空 时，默认从当前时间开始。
        # 
        # 注：
        # 
        # 1)abstime_end和reltime参数都传时，仅reltime参数有效
        # 
        # 2)reltime、abstime_end和reltime参数都没有设置时，默认禁播1天
        # 
        # 3)abstime_start 大于当前时间30天，会报错'}
        self.abstime_start = abstime_start
        # {'en':'End time, specify the end time point of the operation, and use it with abstime_start parameter in seconds.
        # The time format is yyyymmddHMMSS or 10-digit UNIX timestamp, such as 20140306121535, 1511256503.
        # When abstime_end < current time, the parameter is invalid.
        # Note:
        # 1) When both abstime_end and reltime parameters are passed, only reltime parameters are valid.
        # 2) When reltime, abstime_end and reltime parameters are not set, the default one-day ban is applied.
        # 3) When abstime_end is free, if abstime_start is empty, the duration of forbidden sowing is one day longer than the current time; if abstime_start is valuable, the duration of forbidden sowing is one day longer than abstime_start.
        # 4) When abstime_end is less than the current time, an error is reported.
        # 5) When abstime_end is greater than the current time of 30 days, the duration of banning broadcasting is set as: current time + 30 days.', 'zh_CN':'结束时间，指定操作生效结束时间点；与abstime_start参数配合使用，单位为：秒；
        # 时间格式为：yyyymmddHHMMSS或10进制unix时间戳，如：20140306121535、1511256503
        # abstime_end < 当前时间 时，参数无效。
        # 
        # 注：
        # 
        # 1)abstime_end和reltime参数都传时，仅reltime参数有效
        # 2)reltime、abstime_end和reltime参数都没有设置时，默认禁播1天
        # 3)当abstime_end有空时，如果abstime_start为空，则禁播时长是当前时间加1天；若abstime_start有值，则禁播时长是abstime_start加1天
        # 4)当abstime_end小于当前时间，报错。
        # 5)当abstime_end 大于当前时间30天，则禁播时长会设置为：当前时间+30天'}
        self.abstime_end = abstime_end
        # {'en':'The values are: play (back-source pull), publish (live push).', 'zh_CN':'值为：play (回源拉流)，publish(直播推流)。'}
        self.type = type

    def validate(self):
        self.validate_required(self.live_url, 'live_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_url is not None:
            result['liveUrl'] = self.live_url
        if self.reltime is not None:
            result['reltime'] = self.reltime
        if self.abstime_start is not None:
            result['abstimeStart'] = self.abstime_start
        if self.abstime_end is not None:
            result['abstimeEnd'] = self.abstime_end
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveUrl') is not None:
            self.live_url = m.get('liveUrl')
        if m.get('reltime') is not None:
            self.reltime = m.get('reltime')
        if m.get('abstimeStart') is not None:
            self.abstime_start = m.get('abstimeStart')
        if m.get('abstimeEnd') is not None:
            self.abstime_end = m.get('abstimeEnd')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ForbidLivestreamingResponse(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
    ):
        # {'en':'message', 'zh_CN':'错误信息'}
        self.message = message
        # {'en':'code', 'zh_CN':'错误码'}
        self.code = code

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class ForbidLivestreamingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidLivestreamingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidLivestreamingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ForbidLivestreamingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ResumeLivestreamingRequest(TeaModel):
    def __init__(
        self,
        live_url: str = None,
        type: str = None,
    ):
        # {"en":"Push  or pull  address complete url, URL format requirements:
        # 1) The URL must start with'http:/'or'https:/' or'rtmp', and enter an example: http://www.a.com/live/201802221082.
        # 2) The maximum length of each URL is 1000 characters.
        # 3) The domain name of each URL must be the domain name of our company which is speeded up by live broadcasting.
        # 4) If a question mark is included in the url, only the URL before the question mark is submitted.", "zh_CN":"推流或拉流的地址完整的url，url的格式要求：
        # 1）URL 必须以'http://' 或 'https://' 或&lsquo;rtmp&rsquo;开头，输入示例：http://www.a.com/live/201802221082。
        # 2）每个url最大长度 1000 字符。
        # 3）每个url所在的域名必须是在我司直播加速的域名。
        # 4）url中如果包含问号，则只需提交问号前面的url。"}
        self.live_url = live_url
        # {"en":"The values are: play (back-source pull), publish (live push).", "zh_CN":"值为：play (回源拉流)，publish(直播推流)。"}
        self.type = type

    def validate(self):
        self.validate_required(self.live_url, 'live_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_url is not None:
            result['liveUrl'] = self.live_url
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liveUrl') is not None:
            self.live_url = m.get('liveUrl')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ResumeLivestreamingResponse(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
    ):
        # {'en':'message', 'zh_CN':'错误信息'}
        self.message = message
        # {'en':'error code', 'zh_CN':'错误码'}
        self.code = code

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class ResumeLivestreamingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResumeLivestreamingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResumeLivestreamingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResumeLivestreamingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




