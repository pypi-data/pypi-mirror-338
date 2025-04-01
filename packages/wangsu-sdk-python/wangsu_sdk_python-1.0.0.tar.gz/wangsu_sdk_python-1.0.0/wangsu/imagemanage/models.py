# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteImageTagRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImageTagResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: bool = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"result: true/false", "zh_CN":"结果:true/false"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteImageTagPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImageTagParameters(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        tags: str = None,
        name: str = None,
    ):
        # {"en":"project name", "zh_CN":"组织名称"}
        self.project_name = project_name
        # {"en":"image tags,split with \",\"", "zh_CN":"镜像版本号,\",\"分隔"}
        self.tags = tags
        # {"en":"image name,like: project/image", "zh_CN":"镜像名称,格式:project/image"}
        self.name = name

    def validate(self):
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.tags, 'tags')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteImageTagRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImageTagResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetImageDetailRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImageDetailTag(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_name: str = None,
        size: str = None,
        description: str = None,
        image_addr: str = None,
        create_time: int = None,
        push_time: int = None,
    ):
        # {"en":"tag id", "zh_CN":"tag id"}
        self.tag_id = tag_id
        # {"en":"tag name", "zh_CN":"tag名称"}
        self.tag_name = tag_name
        # {"en":"image size", "zh_CN":"镜像大小"}
        self.size = size
        # {"en":"description", "zh_CN":"描述"}
        self.description = description
        # {"en":"image address", "zh_CN":"镜像地址"}
        self.image_addr = image_addr
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"push time", "zh_CN":"推送时间"}
        self.push_time = push_time

    def validate(self):
        self.validate_required(self.tag_id, 'tag_id')
        self.validate_required(self.tag_name, 'tag_name')
        self.validate_required(self.size, 'size')
        self.validate_required(self.description, 'description')
        self.validate_required(self.image_addr, 'image_addr')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.push_time, 'push_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['tagId'] = self.tag_id
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        if self.size is not None:
            result['size'] = self.size
        if self.description is not None:
            result['description'] = self.description
        if self.image_addr is not None:
            result['imageAddr'] = self.image_addr
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.push_time is not None:
            result['pushTime'] = self.push_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagId') is not None:
            self.tag_id = m.get('tagId')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('imageAddr') is not None:
            self.image_addr = m.get('imageAddr')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('pushTime') is not None:
            self.push_time = m.get('pushTime')
        return self


