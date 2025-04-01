# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VideoClipRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
        video_id: str = None,
        seek_start: int = None,
        duration: int = None,
        filename: str = None,
        resolution: str = None,
        frame_rate: int = None,
        video_bit_rate: int = None,
        audio_bit_rate: int = None,
        tassampling_ratek_id: int = None,
        notify_url: str = None,
        suffix: str = None,
        enable_video_transcode: int = None,
    ):
        # {"en":"The length of the customer video clipping task must be less than or equal to 32 bits. The customer must ensure that it is globally unique on the customer platform", "zh_CN":"客户视频剪切任务编码，长度小于等于32位，客户需要保证在客户平台侧全局唯一"}
        self.trans_no = trans_no
        # {"en":"Video that needs to be edited", "zh_CN":"需要剪辑的视频"}
        self.video_id = video_id
        # {"en":"Specifies the start time for video interception, in seconds", "zh_CN":"指定视频截取的开始时间，单位：秒"}
        self.seek_start = seek_start
        # {"en":"Specifies the length of the video capture, in seconds", "zh_CN":"指定视频截取的长度，单位：秒"}
        self.duration = duration
        # {"en":"Output video file name", "zh_CN":"输出视频文件名"}
        self.filename = filename
        # {"en":"Output video resolution in wxh format, for example, 640x480", "zh_CN":"输出视频分辨率，格式为 wxh，例如:640x480"}
        self.resolution = resolution
        # {"en":"Video frame rate: The number of frames displayed per second (unit: Hertz). Commonly used frame rates: 24,25,30, etc", "zh_CN":"视频帧率，每秒显示的帧数，单位：赫兹（Hz）。常用帧率：24，25，30等"}
        self.frame_rate = frame_rate
        # {"en":"Video bit rate, unit: kbit/s. Common video bit rate: 128,1250,5000, etc", "zh_CN":"视频比特率，单位： kbit/s。常用视频比特率：128，1250，5000等"}
        self.video_bit_rate = video_bit_rate
        # {"en":"Audio bit rate, unit: kbit/s. Common bit rate: 64,128,192,256,320, etc", "zh_CN":"音频码率，单位： kbit/s。常用码率：64，128，192，256，320等"}
        self.audio_bit_rate = audio_bit_rate
        # {"en":"Audio sampling frequency (unit: Hertz). Common sampling frequency: 8000,12050,22050,44100, etc. Note: flv only supports 4410220511025", "zh_CN":"音频采样频率，单位：赫兹（Hz）。常用采样频率：8000，12050，22050，44100等。注：flv只支持4410220511025"}
        self.tassampling_ratek_id = tassampling_ratek_id
        # {"en":"The completion address used to receive callback information", "zh_CN":"用于接收回调信息的完成地址"}
        self.notify_url = notify_url
        # {"en":"Output format
        # Value range:
        # flv
        # mp4
        # Default flv", "zh_CN":"输出格式
        # 取值范围 ：
        # flv
        # mp4
        # 默认flv"}
        self.suffix = suffix
        # {"en":"Start forced transcoding, 1: start. 0: Do not start, the default is 0", "zh_CN":"启动强制转码，1:启动。0:不启动 默认是0"}
        self.enable_video_transcode = enable_video_transcode

    def validate(self):
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.seek_start, 'seek_start')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.filename, 'filename')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.seek_start is not None:
            result['seekStart'] = self.seek_start
        if self.duration is not None:
            result['duration'] = self.duration
        if self.filename is not None:
            result['filename'] = self.filename
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.frame_rate is not None:
            result['frameRate'] = self.frame_rate
        if self.video_bit_rate is not None:
            result['videoBitRate'] = self.video_bit_rate
        if self.audio_bit_rate is not None:
            result['audioBitRate'] = self.audio_bit_rate
        if self.tassampling_ratek_id is not None:
            result['tassamplingRatekId'] = self.tassampling_ratek_id
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.enable_video_transcode is not None:
            result['enableVideoTranscode'] = self.enable_video_transcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('seekStart') is not None:
            self.seek_start = m.get('seekStart')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('filename') is not None:
            self.filename = m.get('filename')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('frameRate') is not None:
            self.frame_rate = m.get('frameRate')
        if m.get('videoBitRate') is not None:
            self.video_bit_rate = m.get('videoBitRate')
        if m.get('audioBitRate') is not None:
            self.audio_bit_rate = m.get('audioBitRate')
        if m.get('tassamplingRatekId') is not None:
            self.tassampling_ratek_id = m.get('tassamplingRatekId')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('enableVideoTranscode') is not None:
            self.enable_video_transcode = m.get('enableVideoTranscode')
        return self


class VideoClipResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"code", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"data", "zh_CN":"返回数据"}
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


class VideoClipPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ClearAdTaskQueryRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"AI clear AD task ID", "zh_CN":"AI清除广告任务ID"}
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


class ClearAdTaskQueryData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        status: int = None,
        output: str = None,
    ):
        # {"en":"AI clear AD task ID", "zh_CN":"AI清除广告任务ID"}
        self.task_id = task_id
        # {"en":"Status:
        # 0(not started)
        # 1(in progress)
        # 2(Successful)
        # 3(failure)", "zh_CN":"状态,取值范围:
        # 0(未开始)
        # 1(进行中)
        # 2(成功)
        # 3(失败)"}
        self.status = status
        # {"en":"New video ID", "zh_CN":"生成的新视频ID"}
        self.output = output

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.output, 'output')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.status is not None:
            result['status'] = self.status
        if self.output is not None:
            result['output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('output') is not None:
            self.output = m.get('output')
        return self


class ClearAdTaskQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: ClearAdTaskQueryData = None,
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
            temp_model = ClearAdTaskQueryData()
            self.data = temp_model.from_map(m['data'])
        return self


class ClearAdTaskQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ClearAdTaskQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ClearAdTaskQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ClearAdTaskQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VideoConcatRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
        video_ids: str = None,
        filename: str = None,
        dir_id: str = None,
        notify_url: str = None,
        suffix: str = None,
    ):
        # {"en":"The length of the customer video clipping task must be less than or equal to 32 bits. The customer must ensure that it is globally unique on the customer platform", "zh_CN":"客户视频剪切任务编码，长度小于等于32位，客户需要保证在客户平台侧全局唯一"}
        self.trans_no = trans_no
        # {"en":"Separate the videos to be spliced using commas (,) in the splicing order", "zh_CN":"需要拼接的视频，用英文逗号按拼接顺序分隔"}
        self.video_ids = video_ids
        # {"en":"Output video file name", "zh_CN":"输出视频文件名"}
        self.filename = filename
        # {"en":"ID of the directory to be stored", "zh_CN":"拼接需要存储的目录ID"}
        self.dir_id = dir_id
        # {"en":"The completion address used to receive callback information", "zh_CN":"用于接收回调信息的完成地址"}
        self.notify_url = notify_url
        # {"en":"Output format
        # Value range:
        # flv
        # mp4
        # m3u8
        # Default flv", "zh_CN":"输出格式
        # 取值范围 ：
        # flv
        # mp4
        # m3u8
        # 默认flv"}
        self.suffix = suffix

    def validate(self):
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.video_ids, 'video_ids')
        self.validate_required(self.filename, 'filename')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.video_ids is not None:
            result['videoIds'] = self.video_ids
        if self.filename is not None:
            result['filename'] = self.filename
        if self.dir_id is not None:
            result['dirId'] = self.dir_id
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.suffix is not None:
            result['suffix'] = self.suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('videoIds') is not None:
            self.video_ids = m.get('videoIds')
        if m.get('filename') is not None:
            self.filename = m.get('filename')
        if m.get('dirId') is not None:
            self.dir_id = m.get('dirId')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        return self


class VideoConcatResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"200 success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"返回消息"}
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


class VideoConcatPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VideoConcatQueryRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
    ):
        # {"en":"Customer video cut task code, up to 32 bits", "zh_CN":"客户视频剪切任务编码，32位以下"}
        self.trans_no = trans_no

    def validate(self):
        self.validate_required(self.trans_no, 'trans_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        return self


class VideoConcatQueryVideoResolutions(TeaModel):
    def __init__(
        self,
        clarity: int = None,
        server_type: int = None,
        height: int = None,
        width: int = None,
        file_size: int = None,
    ):
        # {"en":"Clarity. Value range:
        # 1(original painting)
        # 2(fluency)
        # 3(standard definition)
        # 4(HD)
        # 5(Super clear)
        # -99(record file)", "zh_CN":"清晰度。取值范围 ：
        # 1(原画)
        # 2(流畅)
        # 3(标清)
        # 4(高清)
        # 5(超清)
        # -99(录制文件)"}
        self.clarity = clarity
        # {"en":"Terminal type. Value range:
        # 0(PC)
        # 1(original video)", "zh_CN":"	终端类型。取值范围 ：
        # 0(PC)
        # 1(原视频)"}
        self.server_type = server_type
        # {"en":"height", "zh_CN":"高度"}
        self.height = height
        # {"en":"width", "zh_CN":"宽度"}
        self.width = width
        # {"en":"fileSize", "zh_CN":"文件大小(单位为bit)"}
        self.file_size = file_size

    def validate(self):
        self.validate_required(self.clarity, 'clarity')
        self.validate_required(self.server_type, 'server_type')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.file_size, 'file_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.server_type is not None:
            result['serverType'] = self.server_type
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('serverType') is not None:
            self.server_type = m.get('serverType')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class VideoConcatQueryVideoInfo(TeaModel):
    def __init__(
        self,
        video_name: str = None,
        video_id: str = None,
        encrypt: int = None,
        video_size: str = None,
        video_duration: str = None,
        upload_time: str = None,
        update_time: str = None,
        video_description: str = None,
        video_classification: str = None,
        image_url: str = None,
        publish_domain: str = None,
        player_name: str = None,
        player_id: str = None,
        video_state: int = None,
        transcode_state: int = None,
        video_source_code: int = None,
        video_resolutions: List[VideoConcatQueryVideoResolutions] = None,
    ):
        # {"en":"videoName", "zh_CN":"视频名称"}
        self.video_name = video_name
        # {"en":"videoId", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"Whether to encrypt transcoding files
        # Value range:
        # 0(unencrypted)
        # 1(encryption)", "zh_CN":"是否加密转码文件
        # 取值范围 ：
        # 0(不加密)
        # 1(加密)"}
        self.encrypt = encrypt
        # {"en":"The space occupied by the video, and the total space used by the video and its transcoding", "zh_CN":"视频占用空间大小，视频及其转码后视频的总空间使用量"}
        self.video_size = video_size
        # {"en":"videoDuration", "zh_CN":"视频时长"}
        self.video_duration = video_duration
        # {"en":"uploadTime", "zh_CN":"视频上传时间"}
        self.upload_time = upload_time
        # {"en":"updateTime", "zh_CN":"视频修改时间"}
        self.update_time = update_time
        # {"en":"videoDescription", "zh_CN":"视频描述"}
        self.video_description = video_description
        # {"en":"videoClassification", "zh_CN":"视频分类"}
        self.video_classification = video_classification
        # {"en":"imageUrl", "zh_CN":"视频封面URL"}
        self.image_url = image_url
        # {"en":"publishDomain", "zh_CN":"视频的发布域名"}
        self.publish_domain = publish_domain
        # {"en":"playerName", "zh_CN":"视频使用的播放器名称"}
        self.player_name = player_name
        # {"en":"playerId", "zh_CN":"视频使用的播放器ID"}
        self.player_id = player_id
        # {"en":"videoState", "zh_CN":"视频状态
        # 取值范围：
        # 0(正常)
        # 1(屏蔽)"}
        self.video_state = video_state
        # {"en":"If authorized play is not enabled, the video transcoding status ranges from:
        # 1(transcoded)
        # 2(no transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # Value range of transcoding status when the Authorized Play (video encryption) function is enabled:
        # 1(encrypted transcoding)
        # 2(non-encrypted transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # 5(no transcoding)", "zh_CN":"未开启授权播放，视频的转码状态的取值范围 ：
        # 1(已转码)
        # 2(未转码)
        # 3(转码中)
        # 4(转码失败)
        # 开启授权播放（视频加密）功能时的转码状态的取值范围 ：
        # 1(已加密转码)
        # 2(非加密转码)
        # 3(转码中)
        # 4(转码失败)
        # 5(未转码)"}
        self.transcode_state = transcode_state
        # {"en":"Video source
        # Value range:
        # 0(other)
        # 1(Upload)
        # 2 (Live streaming to recording)
        # 3 (Video pull)
        # 4 (Video cutting)
        # 5 (Video Stitching)
        # 6 (edge pull recording)
        # 10 (universal version of live broadcasting to recording)
        # 11 (Uploading SDK)
        # 12 (Upload tool)", "zh_CN":"	视频来源
        # 取值范围：
        # 0(其他)
        # 1(上传)
        # 2（直播转录制）
        # 3（视频拉取）
        # 4（视频剪切）
        # 5（视频拼接）
        # 6（边缘拉流录制）
        # 10（通用版直播转录制）
        # 11（上传SDK）
        # 12（上传工具）"}
        self.video_source_code = video_source_code
        # {"en":"Video resolution and other information", "zh_CN":"视频分辨率等信息"}
        self.video_resolutions = video_resolutions

    def validate(self):
        self.validate_required(self.video_name, 'video_name')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.encrypt, 'encrypt')
        self.validate_required(self.video_size, 'video_size')
        self.validate_required(self.video_duration, 'video_duration')
        self.validate_required(self.upload_time, 'upload_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.video_description, 'video_description')
        self.validate_required(self.video_classification, 'video_classification')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.publish_domain, 'publish_domain')
        self.validate_required(self.player_name, 'player_name')
        self.validate_required(self.player_id, 'player_id')
        self.validate_required(self.video_state, 'video_state')
        self.validate_required(self.transcode_state, 'transcode_state')
        self.validate_required(self.video_source_code, 'video_source_code')
        self.validate_required(self.video_resolutions, 'video_resolutions')
        if self.video_resolutions:
            for k in self.video_resolutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.encrypt is not None:
            result['encrypt'] = self.encrypt
        if self.video_size is not None:
            result['videoSize'] = self.video_size
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.video_description is not None:
            result['videoDescription'] = self.video_description
        if self.video_classification is not None:
            result['videoClassification'] = self.video_classification
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        if self.player_name is not None:
            result['playerName'] = self.player_name
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.video_state is not None:
            result['videoState'] = self.video_state
        if self.transcode_state is not None:
            result['transcodeState'] = self.transcode_state
        if self.video_source_code is not None:
            result['videoSourceCode'] = self.video_source_code
        if self.video_resolutions is not None:
            result['videoResolutions'] = []
            for k in self.video_resolutions:
                result['videoResolutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('encrypt') is not None:
            self.encrypt = m.get('encrypt')
        if m.get('videoSize') is not None:
            self.video_size = m.get('videoSize')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('videoDescription') is not None:
            self.video_description = m.get('videoDescription')
        if m.get('videoClassification') is not None:
            self.video_classification = m.get('videoClassification')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        if m.get('playerName') is not None:
            self.player_name = m.get('playerName')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('videoState') is not None:
            self.video_state = m.get('videoState')
        if m.get('transcodeState') is not None:
            self.transcode_state = m.get('transcodeState')
        if m.get('videoSourceCode') is not None:
            self.video_source_code = m.get('videoSourceCode')
        if m.get('videoResolutions') is not None:
            self.video_resolutions = []
            for k in m.get('videoResolutions'):
                temp_model = VideoConcatQueryVideoResolutions()
                self.video_resolutions.append(temp_model.from_map(k))
        return self


class VideoConcatQueryData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        trans_no: str = None,
        status: int = None,
        video_info: VideoConcatQueryVideoInfo = None,
    ):
        # {"en":"taskId", "zh_CN":"任务ID。"}
        self.task_id = task_id
        # {"en":"transNo", "zh_CN":"业务ID"}
        self.trans_no = trans_no
        # {"en":"status", "zh_CN":"状态
        # 取值范围 ：
        # 1(处理中)
        # 2(成功)
        # 3(失败)"}
        self.status = status
        self.video_info = video_info

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.status, 'status')
        self.validate_required(self.video_info, 'video_info')
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.status is not None:
            result['status'] = self.status
        if self.video_info is not None:
            result['videoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('videoInfo') is not None:
            temp_model = VideoConcatQueryVideoInfo()
            self.video_info = temp_model.from_map(m['videoInfo'])
        return self


class VideoConcatQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: VideoConcatQueryData = None,
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
            temp_model = VideoConcatQueryData()
            self.data = temp_model.from_map(m['data'])
        return self


class VideoConcatQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoConcatQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateClearAdTaskRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        clear_video_ad: bool = None,
        clear_watermark_ad: bool = None,
        clear_text_ad: bool = None,
        video_ad_types: str = None,
        video_ad_level: int = None,
        watermark_ad_type: int = None,
        text_ad_type: int = None,
        notify_url: str = None,
    ):
        # {"en":"videoId", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"Whether to clear video ads. Choose at least one type of AD to remove. If not, the default value is false.", "zh_CN":"是否清除视频广告。至少选择一种要清除的广告。如果不填，默认为false。"}
        self.clear_video_ad = clear_video_ad
        # {"en":"Whether to clear watermark ads. Choose at least one type of AD to remove. If not, the default value is false.", "zh_CN":"是否清除水印广告。至少选择一种要清除的广告。如果不填，默认为false。"}
        self.clear_watermark_ad = clear_watermark_ad
        # {"en":"Whether to clear text ads. Choose at least one type of AD to remove. If not, the default value is false.", "zh_CN":"是否清除文字广告。至少选择一种要清除的广告。如果不填，默认为false。"}
        self.clear_text_ad = clear_text_ad
        # {"en":"Type of video ads processed", "zh_CN":"处理的视频广告类型,取值范围:
        # “0”(清除片头广告)
        # “0,1,2”(清除全部广告，包含片头+片中+片尾)
        # 目前只支持“0”和“0,1,2”两种模式，不填则默认为“0,1,2”清楚全部广告"}
        self.video_ad_types = video_ad_types
        # {"en":"Video AD clearance level, value range:
        # 0(default clearance level, may cause missing deletion)
        # 1(Strong clear level, may cause incorrect deletion)
        # If this parameter is not specified, the default value is 0.", "zh_CN":"视频广告清除等级,取值范围:
        # 0(默认清除等级，可能造成漏删)
        # 1(强力清除等级，可能造成误删)
        # 不填则默认为0。"}
        self.video_ad_level = video_ad_level
        # {"en":"Processing watermark advertising types, value range:
        # 0(stretch blur)
        # 1(Gaussian blur)
        # The default value is 0.
        # After api-1.240.5 (inclusive), the watermarkAdType and textAdType parameters must be consistent. If they are inconsistent, the system automatically uses 0 by default", "zh_CN":"处理水印广告类型,取值范围:
        # 0(拉伸模糊)
        # 1(高斯模糊)
        # 不填默认为0。
        # 版本api-1.240.5（含）之后，watermarkAdType和textAdType两个参数内容必须一致，若不一致系统自动使用默认0 "}
        self.watermark_ad_type = watermark_ad_type
        # {"en":"Clear handling of running horse lamp text advertising", "zh_CN":"处理清楚跑马灯文字广告,取值范围:
        # 0(拉伸模糊)
        # 1(高斯模糊)
        # 不填默认为0。"}
        self.text_ad_type = text_ad_type
        # {"en":"notifyUrl", "zh_CN":"通知地址，必须以 http://或https:// 开头。长度不能超过255个字符。通知内容详见 [AI清除广告-任务完成通知](https://www.wangsu.com/document/cate/70/17168)"}
        self.notify_url = notify_url

    def validate(self):
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.clear_video_ad is not None:
            result['clearVideoAd'] = self.clear_video_ad
        if self.clear_watermark_ad is not None:
            result['clearWatermarkAd'] = self.clear_watermark_ad
        if self.clear_text_ad is not None:
            result['clearTextAd'] = self.clear_text_ad
        if self.video_ad_types is not None:
            result['videoAdTypes'] = self.video_ad_types
        if self.video_ad_level is not None:
            result['videoAdLevel'] = self.video_ad_level
        if self.watermark_ad_type is not None:
            result['watermarkAdType'] = self.watermark_ad_type
        if self.text_ad_type is not None:
            result['textAdType'] = self.text_ad_type
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('clearVideoAd') is not None:
            self.clear_video_ad = m.get('clearVideoAd')
        if m.get('clearWatermarkAd') is not None:
            self.clear_watermark_ad = m.get('clearWatermarkAd')
        if m.get('clearTextAd') is not None:
            self.clear_text_ad = m.get('clearTextAd')
        if m.get('videoAdTypes') is not None:
            self.video_ad_types = m.get('videoAdTypes')
        if m.get('videoAdLevel') is not None:
            self.video_ad_level = m.get('videoAdLevel')
        if m.get('watermarkAdType') is not None:
            self.watermark_ad_type = m.get('watermarkAdType')
        if m.get('textAdType') is not None:
            self.text_ad_type = m.get('textAdType')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        return self


