# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetAudioUploadTokenRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioUploadTokenItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        suffix: str = None,
        audio_id: str = None,
        upload_token: str = None,
        file_full_url: str = None,
    ):
        # {"en":"File name", "zh_CN":"文件名"}
        self.name = name
        # {"en":"File suffix", "zh_CN":"文件后缀"}
        self.suffix = suffix
        # {"en":"Audio id", "zh_CN":"音频id"}
        self.audio_id = audio_id
        # {"en":"Upload token", "zh_CN":"上传token"}
        self.upload_token = upload_token
        # {"en":"The path of the token file was uploaded", "zh_CN":"文件路径"}
        self.file_full_url = file_full_url

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.suffix, 'suffix')
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.upload_token, 'upload_token')
        self.validate_required(self.file_full_url, 'file_full_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.audio_id is not None:
            result['audioId'] = self.audio_id
        if self.upload_token is not None:
            result['uploadToken'] = self.upload_token
        if self.file_full_url is not None:
            result['fileFullUrl'] = self.file_full_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('audioId') is not None:
            self.audio_id = m.get('audioId')
        if m.get('uploadToken') is not None:
            self.upload_token = m.get('uploadToken')
        if m.get('fileFullUrl') is not None:
            self.file_full_url = m.get('fileFullUrl')
        return self


class GetAudioUploadTokenData(TeaModel):
    def __init__(
        self,
        upload_url: str = None,
        bucket_name: str = None,
        http_dns_server: str = None,
        items: List[GetAudioUploadTokenItem] = None,
    ):
        # {"en":"Upload url address", "zh_CN":"上传url地址"}
        self.upload_url = upload_url
        # {"en":"The bucket name of the WCS to upload", "zh_CN":"要上传的WCS的bucket名称"}
        self.bucket_name = bucket_name
        # {"en":"HttpDns server address", "zh_CN":"HttpDns服务器地址"}
        self.http_dns_server = http_dns_server
        # {"en":"Specific token information", "zh_CN":"具体token信息"}
        self.items = items

    def validate(self):
        self.validate_required(self.upload_url, 'upload_url')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.http_dns_server, 'http_dns_server')
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
        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.http_dns_server is not None:
            result['httpDnsServer'] = self.http_dns_server
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('httpDnsServer') is not None:
            self.http_dns_server = m.get('httpDnsServer')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = GetAudioUploadTokenItem()
                self.items.append(temp_model.from_map(k))
        return self


class GetAudioUploadTokenResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetAudioUploadTokenData = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
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
            temp_model = GetAudioUploadTokenData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetAudioUploadTokenPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioUploadTokenParameters(TeaModel):
    def __init__(
        self,
        file_list: str = None,
        domain: str = None,
        overwrite: bool = None,
    ):
        # {"en":"A list of documents that need to get the up-token, expressed as a json string, with url_safe_base64 encoding, up to 50 at a time
        # The parameters are as follows:
        # 1) name: Mandatory. The name of the upload file can contain a maximum of 200 characters
        # 2) suffix: Mandatory, file suffix, such as mp3. Currently, only mp3 format is supported
        # For example: Made from the following string url_safe_base64 coding [{\"name\":\"fileName1\",\"suffix\":\"mp3\"},{\"name\":\"fileName2\",\"suffix\":\"mp3\"}]", "zh_CN":"需要获取上传令牌的文档列表，用json字符串表示，并做url_safe_base64编码，最多一次性获取50个
        # 参数如下：
        # 1）name：必填，上传文件名， 长度最多不能超过200个字符
        # 2）suffix：必填，文件后缀，如mp3，目前只支持mp3格式
        # 例：用以下字符串做url_safe_base64编码[{\"name\":\"fileName1\",\"suffix\":\"mp3\"},{\"name\":\"fileName2\",\"suffix\":\"mp3\"}]"}
        self.file_list = file_list
        # {"en":"Audio domain name: If this parameter is left blank, set it to the default audio domain name. If the domain name does not exist, an error is returned. Without http:// or https://, for example, xxx.com", "zh_CN":"音频域名，如果不填或为空，则设为默认音频域名。如果域名不存在，返回错误。不带http://或https://，例：xxx.com"}
        self.domain = domain
        # {"en":"Upload policy, whether to overwrite. Default to true", "zh_CN":"上传策略，是否覆盖。默认为true"}
        self.overwrite = overwrite

    def validate(self):
        self.validate_required(self.file_list, 'file_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_list is not None:
            result['fileList'] = self.file_list
        if self.domain is not None:
            result['domain'] = self.domain
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileList') is not None:
            self.file_list = m.get('fileList')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        return self


class GetAudioUploadTokenRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioUploadTokenResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetUploadTokenRequest(TeaModel):
    def __init__(
        self,
        origin_file_name: str = None,
        file_id: str = None,
        file_md_5: str = None,
        domain: str = None,
        workflow_id: str = None,
        overwrite: int = None,
        category_names: str = None,
        water_mark_name: str = None,
        trans_code_combine_name: str = None,
        subtitle_id: str = None,
        subtitle: str = None,
    ):
        # {"en":"Upload the file name, including the file format", "zh_CN":"上传文件名，包含文件格式"}
        self.origin_file_name = origin_file_name
        # {"en":"File ID. The value is a string of up to 32 characters. It is used for resumable data from breakpoints. If the data is not transmitted, the resumable data from breakpoints is not supported.", "zh_CN":"文件ID，最长32位的任意字符串。用于断点续传，如果不传则不支持断点续传功能。"}
        self.file_id = file_id
        # {"en":"md5 value of the file, to be deprecated and replaced by fileId", "zh_CN":"文件的md5值，即将弃用，使用fileId代替"}
        self.file_md_5 = file_md_5
        # {"en":"If the video distribution domain name is not transmitted, the default video management domain name is used as the video distribution domain name. You can set the default domain name on the VOD Console > Global Configuration > Default Domain Name", "zh_CN":"视频发布域名，若不传，则以视频管理默认域名作为本视频的发布域名，可通过云点播控制台>全局配置>默认域名设置默认域名"}
        self.domain = domain
        # {"en":"Workflow ID, workflowId overrides cmd, waterMarkName, transCodeCombineName, and subtitleId", "zh_CN":"工作流ID，workflowId会覆盖cmd、waterMarkName、transCodeCombineName、subtitleId"}
        self.workflow_id = workflow_id
        # {"en":"Pass policy, whether to overwrite. Value range:
        # 0(no)
        # 1(Yes)", "zh_CN":"上传策略，是否覆盖。取值范围：
        # 0(否)
        # 1(是)"}
        self.overwrite = overwrite
        # {"en":"Video classification. You can specify parent and child categories.Such as: [{\"childName\":\"sub category 1\",\"parentName\":\"parent category 1\"},{\"childName\":\"subclassification 2\",\"parentName\":\"Parent category 2\"}]", "zh_CN":"视频分类，可指定父分类和子分类。如：[{\"childName\":\"子分类1\",\"parentName\":\"父分类1\"},{\"childName\":\"子分类2\",\"parentName\":\"父分类2\"}]"}
        self.category_names = category_names
        # {"en":"Watermark name. After successful upload, the watermark will be automatically transcoded", "zh_CN":"水印名,上传成功后会自动转码增加水印"}
        self.water_mark_name = water_mark_name
        # {"en":"Transcoding combination name, after successful upload will automatically transcoding to increase clarity", "zh_CN":"转码组合名,上传成功后会自动转码增加清晰度"}
        self.trans_code_combine_name = trans_code_combine_name
        # {"en":"Subtitle ID, corresponding to the material ID of Cloud VOD material management. After successful upload, subtitles will be automatically Transcoding and added; only ass or srt subtitle formats are supported.", "zh_CN":"字幕ID ,对应云点播素材管理的素材ID。上传成功后会自动转码增加字幕；仅支持ass或srt字幕格式。"}
        self.subtitle_id = subtitle_id
        # {"en":"Supports multiple subtitles, up to 13 subtitles can be added. Only supports multi- Bitrate adaptive Transcoding. Only supports vtt subtitle format.
        # The format content is:
        # lang: subtitle code, which can be defined according to your needs
        # subtitleId: subtitle ID, corresponding to the material ID of Cloud VOD material management
        # code[{\"lang\":\"cn\",\"subtitleId\":\"8a36dfe101921000368ac14400000000\"},{\"lang\":\"en-US\",\"subtitleId\":\"8a38e428019210004d56ef8c00000000\"},{\"lang\":\"ko\",\"subtitleId\":\"8a36dfe101921000368ac14400000000\"}] base64 encryption
        # The subtitle language corresponding code of the console player.
        # Language code
        # Chinese: cn
        # English: en-US
        # Japanese:ja
        # Traditional Chinese:zh-tw
        # French:fr
        # German: de
        # Spanish: es
        # Portuguese:pt
        # Russian:ru
        # Korean:ko
        # Thai:th
        # Vietnamese:vt
        # Indonesian:id"
        #   , "zh_CN":"支持多个字幕，最多可以添加13个字幕。只支持多码率自适应转码。仅支持vtt字幕格式。
        # 格式内容为：
        # lang：字幕code，可以根据自己需求定义
        # subtitleId：字幕ID，对应云点播素材管理的素材ID
        # code[{\"lang\":\"cn\",\"subtitleId\":\"8a36dfe101921000368ac14400000000\"},{\"lang\":\"en-US\",\"subtitleId\":\"8a38e428019210004d56ef8c00000000\"},{\"lang\":\"ko\",\"subtitleId\":\"8a36dfe101921000368ac14400000000\"}] 的base64加密
        # 控制台播放器字幕语言对应code。
        # 语言 code
        # 中文：cn
        # 英文：en-US
        # 日文:ja
        # 繁体中文:zh-tw
        # 法语:fr
        # 德语:de
        # 西班牙语:es
        # 葡萄牙语:pt
        # 俄语:ru
        # 韩语:ko
        # 泰语:th
        # 越南语:vt
        # 印尼语:id"}
        self.subtitle = subtitle

    def validate(self):
        self.validate_required(self.origin_file_name, 'origin_file_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_file_name is not None:
            result['originFileName'] = self.origin_file_name
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_md_5 is not None:
            result['fileMd5'] = self.file_md_5
        if self.domain is not None:
            result['domain'] = self.domain
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        if self.category_names is not None:
            result['categoryNames'] = self.category_names
        if self.water_mark_name is not None:
            result['waterMarkName'] = self.water_mark_name
        if self.trans_code_combine_name is not None:
            result['transCodeCombineName'] = self.trans_code_combine_name
        if self.subtitle_id is not None:
            result['subtitleId'] = self.subtitle_id
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originFileName') is not None:
            self.origin_file_name = m.get('originFileName')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileMd5') is not None:
            self.file_md_5 = m.get('fileMd5')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        if m.get('categoryNames') is not None:
            self.category_names = m.get('categoryNames')
        if m.get('waterMarkName') is not None:
            self.water_mark_name = m.get('waterMarkName')
        if m.get('transCodeCombineName') is not None:
            self.trans_code_combine_name = m.get('transCodeCombineName')
        if m.get('subtitleId') is not None:
            self.subtitle_id = m.get('subtitleId')
        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')
        return self


class GetUploadTokenData(TeaModel):
    def __init__(
        self,
        upload_url: str = None,
        file_key: str = None,
        http_dns_server: str = None,
        video_id: str = None,
        upload_token: str = None,
        speed_domainl_url: str = None,
        bucket_name: str = None,
    ):
        # {"en":"Upload domain address", "zh_CN":"上传域名地址"}
        self.upload_url = upload_url
        # {"en":"The relative path to the uploaded file, without the domain name or the leading slash", "zh_CN":"上传文件的相对路径，不带域名和最前面的斜杠"}
        self.file_key = file_key
        # {"en":"HttpDns server address", "zh_CN":"HttpDns服务器地址"}
        self.http_dns_server = http_dns_server
        # {"en":"Video ID. You can use this ID to query information about the video after it is uploaded", "zh_CN":"视频ID，上传完成后可通过该ID查询该视频相关信息"}
        self.video_id = video_id
        # {"en":"Upload token", "zh_CN":"上传token"}
        self.upload_token = upload_token
        # {"en":"[Planned Deprecation] Upload Accelerated domain address", "zh_CN":"【计划弃用】上传加速域名地址"}
        self.speed_domainl_url = speed_domainl_url
        # {"en":"Spatial name", "zh_CN":"空间名称"}
        self.bucket_name = bucket_name

    def validate(self):
        self.validate_required(self.upload_url, 'upload_url')
        self.validate_required(self.file_key, 'file_key')
        self.validate_required(self.http_dns_server, 'http_dns_server')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.upload_token, 'upload_token')
        self.validate_required(self.speed_domainl_url, 'speed_domainl_url')
        self.validate_required(self.bucket_name, 'bucket_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url
        if self.file_key is not None:
            result['fileKey'] = self.file_key
        if self.http_dns_server is not None:
            result['httpDnsServer'] = self.http_dns_server
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.upload_token is not None:
            result['uploadToken'] = self.upload_token
        if self.speed_domainl_url is not None:
            result['speedDomainlUrl'] = self.speed_domainl_url
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')
        if m.get('httpDnsServer') is not None:
            self.http_dns_server = m.get('httpDnsServer')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('uploadToken') is not None:
            self.upload_token = m.get('uploadToken')
        if m.get('speedDomainlUrl') is not None:
            self.speed_domainl_url = m.get('speedDomainlUrl')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        return self


class GetUploadTokenResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetUploadTokenData = None,
    ):
        # {"en":"Create the result status code. 200 indicates success", "zh_CN":"创建结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
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
            temp_model = GetUploadTokenData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetUploadTokenPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetUploadTokenParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetUploadTokenRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetUploadTokenResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PullVideoQueryRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        trans_no: str = None,
    ):
        # {"en":"Task ID
        # taskId and transNo must pass at least one packet, with taskId taking precedence", "zh_CN":"任务ID
        # taskId和transNo至少传一个，taskId优先使用"}
        self.task_id = task_id
        # {"en":"Service ID
        # taskId and transNo must pass at least one packet, with taskId taking precedence", "zh_CN":"业务ID
        # taskId和transNo至少传一个，taskId优先使用"}
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