class GetImageDetailImageInfo(TeaModel):
    def __init__(
        self,
        image_id: int = None,
        project_id: int = None,
        image_name: str = None,
        project_name: str = None,
        tag_count: int = None,
        type: int = None,
        repository_plus: str = None,
        create_time: int = None,
        update_time: int = None,
        tags: List[GetImageDetailTag] = None,
    ):
        # {"en":"image id", "zh_CN":"image id"}
        self.image_id = image_id
        # {"en":"project id", "zh_CN":"组织 id"}
        self.project_id = project_id
        # {"en":"image name", "zh_CN":"镜像名称"}
        self.image_name = image_name
        # {"en":"project name", "zh_CN":"组织名称"}
        self.project_name = project_name
        # {"en":"tag count", "zh_CN":"tag 数量"}
        self.tag_count = tag_count
        # {"en":"project type", "zh_CN":"组织类别"}
        self.type = type
        # {"en":"repository_plus", "zh_CN":"repository_plus"}
        self.repository_plus = repository_plus
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"update time", "zh_CN":"更新时间"}
        self.update_time = update_time
        # {"en":"tag list", "zh_CN":"tag列表"}
        self.tags = tags

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.project_id, 'project_id')
        self.validate_required(self.image_name, 'image_name')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.tag_count, 'tag_count')
        self.validate_required(self.type, 'type')
        self.validate_required(self.repository_plus, 'repository_plus')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.tag_count is not None:
            result['tagCount'] = self.tag_count
        if self.type is not None:
            result['type'] = self.type
        if self.repository_plus is not None:
            result['repository_plus'] = self.repository_plus
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.tags is not None:
            result['tags'] = []
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('tagCount') is not None:
            self.tag_count = m.get('tagCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('repository_plus') is not None:
            self.repository_plus = m.get('repository_plus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('tags') is not None:
            self.tags = []
            for k in m.get('tags'):
                temp_model = GetImageDetailTag()
                self.tags.append(temp_model.from_map(k))
        return self


class GetImageDetailResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetImageDetailImageInfo = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"tags list", "zh_CN":"tags列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetImageDetailImageInfo()
            self.data = temp_model.from_map(m['data'])
        return self


class GetImageDetailPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImageDetailParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        project_name: str = None,
    ):
        # {"en":"image name", "zh_CN":"镜像名称"}
        self.name = name
        # {"en":"project name", "zh_CN":"组织名称"}
        self.project_name = project_name

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.project_name, 'project_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class GetImageDetailRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImageDetailResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PatchImagePullJobOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class PatchImagePullJobFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchImagePullJobManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PatchImagePullJobFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PatchImagePullJobManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PatchImagePullJobFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PatchImagePullJobFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PatchImagePullJobFieldsV1 holds the first JSON version format as described in the 'PatchImagePullJobFieldsV1' type", "zh_CN":"PatchImagePullJobFieldsV1 包含类型 “PatchImagePullJobFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = PatchImagePullJobFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PatchImagePullJobObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[PatchImagePullJobOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PatchImagePullJobManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = PatchImagePullJobOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PatchImagePullJobManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PatchImagePullJobIntstrIntOrString(TeaModel):
    def __init__(
        self,
        int_val: int = None,
        str_val: str = None,
        type: int = None,
    ):
        # {"en": "the integer value", "zh_CN": "整数值"}
        self.int_val = int_val
        # {"en": "the string value", "zh_CN": "字符串值"}
        self.str_val = str_val
        # {"en": "type", "zh_CN": "类型"}
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_val is not None:
            result['intVal'] = self.int_val
        if self.str_val is not None:
            result['strVal'] = self.str_val
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intVal') is not None:
            self.int_val = m.get('intVal')
        if m.get('strVal') is not None:
            self.str_val = m.get('strVal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PatchImagePullJobPullPolicy(TeaModel):
    def __init__(
        self,
        backoff_limit: int = None,
        timeout_seconds: int = None,
    ):
        # {"en": "Specifies the number of retries before marking the pulling task failed. Defaults to 3 +optional", "zh_CN": "backoff次数，默认3"}
        self.backoff_limit = backoff_limit
        # {"en": "Specifies the timeout of the pulling task. Defaults to 600 +optional", "zh_CN": "拉取超时时间"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class PatchImagePullJobImagePullJobSpec(TeaModel):
    def __init__(
        self,
        image: str = None,
        parallelism: PatchImagePullJobIntstrIntOrString = None,
        pull_policy: PatchImagePullJobPullPolicy = None,
        pull_secrets: List[str] = None,
    ):
        # {"en": "Image is the image to be pulled by the job", "zh_CN": "拉取镜像名"}
        self.image = image
        # {"en": "Parallelism is the requested parallelism, it can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.The value range 0-10, +optional", "zh_CN": "并发拉取个数, 范围0-10"}
        self.parallelism = parallelism
        # {"en": "PatchImagePullJobPullPolicy is an optional field to set parameters of the pulling task. If not specified, the system will use the default values.+optional", "zh_CN": "拉取策略"}
        self.pull_policy = pull_policy
        # {"en": "ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling the image.If specified, these secrets will be passed to individual puller implementations for them to use.  For example,in the case of docker, only DockerConfig type secrets are honored.+optional", "zh_CN": "拉取镜像所需的密钥"}
        self.pull_secrets = pull_secrets

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.parallelism:
            self.parallelism.validate()
        if self.pull_policy:
            self.pull_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism.to_map()
        if self.pull_policy is not None:
            result['pullPolicy'] = self.pull_policy.to_map()
        if self.pull_secrets is not None:
            result['pullSecrets'] = self.pull_secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parallelism') is not None:
            temp_model = PatchImagePullJobIntstrIntOrString()
            self.parallelism = temp_model.from_map(m['parallelism'])
        if m.get('pullPolicy') is not None:
            temp_model = PatchImagePullJobPullPolicy()
            self.pull_policy = temp_model.from_map(m['pullPolicy'])
        if m.get('pullSecrets') is not None:
            self.pull_secrets = m.get('pullSecrets')
        return self


class PatchImagePullJobRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PatchImagePullJobObjectMeta = None,
        spec: PatchImagePullJobImagePullJobSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the PatchImagePullJobImagePullJob.", "zh_CN":"PatchImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PatchImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PatchImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PatchImagePullJobImagePullJobStatus(TeaModel):
    def __init__(
        self,
        completion_time: str = None,
        message: str = None,
        start_time: str = None,
        succeeded_rate: str = None,
    ):
        # {"en": "Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务完成时间"}
        self.completion_time = completion_time
        # {"en": "The text prompt for job running status.+optional", "zh_CN": "状态消息"}
        self.message = message
        # {"en": "Represents time when the job was acknowledged by the job controller.It is not guaranteed to be set in happens-before order across separate operations.It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务开始时间"}
        self.start_time = start_time
        # {"en": "The rate of pulling tasks which reached phase Succeeded without not ready nodes. +optional", "zh_CN": "完成成功率"}
        self.succeeded_rate = succeeded_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time
        if self.message is not None:
            result['message'] = self.message
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.succeeded_rate is not None:
            result['succeededRate'] = self.succeeded_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('succeededRate') is not None:
            self.succeeded_rate = m.get('succeededRate')
        return self


class PatchImagePullJobImagePullJob(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PatchImagePullJobObjectMeta = None,
        spec: PatchImagePullJobImagePullJobSpec = None,
        status: PatchImagePullJobImagePullJobStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the PatchImagePullJobImagePullJob.", "zh_CN":"PatchImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec
        # {"en":"Most recently observed status of the PatchImagePullJobImagePullJob.", "zh_CN":"最近观测到的 PatchImagePullJobImagePullJob 状态。"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PatchImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PatchImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PatchImagePullJobImagePullJobStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class PatchImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PatchImagePullJobImagePullJob = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"imagepulljob", "zh_CN":"imagepulljob"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = PatchImagePullJobImagePullJob()
            self.data = temp_model.from_map(m['data'])
        return self


class PatchImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"imagepulljob name", "zh_CN":"imagepulljob 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class PatchImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeployVmpImagePreheatingRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        node_names: List[str] = None,
    ):
        # {"en":"Image ID", "zh_CN":"镜像id"}
        self.image_id = image_id
        # {"en":"Name of preheating node", "zh_CN":"预热节点"}
        self.node_names = node_names

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.node_names, 'node_names')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.node_names is not None:
            result['nodeNames'] = self.node_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('nodeNames') is not None:
            self.node_names = m.get('nodeNames')
        return self


class DeployVmpImagePreheatingResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployVmpImagePreheatingPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployVmpImagePreheatingParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployVmpImagePreheatingRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeployVmpImagePreheatingResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPQueryImageRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryImageResponse(TeaModel):
    def __init__(
        self,
        images: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
        created_at: str = None,
        size: str = None,
        state: str = None,
    ):
        # {"en":"Image information array", "zh_CN":"镜像信息数组"}
        self.images = images
        # {"en":"Image unique ID, global unique", "zh_CN":"镜像唯一标识，全局唯一"}
        self.id = id
        # {"en":"Mirror name", "zh_CN":"镜像名称"}
        self.name = name
        # {"en":"Mirror belongs to the Lord.", "zh_CN":"镜像属主"}
        self.type = type
        # {"en":"Image creation time, such as: 2017-11-04 14:17:41", "zh_CN":"镜像创建时间，如：2017-11-04 14:17:41"}
        self.created_at = created_at
        # {"en":"Image size in GB", "zh_CN":"镜像大小，单位是GB"}
        self.size = size
        # {"en":"Mirror Status", "zh_CN":"镜像状态"}
        self.state = state

    def validate(self):
        self.validate_required(self.images, 'images')
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.type, 'type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.size, 'size')
        self.validate_required(self.state, 'state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['images'] = self.images
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class VMPQueryImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryImageParameters(TeaModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_dir: str = None,
        limit: int = None,
        marker: str = None,
        ids: str = None,
        name: str = None,
        type: str = None,
        state: str = None,
    ):
        # {"en":"There can be multiple field names for sorting. The values are:
        # Name, createdat, type, size, state", "zh_CN":"排序的字段名称，可以有多个，取值：
        # name、createdAt、type、size、state"}
        self.sort_key = sort_key
        # {"en":"Sorting direction must follow sortkey. Value:
        # Desc: descending, default
        # ASC: ascending order", "zh_CN":"排序方向，必须跟在sortKey后面出现，取值：
        # desc：降序，默认值
        # asc：升序"}
        self.sort_dir = sort_dir
        # {"en":"The number of items displayed on each page is 20 by default", "zh_CN":"每个页面显示条数，默认是20"}
        self.limit = limit
        # {"en":"Query from the image ID specified by the marker", "zh_CN":"从marker指定的镜像id开始查询"}
        self.marker = marker
        # {"en":"Mirror ID. A maximum of 100 IDS can be queried at a time. The IDs are separated by a half angle comma character ','.", "zh_CN":"镜像 ID。单次最多查询 100 条 ID，ID 之间用半角逗号字符','隔开。"}
        self.ids = ids
        # {"en":"Mirror name", "zh_CN":"镜像名称"}
        self.name = name
        # {"en":"The image belongs to the master. Is it a public image or a user-defined image? Value:
        # 
        # Common: official image
        # 
        # Snapshot: user snapshot image
        # 
        # Custom: user defined image'", "zh_CN":"镜像属主，是公共镜像还是用户自定义镜像，取值：
        # COMMON：官方镜像
        # SNAPSHOT：用户快照镜像
        # CUSTOM：用户自定义镜像"}
        self.type = type
        # {"en":"Image status, value:
        # 
        # Active: available status
        # 
        # Building: Creating
        # 
        # Inactive: not available (such as creation failure, etc.)'", "zh_CN":"镜像状态，取值：
        # ACTIVE：可用状态
        # BUILDING：创建中
        # INACTIVE：不可用（如创建失败等）"}
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_dir is not None:
            result['sortDir'] = self.sort_dir
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortDir') is not None:
            self.sort_dir = m.get('sortDir')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class VMPQueryImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPQueryImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateHarborProjectAssignRole(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: int = None,
    ):
        # {"en":"user name", "zh_CN":"用户名称"}
        self.name = name
        # {"en":"1: admin, 2: edit, 3: access", "zh_CN":"1: 管理,2: 编辑, 3：访问"}
        self.role = role

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.role, 'role')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class CreateHarborProjectRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        pub: bool = None,
        describe: str = None,
        assign_roles: List[CreateHarborProjectAssignRole] = None,
    ):
        # {"en":"project name", "zh_CN":"项目名称"}
        self.name = name
        # {"en":"false: private, true: public", "zh_CN":"false: 私有,true:公开"}
        self.pub = pub
        # {"en":"project describe", "zh_CN":"项目描述"}
        self.describe = describe
        # {"en":"authorized user", "zh_CN":"授权用户"}
        self.assign_roles = assign_roles

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.pub, 'pub')
        if self.assign_roles:
            for k in self.assign_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.pub is not None:
            result['pub'] = self.pub
        if self.describe is not None:
            result['describe'] = self.describe
        if self.assign_roles is not None:
            result['assignRoles'] = []
            for k in self.assign_roles:
                result['assignRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pub') is not None:
            self.pub = m.get('pub')
        if m.get('describe') is not None:
            self.describe = m.get('describe')
        if m.get('assignRoles') is not None:
            self.assign_roles = []
            for k in m.get('assignRoles'):
                temp_model = CreateHarborProjectAssignRole()
                self.assign_roles.append(temp_model.from_map(k))
        return self


class CreateHarborProjectResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: int = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"project id", "zh_CN":"项目id"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateHarborProjectPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborProjectParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborProjectRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborProjectResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ManageOemImageAppParamsObject(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ManageOemImageOperateObject(TeaModel):
    def __init__(
        self,
        id: str = None,
        op: str = None,
        params: ManageOemImageAppParamsObject = None,
    ):
        # {"en":"ephone oem image id", "zh_CN":"云手机oem镜像id"}
        self.id = id
        # {"en":"operate type", "zh_CN":"操作类型，可选值：delete"}
        self.op = op
        # {"en":"oem image operate params", "zh_CN":"操作的参数"}
        self.params = params

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.op, 'op')
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.op is not None:
            result['op'] = self.op
        if self.params is not None:
            result['params'] = self.params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('params') is not None:
            temp_model = ManageOemImageAppParamsObject()
            self.params = temp_model.from_map(m['params'])
        return self


class ManageOemImageRequest(TeaModel):
    def __init__(
        self,
        oem_images: List[ManageOemImageOperateObject] = None,
    ):
        # {"en":"list of apps to operate on", "zh_CN":"操作的云手机应用数组"}
        self.oem_images = oem_images

    def validate(self):
        self.validate_required(self.oem_images, 'oem_images')
        if self.oem_images:
            for k in self.oem_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_images is not None:
            result['oemImages'] = []
            for k in self.oem_images:
                result['oemImages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemImages') is not None:
            self.oem_images = []
            for k in m.get('oemImages'):
                temp_model = ManageOemImageOperateObject()
                self.oem_images.append(temp_model.from_map(k))
        return self


