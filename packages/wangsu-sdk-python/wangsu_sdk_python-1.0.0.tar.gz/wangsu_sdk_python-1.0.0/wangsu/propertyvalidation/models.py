# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetPropertyValidationTaskPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a validation task", "zh_CN": "验证任务的id。"}
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


class GetPropertyValidationTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropertyValidationTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropertyValidationTaskRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropertyValidationTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropertyValidationTaskResponse(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        version: int = None,
        submission_time: str = None,
        status: str = None,
        status_details: str = None,
        api_request_id: str = None,
        finish_time: str = None,
        name: str = None,
        cache_version: str = None,
        webhook: str = None,
    ):
        # {"en" : "ID of the property being validated.", "zh_CN": "提交验证的加速项目的ID。"}
        self.property_id = property_id
        # {"en" : "Version of the property being validated.", "zh_CN": "提交验证的加速项目的版本号。"}
        self.version = version
        # {"en" : "An RFC 3339 format string indicating when the task was created. Example: '2019-11-12T03:06:16Z'", "zh_CN": "RFC 3339格式的日期，表示验证任务的提交时间。如：'2019-11-12T03:06:16Z'。"}
        self.submission_time = submission_time
        # {"en" : "Enum: waiting,failed,succeeded,in progress 
        # Indicates the validation task's status.", "zh_CN": "取值范围: waiting,failed,succeeded,in progress 
        # 验证任务的执行状态，包括等待中，进行中，验证成功，验证失败等状态。"}
        self.status = status
        # {"en" : "Further information about the task's current status.
        # ", "zh_CN": "当前任务状态的描述信息。"}
        self.status_details = status_details
        # {"en" : "Refers to the ID of the associated API request.", "zh_CN": "API请求的ID。"}
        self.api_request_id = api_request_id
        # {"en" : "An RFC 3339 date indicating when the task finished.", "zh_CN": "RFC 3339格式的日期，表示验证任务的完成时间。"}
        self.finish_time = finish_time
        # {"en" : "Name of the property validation task.", "zh_CN": "验证任务的名称。"}
        self.name = name
        # {"en" : "CDN cache version used when validating the property.", "zh_CN": "验证加速项目时使用的CDN Pro cache服务器的版本。"}
        self.cache_version = cache_version
        # {"en" : "ID of a webhook to call when the validation task completes.", "zh_CN": "验证任务完成时需要调用的webhook ID。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')
        self.validate_required(self.submission_time, 'submission_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_details, 'status_details')
        self.validate_required(self.api_request_id, 'api_request_id')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.cache_version, 'cache_version')
        self.validate_required(self.webhook, 'webhook')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_details is not None:
            result['statusDetails'] = self.status_details
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.name is not None:
            result['name'] = self.name
        if self.cache_version is not None:
            result['cacheVersion'] = self.cache_version
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDetails') is not None:
            self.status_details = m.get('statusDetails')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cacheVersion') is not None:
            self.cache_version = m.get('cacheVersion')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self






class GetListOfPropertyValidationTasksPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyValidationTasksParameters(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        property_version: str = None,
        status: str = None,
        limit: int = None,
        offset: int = None,
        search: str = None,
        sort_by: str = None,
        sort_order: str = None,
        startdate: str = None,
        enddate: str = None,
    ):
        # {"en" : "Return validation tasks associated only with a specific property ID.", "zh_CN": "指定加速项目ID，查询该加速项目相关的验证任务。"}
        self.property_id = property_id
        # {"en" : "Return validation tasks only for a particular property version.
        # ", "zh_CN": "指定加速项目版本，查询该加速项目版本相关的验证任务。"}
        self.property_version = property_version
        # {"en" : "Enum: waiting,in progress,succeeded,failed 
        # Filter validation tasks per status. By default, all tasks are returned regardless of their status. ", "zh_CN": "取值范围: waiting,in progress,succeeded,failed 
        # 根据状态查询验证任务。默认情况下，查询所有状态下的验证任务。"}
        self.status = status
        # {"en" : "Default: 100 Range: [ 1 .. 200 ] 
        # Indicates the maximum number of validation tasks to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Default: 0 Range: >= 0 
        # Indicates the index of the first validation task to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "The results will be filtered based on the presence of the value as a validation task ID or in a task name.", "zh_CN": "根据该关键字匹配验证任务的ID或者名称进行查询。"}
        self.search = search
        # {"en" : "Enum: submissionTime,finishTime 
        # Default: finishTime 
        # Return results sorted by when the task was submitted (submissionTime) or when the task was completed (finishTime). ", "zh_CN": "取值范围: submissionTime,finishTime 
        # 默认值: finishTime 
        # 查询结果根据验证任务的提交时间（submissionTime）或者完成时间（finishTime）进行排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc,desc 
        # Default: desc 
        # Return results sorted in ascending (asc) or descending (desc) order.
        # ", "zh_CN": "取值范围: asc,desc 
        # 默认值: desc 
        # 查询结果按照升序（asc）或者降序（desc）返回。"}
        self.sort_order = sort_order
        # {"en" : "Enter an RFC 3339 format date to return validation tasks which were submitted by this date.", "zh_CN": "指定RFC 3339格式的日期，查询提交时间晚于该日期的验证任务。"}
        self.startdate = startdate
        # {"en" : "Enter an RFC 3339 format date to return validation tasks which were submitted no later than this date.", "zh_CN": "指定RFC 3339格式的日期，查询提交时间早于该日期的验证任务。"}
        self.enddate = enddate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.property_version is not None:
            result['propertyVersion'] = self.property_version
        if self.status is not None:
            result['status'] = self.status
        if self.limit is not None:
            result['limit'] = self.limit
        if self.offset is not None:
            result['offset'] = self.offset
        if self.search is not None:
            result['search'] = self.search
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.startdate is not None:
            result['startdate'] = self.startdate
        if self.enddate is not None:
            result['enddate'] = self.enddate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('propertyVersion') is not None:
            self.property_version = m.get('propertyVersion')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        return self


class GetListOfPropertyValidationTasksRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyValidationTasksRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyValidationTasksResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyValidationTasksResponseValidations(TeaModel):
    def __init__(
        self,
        id: str = None,
        property_id: str = None,
        version: int = None,
        submission_time: str = None,
        status: str = None,
        cache_version: str = None,
        api_request_id: str = None,
    ):
        # {"en" : "ID of the validation task.", "zh_CN": "验证任务ID。"}
        self.id = id
        # {"en" : "ID of the property that was validated.", "zh_CN": "提交验证的加速项目的ID。"}
        self.property_id = property_id
        # {"en" : "Range: >= 1 
        # Version of the property that was validated.", "zh_CN": "取值范围: >= 1 
        # 提交验证的加速项目的版本。"}
        self.version = version
        # {"en" : "An RFC 3339 format string indicating when the validation task was submitted. Example: '2019-11-12T03:09:26Z'", "zh_CN": "RFC 3339格式的日期，表示验证任务的提交时间。如：'2019-11-12T03:09:26Z'。"}
        self.submission_time = submission_time
        # {"en" : "Enum: waiting,in progress,succeeded,failed 
        # Status of the validation task.", "zh_CN": "取值范围: waiting,in progress,succeeded,failed 
        # 验证任务的执行状态，包括等待中，进行中，验证成功以及验证失败等状态。"}
        self.status = status
        # {"en" : "Identifies the internal cache version on which the property was validated.", "zh_CN": "验证加速项目时使用的CDN Pro cache服务器的版本。"}
        self.cache_version = cache_version
        # {"en" : "Indicates the associated API request.", "zh_CN": "API请求ID。"}
        self.api_request_id = api_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.status is not None:
            result['status'] = self.status
        if self.cache_version is not None:
            result['cacheVersion'] = self.cache_version
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('cacheVersion') is not None:
            self.cache_version = m.get('cacheVersion')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        return self


class GetListOfPropertyValidationTasksResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        validations: List[GetListOfPropertyValidationTasksResponseValidations] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of validation tasks", "zh_CN": "取值范围: >= 0 
        # 验证任务的总数。"}
        self.count = count
        # {"en" : "Summarizes validation tasks. Further details about a validation task can be obtained by calling the Query a property validation task API.", "zh_CN": "验证任务摘要信息。通过调用'查询验证任务详情'接口，可获得有关验证任务的详细信息。"}
        self.validations = validations

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.validations, 'validations')
        if self.validations:
            for k in self.validations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.validations is not None:
            result['validations'] = []
            for k in self.validations:
                result['validations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('validations') is not None:
            self.validations = []
            for k in m.get('validations'):
                temp_model = GetListOfPropertyValidationTasksResponseValidations()
                self.validations.append(temp_model.from_map(k))
        return self






class CreateAValidationTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAValidationTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAValidationTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAValidationTaskRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        property_id: str = None,
        version: int = None,
        webhook: str = None,
    ):
        # {"en" : "Name of the validation task.", "zh_CN": "验证任务的名称。"}
        self.name = name
        # {"en" : "Indicates the property to validate.", "zh_CN": "需要验证的加速项目的ID。"}
        self.property_id = property_id
        # {"en" : "Indicates the version of the property to validate.", "zh_CN": "需要验证的加速项目的版本号。"}
        self.version = version
        # {"en" : "ID of a webhook to call when the validation task completes.", "zh_CN": "验证任务完成时需要调用的webhook ID。webhook是指通过“创建webhook接口”创建的回调接口。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class CreateAValidationTaskResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAValidationTaskResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header contains a URL to the validation task. Example: <code>Location: https://{domain}/cdn/validations/5dca2205f9e9cc0001df7b24</code>", "zh_CN":"通过Location响应头返回新建的验证任务的URL。URL中包含了验证任务的ID，可使用该ID调用'查询验证任务详情'接口来查看任务详情。URL示例：<code>Location: https://{domain}/cdn/validations/5dca2205f9e9cc0001df7b24</code>"}
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