class PullVideoQueryVideoFile(TeaModel):
    def __init__(
        self,
        clarity: int = None,
        server_type: int = None,
        bitrate: int = None,
        resolution: str = None,
        file_size: int = None,
        file_url: str = None,
    ):
        # {"en":"Clarity. Value range:
        # 1(original painting)
        # 2(fluency)
        # 3(standard definition)
        # 4(HD)
        # 5(Super clear)", "zh_CN":"清晰度。取值范围 ：
        # 1(原画)
        # 2(流畅)
        # 3(标清)
        # 4(高清)
        # 5(超清)"}
        self.clarity = clarity
        # {"en":"Terminal type. Value range:
        # 0(PC)
        # 1(original video)", "zh_CN":"终端类型。取值范围 ：
        # 0(PC)
        # 1(原视频)"}
        self.server_type = server_type
        # {"en":"Bit rate", "zh_CN":"码率"}
        self.bitrate = bitrate
        # {"en":"resolution", "zh_CN":"分辨率"}
        self.resolution = resolution
        # {"en":"File size", "zh_CN":"文件大小"}
        self.file_size = file_size
        # {"en":"Video url", "zh_CN":"视频url"}
        self.file_url = file_url

    def validate(self):
        self.validate_required(self.clarity, 'clarity')
        self.validate_required(self.server_type, 'server_type')
        self.validate_required(self.bitrate, 'bitrate')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.file_url, 'file_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.server_type is not None:
            result['serverType'] = self.server_type
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('serverType') is not None:
            self.server_type = m.get('serverType')
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        return self