class ManageOemImageTask(TeaModel):
    def __init__(
        self,
        id: str = None,
        message: str = None,
    ):
        # {"en":"task id", "zh_CN":"任务单id"}
        self.id = id
        # {"en":"message", "zh_CN":"任务单消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ManageOemImageResponse(TeaModel):
    def __init__(
        self,
        tasks: List[ManageOemImageTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.tasks, 'tasks')
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tasks is not None:
            result['tasks'] = []
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = []
            for k in m.get('tasks'):
                temp_model = ManageOemImageTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ManageOemImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ManageOemImageParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ManageOemImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ManageOemImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateOemImageOemImageReq(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        # {"en":"ephone instance id", "zh_CN":"云手机实例ID"}
        self.instance_id = instance_id
        # {"en":"oem alias name", "zh_CN":"oem镜像名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateOemImageRequest(TeaModel):
    def __init__(
        self,
        oem_images: List[CreateOemImageOemImageReq] = None,
    ):
        # {"en":"list of ephones", "zh_CN":"云手机请求列表"}
        self.oem_images = oem_images

    def validate(self):
        self.validate_required(self.oem_images, 'oem_images')
        if self.oem_images:
            for k in self.oem_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_images is not None:
            result['oemImages'] = []
            for k in self.oem_images:
                result['oemImages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemImages') is not None:
            self.oem_images = []
            for k in m.get('oemImages'):
                temp_model = CreateOemImageOemImageReq()
                self.oem_images.append(temp_model.from_map(k))
        return self


class CreateOemImageOemImageInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        instance_id: str = None,
    ):
        # {"en":"oem image id", "zh_CN":"oem 镜像ID"}
        self.id = id
        # {"en":"oem alias name", "zh_CN":"OEM名称"}
        self.name = name
        # {"en":"ephone instance id", "zh_CN":"云手机实例ID"}
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateOemImageResponse(TeaModel):
    def __init__(
        self,
        oem_images: List[CreateOemImageOemImageInfo] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"oem image detail", "zh_CN":"Oem镜像详情"}
        self.oem_images = oem_images
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.oem_images, 'oem_images')
        if self.oem_images:
            for k in self.oem_images:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_images is not None:
            result['oemImages'] = []
            for k in self.oem_images:
                result['oemImages'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemImages') is not None:
            self.oem_images = []
            for k in m.get('oemImages'):
                temp_model = CreateOemImageOemImageInfo()
                self.oem_images.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateOemImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOemImageParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOemImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOemImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateImagePullJobOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class UpdateImagePullJobFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateImagePullJobManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateImagePullJobFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateImagePullJobManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateImagePullJobFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateImagePullJobFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateImagePullJobFieldsV1 holds the first JSON version format as described in the 'UpdateImagePullJobFieldsV1' type", "zh_CN":"UpdateImagePullJobFieldsV1 包含类型 “UpdateImagePullJobFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = UpdateImagePullJobFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateImagePullJobObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[UpdateImagePullJobOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateImagePullJobManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = UpdateImagePullJobOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateImagePullJobManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateImagePullJobIntstrIntOrString(TeaModel):
    def __init__(
        self,
        int_val: int = None,
        str_val: str = None,
        type: int = None,
    ):
        # {"en": "the integer value", "zh_CN": "整数值"}
        self.int_val = int_val
        # {"en": "the string value", "zh_CN": "字符串值"}
        self.str_val = str_val
        # {"en": "type", "zh_CN": "类型"}
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_val is not None:
            result['intVal'] = self.int_val
        if self.str_val is not None:
            result['strVal'] = self.str_val
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intVal') is not None:
            self.int_val = m.get('intVal')
        if m.get('strVal') is not None:
            self.str_val = m.get('strVal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateImagePullJobPullPolicy(TeaModel):
    def __init__(
        self,
        backoff_limit: int = None,
        timeout_seconds: int = None,
    ):
        # {"en": "Specifies the number of retries before marking the pulling task failed. Defaults to 3 +optional", "zh_CN": "backoff次数，默认3"}
        self.backoff_limit = backoff_limit
        # {"en": "Specifies the timeout of the pulling task. Defaults to 600 +optional", "zh_CN": "拉取超时时间"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class UpdateImagePullJobImagePullJobSpec(TeaModel):
    def __init__(
        self,
        image: str = None,
        parallelism: UpdateImagePullJobIntstrIntOrString = None,
        pull_policy: UpdateImagePullJobPullPolicy = None,
        pull_secrets: List[str] = None,
    ):
        # {"en": "Image is the image to be pulled by the job", "zh_CN": "拉取镜像名"}
        self.image = image
        # {"en": "Parallelism is the requested parallelism, it can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.The value range 0-10, +optional", "zh_CN": "并发拉取个数, 范围0-10"}
        self.parallelism = parallelism
        # {"en": "UpdateImagePullJobPullPolicy is an optional field to set parameters of the pulling task. If not specified, the system will use the default values.+optional", "zh_CN": "拉取策略"}
        self.pull_policy = pull_policy
        # {"en": "ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling the image.If specified, these secrets will be passed to individual puller implementations for them to use.  For example,in the case of docker, only DockerConfig type secrets are honored.+optional", "zh_CN": "拉取镜像所需的密钥"}
        self.pull_secrets = pull_secrets

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.parallelism:
            self.parallelism.validate()
        if self.pull_policy:
            self.pull_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism.to_map()
        if self.pull_policy is not None:
            result['pullPolicy'] = self.pull_policy.to_map()
        if self.pull_secrets is not None:
            result['pullSecrets'] = self.pull_secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parallelism') is not None:
            temp_model = UpdateImagePullJobIntstrIntOrString()
            self.parallelism = temp_model.from_map(m['parallelism'])
        if m.get('pullPolicy') is not None:
            temp_model = UpdateImagePullJobPullPolicy()
            self.pull_policy = temp_model.from_map(m['pullPolicy'])
        if m.get('pullSecrets') is not None:
            self.pull_secrets = m.get('pullSecrets')
        return self


class UpdateImagePullJobImagePullJobStatus(TeaModel):
    def __init__(
        self,
        completion_time: str = None,
        message: str = None,
        start_time: str = None,
        succeeded_rate: str = None,
    ):
        # {"en": "Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务完成时间"}
        self.completion_time = completion_time
        # {"en": "The text prompt for job running status.+optional", "zh_CN": "状态消息"}
        self.message = message
        # {"en": "Represents time when the job was acknowledged by the job controller.It is not guaranteed to be set in happens-before order across separate operations.It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务开始时间"}
        self.start_time = start_time
        # {"en": "The rate of pulling tasks which reached phase Succeeded without not ready nodes. +optional", "zh_CN": "完成成功率"}
        self.succeeded_rate = succeeded_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time
        if self.message is not None:
            result['message'] = self.message
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.succeeded_rate is not None:
            result['succeededRate'] = self.succeeded_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('succeededRate') is not None:
            self.succeeded_rate = m.get('succeededRate')
        return self


class UpdateImagePullJobRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateImagePullJobObjectMeta = None,
        spec: UpdateImagePullJobImagePullJobSpec = None,
        status: UpdateImagePullJobImagePullJobStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the UpdateImagePullJobImagePullJob.", "zh_CN":"UpdateImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec
        # {"en":"Most recently observed status of the UpdateImagePullJobImagePullJob.", "zh_CN":"最近观测到的 UpdateImagePullJobImagePullJob 状态。"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdateImagePullJobImagePullJobStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdateImagePullJobImagePullJob(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateImagePullJobObjectMeta = None,
        spec: UpdateImagePullJobImagePullJobSpec = None,
        status: UpdateImagePullJobImagePullJobStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the UpdateImagePullJobImagePullJob.", "zh_CN":"UpdateImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec
        # {"en":"Most recently observed status of the UpdateImagePullJobImagePullJob.", "zh_CN":"最近观测到的 UpdateImagePullJobImagePullJob 状态。"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdateImagePullJobImagePullJobStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdateImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateImagePullJobImagePullJob = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"imagepulljob", "zh_CN":"imagepulljob"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = UpdateImagePullJobImagePullJob()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"imagepulljob name", "zh_CN":"imagepulljob 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteHarborUserRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborUserResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: int = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"none", "zh_CN":"无"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteHarborUserPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"user name", "zh_CN":"用户名"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteHarborUserParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborUserRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborUserResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetImagePullJobRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImagePullJobOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class GetImagePullJobFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImagePullJobManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetImagePullJobFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetImagePullJobManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetImagePullJobFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetImagePullJobFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetImagePullJobFieldsV1 holds the first JSON version format as described in the 'GetImagePullJobFieldsV1' type", "zh_CN":"GetImagePullJobFieldsV1 包含类型 “GetImagePullJobFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = GetImagePullJobFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetImagePullJobObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[GetImagePullJobOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetImagePullJobManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = GetImagePullJobOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetImagePullJobManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetImagePullJobIntstrIntOrString(TeaModel):
    def __init__(
        self,
        int_val: int = None,
        str_val: str = None,
        type: int = None,
    ):
        # {"en": "the integer value", "zh_CN": "整数值"}
        self.int_val = int_val
        # {"en": "the string value", "zh_CN": "字符串值"}
        self.str_val = str_val
        # {"en": "type", "zh_CN": "类型"}
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_val is not None:
            result['intVal'] = self.int_val
        if self.str_val is not None:
            result['strVal'] = self.str_val
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intVal') is not None:
            self.int_val = m.get('intVal')
        if m.get('strVal') is not None:
            self.str_val = m.get('strVal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetImagePullJobPullPolicy(TeaModel):
    def __init__(
        self,
        backoff_limit: int = None,
        timeout_seconds: int = None,
    ):
        # {"en": "Specifies the number of retries before marking the pulling task failed. Defaults to 3 +optional", "zh_CN": "backoff次数，默认3"}
        self.backoff_limit = backoff_limit
        # {"en": "Specifies the timeout of the pulling task. Defaults to 600 +optional", "zh_CN": "拉取超时时间"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class GetImagePullJobImagePullJobSpec(TeaModel):
    def __init__(
        self,
        image: str = None,
        parallelism: GetImagePullJobIntstrIntOrString = None,
        pull_policy: GetImagePullJobPullPolicy = None,
        pull_secrets: List[str] = None,
    ):
        # {"en": "Image is the image to be pulled by the job", "zh_CN": "拉取镜像名"}
        self.image = image
        # {"en": "Parallelism is the requested parallelism, it can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.The value range 0-10, +optional", "zh_CN": "并发拉取个数, 范围0-10"}
        self.parallelism = parallelism
        # {"en": "GetImagePullJobPullPolicy is an optional field to set parameters of the pulling task. If not specified, the system will use the default values.+optional", "zh_CN": "拉取策略"}
        self.pull_policy = pull_policy
        # {"en": "ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling the image.If specified, these secrets will be passed to individual puller implementations for them to use.  For example,in the case of docker, only DockerConfig type secrets are honored.+optional", "zh_CN": "拉取镜像所需的密钥"}
        self.pull_secrets = pull_secrets

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.parallelism:
            self.parallelism.validate()
        if self.pull_policy:
            self.pull_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism.to_map()
        if self.pull_policy is not None:
            result['pullPolicy'] = self.pull_policy.to_map()
        if self.pull_secrets is not None:
            result['pullSecrets'] = self.pull_secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parallelism') is not None:
            temp_model = GetImagePullJobIntstrIntOrString()
            self.parallelism = temp_model.from_map(m['parallelism'])
        if m.get('pullPolicy') is not None:
            temp_model = GetImagePullJobPullPolicy()
            self.pull_policy = temp_model.from_map(m['pullPolicy'])
        if m.get('pullSecrets') is not None:
            self.pull_secrets = m.get('pullSecrets')
        return self


class GetImagePullJobImagePullJobStatus(TeaModel):
    def __init__(
        self,
        completion_time: str = None,
        message: str = None,
        start_time: str = None,
        succeeded_rate: str = None,
    ):
        # {"en": "Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务完成时间"}
        self.completion_time = completion_time
        # {"en": "The text prompt for job running status.+optional", "zh_CN": "状态消息"}
        self.message = message
        # {"en": "Represents time when the job was acknowledged by the job controller.It is not guaranteed to be set in happens-before order across separate operations.It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务开始时间"}
        self.start_time = start_time
        # {"en": "The rate of pulling tasks which reached phase Succeeded without not ready nodes. +optional", "zh_CN": "完成成功率"}
        self.succeeded_rate = succeeded_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time
        if self.message is not None:
            result['message'] = self.message
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.succeeded_rate is not None:
            result['succeededRate'] = self.succeeded_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('succeededRate') is not None:
            self.succeeded_rate = m.get('succeededRate')
        return self


class GetImagePullJobImagePullJob(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetImagePullJobObjectMeta = None,
        spec: GetImagePullJobImagePullJobSpec = None,
        status: GetImagePullJobImagePullJobStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the GetImagePullJobImagePullJob.", "zh_CN":"GetImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec
        # {"en":"Most recently observed status of the GetImagePullJobImagePullJob.", "zh_CN":"最近观测到的 GetImagePullJobImagePullJob 状态。"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = GetImagePullJobImagePullJobStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class GetImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetImagePullJobImagePullJob = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"imagepulljob", "zh_CN":"imagepulljob"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetImagePullJobImagePullJob()
            self.data = temp_model.from_map(m['data'])
        return self


class GetImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"imagepulljob name", "zh_CN":"imagepulljob 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryVmpImagePreheatingStateRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryVmpImagePreheatingStatePreHeatingInfo(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        state: str = None,
    ):
        # {"en":"Node name", "zh_CN":"节点名称"}
        self.node_name = node_name
        # {"en":"Preheating status: SUCCESS - preheated; FAIL - preheating failed; SENDING - preheating", "zh_CN":"预热状态：SUCCESS-已预热；FAIL-预热失败；SENDING-预热中"}
        self.state = state

    def validate(self):
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.state, 'state')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class QueryVmpImagePreheatingStateResponse(TeaModel):
    def __init__(
        self,
        pre_heating_info: List[QueryVmpImagePreheatingStatePreHeatingInfo] = None,
    ):
        self.pre_heating_info = pre_heating_info

    def validate(self):
        self.validate_required(self.pre_heating_info, 'pre_heating_info')
        if self.pre_heating_info:
            for k in self.pre_heating_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_heating_info is not None:
            result['preHeatingInfo'] = []
            for k in self.pre_heating_info:
                result['preHeatingInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preHeatingInfo') is not None:
            self.pre_heating_info = []
            for k in m.get('preHeatingInfo'):
                temp_model = QueryVmpImagePreheatingStatePreHeatingInfo()
                self.pre_heating_info.append(temp_model.from_map(k))
        return self


class QueryVmpImagePreheatingStatePaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"no", "zh_CN":"镜像id"}
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


class QueryVmpImagePreheatingStateParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryVmpImagePreheatingStateRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryVmpImagePreheatingStateResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPCreateImageRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        instance_uuid: str = None,
        image_src_url: str = None,
        md_5: str = None,
        ostype: str = None,
        min_disk: int = None,
        qga_enabled: str = None,
    ):
        # {"en":"Mirror name", "zh_CN":"镜像名称"}
        self.name = name
        # {"en":"Virtual machine instance ID, optional parameter. This parameter and imagesrcurl must be one of two choices", "zh_CN":"虚拟机实例标识，可选参数，该参数与imageSrcUrl必须二选一"}
        self.instance_uuid = instance_uuid
        # {"en":"Virtual machine image URL address, optional parameter. The parameter and instanceuuid must be one of two choices.", "zh_CN":"虚拟机镜像Url地址，可选参数，该参数与instanceUuid必须二选一"}
        self.image_src_url = image_src_url
        # {"en":"MD5 value of virtual machine image, used with imagesrcurl", "zh_CN":"虚拟机镜像的md5值，与imageSrcUrl配合使用"}
        self.md_5 = md_5
        # {"en":"Operating system type, if the URL address is carried, this parameter is required; if the virtual machine is specified to be created, the ostype of the virtual machine shall prevail.
        # 
        # There are two values: windows and Linux'", "zh_CN":"操作系统类型，如果携带的是url地址时，该参数必填；如果是指定虚拟机创建，则以虚拟机的ostype为准。
        # 有2种取值：windows、linux"}
        self.ostype = ostype
        # {"en":"Minimum requirements for system disk, unit: GB. The system disk size of the selected template must be greater than or equal to this value, otherwise virtual machine creation fails", "zh_CN":"系统盘最小要求，单位是GB。选择的模板的系统盘大小必须大于等于该值，否则虚拟机创建失败"}
        self.min_disk = min_disk
        # {"en":"Whether QEMU guest agent is enabled for the image, and password reset is supported for the opened image
        # 
        # There are two values: true and false'", "zh_CN":"镜像是否开启了qemu guest agent，有开启的镜像支持密码重置
        # 有2种取值：TRUE、FALSE"}
        self.qga_enabled = qga_enabled

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.instance_uuid is not None:
            result['instanceUuid'] = self.instance_uuid
        if self.image_src_url is not None:
            result['imageSrcUrl'] = self.image_src_url
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.ostype is not None:
            result['ostype'] = self.ostype
        if self.min_disk is not None:
            result['minDisk'] = self.min_disk
        if self.qga_enabled is not None:
            result['qgaEnabled'] = self.qga_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceUuid') is not None:
            self.instance_uuid = m.get('instanceUuid')
        if m.get('imageSrcUrl') is not None:
            self.image_src_url = m.get('imageSrcUrl')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('ostype') is not None:
            self.ostype = m.get('ostype')
        if m.get('minDisk') is not None:
            self.min_disk = m.get('minDisk')
        if m.get('qgaEnabled') is not None:
            self.qga_enabled = m.get('qgaEnabled')
        return self


class VMPCreateImageResponse(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"Image unique ID, global unique", "zh_CN":"镜像唯一标识，全局唯一"}
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


class VMPCreateImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateImageParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPCreateImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListHarborUserRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborUserUser(TeaModel):
    def __init__(
        self,
        id: int = None,
        username: str = None,
        create_time: int = None,
        update_time: int = None,
        projects: List[str] = None,
    ):
        # {"zh_CN":"用户id","en":"user id"}
        self.id = id
        # {"zh_CN":"用户名","en":"username"}
        self.username = username
        # {"zh_CN":"创建时间","en":"creation time"}
        self.create_time = create_time
        # {"zh_CN":"更新时间","en":"Update time"}
        self.update_time = update_time
        # {"zh_CN":"用户所属项目","en":"ListHarborUserUser's project"}
        self.projects = projects

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.username, 'username')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.projects, 'projects')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.username is not None:
            result['username'] = self.username
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.projects is not None:
            result['projects'] = self.projects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('projects') is not None:
            self.projects = m.get('projects')
        return self


