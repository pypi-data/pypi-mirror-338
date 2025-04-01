# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteSecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecretStatusDetails(TeaModel):
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


class DeleteSecretStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteSecretStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteSecretStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
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
            temp_model = DeleteSecretStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteSecretStatus = None,
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
            temp_model = DeleteSecretStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteSecretPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"secret name", "zh_CN":"secret 名称"}
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


class DeleteSecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateConfigmapOwnerReference(TeaModel):
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


class CreateConfigmapFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateConfigmapManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateConfigmapFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateConfigmapManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateConfigmapFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateConfigmapFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateConfigmapFieldsV1 holds the first JSON version format as described in the 'CreateConfigmapFieldsV1' type", "zh_CN":"CreateConfigmapFieldsV1 包含类型 “CreateConfigmapFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = CreateConfigmapFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateConfigmapObjectMeta(TeaModel):
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
        owner_references: List[CreateConfigmapOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateConfigmapManagedFieldsEntry] = None,
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
                temp_model = CreateConfigmapOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateConfigmapManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateConfigmapRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the CreateConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 CreateConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class CreateConfigmapConfigMap(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the CreateConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 CreateConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class CreateConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateConfigmapConfigMap = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"configmap object", "zh_CN":"configmap对象"}
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
            temp_model = CreateConfigmapConfigMap()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateConfigmapPaths(TeaModel):
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


class CreateConfigmapParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateSecretOwnerReference(TeaModel):
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


class CreateSecretFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSecretManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateSecretFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateSecretManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateSecretFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateSecretFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateSecretFieldsV1 holds the first JSON version format as described in the 'CreateSecretFieldsV1' type", "zh_CN":"CreateSecretFieldsV1 包含类型 “CreateSecretFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = CreateSecretFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateSecretObjectMeta(TeaModel):
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
        owner_references: List[CreateSecretOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateSecretManagedFieldsEntry] = None,
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
                temp_model = CreateSecretOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateSecretManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateSecretRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the CreateSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 CreateSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSecretSecret(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the CreateSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 CreateSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = CreateSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateSecretSecret = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"secret object", "zh_CN":"secret对象"}
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
            temp_model = CreateSecretSecret()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateSecretPaths(TeaModel):
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


class CreateSecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteConfigmapRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteConfigmapStatusDetails(TeaModel):
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


class DeleteConfigmapStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteConfigmapStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteConfigmapStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
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
            temp_model = DeleteConfigmapStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteConfigmapStatus = None,
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
            temp_model = DeleteConfigmapStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteConfigmapPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"configmap name", "zh_CN":"configmap 名称"}
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


class DeleteConfigmapParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetTokenRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTokenResponse(TeaModel):
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
        # {"en":"token", "zh_CN":"token"}
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


class GetTokenPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTokenParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTokenRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetTokenResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetConfigmapRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetConfigmapOwnerReference(TeaModel):
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


class GetConfigmapFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetConfigmapManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetConfigmapFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetConfigmapManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetConfigmapFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetConfigmapFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetConfigmapFieldsV1 holds the first JSON version format as described in the 'GetConfigmapFieldsV1' type", "zh_CN":"GetConfigmapFieldsV1 包含类型 “GetConfigmapFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = GetConfigmapFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetConfigmapObjectMeta(TeaModel):
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
        owner_references: List[GetConfigmapOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetConfigmapManagedFieldsEntry] = None,
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
                temp_model = GetConfigmapOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetConfigmapManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetConfigmapConfigMap(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the GetConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 GetConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class GetConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetConfigmapConfigMap = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"configmap", "zh_CN":"configmap"}
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
            temp_model = GetConfigmapConfigMap()
            self.data = temp_model.from_map(m['data'])
        return self


class GetConfigmapPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"configmap name", "zh_CN":"configmap 名称"}
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


class GetConfigmapParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListConfigmapRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListConfigmapListMeta(TeaModel):
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


class ListConfigmapOwnerReference(TeaModel):
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


class ListConfigmapFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListConfigmapManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListConfigmapFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListConfigmapManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListConfigmapFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListConfigmapFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListConfigmapFieldsV1 holds the first JSON version format as described in the 'ListConfigmapFieldsV1' type", "zh_CN":"ListConfigmapFieldsV1 包含类型 “ListConfigmapFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = ListConfigmapFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListConfigmapObjectMeta(TeaModel):
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
        owner_references: List[ListConfigmapOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListConfigmapManagedFieldsEntry] = None,
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
                temp_model = ListConfigmapOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListConfigmapManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListConfigmapConfigMap(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the ListConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 ListConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class ListConfigmapConfigMapList(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListConfigmapListMeta = None,
        items: List[ListConfigmapConfigMap] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListConfigmapConfigMap", "zh_CN":"ListConfigmapConfigMap 列表"}
        self.items = items

    def validate(self):
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
            temp_model = ListConfigmapListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListConfigmapConfigMap()
                self.items.append(temp_model.from_map(k))
        return self


class ListConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListConfigmapConfigMapList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"configmap list", "zh_CN":"configmap列表"}
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
            temp_model = ListConfigmapConfigMapList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListConfigmapPaths(TeaModel):
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


class ListConfigmapParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"The name of configmap", "zh_CN":"configmap 名称"}
        self.name = name
        # {"en":"labelSelector", "zh_CN":"labelSelector"}
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListSecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSecretListMeta(TeaModel):
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


