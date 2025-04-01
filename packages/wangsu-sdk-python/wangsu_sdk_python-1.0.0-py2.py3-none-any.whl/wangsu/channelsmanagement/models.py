# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetChannelShareUrlRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Channel push ID", "zh_CN":"频道推流 ID"}
        self.pull_id = pull_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetChannelShareUrlResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"200 success", "zh_CN":"200，操作成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"分享页url"}
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


class GetChannelShareUrlPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelShareUrlParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelShareUrlRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelShareUrlResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetChannelListRequest(TeaModel):
    def __init__(
        self,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
        app_scenario: str = None,
    ):
        # {"en":"Gets the sorting of the channel list, default is 0;
        # 0. In descending order by creation time; 1. In ascending order by creation time", "zh_CN":"获取频道列表的排序，默认为 0； 
        # 0、按创建时间降序，1、按创建时间升序 "}
        self.list_order = list_order
        # {"en":"The number of pages in the channel page list, starting from 1; Default 1", "zh_CN":"频道分页列表中第几页，从 1 开始取值；默认 1"}
        self.page_index = page_index
        # {"en":"Average number of channels per page. The default value is 10. The value ranges from 1 to 50", "zh_CN":"平均每页频道数量，默认为 10，取值在 1-50 之间"}
        self.page_size = page_size
        # {"en":"Application scenario", "zh_CN":"应用场景 "}
        self.app_scenario = app_scenario

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.app_scenario is not None:
            result['appScenario'] = self.app_scenario
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('appScenario') is not None:
            self.app_scenario = m.get('appScenario')
        return self


class GetChannelListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: 'GetChannelListDataList' = None,
        message: str = None,
    ):
        # {'en':'code', 'zh_CN':'返回状态码'}
        self.code = code
        self.data = data
        # {'en':'message', 'zh_CN':'返回消息'}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetChannelListDataList()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetChannelListChannelList(TeaModel):
    def __init__(
        self,
        app_scenario: str = None,
        channel_name: str = None,
        channel_status: int = None,
        channel_type: str = None,
        create_time: str = None,
        directory_id: str = None,
        live_2vod: str = None,
        pull_id: str = None,
        push_url: str = None,
        srt_push_url: str = None,
        user_id: str = None,
    ):
        # {"en":"Application scenario", "zh_CN":"应用场景"}
        self.app_scenario = app_scenario
        # {"en":"Channel name", "zh_CN":"频道名称"}
        self.channel_name = channel_name
        # {"en":"Channel current live status;
        # 1:live broadcast 2:not broadcast 3:banned", "zh_CN":"频道当前直播状态； 
        # 1、直播中   2、未开播  3、禁播 "}
        self.channel_status = channel_status
        # {"en":"Channel type", "zh_CN":"频道类型"}
        self.channel_type = channel_type
        # {"en":"Channel creation time, for example, 2016-05-08 12:00:00", "zh_CN":"频道创建时间，例如：2016-05-08 12:00:00"}
        self.create_time = create_time
        # {"en":"Recorded directory ID. The value is returned only when the value-added service of recorded directory management is enabled and the recorded directory is configured for the channel.", "zh_CN":"录制目录 ID，有开通录制目录管理增值服务且有给频道配置过录制目录才会有返回值。"}
        self.directory_id = directory_id
        # {"en":"If it is enabled, push it and record it. If 1 is enabled, 0 is disabled.", "zh_CN":"是否开启即推即录，1 开启，0 未开启。"}
        self.live_2vod = live_2vod
        # {"en":"Pull flow ID", "zh_CN":"拉流 ID"}
        self.pull_id = pull_id
        # {"en":"Push URL", "zh_CN":"推流 URL"}
        self.push_url = push_url
        # {"en":"The URL is in SRT format", "zh_CN":"SRT 格式的推流 URL"}
        self.srt_push_url = srt_push_url
        # {"en":"User ID for creating a channel", "zh_CN":"创建频道的用户 ID"}
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.app_scenario, 'app_scenario')
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.channel_status, 'channel_status')
        self.validate_required(self.channel_type, 'channel_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.live_2vod, 'live_2vod')
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.push_url, 'push_url')
        self.validate_required(self.srt_push_url, 'srt_push_url')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_scenario is not None:
            result['appScenario'] = self.app_scenario
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.channel_status is not None:
            result['channelStatus'] = self.channel_status
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.live_2vod is not None:
            result['live2vod'] = self.live_2vod
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.push_url is not None:
            result['pushUrl'] = self.push_url
        if self.srt_push_url is not None:
            result['srtPushUrl'] = self.srt_push_url
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appScenario') is not None:
            self.app_scenario = m.get('appScenario')
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('channelStatus') is not None:
            self.channel_status = m.get('channelStatus')
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('live2vod') is not None:
            self.live_2vod = m.get('live2vod')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('pushUrl') is not None:
            self.push_url = m.get('pushUrl')
        if m.get('srtPushUrl') is not None:
            self.srt_push_url = m.get('srtPushUrl')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetChannelListDataList(TeaModel):
    def __init__(
        self,
        channel_list: List[GetChannelListChannelList] = None,
        channel_toal: int = None,
    ):
        self.channel_list = channel_list
        # {'en':'The number of records currently returned for the channel list information. Note that the number of records returned here is only the number of records for the current page.', 'zh_CN':'当前返回的频道列表信息的记录数，注意这里返回的记录数只是当前页的记录数。'}
        self.channel_toal = channel_toal

    def validate(self):
        self.validate_required(self.channel_list, 'channel_list')
        if self.channel_list:
            for k in self.channel_list:
                if k:
                    k.validate()
        self.validate_required(self.channel_toal, 'channel_toal')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_list is not None:
            result['channelList'] = []
            for k in self.channel_list:
                result['channelList'].append(k.to_map() if k else None)
        if self.channel_toal is not None:
            result['channelToal'] = self.channel_toal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelList') is not None:
            self.channel_list = []
            for k in m.get('channelList'):
                temp_model = GetChannelListChannelList()
                self.channel_list.append(temp_model.from_map(k))
        if m.get('channelToal') is not None:
            self.channel_toal = m.get('channelToal')
        return self


class GetChannelListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetChannelConfRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream id, unique ID of the channel", "zh_CN":"拉流 id，频道的唯一 ID"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetChannelConfResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: 'GetChannelConfDataList' = None,
        message: str = None,
    ):
        # {'en':'Status code', 'zh_CN':'返回状态码'}
        self.code = code
        self.data = data
        # {'en':'Operational information', 'zh_CN':'操作信息'}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetChannelConfDataList()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetChannelConfPullUrlList(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        fluent_pull_url: str = None,
        fluent_zkgq_pull_url: str = None,
        hd_pull_url: str = None,
        hd_zkgq_pull_url: str = None,
        high_pull_url: str = None,
        high_zkgq_pull_url: str = None,
        origin_pull_url: str = None,
        origin_zkgq_pull_url: str = None,
        sd_pull_url: str = None,
        sd_zkgq_pull_url: str = None,
    ):
        # {"en":"Audio Url", "zh_CN":"音频Url"}
        self.audio_url = audio_url
        # {"en":"Smooth bit rate pull stream url", "zh_CN":"流畅码率拉流 url"}
        self.fluent_pull_url = fluent_pull_url
        # {"en":"Smooth bit rate (smart HD) pull stream url", "zh_CN":"流畅码率（智控高清）拉流 url"}
        self.fluent_zkgq_pull_url = fluent_zkgq_pull_url
        # {"en":"Ultra clear bit rate pull url", "zh_CN":"超清码率拉流 url "}
        self.hd_pull_url = hd_pull_url
        # {"en":"Ultra - clear bit rate (intelligent control HD) pull - stream url", "zh_CN":"超清码率（智控高清）拉流 url"}
        self.hd_zkgq_pull_url = hd_zkgq_pull_url
        # {"en":"Hd bit rate pull stream url", "zh_CN":"高清码率拉流 url"}
        self.high_pull_url = high_pull_url
        # {"en":"Hd bit rate (intelligent control HD) pull url", "zh_CN":"高清码率（智控高清）拉流 url"}
        self.high_zkgq_pull_url = high_zkgq_pull_url
        # {"en":"Source rate pull url", "zh_CN":"源码率拉流 url"}
        self.origin_pull_url = origin_pull_url
        # {"en":"Source rate (intelligent control HD) pull url", "zh_CN":"源码率（智控高清）拉流 url"}
        self.origin_zkgq_pull_url = origin_zkgq_pull_url
        # {"en":"Standard definition bit rate pull url", "zh_CN":"标清码率拉流 url"}
        self.sd_pull_url = sd_pull_url
        # {"en":"Standard definition code rate (intelligent control HD) pull url", "zh_CN":"标清码率（智控高清）拉流 url"}
        self.sd_zkgq_pull_url = sd_zkgq_pull_url

    def validate(self):
        self.validate_required(self.audio_url, 'audio_url')
        self.validate_required(self.fluent_pull_url, 'fluent_pull_url')
        self.validate_required(self.fluent_zkgq_pull_url, 'fluent_zkgq_pull_url')
        self.validate_required(self.hd_pull_url, 'hd_pull_url')
        self.validate_required(self.hd_zkgq_pull_url, 'hd_zkgq_pull_url')
        self.validate_required(self.high_pull_url, 'high_pull_url')
        self.validate_required(self.high_zkgq_pull_url, 'high_zkgq_pull_url')
        self.validate_required(self.origin_pull_url, 'origin_pull_url')
        self.validate_required(self.origin_zkgq_pull_url, 'origin_zkgq_pull_url')
        self.validate_required(self.sd_pull_url, 'sd_pull_url')
        self.validate_required(self.sd_zkgq_pull_url, 'sd_zkgq_pull_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url
        if self.fluent_pull_url is not None:
            result['fluentPullUrl'] = self.fluent_pull_url
        if self.fluent_zkgq_pull_url is not None:
            result['fluentZkgqPullUrl'] = self.fluent_zkgq_pull_url
        if self.hd_pull_url is not None:
            result['hdPullUrl'] = self.hd_pull_url
        if self.hd_zkgq_pull_url is not None:
            result['hdZkgqPullUrl'] = self.hd_zkgq_pull_url
        if self.high_pull_url is not None:
            result['highPullUrl'] = self.high_pull_url
        if self.high_zkgq_pull_url is not None:
            result['highZkgqPullUrl'] = self.high_zkgq_pull_url
        if self.origin_pull_url is not None:
            result['originPullUrl'] = self.origin_pull_url
        if self.origin_zkgq_pull_url is not None:
            result['originZkgqPullUrl'] = self.origin_zkgq_pull_url
        if self.sd_pull_url is not None:
            result['sdPullUrl'] = self.sd_pull_url
        if self.sd_zkgq_pull_url is not None:
            result['sdZkgqPullUrl'] = self.sd_zkgq_pull_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')
        if m.get('fluentPullUrl') is not None:
            self.fluent_pull_url = m.get('fluentPullUrl')
        if m.get('fluentZkgqPullUrl') is not None:
            self.fluent_zkgq_pull_url = m.get('fluentZkgqPullUrl')
        if m.get('hdPullUrl') is not None:
            self.hd_pull_url = m.get('hdPullUrl')
        if m.get('hdZkgqPullUrl') is not None:
            self.hd_zkgq_pull_url = m.get('hdZkgqPullUrl')
        if m.get('highPullUrl') is not None:
            self.high_pull_url = m.get('highPullUrl')
        if m.get('highZkgqPullUrl') is not None:
            self.high_zkgq_pull_url = m.get('highZkgqPullUrl')
        if m.get('originPullUrl') is not None:
            self.origin_pull_url = m.get('originPullUrl')
        if m.get('originZkgqPullUrl') is not None:
            self.origin_zkgq_pull_url = m.get('originZkgqPullUrl')
        if m.get('sdPullUrl') is not None:
            self.sd_pull_url = m.get('sdPullUrl')
        if m.get('sdZkgqPullUrl') is not None:
            self.sd_zkgq_pull_url = m.get('sdZkgqPullUrl')
        return self


class GetChannelConfPullConfigureList(TeaModel):
    def __init__(
        self,
        pull_domain: str = None,
        pull_protocol: str = None,
        pull_url_list: List[GetChannelConfPullUrlList] = None,
    ):
        # {"en":"Pull the live stream domain name", "zh_CN":"拉流域名"}
        self.pull_domain = pull_domain
        # {"en":"Pull-flow protocol", "zh_CN":"拉流协议"}
        self.pull_protocol = pull_protocol
        self.pull_url_list = pull_url_list

    def validate(self):
        self.validate_required(self.pull_domain, 'pull_domain')
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.pull_url_list, 'pull_url_list')
        if self.pull_url_list:
            for k in self.pull_url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_domain is not None:
            result['pullDomain'] = self.pull_domain
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.pull_url_list is not None:
            result['pullUrlList'] = []
            for k in self.pull_url_list:
                result['pullUrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullDomain') is not None:
            self.pull_domain = m.get('pullDomain')
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('pullUrlList') is not None:
            self.pull_url_list = []
            for k in m.get('pullUrlList'):
                temp_model = GetChannelConfPullUrlList()
                self.pull_url_list.append(temp_model.from_map(k))
        return self


class GetChannelConfPushConfigureInfo(TeaModel):
    def __init__(
        self,
        push_protocol: str = None,
        push_url: str = None,
    ):
        # {"en":"Push-flow protocol", "zh_CN":"推流协议"}
        self.push_protocol = push_protocol
        # {"en":"Push URL", "zh_CN":"推流 URL"}
        self.push_url = push_url

    def validate(self):
        self.validate_required(self.push_protocol, 'push_protocol')
        self.validate_required(self.push_url, 'push_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_protocol is not None:
            result['pushProtocol'] = self.push_protocol
        if self.push_url is not None:
            result['pushUrl'] = self.push_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pushProtocol') is not None:
            self.push_protocol = m.get('pushProtocol')
        if m.get('pushUrl') is not None:
            self.push_url = m.get('pushUrl')
        return self


class GetChannelConfSrtPullConfigureList(TeaModel):
    def __init__(
        self,
        pull_domain: str = None,
        pull_protocol: str = None,
        pull_url_list: List[GetChannelConfPullUrlList] = None,
    ):
        # {"en":"Pull the live stream domain name", "zh_CN":"拉流域名"}
        self.pull_domain = pull_domain
        # {"en":"Pull-flow protocol", "zh_CN":"拉流协议"}
        self.pull_protocol = pull_protocol
        self.pull_url_list = pull_url_list

    def validate(self):
        self.validate_required(self.pull_domain, 'pull_domain')
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.pull_url_list, 'pull_url_list')
        if self.pull_url_list:
            for k in self.pull_url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_domain is not None:
            result['pullDomain'] = self.pull_domain
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.pull_url_list is not None:
            result['pullUrlList'] = []
            for k in self.pull_url_list:
                result['pullUrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullDomain') is not None:
            self.pull_domain = m.get('pullDomain')
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('pullUrlList') is not None:
            self.pull_url_list = []
            for k in m.get('pullUrlList'):
                temp_model = GetChannelConfPullUrlList()
                self.pull_url_list.append(temp_model.from_map(k))
        return self