class ListHarborUserUserList(TeaModel):
    def __init__(
        self,
        items: List[ListHarborUserUser] = None,
        total: int = None,
    ):
        # {"zh_CN":"用户列表","en":"user list"}
        self.items = items
        # {"zh_CN":"记录总数","en":"total number of records"}
        self.total = total

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListHarborUserUser()
                self.items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListHarborUserResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListHarborUserUserList = None,
    ):
        # {"zh_CN":"请求返回码","en":"Request return code"}
        self.code = code
        # {"zh_CN":"请求返回信息","en":"Request return information"}
        self.msg = msg
        # {"zh_CN":"请求识别码","en":"Request ID"}
        self.request_id = request_id
        # {"zh_CN":"用户列表","en":"user list"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListHarborUserUserList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListHarborUserPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborUserParameters(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"zh_CN":"搜索关键字","en":"search for the keyword"}
        self.keyword = keyword
        # {"zh_CN":"分页页数: 默认0","en":"Number of pagination pages: Default 0"}
        self.page_index = page_index
        # {"zh_CN":"每页记录数: 默认10","en":"Number of records per page: Default 10"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListHarborUserRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborUserResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryOemImageRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOemImageOemImageInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        instance_id: str = None,
        status: str = None,
        create_at: str = None,
        available_at: str = None,
    ):
        # {"en":"oem image id", "zh_CN":"oem 镜像ID"}
        self.id = id
        # {"en":"oem alias name", "zh_CN":"OEM名称"}
        self.name = name
        # {"en":"ephone instance id", "zh_CN":"云手机实例id"}
        self.instance_id = instance_id
        # {"en":"oem image status", "zh_CN":"OEM镜像可用状态。1-Available，代表可用，2-Unavailable，代表不可用"}
        self.status = status
        # {"en":"create time", "zh_CN":"创建时间"}
        self.create_at = create_at
        # {"en":"available time", "zh_CN":"可用时间"}
        self.available_at = available_at

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_at, 'create_at')
        self.validate_required(self.available_at, 'available_at')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.create_at is not None:
            result['createAt'] = self.create_at
        if self.available_at is not None:
            result['availableAt'] = self.available_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createAt') is not None:
            self.create_at = m.get('createAt')
        if m.get('availableAt') is not None:
            self.available_at = m.get('availableAt')
        return self


