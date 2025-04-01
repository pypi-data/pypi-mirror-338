# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetDeploymentTaskPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of the deployment task.", "zh_CN": "部署任务id。"}
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


class GetDeploymentTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDeploymentTaskRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDeploymentTaskRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDeploymentTaskResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetDeploymentTaskResponseActions(TeaModel):
    def __init__(
        self,
        action: str = None,
        property_id: str = None,
        certificate_id: str = None,
        version: str = None,
    ):
        # {"en" : "Enum: deploy_property,remove_property,deploy_cert,remove_cert 
        # Describe an action to take. You can deploy a property, remove a property, deploy a certificate, or remove a certificate.", "zh_CN": "取值范围: deploy_property,remove_property,deploy_cert,remove_cert 
        # 指定操作类型，包括部署加速项目、卸载加速项目、部署证书以及卸载证书。"}
        self.action = action
        # {"en" : "ID of the property to deploy or remove from the staging or production environment.", "zh_CN": "指定要部署或卸载的加速项目ID。"}
        self.property_id = property_id
        # {"en" : "Indicates the certificate to deploy or remove from the staging or production environment.", "zh_CN": "指定要部署或卸载的证书ID。"}
        self.certificate_id = certificate_id
        # {"en" : "Indicates the version of the certificate or property to deploy or remove.", "zh_CN": "指定要部署或卸载的证书或加速项目的版本。"}
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetDeploymentTaskResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        submission_time: str = None,
        actions: List[GetDeploymentTaskResponseActions] = None,
        target: str = None,
        finish_time: str = None,
        status: str = None,
        status_details: str = None,
        api_request_id: str = None,
        webhook: str = None,
    ):
        # {"en" : "Name of the deployment task.", "zh_CN": "部署任务的名称。"}
        self.name = name
        # {"en" : "RFC 3339 date indicating when the task was created.", "zh_CN": "RFC 3339格式的日期，表示任务的创建时间。"}
        self.submission_time = submission_time
        # {"en" : "This array contains all the actions related to a deployment. They can include deployment and removal of properties and certificates to the staging or production environments.", "zh_CN": "部署任务所要执行的操作，可以包括加速项目和证书的部署或卸载操作。"}
        self.actions = actions
        # {"en" : "Enum: staging,production 
        # Indicates the environment affected by the deployment.", "zh_CN": "取值范围: staging,production 
        # 部署任务对应的环境。"}
        self.target = target
        # {"en" : "RFC 3339 date indicating when the task completed.", "zh_CN": "RFC 3339格式的日期，表示任务完成的时间。"}
        self.finish_time = finish_time
        # {"en" : "Enum: waiting,in progress,failed,succeeded 
        # Indicates the status of the deployment task.
        # ", "zh_CN": "取值范围: waiting,in progress,failed,succeeded 
        # 部署任务的执行状态，包括等待中，进行中，部署失败，部署成功等状态。
        # "}
        self.status = status
        # {"en" : "Additional information about the status of the deployment task.
        # ", "zh_CN": "部署任务执行状态的描述信息。
        # "}
        self.status_details = status_details
        # {"en" : "ID of the API call to create the deployment task.
        # ", "zh_CN": "创建部署任务时的API请求ID。"}
        self.api_request_id = api_request_id
        # {"en" : "ID of a webhook to call when the deployment task completes.", "zh_CN": "部署任务完成时要调用的webhook的ID。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.submission_time, 'submission_time')
        self.validate_required(self.actions, 'actions')
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        self.validate_required(self.target, 'target')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_details, 'status_details')
        self.validate_required(self.api_request_id, 'api_request_id')
        self.validate_required(self.webhook, 'webhook')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.actions is not None:
            result['actions'] = []
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_details is not None:
            result['statusDetails'] = self.status_details
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('actions') is not None:
            self.actions = []
            for k in m.get('actions'):
                temp_model = GetDeploymentTaskResponseActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusDetails') is not None:
            self.status_details = m.get('statusDetails')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self






class CreateADeploymentTaskPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateADeploymentTaskParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateADeploymentTaskRequestHeader(TeaModel):
    def __init__(
        self,
        check_certificate: str = None,
        check_usage: str = None,
    ):
        # {"en":"By default, if you deploy a property using a certificate, we check that the hostnames in the property are covered by the subject alternative name (SAN) of the certificate and that the certificate has not expired. For test purposes, you can bypass this check by passing the <i>Check-Certificate: no</i> header when creating the deployment task. You should not use this header when deploying for real users of your content since their browsers will warn about the invalid certificate and discourage them from visiting.", "zh_CN":"当您提交部署任务时，后台会校验加速项目所引用的证书是否已过期，以及加速域名是否与证书的授权域名匹配。如果您的部署操作是出于测试目的，您可以在调用接口时传入请求头<i>Check-Certificate: no</i>来跳过校验。非测试目的，不建议跳过校验。"}
        self.check_certificate = check_certificate
        # {"en":"When you request to undeploy a property, we check if the hostnames in the property are still active. Undeployment of the property will be rejected if there are requests to the hostnames in the past 24 hours. This is to prevent accidental undeployment. If you are sure that the property can be undeployed, you can bypass this check by passing the <i>Check-Usage: no</i> header.", "zh_CN":"当您卸载加速项目时，后台会校验加速项目下的域名是否处于活跃状态。如果域名在过去24小时仍有产生请求，则会拒绝卸载加速项目，避免误操作。如果您确定要卸载加速项目，可以在调用接口时传入请求头<i>Check-Usage: no</i>来跳过校验。"}
        self.check_usage = check_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_certificate is not None:
            result['Check-Certificate'] = self.check_certificate
        if self.check_usage is not None:
            result['Check-Usage'] = self.check_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check-Certificate') is not None:
            self.check_certificate = m.get('Check-Certificate')
        if m.get('Check-Usage') is not None:
            self.check_usage = m.get('Check-Usage')
        return self