class GetChannelConfDataList(TeaModel):
    def __init__(
        self,
        app_scenario: str = None,
        channel_name: str = None,
        channel_status: int = None,
        create_time: str = None,
        create_user: str = None,
        directory_id: str = None,
        live_2vod: str = None,
        player_id: str = None,
        video_encrypted: int = None,
        hls_encrypt_duration: int = None,
        pull_configure_list: List[GetChannelConfPullConfigureList] = None,
        push_configure_info: List[GetChannelConfPushConfigureInfo] = None,
        srt_pull_configure_list: List[GetChannelConfSrtPullConfigureList] = None,
    ):
        # {"en":"Application scenario", "zh_CN":"应用场景"}
        self.app_scenario = app_scenario
        # {"en":"Channel name", "zh_CN":"频道名称"}
        self.channel_name = channel_name
        # {"en":"Live channel current status;
        # 1:live broadcast 2:not broadcast 3:banned", "zh_CN":"频道当前直播状态； 
        # 1、直播中   2、未开播  3、禁播 "}
        self.channel_status = channel_status
        # {"en":"Channel creation time, for example, 2016-05-08 12:00:00", "zh_CN":"频道创建时间，例如：2016-05-08 12:00:00"}
        self.create_time = create_time
        # {"en":"The user name who created the channel", "zh_CN":"创建频道的 userName"}
        self.create_user = create_user
        # {"en":"Recorded directory ID. The value is returned only when the value-added service of recorded directory management is enabled and the recorded directory is configured for the channel.", "zh_CN":"录制目录 ID，有开通录制目录管理增值服务且有给频道配置过录制目录才会有返回值。"}
        self.directory_id = directory_id
        # {"en":"If it is enabled, push it and record it. If 1 is enabled, 0 is disabled.", "zh_CN":"是否开启即推即录，1 开启，0 未开启。"}
        self.live_2vod = live_2vod
        # {"en":"The flash player ID used by the channel", "zh_CN":"频道使用的 flash 播放器 ID "}
        self.player_id = player_id
        # {"en":"Video stream encryption. 0: No encryption is required 1:HLS universal encryption 2:DRM encryption", "zh_CN":"视频流加密。0:不做任何加密 1:HLS通用加密 2:DRM加密"}
        self.video_encrypted = video_encrypted
        # {"en":"HLS universal encryption validity time (unit: second)", "zh_CN":"HLS通用加密有效时间（单位：秒）"}
        self.hls_encrypt_duration = hls_encrypt_duration
        self.pull_configure_list = pull_configure_list
        self.push_configure_info = push_configure_info
        self.srt_pull_configure_list = srt_pull_configure_list

    def validate(self):
        self.validate_required(self.app_scenario, 'app_scenario')
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.channel_status, 'channel_status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.live_2vod, 'live_2vod')
        self.validate_required(self.player_id, 'player_id')
        self.validate_required(self.video_encrypted, 'video_encrypted')
        self.validate_required(self.hls_encrypt_duration, 'hls_encrypt_duration')
        self.validate_required(self.pull_configure_list, 'pull_configure_list')
        if self.pull_configure_list:
            for k in self.pull_configure_list:
                if k:
                    k.validate()
        self.validate_required(self.push_configure_info, 'push_configure_info')
        if self.push_configure_info:
            for k in self.push_configure_info:
                if k:
                    k.validate()
        self.validate_required(self.srt_pull_configure_list, 'srt_pull_configure_list')
        if self.srt_pull_configure_list:
            for k in self.srt_pull_configure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_scenario is not None:
            result['appScenario'] = self.app_scenario
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.channel_status is not None:
            result['channelStatus'] = self.channel_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.live_2vod is not None:
            result['live2vod'] = self.live_2vod
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.video_encrypted is not None:
            result['videoEncrypted'] = self.video_encrypted
        if self.hls_encrypt_duration is not None:
            result['hlsEncryptDuration'] = self.hls_encrypt_duration
        if self.pull_configure_list is not None:
            result['pullConfigureList'] = []
            for k in self.pull_configure_list:
                result['pullConfigureList'].append(k.to_map() if k else None)
        if self.push_configure_info is not None:
            result['pushConfigureInfo'] = []
            for k in self.push_configure_info:
                result['pushConfigureInfo'].append(k.to_map() if k else None)
        if self.srt_pull_configure_list is not None:
            result['srtPullConfigureList'] = []
            for k in self.srt_pull_configure_list:
                result['srtPullConfigureList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appScenario') is not None:
            self.app_scenario = m.get('appScenario')
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('channelStatus') is not None:
            self.channel_status = m.get('channelStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('live2vod') is not None:
            self.live_2vod = m.get('live2vod')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('videoEncrypted') is not None:
            self.video_encrypted = m.get('videoEncrypted')
        if m.get('hlsEncryptDuration') is not None:
            self.hls_encrypt_duration = m.get('hlsEncryptDuration')
        if m.get('pullConfigureList') is not None:
            self.pull_configure_list = []
            for k in m.get('pullConfigureList'):
                temp_model = GetChannelConfPullConfigureList()
                self.pull_configure_list.append(temp_model.from_map(k))
        if m.get('pushConfigureInfo') is not None:
            self.push_configure_info = []
            for k in m.get('pushConfigureInfo'):
                temp_model = GetChannelConfPushConfigureInfo()
                self.push_configure_info.append(temp_model.from_map(k))
        if m.get('srtPullConfigureList') is not None:
            self.srt_pull_configure_list = []
            for k in m.get('srtPullConfigureList'):
                temp_model = GetChannelConfSrtPullConfigureList()
                self.srt_pull_configure_list.append(temp_model.from_map(k))
        return self


class GetChannelConfPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelConfParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelConfRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelConfResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateRecordTaskRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        trans_no: str = None,
        quick_start: bool = None,
        start_time: int = None,
        end_time: int = None,
        notify_url: str = None,
        file_type: str = None,
        is_concat: bool = None,
        http_pull_record: bool = None,
        key: str = None,
    ):
        # {"en":"Channel pull ID. If an unstarted, started task already exists for the pullId, you cannot add another task for the same pullId.", "zh_CN":"频道拉流 ID。如果该 pullId 已存在未开始、已开始的任务，则不能再添加同一个 pullId 的任务。"}
        self.pull_id = pull_id
        # {"en":"The service ID must be unique. You are advised to use a 32-bit UUID and the value can be a string of up to 32 characters", "zh_CN":"业务 ID，需用户自己控制唯一性，建议使用 32位 UUID，并且最长为 32 位字符串"}
        self.trans_no = trans_no
        # {"en":"Whether to start recording immediately: true: start recording immediately; false: start recording periodically. When true, startRecordTime must not be passed or be an empty string.", "zh_CN":"是否立即启动录制，true 表示立即启动，false为定时启动。当为 true 时，startRecordTime必须不传或为空字符串。"}
        self.quick_start = quick_start
        # {"en":"Schedule a recording start time. The format is a timestamp in seconds, for example, 1502438820. Actual participation in the specific program calculation, will automatically remove the number of extra seconds accurate to minutes, the actual accuracy is only minutes. The recording start time accurate to one minute later must be later than the current time. This parameter is mandatory when quickStart is false.", "zh_CN":"计划录制开始时间。格式为秒级时间戳，如1502438820。实际参与到具体程序运算中，会自动去除多余秒数精确到分钟，实际精度只到分钟。精确到分钟后的录制开始时间必须是大于当前时间。当 quickStart 为 false 时必填。"}
        self.start_time = start_time
        # {"en":"Scheduled recording end time. This parameter is mandatory. The format is a timestamp in seconds, for example, 1502438880. Actual participation in the specific program calculation, will automatically remove the number of extra seconds accurate to minutes, the actual accuracy is only minutes. The recording end time accurate to minute must be later than the current time and later than the start time accurate to minute. The interval between the end time and the start time, which is accurate to minutes by seconds, cannot exceed 72 hours. There will be a small error between the recorded video duration and the planned recording time", "zh_CN":"计划录制结束时间，必填。格式为秒级时间戳，如 1502438880。 实际参与到具体程序运算中，会自动去除多余秒数精确到分钟，实际精度只到分钟。精确到分钟后的录制结束时间必须大于当前时间且大于精确到分钟后的开始时间。结束时间与开始时间去除秒数精确到分钟的时间，最大间隔不能超过 72 小时。录制的视频时长与计划录制时间会有少量误差。"}
        self.end_time = end_time
        # {"en":"User-defined notification address", "zh_CN":"用户自定义的通知地址，必须以 http://开头或 https://开头。"}
        self.notify_url = notify_url
        # {"en":"Recorded file format, default is mp4, optional flv, or m3u8, value is lowercase", "zh_CN":"录制文件的格式，默认是 mp4,可选 flv，或m3u8，值为小写"}
        self.file_type = file_type
        # {"en":"The default value is flase. If true, the fileType must be in m3u8 format. Otherwise, a parameter error will be reported. The recording function of third-party storage does not support splicing", "zh_CN":"是否合并成一个视频，默认是 flase，如果选true,则 fileType 必须是 m3u8 格式才支持，否则会报参数错误。开启第三方存储录制时不支持拼接"}
        self.is_concat = is_concat
        # {"en":"The default value is false. When set to true, http pull streams are invoked to record. The specific decision logic is as follows: 1. There are two types of http headers: http and https. 2. Encapsulation protocol determination. The default is HDL. 1) If the corresponding pull-flow protocol includes HDL and HLS. HDL is preferred. 2) If the corresponding pull-flow protocol only has HLS, set the value to HLS. 3) If the corresponding pull-flow protocol does not have HDL and HLS. An error message is displayed. If the parameter is true, the domain name corresponding to the flow needs to be configured with HDL or HLS", "zh_CN":"默认值 false，当设置成 true 时，则调用 http拉流去做录制。具体判定逻辑：1、http 协议头有 http 和 https 两种，内部通过查询拉流配置确定。2、封装协议判定。默认取 HDL。1）如对应的拉流协议有 HDL,HLS 两种。优先取HDL。2）如对应拉流协议只有 HLS，取 HLS。3）如对应拉流协议无 HDL 和 HLS。报错，返回提示当该入参为“true”时，该流对应的域名需要配置 HDL 或者 HLS 协议的拉流。"}
        self.http_pull_record = http_pull_record
        # {"en":"Third-party storage Specifies the storage path for recording (without file suffixes).", "zh_CN":"第三方存储录制时指定存储路径（不含文件后缀）"}
        self.key = key

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.quick_start, 'quick_start')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.quick_start is not None:
            result['quickStart'] = self.quick_start
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.is_concat is not None:
            result['isConcat'] = self.is_concat
        if self.http_pull_record is not None:
            result['httpPullRecord'] = self.http_pull_record
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('quickStart') is not None:
            self.quick_start = m.get('quickStart')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('isConcat') is not None:
            self.is_concat = m.get('isConcat')
        if m.get('httpPullRecord') is not None:
            self.http_pull_record = m.get('httpPullRecord')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class CreateRecordTaskData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"taskId", "zh_CN":"直播录制任务id"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateRecordTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CreateRecordTaskData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = CreateRecordTaskData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateRecordTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRecordTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRecordTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRecordTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateChannelRequest(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        channel_type: str = None,
        push_domain: str = None,
        pull_protocol: str = None,
        pull_rate: str = None,
        player_id: str = None,
        directory_id: str = None,
        check: str = None,
        white_board_config: str = None,
        func_config: str = None,
        live_2vod: str = None,
        app_scenario: str = None,
        video_encrypted: int = None,
        hls_encrypt_duration: int = None,
    ):
        # {"en":"Channel name,the value contains a maximum of 255 characters", "zh_CN":"频道名称，最长 255 个字符"}
        self.channel_name = channel_name
        # {"en":"Channel type,It must be the channel type configured under the name of the push basin.
        # It can only be a combination of English digits and underscores.
        # The system automatically generates a push
        # Use this domain when streaming urls,
        # For example:
        # rtmp:// push channel name/channel type/pushId
        # pushId is automatically assigned by the system after the channel is successfully created", "zh_CN":"频道类型，必须是推流域名下配置的频道类型，
        # 只能是英文数字下划线组合；系统自动生成推
        # 流 URL 时使用该域名，例如： 
        # rtmp://推流域名／频道类型／pushId 
        # pushId 在频道创建成功后由系统自动分配"}
        self.channel_type = channel_type
        # {"en":"Source push domain name,This domain name is used when the system automatically generates a URL for pushing streams.
        # For example, rtmp:// push the channel name/channel type/pushId
        # pushId is automatically allocated by the system after the channel is created successfully.", "zh_CN":"源端推流域名；  
        # 创建成功后系统自动生成推流 URL 时使用该域
        # 名，例如：rtmp://推流域名／频道类型／
        # pushId 
        # pushId 在频道创建成功后由系统自动分配；"}
        self.push_domain = push_domain
        # {"en":"Play the pull stream protocol,The default value is 0. Multiple options can be selected.
        # 2 and 3 cannot be selected at the same time. The protocol must be included in the basin name
        # The actual configuration protocol type is as follows:
        # 0:RTMP, 1:HDL, 2:HLS, 3:HDS
        # After the URL is created successfully, the system automatically generates the URL for playing the pull stream:
        # For example, rtmp:// pull watershed name/channel type/pushId.
        # If 2.19 Creating a Live Recording Task is required,
        # This parameter must contain at least one of RTMP or HDL protocols when creating a channel.", "zh_CN":"播放拉流协议，默认为 0，可多选； 
        # 2 和 3 不可同时选择，协议需包含在推流域名
        # 实际配置的转出协议类型中： 
        # 0、 RTMP，1、HDL，2、HLS，3、HDS 
        # 创建成功后，系统会自动生成播放拉流 URL：例
        # 如：rtmp://拉流域名／频道类型／pushId。 
        # 如果需要使用 2.19 创建直播录制任务接口进
        # 行录制，则创建频道时该参数必须至少包含
        # RTMP 协议或 HDL 协议中的一个。"}
        self.pull_protocol = pull_protocol
        # {"en":"Player pull bit rate,Multiple options can be selected to ensure that the selected bit rate is included in the range of the transcoding bit rate configured in the push basin name;
        # 0:source rate, 1:smooth, 2:standard definition, 3:HD, 4:super clear", "zh_CN":"播放端拉流码率，可多选，确保选择的码率包含在
        # 推流域名配置的转码码率范围内； 
        # 0、源码率，1、流畅，2、标清，3、高清，4、超清 "}
        self.pull_rate = pull_rate
        # {"en":"The player ID used by the channel. If not set, the default player is used.", "zh_CN":"频道使用的播放器 ID，未设置则使用默认播放器。"}
        self.player_id = player_id
        # {"en":"Record directory ID. For details, see Creating a Record Directory. If the record directory management function is not enabled, you do not need to enter this parameter.", "zh_CN":"录制目录 ID，详见 新建录制目录 如果未开通录制目录管理功能，无需填写。"}
        self.directory_id = directory_id
        # {"en":"Stream check string", "zh_CN":"流校验串"}
        self.check = check
        # {"en":"If this parameter is not specified, the whiteboard function remains unchanged. urlsafe Base64-encoded JSON string,
        # Example: eyJvcGVuIjogMSwid2hpdGVCb2FyZElkIjogInh4eCJ9
        # The format of the json string before encoding is as follows:
        # {\"open\": 1,\"whiteBoardId\": \"xxx\"}
        # There are two attributes:
        # open, mandatory. Whether to enable the whiteboard. 0 is disabled and 1 is enabled.
        # whiteBoardId is mandatory. This parameter is mandatory only when the whiteboard id and open are 1.
        # This interface does not support changing whiteboard ids", "zh_CN":"如果不传此参数，则白板功能保持原样，不修改。经过 urlsafe base64 编码的 JSON 字符串, 
        # 例：
        # eyJvcGVuIjogMSwid2hpdGVCb2FyZElkIjogInh4eCJ
        # 9 
        # 编码前的 json 串格式如下： 
        # {\"open\": 1,\"whiteBoardId\": \"xxx\"} 
        # 有两个属性： 
        # open，必填，是否开启白板，0 不开启，1 开启； 
        # whiteBoardId，非必填，白板 id，open 为 1 时才
        # 需要设值。 
        # 此接口不支持修改白板 id "}
        self.white_board_config = white_board_config
        # {"en":"Function configuration parameter. Currently, you can only set whether to display the share button on the web page. If the parameter is not transmitted, no modification is performed.
        # Parameter values are urlsafe base64 encoded JSON strings,
        # For example, eyJzaGFyZSI6IDF9,
        # The json string before encoding is {\"share\": 1}
        # For example: eyJzaGFyZSI6IDB9,
        # The json string before encoding is {\"share\": 0}
        # The funcConfig parameter must be valid if it is passed and is not empty, and the value of the share entry can only be one of 0 or 1.", "zh_CN":"功能配置参数，目前只支持设置是否在网页推流
        # 页面显示分享按钮。如果参数不传，则不做任何
        # 修改。 
        # 参数值为经过 urlsafe base64 编码的 JSON 字符
        # 串，例如：eyJzaGFyZSI6IDF9，编码前的 json 串
        # 为{\"share\": 1} 
        # 如：eyJzaGFyZSI6IDB9，编码前的 json 串为
        # {\"share\": 0} 
        # funcConfig 参数如果有传且不为空，所传值必须
        # 为合法，且 share 项的值只能是 0 或 1 中的某一
        # 个。 "}
        self.func_config = func_config
        # {"en":"If it is enabled, push it and record it. 1 is enabled, 0 is not enabled. If the customer does not provide the required value-added service, this parameter is ignored.", "zh_CN":"是否开启即推即录，1 开启，0 不开启。如果该客户
        # 未开通应对的增值服务，接口中忽略此参数。"}
        self.live_2vod = live_2vod
        # {"en":"Application scenario: The specified application scenario must exist", "zh_CN":"应用场景，指定应用场景时应用场景需已存在"}
        self.app_scenario = app_scenario
        # {"en":"Video stream encryption. 0: No encryption is required 1:HLS universal encryption 2:DRM encryption. The default value is 0", "zh_CN":"视频流加密。0:不做任何加密 1:HLS通用加密 2:DRM加密，默认为0"}
        self.video_encrypted = video_encrypted
        # {"en":"HLS Universal encryption validity time (unit: second). If videoEncryted encryption type is HLS Universal Encryption and the current field is not filled in, the default value is 604800 (7 days)", "zh_CN":"HLS通用加密有效时间（单位：秒）。如果videoEncryted的加密类型为HLS通用加密，而当前字段未填，则默认值为604800（7天）"}
        self.hls_encrypt_duration = hls_encrypt_duration

    def validate(self):
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.channel_type, 'channel_type')
        self.validate_required(self.push_domain, 'push_domain')
        self.validate_required(self.pull_rate, 'pull_rate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.push_domain is not None:
            result['pushDomain'] = self.push_domain
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.pull_rate is not None:
            result['pullRate'] = self.pull_rate
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.check is not None:
            result['check'] = self.check
        if self.white_board_config is not None:
            result['whiteBoardConfig'] = self.white_board_config
        if self.func_config is not None:
            result['funcConfig'] = self.func_config
        if self.live_2vod is not None:
            result['live2vod'] = self.live_2vod
        if self.app_scenario is not None:
            result['appScenario'] = self.app_scenario
        if self.video_encrypted is not None:
            result['videoEncrypted'] = self.video_encrypted
        if self.hls_encrypt_duration is not None:
            result['hlsEncryptDuration'] = self.hls_encrypt_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('pushDomain') is not None:
            self.push_domain = m.get('pushDomain')
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('pullRate') is not None:
            self.pull_rate = m.get('pullRate')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('check') is not None:
            self.check = m.get('check')
        if m.get('whiteBoardConfig') is not None:
            self.white_board_config = m.get('whiteBoardConfig')
        if m.get('funcConfig') is not None:
            self.func_config = m.get('funcConfig')
        if m.get('live2vod') is not None:
            self.live_2vod = m.get('live2vod')
        if m.get('appScenario') is not None:
            self.app_scenario = m.get('appScenario')
        if m.get('videoEncrypted') is not None:
            self.video_encrypted = m.get('videoEncrypted')
        if m.get('hlsEncryptDuration') is not None:
            self.hls_encrypt_duration = m.get('hlsEncryptDuration')
        return self


class CreateChannelData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        pull_id: str = None,
    ):
        # {"en":"Create timestamp", "zh_CN":"创建时间戳"}
        self.create_time = create_time
        # {"en":"Pull stream ID, a globally unique value.", "zh_CN":"拉流 ID，全局唯一值。"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class CreateChannelResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CreateChannelData = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Operational information", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = CreateChannelData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SetChannelStateRealtimeBackRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        notify_url: str = None,
        open: int = None,
    ):
        # {"en":"Pushname, you need to enable the channel status callback function to push the basin name", "zh_CN":"推流域名，需要开启频道状态回调功能的推流域名"}
        self.domain_name = domain_name
        # {"en":"The callback address must start with http:// or https:// in lower case.", "zh_CN":"回调地址，必须以小写的 http://开头或https://开头。"}
        self.notify_url = notify_url
        # {"en":"1: enable, 0: disable. The default value is 1", "zh_CN":"1：开启，0：关闭，新增时默认 1"}
        self.open = open

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')
        self.validate_required(self.open, 'open')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.open is not None:
            result['open'] = self.open
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('open') is not None:
            self.open = m.get('open')
        return self