class PullVideoQueryVideoInfo(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        duration: int = None,
        video_file_list: List[PullVideoQueryVideoFile] = None,
    ):
        # {"en":"Video id", "zh_CN":"视频id"}
        self.video_id = video_id
        # {"en":"duration", "zh_CN":"时长"}
        self.duration = duration
        # {"en":"Video file list", "zh_CN":"视频文件列表"}
        self.video_file_list = video_file_list

    def validate(self):
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.video_file_list, 'video_file_list')
        if self.video_file_list:
            for k in self.video_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.duration is not None:
            result['duration'] = self.duration
        if self.video_file_list is not None:
            result['videoFileList'] = []
            for k in self.video_file_list:
                result['videoFileList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('videoFileList') is not None:
            self.video_file_list = []
            for k in m.get('videoFileList'):
                temp_model = PullVideoQueryVideoFile()
                self.video_file_list.append(temp_model.from_map(k))
        return self


class PullVideoQueryItem(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        fetch_url: str = None,
        md_5: str = None,
        pull_status: int = None,
        cmd_status: int = None,
        video_info: PullVideoQueryVideoInfo = None,
    ):
        # {"en":"File name", "zh_CN":"文件名"}
        self.file_name = file_name
        # {"en":"Pull URL", "zh_CN":"拉取URL"}
        self.fetch_url = fetch_url
        # {"en":"Video md5", "zh_CN":"视频md5"}
        self.md_5 = md_5
        # {"en":"Pull the task execution status
        # Value range:
        # 1(in process)
        # 2(Successful)
        # 3(Failure)", "zh_CN":"拉取任务执行状态
        # 取值范围 ：
        # 1(处理中)
        # 2(成功)
        # 3(失败)"}
        self.pull_status = pull_status
        # {"en":"Execution status of the integration command
        # Value range:
        # 1(in process)
        # 2(Successful)
        # 3(Failure)", "zh_CN":"一体化命令执行状态
        # 取值范围 ：
        # 1(处理中)
        # 2(成功)
        # 3(失败)"}
        self.cmd_status = cmd_status
        # {"en":"Contains video id, video file list.
        # Video information includes bit rate, sharpness, resolution, terminal type, video URL", "zh_CN":"包含视频id,视频文件列表。
        # 视频信息包含码率，清晰度，分辨率，终端类型，视频URL"}
        self.video_info = video_info

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.fetch_url, 'fetch_url')
        self.validate_required(self.md_5, 'md_5')
        self.validate_required(self.pull_status, 'pull_status')
        self.validate_required(self.cmd_status, 'cmd_status')
        self.validate_required(self.video_info, 'video_info')
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.fetch_url is not None:
            result['fetchUrl'] = self.fetch_url
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.pull_status is not None:
            result['pullStatus'] = self.pull_status
        if self.cmd_status is not None:
            result['cmdStatus'] = self.cmd_status
        if self.video_info is not None:
            result['videoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fetchUrl') is not None:
            self.fetch_url = m.get('fetchUrl')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('pullStatus') is not None:
            self.pull_status = m.get('pullStatus')
        if m.get('cmdStatus') is not None:
            self.cmd_status = m.get('cmdStatus')
        if m.get('videoInfo') is not None:
            temp_model = PullVideoQueryVideoInfo()
            self.video_info = temp_model.from_map(m['videoInfo'])
        return self