class CreateClearAdTaskData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # {"en":"taskId", "zh_CN":"AI清除广告任务ID"}
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


class CreateClearAdTaskResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CreateClearAdTaskData = None,
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
            temp_model = CreateClearAdTaskData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateClearAdTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateClearAdTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateClearAdTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateClearAdTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class TransCodeRequest(TeaModel):
    def __init__(
        self,
        video_ids: str = None,
        water_mark_template_name: str = None,
        trans_code_template_name: str = None,
        watermark_template_id: str = None,
        trans_code_template_id: str = None,
        subtitle_id: str = None,
        subtitle: str = None,
    ):
        # {"en":"Please provide the ID of the video(s) you want to view. If there are multiple videos, separate each ID with a comma ,", "zh_CN":"视频ID，多个视频通过“,“隔开；"}
        self.video_ids = video_ids
        # {"en":"By default, there is no watermark added to the video. However, you have the option to select a watermark template from our cloud-based management platform and add it to your video on-demand.", "zh_CN":"水印模板名，默认不添加水印，可选择云点播管理平台中的模板为视频添加水印；"}
        self.water_mark_template_name = water_mark_template_name
        # {"en":"The transcoding combination template name, by default, is set to the template provided by the cloud VOD management platform.", "zh_CN":"转码组合模板名，默认使用云点播管理平台设置的默认模板，"}
        self.trans_code_template_name = trans_code_template_name
        # {"en":"The Watermark template Id is optional and by default no watermark is added to the video. However, you can conveniently choose a template from the cloud-based management platform to easily add a watermark to your videos", "zh_CN":"水印模板Id，默认不添加水印，可选择云点播管理平台中的模板为视频添加水印；"}
        self.watermark_template_id = watermark_template_id
        # {"en":"Transcoding combination template ID, the default template set by the cloud on-demand management platform is used by default", "zh_CN":"转码组合模板ID，默认使用云点播管理平台设置的默认模板"}
        self.trans_code_template_id = trans_code_template_id
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
        self.validate_required(self.video_ids, 'video_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_ids is not None:
            result['videoIds'] = self.video_ids
        if self.water_mark_template_name is not None:
            result['waterMarkTemplateName'] = self.water_mark_template_name
        if self.trans_code_template_name is not None:
            result['transCodeTemplateName'] = self.trans_code_template_name
        if self.watermark_template_id is not None:
            result['watermarkTemplateId'] = self.watermark_template_id
        if self.trans_code_template_id is not None:
            result['transCodeTemplateId'] = self.trans_code_template_id
        if self.subtitle_id is not None:
            result['subtitleId'] = self.subtitle_id
        if self.subtitle is not None:
            result['subtitle'] = self.subtitle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoIds') is not None:
            self.video_ids = m.get('videoIds')
        if m.get('waterMarkTemplateName') is not None:
            self.water_mark_template_name = m.get('waterMarkTemplateName')
        if m.get('transCodeTemplateName') is not None:
            self.trans_code_template_name = m.get('transCodeTemplateName')
        if m.get('watermarkTemplateId') is not None:
            self.watermark_template_id = m.get('watermarkTemplateId')
        if m.get('transCodeTemplateId') is not None:
            self.trans_code_template_id = m.get('transCodeTemplateId')
        if m.get('subtitleId') is not None:
            self.subtitle_id = m.get('subtitleId')
        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')
        return self


class TransCodeResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"data", "zh_CN":"返回数据"}
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


class TransCodePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TransCodeParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TransCodeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TransCodeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VideoClipQueryRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
    ):
        # {"en":"Customer video cut task code, up to 32 bits", "zh_CN":"客户视频剪切任务编码，32位以下"}
        self.trans_no = trans_no

    def validate(self):
        self.validate_required(self.trans_no, 'trans_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        return self


class VideoClipQueryVideoResolution(TeaModel):
    def __init__(
        self,
        clarity: int = None,
        server_type: int = None,
        height: int = None,
        width: int = None,
        file_size: int = None,
    ):
        # {"en":"Clarity. Value range:
        # 1(original painting)
        # 2(fluency)
        # 3(standard definition)
        # 4(HD)
        # 5(Super clear)
        # -99(record file)", "zh_CN":"清晰度。取值范围 ：
        # 1(原画)
        # 2(流畅)
        # 3(标清)
        # 4(高清)
        # 5(超清)
        # -99(录制文件)"}
        self.clarity = clarity
        # {"en":"Terminal type. Value range:
        # 0(PC)
        # 1(original video)", "zh_CN":"	终端类型。取值范围 ：
        # 0(PC)
        # 1(原视频)"}
        self.server_type = server_type
        # {"en":"height", "zh_CN":"高度"}
        self.height = height
        # {"en":"width", "zh_CN":"宽度"}
        self.width = width
        # {"en":"fileSize", "zh_CN":"文件大小(单位为bit)"}
        self.file_size = file_size

    def validate(self):
        self.validate_required(self.clarity, 'clarity')
        self.validate_required(self.server_type, 'server_type')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.file_size, 'file_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.server_type is not None:
            result['serverType'] = self.server_type
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('serverType') is not None:
            self.server_type = m.get('serverType')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class VideoClipQueryVideoInfo(TeaModel):
    def __init__(
        self,
        video_name: str = None,
        video_id: str = None,
        encrypt: int = None,
        video_size: str = None,
        video_duration: str = None,
        upload_time: str = None,
        update_time: str = None,
        video_description: str = None,
        video_classification: str = None,
        image_url: str = None,
        publish_domain: str = None,
        player_name: str = None,
        player_id: str = None,
        video_state: int = None,
        transcode_state: int = None,
        video_source_code: int = None,
        video_resolutions: List[VideoClipQueryVideoResolution] = None,
    ):
        # {"en":"videoName", "zh_CN":"视频名称"}
        self.video_name = video_name
        # {"en":"videoId", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"Whether to encrypt transcoding files
        # Value range:
        # 0(unencrypted)
        # 1(encryption)", "zh_CN":"是否加密转码文件
        # 取值范围 ：
        # 0(不加密)
        # 1(加密)"}
        self.encrypt = encrypt
        # {"en":"The space occupied by the video, and the total space used by the video and its transcoding", "zh_CN":"视频占用空间大小，视频及其转码后视频的总空间使用量"}
        self.video_size = video_size
        # {"en":"videoDuration", "zh_CN":"视频时长"}
        self.video_duration = video_duration
        # {"en":"uploadTime", "zh_CN":"视频上传时间"}
        self.upload_time = upload_time
        # {"en":"updateTime", "zh_CN":"视频修改时间"}
        self.update_time = update_time
        # {"en":"videoDescription", "zh_CN":"视频描述"}
        self.video_description = video_description
        # {"en":"videoClassification", "zh_CN":"视频分类"}
        self.video_classification = video_classification
        # {"en":"Video cover URL", "zh_CN":"视频封面URL"}
        self.image_url = image_url
        # {"en":"publishDomain", "zh_CN":"视频的发布域名"}
        self.publish_domain = publish_domain
        # {"en":"playerName", "zh_CN":"视频使用的播放器名称"}
        self.player_name = player_name
        # {"en":"playerId", "zh_CN":"视频使用的播放器ID"}
        self.player_id = player_id
        # {"en":"Video state
        # Value range:
        # 0(normal)
        # 1(mask)", "zh_CN":"视频状态
        # 取值范围：
        # 0(正常)
        # 1(屏蔽)"}
        self.video_state = video_state
        # {"en":"If authorized play is not enabled, the video transcoding status ranges from:
        # 1(transcoded)
        # 2(no transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # Value range of transcoding status when the Authorized Play (video encryption) function is enabled:
        # 1(encrypted transcoding)
        # 2(non-encrypted transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # 5(no transcoding)", "zh_CN":"未开启授权播放，视频的转码状态的取值范围 ：
        # 1(已转码)
        # 2(未转码)
        # 3(转码中)
        # 4(转码失败)
        # 开启授权播放（视频加密）功能时的转码状态的取值范围 ：
        # 1(已加密转码)
        # 2(非加密转码)
        # 3(转码中)
        # 4(转码失败)
        # 5(未转码)"}
        self.transcode_state = transcode_state
        # {"en":"Video source
        # Value range:
        # 0(other)
        # 1(Upload)
        # 2 (Live streaming to recording)
        # 3 (Video pull)
        # 4 (Video cutting)
        # 5 (Video Stitching)
        # 6 (edge pull recording)
        # 10 (universal version of live broadcasting to recording)
        # 11 (Uploading SDK)
        # 12 (Upload tool)", "zh_CN":"	视频来源
        # 取值范围：
        # 0(其他)
        # 1(上传)
        # 2（直播转录制）
        # 3（视频拉取）
        # 4（视频剪切）
        # 5（视频拼接）
        # 6（边缘拉流录制）
        # 10（通用版直播转录制）
        # 11（上传SDK）
        # 12（上传工具）"}
        self.video_source_code = video_source_code
        # {"en":"Video resolution and other information", "zh_CN":"视频分辨率等信息"}
        self.video_resolutions = video_resolutions

    def validate(self):
        self.validate_required(self.video_name, 'video_name')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.encrypt, 'encrypt')
        self.validate_required(self.video_size, 'video_size')
        self.validate_required(self.video_duration, 'video_duration')
        self.validate_required(self.upload_time, 'upload_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.video_description, 'video_description')
        self.validate_required(self.video_classification, 'video_classification')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.publish_domain, 'publish_domain')
        self.validate_required(self.player_name, 'player_name')
        self.validate_required(self.player_id, 'player_id')
        self.validate_required(self.video_state, 'video_state')
        self.validate_required(self.transcode_state, 'transcode_state')
        self.validate_required(self.video_source_code, 'video_source_code')
        self.validate_required(self.video_resolutions, 'video_resolutions')
        if self.video_resolutions:
            for k in self.video_resolutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.encrypt is not None:
            result['encrypt'] = self.encrypt
        if self.video_size is not None:
            result['videoSize'] = self.video_size
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.video_description is not None:
            result['videoDescription'] = self.video_description
        if self.video_classification is not None:
            result['videoClassification'] = self.video_classification
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        if self.player_name is not None:
            result['playerName'] = self.player_name
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.video_state is not None:
            result['videoState'] = self.video_state
        if self.transcode_state is not None:
            result['transcodeState'] = self.transcode_state
        if self.video_source_code is not None:
            result['videoSourceCode'] = self.video_source_code
        if self.video_resolutions is not None:
            result['videoResolutions'] = []
            for k in self.video_resolutions:
                result['videoResolutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('encrypt') is not None:
            self.encrypt = m.get('encrypt')
        if m.get('videoSize') is not None:
            self.video_size = m.get('videoSize')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('videoDescription') is not None:
            self.video_description = m.get('videoDescription')
        if m.get('videoClassification') is not None:
            self.video_classification = m.get('videoClassification')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        if m.get('playerName') is not None:
            self.player_name = m.get('playerName')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('videoState') is not None:
            self.video_state = m.get('videoState')
        if m.get('transcodeState') is not None:
            self.transcode_state = m.get('transcodeState')
        if m.get('videoSourceCode') is not None:
            self.video_source_code = m.get('videoSourceCode')
        if m.get('videoResolutions') is not None:
            self.video_resolutions = []
            for k in m.get('videoResolutions'):
                temp_model = VideoClipQueryVideoResolution()
                self.video_resolutions.append(temp_model.from_map(k))
        return self


class VideoClipQueryData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        trans_no: str = None,
        status: int = None,
        video_info: VideoClipQueryVideoInfo = None,
    ):
        # {"en":"taskId", "zh_CN":"任务ID。"}
        self.task_id = task_id
        # {"en":"transNo", "zh_CN":"业务ID"}
        self.trans_no = trans_no
        # {"en":"
        # state
        # Value range:
        # 1(in process)
        # 2(Successful)
        # 3(Failure)", "zh_CN":"状态
        # 取值范围 ：
        # 1(处理中)
        # 2(成功)
        # 3(失败)"}
        self.status = status
        self.video_info = video_info

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.status, 'status')
        self.validate_required(self.video_info, 'video_info')
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.status is not None:
            result['status'] = self.status
        if self.video_info is not None:
            result['videoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('videoInfo') is not None:
            temp_model = VideoClipQueryVideoInfo()
            self.video_info = temp_model.from_map(m['videoInfo'])
        return self


class VideoClipQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: VideoClipQueryData = None,
    ):
        # {"en":"code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"message", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"data", "zh_CN":"返回数据"}
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
            temp_model = VideoClipQueryData()
            self.data = temp_model.from_map(m['data'])
        return self


class VideoClipQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoClipQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