class QueryOemImageResponse(TeaModel):
    def __init__(
        self,
        oem_images: List[QueryOemImageOemImageInfo] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"list of ome image", "zh_CN":"云手机oem镜像列表"}
        self.oem_images = oem_images
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"创建消息"}
        self.result = result

    def validate(self):
        self.validate_required(self.oem_images, 'oem_images')
        if self.oem_images:
            for k in self.oem_images:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oem_images is not None:
            result['oemImages'] = []
            for k in self.oem_images:
                result['oemImages'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oemImages') is not None:
            self.oem_images = []
            for k in m.get('oemImages'):
                temp_model = QueryOemImageOemImageInfo()
                self.oem_images.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryOemImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOemImageParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
        name: str = None,
    ):
        # {"en":"oem image id to be queried", "zh_CN":"要查询的oem镜像id"}
        self.ids = ids
        # {"en":"oem image name bo be queried", "zh_CN":"要查询的oem镜像名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryOemImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryOemImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteImagePullJobRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImagePullJobStatusDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        kind: str = None,
        group: str = None,
        uid: str = None,
    ):
        # {"en":"The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described)", "zh_CN":"与状态 StatusReason 关联的资源的名称属性（当有一个可以描述的名称时）"}
        self.name = name
        # {"en":"The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind", "zh_CN":"与状态 StatusReason 关联的资源的种类属性"}
        self.kind = kind
        # {"en":"The group attribute of the resource associated with the status StatusReason", "zh_CN":"与状态 StatusReason 关联的资源的组属性"}
        self.group = group
        # {"en":"UID of the resource. (when there is a single resource which can be described)", "zh_CN":"资源的 UID（当有单个可以描述的资源时）"}
        self.uid = uid

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.group, 'group')
        self.validate_required(self.uid, 'uid')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.kind is not None:
            result['kind'] = self.kind
        if self.group is not None:
            result['group'] = self.group
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class DeleteImagePullJobStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteImagePullJobStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteImagePullJobStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
        self.status = status
        # {"en":"Suggested HTTP return code for this status, 0 if not set", "zh_CN":"此状态的建议 HTTP 返回代码，如果未设置，则为 0"}
        self.code = code
        # {"en":"Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type", "zh_CN":"与原因（Reason）相关的扩展数据。每个原因都可以定义自己的扩展细节。 此字段是可选的，并且不保证返回的数据符合任何模式，除非由原因类型定义"}
        self.details = details

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.status, 'status')
        self.validate_required(self.code, 'code')
        self.validate_required(self.details, 'details')
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.status is not None:
            result['status'] = self.status
        if self.code is not None:
            result['code'] = self.code
        if self.details is not None:
            result['details'] = self.details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('details') is not None:
            temp_model = DeleteImagePullJobStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteImagePullJobStatus = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"status", "zh_CN":"status"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = DeleteImagePullJobStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"imagepulljob name", "zh_CN":"imagepulljob 名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetHarborProjectRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborProjectAssignRole(TeaModel):
    def __init__(
        self,
        repo_user_id: int = None,
        repo_user_name: str = None,
        role: int = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # {"en":"user id", "zh_CN":"用户id"}
        self.repo_user_id = repo_user_id
        # {"en":"user name", "zh_CN":"用户名称"}
        self.repo_user_name = repo_user_name
        # {"en":"1: admin, 2: edit, 3: access", "zh_CN":"1: 管理,2: 编辑, 3：访问"}
        self.role = role
        # {"en":"project createTime", "zh_CN":"项目创建时间"}
        self.create_time = create_time
        # {"en":"project updateTime", "zh_CN":"项目更新时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.repo_user_id, 'repo_user_id')
        self.validate_required(self.repo_user_name, 'repo_user_name')
        self.validate_required(self.role, 'role')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_user_id is not None:
            result['repoUserId'] = self.repo_user_id
        if self.repo_user_name is not None:
            result['repoUserName'] = self.repo_user_name
        if self.role is not None:
            result['role'] = self.role
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('repoUserId') is not None:
            self.repo_user_id = m.get('repoUserId')
        if m.get('repoUserName') is not None:
            self.repo_user_name = m.get('repoUserName')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetHarborProjectProjectDetail(TeaModel):
    def __init__(
        self,
        id: int = None,
        project_name: str = None,
        pub: bool = None,
        describe: str = None,
        create_time: int = None,
        update_time: int = None,
        assign_roles: List[GetHarborProjectAssignRole] = None,
    ):
        # {"en":"project id", "zh_CN":"项目id"}
        self.id = id
        # {"en":"project name", "zh_CN":"项目名称"}
        self.project_name = project_name
        # {"en":"0: private, 1: public", "zh_CN":"0: 私有, 1: 公开"}
        self.pub = pub
        # {"en":"project describe", "zh_CN":"项目描述"}
        self.describe = describe
        # {"en":"project createTime", "zh_CN":"项目创建时间"}
        self.create_time = create_time
        # {"en":"project updateTime", "zh_CN":"项目更新时间"}
        self.update_time = update_time
        # {"en":"authorized user", "zh_CN":"授权用户"}
        self.assign_roles = assign_roles

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.pub, 'pub')
        self.validate_required(self.describe, 'describe')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.assign_roles, 'assign_roles')
        if self.assign_roles:
            for k in self.assign_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.pub is not None:
            result['pub'] = self.pub
        if self.describe is not None:
            result['describe'] = self.describe
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.assign_roles is not None:
            result['assignRoles'] = []
            for k in self.assign_roles:
                result['assignRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('pub') is not None:
            self.pub = m.get('pub')
        if m.get('describe') is not None:
            self.describe = m.get('describe')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('assignRoles') is not None:
            self.assign_roles = []
            for k in m.get('assignRoles'):
                temp_model = GetHarborProjectAssignRole()
                self.assign_roles.append(temp_model.from_map(k))
        return self


class GetHarborProjectResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetHarborProjectProjectDetail = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"project detal", "zh_CN":"项目详情"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetHarborProjectProjectDetail()
            self.data = temp_model.from_map(m['data'])
        return self


class GetHarborProjectPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"project name", "zh_CN":"项目名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetHarborProjectParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborProjectRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborProjectResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ResetHarborUserPwdRequest(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        # {"en":"user name", "zh_CN":"用户名称"}
        self.username = username

    def validate(self):
        self.validate_required(self.username, 'username')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ResetHarborUserPwdResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"password", "zh_CN":"密码"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ResetHarborUserPwdPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResetHarborUserPwdParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResetHarborUserPwdRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ResetHarborUserPwdResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VMPRemoveImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        # {"en":"Image unique identification", "zh_CN":"镜像唯一标识"}
        self.image_id = image_id

    def validate(self):
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['imageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        return self


class VMPRemoveImageResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveImagePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveImageParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveImageRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VMPRemoveImageResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateHarborUserRequest(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        # {"en":"user name", "zh_CN":"用户名称"}
        self.username = username

    def validate(self):
        self.validate_required(self.username, 'username')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateHarborUserResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"password", "zh_CN":"密码"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateHarborUserPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborUserParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborUserRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHarborUserResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListImagePullJobRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListImagePullJobListMeta(TeaModel):
    def __init__(
        self,
        self_link: str = None,
        resource_version: str = None,
        continue_: str = None,
        remaining_item_count: int = None,
    ):
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system", "zh_CN":"selfLink 表示此对象的 URL，由系统填充，只读。已弃用：selfLink 是一个遗留的只读字段，不再由系统填充。"}
        self.self_link = self_link
        # {"en":"String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only", "zh_CN":"标识该对象的服务器内部版本的字符串，客户端可以用该字段来确定对象何时被更改。 该值对客户端是不透明的，并且应该原样传回给服务器。该值由系统填充，只读"}
        self.resource_version = resource_version
        # {"en":"continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message", "zh_CN":"如果用户对返回的条目数量设置了限制，则 continue 可能被设置，表示服务器有更多可用的数据。 该值是不透明的，可用于向提供此列表服务的端点发出另一个请求，以检索下一组可用的对象。 如果服务器配置已更改或时间已过去几分钟，则可能无法继续提供一致的列表。 除非你在错误消息中收到此令牌（token），否则使用此 continue 值时返回的 resourceVersion 字段应该和第一个响应中的值是相同的"}
        self.continue_ = continue_
        # {"en":"remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is estimating the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact", "zh_CN":"remainingItemCount 是列表中未包含在此列表响应中的后续项目的数量。 如果列表请求包含标签或字段选择器，则剩余项目的数量是未知的，并且在序列化期间该字段将保持未设置和省略。 如果列表是完整的（因为它没有分块或者这是最后一个块），那么就没有剩余的项目，并且在序列化过程中该字段将保持未设置和省略。 早于 v1.15 的服务器不设置此字段。remainingItemCount 的预期用途是估计集合的大小。 客户端不应依赖于设置准确的 remainingItemCount"}
        self.remaining_item_count = remaining_item_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.continue_ is not None:
            result['continue'] = self.continue_
        if self.remaining_item_count is not None:
            result['remainingItemCount'] = self.remaining_item_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('continue') is not None:
            self.continue_ = m.get('continue')
        if m.get('remainingItemCount') is not None:
            self.remaining_item_count = m.get('remainingItemCount')
        return self


class ListImagePullJobOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class ListImagePullJobFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListImagePullJobManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListImagePullJobFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListImagePullJobManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListImagePullJobFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListImagePullJobFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListImagePullJobFieldsV1 holds the first JSON version format as described in the 'ListImagePullJobFieldsV1' type", "zh_CN":"ListImagePullJobFieldsV1 包含类型 “ListImagePullJobFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = ListImagePullJobFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListImagePullJobObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[ListImagePullJobOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListImagePullJobManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = ListImagePullJobOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListImagePullJobManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListImagePullJobIntstrIntOrString(TeaModel):
    def __init__(
        self,
        int_val: int = None,
        str_val: str = None,
        type: int = None,
    ):
        # {"en": "the integer value", "zh_CN": "整数值"}
        self.int_val = int_val
        # {"en": "the string value", "zh_CN": "字符串值"}
        self.str_val = str_val
        # {"en": "type", "zh_CN": "类型"}
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_val is not None:
            result['intVal'] = self.int_val
        if self.str_val is not None:
            result['strVal'] = self.str_val
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intVal') is not None:
            self.int_val = m.get('intVal')
        if m.get('strVal') is not None:
            self.str_val = m.get('strVal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListImagePullJobPullPolicy(TeaModel):
    def __init__(
        self,
        backoff_limit: int = None,
        timeout_seconds: int = None,
    ):
        # {"en": "Specifies the number of retries before marking the pulling task failed. Defaults to 3 +optional", "zh_CN": "backoff次数，默认3"}
        self.backoff_limit = backoff_limit
        # {"en": "Specifies the timeout of the pulling task. Defaults to 600 +optional", "zh_CN": "拉取超时时间"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class ListImagePullJobImagePullJobSpec(TeaModel):
    def __init__(
        self,
        image: str = None,
        parallelism: ListImagePullJobIntstrIntOrString = None,
        pull_policy: ListImagePullJobPullPolicy = None,
        pull_secrets: List[str] = None,
    ):
        # {"en": "Image is the image to be pulled by the job", "zh_CN": "拉取镜像名"}
        self.image = image
        # {"en": "Parallelism is the requested parallelism, it can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.The value range 0-10, +optional", "zh_CN": "并发拉取个数, 范围0-10"}
        self.parallelism = parallelism
        # {"en": "ListImagePullJobPullPolicy is an optional field to set parameters of the pulling task. If not specified, the system will use the default values.+optional", "zh_CN": "拉取策略"}
        self.pull_policy = pull_policy
        # {"en": "ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling the image.If specified, these secrets will be passed to individual puller implementations for them to use.  For example,in the case of docker, only DockerConfig type secrets are honored.+optional", "zh_CN": "拉取镜像所需的密钥"}
        self.pull_secrets = pull_secrets

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.parallelism:
            self.parallelism.validate()
        if self.pull_policy:
            self.pull_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism.to_map()
        if self.pull_policy is not None:
            result['pullPolicy'] = self.pull_policy.to_map()
        if self.pull_secrets is not None:
            result['pullSecrets'] = self.pull_secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parallelism') is not None:
            temp_model = ListImagePullJobIntstrIntOrString()
            self.parallelism = temp_model.from_map(m['parallelism'])
        if m.get('pullPolicy') is not None:
            temp_model = ListImagePullJobPullPolicy()
            self.pull_policy = temp_model.from_map(m['pullPolicy'])
        if m.get('pullSecrets') is not None:
            self.pull_secrets = m.get('pullSecrets')
        return self


class ListImagePullJobImagePullJob(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListImagePullJobObjectMeta = None,
        spec: ListImagePullJobImagePullJobSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the ListImagePullJobImagePullJob.", "zh_CN":"ListImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class ListImagePullJobImagePullJobList(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListImagePullJobListMeta = None,
        items: List[ListImagePullJobImagePullJob] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListImagePullJobImagePullJob", "zh_CN":"ListImagePullJobImagePullJob 列表"}
        self.items = items

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListImagePullJobListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListImagePullJobImagePullJob()
                self.items.append(temp_model.from_map(k))
        return self


class ListImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListImagePullJobImagePullJobList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"imagepulljob list", "zh_CN":"imagepulljob列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListImagePullJobImagePullJobList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class ListImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteHarborProjectRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborProjectResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: int = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"none", "zh_CN":"无"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteHarborProjectPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"project name", "zh_CN":"项目名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteHarborProjectParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborProjectRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHarborProjectResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListHarborProjectRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborProjectProject(TeaModel):
    def __init__(
        self,
        id: int = None,
        project_name: str = None,
        pub: bool = None,
        describe: str = None,
        create_time: int = None,
        update_time: int = None,
        repo_users: List[str] = None,
    ):
        # {"en":"project id", "zh_CN":"项目id"}
        self.id = id
        # {"en":"project name", "zh_CN":"项目名称"}
        self.project_name = project_name
        # {"en":"0: private, 1: public", "zh_CN":"0: 私有, 1: 公开"}
        self.pub = pub
        # {"en":"project describe", "zh_CN":"项目描述"}
        self.describe = describe
        # {"en":"project createTime", "zh_CN":"项目创建时间"}
        self.create_time = create_time
        # {"en":"project updateTime", "zh_CN":"项目更新时间"}
        self.update_time = update_time
        # {"en":"project members", "zh_CN":"项目成员"}
        self.repo_users = repo_users

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.pub, 'pub')
        self.validate_required(self.describe, 'describe')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.repo_users, 'repo_users')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.pub is not None:
            result['pub'] = self.pub
        if self.describe is not None:
            result['describe'] = self.describe
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.repo_users is not None:
            result['repoUsers'] = self.repo_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('pub') is not None:
            self.pub = m.get('pub')
        if m.get('describe') is not None:
            self.describe = m.get('describe')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('repoUsers') is not None:
            self.repo_users = m.get('repoUsers')
        return self


class ListHarborProjectProjectList(TeaModel):
    def __init__(
        self,
        items: List[ListHarborProjectProject] = None,
        total: int = None,
    ):
        # {"en":"projects", "zh_CN":"项目列表"}
        self.items = items
        # {"en":"total records count", "zh_CN":"记录总数"}
        self.total = total

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListHarborProjectProject()
                self.items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListHarborProjectResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListHarborProjectProjectList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"project list", "zh_CN":"项目列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = ListHarborProjectProjectList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListHarborProjectPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborProjectParameters(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"en":"search keyword", "zh_CN":"搜索关键字"}
        self.keyword = keyword
        # {"en":"page index: default 0", "zh_CN":"分页页数: 默认0"}
        self.page_index = page_index
        # {"en":"page size: default 10", "zh_CN":"每页记录数: 默认10"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListHarborProjectRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHarborProjectResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateImagePullJobOwnerReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
        controller: bool = None,
        block_owner_deletion: bool = None,
    ):
        # {"en":"API version of the referent", "zh_CN":"被引用资源的 API 版本"}
        self.api_version = api_version
        # {"en":"Kind of the referent", "zh_CN":"被引用资源的类别"}
        self.kind = kind
        # {"en":"Name of the referent", "zh_CN":"被引用资源的名称"}
        self.name = name
        # {"en":"UID of the referent", "zh_CN":"被引用资源的 uid"}
        self.uid = uid
        # {"en":"If true, this reference points to the managing controller", "zh_CN":"如果为 true，则此引用指向管理的控制器"}
        self.controller = controller
        # {"en":"If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed", "zh_CN":"如果为 true，**并且** 如果属主具有 “foregroundDeletion” 终结器，则在删除此引用之前，无法从键值存储中删除属主。 默认为 false。要设置此字段，用户需要属主的 “delete” 权限， 否则将返回 422 (Unprocessable Entity)"}
        self.block_owner_deletion = block_owner_deletion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        if self.controller is not None:
            result['controller'] = self.controller
        if self.block_owner_deletion is not None:
            result['blockOwnerDeletion'] = self.block_owner_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('controller') is not None:
            self.controller = m.get('controller')
        if m.get('blockOwnerDeletion') is not None:
            self.block_owner_deletion = m.get('blockOwnerDeletion')
        return self


class CreateImagePullJobFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateImagePullJobManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateImagePullJobFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateImagePullJobManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateImagePullJobFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateImagePullJobFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateImagePullJobFieldsV1 holds the first JSON version format as described in the 'CreateImagePullJobFieldsV1' type", "zh_CN":"CreateImagePullJobFieldsV1 包含类型 “CreateImagePullJobFieldsV1” 中描述的第一个 JSON 版本格式"}
        self.fields_v1 = fields_v1
        # {"en":"the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource", "zh_CN":"用于更新该对象的子资源的名称，如果对象是通过主资源更新的，则为空字符串。 该字段的值用于区分管理者，即使他们共享相同的名称。例如，状态更新将不同于使用相同管理者名称的常规更新。 请注意，apiVersion 字段与 subresource 字段无关，它始终对应于主资源的版本"}
        self.subresource = subresource

    def validate(self):
        if self.fields_v1:
            self.fields_v1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['manager'] = self.manager
        if self.operation is not None:
            result['operation'] = self.operation
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.time is not None:
            result['time'] = self.time
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.fields_v1 is not None:
            result['fieldsV1'] = self.fields_v1.to_map()
        if self.subresource is not None:
            result['subresource'] = self.subresource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('manager') is not None:
            self.manager = m.get('manager')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('fieldsV1') is not None:
            temp_model = CreateImagePullJobFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateImagePullJobObjectMeta(TeaModel):
    def __init__(
        self,
        name: str = None,
        generate_name: str = None,
        namespace: str = None,
        self_link: str = None,
        uid: str = None,
        resource_version: str = None,
        generation: int = None,
        creation_timestamp: str = None,
        deletion_timestamp: str = None,
        deletion_grace_period_seconds: int = None,
        labels: Dict[str, str] = None,
        annotations: Dict[str, str] = None,
        owner_references: List[CreateImagePullJobOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateImagePullJobManagedFieldsEntry] = None,
    ):
        # {"en":"must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated", "zh_CN":"name 在命名空间内必须是唯一的。创建资源时需要，尽管某些资源可能允许客户端请求自动地生成适当的名称。 名称主要用于创建幂等性和配置定义。无法更新"}
        self.name = name
        # {"en":"an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server", "zh_CN":"一个可选前缀，由服务器使用，仅在未提供 name 字段时生成唯一名称。 如果使用此字段，则返回给客户端的名称将与传递的名称不同。该值还将与唯一的后缀组合。 提供的值与 name 字段具有相同的验证规则，并且可能会根据所需的后缀长度被截断，以使该值在服务器上唯一"}
        self.generate_name = generate_name
        # {"en":"Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.Must be a DNS_LABEL. Cannot be updated", "zh_CN":"namespace 定义了一个值空间，其中每个名称必须唯一。空命名空间相当于 “default” 命名空间，但 “default” 是规范表示。 并非所有对象都需要限定在命名空间中——这些对象的此字段的值将为空。必须是 DNS_LABEL。无法更新。"}
        self.namespace = namespace
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.", "zh_CN":"表示此对象的 URL。由系统填充。只读。已弃用。Kubernetes 将在 1.20 版本中停止传播该字段，并计划在 1.21 版本中删除该字段。"}
        self.self_link = self_link
        # {"en":"UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.Populated by the system. Read-only", "zh_CN":"该对象在时间和空间上的唯一值。它通常由服务器在成功创建资源时生成，并且不允许使用 PUT 操作更改。由系统填充。只读"}
        self.uid = uid
        # {"en":"An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.Populated by the system. Read-only. Value must be treated as opaque by clients and", "zh_CN":"一个不透明的值，表示此对象的内部版本，客户端可以使用该值来确定对象是否已被更改。 可用于乐观并发、变更检测以及对资源或资源集的监听操作。 客户端必须将这些值视为不透明的，且未更改地传回服务器。 它们可能仅对特定资源或一组资源有效。由系统填充。只读。客户端必须将值视为不透明。"}
        self.resource_version = resource_version
        # {"en":"A sequence number representing a specific generation of the desired state. Populated by the system. Read-only", "zh_CN":"表示期望状态的特定生成的序列号。由系统填充。只读"}
        self.generation = generation
        # {"en":"a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.Populated by the system. Read-only. Null for lists", "zh_CN":"一个时间戳，表示创建此对象时的服务器时间。 不能保证在单独的操作中按发生前的顺序设置。 客户端不得设置此值。它以 RFC3339 形式表示，并采用 UTC。由系统填充。只读。列表为空"}
        self.creation_timestamp = creation_timestamp
        # {"en":"RFC 3339 date and time at which this resource will be deleted", "zh_CN":"删除此资源的 RFC 3339 日期和时间"}
        self.deletion_timestamp = deletion_timestamp
        # {"en":"Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only", "zh_CN":"此对象从系统中删除之前允许正常终止的秒数。 仅当设置了 deletionTimestamp 时才设置。 只能缩短。只读"}
        self.deletion_grace_period_seconds = deletion_grace_period_seconds
        # {"en":"Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services", "zh_CN":"可用于组织和分类（确定范围和选择）对象的字符串键和值的映射。 可以匹配 ReplicationController 和 Service 的选择算符"}
        self.labels = labels
        # {"en":"Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects", "zh_CN":"annotations 是一个非结构化的键值映射，存储在资源中，可以由外部工具设置以存储和检索任意元数据。 它们不可查询，在修改对象时应保留"}
        self.annotations = annotations
        # {"en":"List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller", "zh_CN":"此对象所依赖的对象列表。如果列表中的所有对象都已被删除，则该对象将被垃圾回收。 如果此对象由控制器管理，则此列表中的条目将指向此控制器，controller 字段设置为 true。 管理控制器不能超过一个"}
        self.owner_references = owner_references
        # {"en":"Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.", "zh_CN":"在从注册表中删除对象之前该字段必须为空。 每个条目都是负责的组件的标识符，各组件将从列表中删除自己对应的条目。 如果对象的 deletionTimestamp 非空，则只能删除此列表中的条目。 终结器可以按任何顺序处理和删除。没有按照顺序执行， 因为它引入了终结器卡住的重大风险。finalizers 是一个共享字段， 任何有权限的参与者都可以对其进行重新排序。如果按顺序处理终结器列表， 那么这可能导致列表中第一个负责终结器的组件正在等待列表中靠后负责终结器的组件产生的信号（字段值、外部系统或其他）， 从而导致死锁。在没有强制排序的情况下，终结者可以在它们之间自由排序， 并且不容易受到列表中排序更改的影响。"}
        self.finalizers = finalizers
        # {"en":"name of cluster", "zh_CN":"集群名称"}
        self.cluster_name = cluster_name
        # {"en":"ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object", "zh_CN":"managedFields 将 workflow-id 和版本映射到由该工作流管理的字段集。 这主要用于内部管理，用户通常不需要设置或理解该字段。 工作流可以是用户名、控制器名或特定应用路径的名称，如 “ci-cd”。 字段集始终存在于修改对象时工作流使用的版本"}
        self.managed_fields = managed_fields

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
                if k:
                    k.validate()
        if self.managed_fields:
            for k in self.managed_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.generate_name is not None:
            result['generateName'] = self.generate_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.self_link is not None:
            result['selfLink'] = self.self_link
        if self.uid is not None:
            result['uid'] = self.uid
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        if self.generation is not None:
            result['generation'] = self.generation
        if self.creation_timestamp is not None:
            result['creationTimestamp'] = self.creation_timestamp
        if self.deletion_timestamp is not None:
            result['deletionTimestamp'] = self.deletion_timestamp
        if self.deletion_grace_period_seconds is not None:
            result['deletionGracePeriodSeconds'] = self.deletion_grace_period_seconds
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.owner_references is not None:
            result['ownerReferences'] = []
            for k in self.owner_references:
                result['ownerReferences'].append(k.to_map() if k else None)
        if self.finalizers is not None:
            result['finalizers'] = self.finalizers
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.managed_fields is not None:
            result['managedFields'] = []
            for k in self.managed_fields:
                result['managedFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('generateName') is not None:
            self.generate_name = m.get('generateName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('selfLink') is not None:
            self.self_link = m.get('selfLink')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('creationTimestamp') is not None:
            self.creation_timestamp = m.get('creationTimestamp')
        if m.get('deletionTimestamp') is not None:
            self.deletion_timestamp = m.get('deletionTimestamp')
        if m.get('deletionGracePeriodSeconds') is not None:
            self.deletion_grace_period_seconds = m.get('deletionGracePeriodSeconds')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('ownerReferences') is not None:
            self.owner_references = []
            for k in m.get('ownerReferences'):
                temp_model = CreateImagePullJobOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateImagePullJobManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateImagePullJobIntstrIntOrString(TeaModel):
    def __init__(
        self,
        int_val: int = None,
        str_val: str = None,
        type: int = None,
    ):
        # {"en": "the integer value", "zh_CN": "整数值"}
        self.int_val = int_val
        # {"en": "the string value", "zh_CN": "字符串值"}
        self.str_val = str_val
        # {"en": "type", "zh_CN": "类型"}
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_val is not None:
            result['intVal'] = self.int_val
        if self.str_val is not None:
            result['strVal'] = self.str_val
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intVal') is not None:
            self.int_val = m.get('intVal')
        if m.get('strVal') is not None:
            self.str_val = m.get('strVal')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateImagePullJobPullPolicy(TeaModel):
    def __init__(
        self,
        backoff_limit: int = None,
        timeout_seconds: int = None,
    ):
        # {"en": "Specifies the number of retries before marking the pulling task failed. Defaults to 3 +optional", "zh_CN": "backoff次数，默认3"}
        self.backoff_limit = backoff_limit
        # {"en": "Specifies the timeout of the pulling task. Defaults to 600 +optional", "zh_CN": "拉取超时时间"}
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backoff_limit is not None:
            result['backoffLimit'] = self.backoff_limit
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backoffLimit') is not None:
            self.backoff_limit = m.get('backoffLimit')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class CreateImagePullJobImagePullJobSpec(TeaModel):
    def __init__(
        self,
        image: str = None,
        parallelism: CreateImagePullJobIntstrIntOrString = None,
        pull_policy: CreateImagePullJobPullPolicy = None,
        pull_secrets: List[str] = None,
    ):
        # {"en": "Image is the image to be pulled by the job", "zh_CN": "拉取镜像名"}
        self.image = image
        # {"en": "Parallelism is the requested parallelism, it can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.The value range 0-10, +optional", "zh_CN": "并发拉取个数, 范围0-10"}
        self.parallelism = parallelism
        # {"en": "CreateImagePullJobPullPolicy is an optional field to set parameters of the pulling task. If not specified, the system will use the default values.+optional", "zh_CN": "拉取策略"}
        self.pull_policy = pull_policy
        # {"en": "ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling the image.If specified, these secrets will be passed to individual puller implementations for them to use.  For example,in the case of docker, only DockerConfig type secrets are honored.+optional", "zh_CN": "拉取镜像所需的密钥"}
        self.pull_secrets = pull_secrets

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.parallelism:
            self.parallelism.validate()
        if self.pull_policy:
            self.pull_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism.to_map()
        if self.pull_policy is not None:
            result['pullPolicy'] = self.pull_policy.to_map()
        if self.pull_secrets is not None:
            result['pullSecrets'] = self.pull_secrets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parallelism') is not None:
            temp_model = CreateImagePullJobIntstrIntOrString()
            self.parallelism = temp_model.from_map(m['parallelism'])
        if m.get('pullPolicy') is not None:
            temp_model = CreateImagePullJobPullPolicy()
            self.pull_policy = temp_model.from_map(m['pullPolicy'])
        if m.get('pullSecrets') is not None:
            self.pull_secrets = m.get('pullSecrets')
        return self


class CreateImagePullJobRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateImagePullJobObjectMeta = None,
        spec: CreateImagePullJobImagePullJobSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the CreateImagePullJobImagePullJob.", "zh_CN":"CreateImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateImagePullJobImagePullJobStatus(TeaModel):
    def __init__(
        self,
        completion_time: str = None,
        message: str = None,
        start_time: str = None,
        succeeded_rate: str = None,
    ):
        # {"en": "Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务完成时间"}
        self.completion_time = completion_time
        # {"en": "The text prompt for job running status.+optional", "zh_CN": "状态消息"}
        self.message = message
        # {"en": "Represents time when the job was acknowledged by the job controller.It is not guaranteed to be set in happens-before order across separate operations.It is represented in RFC3339 form and is in UTC.+optional", "zh_CN": "任务开始时间"}
        self.start_time = start_time
        # {"en": "The rate of pulling tasks which reached phase Succeeded without not ready nodes. +optional", "zh_CN": "完成成功率"}
        self.succeeded_rate = succeeded_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time
        if self.message is not None:
            result['message'] = self.message
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.succeeded_rate is not None:
            result['succeededRate'] = self.succeeded_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('succeededRate') is not None:
            self.succeeded_rate = m.get('succeededRate')
        return self


class CreateImagePullJobImagePullJob(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateImagePullJobObjectMeta = None,
        spec: CreateImagePullJobImagePullJobSpec = None,
        status: CreateImagePullJobImagePullJobStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Specification of the desired behavior of the CreateImagePullJobImagePullJob.", "zh_CN":"CreateImagePullJobImagePullJob 预期行为的规约。"}
        self.spec = spec
        # {"en":"Most recently observed status of the CreateImagePullJobImagePullJob.", "zh_CN":"最近观测到的 CreateImagePullJobImagePullJob 状态。"}
        self.status = status

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        if self.spec:
            self.spec.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateImagePullJobObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateImagePullJobImagePullJobSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = CreateImagePullJobImagePullJobStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class CreateImagePullJobResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateImagePullJobImagePullJob = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"imagepulljob object", "zh_CN":"imagepulljob对象"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = CreateImagePullJobImagePullJob()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateImagePullJobPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class CreateImagePullJobParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateImagePullJobRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateImagePullJobResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateHarborProjectAssignRole(TeaModel):
    def __init__(
        self,
        name: str = None,
        role: int = None,
    ):
        # {"en":"user name", "zh_CN":"用户名称"}
        self.name = name
        # {"en":"1: admin, 2: edit, 3: access", "zh_CN":"1: 管理,2: 编辑, 3：访问"}
        self.role = role

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.role, 'role')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class UpdateHarborProjectRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        pub: bool = None,
        describe: str = None,
        assign_roles: List[UpdateHarborProjectAssignRole] = None,
    ):
        # {"en":"project name", "zh_CN":"项目名称"}
        self.name = name
        # {"en":"false: private, true: public", "zh_CN":"false: 私有,true:公开"}
        self.pub = pub
        # {"en":"project describe", "zh_CN":"项目描述"}
        self.describe = describe
        # {"en":"authorized user", "zh_CN":"授权用户"}
        self.assign_roles = assign_roles

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.pub, 'pub')
        if self.assign_roles:
            for k in self.assign_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.pub is not None:
            result['pub'] = self.pub
        if self.describe is not None:
            result['describe'] = self.describe
        if self.assign_roles is not None:
            result['assignRoles'] = []
            for k in self.assign_roles:
                result['assignRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pub') is not None:
            self.pub = m.get('pub')
        if m.get('describe') is not None:
            self.describe = m.get('describe')
        if m.get('assignRoles') is not None:
            self.assign_roles = []
            for k in m.get('assignRoles'):
                temp_model = UpdateHarborProjectAssignRole()
                self.assign_roles.append(temp_model.from_map(k))
        return self


class UpdateHarborProjectResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: int = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"none", "zh_CN":"无"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateHarborProjectPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHarborProjectParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHarborProjectRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHarborProjectResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetHarborUserRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborUserUser(TeaModel):
    def __init__(
        self,
        id: int = None,
        username: str = None,
        create_time: int = None,
        update_time: int = None,
    ):
        # {"en":"user id", "zh_CN":"用户id"}
        self.id = id
        # {"en":"user name", "zh_CN":"用户名"}
        self.username = username
        # {"en":"createTime", "zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"updateTime", "zh_CN":"更新时间"}
        self.update_time = update_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.username, 'username')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.username is not None:
            result['username'] = self.username
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetHarborUserResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetHarborUserUser = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"user detail", "zh_CN":"用户详情"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            temp_model = GetHarborUserUser()
            self.data = temp_model.from_map(m['data'])
        return self


class GetHarborUserPaths(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # {"en":"user name", "zh_CN":"用户名"}
        self.name = name

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetHarborUserParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborUserRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHarborUserResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