class PullVideoQueryData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        trans_no: str = None,
        timestamp: str = None,
        status: int = None,
        items: List[PullVideoQueryItem] = None,
    ):
        # {"en":"Task ID", "zh_CN":"任务ID"}
        self.task_id = task_id
        # {"en":"trans NO", "zh_CN":"业务ID"}
        self.trans_no = trans_no
        # {"en":"Millisecond timestamp", "zh_CN":"毫秒级时间戳"}
        self.timestamp = timestamp
        # {"en":"Task status
        # Value range:
        # 1(in process)
        # 2(Completed)", "zh_CN":"任务状态
        # 取值范围 ：
        # 1(处理中)
        # 2(已完成)"}
        self.status = status
        # {"en":"Pull the result status information for each video.
        # If the processing request includes multiple videos, items contain multiple pieces of information", "zh_CN":"每个视频拉取结果状态信息。
        # 如果处理请求包括多个视频，则items包含多条信息"}
        self.items = items

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.timestamp, 'timestamp')
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
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.status is not None:
            result['status'] = self.status
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = PullVideoQueryItem()
                self.items.append(temp_model.from_map(k))
        return self


class PullVideoQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: PullVideoQueryData = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
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
            temp_model = PullVideoQueryData()
            self.data = temp_model.from_map(m['data'])
        return self


class PullVideoQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetMaterialUploadTokenFile(TeaModel):
    def __init__(
        self,
        name: str = None,
        suffix: str = None,
    ):
        # {"en":"The upload file name contains a maximum of 40 characters", "zh_CN":"上传文件名， 长度最多不能超过40个字符"}
        self.name = name
        # {"en":"GetMaterialUploadTokenFile suffix", "zh_CN":"文件后缀"}
        self.suffix = suffix

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.suffix is not None:
            result['suffix'] = self.suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        return self


class GetMaterialUploadTokenRequest(TeaModel):
    def __init__(
        self,
        file_list: List[GetMaterialUploadTokenFile] = None,
        domain: str = None,
        overwrite: bool = None,
    ):
        # {"en":"A list of documents (parameters including name and suffix) that need to be passed up tokens. A maximum of 50 documents need to be obtained at one time
        # For example: [{"name":"fileName1","suffix":"jpg"},{"name":"fileName2","suffix":"jpg"}]", "zh_CN":"需要获取上传令牌的文档列表（参数包含name、suffix），最多一次性获取50个
        # 例：[{"name":"fileName1","suffix":"jpg"},{"name":"fileName2","suffix":"jpg"}]"}
        self.file_list = file_list
        # {"en":"Material domain name. If this parameter is left blank, set it to the default material domain name. If the domain name does not exist, an error is returned. Without http:// or https://, for example, xxx.com", "zh_CN":"素材域名，如果不填或为空，则设为默认素材域名。如果域名不存在，返回错误。不带http://或https://，例：xxx.com"}
        self.domain = domain
        # {"en":"Upload policy, whether to overwrite. Default is false", "zh_CN":"上传策略，是否覆盖。默认为false"}
        self.overwrite = overwrite

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
        if self.file_list is not None:
            result['fileList'] = []
            for k in self.file_list:
                result['fileList'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['domain'] = self.domain
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileList') is not None:
            self.file_list = []
            for k in m.get('fileList'):
                temp_model = GetMaterialUploadTokenFile()
                self.file_list.append(temp_model.from_map(k))
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        return self


class GetMaterialUploadTokenItem(TeaModel):
    def __init__(
        self,
        name: str = None,
        suffix: str = None,
        material_id: str = None,
        upload_token: str = None,
        file_full_url: str = None,
    ):
        # {"en":"GetMaterialUploadTokenFile name", "zh_CN":"文件名"}
        self.name = name
        # {"en":"GetMaterialUploadTokenFile suffix", "zh_CN":"文件后缀"}
        self.suffix = suffix
        # {"en":"Material id", "zh_CN":"素材id"}
        self.material_id = material_id
        # {"en":"Upload token", "zh_CN":"上传token"}
        self.upload_token = upload_token
        # {"en":"GetMaterialUploadTokenFile path", "zh_CN":"文件路径"}
        self.file_full_url = file_full_url

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.suffix, 'suffix')
        self.validate_required(self.material_id, 'material_id')
        self.validate_required(self.upload_token, 'upload_token')
        self.validate_required(self.file_full_url, 'file_full_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.material_id is not None:
            result['materialId'] = self.material_id
        if self.upload_token is not None:
            result['uploadToken'] = self.upload_token
        if self.file_full_url is not None:
            result['fileFullUrl'] = self.file_full_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('materialId') is not None:
            self.material_id = m.get('materialId')
        if m.get('uploadToken') is not None:
            self.upload_token = m.get('uploadToken')
        if m.get('fileFullUrl') is not None:
            self.file_full_url = m.get('fileFullUrl')
        return self


class GetMaterialUploadTokenData(TeaModel):
    def __init__(
        self,
        upload_url: str = None,
        bucket_name: str = None,
        http_dns_server: str = None,
        items: List[GetMaterialUploadTokenItem] = None,
    ):
        # {"en":"Upload url address", "zh_CN":"上传url地址"}
        self.upload_url = upload_url
        # {"en":"The bucket name of the WCS to upload", "zh_CN":"要上传的WCS的bucket名称"}
        self.bucket_name = bucket_name
        # {"en":"HttpDns server address", "zh_CN":"HttpDns服务器地址"}
        self.http_dns_server = http_dns_server
        # {"en":"Specific token information", "zh_CN":"具体token信息"}
        self.items = items

    def validate(self):
        self.validate_required(self.upload_url, 'upload_url')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.http_dns_server, 'http_dns_server')
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
        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.http_dns_server is not None:
            result['httpDnsServer'] = self.http_dns_server
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('httpDnsServer') is not None:
            self.http_dns_server = m.get('httpDnsServer')
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = GetMaterialUploadTokenItem()
                self.items.append(temp_model.from_map(k))
        return self


class GetMaterialUploadTokenResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetMaterialUploadTokenData = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
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
            temp_model = GetMaterialUploadTokenData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetMaterialUploadTokenPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialUploadTokenParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialUploadTokenRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialUploadTokenResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PullVideoRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
        cmd: str = None,
        file_list: str = None,
        workflow_id: str = None,
        notify_url: str = None,
        separate: int = None,
        fetch_ts: int = None,
    ):
        # {"en":"The service ID must be unique and controlled by users
        # It is recommended that a 32-bit UUID be a string of up to 32 characters", "zh_CN":"业务ID，需用户自己控制唯一性
        # 建议使用32位UUID，并且最长为32位字符串"}
        self.trans_no = trans_no
        # {"en":"Command in the following format
        # {tcTemplateName:xxxx,workflowCode:xxx}", "zh_CN":"命令，格式如下
        # {tcTemplateName:xxxx,workflowCode:xxx}"}
        self.cmd = cmd
        # {"en":"The url and corresponding parameters of the video to be pulled are expressed in json strings and encoded in url_safe_base64. A maximum of 50 urls and parameters can be pulled at a time.
        # The parameters are as follows:
        # 1) filName: Specifies the name of the pulled file. It is recommended to include a format suffix. If no format suffix is included, the pulled video will not have a format suffix. If not, the file name is the URI at the end of the URL
        # 2) fetchUrl: Required, url of the file to be pulled
        # 3) md5: indicates the md5 value of the file to be pulled. Used to verify whether a file is damaged after being pulled. Do not fill, do not check
        # Example: Use the following string for url_safe_base64 encoding [{\"fileName\":\"fileName1\",\"fetchUrl\":\"fetchUrl1\",\"md5\":\"md51\"},{\"fileName\":\"fileName2\",\"fetchUrl\":\"fetchUrl2\",\"md5\":\"md52\"}]", "zh_CN":"待拉取视频的url及对应参数，用json字符串表示，并做url_safe_base64编码，最多一次性拉取50个。
        # 参数如下：
        # 1）fileName:指定拉取文件的文件名，建议包含格式后缀，如果不包含格式后缀，拉取后的视频也会没有格式后缀。如果不传，以URL最后一段URI为文件名
        # 2）fetchUrl:必填，待拉取文件url
        # 3）md5:待拉取文件md5值；用于验证拉取后文件是否有损坏。不填就不校验
        # 例：用以下字符串做url_safe_base64编码[{\"fileName\":\"fileName1\",\"fetchUrl\":\"fetchUrl1\",\"md5\":\"md51\"},{\"fileName\":\"fileName2\",\"fetchUrl\":\"fetchUrl2\",\"md5\":\"md52\"}]"}
        self.file_list = file_list
        # {"en":"Workflow ID", "zh_CN":"工作流ID"}
        self.workflow_id = workflow_id
        # {"en":"url to receive processing results. This url does not need to be encrypted.
        # For details about the notification content, see the interface document. The notification content is encoded in url_safe_base64", "zh_CN":"接收处理结果的url，该url不需要做加密操作。
        # 通知内容详见接口文档的说明，通知的内容会做url_safe_base64编码"}
        self.notify_url = notify_url
        # {"en":"Whether the processing instructions for pulling multiple videos are notified separately.
        # Value range:
        # 0(entire batch merge notification)
        # 1(each video is notified independently)
        # Default is 0", "zh_CN":"拉取多个视频的处理指令是否分开通知。
        # 取值范围 ：
        # 0(整个批次合并通知)
        # 1(每个视频独立通知)
        # 默认为0"}
        self.separate = separate
        # {"en":"The default value is 1.
        # 0: indicates not to capture TS files 
        # 1: Indicates that TS files need to be captured
        # Note: Encrypted hls files cannot be pulled", "zh_CN":"默认为1；
        # 0：表示不抓取TS文件 
        # 1：表示需要抓取TS文件
        # 备注：不能拉取加密的hls文件"}
        self.fetch_ts = fetch_ts

    def validate(self):
        self.validate_required(self.file_list, 'file_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.file_list is not None:
            result['fileList'] = self.file_list
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.separate is not None:
            result['separate'] = self.separate
        if self.fetch_ts is not None:
            result['fetchTs'] = self.fetch_ts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('fileList') is not None:
            self.file_list = m.get('fileList')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('separate') is not None:
            self.separate = m.get('separate')
        if m.get('fetchTs') is not None:
            self.fetch_ts = m.get('fetchTs')
        return self


class PullVideoFile(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        fetch_url: str = None,
        md_5: str = None,
    ):
        # {"en":"You are advised to include a format suffix. If no format suffix is included, the video that is pulled does not have a format suffix. If not, the file name is the URI at the end of the URL", "zh_CN":"指定拉取文件的文件名，建议包含格式后缀，如果不包含格式后缀，拉取后的视频也会没有格式后缀。如果不传，以URL最后一段URI为文件名"}
        self.file_name = file_name
        # {"en":"url of the file to be pulled", "zh_CN":"待拉取文件url"}
        self.fetch_url = fetch_url
        # {"en":"md5 value of the file to be pulled; Used to verify whether a file is damaged after being pulled. Do not fill, do not check", "zh_CN":"待拉取文件md5值；用于验证拉取后文件是否有损坏。不填就不校验"}
        self.md_5 = md_5

    def validate(self):
        self.validate_required(self.fetch_url, 'fetch_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.fetch_url is not None:
            result['fetchUrl'] = self.fetch_url
        if self.md_5 is not None:
            result['md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fetchUrl') is not None:
            self.fetch_url = m.get('fetchUrl')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        return self


class PullVideoData(TeaModel):
    def __init__(
        self,
        tran_no: str = None,
        task_id: str = None,
    ):
        # {"en":"trans NO", "zh_CN":"业务ID"}
        self.tran_no = tran_no
        # {"en":"Task ID", "zh_CN":"任务ID"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.tran_no, 'tran_no')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tran_no is not None:
            result['tranNo'] = self.tran_no
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tranNo') is not None:
            self.tran_no = m.get('tranNo')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class PullVideoResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: PullVideoData = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
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
            temp_model = PullVideoData()
            self.data = temp_model.from_map(m['data'])
        return self


class PullVideoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PullVideoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