class ListSecretOwnerReference(TeaModel):
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


class ListSecretFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSecretManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListSecretFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListSecretManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListSecretFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListSecretFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListSecretFieldsV1 holds the first JSON version format as described in the 'ListSecretFieldsV1' type", "zh_CN":"ListSecretFieldsV1 包含类型 “ListSecretFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = ListSecretFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListSecretObjectMeta(TeaModel):
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
        owner_references: List[ListSecretOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListSecretManagedFieldsEntry] = None,
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
                temp_model = ListSecretOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListSecretManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListSecretSecret(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the ListSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 ListSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = ListSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSecretSecretList(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: ListSecretListMeta = None,
        items: List[ListSecretSecret] = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListSecretSecret", "zh_CN":"ListSecretSecret 列表"}
        self.items = items

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
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
        if self.kind is not None:
            result['kind'] = self.kind
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()
        if self.items is not None:
            result['items'] = []
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = ListSecretListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListSecretSecret()
                self.items.append(temp_model.from_map(k))
        return self


class ListSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListSecretSecretList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"secret list", "zh_CN":"secret 列表"}
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
            temp_model = ListSecretSecretList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListSecretPaths(TeaModel):
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


class ListSecretParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"secret name", "zh_CN":"secret 名称"}
        self.name = name
        # {"en":"labelSelector", "zh_CN":"labelSelector"}
        self.label_selector = label_selector

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            self.label_selector = m.get('labelSelector')
        return self


class ListSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateSecretOwnerReference(TeaModel):
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


class UpdateSecretFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSecretManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateSecretFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateSecretManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateSecretFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateSecretFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateSecretFieldsV1 holds the first JSON version format as described in the 'UpdateSecretFieldsV1' type", "zh_CN":"UpdateSecretFieldsV1 包含类型 “UpdateSecretFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = UpdateSecretFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateSecretObjectMeta(TeaModel):
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
        owner_references: List[UpdateSecretOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateSecretManagedFieldsEntry] = None,
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
                temp_model = UpdateSecretOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateSecretManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateSecretRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the UpdateSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 UpdateSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateSecretSecret(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the UpdateSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 UpdateSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateSecretSecret = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"secret", "zh_CN":"secret"}
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
            temp_model = UpdateSecretSecret()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateSecretPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"secret name", "zh_CN":"secret 名称"}
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


class UpdateSecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutPatchSecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchSecretOwnerReference(TeaModel):
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


class PutPatchSecretFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchSecretManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutPatchSecretFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutPatchSecretManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutPatchSecretFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutPatchSecretFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutPatchSecretFieldsV1 holds the first JSON version format as described in the 'PutPatchSecretFieldsV1' type", "zh_CN":"PutPatchSecretFieldsV1 包含类型 “PutPatchSecretFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = PutPatchSecretFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutPatchSecretObjectMeta(TeaModel):
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
        owner_references: List[PutPatchSecretOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutPatchSecretManagedFieldsEntry] = None,
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
                temp_model = PutPatchSecretOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutPatchSecretManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutPatchSecretSecret(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutPatchSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the PutPatchSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 PutPatchSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PutPatchSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PutPatchSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutPatchSecretSecret = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"secret", "zh_CN":"secret"}
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
            temp_model = PutPatchSecretSecret()
            self.data = temp_model.from_map(m['data'])
        return self


class PutPatchSecretPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"secret name", "zh_CN":"secret 名称"}
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


class PutPatchSecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutPatchConfigmapRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchConfigmapOwnerReference(TeaModel):
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


class PutPatchConfigmapFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchConfigmapManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutPatchConfigmapFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutPatchConfigmapManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutPatchConfigmapFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutPatchConfigmapFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutPatchConfigmapFieldsV1 holds the first JSON version format as described in the 'PutPatchConfigmapFieldsV1' type", "zh_CN":"PutPatchConfigmapFieldsV1 包含类型 “PutPatchConfigmapFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = PutPatchConfigmapFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutPatchConfigmapObjectMeta(TeaModel):
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
        owner_references: List[PutPatchConfigmapOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutPatchConfigmapManagedFieldsEntry] = None,
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
                temp_model = PutPatchConfigmapOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutPatchConfigmapManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutPatchConfigmapConfigMap(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutPatchConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the PutPatchConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 PutPatchConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = PutPatchConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class PutPatchConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutPatchConfigmapConfigMap = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"configmap", "zh_CN":"configmap"}
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
            temp_model = PutPatchConfigmapConfigMap()
            self.data = temp_model.from_map(m['data'])
        return self


class PutPatchConfigmapPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"configmap name", "zh_CN":"configmap 名称"}
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


class PutPatchConfigmapParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateConfigmapOwnerReference(TeaModel):
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


class UpdateConfigmapFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateConfigmapManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateConfigmapFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateConfigmapManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateConfigmapFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateConfigmapFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateConfigmapFieldsV1 holds the first JSON version format as described in the 'UpdateConfigmapFieldsV1' type", "zh_CN":"UpdateConfigmapFieldsV1 包含类型 “UpdateConfigmapFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = UpdateConfigmapFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateConfigmapObjectMeta(TeaModel):
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
        owner_references: List[UpdateConfigmapOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateConfigmapManagedFieldsEntry] = None,
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
                temp_model = UpdateConfigmapOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateConfigmapManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateConfigmapRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the UpdateConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 UpdateConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class UpdateConfigmapConfigMap(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateConfigmapObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        binary_data: Dict[str, str] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the UpdateConfigmapConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"binaryData 包含二进制数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 binaryData 可以包含不在 UTF-8 范围中的字节序列。 binaryData 中存储的键不得与 data 字段中的键重叠，这在验证过程中是强制要求。 使用此字段需要 apiserver 和 kubelet 的版本高于 1.10"}
        self.immutable = immutable
        # {"en":"Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process", "zh_CN":"data 包含配置数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 如果值包含非 UTF-8 字节序列，则必须使用 binaryData 字段。 data 中存储的键不得与 binaryData 字段中的键重叠，这在验证过程中是强制要求"}
        self.data = data
        # {"en":"BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet", "zh_CN":"如果 immutable 设为 true， 则确保不会更新 UpdateConfigmapConfigMap 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.binary_data = binary_data

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.binary_data is not None:
            result['binaryData'] = self.binary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = UpdateConfigmapObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('binaryData') is not None:
            self.binary_data = m.get('binaryData')
        return self


class UpdateConfigmapResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateConfigmapConfigMap = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"configmap", "zh_CN":"configmap"}
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
            temp_model = UpdateConfigmapConfigMap()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateConfigmapPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"configmap name", "zh_CN":"configmap 名称"}
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


class UpdateConfigmapParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateConfigmapRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateConfigmapResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetSecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSecretOwnerReference(TeaModel):
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


class GetSecretFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSecretManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetSecretFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetSecretManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetSecretFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetSecretFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetSecretFieldsV1 holds the first JSON version format as described in the 'GetSecretFieldsV1' type", "zh_CN":"GetSecretFieldsV1 包含类型 “GetSecretFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = GetSecretFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetSecretObjectMeta(TeaModel):
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
        owner_references: List[GetSecretOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetSecretManagedFieldsEntry] = None,
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
                temp_model = GetSecretOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetSecretManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetSecretSecret(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetSecretObjectMeta = None,
        immutable: bool = None,
        data: Dict[str, str] = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"Immutable, if set to true, ensures that data stored in the GetSecretSecret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil", "zh_CN":"如果 immutable 设为 true，则确保不会更新 GetSecretSecret 中存储的数据（只能修改对象元数据）。 如果未设为 true，则可以随时修改此字段。 默认为 nil"}
        self.immutable = immutable
        # {"en":"Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here", "zh_CN":"data 包含秘密数据。 每个键必须由字母、数字、“-”、“_” 或 “.” 组成。 秘密数据的序列化格式是 base64 编码的字符串，表示此处的任意（可能是非字符串）数据值"}
        self.data = data
        # {"en":"stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API", "zh_CN":"stringData 允许指定字符串格式的非二进制秘密数据。 为了方便起见，它作为只写输入字段提供。 写入时将所有键和值合并到 data 字段，且覆盖任何现有的值。 从 API 读取时绝不会输出 stringData 字段"}
        self.string_data = string_data
        # {"en":"Used to facilitate programmatic handling of secret data", "zh_CN":"用于满足程序化方式处理秘密数据"}
        self.type = type

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()

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
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.data is not None:
            result['data'] = self.data
        if self.string_data is not None:
            result['stringData'] = self.string_data
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('metadata') is not None:
            temp_model = GetSecretObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('stringData') is not None:
            self.string_data = m.get('stringData')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSecretResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetSecretSecret = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"secret", "zh_CN":"secret"}
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
            temp_model = GetSecretSecret()
            self.data = temp_model.from_map(m['data'])
        return self


class GetSecretPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"secret name", "zh_CN":"secret 名称"}
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


class GetSecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




