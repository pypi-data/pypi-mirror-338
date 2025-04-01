# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class LiveVideoConcatRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        trans_no: str = None,
        start: int = None,
        end: int = None,
        fname: str = None,
        suffix: str = None,
        notify: str = None,
        enable_video_transcode: int = None,
    ):
        # {"en":"Channel pull id", "zh_CN":"频道拉流id"}
        self.pull_id = pull_id
        # {"en":"The service ID must be unique. You are advised to use a 32-bit UUID and the value can be a string of up to 32 characters", "zh_CN":"业务ID，需用户自己控制唯一性，建议使用32位UUID，并且最长为32位字符串"}
        self.trans_no = trans_no
        # {"en":"Start time, unix time stamp. Default is the first broadcast start time", "zh_CN":"开始时间，unix时间戳，默认为第一次直播开始时间"}
        self.start = start
        # {"en":"End time, unix timestamp, default current time. End time Future time is prohibited", "zh_CN":"结束时间，unix时间戳，默认当前时间。结束时间禁止填未来时间"}
        self.end = end
        # {"en":"File name. If it is empty, the system automatically generates a file name (stream name _ start time _ end time).", "zh_CN":"文件名。若为空则系统自动生成一个文件名（流名_开始时间_结束时间）"}
        self.fname = fname
        # {"en":"The optional file format is:
        # 
        # flv: FLV format, which combines multiple recorded videos into a single flv file. Default format
        # 
        # mp4: MP4 format, which combines multiple recorded videos into a single mp4 file.
        # 
        # Format not supported:
        # 
        # m3u8: indicates the HLS format", "zh_CN":"文件格式，可选文件格式为：
        # 
        # flv：FLV格式，将多个录制视频合并成单个flv文件。默认格式
        # 
        # mp4：MP4格式，将多个录制视频合并成单个mp4文件。
        # 
        # 不支持格式：
        # 
        # m3u8：HLS格式"}
        self.suffix = suffix
        # {"en":"Callback address. When the task is complete, the callback address is not specified. If the address is not specified, the callback is not performed", "zh_CN":"回调地址。完成任务后回调通知地址，不指定表示不做回调"}
        self.notify = notify
        # {"en":"Start forced transcoding, 1: start. 0: Do not start, the default is 0", "zh_CN":"启动强制转码，1:启动。0:不启动 默认是0"}
        self.enable_video_transcode = enable_video_transcode

    def validate(self):
        self.validate_required(self.pull_id, 'pull_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.fname is not None:
            result['fname'] = self.fname
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.notify is not None:
            result['notify'] = self.notify
        if self.enable_video_transcode is not None:
            result['enableVideoTranscode'] = self.enable_video_transcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('fname') is not None:
            self.fname = m.get('fname')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('notify') is not None:
            self.notify = m.get('notify')
        if m.get('enableVideoTranscode') is not None:
            self.enable_video_transcode = m.get('enableVideoTranscode')
        return self


class LiveVideoConcatData(TeaModel):
    def __init__(
        self,
        tran_no: str = None,
    ):
        # {"en":"transNo", "zh_CN":"业务ID"}
        self.tran_no = tran_no

    def validate(self):
        self.validate_required(self.tran_no, 'tran_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tran_no is not None:
            result['tranNo'] = self.tran_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tranNo') is not None:
            self.tran_no = m.get('tranNo')
        return self


class LiveVideoConcatResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: LiveVideoConcatData = None,
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
            temp_model = LiveVideoConcatData()
            self.data = temp_model.from_map(m['data'])
        return self


class LiveVideoConcatPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetRecordTaskListQueryRequest(TeaModel):
    def __init__(
        self,
        pull_id: str = None,
        trans_no: str = None,
        status: int = None,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Channel pull ID. Multiple streaming IDs are separated by ,; if not filled in, recording tasks for all channels will be returned by default", "zh_CN":"频道拉流ID。多个拉流id用,隔开；未填写默认返回所有频道的录制任务"}
        self.pull_id = pull_id
        # {"en":"Business ID needs to be uniquely controlled by the user. Use , to separate multiple ones.", "zh_CN":"业务ID，需用户自己控制唯一性。多个用,隔开。"}
        self.trans_no = trans_no
        # {"en":"The status of the recording task. If not filled in, all will be queried. 0 has not started, 1 has started, 2 has ended normally, and 3 has terminated.", "zh_CN":"录制任务的状态， 不填则查询所有，0未开始，1已开始，2正常结束，3终止"}
        self.status = status
        # {"en":"List order, value range: <br>
        # 0(in descending order by creation time)<br>
        # 1(in ascending order of creation time) The default value is 0", "zh_CN":"列表排列顺序，取值范围 ：<br>
        # 0(按创建时间降序排列)<br>
        # 1(按创建时间升序排列)默认为0"}
        self.list_order = list_order
        # {"en":"The page number in the task paging list starts from 1; the default is 1", "zh_CN":"task分页列表中第几页，从1开始取值；默认1"}
        self.page_index = page_index
        # {"en":"The average number of channels per page, the default is 10, the value is between 1-50.", "zh_CN":"平均每页频道数量，默认为10，取值在1-50之间"}
        self.page_size = page_size
        # {"en":"Query starting time, the time format is, 2016-01-01 12:00:00; used to query recording tasks according to the creation time period; if not filled in, query all queries all", "zh_CN":"查询起始时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询录制任务；如果不填则查询所有查询所有"}
        self.start_time = start_time
        # {"en":"Query deadline, the time format is, 2016-01-01 12:00:00; used to query recording tasks according to the creation time period, which is less than the current query time;. If not filled in, query all query all", "zh_CN":"查询截止时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询录制任务，小于当前查询时间；。如果不填则查询所有查询所有"}
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.status is not None:
            result['status'] = self.status
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class GetRecordTaskListQueryRecordTaskQuery(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        pull_id: str = None,
        status: int = None,
        trans_no: str = None,
        file_type: str = None,
        is_concat: bool = None,
        start_time: str = None,
        end_time: str = None,
    ):
        # {"en":"Task Id", "zh_CN":"直播录制任务ID"}
        self.task_id = task_id
        # {"en":"Channel streaming ID", "zh_CN":"频道拉流ID"}
        self.pull_id = pull_id
        # {"en":"The status of the recording task, 0 has not started, 1 has started, 2 has ended normally, and 3 has terminated", "zh_CN":"录制任务的状态， 0未开始，1已开始，2正常结束，3终止"}
        self.status = status
        # {"en":"Custom task number passed in by the customer", "zh_CN":"客户传入的自定义任务编号"}
        self.trans_no = trans_no
        # {"en":"Recording file format", "zh_CN":"录制文件的格式"}
        self.file_type = file_type
        # {"en":"Whether to merge into one video", "zh_CN":"是否合并成一个视频"}
        self.is_concat = is_concat
        # {"en":"Task start time", "zh_CN":"任务开始时间"}
        self.start_time = start_time
        # {"en":"Task end time", "zh_CN":"任务结束时间"}
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.pull_id, 'pull_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.trans_no, 'trans_no')
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.is_concat, 'is_concat')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

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
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.is_concat is not None:
            result['isConcat'] = self.is_concat
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('isConcat') is not None:
            self.is_concat = m.get('isConcat')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self


class GetRecordTaskListQueryRecordTask(TeaModel):
    def __init__(
        self,
        record_task_total: int = None,
        record_task_query_response_list: List[GetRecordTaskListQueryRecordTaskQuery] = None,
    ):
        # {"en":"The number of records of the recording task list information currently returned. Note that the number of records returned here is only the number of records on the current page.", "zh_CN":"当前返回的录制任务列表信息的记录数，注意这里返回的记录数只是当前页的记录数"}
        self.record_task_total = record_task_total
        # {"en":"Recording task list", "zh_CN":"录制任务列表"}
        self.record_task_query_response_list = record_task_query_response_list

    def validate(self):
        self.validate_required(self.record_task_total, 'record_task_total')
        self.validate_required(self.record_task_query_response_list, 'record_task_query_response_list')
        if self.record_task_query_response_list:
            for k in self.record_task_query_response_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_task_total is not None:
            result['recordTaskTotal'] = self.record_task_total
        if self.record_task_query_response_list is not None:
            result['recordTaskQueryResponseList'] = []
            for k in self.record_task_query_response_list:
                result['recordTaskQueryResponseList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordTaskTotal') is not None:
            self.record_task_total = m.get('recordTaskTotal')
        if m.get('recordTaskQueryResponseList') is not None:
            self.record_task_query_response_list = []
            for k in m.get('recordTaskQueryResponseList'):
                temp_model = GetRecordTaskListQueryRecordTaskQuery()
                self.record_task_query_response_list.append(temp_model.from_map(k))
        return self


class GetRecordTaskListQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetRecordTaskListQueryRecordTask = None,
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
            temp_model = GetRecordTaskListQueryRecordTask()
            self.data = temp_model.from_map(m['data'])
        return self


class GetRecordTaskListQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordTaskListQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordTaskListQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetRecordTaskListQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class LiveVideoConcatQueryRequest(TeaModel):
    def __init__(
        self,
        trans_no: str = None,
        pull_id: str = None,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Service ID, service ID and channel pull id cannot be empty at the same time", "zh_CN":"业务ID，业务ID和频道拉流id不可以同时为空"}
        self.trans_no = trans_no
        # {"en":"Channel pull id, service ID, and channel pull id cannot be empty at the same time", "zh_CN":"频道拉流id，业务ID和频道拉流id不可以同时为空"}
        self.pull_id = pull_id
        # {"en":"List order, value range:
        # 0(in descending order of creation time)
        # 1(in ascending order of creation time)
        # Default is 0", "zh_CN":"列表排列顺序，取值范围 ：
        # 0(按创建时间降序排列)
        # 1(按创建时间升序排列)
        # 默认为0"}
        self.list_order = list_order
        # {"en":"On the page of the scenario list, the value starts from 1. The default value is 1. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"取场景列表第几页，从1开始取值,默认为1。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_index = page_index
        # {"en":"Average Number of scenarios per page. The value ranges from 1 to 50. The default value is 10. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"平均每页场景数量，取值范围1-50，默认为10。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trans_no is not None:
            result['transNo'] = self.trans_no
        if self.pull_id is not None:
            result['pullId'] = self.pull_id
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transNo') is not None:
            self.trans_no = m.get('transNo')
        if m.get('pullId') is not None:
            self.pull_id = m.get('pullId')
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class LiveVideoConcatQueryVideoResolutions(TeaModel):
    def __init__(
        self,
        clarity: int = None,
        server_type: int = None,
        height: int = None,
        width: int = None,
        file_size: int = None,
    ):
        # {"en":"Clarity. Value range: 1(original painting), 2(smooth), 3(standard definition), 4(HD), 5(ultra HD), -99(recorded file)", "zh_CN":"清晰度。取值范围 ：1(原画)，2(流畅)，3(标清)，4(高清)，5(超清)，-99(录制文件)"}
        self.clarity = clarity
        # {"en":"Terminal type. Value range: 0(PC), 1(original video)", "zh_CN":"终端类型。取值范围 ：0(PC)，1(原视频)"}
        self.server_type = server_type
        # {"en":"Height", "zh_CN":"高度"}
        self.height = height
        # {"en":"Width", "zh_CN":"宽度"}
        self.width = width
        # {"en":"File size(bit)", "zh_CN":"文件大小(单位为bit)"}
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


class LiveVideoConcatQueryVideoInfo(TeaModel):
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
        video_state: str = None,
        transcode_state: str = None,
        video_source_code: int = None,
        video_resolutions: List[LiveVideoConcatQueryVideoResolutions] = None,
    ):
        # {"en":"Video name", "zh_CN":"视频名称"}
        self.video_name = video_name
        # {"en":"Video id", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"Whether to encrypt transcoding files
        # Value range: 0(unencrypted), 1(encrypted)", "zh_CN":"是否加密转码文件
        # 取值范围 ：0(不加密)，1(加密)"}
        self.encrypt = encrypt
        # {"en":"The space occupied by the video, and the total space used by the video and its transcoding", "zh_CN":"视频占用空间大小，视频及其转码后视频的总空间使用量"}
        self.video_size = video_size
        # {"en":"Video duration", "zh_CN":"视频时长"}
        self.video_duration = video_duration
        # {"en":"Video upload time", "zh_CN":"视频上传时间"}
        self.upload_time = upload_time
        # {"en":"Video modification time", "zh_CN":"视频修改时间"}
        self.update_time = update_time
        # {"en":"Video description", "zh_CN":"视频描述"}
        self.video_description = video_description
        # {"en":"Video classification", "zh_CN":"视频分类"}
        self.video_classification = video_classification
        # {"en":"Video cover URL", "zh_CN":"视频封面URL"}
        self.image_url = image_url
        # {"en":"The domain name of the video", "zh_CN":"视频的发布域名"}
        self.publish_domain = publish_domain
        # {"en":"Name of the player used by the video", "zh_CN":"视频使用的播放器名称"}
        self.player_name = player_name
        # {"en":"The player ID used by the video", "zh_CN":"视频使用的播放器ID"}
        self.player_id = player_id
        # {"en":"Video state
        # Value range: 0(normal), 1(masked)", "zh_CN":"视频状态
        # 取值范围：0(正常)，1(屏蔽)"}
        self.video_state = video_state
        # {"en":"If authorized play is not enabled, the video transcoding status ranges from:
        # 1(transcoding), 2(not transcoding), 3(transcoding), 4(transcoding failed)
        # Value range of transcoding status when the Authorized Play (video encryption) function is enabled:
        # 1(encrypted transcoding), 2(unencrypted transcoding), 3(in transcoding), 4(transcoding failed), 5(not transcoding)", "zh_CN":"未开启授权播放，视频的转码状态的取值范围 ：
        # 1(已转码)，2(未转码)，3(转码中)，4(转码失败)
        # 开启授权播放（视频加密）功能时的转码状态的取值范围 ：
        # 1(已加密转码)，2(非加密转码)，3(转码中)，4(转码失败)，5(未转码)"}
        self.transcode_state = transcode_state
        # {"en":"Video source
        # Value range:
        # 0(other), 1(upload), 2 (live to record), 3 (video pull), 4 (video cut), 5 (video splicing), 6 (edge pull to record), 10 (general version live to record), 11 (upload SDK), 12 (upload tool)", "zh_CN":"视频来源
        # 取值范围：
        # 0(其他)，1(上传)，2（直播转录制），3（视频拉取），4（视频剪切），5（视频拼接），6（边缘拉流录制），10（通用版直播转录制），11（上传SDK），12（上传工具）"}
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
                temp_model = LiveVideoConcatQueryVideoResolutions()
                self.video_resolutions.append(temp_model.from_map(k))
        return self


class LiveVideoConcatQueryData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        tran_no: str = None,
        status: int = None,
        video_info: LiveVideoConcatQueryVideoInfo = None,
    ):
        # {"en":"Task id", "zh_CN":"任务ID"}
        self.task_id = task_id
        # {"en":"transNo", "zh_CN":"业务ID"}
        self.tran_no = tran_no
        # {"en":"status", "zh_CN":"状态
        # 取值范围：
        # 1：处理中
        # 2：成功
        # 3：失败"}
        self.status = status
        # {"en":"Video details; This is only returned if statu is equal to 2", "zh_CN":"视频详情；只要statu = 2的时候才会返回这个值"}
        self.video_info = video_info

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.tran_no, 'tran_no')
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
        if self.tran_no is not None:
            result['tranNo'] = self.tran_no
        if self.status is not None:
            result['status'] = self.status
        if self.video_info is not None:
            result['videoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('tranNo') is not None:
            self.tran_no = m.get('tranNo')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('videoInfo') is not None:
            temp_model = LiveVideoConcatQueryVideoInfo()
            self.video_info = temp_model.from_map(m['videoInfo'])
        return self


class LiveVideoConcatQueryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[LiveVideoConcatQueryData] = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
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
                temp_model = LiveVideoConcatQueryData()
                self.data.append(temp_model.from_map(k))
        return self


class LiveVideoConcatQueryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatQueryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatQueryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class LiveVideoConcatQueryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