class SetChannelStateRealtimeBackData(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetChannelStateRealtimeBackResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: SetChannelStateRealtimeBackData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = SetChannelStateRealtimeBackData()
            self.data = temp_model.from_map(m['data'])
        return self


class SetChannelStateRealtimeBackPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetChannelStateRealtimeBackParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetChannelStateRealtimeBackRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetChannelStateRealtimeBackResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteChannelRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream id, channel unique identification, multiple ids separated by \",\";", "zh_CN":"拉流 id，频道唯一标识，多个 ID 用\",\"隔开；"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class DeleteChannelResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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


class DeleteChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelEditRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        channel_name: str = None,
        reset_push_id: str = None,
        pull_rate: str = None,
        directory_id: str = None,
        check: str = None,
        white_board_config: str = None,
        func_config: str = None,
        live_2vod: str = None,
        app_scenario: str = None,
        video_encrypted: int = None,
        hls_encrypt_duration: int = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流 id"}
        self.pull_id = pull_id
        # {"en":"Channel name,The value contains a maximum of 255 characters", "zh_CN":"频道名称，最长 255 个字符"}
        self.channel_name = channel_name
        # {"en":"Reset the push stream ID. The default is 0,1 reset and 0 does not reset", "zh_CN":"重设推流 ID，默认为 0，1 为重设，0 为不重设"}
        self.reset_push_id = reset_push_id
        # {"en":"The player pulls the stream bit rate. Multiple options can be selected to ensure that the selected bit rate is included in the range of the transcoding bit rate configured in the push basin name.
        # 0:source rate, 1:smooth, 2:standard definition, 3:HD, 4:super clear", "zh_CN":"播放端拉流码率，可多选，确保选择的码率包含在
        # 推流域名配置的转码码率范围内； 
        # 0、源码率，1、流畅，2、标清，3、高清，4、超清 "}
        self.pull_rate = pull_rate
        # {"en":"ID of the recording directory. For details, see Creating a Recording Directory
        # If the recorded directory management function is not enabled, this parameter is not required.", "zh_CN":"录制目录 ID，详见 新建录制目录 
        # 如果未开通录制目录管理功能，无需填写。"}
        self.directory_id = directory_id
        # {"en":"Stream check string", "zh_CN":"流校验串"}
        self.check = check
        # {"en":"If this parameter is not specified, the whiteboard function remains unchanged. urlsafe Base64-encoded JSON string,
        # Example: eyJvcGVuIjogMSwid2hpdGVCb2FyZElkIjogInh4eCJ9
        # The format of the json string before encoding is as follows:
        # {\"open\": 1,\"whiteBoardId\": \"xxx\"}
        # There are two attributes:
        # open, mandatory. Whether to enable the whiteboard. 0 is disabled and 1 is enabled.
        # whiteBoardId is mandatory. This parameter is mandatory only when the whiteboard id and open are 1.
        # This interface does not support changing whiteboard ids", "zh_CN":"如果不传此参数，则白板功能保持原样，不修改。经过 urlsafe base64 编码的 JSON 字符串, 
        # 例：
        # eyJvcGVuIjogMSwid2hpdGVCb2FyZElkIjogInh4eCJ9 
        # 编码前的 json 串格式如下： 
        # {\"open\": 1,\"whiteBoardId\": \"xxx\"} 
        # 有两个属性： 
        # open，必填，是否开启白板，0 不开启，1 开启； 
        # whiteBoardId，非必填，白板 id，open 为 1 时才
        # 需要设值。 
        # 此接口不支持修改白板 id "}
        self.white_board_config = white_board_config
        # {"en":"Function configuration parameter. Currently, you can only set whether to display the share button on the web page. If the parameter is not transmitted, no modification is performed.
        # Parameter values are urlsafe base64 encoded JSON strings,
        # For example, eyJzaGFyZSI6IDF9,
        # The json string before encoding is {\"share\": 1}
        # For example: eyJzaGFyZSI6IDB9,
        # The json string before encoding is {\"share\": 0}
        # The funcConfig parameter must be valid if it is passed and is not empty, and the value of the share entry can only be one of 0 or 1.", "zh_CN":"功能配置参数，目前只支持设置是否在网页推流
        # 页面显示分享按钮。如果参数不传，则不做任何
        # 修改。 
        # 参数值为经过 urlsafe base64 编码的 JSON 字符
        # 串，例如：eyJzaGFyZSI6IDF9，编码前的 json 串
        # 为{\"share\": 1} 
        # 如：eyJzaGFyZSI6IDB9，编码前的 json 串为
        # {\"share\": 0} 
        # funcConfig 参数如果有传且不为空，所传值必须
        # 为合法，且 share 项的值只能是 0 或 1 中的某一
        # 个。 "}
        self.func_config = func_config
        # {"en":"If it is enabled, push it and record it. 1 is enabled, 0 is not enabled. If the customer
        # This parameter is ignored because the value-added service is not enabled.", "zh_CN":"是否开启即推即录，1 开启，0 不开启。如果该客户
        # 未开通应对的增值服务，接口中忽略此参数。"}
        self.live_2vod = live_2vod
        # {"en":"Application scenario: The specified application scenario must exist", "zh_CN":"应用场景，指定应用场景时应用场景需已存在"}
        self.app_scenario = app_scenario
        # {"en":"Video stream encryption. 0: No encryption is required 1:HLS universal encryption 2:DRM encryption", "zh_CN":"视频流加密。0:不做任何加密 1:HLS通用加密 2:DRM加密"}
        self.video_encrypted = video_encrypted
        # {"en":"HLS Universal encryption validity time (unit: second).
        # 1. videoEncryted encryption type has been HLS universal encryption
        # (1) If the current field has been filled in, the valid duration will be updated according to the current time and the valid time.
        # (2) If the current field is not filled in, the validity period will not be updated.
        # 2. videoEncryted encryption type changed from other to HLS universal encryption,
        # (1) If the current field is not filled in, the default value is 604800 (7 days).
        # (2) If the current field has been filled in, the valid duration will be updated according to the current time and the valid time.", "zh_CN":"HLS通用加密有效时间（单位：秒）。
        # 1. videoEncryted的加密类型已经是HLS通用加密的情况
        #     （1）当前字段已填写，则根据当前时间和填入有效时间重新更新有效时长。
        #     （2）当前字段未填写，则不更新有效时长。
        # 2. videoEncryted的加密类型由其他改为HLS通用加密的情况，
        #     （1）当前字段未填写，则默认值为604800（7天）。
        #     （2）当前字段已填写，则根据当前时间和填入有效时间重新更新有效时长。"}
        self.hls_encrypt_duration = hls_encrypt_duration

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.reset_push_id is not None:
            result['resetPushId'] = self.reset_push_id
        if self.pull_rate is not None:
            result['pullRate'] = self.pull_rate
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.check is not None:
            result['check'] = self.check
        if self.white_board_config is not None:
            result['whiteBoardConfig'] = self.white_board_config
        if self.func_config is not None:
            result['funcConfig'] = self.func_config
        if self.live_2vod is not None:
            result['live2vod'] = self.live_2vod
        if self.app_scenario is not None:
            result['appScenario'] = self.app_scenario
        if self.video_encrypted is not None:
            result['videoEncrypted'] = self.video_encrypted
        if self.hls_encrypt_duration is not None:
            result['hlsEncryptDuration'] = self.hls_encrypt_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('resetPushId') is not None:
            self.reset_push_id = m.get('resetPushId')
        if m.get('pullRate') is not None:
            self.pull_rate = m.get('pullRate')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('check') is not None:
            self.check = m.get('check')
        if m.get('whiteBoardConfig') is not None:
            self.white_board_config = m.get('whiteBoardConfig')
        if m.get('funcConfig') is not None:
            self.func_config = m.get('funcConfig')
        if m.get('live2vod') is not None:
            self.live_2vod = m.get('live2vod')
        if m.get('appScenario') is not None:
            self.app_scenario = m.get('appScenario')
        if m.get('videoEncrypted') is not None:
            self.video_encrypted = m.get('videoEncrypted')
        if m.get('hlsEncryptDuration') is not None:
            self.hls_encrypt_duration = m.get('hlsEncryptDuration')
        return self


class ChannelEditData(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        push_url: str = None,
        srt_push_url: str = None,
    ):
        # {"en":"Channel name,The value contains a maximum of 255 characters", "zh_CN":"频道名称，最长 255 个字符"}
        self.channel_name = channel_name
        # {"en":"Push URL", "zh_CN":"推流 URL"}
        self.push_url = push_url
        # {"en":"The URL is in SRT format", "zh_CN":"SRT 格式的推流 URL"}
        self.srt_push_url = srt_push_url

    def validate(self):
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.push_url, 'push_url')
        self.validate_required(self.srt_push_url, 'srt_push_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.push_url is not None:
            result['pushUrl'] = self.push_url
        if self.srt_push_url is not None:
            result['srtPushUrl'] = self.srt_push_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('pushUrl') is not None:
            self.push_url = m.get('pushUrl')
        if m.get('srtPushUrl') is not None:
            self.srt_push_url = m.get('srtPushUrl')
        return self


class ChannelEditResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: ChannelEditData = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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
            temp_model = ChannelEditData()
            self.data = temp_model.from_map(m['data'])
        return self


class ChannelEditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelEditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelEditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelEditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelReBrodcastRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream id, channel unique identification, multiple ids separated by \",\";", "zh_CN":"拉流 id，频道唯一标识，多个 ID 用\",\"隔开；"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class ChannelReBrodcastResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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


class ChannelReBrodcastPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelReBrodcastParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelReBrodcastRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelReBrodcastResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
    ):
        # {"en":"id of the recording directory whose information you want to obtain", "zh_CN":"需要获取录制目录信息的录制目录id"}
        self.directory_id = directory_id

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        return self


