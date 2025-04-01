# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetPublishCodeRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        code_type: int = None,
    ):
        # {"en":"Video ID", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"
        # Play code type
        # Value range:
        # 0(all)
        # 2(swf code)
        # 4(Video URL)
        # 5(Adaptive code)
        # 6(Try watch video URL)
        # 7(Try watch adaptive code)
        # 8(The customized encrypted play code)
        # The default is 0;
        # General licensed video only has adaptive/video URL.
        # Normal encrypted video only swf/ customer custom/video URL.
        # Non-encrypted video only has swf/ Adaptive/Custom/video URL", "zh_CN":"播放代码类型
        # 取值范围 ：
        # 0(全部)
        # 2(swf代码)
        # 4(视频URL)
        # 5(自适应代码)
        # 6(试看视频URL)
        # 7(试看自适应代码)
        # 8(加密客户定制的播放代码)
        # 默认为0；
        # 通用授权视频只有自适应/视频URL。
        # 普通加密视频只swf/客户自定义/视频URL。
        # 非加密视频只有swf/自适应/客户自定义/视频URL"}
        self.code_type = code_type

    def validate(self):
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.code_type is not None:
            result['codeType'] = self.code_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        return self


class GetPublishCodeDataVideoUrl(TeaModel):
    def __init__(
        self,
        fluent_url: str = None,
        hd_pull_url: str = None,
        high_url: str = None,
        origin_url: str = None,
        sd_url: str = None,
        url_type: str = None,
    ):
        # {'en':'Smooth bit rate video url', 'zh_CN':'流畅码率视频url'}
        self.fluent_url = fluent_url
        # {'en':'Ultra clear bit rate video url', 'zh_CN':'超清码率视频url'}
        self.hd_pull_url = hd_pull_url
        # {'en':'Hd bit rate video url', 'zh_CN':'高清码率视频url'}
        self.high_url = high_url
        # {'en':'Original video url', 'zh_CN':'原画视频url'}
        self.origin_url = origin_url
        # {'en':'Standard definition bit rate video url', 'zh_CN':'标清码率视频url'}
        self.sd_url = sd_url
        # {'en':'PC/mobile terminal', 'zh_CN':'PC端/移动端'}
        self.url_type = url_type

    def validate(self):
        self.validate_required(self.fluent_url, 'fluent_url')
        self.validate_required(self.hd_pull_url, 'hd_pull_url')
        self.validate_required(self.high_url, 'high_url')
        self.validate_required(self.origin_url, 'origin_url')
        self.validate_required(self.sd_url, 'sd_url')
        self.validate_required(self.url_type, 'url_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fluent_url is not None:
            result['fluentUrl'] = self.fluent_url
        if self.hd_pull_url is not None:
            result['hdPullUrl'] = self.hd_pull_url
        if self.high_url is not None:
            result['highUrl'] = self.high_url
        if self.origin_url is not None:
            result['originUrl'] = self.origin_url
        if self.sd_url is not None:
            result['sdUrl'] = self.sd_url
        if self.url_type is not None:
            result['urlType'] = self.url_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fluentUrl') is not None:
            self.fluent_url = m.get('fluentUrl')
        if m.get('hdPullUrl') is not None:
            self.hd_pull_url = m.get('hdPullUrl')
        if m.get('highUrl') is not None:
            self.high_url = m.get('highUrl')
        if m.get('originUrl') is not None:
            self.origin_url = m.get('originUrl')
        if m.get('sdUrl') is not None:
            self.sd_url = m.get('sdUrl')
        if m.get('urlType') is not None:
            self.url_type = m.get('urlType')
        return self


class GetPublishCodeData(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        encrypt: int = None,
        auto_code: str = None,
        swf_code: str = None,
        custom_code: str = None,
        video_url: List[GetPublishCodeDataVideoUrl] = None,
    ):
        # {'en':'videoId', 'zh_CN':'视频ID'}
        self.video_id = video_id
        # {'en':'
        # Whether the video is encrypted
        # Value range:
        # 0(unencrypted)
        # 1(encryption)', 'zh_CN':'视频是否加密
        # 取值范围 ：
        # 0(不加密)
        # 1(加密)'}
        self.encrypt = encrypt
        # {'en':'Video adaptive code, encrypted video is empty', 'zh_CN':'视频自适应代码，加密视频为空'}
        self.auto_code = auto_code
        # {'en':'Video swf code', 'zh_CN':'视频swf代码'}
        self.swf_code = swf_code
        # {'en':'Custom play code. The default value is null. If you have personalized needs, please contact customer service.', 'zh_CN':'客户定制的播放代码。默认为空。如有个性化需求，请与客服联系。'}
        self.custom_code = custom_code
        self.video_url = video_url

    def validate(self):
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.encrypt, 'encrypt')
        self.validate_required(self.auto_code, 'auto_code')
        self.validate_required(self.swf_code, 'swf_code')
        self.validate_required(self.custom_code, 'custom_code')
        self.validate_required(self.video_url, 'video_url')
        if self.video_url:
            for k in self.video_url:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.encrypt is not None:
            result['encrypt'] = self.encrypt
        if self.auto_code is not None:
            result['autoCode'] = self.auto_code
        if self.swf_code is not None:
            result['swfCode'] = self.swf_code
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.video_url is not None:
            result['videoUrl'] = []
            for k in self.video_url:
                result['videoUrl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('encrypt') is not None:
            self.encrypt = m.get('encrypt')
        if m.get('autoCode') is not None:
            self.auto_code = m.get('autoCode')
        if m.get('swfCode') is not None:
            self.swf_code = m.get('swfCode')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('videoUrl') is not None:
            self.video_url = []
            for k in m.get('videoUrl'):
                temp_model = GetPublishCodeDataVideoUrl()
                self.video_url.append(temp_model.from_map(k))
        return self


class GetPublishCodeResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetPublishCodeData = None,
        message: str = None,
    ):
        # {'en':'Status code', 'zh_CN':'返回状态码'}
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
            temp_model = GetPublishCodeData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetPublishCodePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPublishCodeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPublishCodeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPublishCodeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