class CreateADeploymentTaskRequestActions(TeaModel):
    def __init__(
        self,
        action: str = None,
        property_id: str = None,
        certificate_id: str = None,
        version: str = None,
    ):
        # {"en" : "Enum: deploy_property,remove_property,deploy_cert,remove_cert 
        # Describe an action to take. You can deploy a property, remove a property, deploy a certificate, or remove a certificate.", "zh_CN": "取值范围: deploy_property,remove_property,deploy_cert,remove_cert 
        # 指定操作类型，包括部署加速项目、卸载加速项目、部署证书以及卸载证书。"}
        self.action = action
        # {"en" : "ID of the property to deploy or remove from the staging or production environment.", "zh_CN": "指定要部署或卸载的加速项目ID。"}
        self.property_id = property_id
        # {"en" : "Indicates the certificate to deploy or remove from the staging or production environment.", "zh_CN": "指定要部署或卸载的证书ID。"}
        self.certificate_id = certificate_id
        # {"en" : "Indicates the version of the certificate or property to deploy or remove.", "zh_CN": "指定要部署或卸载的证书或加速项目的版本。"}
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateADeploymentTaskRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: str = None,
        actions: List[CreateADeploymentTaskRequestActions] = None,
        webhook: str = None,
    ):
        # {"en" : "Name of the deployment task.", "zh_CN": "部署任务的名称。"}
        self.name = name
        # {"en" : "Enum: staging,production 
        # Indicates whether to deploy to staging or production.", "zh_CN": "取值范围: staging,production 
        # 指定部署任务的目标环境，即演练或生产环境。"}
        self.target = target
        # {"en" : "This array contains all the actions related to a deployment. They can include deployment and removal of properties and certificates to the staging or production environments.", "zh_CN": "部署任务所要执行的操作，可以包括加速项目和证书的部署或卸载操作。"}
        self.actions = actions
        # {"en" : "ID of a webhook to call when the deployment task completes.", "zh_CN": "部署任务完成时要调用的webhook的ID。"}
        self.webhook = webhook

    def validate(self):
        self.validate_required(self.target, 'target')
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target
        if self.actions is not None:
            result['actions'] = []
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('actions') is not None:
            self.actions = []
            for k in m.get('actions'):
                temp_model = CreateADeploymentTaskRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class CreateADeploymentTaskResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateADeploymentTaskResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The Location header's value will be the URL of the new deployment task.  Example: <code>Location: https://{domain}/cdn/deploymentTasks/ac8e3085-ef92-4c12-ab1b-19b18ac9383c</code>", "zh_CN":"通过Location响应头返回新建的部署任务的URL。可使用该URL调用'获取部署任务详细信息'接口来查看部署任务的详细信息。URL示例：<code>Location: https://{domain}/cdn/deploymentTasks/ac8e3085-ef92-4c12-ab1b-19b18ac9383c</code>"}
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






class GetListOfDeploymentTasksPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfDeploymentTasksParameters(TeaModel):
    def __init__(
        self,
        offset: int = None,
        limit: int = None,
        property_id: str = None,
        certificate_id: str = None,
        target: str = None,
        status: str = None,
        search: str = None,
        task_ids: str = None,
        sort_by: str = None,
        sort_order: str = None,
        startdate: str = None,
        enddate: str = None,
    ):
        # {"en" : "Default: 0 Range: >= 0 
        # Index of the first task to return. ", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: <= 200 
        # Maximum number of tasks to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Only return deployment tasks related to this property.", "zh_CN": "指定加速项目ID，查询该加速项目相关的部署任务。"}
        self.property_id = property_id
        # {"en" : "Only return deployment tasks related to this certificate.", "zh_CN": "指定证书ID，查询该证书相关的部署任务。"}
        self.certificate_id = certificate_id
        # {"en" : "Enum: staging,production 
        # Return deployment tasks to a particular environment. By default, all tasks are returned.", "zh_CN": "取值范围: staging,production 
        # 根据部署环境查询。默认情况下，查询所有环境的部署任务。"}
        self.target = target
        # {"en" : "Enum: waiting,inprogress,succeeded,failed 
        # Filter deployment tasks per status. By default, all tasks are returned regardless of their status. ", "zh_CN": "取值范围: waiting,inprogress,succeeded,failed 
        # 根据状态查询部署任务。默认情况下，查询所有状态下的部署任务。"}
        self.status = status
        # {"en" : "Filter based on text in the deployment name or in a property's hostname.", "zh_CN": "根据搜索关键字匹配部署任务名称及加速项目下的域名进行查询。"}
        self.search = search
        # {"en" : "A comma-separated list of task IDs indicating which ones to return.", "zh_CN": "根据部署任务ID查询。可指定多个ID，以逗号分隔。"}
        self.task_ids = task_ids
        # {"en" : "Enum: submissionTime,finishTime 
        # Default: finishTime 
        # Return results sorted by this value.", "zh_CN": "取值范围: submissionTime,finishTime 
        # 默认值: finishTime 
        # 根据任务提交时间或完成时间进行排序。"}
        self.sort_by = sort_by
        # {"en" : "Enum: asc,desc 
        # Default: desc 
        # Return results in this order.", "zh_CN": "取值范围: asc,desc 
        # 默认值: desc 
        # 指定排序顺序。"}
        self.sort_order = sort_order
        # {"en" : "Enter an RFC 3339 format date to return deployments which were submitted by this date.", "zh_CN": "指定RFC 3339格式的日期，查询提交时间晚于该日期的部署任务。"}
        self.startdate = startdate
        # {"en" : "Enter an RFC 3339 format date to return deployments which were submitted no later than this date.", "zh_CN": "指定RFC 3339格式的日期，查询提交时间早于该日期的部署任务。"}
        self.enddate = enddate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.certificate_id is not None:
            result['certificateId'] = self.certificate_id
        if self.target is not None:
            result['target'] = self.target
        if self.status is not None:
            result['status'] = self.status
        if self.search is not None:
            result['search'] = self.search
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
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
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('certificateId') is not None:
            self.certificate_id = m.get('certificateId')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('startdate') is not None:
            self.startdate = m.get('startdate')
        if m.get('enddate') is not None:
            self.enddate = m.get('enddate')
        return self


class GetListOfDeploymentTasksRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfDeploymentTasksRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfDeploymentTasksResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfDeploymentTasksResponseDeploy(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        submission_time: str = None,
        finish_time: str = None,
        status: str = None,
        target: str = None,
        api_request_id: str = None,
    ):
        # {"en" : "ID representing the deployment task. You can obtain more information about a task by calling the Query deployment task API.", "zh_CN": "部署任务的ID。您可以通过调用'获取部署任务的详细信息'接口来获取部署任务的更多信息。"}
        self.id = id
        # {"en" : "Name of the deployment task.", "zh_CN": "部署任务的名称。"}
        self.name = name
        # {"en" : "An RFC 3339 format date indicates when the task was submitted.", "zh_CN": "RFC 3339格式的日期，表示任务的提交时间。"}
        self.submission_time = submission_time
        # {"en" : "An RFC 3339 date indicates when the task completed.", "zh_CN": "RFC 3339格式的日期，表示任务的完成时间。"}
        self.finish_time = finish_time
        # {"en" : "Enum: waiting,inprogress,failed,succeeded 
        # Indicates the status of the deployment task.", "zh_CN": "取值范围: waiting,inprogress,failed,succeeded 
        # 部署任务的执行状态，包括等待中，执行中，部署失败，部署成功等状态。"}
        self.status = status
        # {"en" : "Enum: staging,production 
        # Indicates where the deployment will go to.", "zh_CN": "取值范围: staging,production 
        # 部署任务对应的环境，即演练环境或生产环境。"}
        self.target = target
        # {"en" : "An internal ID indicating the associated API call.", "zh_CN": "API请求的ID。"}
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
        if self.name is not None:
            result['name'] = self.name
        if self.submission_time is not None:
            result['submissionTime'] = self.submission_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.status is not None:
            result['status'] = self.status
        if self.target is not None:
            result['target'] = self.target
        if self.api_request_id is not None:
            result['apiRequestId'] = self.api_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('submissionTime') is not None:
            self.submission_time = m.get('submissionTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('apiRequestId') is not None:
            self.api_request_id = m.get('apiRequestId')
        return self


class GetListOfDeploymentTasksResponse(TeaModel):
    def __init__(
        self,
        deploy: List[GetListOfDeploymentTasksResponseDeploy] = None,
        count: int = None,
    ):
        # {"en" : "List of deployment task summaries.", "zh_CN": "部署任务列表。"}
        self.deploy = deploy
        # {"en" : "Range: >= 0 
        # Total number of deployment tasks.", "zh_CN": "取值范围: >= 0 
        # 部署任务的总数。"}
        self.count = count

    def validate(self):
        self.validate_required(self.deploy, 'deploy')
        if self.deploy:
            for k in self.deploy:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy is not None:
            result['deploy'] = []
            for k in self.deploy:
                result['deploy'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploy') is not None:
            self.deploy = []
            for k in m.get('deploy'):
                temp_model = GetListOfDeploymentTasksResponseDeploy()
                self.deploy.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self