class GetDirectoryData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_type: str = None,
        first_level_directory: str = None,
        second_level_directory: str = None,
        third_level_directory: str = None,
        update_time: str = None,
    ):
        # {"en":"Record directory creation time", "zh_CN":"录制目录创建时间"}
        self.create_time = create_time
        # {"en":"Recorded directory ID", "zh_CN":"录制目录 ID"}
        self.directory_id = directory_id
        # {"en":"Directory type", "zh_CN":"目录类型"}
        self.directory_type = directory_type
        # {"en":"Primary directory", "zh_CN":"一级目录"}
        self.first_level_directory = first_level_directory
        # {"en":"Secondary directory", "zh_CN":"二级目录"}
        self.second_level_directory = second_level_directory
        # {"en":"Three-level directory", "zh_CN":"三级目录"}
        self.third_level_directory = third_level_directory
        # {"en":"Record directory modification time", "zh_CN":"录制目录修改时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.first_level_directory, 'first_level_directory')
        self.validate_required(self.second_level_directory, 'second_level_directory')
        self.validate_required(self.third_level_directory, 'third_level_directory')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_type is not None:
            result['directoryType'] = self.directory_type
        if self.first_level_directory is not None:
            result['firstLevelDirectory'] = self.first_level_directory
        if self.second_level_directory is not None:
            result['secondLevelDirectory'] = self.second_level_directory
        if self.third_level_directory is not None:
            result['thirdLevelDirectory'] = self.third_level_directory
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')
        if m.get('firstLevelDirectory') is not None:
            self.first_level_directory = m.get('firstLevelDirectory')
        if m.get('secondLevelDirectory') is not None:
            self.second_level_directory = m.get('secondLevelDirectory')
        if m.get('thirdLevelDirectory') is not None:
            self.third_level_directory = m.get('thirdLevelDirectory')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetDirectoryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetDirectoryData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = GetDirectoryData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetDirectoryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetChannelLiveStateRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"pullid", "zh_CN":"拉流 id"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetChannelLiveStateData(TeaModel):
    def __init__(
        self,
        channel_state: str = None,
    ):
        # {"en":"Return the live stream status corresponding to each pull stream ID:
        # 1:live broadcast 2:not broadcast 3:banned", "zh_CN":"返回每个拉流 ID 对应的直播流实时状态： 
        # 1、直播中   2、未开播  3、禁播 "}
        self.channel_state = channel_state

    def validate(self):
        self.validate_required(self.channel_state, 'channel_state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_state is not None:
            result['channelState'] = self.channel_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelState') is not None:
            self.channel_state = m.get('channelState')
        return self


class GetChannelLiveStateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetChannelLiveStateData = None,
    ):
        # {"en":"200 success", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = GetChannelLiveStateData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetChannelLiveStatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelLiveStateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelLiveStateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetChannelLiveStateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetRecordFileInfoRequest(TeaModel):
    def __init__(
        self,
        pull_ids: str = None,
        video_ids: str = None,
    ):
        # {"en":"pullIds", "zh_CN":"1至多个频道ID，用半角逗号（,）隔开。要求不能输入数字、大小写英文、半角逗号以外的其他字符，否则会认为是非法字符。但是如果输入的是空字符串则不会认为是非法字符，而是认为该参数为空。pullIds 不能全部是逗号。pullIds 中的频道 ID 个数不能超过 50 个。pullIds 和videoIds 两个参数必须有且只有一个不为空。"}
        self.pull_ids = pull_ids
        # {"en":"videoIds", "zh_CN":"1至多个视频ID，用半角逗号（,）隔开。要求不能输入数字、大小写英文、半角逗号以外的其他字符，否则会认为是非法字符。但是如果输入的是空字符串则不会认为是非法字符，而是认为该参数为空。videoIds 不能全部是逗号。videoIds 中的频道 ID 个数不能超过 50 个。pullIds 和videoIds 两个参数必须有且只有一个不为空。"}
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_ids is not None:
            result['pullIds'] = self.pull_ids
        if self.video_ids is not None:
            result['videoIds'] = self.video_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullIds') is not None:
            self.pull_ids = m.get('pullIds')
        if m.get('videoIds') is not None:
            self.video_ids = m.get('videoIds')
        return self


class GetRecordFileInfoList(TeaModel):
    def __init__(
        self,
        password: str = None,
        pull_id: str = None,
        share_page_url: str = None,
        start_time: int = None,
        video_duration: int = None,
        video_id: str = None,
        video_name: str = None,
    ):
        # {"en":"Watch Password", "zh_CN":"观看密码"}
        self.password = password
        # {"en":"Channel pull ID", "zh_CN":"频道拉流 ID"}
        self.pull_id = pull_id
        # {"en":"Share page url, if the encrypted transcoding video sharing page url is empty.", "zh_CN":"分享页 url，如果加密转码的视频分享页 url 为空。"}
        self.share_page_url = share_page_url
        # {"en":"Recording start time", "zh_CN":"录制开始时间"}
        self.start_time = start_time
        # {"en":"Recording duration", "zh_CN":"录制时长"}
        self.video_duration = video_duration
        # {"en":"videoId", "zh_CN":"视频 ID"}
        self.video_id = video_id
        # {"en":"videoName", "zh_CN":"视频名称"}
        self.video_name = video_name

    def validate(self):
        self.validate_required(self.password, 'password')
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.share_page_url, 'share_page_url')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.video_duration, 'video_duration')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.video_name, 'video_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.share_page_url is not None:
            result['sharePageUrl'] = self.share_page_url
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.video_name is not None:
            result['videoName'] = self.video_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('sharePageUrl') is not None:
            self.share_page_url = m.get('sharePageUrl')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        return self


class GetRecordFileInfoResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetRecordFileInfoList[GetRecordFileInfoList] = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
                temp_model = GetRecordFileInfoList()
                self.data.append(temp_model.from_map(k))
        return self


class GetRecordFileInfoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordFileInfoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordFileInfoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordFileInfoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EndForwardTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"taskId", "zh_CN":"转推任务 ID"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class EndForwardTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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


class EndForwardTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndForwardTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndForwardTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndForwardTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ChannelForbiddenRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream id, channel unique identification, multiple ids separated by \",\";", "zh_CN":"拉流 id，频道唯一标识，多个 ID 用\",\"隔开；"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class ChannelForbiddenResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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


class ChannelForbiddenPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelForbiddenParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelForbiddenRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ChannelForbiddenResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPullChannelListRequest(TeaModel):
    def __init__(
        self,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Gets the sorting of the channel list; 0. In descending order by creation time; 1. In ascending order by creation time. Default is 0", "zh_CN":"获取频道列表的排序；0、按创建时间降序，1、按创建时间升序。默认为 0"}
        self.list_order = list_order
        # {"en":"The number of pages in the channel page list, starting from 1; Default is 1", "zh_CN":"频道分页列表中第几页，从 1 开始取值；默认为 1"}
        self.page_index = page_index
        # {"en":"Average number of channels per page, ranging from 1 to 50; Default is 10", "zh_CN":"平均每页频道数量，取值在 1-50 之间；默认为 10"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetPullChannelListChannelListItem(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        channel_type: str = None,
        source_pull_protocol: str = None,
        source_pull_url: str = None,
        create_time: str = None,
        user_id: str = None,
        pull_id: str = None,
    ):
        # {"en":"channelName", "zh_CN":"频道名称"}
        self.channel_name = channel_name
        # {"en":"channelType", "zh_CN":"频道类型"}
        self.channel_type = channel_type
        # {"en":"Sources-end pull-through protocols: RTMP, Http flv, RTMP, Http flv, HLS, HDS, TS", "zh_CN":"源端拉流协议，RTMP、Http flv、RTMP、Http flv、HLS、HDS、TS"}
        self.source_pull_protocol = source_pull_protocol
        # {"en":"sourcePullUrl", "zh_CN":"源端拉流 url"}
        self.source_pull_url = source_pull_url
        # {"en":"createTime", "zh_CN":"频道创建时间，例如 2015-05-07 12:00:00"}
        self.create_time = create_time
        # {"en":"userId", "zh_CN":"创建频道的用户id"}
        self.user_id = user_id
        # {"en":"pullId", "zh_CN":"拉流id"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.channel_type, 'channel_type')
        self.validate_required(self.source_pull_protocol, 'source_pull_protocol')
        self.validate_required(self.source_pull_url, 'source_pull_url')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.source_pull_protocol is not None:
            result['sourcePullProtocol'] = self.source_pull_protocol
        if self.source_pull_url is not None:
            result['sourcePullUrl'] = self.source_pull_url
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('sourcePullProtocol') is not None:
            self.source_pull_protocol = m.get('sourcePullProtocol')
        if m.get('sourcePullUrl') is not None:
            self.source_pull_url = m.get('sourcePullUrl')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetPullChannelListData(TeaModel):
    def __init__(
        self,
        channel_toal: str = None,
        channel_list: List[GetPullChannelListChannelListItem] = None,
    ):
        # {"en":"Number of channels", "zh_CN":"频道总数"}
        self.channel_toal = channel_toal
        # {"en":"Channel list array", "zh_CN":"频道列表数组"}
        self.channel_list = channel_list

    def validate(self):
        self.validate_required(self.channel_toal, 'channel_toal')
        self.validate_required(self.channel_list, 'channel_list')
        if self.channel_list:
            for k in self.channel_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_toal is not None:
            result['channelToal'] = self.channel_toal
        if self.channel_list is not None:
            result['channelList'] = []
            for k in self.channel_list:
                result['channelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToal') is not None:
            self.channel_toal = m.get('channelToal')
        if m.get('channelList') is not None:
            self.channel_list = []
            for k in m.get('channelList'):
                temp_model = GetPullChannelListChannelListItem()
                self.channel_list.append(temp_model.from_map(k))
        return self


class GetPullChannelListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetPullChannelListData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = GetPullChannelListData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPullChannelListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPullChannelConfigureRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream id, unique ID of the channel", "zh_CN":"拉流 id，频道的唯一 ID"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class GetPullChannelConfigurePullUrlListItem(TeaModel):
    def __init__(
        self,
        origin_pull_url: str = None,
        fluent_pull_url: str = None,
        sd_pull_url: str = None,
        high_pull_url: str = None,
        hd_pull_url: str = None,
    ):
        # {"en":"originPullUrl", "zh_CN":"源码率拉流url"}
        self.origin_pull_url = origin_pull_url
        # {"en":"fluentPullUrl", "zh_CN":"流畅码率拉流url"}
        self.fluent_pull_url = fluent_pull_url
        # {"en":"sdPullUrl", "zh_CN":"标清码率拉流url"}
        self.sd_pull_url = sd_pull_url
        # {"en":"highPullUrl", "zh_CN":"高清码率拉流url"}
        self.high_pull_url = high_pull_url
        # {"en":"hdPullUrl", "zh_CN":"超清码率拉流url"}
        self.hd_pull_url = hd_pull_url

    def validate(self):
        self.validate_required(self.origin_pull_url, 'origin_pull_url')
        self.validate_required(self.fluent_pull_url, 'fluent_pull_url')
        self.validate_required(self.sd_pull_url, 'sd_pull_url')
        self.validate_required(self.high_pull_url, 'high_pull_url')
        self.validate_required(self.hd_pull_url, 'hd_pull_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_pull_url is not None:
            result['originPullUrl'] = self.origin_pull_url
        if self.fluent_pull_url is not None:
            result['fluentPullUrl'] = self.fluent_pull_url
        if self.sd_pull_url is not None:
            result['sdPullUrl'] = self.sd_pull_url
        if self.high_pull_url is not None:
            result['highPullUrl'] = self.high_pull_url
        if self.hd_pull_url is not None:
            result['hdPullUrl'] = self.hd_pull_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originPullUrl') is not None:
            self.origin_pull_url = m.get('originPullUrl')
        if m.get('fluentPullUrl') is not None:
            self.fluent_pull_url = m.get('fluentPullUrl')
        if m.get('sdPullUrl') is not None:
            self.sd_pull_url = m.get('sdPullUrl')
        if m.get('highPullUrl') is not None:
            self.high_pull_url = m.get('highPullUrl')
        if m.get('hdPullUrl') is not None:
            self.hd_pull_url = m.get('hdPullUrl')
        return self


class GetPullChannelConfigurePullConfigureListItem(TeaModel):
    def __init__(
        self,
        pull_protocol: str = None,
        pull_url_list: List[GetPullChannelConfigurePullUrlListItem] = None,
    ):
        # {"en":"Player pull stream protocol", "zh_CN":"播放端拉流协议"}
        self.pull_protocol = pull_protocol
        # {"en":"pullUrlList", "zh_CN":"拉流 url 列表"}
        self.pull_url_list = pull_url_list

    def validate(self):
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.pull_url_list, 'pull_url_list')
        if self.pull_url_list:
            for k in self.pull_url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.pull_url_list is not None:
            result['pullUrlList'] = []
            for k in self.pull_url_list:
                result['pullUrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('pullUrlList') is not None:
            self.pull_url_list = []
            for k in m.get('pullUrlList'):
                temp_model = GetPullChannelConfigurePullUrlListItem()
                self.pull_url_list.append(temp_model.from_map(k))
        return self


class GetPullChannelConfigureSourcePullConfigureInfoListItem(TeaModel):
    def __init__(
        self,
        source_pull_url: str = None,
        source_pull_protocol: str = None,
        pull_configure_list: List[GetPullChannelConfigurePullConfigureListItem] = None,
    ):
        # {"en":"Source pull url The system pulls the live stream as the live stream source", "zh_CN":"源端拉流 url系统会拉取该直播流作为直播源"}
        self.source_pull_url = source_pull_url
        # {"en":"Source pull protocol: A channel can have only one back pull protocol, and a source pull basin name can be used for only one source pull protocol channel. 0, RTMP, 1, Http flv", "zh_CN":"源端拉流协议，一个频道只能有一种回源拉流协议，且一个源拉流域名只能用于一种源拉流协议频道；0、RTMP，1、Http flv"}
        self.source_pull_protocol = source_pull_protocol
        # {"en":"Player pull-down configuration information list (pull-down protocol, pull-down url)", "zh_CN":"播放端拉流配置信息列表（拉流协议，拉流 url）"}
        self.pull_configure_list = pull_configure_list

    def validate(self):
        self.validate_required(self.source_pull_url, 'source_pull_url')
        self.validate_required(self.source_pull_protocol, 'source_pull_protocol')
        self.validate_required(self.pull_configure_list, 'pull_configure_list')
        if self.pull_configure_list:
            for k in self.pull_configure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_pull_url is not None:
            result['sourcePullUrl'] = self.source_pull_url
        if self.source_pull_protocol is not None:
            result['sourcePullProtocol'] = self.source_pull_protocol
        if self.pull_configure_list is not None:
            result['pullConfigureList'] = []
            for k in self.pull_configure_list:
                result['pullConfigureList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourcePullUrl') is not None:
            self.source_pull_url = m.get('sourcePullUrl')
        if m.get('sourcePullProtocol') is not None:
            self.source_pull_protocol = m.get('sourcePullProtocol')
        if m.get('pullConfigureList') is not None:
            self.pull_configure_list = []
            for k in m.get('pullConfigureList'):
                temp_model = GetPullChannelConfigurePullConfigureListItem()
                self.pull_configure_list.append(temp_model.from_map(k))
        return self


class GetPullChannelConfigureData(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        channel_status: str = None,
        create_time: str = None,
        create_user: str = None,
        player_id: str = None,
        source_pull_configure_info_list: List[GetPullChannelConfigureSourcePullConfigureInfoListItem] = None,
    ):
        # {"en":"Channel name, maximum 40 Chinese characters", "zh_CN":"频道名称，最长 40 中文"}
        self.channel_name = channel_name
        # {"en":"Keep the field and always return it", "zh_CN":"保留字段，始终返回"}
        self.channel_status = channel_status
        # {"en":"Source channel creation time, for example, 2016-05-08 12:00:00", "zh_CN":"源频道创建时间，例如：2016-05-08 12:00:00"}
        self.create_time = create_time
        # {"en":"createUser", "zh_CN":"创建频道的 userName"}
        self.create_user = create_user
        # {"en":"flash player ID used by the channel. If not set, the default player is used", "zh_CN":"频道使用的 flash 播放器 ID，未设置则使用默认播放器"}
        self.player_id = player_id
        # {"en":"Source pull channel configuration information", "zh_CN":"源拉流频道配置信息"}
        self.source_pull_configure_info_list = source_pull_configure_info_list

    def validate(self):
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.channel_status, 'channel_status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.player_id, 'player_id')
        self.validate_required(self.source_pull_configure_info_list, 'source_pull_configure_info_list')
        if self.source_pull_configure_info_list:
            for k in self.source_pull_configure_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.channel_status is not None:
            result['channelStatus'] = self.channel_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.source_pull_configure_info_list is not None:
            result['sourcePullConfigureInfoList'] = []
            for k in self.source_pull_configure_info_list:
                result['sourcePullConfigureInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('channelStatus') is not None:
            self.channel_status = m.get('channelStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('sourcePullConfigureInfoList') is not None:
            self.source_pull_configure_info_list = []
            for k in m.get('sourcePullConfigureInfoList'):
                temp_model = GetPullChannelConfigureSourcePullConfigureInfoListItem()
                self.source_pull_configure_info_list.append(temp_model.from_map(k))
        return self


class GetPullChannelConfigureResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetPullChannelConfigureData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = GetPullChannelConfigureData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPullChannelConfigurePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelConfigureParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelConfigureRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPullChannelConfigureResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditPullChannelRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        channel_name: str = None,
        source_pull_url: str = None,
        source_pull_protocol: str = None,
        pull_rate: str = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流 id"}
        self.pull_id = pull_id
        # {"en":"Channel name, maximum 255 characters; Unfilled default unchanged", "zh_CN":"频道名称，最长255字符；不填默认不变"}
        self.channel_name = channel_name
        # {"en":"Source pull url", "zh_CN":"源端拉流 url"}
        self.source_pull_url = source_pull_url
        # {"en":"Source pull protocol: A channel can have only one back pull protocol, and a source pull basin name can be used for only one source pull protocol channel. 0, RTMP, 1, Http flv, 2, HLS, 3, HDS", "zh_CN":"源端拉流协议，一个频道只能有一种回源拉流协议，且一个源拉流域名只能用于一种源拉流协议频道；0、RTMP，1、Http flv，2、HLS，3、HDS"}
        self.source_pull_protocol = source_pull_protocol
        # {"en":"The player can select multiple bit rates, separated by commas (,), and ensure that the selected bit rates are within the range of the transcoding bit rates configured by the basin name. 0, source rate, 1, smooth, 2, standard definition, 3, HD, 4, super clear;", "zh_CN":"播放端拉流码率，可多选，用“，”隔开，确保选择的码率包含在推流域名配置的转码码率范围内；0、源码率，1、流畅，2、标清，3、高清，4、超清；"}
        self.pull_rate = pull_rate

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.source_pull_url is not None:
            result['sourcePullUrl'] = self.source_pull_url
        if self.source_pull_protocol is not None:
            result['sourcePullProtocol'] = self.source_pull_protocol
        if self.pull_rate is not None:
            result['pullRate'] = self.pull_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('sourcePullUrl') is not None:
            self.source_pull_url = m.get('sourcePullUrl')
        if m.get('sourcePullProtocol') is not None:
            self.source_pull_protocol = m.get('sourcePullProtocol')
        if m.get('pullRate') is not None:
            self.pull_rate = m.get('pullRate')
        return self


class EditPullChannelData(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPullChannelResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: EditPullChannelData = None,
    ):
        # {"en":"status code", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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
            temp_model = EditPullChannelData()
            self.data = temp_model.from_map(m['data'])
        return self


class EditPullChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPullChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPullChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPullChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetSinglePullCodeRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        player_id: str = None,
        player_size: str = None,
        auto_play: int = None,
        code_type: str = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流 id"}
        self.pull_id = pull_id
        # {"en":"Enter the player ID configured for the channel, which must be consistent with that maintained in 3. Player Management. Do not enter the default player.", "zh_CN":"填写为该频道配置的播放器 ID，必须与三、播放器管理中维护的一致。不填写就采用默认播放器。"}
        self.player_id = player_id
        # {"en":"To match the aspect ratio of the amplifier, five fixed options are provided
        # (1280*720, 1024*768, 1024*576, 640*360,
        # 480*360), and a self-defining lattice with a length-to-width ratio greater than
        # 480 times 360, which is less than 1920 times 1080. The default value is 480 x 360", "zh_CN":"配置播放器的长宽比，提供五个固定选项
        # （ 1280*720 、 1024*768 、 1024*576 、 640*360 、
        # 480*360 ），及一个自定义格式 ，长宽比大于
        # 480*360，小于 1920*1080。不填写默认 480*360"}
        self.player_size = player_size
        # {"en":"Whether the video plays automatically. The default value is 0.
        # 0 indicates non-autoplay, 1 indicates autoplay", "zh_CN":"视频是否自动播放，默认为 0； 
        # 0 为非自动播放，1 为自动播放"}
        self.auto_play = auto_play
        # {"en":"Select the type of playback code you want to get. The default is all code:
        # 0:all, 2:swf code, 4:video url, 5:adaptive code;", "zh_CN":"选择需要获取的播放代码类型，默认为全部代码： 
        # 0、全部，2、swf 代码， 4、视频 url，5、自适应代码；  "}
        self.code_type = code_type

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.player_size is not None:
            result['playerSize'] = self.player_size
        if self.auto_play is not None:
            result['autoPlay'] = self.auto_play
        if self.code_type is not None:
            result['codeType'] = self.code_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('playerSize') is not None:
            self.player_size = m.get('playerSize')
        if m.get('autoPlay') is not None:
            self.auto_play = m.get('autoPlay')
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        return self


class GetSinglePullCodeUrlInfo(TeaModel):
    def __init__(
        self,
        fluent_pull_url: str = None,
        fluent_zkgq_pull_url: str = None,
        hd_pull_url: str = None,
        hd_zkgq_pull_url: str = None,
        high_pull_url: str = None,
        high_zkgq_pull_url: str = None,
        origin_pull_url: str = None,
        origin_zkgq_pull_url: str = None,
        sd_pull_url: str = None,
        sd_zkgq_pull_url: str = None,
    ):
        # {"en":"Smooth bit rate pull stream url", "zh_CN":"流畅码率拉流 url"}
        self.fluent_pull_url = fluent_pull_url
        # {"en":"Smooth bit rate (smart HD) pull stream url", "zh_CN":"流畅码率（智控高清）拉流 url"}
        self.fluent_zkgq_pull_url = fluent_zkgq_pull_url
        # {"en":"Ultra clear bit rate pull url", "zh_CN":"超清码率拉流 url "}
        self.hd_pull_url = hd_pull_url
        # {"en":"Ultra - clear bit rate (intelligent control HD) pull - stream url", "zh_CN":"超清码率（智控高清）拉流 url"}
        self.hd_zkgq_pull_url = hd_zkgq_pull_url
        # {"en":"Hd bit rate pull stream url", "zh_CN":"高清码率拉流 url"}
        self.high_pull_url = high_pull_url
        # {"en":"Hd bit rate (intelligent control HD) pull url", "zh_CN":"高清码率（智控高清）拉流 url"}
        self.high_zkgq_pull_url = high_zkgq_pull_url
        # {"en":"Source rate pull url", "zh_CN":"源码率拉流 url"}
        self.origin_pull_url = origin_pull_url
        # {"en":"Source rate (intelligent control HD) pull url", "zh_CN":"源码率（智控高清）拉流 url"}
        self.origin_zkgq_pull_url = origin_zkgq_pull_url
        # {"en":"Standard definition bit rate pull url", "zh_CN":"标清码率拉流 url"}
        self.sd_pull_url = sd_pull_url
        # {"en":"Standard definition code rate (intelligent control HD) pull url", "zh_CN":"标清码率（智控高清）拉流 url"}
        self.sd_zkgq_pull_url = sd_zkgq_pull_url

    def validate(self):
        self.validate_required(self.fluent_pull_url, 'fluent_pull_url')
        self.validate_required(self.fluent_zkgq_pull_url, 'fluent_zkgq_pull_url')
        self.validate_required(self.hd_pull_url, 'hd_pull_url')
        self.validate_required(self.hd_zkgq_pull_url, 'hd_zkgq_pull_url')
        self.validate_required(self.high_pull_url, 'high_pull_url')
        self.validate_required(self.high_zkgq_pull_url, 'high_zkgq_pull_url')
        self.validate_required(self.origin_pull_url, 'origin_pull_url')
        self.validate_required(self.origin_zkgq_pull_url, 'origin_zkgq_pull_url')
        self.validate_required(self.sd_pull_url, 'sd_pull_url')
        self.validate_required(self.sd_zkgq_pull_url, 'sd_zkgq_pull_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fluent_pull_url is not None:
            result['fluentPullUrl'] = self.fluent_pull_url
        if self.fluent_zkgq_pull_url is not None:
            result['fluentZkgqPullUrl'] = self.fluent_zkgq_pull_url
        if self.hd_pull_url is not None:
            result['hdPullUrl'] = self.hd_pull_url
        if self.hd_zkgq_pull_url is not None:
            result['hdZkgqPullUrl'] = self.hd_zkgq_pull_url
        if self.high_pull_url is not None:
            result['highPullUrl'] = self.high_pull_url
        if self.high_zkgq_pull_url is not None:
            result['highZkgqPullUrl'] = self.high_zkgq_pull_url
        if self.origin_pull_url is not None:
            result['originPullUrl'] = self.origin_pull_url
        if self.origin_zkgq_pull_url is not None:
            result['originZkgqPullUrl'] = self.origin_zkgq_pull_url
        if self.sd_pull_url is not None:
            result['sdPullUrl'] = self.sd_pull_url
        if self.sd_zkgq_pull_url is not None:
            result['sdZkgqPullUrl'] = self.sd_zkgq_pull_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fluentPullUrl') is not None:
            self.fluent_pull_url = m.get('fluentPullUrl')
        if m.get('fluentZkgqPullUrl') is not None:
            self.fluent_zkgq_pull_url = m.get('fluentZkgqPullUrl')
        if m.get('hdPullUrl') is not None:
            self.hd_pull_url = m.get('hdPullUrl')
        if m.get('hdZkgqPullUrl') is not None:
            self.hd_zkgq_pull_url = m.get('hdZkgqPullUrl')
        if m.get('highPullUrl') is not None:
            self.high_pull_url = m.get('highPullUrl')
        if m.get('highZkgqPullUrl') is not None:
            self.high_zkgq_pull_url = m.get('highZkgqPullUrl')
        if m.get('originPullUrl') is not None:
            self.origin_pull_url = m.get('originPullUrl')
        if m.get('originZkgqPullUrl') is not None:
            self.origin_zkgq_pull_url = m.get('originZkgqPullUrl')
        if m.get('sdPullUrl') is not None:
            self.sd_pull_url = m.get('sdPullUrl')
        if m.get('sdZkgqPullUrl') is not None:
            self.sd_zkgq_pull_url = m.get('sdZkgqPullUrl')
        return self


class GetSinglePullCodeVideoUrl(TeaModel):
    def __init__(
        self,
        pull_protocol: str = None,
        url_info: GetSinglePullCodeUrlInfo = None,
    ):
        # {"en":"Pull-flow protocol, 0, RTMP, 1, Http flv, 2, HLS, 3, HDS, 4, Http TS", "zh_CN":"拉流协议，0、RTMP，1、Http flv，2、HLS，3、HDS，4、Http TS"}
        self.pull_protocol = pull_protocol
        self.url_info = url_info

    def validate(self):
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.url_info, 'url_info')
        if self.url_info:
            self.url_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.url_info is not None:
            result['urlInfo'] = self.url_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('urlInfo') is not None:
            temp_model = GetSinglePullCodeUrlInfo()
            self.url_info = temp_model.from_map(m['urlInfo'])
        return self


class GetSinglePullCodeSrtVideoUrl(TeaModel):
    def __init__(
        self,
        pull_protocol: str = None,
        url_info: GetSinglePullCodeUrlInfo = None,
    ):
        # {"en":"Pull-flow protocol, 0, RTMP, 1, Http flv, 2, HLS, 3, HDS, 4, Http TS", "zh_CN":"拉流协议，0、RTMP，1、Http flv，2、HLS，3、HDS，4、Http TS"}
        self.pull_protocol = pull_protocol
        self.url_info = url_info

    def validate(self):
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.url_info, 'url_info')
        if self.url_info:
            self.url_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.url_info is not None:
            result['urlInfo'] = self.url_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('urlInfo') is not None:
            temp_model = GetSinglePullCodeUrlInfo()
            self.url_info = temp_model.from_map(m['urlInfo'])
        return self


class GetSinglePullCodePullCodeInfo(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        video_url: List[GetSinglePullCodeVideoUrl] = None,
        auto_code: str = None,
        swf_code: str = None,
        srt_video_url: List[GetSinglePullCodeSrtVideoUrl] = None,
        audio_auto_code: str = None,
    ):
        # {"en":"Pull flow ID", "zh_CN":"拉流 ID"}
        self.pull_id = pull_id
        # {"en":"List of channel pull urls", "zh_CN":"频道拉流 url 列表"}
        self.video_url = video_url
        # {"en":"Video adaptive code, encrypted video is empty", "zh_CN":"视频自适应代码，加密视频为空"}
        self.auto_code = auto_code
        # {"en":"Channel swf code", "zh_CN":"频道 swf 代码"}
        self.swf_code = swf_code
        # {"en":"A list of pull-down urls in channel SRT format", "zh_CN":"频道 SRT 格式的拉流 url 列表"}
        self.srt_video_url = srt_video_url
        # {"en":"Audio adaptive code, encrypted video is empty", "zh_CN":"音频自适应代码，加密视频为空"}
        self.audio_auto_code = audio_auto_code

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.video_url, 'video_url')
        if self.video_url:
            for k in self.video_url:
                if k:
                    k.validate()
        self.validate_required(self.auto_code, 'auto_code')
        self.validate_required(self.swf_code, 'swf_code')
        self.validate_required(self.srt_video_url, 'srt_video_url')
        if self.srt_video_url:
            for k in self.srt_video_url:
                if k:
                    k.validate()
        self.validate_required(self.audio_auto_code, 'audio_auto_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.video_url is not None:
            result['videoUrl'] = []
            for k in self.video_url:
                result['videoUrl'].append(k.to_map() if k else None)
        if self.auto_code is not None:
            result['autoCode'] = self.auto_code
        if self.swf_code is not None:
            result['swfCode'] = self.swf_code
        if self.srt_video_url is not None:
            result['srtVideoUrl'] = []
            for k in self.srt_video_url:
                result['srtVideoUrl'].append(k.to_map() if k else None)
        if self.audio_auto_code is not None:
            result['audioAutoCode'] = self.audio_auto_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('videoUrl') is not None:
            self.video_url = []
            for k in m.get('videoUrl'):
                temp_model = GetSinglePullCodeVideoUrl()
                self.video_url.append(temp_model.from_map(k))
        if m.get('autoCode') is not None:
            self.auto_code = m.get('autoCode')
        if m.get('swfCode') is not None:
            self.swf_code = m.get('swfCode')
        if m.get('srtVideoUrl') is not None:
            self.srt_video_url = []
            for k in m.get('srtVideoUrl'):
                temp_model = GetSinglePullCodeSrtVideoUrl()
                self.srt_video_url.append(temp_model.from_map(k))
        if m.get('audioAutoCode') is not None:
            self.audio_auto_code = m.get('audioAutoCode')
        return self


class GetSinglePullCodeResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSinglePullCodePullCodeInfo = None,
        message: str = None,
    ):
        # {'en':'status code', 'zh_CN':'返回状态码'}
        self.code = code
        self.data = data
        # {'en':'message', 'zh_CN':'返回消息'}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetSinglePullCodePullCodeInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetSinglePullCodePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSinglePullCodeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSinglePullCodeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSinglePullCodeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetForwardTaskListRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        task_id: str = None,
        status: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"pullId", "zh_CN":"频道 ID"}
        self.pull_id = pull_id
        # {"en":"taskId", "zh_CN":"转推任务 ID"}
        self.task_id = task_id
        # {"en":"Task forwarding status, used to filter tasks. Value range: 0: not started. 1: transfer process; 2: has ended; 3: abnormal; Multiple options are supported, separated by hyphens (ids) in English", "zh_CN":"转推任务状态，用于筛选任务，取值范围：0：未开始；1：转推中；2：已结束；3：异常；支持多选，使用英文,号隔开"}
        self.status = status
        # {"en":"On which page, the value starts from 1. The default value is 1.", "zh_CN":"取第几页，从 1 开始取值,默认为 1。"}
        self.page_index = page_index
        # {"en":"Number of forwarding tasks per page. The value ranges from 1 to 50. The default value is 10.", "zh_CN":"每页转推任务数量，取值范围 1-50，默认为10。"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.status is not None:
            result['status'] = self.status
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetForwardTaskListCodingParams(TeaModel):
    def __init__(
        self,
        bitrate: int = None,
        resolution: str = None,
        frame_rate: int = None,
        vcodec: str = None,
        acodec: str = None,
        wmimage: str = None,
        wmposition: str = None,
    ):
        # {"en":"Bit rate, in kbps, for example, 1200", "zh_CN":"码率，单位 kbps，例如 1200"}
        self.bitrate = bitrate
        # {"en":"Resolution, for example: 420x720 (with a lowercase x in the middle)", "zh_CN":"分辨率，例如：420x720 (中间是小写字母的 x)"}
        self.resolution = resolution
        # {"en":"Frame rate, for example, 25", "zh_CN":"帧率，例如：25"}
        self.frame_rate = frame_rate
        # {"en":"libx264, supported schemes: libx264, libx265, libvpx, etc. Also need to add watermark fixed fill in libx264", "zh_CN":"libx264，支持方案：libx264，libx265，libvpx 等。同时需添加水印时固定填写为libx264。"}
        self.vcodec = vcodec
        # {"en":"libfaac, supported schemes: libmp3lame, libfaac, libvorbis, etc", "zh_CN":"libfaac，支持方案：libmp3lame，libfaac，libvorbis 等。"}
        self.acodec = acodec
        # {"en":"Watermark image URL address: If the url contains &, url escape is required", "zh_CN":"水印图片的 URL 地址：如果 url 中带&，则需要进行 url 转义"}
        self.wmimage = wmimage
        # {"en":"Watermark position", "zh_CN":"水印位置，TOP_LEFT 左上角；TOP_CENTER 上部居中；TOP_RIGHT 右上角；CENTER_LEFT 中部靠左；CENTER 居中；CENTER_RIGHT 中部靠右；BOTTOM_LEFT 左下角；BOTTOM_CENTER 下居中；BOTTOM_RIGHT 右下角。"}
        self.wmposition = wmposition

    def validate(self):
        self.validate_required(self.bitrate, 'bitrate')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.frame_rate, 'frame_rate')
        self.validate_required(self.vcodec, 'vcodec')
        self.validate_required(self.acodec, 'acodec')
        self.validate_required(self.wmimage, 'wmimage')
        self.validate_required(self.wmposition, 'wmposition')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.frame_rate is not None:
            result['frameRate'] = self.frame_rate
        if self.vcodec is not None:
            result['vcodec'] = self.vcodec
        if self.acodec is not None:
            result['acodec'] = self.acodec
        if self.wmimage is not None:
            result['wmimage'] = self.wmimage
        if self.wmposition is not None:
            result['wmposition'] = self.wmposition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('frameRate') is not None:
            self.frame_rate = m.get('frameRate')
        if m.get('vcodec') is not None:
            self.vcodec = m.get('vcodec')
        if m.get('acodec') is not None:
            self.acodec = m.get('acodec')
        if m.get('wmimage') is not None:
            self.wmimage = m.get('wmimage')
        if m.get('wmposition') is not None:
            self.wmposition = m.get('wmposition')
        return self


class GetForwardTaskListForwardTastListItem(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        pull_id: str = None,
        status: int = None,
        forward_url: str = None,
        start_time: int = None,
        end_time: int = None,
        notify_url: str = None,
        create_user: str = None,
        crreate_time: int = None,
        coding_params: GetForwardTaskListCodingParams = None,
    ):
        # {"en":"taskId", "zh_CN":"转推任务 ID"}
        self.task_id = task_id
        # {"en":"pullId", "zh_CN":"频道 ID"}
        self.pull_id = pull_id
        # {"en":"Task status, which is used to filter tasks. Value range: 0: not started. 1: transfer process; 2: has ended; 3: Exception", "zh_CN":"任务状态，用于筛选任务，取值范围：0：未开始；1：转推中；2：已结束；3：异常"}
        self.status = status
        # {"en":"forwardUrl", "zh_CN":"转推地址"}
        self.forward_url = forward_url
        # {"en":"Start push time, second timestamp", "zh_CN":"开始转推时间,秒级时间戳"}
        self.start_time = start_time
        # {"en":"End of push time, second timestamp", "zh_CN":"结束转推时间,秒级时间戳"}
        self.end_time = end_time
        # {"en":"User-defined notification address", "zh_CN":"用户自定义的通知地址，以 http://开头或https://开头。"}
        self.notify_url = notify_url
        # {"en":"createUser", "zh_CN":"创建人"}
        self.create_user = create_user
        # {"en":"crreateTime", "zh_CN":"创建时间"}
        self.crreate_time = crreate_time
        # {"en":"Set the push encoding parameter", "zh_CN":"转推编码参数设置"}
        self.coding_params = coding_params

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.forward_url, 'forward_url')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.notify_url, 'notify_url')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.crreate_time, 'crreate_time')
        self.validate_required(self.coding_params, 'coding_params')
        if self.coding_params:
            self.coding_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.status is not None:
            result['status'] = self.status
        if self.forward_url is not None:
            result['forwardUrl'] = self.forward_url
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.crreate_time is not None:
            result['crreateTime'] = self.crreate_time
        if self.coding_params is not None:
            result['codingParams'] = self.coding_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('forwardUrl') is not None:
            self.forward_url = m.get('forwardUrl')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('crreateTime') is not None:
            self.crreate_time = m.get('crreateTime')
        if m.get('codingParams') is not None:
            temp_model = GetForwardTaskListCodingParams()
            self.coding_params = temp_model.from_map(m['codingParams'])
        return self


class GetForwardTaskListData(TeaModel):
    def __init__(
        self,
        total: int = None,
        forward_tast_list: GetForwardTaskListForwardTastListItem = None,
    ):
        # {"en":"The number of task list records that are currently returned", "zh_CN":"当前返回的任务列表信息的记录数"}
        self.total = total
        # {"en":"ForwardTaskList information", "zh_CN":"转推任务列表信息"}
        self.forward_tast_list = forward_tast_list

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.forward_tast_list, 'forward_tast_list')
        if self.forward_tast_list:
            self.forward_tast_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.forward_tast_list is not None:
            result['forwardTastList'] = self.forward_tast_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('forwardTastList') is not None:
            temp_model = GetForwardTaskListForwardTastListItem()
            self.forward_tast_list = temp_model.from_map(m['forwardTastList'])
        return self


class GetForwardTaskListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetForwardTaskListData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = GetForwardTaskListData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetForwardTaskListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetForwardTaskListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetForwardTaskListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetForwardTaskListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DisconnectStreamRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Channel pull ID, unique identifier of the channel", "zh_CN":"频道拉流 ID，频道唯一标识"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class DisconnectStreamResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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


class DisconnectStreamPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisconnectStreamParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisconnectStreamRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DisconnectStreamResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EndRecordTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"id of the live recording task", "zh_CN":"直播录制任务id"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class EndRecordTaskData(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndRecordTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: EndRecordTaskData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = EndRecordTaskData()
            self.data = temp_model.from_map(m['data'])
        return self


class EndRecordTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndRecordTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndRecordTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EndRecordTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class StartForwardTaskRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        forward_url: str = None,
        start_time: int = None,
        end_time: int = None,
        coding_params: str = None,
        notify_url: str = None,
    ):
        # {"en":"pullId", "zh_CN":"频道 ID"}
        self.pull_id = pull_id
        # {"en":"Indicates the address to be forwarded. Only the rtmp format is supported.", "zh_CN":"需要转推的地址，只支持 rtmp 格式推流。"}
        self.forward_url = forward_url
        # {"en":"Scheduled start time, timestamp in seconds. If the start time is less than the current time, push immediately from the current time.", "zh_CN":"计划开始时间，秒级时间戳，开始小于当前时间时，则从当前时间立即开始转推。"}
        self.start_time = start_time
        # {"en":"The scheduled end time is a timestamp in seconds. The end time must be more than 5 minutes later than the start time and more than 5 minutes later than the current time.", "zh_CN":"计划结束时间，秒级时间戳，结束时间必须晚于开始时间 5 分钟以上，并且晚于当前时间 5 分钟以上。"}
        self.end_time = end_time
        # {"en":"jsonType", "zh_CN":"此字段为json类型，字段如下：
        #   bitrate int 非必填 码率，单位 kbps，例如 800
        #   resolution string 非必填 分辨率，例如：420x720 (中间是小写字母的“x”)
        #   frameRate int 非必填 帧率，例如：25
        #   vcodec string 非必填 libx264，支持方案：libx264，libx265，libvpx 等。同时需添加水印时固定填写为libx264
        #   acodec string 非必填 libfaac，支持方案：libmp3lame，libfaac，libvorbis 等
        #   wmimage string 非必填 水印图片的 URL 地址：如果 url 中带&，则需要进行 url 转义。wmimage 参数和wmposition 参数必须同时都传或同时不传
        #   wmposition string 非必填 水印位置。wmimage 参数和 wmposition 参数必须同时都传或同时不传。TOP_LEFT 左上角；TOP_CENTER 上部居中；TOP_RIGHT 右上角；CENTER_LEFT 中部靠左；CENTER 居中；CENTER_RIGHT 中部靠右；BOTTOM_LEFT 左下角；BOTTOM_CENTER 下居中；BOTTOM_RIGHT 右下角 
        #   "}
        self.coding_params = coding_params
        # {"en":"User-defined notification address", "zh_CN":"用户自定义的通知地址，必须以 http://开头或 https://开头。"}
        self.notify_url = notify_url

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.forward_url, 'forward_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.forward_url is not None:
            result['forwardUrl'] = self.forward_url
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.coding_params is not None:
            result['codingParams'] = self.coding_params
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('forwardUrl') is not None:
            self.forward_url = m.get('forwardUrl')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('codingParams') is not None:
            self.coding_params = m.get('codingParams')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        return self


class StartForwardTaskData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"taskId", "zh_CN":"转推任务 ID"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class StartForwardTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: StartForwardTaskData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = StartForwardTaskData()
            self.data = temp_model.from_map(m['data'])
        return self


class StartForwardTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StartForwardTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StartForwardTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class StartForwardTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreatePullChannelRequest(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        source_pull_url: str = None,
        source_pull_protocol: str = None,
        pull_domain: str = None,
        pull_protocol: str = None,
        pull_rate: str = None,
        player_id: str = None,
    ):
        # {"en":"Channel name, The value contains a maximum of 255 characters", "zh_CN":"频道名称，最长255个字符"}
        self.channel_name = channel_name
        # {"en":"Source pull url The system pulls the live stream as the live stream source", "zh_CN":"源端拉流 url系统会拉取该直播流作为直播源"}
        self.source_pull_url = source_pull_url
        # {"en":"Source pull protocol: A channel can have only one back pull protocol, and a source pull basin name can be used for only one source pull protocol channel. 0, RTMP, 1, Http flv", "zh_CN":"源端拉流协议，一个频道只能有一种回源拉流协议，且一个源拉流域名只能用于一种源拉流协议频道；0、RTMP，1、Http flv"}
        self.source_pull_protocol = source_pull_protocol
        # {"en":"Player end pull basin name; The domain name must exist in the background domain name list of the cloud live streaming service", "zh_CN":"播放端拉流域名；域名必须存在于云直播服务后台域名列表中"}
        self.pull_domain = pull_domain
        # {"en":"The value can be multiple, separated by commas (,). The default value is 0 and 2/3. The value cannot be both. 0, RTMP, 1, Http flv, 2, HLS, 3, HDS", "zh_CN":"播放端拉流协议，可多选，用“，”隔开，默认选择 0，2/3 不可同时选择，协议需包含在推流域名实际配置的转出协议类型中；0、RTMP，1、Http flv，2、HLS，3、HDS"}
        self.pull_protocol = pull_protocol
        # {"en":"The player can select multiple bit rates, separated by commas (,), and ensure that the selected bit rates are within the range of the transcoding bit rates configured by the basin name. 0, source rate, 1, smooth, 2, standard definition, 3, HD, 4, super clear;", "zh_CN":"播放端拉流码率，可多选，用“，”隔开，确保选择的码率包含在推流域名配置的转码码率范围内；0、源码率，1、流畅，2、标清，3、高清，4、超清；"}
        self.pull_rate = pull_rate
        # {"en":"flash player ID used by the channel. If not set, the default player is used", "zh_CN":"频道使用的 flash 播放器 ID，未设置则使用默认播放器"}
        self.player_id = player_id

    def validate(self):
        self.validate_required(self.channel_name, 'channel_name')
        self.validate_required(self.source_pull_url, 'source_pull_url')
        self.validate_required(self.source_pull_protocol, 'source_pull_protocol')
        self.validate_required(self.pull_domain, 'pull_domain')
        self.validate_required(self.pull_rate, 'pull_rate')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.source_pull_url is not None:
            result['sourcePullUrl'] = self.source_pull_url
        if self.source_pull_protocol is not None:
            result['sourcePullProtocol'] = self.source_pull_protocol
        if self.pull_domain is not None:
            result['pullDomain'] = self.pull_domain
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.pull_rate is not None:
            result['pullRate'] = self.pull_rate
        if self.player_id is not None:
            result['playerId'] = self.player_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('sourcePullUrl') is not None:
            self.source_pull_url = m.get('sourcePullUrl')
        if m.get('sourcePullProtocol') is not None:
            self.source_pull_protocol = m.get('sourcePullProtocol')
        if m.get('pullDomain') is not None:
            self.pull_domain = m.get('pullDomain')
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('pullRate') is not None:
            self.pull_rate = m.get('pullRate')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        return self


class CreatePullChannelData(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
    ):
        # {"en":"Pull stream ID, globally unique, immutable", "zh_CN":"拉流 ID，全局唯一值，不可变"}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class CreatePullChannelResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CreatePullChannelData = None,
    ):
        # {"en":"status code", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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
            temp_model = CreatePullChannelData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreatePullChannelPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePullChannelParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePullChannelRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePullChannelResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetDirectoryListRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Page number, default is 1", "zh_CN":"第几页，默认为 1"}
        self.page_index = page_index
        # {"en":"The value ranges from 1 to 50. The default value is 10", "zh_CN":"每页数量，默认为 10，取值范围 1-50"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetDirectoryListDirectoryListItem(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_type: str = None,
        first_level_directory: str = None,
        second_level_directory: str = None,
        third_level_directory: str = None,
        update_time: str = None,
    ):
        # {"en":"Record directory creation time", "zh_CN":"录制目录创建时间"}
        self.create_time = create_time
        # {"en":"Record directory id", "zh_CN":"录制目录 ID"}
        self.directory_id = directory_id
        # {"en":"Record directory type", "zh_CN":"录制目录 type"}
        self.directory_type = directory_type
        # {"en":"Primary directory", "zh_CN":"一级目录"}
        self.first_level_directory = first_level_directory
        # {"en":"Secondary directory", "zh_CN":"二级目录"}
        self.second_level_directory = second_level_directory
        # {"en":"Three-level directory", "zh_CN":"三级目录"}
        self.third_level_directory = third_level_directory
        # {"en":"Record directory modification time", "zh_CN":"录制目录修改时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.first_level_directory, 'first_level_directory')
        self.validate_required(self.second_level_directory, 'second_level_directory')
        self.validate_required(self.third_level_directory, 'third_level_directory')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_type is not None:
            result['directoryType'] = self.directory_type
        if self.first_level_directory is not None:
            result['firstLevelDirectory'] = self.first_level_directory
        if self.second_level_directory is not None:
            result['secondLevelDirectory'] = self.second_level_directory
        if self.third_level_directory is not None:
            result['thirdLevelDirectory'] = self.third_level_directory
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')
        if m.get('firstLevelDirectory') is not None:
            self.first_level_directory = m.get('firstLevelDirectory')
        if m.get('secondLevelDirectory') is not None:
            self.second_level_directory = m.get('secondLevelDirectory')
        if m.get('thirdLevelDirectory') is not None:
            self.third_level_directory = m.get('thirdLevelDirectory')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetDirectoryListData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        directory_list: List[GetDirectoryListDirectoryListItem] = None,
    ):
        # {"en":"Total number of recorded directories", "zh_CN":"录制目录总数量"}
        self.total_count = total_count
        # {"en":"The recorded directory list is returned", "zh_CN":"返回的录制目录列表信息"}
        self.directory_list = directory_list

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.directory_list, 'directory_list')
        if self.directory_list:
            for k in self.directory_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.directory_list is not None:
            result['directoryList'] = []
            for k in self.directory_list:
                result['directoryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('directoryList') is not None:
            self.directory_list = []
            for k in m.get('directoryList'):
                temp_model = GetDirectoryListDirectoryListItem()
                self.directory_list.append(temp_model.from_map(k))
        return self


class GetDirectoryListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[GetDirectoryListData] = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
                temp_model = GetDirectoryListData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDirectoryListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDirectoryListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DirectoryCreateRequest(TeaModel):
    def __init__(
        self,
        directory_type: str = None,
        first_level_directory: str = None,
        second_level_directory: str = None,
        third_level_directory: str = None,
    ):
        # {"en":"Directory type. The value contains a maximum of 40 fields, including letters, digits, and underscores (_). The name of a user must be unique.", "zh_CN":"目录类型, 只支持中文、大小写字母、数字和下划线，不超过 40 个字段，同个用户下名称不能重复。"}
        self.directory_type = directory_type
        # {"en":"The level-1 directory cannot start with cloudv or cloudv-, contains a maximum of 128 fields, supports only lowercase letters, digits, and hyphens (-), and cannot be the same as the reserved character. Reserved words have video, live, pullvideo, clip, concat, watermarker, logo, buffer, record, static, AD", "zh_CN":"一级目录，不能以 cloudv 或 cloudv-开头,长度不超过 128 个字段，只支持小写字母、数字和中划线 ， 不 能 与 保 留 字 同 名 ， 保 留 字 有video,live,pullvideo,clip,concat,watermarker,logo,buffer,record,static,ad"}
        self.first_level_directory = first_level_directory
        # {"en":"The second-level directory cannot start with cloudv or cloudv- and contains a maximum of 128 fields. Only lowercase letters, digits, and hyphens (-) are supported", "zh_CN":"二级目录，不能以 cloudv 或 cloudv-开头,长度不超过 128 个字段，只支持小写字母、数字和中划线"}
        self.second_level_directory = second_level_directory
        # {"en":"The three-level directory cannot start with cloudv or cloudv-, contains a maximum of 128 fields, and supports only lowercase letters, digits, and hyphens (-)", "zh_CN":"三级目录，不能以 cloudv 或 cloudv-开头,长度不超过 128 个字段，只支持小写字母、数字和中划线"}
        self.third_level_directory = third_level_directory

    def validate(self):
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.first_level_directory, 'first_level_directory')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_type is not None:
            result['directoryType'] = self.directory_type
        if self.first_level_directory is not None:
            result['firstLevelDirectory'] = self.first_level_directory
        if self.second_level_directory is not None:
            result['secondLevelDirectory'] = self.second_level_directory
        if self.third_level_directory is not None:
            result['thirdLevelDirectory'] = self.third_level_directory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')
        if m.get('firstLevelDirectory') is not None:
            self.first_level_directory = m.get('firstLevelDirectory')
        if m.get('secondLevelDirectory') is not None:
            self.second_level_directory = m.get('secondLevelDirectory')
        if m.get('thirdLevelDirectory') is not None:
            self.third_level_directory = m.get('thirdLevelDirectory')
        return self


class DirectoryCreateData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_type: str = None,
        first_level_directory: str = None,
        second_level_directory: str = None,
        third_level_directory: str = None,
        update_time: str = None,
    ):
        # {"en":"Record directory creation time", "zh_CN":"录制目录创建时间"}
        self.create_time = create_time
        # {"en":"Recorded directory ID", "zh_CN":"录制目录 ID"}
        self.directory_id = directory_id
        # {"en":"Directory type", "zh_CN":"目录类型"}
        self.directory_type = directory_type
        # {"en":"Primary directory", "zh_CN":"一级目录"}
        self.first_level_directory = first_level_directory
        # {"en":"Secondary directory", "zh_CN":"二级目录"}
        self.second_level_directory = second_level_directory
        # {"en":"Three-level directory", "zh_CN":"三级目录"}
        self.third_level_directory = third_level_directory
        # {"en":"Record directory modification time", "zh_CN":"录制目录修改时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.first_level_directory, 'first_level_directory')
        self.validate_required(self.second_level_directory, 'second_level_directory')
        self.validate_required(self.third_level_directory, 'third_level_directory')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.directory_type is not None:
            result['directoryType'] = self.directory_type
        if self.first_level_directory is not None:
            result['firstLevelDirectory'] = self.first_level_directory
        if self.second_level_directory is not None:
            result['secondLevelDirectory'] = self.second_level_directory
        if self.third_level_directory is not None:
            result['thirdLevelDirectory'] = self.third_level_directory
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')
        if m.get('firstLevelDirectory') is not None:
            self.first_level_directory = m.get('firstLevelDirectory')
        if m.get('secondLevelDirectory') is not None:
            self.second_level_directory = m.get('secondLevelDirectory')
        if m.get('thirdLevelDirectory') is not None:
            self.third_level_directory = m.get('thirdLevelDirectory')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class DirectoryCreateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: DirectoryCreateData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = DirectoryCreateData()
            self.data = temp_model.from_map(m['data'])
        return self


class DirectoryCreatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DirectoryCreateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DirectoryCreateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DirectoryCreateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SetPushTsatcRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        effective_hour_long: str = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流 id"}
        self.pull_id = pull_id
        # {"en":"Validity period: Set the validity period of anti-leaver link parameters, accurate to second.", "zh_CN":"有效时长，设置防盗链参数有效期，精确到秒。"}
        self.effective_hour_long = effective_hour_long

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.effective_hour_long, 'effective_hour_long')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.effective_hour_long is not None:
            result['effectiveHourLong'] = self.effective_hour_long
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('effectiveHourLong') is not None:
            self.effective_hour_long = m.get('effectiveHourLong')
        return self


class SetPushTsatcData(TeaModel):
    def __init__(
        self,
        push_url: str = None,
    ):
        # {"en":"Push URL", "zh_CN":"推流 URL"}
        self.push_url = push_url

    def validate(self):
        self.validate_required(self.push_url, 'push_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_url is not None:
            result['pushUrl'] = self.push_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pushUrl') is not None:
            self.push_url = m.get('pushUrl')
        return self


class SetPushTsatcResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: SetPushTsatcData = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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
            temp_model = SetPushTsatcData()
            self.data = temp_model.from_map(m['data'])
        return self


class SetPushTsatcPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPushTsatcParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPushTsatcRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPushTsatcResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class BatchChannelLiveStateRequest(TeaModel):
    def __init__(
        self,
        pull_ids: str = None,
    ):
        # {"en":"Pull stream id. Multiple pull stream ids are separated by \",\"; Left blank Default return all channel status", "zh_CN":"拉流 id，多个拉流 id 用\",\"隔开；未填写默认返回所有频道的状态"}
        self.pull_ids = pull_ids

    def validate(self):
        self.validate_required(self.pull_ids, 'pull_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_ids is not None:
            result['pullIds'] = self.pull_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullIds') is not None:
            self.pull_ids = m.get('pullIds')
        return self


class BatchChannelLiveStateChannelStatusList(TeaModel):
    def __init__(
        self,
        channel_status: str = None,
        pull_id: str = None,
    ):
        # {"en":"Return the live stream status corresponding to each pull stream ID:
        # 1. Live broadcast 2. Not live broadcast 3. Banned", "zh_CN":"返回每个拉流 ID 对应的直播流实时状态： 
        # 1、直播中   2、未直播  3、禁播"}
        self.channel_status = channel_status
        # {"en":"The pull stream id of the channel to be queried must correspond to ChannelState", "zh_CN":"待查询频道的拉流 id，与 ChannelState 要一一对应 "}
        self.pull_id = pull_id

    def validate(self):
        self.validate_required(self.channel_status, 'channel_status')
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_status is not None:
            result['channelStatus'] = self.channel_status
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelStatus') is not None:
            self.channel_status = m.get('channelStatus')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        return self


class BatchChannelLiveStateResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[BatchChannelLiveStateChannelStatusList] = None,
    ):
        # {"en":"status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"return data", "zh_CN":"返回数据"}
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
                temp_model = BatchChannelLiveStateChannelStatusList()
                self.data.append(temp_model.from_map(k))
        return self


class BatchChannelLiveStatePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BatchChannelLiveStateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BatchChannelLiveStateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class BatchChannelLiveStateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RecordTaskQueryRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        trans_no: str = None,
    ):
        # {"en":"id of the live recording task", "zh_CN":"直播录制任务id"}
        self.task_id = task_id
        # {"en":"The custom task number passed by the customer,transNo and taskId have at least one value that is not empty or an empty string. If both values are passed, only taskId is used as the query condition.", "zh_CN":"客户传入的自定义任务编号,transNo 和 taskId 至少有一个值不为空或空字符串，如果两个都有传的情况下，只使用 taskId 作为查询条件。"}
        self.trans_no = trans_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        return self


class RecordTaskQueryFileListItem(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        video_id: str = None,
        file_size: str = None,
        video_duration: str = None,
        start_time: str = None,
        end_time: str = None,
        file_url: str = None,
    ):
        # {"en":"Video name", "zh_CN":"视频名称"}
        self.file_name = file_name
        # {"en":"Video id", "zh_CN":"视频id"}
        self.video_id = video_id
        # {"en":"Video size", "zh_CN":"视频大小"}
        self.file_size = file_size
        # {"en":"Video duration", "zh_CN":"视频时长"}
        self.video_duration = video_duration
        # {"en":"Task start time", "zh_CN":"任务开始时间"}
        self.start_time = start_time
        # {"en":"Task end time", "zh_CN":"任务结束时间"}
        self.end_time = end_time
        # {"en":"URL of the recording file. If the value-added recording directory management service is enabled, the recorded files are saved to the corresponding recording directory of the channel.", "zh_CN":"录制文件的 URL。如果有开通录制目录管理增值服务，则录制文件会保存到频道对应的录制目录下。"}
        self.file_url = file_url

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.video_duration, 'video_duration')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.file_url, 'file_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        return self


class RecordTaskQueryData(TeaModel):
    def __init__(
        self,
        status: int = None,
        trans_no: str = None,
        task_id: str = None,
        file_list: List[RecordTaskQueryFileListItem] = None,
    ):
        # {"en":"Status of the recording task: 0 is not started, 1 is started, 2 is normally finished, and 3 is terminated", "zh_CN":"录制任务的状态， 0 未开始，1 已开始，2 正常结束，3 终止"}
        self.status = status
        # {"en":"The custom task number passed in by the customer", "zh_CN":"客户传入的自定义任务编号"}
        self.trans_no = trans_no
        # {"en":"Id of the live recording task", "zh_CN":"直播录制任务 ID"}
        self.task_id = task_id
        # {"en":"List of files that have completed recording", "zh_CN":"录制完成的文件列表"}
        self.file_list = file_list

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.task_id, 'task_id')
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
        if self.status is not None:
            result['status'] = self.status
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.file_list is not None:
            result['fileList'] = []
            for k in self.file_list:
                result['fileList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('fileList') is not None:
            self.file_list = []
            for k in m.get('fileList'):
                temp_model = RecordTaskQueryFileListItem()
                self.file_list.append(temp_model.from_map(k))
        return self


class RecordTaskQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: RecordTaskQueryData = None,
    ):
        # {"en":"200 success", "zh_CN":"200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
            temp_model = RecordTaskQueryData()
            self.data = temp_model.from_map(m['data'])
        return self


class RecordTaskQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RecordTaskQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RecordTaskQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RecordTaskQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SetPullTsatcRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        effective_hour_long: str = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流 id"}
        self.pull_id = pull_id
        # {"en":"Validity period: Set the validity period of anti-leaver link parameters, accurate to second.", "zh_CN":"有效时长，设置防盗链参数有效期，精确到秒。"}
        self.effective_hour_long = effective_hour_long

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.effective_hour_long, 'effective_hour_long')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.effective_hour_long is not None:
            result['effectiveHourLong'] = self.effective_hour_long
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('effectiveHourLong') is not None:
            self.effective_hour_long = m.get('effectiveHourLong')
        return self


class SetPullTsatcPullUrlInfoList(TeaModel):
    def __init__(
        self,
        pull_domain: str = None,
        pull_protocol: str = None,
        audio_url: str = None,
        fluent_pull_url: str = None,
        fluent_zkgq_pull_url: str = None,
        hd_pull_url: str = None,
        hd_zkgq_pull_url: str = None,
        high_pull_url: str = None,
        high_zkgq_pull_url: str = None,
        origin_pull_url: str = None,
        origin_zkgq_pull_url: str = None,
        sd_pull_url: str = None,
        sd_zkgq_pull_url: str = None,
    ):
        # {"en":"Pull domain", "zh_CN":"拉流域名"}
        self.pull_domain = pull_domain
        # {"en":"Pull protocal", "zh_CN":"拉流协议"}
        self.pull_protocol = pull_protocol
        # {"en":"Audio Url", "zh_CN":"音频Url"}
        self.audio_url = audio_url
        # {"en":"Fluent code rate of flow url", "zh_CN":"流畅码率拉流 url"}
        self.fluent_pull_url = fluent_pull_url
        # {"en":"Fluent code rate of flow url(smart HD)", "zh_CN":"流畅码率（智控高清）拉流 url"}
        self.fluent_zkgq_pull_url = fluent_zkgq_pull_url
        # {"en":"Super clear bit rate of flow url", "zh_CN":"超清码率拉流 url "}
        self.hd_pull_url = hd_pull_url
        # {"en":"Super clear bit rate of flow url(smart HD)", "zh_CN":"超清码率（智控高清）拉流 url"}
        self.hd_zkgq_pull_url = hd_zkgq_pull_url
        # {"en":"High clear bit of flow url", "zh_CN":"高清码率拉流 url"}
        self.high_pull_url = high_pull_url
        # {"en":"High clear bit of flow url(smart HD)", "zh_CN":"高清码率（智控高清）拉流 url"}
        self.high_zkgq_pull_url = high_zkgq_pull_url
        # {"en":"Origin bit of flow url", "zh_CN":"源码率拉流 url"}
        self.origin_pull_url = origin_pull_url
        # {"en":"Origin bit of flow url(smart HD)", "zh_CN":"源码率（智控高清）拉流 url"}
        self.origin_zkgq_pull_url = origin_zkgq_pull_url
        # {"en":"Standard bit of flow url", "zh_CN":"标清码率拉流 url"}
        self.sd_pull_url = sd_pull_url
        # {"en":"Standard bit of flow url(smart HD)", "zh_CN":"标清码率（智控高清）拉流 url"}
        self.sd_zkgq_pull_url = sd_zkgq_pull_url

    def validate(self):
        self.validate_required(self.pull_domain, 'pull_domain')
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.audio_url, 'audio_url')
        self.validate_required(self.fluent_pull_url, 'fluent_pull_url')
        self.validate_required(self.fluent_zkgq_pull_url, 'fluent_zkgq_pull_url')
        self.validate_required(self.hd_pull_url, 'hd_pull_url')
        self.validate_required(self.hd_zkgq_pull_url, 'hd_zkgq_pull_url')
        self.validate_required(self.high_pull_url, 'high_pull_url')
        self.validate_required(self.high_zkgq_pull_url, 'high_zkgq_pull_url')
        self.validate_required(self.origin_pull_url, 'origin_pull_url')
        self.validate_required(self.origin_zkgq_pull_url, 'origin_zkgq_pull_url')
        self.validate_required(self.sd_pull_url, 'sd_pull_url')
        self.validate_required(self.sd_zkgq_pull_url, 'sd_zkgq_pull_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_domain is not None:
            result['pullDomain'] = self.pull_domain
        if self.pull_protocol is not None:
            result['pullProtocol'] = self.pull_protocol
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url
        if self.fluent_pull_url is not None:
            result['fluentPullUrl'] = self.fluent_pull_url
        if self.fluent_zkgq_pull_url is not None:
            result['fluentZkgqPullUrl'] = self.fluent_zkgq_pull_url
        if self.hd_pull_url is not None:
            result['hdPullUrl'] = self.hd_pull_url
        if self.hd_zkgq_pull_url is not None:
            result['hdZkgqPullUrl'] = self.hd_zkgq_pull_url
        if self.high_pull_url is not None:
            result['highPullUrl'] = self.high_pull_url
        if self.high_zkgq_pull_url is not None:
            result['highZkgqPullUrl'] = self.high_zkgq_pull_url
        if self.origin_pull_url is not None:
            result['originPullUrl'] = self.origin_pull_url
        if self.origin_zkgq_pull_url is not None:
            result['originZkgqPullUrl'] = self.origin_zkgq_pull_url
        if self.sd_pull_url is not None:
            result['sdPullUrl'] = self.sd_pull_url
        if self.sd_zkgq_pull_url is not None:
            result['sdZkgqPullUrl'] = self.sd_zkgq_pull_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullDomain') is not None:
            self.pull_domain = m.get('pullDomain')
        if m.get('pullProtocol') is not None:
            self.pull_protocol = m.get('pullProtocol')
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')
        if m.get('fluentPullUrl') is not None:
            self.fluent_pull_url = m.get('fluentPullUrl')
        if m.get('fluentZkgqPullUrl') is not None:
            self.fluent_zkgq_pull_url = m.get('fluentZkgqPullUrl')
        if m.get('hdPullUrl') is not None:
            self.hd_pull_url = m.get('hdPullUrl')
        if m.get('hdZkgqPullUrl') is not None:
            self.hd_zkgq_pull_url = m.get('hdZkgqPullUrl')
        if m.get('highPullUrl') is not None:
            self.high_pull_url = m.get('highPullUrl')
        if m.get('highZkgqPullUrl') is not None:
            self.high_zkgq_pull_url = m.get('highZkgqPullUrl')
        if m.get('originPullUrl') is not None:
            self.origin_pull_url = m.get('originPullUrl')
        if m.get('originZkgqPullUrl') is not None:
            self.origin_zkgq_pull_url = m.get('originZkgqPullUrl')
        if m.get('sdPullUrl') is not None:
            self.sd_pull_url = m.get('sdPullUrl')
        if m.get('sdZkgqPullUrl') is not None:
            self.sd_zkgq_pull_url = m.get('sdZkgqPullUrl')
        return self


class SetPullTsatcResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[SetPullTsatcPullUrlInfoList] = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Operational infomation", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
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
                temp_model = SetPullTsatcPullUrlInfoList()
                self.data.append(temp_model.from_map(k))
        return self


class SetPullTsatcPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPullTsatcParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPullTsatcRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetPullTsatcResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




